const http = require('node:http');
const { randomUUID } = require('node:crypto');
const { URL } = require('node:url');

const { McpServer } = require('@modelcontextprotocol/sdk/server/mcp.js');
const { StreamableHTTPServerTransport } = require('@modelcontextprotocol/sdk/server/streamableHttp.js');
const { isInitializeRequest } = require('@modelcontextprotocol/sdk/types.js');

const { registerTools } = require('./tools');
const { supabase } = require('./supabaseClient');
const { createTokenVerifier, AuthenticationError } = require('./auth');
const { createUsageLogger } = require('./usageLogger');
const { baseLogger } = require('./logger');

const serverInfo = {
  name: 'feature-grounding-mcp',
  version: '0.2.0',
  description: 'Grounding data lookup server for UI automation agents.',
};

const INSTRUCTIONS =
  'Use the provided tools to query feature grounding data by surface, feature key, or description.';
const HEALTH_RESOURCE_URI = 'mcp://feature-grounding/health';
const MAX_REQUEST_BYTES = Number(process.env.MCP_MAX_REQUEST_BYTES ?? 4 * 1024 * 1024);
const PORT = Number(process.env.MCP_SERVER_PORT ?? process.env.PORT ?? 3333);
const HOST = process.env.MCP_SERVER_HOST ?? '0.0.0.0';
const RESOURCE_METADATA_URL = process.env.MCP_RESOURCE_METADATA_URL;
const ALLOWED_ORIGINS = (process.env.MCP_ALLOWED_ORIGINS ?? '')
  .split(',')
  .map((origin) => origin.trim())
  .filter(Boolean);

const tokenCacheTtlMs = process.env.MCP_TOKEN_CACHE_TTL_MS
  ? Number(process.env.MCP_TOKEN_CACHE_TTL_MS)
  : undefined;

const RATE_LIMIT_WINDOW_MS = Number(process.env.MCP_RATE_LIMIT_WINDOW_MS ?? 60_000);
const RATE_LIMIT_MAX = Number(process.env.MCP_RATE_LIMIT_MAX ?? 120);

const tokenVerifier = createTokenVerifier({
  supabase,
  cacheTtlMs: tokenCacheTtlMs,
  logger: baseLogger.child({ component: 'tokenVerifier' }),
});
const usageLogger = createUsageLogger({ supabase, logger: baseLogger.child({ component: 'usageLogger' }) });

const sessions = new Map();
const httpServer = http.createServer(handleHttpRequest);
const rateLimiter = new Map();

function checkRateLimit(tokenId) {
  if (!RATE_LIMIT_MAX || RATE_LIMIT_MAX <= 0) {
    return true;
  }
  const now = Date.now();
  const entry = rateLimiter.get(tokenId) ?? { count: 0, resetAt: now + RATE_LIMIT_WINDOW_MS };
  if (now >= entry.resetAt) {
    entry.count = 0;
    entry.resetAt = now + RATE_LIMIT_WINDOW_MS;
  }
  entry.count += 1;
  rateLimiter.set(tokenId, entry);
  return entry.count <= RATE_LIMIT_MAX;
}

function createMcpServer() {
  const server = new McpServer(serverInfo, {
    capabilities: {
      tools: {},
      logging: {},
    },
    instructions: INSTRUCTIONS,
  });

  registerTools(server, { usageLogger });

  server.resource('health', HEALTH_RESOURCE_URI, async () => ({
    contents: [
      {
        type: 'text',
        text: 'feature-grounding-mcp OK',
        uri: HEALTH_RESOURCE_URI,
      },
    ],
  }));

  return server;
}

function applyCors(req, res) {
  const origin = req.headers.origin;
  if (ALLOWED_ORIGINS.length === 0) {
    if (origin) {
      res.setHeader('Access-Control-Allow-Origin', origin);
    } else {
      res.setHeader('Access-Control-Allow-Origin', '*');
    }
  } else if (origin && ALLOWED_ORIGINS.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type, Mcp-Session-Id, Mcp-Protocol-Version');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Expose-Headers', 'Mcp-Session-Id');
}

function sendJson(res, status, payload, extraHeaders = {}) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json');
  for (const [key, value] of Object.entries(extraHeaders)) {
    if (value !== undefined) {
      res.setHeader(key, value);
    }
  }
  res.end(JSON.stringify(payload));
}

function createAuthenticateHeader({ code, message }) {
  const params = [`error="${code}"`, `error_description="${message.replace(/"/g, '\\"')}"`];
  if (RESOURCE_METADATA_URL) {
    params.push(`resource_metadata="${RESOURCE_METADATA_URL}"`);
  }
  return `Bearer ${params.join(', ')}`;
}

function getSessionId(req) {
  const raw = req.headers['mcp-session-id'];
  if (Array.isArray(raw)) {
    return raw[raw.length - 1];
  }
  return raw;
}

async function authenticateRequest(req, res) {
  try {
    const authInfo = await tokenVerifier.verify({ authorizationHeader: req.headers.authorization });
    req.auth = authInfo;
    return authInfo;
  } catch (error) {
    if (error instanceof AuthenticationError) {
      const header = createAuthenticateHeader({ code: error.code, message: error.message });
      sendJson(res, error.status, { error: error.code, message: error.message }, {
        'WWW-Authenticate': header,
      });
      return undefined;
    }
    sendJson(res, 500, { error: 'server_error', message: 'Authentication failed unexpectedly.' });
    return undefined;
  }
}

async function readJsonBody(req) {
  const chunks = [];
  let total = 0;
  for await (const chunk of req) {
    const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
    total += buffer.length;
    if (total > MAX_REQUEST_BYTES) {
      const error = new Error('Payload too large.');
      error.status = 413;
      error.code = 'payload_too_large';
      throw error;
    }
    chunks.push(buffer);
  }

  if (chunks.length === 0) {
    const error = new Error('Request body must not be empty.');
    error.status = 400;
    error.code = 'invalid_request';
    throw error;
  }

  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  } catch (parseError) {
    const error = new Error('Invalid JSON payload.');
    error.status = 400;
    error.code = 'invalid_json';
    throw error;
  }
}

function containsInitializationMessage(json) {
  const messages = Array.isArray(json) ? json : [json];
  return messages.some((message) => {
    try {
      return isInitializeRequest(message);
    } catch (_error) {
      return false;
    }
  });
}

async function handleHttpRequest(req, res) {
  const requestStart = Date.now();
  const requestId = randomUUID();
  let responded = false;

  applyCors(req, res);

  if (ALLOWED_ORIGINS.length > 0) {
    const origin = req.headers.origin;
    if (origin && !ALLOWED_ORIGINS.includes(origin)) {
      sendJson(res, 403, { error: 'forbidden', message: 'Origin is not allowed.' });
      baseLogger.warn('request.rejected_origin', { requestId, origin, path: req.url });
      return;
    }
  }

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    baseLogger.debug('request.options', { requestId, path: req.url });
    return;
  }

  const hostHeader = req.headers.host ?? 'localhost';
  const requestUrl = new URL(req.url ?? '/', `http://${hostHeader}`);
  const requestLogger = baseLogger.child({ requestId, method: req.method, path: requestUrl.pathname });

  const respond = (status, payload, headers = {}, extra = {}) => {
    if (!res.writableEnded) {
      sendJson(res, status, payload, headers);
    }
    responded = true;
    requestLogger.info('request.finish', {
      status,
      durationMs: Date.now() - requestStart,
      ...extra,
    });
  };

  requestLogger.info('request.start', {
    origin: req.headers.origin ?? null,
    sessionId: getSessionId(req) ?? null,
  });

  if (requestUrl.pathname === '/health' && req.method === 'GET') {
    respond(200, {
      status: 'ok',
      uptimeSeconds: Math.round(process.uptime()),
      activeSessions: sessions.size,
    });
    return;
  }

  if (requestUrl.pathname !== '/mcp') {
    respond(404, { error: 'not_found', message: 'Unknown path.' });
    return;
  }

  const authInfo = await authenticateRequest(req, res);
  if (!authInfo) {
    requestLogger.warn('request.auth_failed', { durationMs: Date.now() - requestStart });
    return;
  }
  requestLogger.debug('request.authenticated', { developerId: authInfo.developerId, tokenId: authInfo.tokenId });

  if (!checkRateLimit(authInfo.tokenId)) {
    respond(429, { error: 'rate_limited', message: 'Too many requests for this token. Try again shortly.' }, {}, {
      developerId: authInfo.developerId,
      tokenId: authInfo.tokenId,
    });
    return;
  }

  if (req.method === 'POST') {
    let parsedBody;
    try {
      parsedBody = await readJsonBody(req);
    } catch (error) {
      const status = error.status ?? 400;
      respond(status, { error: error.code ?? 'invalid_request', message: error.message });
      return;
    }

    const sessionId = getSessionId(req);
    if (sessionId) {
      const session = sessions.get(sessionId);
      if (!session) {
        respond(404, { error: 'session_not_found', message: 'Unknown session ID.' });
        return;
      }
      if (session.tokenId !== authInfo.tokenId) {
        respond(403, { error: 'invalid_token', message: 'Session token mismatch.' });
        return;
      }
      try {
        await session.transport.handleRequest(req, res, parsedBody);
        requestLogger.info('request.session_continue', { sessionId, durationMs: Date.now() - requestStart });
      } catch (error) {
        requestLogger.error('request.session_error', { error: error.message, stack: error.stack });
        if (!res.headersSent) {
          respond(500, { error: 'server_error', message: 'Failed to process request.' });
        }
      }
      return;
    }

    if (!containsInitializationMessage(parsedBody)) {
      respond(400, {
        error: 'invalid_request',
        message: 'Initialization request must be the first call without an MCP session.',
      });
      return;
    }

    const mcpServer = createMcpServer();
    let serverClosed = false;
    const closeServer = async () => {
      if (serverClosed) {
        return;
      }
      serverClosed = true;
      try {
        await mcpServer.close();
      } catch (error) {
        console.warn('[feature-grounding-mcp] failed to close MCP server', error);
      }
    };

    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        sessions.set(sessionId, {
          transport,
          server: mcpServer,
          tokenId: authInfo.tokenId,
          closeServer,
        });
        requestLogger.info('session.initialized', { sessionId, developerId: authInfo.developerId });
      },
      onsessionclosed: async (sessionId) => {
        sessions.delete(sessionId);
        await closeServer();
        requestLogger.info('session.closed', { sessionId });
      },
    });

    transport.onclose = () => {
      const activeSessionId = transport.sessionId;
      if (activeSessionId) {
        sessions.delete(activeSessionId);
      }
      void closeServer();
    };

    try {
      await mcpServer.connect(transport);
      await transport.handleRequest(req, res, parsedBody);
      requestLogger.info('request.initialized', { durationMs: Date.now() - requestStart });
    } catch (error) {
      await closeServer();
      requestLogger.error('request.init_error', { error: error.message, stack: error.stack });
      if (!res.headersSent) {
        respond(500, { error: 'server_error', message: 'Failed to initialize MCP session.' });
      }
    }
    return;
  }

  const sessionId = getSessionId(req);
  if (!sessionId) {
    sendJson(res, 400, {
      error: 'invalid_request',
      message: 'Mcp-Session-Id header is required after initialization.',
    });
    return;
  }

  const session = sessions.get(sessionId);
  if (!session) {
    respond(404, { error: 'session_not_found', message: 'Unknown session ID.' });
    return;
  }

  if (session.tokenId !== authInfo.tokenId) {
    respond(403, { error: 'invalid_token', message: 'Session token mismatch.' });
    return;
  }

  if (req.method === 'GET') {
    try {
      await session.transport.handleRequest(req, res);
      requestLogger.debug('request.sse_continue', { sessionId, durationMs: Date.now() - requestStart });
    } catch (error) {
      requestLogger.error('request.sse_error', { error: error.message, stack: error.stack });
      if (!res.headersSent) {
        respond(500, { error: 'server_error', message: 'Failed to process request.' });
      }
    }
    return;
  }

  if (req.method === 'DELETE') {
    try {
      await session.transport.handleRequest(req, res);
      requestLogger.info('session.terminated', { sessionId, durationMs: Date.now() - requestStart });
    } catch (error) {
      requestLogger.error('session.termination_error', { error: error.message, stack: error.stack });
      if (!res.headersSent) {
        respond(500, { error: 'server_error', message: 'Failed to terminate session.' });
      }
    } finally {
      sessions.delete(sessionId);
      await session.closeServer();
    }
    return;
  }

  respond(405, { error: 'method_not_allowed', message: 'Unsupported HTTP method.' });
}

httpServer.listen(PORT, HOST, () => {
  baseLogger.info('server.started', { host: HOST, port: PORT });
});

async function shutdown() {
  baseLogger.warn('server.shutdown_start');
  httpServer.close();
  const closePromises = [];
  for (const [sessionId, session] of sessions.entries()) {
    sessions.delete(sessionId);
    closePromises.push(
      (async () => {
        try {
          await session.transport.close();
        } catch (error) {
          baseLogger.warn('server.transport_close_failed', { sessionId, error: error.message });
        }
        try {
          await session.closeServer();
        } catch (error) {
          baseLogger.warn('server.close_failed', { sessionId, error: error.message });
        }
      })()
    );
  }
  await Promise.all(closePromises);
  process.exit(0);
}

process.on('SIGINT', () => {
  shutdown().catch((error) => {
    baseLogger.error('server.shutdown_error', { error: error.message, stack: error.stack });
    process.exit(1);
  });
});

module.exports = {
  createMcpServer,
  httpServer,
};

const crypto = require('node:crypto');

const BEARER_PREFIX = 'bearer ';
const DEFAULT_CACHE_TTL_MS = 60 * 1000;
const DEFAULT_LAST_USED_UPDATE_INTERVAL_MS = 60 * 1000;

class AuthenticationError extends Error {
  constructor(message, { status = 401, code = 'invalid_token' } = {}) {
    super(message);
    this.name = 'AuthenticationError';
    this.status = status;
    this.code = code;
  }
}

function timingSafeEqualHex(a, b) {
  const aBuffer = Buffer.from(a, 'hex');
  const bBuffer = Buffer.from(b, 'hex');

  if (aBuffer.length !== bBuffer.length) {
    return false;
  }

  return crypto.timingSafeEqual(aBuffer, bBuffer);
}

function sha256Hex(value) {
  return crypto.createHash('sha256').update(value).digest('hex');
}

function buildCache({ ttlMs }) {
  const entries = new Map();

  function get(key) {
    const entry = entries.get(key);
    if (!entry) {
      return undefined;
    }
    if (entry.expiresAt <= Date.now()) {
      entries.delete(key);
      return undefined;
    }
    return entry.value;
  }

  function set(key, value) {
    entries.set(key, { value, expiresAt: Date.now() + ttlMs });
  }

  function deleteKey(key) {
    entries.delete(key);
  }

  function clear() {
    entries.clear();
  }

  return { get, set, delete: deleteKey, clear };
}

function parseAuthorizationHeader(header) {
  if (!header || typeof header !== 'string') {
    throw new AuthenticationError('Missing Authorization header.');
  }

  const lower = header.toLowerCase();
  if (!lower.startsWith(BEARER_PREFIX)) {
    throw new AuthenticationError("Authorization header must use the 'Bearer' scheme.");
  }

  const token = header.slice(BEARER_PREFIX.length).trim();
  if (!token) {
    throw new AuthenticationError('Missing bearer token after scheme.');
  }

  return token;
}

function splitToken(token) {
  const parts = token.split('.');
  if (parts.length !== 2 || !parts[0] || !parts[1]) {
    throw new AuthenticationError('Invalid token format.', { code: 'invalid_token' });
  }

  return { prefix: parts[0], secret: parts[1] };
}

function createTokenVerifier({
  supabase,
  cacheTtlMs = DEFAULT_CACHE_TTL_MS,
  lastUsedUpdateIntervalMs = DEFAULT_LAST_USED_UPDATE_INTERVAL_MS,
  logger = console,
}) {
  if (!supabase) {
    throw new Error('Token verifier requires a Supabase client.');
  }

  const cache = buildCache({ ttlMs: cacheTtlMs });
  const lastUsedTracker = new Map();

  async function updateLastUsedAt(tokenId) {
    const previous = lastUsedTracker.get(tokenId) ?? 0;
    if (Date.now() - previous < lastUsedUpdateIntervalMs) {
      return;
    }

    lastUsedTracker.set(tokenId, Date.now());
    try {
      const { error } = await supabase
        .from('mcp_api_tokens')
        .update({ last_used_at: new Date().toISOString() })
        .eq('id', tokenId);

      if (error) {
        logger.warn('token.last_used_update_failed', { error: error.message, tokenId });
      }
    } catch (error) {
      logger.warn('token.last_used_update_failed', { error: error.message, tokenId });
    }
  }

  async function verify({ authorizationHeader }) {
    const rawToken = parseAuthorizationHeader(authorizationHeader);
    const { prefix, secret } = splitToken(rawToken);
    const fullToken = `${prefix}.${secret}`;
    const cacheKey = sha256Hex(fullToken);

    const cached = cache.get(cacheKey);
    if (cached) {
      void updateLastUsedAt(cached.tokenId);
      return cached;
    }

    const { data, error } = await supabase
      .from('mcp_api_tokens')
      .select(
        [
          'id',
          'developer_id',
          'agent_id',
          'token_prefix',
          'token_hash',
          'is_active',
          'expires_at',
          'revoked_at',
          'scopes',
          'metadata',
        ].join(', ')
      )
      .eq('token_prefix', prefix)
      .limit(5);

    if (error) {
      throw new AuthenticationError(`Authorization lookup failed: ${error.message}.`, {
        status: 500,
        code: 'server_error',
      });
    }

    if (!data || data.length === 0) {
      throw new AuthenticationError('Unknown API token.');
    }

    const matches = data.filter((row) => timingSafeEqualHex(row.token_hash ?? '', sha256Hex(fullToken)));
    if (!matches.length) {
      throw new AuthenticationError('Unknown API token.');
    }

    const tokenRow = matches[0];

    if (tokenRow.is_active === false || tokenRow.revoked_at) {
      throw new AuthenticationError('API token has been revoked.', { code: 'invalid_token' });
    }

    if (tokenRow.expires_at) {
      const expiresAt = new Date(tokenRow.expires_at).getTime();
      if (!Number.isNaN(expiresAt) && expiresAt <= Date.now()) {
        throw new AuthenticationError('API token has expired.', { code: 'invalid_token' });
      }
    }

    const authInfo = {
      tokenId: tokenRow.id,
      developerId: tokenRow.developer_id,
      agentId: tokenRow.agent_id ?? null,
      scopes: Array.isArray(tokenRow.scopes) ? tokenRow.scopes : [],
      metadata: tokenRow.metadata ?? null,
    };

    cache.set(cacheKey, authInfo);
    void updateLastUsedAt(tokenRow.id);
    return authInfo;
  }

  return {
    verify,
    AuthenticationError,
    clearCache: () => cache.clear(),
  };
}

module.exports = {
  AuthenticationError,
  createTokenVerifier,
};

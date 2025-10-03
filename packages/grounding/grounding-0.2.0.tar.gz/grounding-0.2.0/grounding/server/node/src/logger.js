const levels = { error: 0, warn: 1, info: 2, debug: 3 };
const levelNames = Object.keys(levels);

const envLevel = (process.env.MCP_LOG_LEVEL || 'info').toLowerCase();
const envFormat = (process.env.MCP_LOG_FORMAT || 'json').toLowerCase();
const currentLevel = levels[envLevel] ?? levels.info;

function createLogger(defaultFields = {}) {
  function log(level, message, fields = {}) {
    const levelValue = levels[level];
    if (levelValue === undefined || levelValue > currentLevel) {
      return;
    }
    const entry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      ...defaultFields,
      ...fields,
    };
    if (envFormat === 'json') {
      // eslint-disable-next-line no-console
      console.log(JSON.stringify(entry));
    } else {
      const extra = { ...entry };
      delete extra.timestamp;
      delete extra.level;
      delete extra.message;
      const extraText = Object.keys(extra).length ? ` ${JSON.stringify(extra)}` : '';
      // eslint-disable-next-line no-console
      console.log(`[${entry.timestamp}] [${level.toUpperCase()}] ${message}${extraText}`);
    }
  }

  return {
    log,
    error: (message, fields) => log('error', message, fields),
    warn: (message, fields) => log('warn', message, fields),
    info: (message, fields) => log('info', message, fields),
    debug: (message, fields) => log('debug', message, fields),
    child: (fields) => createLogger({ ...defaultFields, ...fields }),
  };
}

const baseLogger = createLogger({ service: 'feature-grounding-mcp' });

module.exports = {
  baseLogger,
  createLogger,
  levelNames,
};

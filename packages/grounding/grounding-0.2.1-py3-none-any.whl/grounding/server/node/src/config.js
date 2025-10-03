const path = require('path');
const fs = require('fs');
const dotenv = require('dotenv');

const explicitEnvPath = process.env.MCP_SERVER_ENV_PATH;
const defaultEnvPath = path.resolve(process.cwd(), '.env');

const candidatePaths = [explicitEnvPath, defaultEnvPath, path.resolve(process.cwd(), '..', '.env')].filter(
  (envPath, index, all) => envPath && all.indexOf(envPath) === index
);

for (const envPath of candidatePaths) {
  if (fs.existsSync(envPath)) {
    dotenv.config({ path: envPath });
  }
}

const OS_NAME_VALUES = ['Android', 'Linux', 'Windows', 'Windows-2022', 'iOS', 'macOS'];
const BROWSER_NAME_VALUES = ['Chrome', 'Desktop', 'Edge', 'Firefox', 'Other', 'Safari'];
const APPLICATION_TYPE_VALUES = [
  'desktop_application',
  'web_application',
  'desktop_application, web_application',
];

function getSupabaseConfig() {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY;

  if (!url) {
    throw new Error('Missing SUPABASE_URL environment variable.');
  }

  if (!key) {
    throw new Error('Missing Supabase API key. Set SUPABASE_SERVICE_ROLE_KEY or SUPABASE_ANON_KEY.');
  }

  return { url, key };
}

module.exports = {
  OS_NAME_VALUES,
  BROWSER_NAME_VALUES,
  APPLICATION_TYPE_VALUES,
  getSupabaseConfig,
};

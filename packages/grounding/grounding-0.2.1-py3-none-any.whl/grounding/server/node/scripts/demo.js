#!/usr/bin/env node
/*
 * Simple smoke test for the feature grounding MCP data access helpers.
 * Run with:
 *   node scripts/demo.js
 * Environment variables SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_ANON_KEY)
 * must be set before running.
 */

const path = require('path');
const dotenv = require('dotenv');

dotenv.config({ path: process.env.MCP_SERVER_ENV_PATH || path.resolve(process.cwd(), '..', '.env') });

const { listSurfaces, getFeature, findFeature } = require('../src/tools');

async function main() {
  console.log('Running feature grounding demo...');

  const surfaces = await listSurfaces({
    os: 'macOS',
    browser: 'Chrome',
    includeInactive: false,
  });
  console.log('\nSurfaces (macOS / Chrome):');
  console.dir(surfaces, { depth: null });

  const feature = await getFeature({
    featureKey: 'gmail.compose',
    os: 'macOS',
    browser: 'Chrome',
  });
  console.log('\nSingle feature lookup (gmail.compose):');
  console.dir(feature, { depth: null });

  const search = await findFeature({
    os: 'macOS',
    browser: 'Chrome',
    description: 'compose new email',
    limit: 5,
  });
  console.log('\nFind feature ("compose new email"):');
  console.dir(search, { depth: null });
}

main().catch((error) => {
  console.error('Demo failed:', error);
  process.exit(1);
});

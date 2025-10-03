const { createClient } = require('@supabase/supabase-js');
const { getSupabaseConfig } = require('./config');

const { url, key } = getSupabaseConfig();

const supabase = createClient(url, key, {
  auth: {
    persistSession: false,
  },
  global: {
    headers: {
      'x-client-info': 'feature-grounding-mcp/0.1.0',
    },
  },
});

function buildFeatureQuery({
  os,
  browser,
  surface,
  includeInactive = false,
  columns = '*',
} = {}) {
  let query = supabase.from('feature_data').select(columns);

  if (os) {
    query = query.eq('os_name', os);
  }

  if (browser) {
    query = query.eq('browser_name', browser);
  }

  if (surface) {
    query = query.eq('surface', surface);
  }

  if (!includeInactive) {
    query = query.eq('is_active', true);
  }

  return query;
}

function buildKeyboardShortcutQuery({
  applicationName,
  os,
  applicationType,
  columns = '*',
} = {}) {
  let query = supabase.from('keyboard_shortcuts').select(columns);

  if (applicationName) {
    query = query.eq('application_name', applicationName);
  }

  if (os) {
    query = query.eq('os_name', os);
  }

  if (applicationType && applicationType.includes(',')) {
    query = query.eq('application_type', applicationType);
  }

  return query;
}

function matchKeyboardShortcuts({
  applicationName,
  os,
  applicationType,
  action,
  limit,
}) {
  return supabase.rpc('match_keyboard_shortcuts', {
    p_application_name: applicationName ?? null,
    p_os_name: os ?? null,
    p_application_type: applicationType ?? null,
    p_action: action ?? null,
    p_limit: limit ?? null,
  });
}

module.exports = {
  supabase,
  buildFeatureQuery,
  buildKeyboardShortcutQuery,
  matchKeyboardShortcuts,
};

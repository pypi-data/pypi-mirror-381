const { buildFeatureQuery, buildKeyboardShortcutQuery, matchKeyboardShortcuts } = require('./supabaseClient');
const { mapFeatureRow } = require('./mappers');
const { scoreFeature, scoreKeyboardShortcut, escapeIlikePattern } = require('./scoring');
const {
  listSurfacesInputSchema,
  listSurfacesInputShape,
  listSurfacesResultSchema,
  listSurfacesResultShape,
  getFeatureInputSchema,
  getFeatureInputShape,
  getFeatureResultSchema,
  getFeatureResultShape,
  findFeatureInputSchema,
  findFeatureInputShape,
  findFeatureResultSchema,
  findFeatureResultShape,
  listShortcutsInputSchema,
  listShortcutsInputShape,
  listShortcutsResultSchema,
  listShortcutsResultShape,
  getShortcutInputSchema,
  getShortcutInputShape,
  getShortcutResultSchema,
  getShortcutResultShape,
  findShortcutInputSchema,
  findShortcutInputShape,
  findShortcutResultSchema,
  findShortcutResultShape,
} = require('./schema');

const MAX_SAMPLE_KEYS = 5;

async function listSurfaces(args) {
  const query = buildFeatureQuery({
    os: args.os,
    browser: args.browser,
    includeInactive: args.includeInactive,
    columns: 'surface, os_name, browser_name, feature_key, is_active',
  }).order('surface', { ascending: true });

  const { data, error } = await query;

  if (error) {
    throw new Error(`Supabase error: ${error.message}`);
  }

  const surfaceMap = new Map();

  for (const row of data ?? []) {
    const entry = surfaceMap.get(row.surface) || {
      surface: row.surface,
      osName: row.os_name,
      browserName: row.browser_name,
      totalFeatures: 0,
      activeFeatures: 0,
      sampleFeatureKeys: [],
    };

    entry.totalFeatures += 1;
    if (row.is_active) {
      entry.activeFeatures += 1;
    }
    if (entry.sampleFeatureKeys.length < MAX_SAMPLE_KEYS) {
      entry.sampleFeatureKeys.push(row.feature_key);
    }

    surfaceMap.set(row.surface, entry);
  }

  const surfaces = Array.from(surfaceMap.values()).sort((a, b) => a.surface.localeCompare(b.surface));

  return { surfaces };
}

async function getFeature(args) {
  let query = buildFeatureQuery({
    os: args.os,
    browser: args.browser,
    surface: args.surface,
    includeInactive: args.includeInactive,
  }).eq('feature_key', args.featureKey)
    .order('version', { ascending: false })
    .order('updated_at', { ascending: false });

  if (args.version != null) {
    query = query.eq('version', args.version);
  }

  const { data, error } = await query.limit(args.version != null ? 10 : 1);

  if (error) {
    throw new Error(`Supabase error: ${error.message}`);
  }

  const features = (data ?? []).map(mapFeatureRow);
  return {
    feature: features[0] ?? null,
    matchedCount: features.length,
  };
}

async function fetchCandidates(args, candidateLimit) {
  const baseParams = {
    os: args.os,
    browser: args.browser,
    surface: args.surface,
    includeInactive: args.includeInactive,
  };

  const candidates = new Map();

  async function run(modifier) {
    let query = buildFeatureQuery(baseParams)
      .order('updated_at', { ascending: false })
      .order('version', { ascending: false });

    if (modifier) {
      query = modifier(query);
    }

    const { data, error } = await query.limit(candidateLimit);

    if (error) {
      throw new Error(`Supabase error: ${error.message}`);
    }

    for (const row of data ?? []) {
      candidates.set(row.id, row);
    }
  }

  if (args.featureKey) {
    const pattern = `%${escapeIlikePattern(args.featureKey)}%`;
    await run((query) => query.ilike('feature_key', pattern));
  }

  if (args.featureText) {
    await run((query) => query.contains('feature_text_exact', [args.featureText]));
  }

  if (args.description) {
    const normalized = args.description.trim().replace(/\s+/g, ' ');
    const pattern = `%${escapeIlikePattern(normalized)}%`;
    await run((query) => query.ilike('description', pattern));
    await run((query) => query.ilike('ui_region_hint', pattern));
  }

  if (args.applicationName) {
    const pattern = `%${escapeIlikePattern(args.applicationName)}%`;
    await run((query) => query.ilike('application_name', pattern));
  }

  if (args.applicationPage) {
    const pattern = `%${escapeIlikePattern(args.applicationPage)}%`;
    await run((query) => query.ilike('application_page', pattern));
  }

  if (!candidates.size) {
    await run((query) => query);
  }

  return Array.from(candidates.values());
}

async function findFeature(args) {
  const candidateLimit = Math.max(args.limit * 4, 20);
  const candidateRows = await fetchCandidates(args, candidateLimit);

  const scored = candidateRows.map((row) => {
    const feature = mapFeatureRow(row);
    const { score, matchedFields } = scoreFeature(feature, args);
    return {
      ...feature,
      score: Number(score.toFixed(3)),
      matchedFields: matchedFields.length ? matchedFields : undefined,
    };
  });

  scored.sort((a, b) => {
    const scoreDiff = (b.score ?? 0) - (a.score ?? 0);
    if (Math.abs(scoreDiff) > 1e-3) {
      return scoreDiff;
    }
    return new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime();
  });

  const items = scored.slice(0, args.limit);

  return {
    items,
    limit: args.limit,
    returned: items.length,
  };
}

function mapShortcutRow(row) {
  return {
    id: row.id,
    applicationName: row.application_name,
    osName: row.os_name,
    applicationType: row.application_type,
    action: row.action,
    shortcut: row.shortcut,
    createdAt: row.created_at,
  };
}

async function listKeyboardShortcuts(args) {
  const limit = args.limit ?? 50;
  const { data, error } = await matchKeyboardShortcuts({
    applicationName: args.applicationName,
    os: args.os,
    applicationType: args.applicationType,
    action: args.action,
    limit,
  });

  if (error) {
    throw new Error(`Supabase error: ${error.message}`);
  }

  const shortcuts = (data ?? []).map(mapShortcutRow);

  return {
    shortcuts,
    count: shortcuts.length,
  };
}

async function getKeyboardShortcut(args) {
  let query = buildKeyboardShortcutQuery({
    applicationName: args.applicationName,
    os: args.os,
    applicationType: args.applicationType,
  }).ilike('action', args.action)
    .order('created_at', { ascending: false });

  const { data, error } = await query.limit(10);

  if (error) {
    throw new Error(`Supabase error: ${error.message}`);
  }

  const shortcuts = (data ?? []).map(mapShortcutRow);
  return {
    shortcut: shortcuts[0] ?? null,
    matchedCount: shortcuts.length,
  };
}

async function fetchShortcutCandidates(args, candidateLimit) {
  const baseParams = {
    applicationName: args.applicationName,
    os: args.os,
    applicationType: args.applicationType,
  };

  const candidates = new Map();

  async function run(modifier) {
    let query = buildKeyboardShortcutQuery(baseParams).order('created_at', { ascending: false });

    if (modifier) {
      query = modifier(query);
    }

    const { data, error } = await query.limit(candidateLimit);

    if (error) {
      throw new Error(`Supabase error: ${error.message}`);
    }

    for (const row of data ?? []) {
      candidates.set(row.id, row);
    }
  }

  if (args.action) {
    const pattern = `%${escapeIlikePattern(args.action)}%`;
    await run((query) => query.ilike('action', pattern));
  }

  if (args.shortcut) {
    const pattern = `%${escapeIlikePattern(args.shortcut)}%`;
    await run((query) => query.ilike('shortcut', pattern));
  }

  if (!candidates.size) {
    await run((query) => query);
  }

  return Array.from(candidates.values());
}

async function findKeyboardShortcut(args) {
  const candidateLimit = Math.max(args.limit * 4, 20);
  const candidateRows = await fetchShortcutCandidates(args, candidateLimit);

  const scored = candidateRows.map((row) => {
    const shortcut = mapShortcutRow(row);
    const { score, matchedFields } = scoreKeyboardShortcut(shortcut, args);
    return {
      ...shortcut,
      score: Number(score.toFixed(3)),
      matchedFields: matchedFields.length ? matchedFields : undefined,
    };
  });

  scored.sort((a, b) => {
    const scoreDiff = (b.score ?? 0) - (a.score ?? 0);
    if (Math.abs(scoreDiff) > 1e-3) {
      return scoreDiff;
    }
    return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
  });

  const items = scored.slice(0, args.limit);

  return {
    items,
    limit: args.limit,
    returned: items.length,
  };
}

function formatSurfacesSummary(result) {
  if (!result.surfaces.length) {
    return 'No surfaces found for the requested filters.';
  }

  const lines = result.surfaces.slice(0, 5).map((surface) => `• ${surface.surface} (${surface.activeFeatures}/${surface.totalFeatures} active)`);
  const moreCount = result.surfaces.length - lines.length;
  if (moreCount > 0) {
    lines.push(`…and ${moreCount} more surfaces.`);
  }
  return lines.join('\n');
}

function formatShortcutsSummary(result) {
  if (!result.shortcuts.length) {
    return 'No keyboard shortcuts found.';
  }

  const lines = result.shortcuts.slice(0, 5).map((shortcut) => {
    return `${shortcut.action}: ${shortcut.shortcut}`;
  });

  const remaining = result.shortcuts.length - lines.length;
  if (remaining > 0) {
    lines.push(`…and ${remaining} more shortcuts.`);
  }

  return lines.join('\n');
}

function formatFeatureSummary(result) {
  if (!result.feature) {
    return 'Feature not found.';
  }
  const feature = result.feature;
  return `Feature ${feature.featureKey} on ${feature.surface} (v${feature.version})`;
}

function formatFindSummary(result) {
  if (!result.items.length) {
    return 'No matching features found.';
  }
  const lines = result.items.map((item, index) => {
    const rank = index + 1;
    const score = item.score != null ? ` score=${item.score}` : '';
    return `${rank}. ${item.featureKey} on ${item.surface}${score}`;
  });
  return lines.join('\n');
}

function formatShortcutSummary(result) {
  if (!result.shortcut) {
    return 'Keyboard shortcut not found.';
  }
  return `${result.shortcut.action}: ${result.shortcut.shortcut}`;
}

function formatFindShortcutSummary(result) {
  if (!result.items.length) {
    return 'No matching keyboard shortcuts found.';
  }
  const lines = result.items.map((item, index) => {
    const rank = index + 1;
    const score = item.score != null ? ` score=${item.score}` : '';
    return `${rank}. ${item.action}: ${item.shortcut}${score}`;
  });
  return lines.join('\n');
}

function wrapSuccess(structuredContent, summary) {
  return {
    content: [
      {
        type: 'text',
        text: summary,
      },
    ],
    structuredContent,
  };
}

function wrapError(message) {
  return {
    isError: true,
    content: [
      {
        type: 'text',
        text: message,
      },
    ],
  };
}

function registerTools(server, options = {}) {
  const usageLogger = options.usageLogger;

  function startLog(toolName) {
    return {
      toolName,
      startedAt: new Date(),
      status: 'error',
      args: undefined,
      response: undefined,
      errorMessage: undefined,
    };
  }

  function finishLog(logContext, extra) {
    const authInfo = extra?.authInfo;
    if (!usageLogger || !authInfo) {
      return;
    }

    const durationMs = Date.now() - logContext.startedAt.getTime();

    usageLogger
      .logUsage({
        startedAt: logContext.startedAt.toISOString(),
        durationMs,
        tokenId: authInfo.tokenId,
        developerId: authInfo.developerId,
        agentId: authInfo.agentId,
        toolName: logContext.toolName,
        status: logContext.status,
        args: logContext.args,
        response: logContext.response,
        errorMessage: logContext.errorMessage,
      })
      .catch((error) => {
        console.warn('[feature-grounding-mcp] failed to log usage event', error);
      });
  }
  server.registerTool(
    'list_surfaces',
    {
      title: 'List Known UI Surfaces',
      description: 'List surfaces that have grounding data for the specified OS and browser.',
      inputSchema: listSurfacesInputShape,
      outputSchema: listSurfacesResultShape,
      annotations: {
        title: 'List surfaces with grounding data',
      },
    },
    async (args, extra) => {
      const logContext = startLog('list_surfaces');
      try {
        const parsedArgs = listSurfacesInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await listSurfaces(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatSurfacesSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`list_surfaces failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );

  server.registerTool(
    'get_feature',
    {
      title: 'Get Feature by Key',
      description: 'Fetch a specific feature grounding record by its feature key.',
      inputSchema: getFeatureInputShape,
      outputSchema: getFeatureResultShape,
      annotations: {
        title: 'Lookup a feature grounding entry',
        readOnlyHint: true,
        idempotentHint: true,
      },
    },
    async (args, extra) => {
      const logContext = startLog('get_feature');
      try {
        const parsedArgs = getFeatureInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await getFeature(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatFeatureSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`get_feature failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );

  server.registerTool(
    'find_feature',
    {
      title: 'Find Feature by Description',
      description: 'Search for features that match the supplied description, application context, surface, or text snippets.',
      inputSchema: findFeatureInputShape,
      outputSchema: findFeatureResultShape,
      annotations: {
        title: 'Search grounding data for matching features',
        readOnlyHint: true,
        idempotentHint: true,
        openWorldHint: false,
      },
    },
    async (args, extra) => {
      const logContext = startLog('find_feature');
      try {
        const parsedArgs = findFeatureInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await findFeature(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatFindSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`find_feature failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );

  server.registerTool(
    'list_keyboard_shortcuts',
    {
      title: 'List Keyboard Shortcuts',
      description: 'Retrieve keyboard shortcuts for a specific application and OS.',
      inputSchema: listShortcutsInputShape,
      outputSchema: listShortcutsResultShape,
      annotations: {
        title: 'Fetch official keyboard shortcuts',
        readOnlyHint: true,
        idempotentHint: true,
      },
    },
    async (args, extra) => {
      const logContext = startLog('list_keyboard_shortcuts');
      try {
        const parsedArgs = listShortcutsInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await listKeyboardShortcuts(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatShortcutsSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`list_keyboard_shortcuts failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );

  server.registerTool(
    'get_keyboard_shortcut',
    {
      title: 'Get Keyboard Shortcut',
      description: 'Fetch a specific keyboard shortcut by its action name for a given application and operating system.',
      inputSchema: getShortcutInputShape,
      outputSchema: getShortcutResultShape,
      annotations: {
        title: 'Lookup a keyboard shortcut by action',
        readOnlyHint: true,
        idempotentHint: true,
      },
    },
    async (args, extra) => {
      const logContext = startLog('get_keyboard_shortcut');
      try {
        const parsedArgs = getShortcutInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await getKeyboardShortcut(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatShortcutSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`get_keyboard_shortcut failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );

  server.registerTool(
    'find_keyboard_shortcut',
    {
      title: 'Find Keyboard Shortcut',
      description: 'Search for keyboard shortcuts that match the supplied action or shortcut key pattern.',
      inputSchema: findShortcutInputShape,
      outputSchema: findShortcutResultShape,
      annotations: {
        title: 'Search keyboard shortcuts',
        readOnlyHint: true,
        idempotentHint: true,
        openWorldHint: false,
      },
    },
    async (args, extra) => {
      const logContext = startLog('find_keyboard_shortcut');
      try {
        const parsedArgs = findShortcutInputSchema.parse(args);
        logContext.args = parsedArgs;
        const result = await findKeyboardShortcut(parsedArgs);
        logContext.response = result;
        logContext.status = 'ok';
        return wrapSuccess(result, formatFindShortcutSummary(result));
      } catch (error) {
        logContext.errorMessage = error.message;
        return wrapError(`find_keyboard_shortcut failed: ${error.message}`);
      } finally {
        finishLog(logContext, extra);
      }
    }
  );
}

module.exports = {
  registerTools,
  // Exported for direct testing or ad-hoc scripts.
  listSurfaces,
  getFeature,
  findFeature,
  listKeyboardShortcuts,
  getKeyboardShortcut,
  findKeyboardShortcut,
};

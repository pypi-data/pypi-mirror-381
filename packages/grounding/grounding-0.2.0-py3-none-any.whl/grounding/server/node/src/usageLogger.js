function sanitizeJson(value, maxLength = 2048) {
  if (value == null) {
    return null;
  }

  try {
    const serialized = JSON.stringify(value);
    if (serialized.length <= maxLength) {
      return value;
    }

    return {
      truncated: true,
      preview: serialized.slice(0, maxLength),
    };
  } catch (_error) {
    return { error: 'non-serializable' };
  }
}

function createUsageLogger({ supabase, logger = console }) {
  if (!supabase) {
    throw new Error('Usage logger requires a Supabase client.');
  }

  async function logUsage({
    startedAt,
    durationMs,
    tokenId,
    developerId,
    agentId,
    toolName,
    status,
    args,
    response,
    errorMessage,
  }) {
    const payload = {
      token_id: tokenId,
      developer_id: developerId,
      agent_id: agentId ?? null,
      tool_name: toolName,
      status,
      duration_ms: durationMs,
      started_at: startedAt,
      request_arguments: sanitizeJson(args),
      response_metadata: sanitizeJson(response),
      error_message: errorMessage ?? null,
    };

    try {
      const { error } = await supabase.from('mcp_usage_events').insert(payload);
      if (error) {
        logger.warn('usage.insert_failed', { error: error.message });
      }
    } catch (error) {
      logger.warn('usage.insert_failed', { error: error.message });
    }
  }

  return { logUsage };
}

module.exports = {
  createUsageLogger,
};

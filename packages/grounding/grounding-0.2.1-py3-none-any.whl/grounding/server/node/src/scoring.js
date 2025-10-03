function tokenize(input) {
  return String(input)
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter(Boolean);
}

function tokenSimilarity(source, query) {
  const sourceTokens = new Set(tokenize(source));
  const queryTokens = Array.from(new Set(tokenize(query)));

  if (queryTokens.length === 0) {
    return 0;
  }

  let matches = 0;
  for (const token of queryTokens) {
    if (sourceTokens.has(token)) {
      matches += 1;
    }
  }

  return matches / queryTokens.length;
}

function substringSimilarity(source, query) {
  const normalizedSource = String(source).toLowerCase();
  const normalizedQuery = String(query).toLowerCase();
  if (!normalizedSource || !normalizedQuery) {
    return 0;
  }
  return normalizedSource.includes(normalizedQuery) ? Math.min(normalizedQuery.length / normalizedSource.length, 1) : 0;
}

function scoreFeature(feature, { description, featureText, featureKey, surface, applicationName, applicationPage }) {
  let score = 0;
  const matchedFields = [];

  if (description) {
    const descriptionScore = tokenSimilarity(feature.description, description);
    const regionScore = feature.uiRegionHint ? tokenSimilarity(feature.uiRegionHint, description) * 0.8 : 0;
    const combined = Math.max(descriptionScore, regionScore);
    if (combined > 0) {
      matchedFields.push('description');
      score += combined * 0.6;
    }
  }

  if (featureText) {
    if (feature.featureTextExact.some((text) => String(text).toLowerCase() === featureText.toLowerCase())) {
      matchedFields.push('featureTextExact');
      score += 0.4;
    } else {
      const arraySimilarity = Math.max(
        ...feature.featureTextExact.map((text) => substringSimilarity(text, featureText)),
        0
      );
      if (arraySimilarity > 0) {
        matchedFields.push('featureTextExact');
        score += arraySimilarity * 0.3;
      }
    }
  }

  if (featureKey) {
    if (feature.featureKey === featureKey) {
      matchedFields.push('featureKey');
      score += 0.8;
    } else if (feature.featureKey.toLowerCase().includes(featureKey.toLowerCase())) {
      matchedFields.push('featureKey');
      score += 0.4;
    }
  }

  if (surface && feature.surface === surface) {
    matchedFields.push('surface');
    score += 0.2;
  }

  if (applicationName && feature.applicationName) {
    if (feature.applicationName.toLowerCase() === applicationName.toLowerCase()) {
      matchedFields.push('applicationName');
      score += 0.3;
    } else if (feature.applicationName.toLowerCase().includes(applicationName.toLowerCase())) {
      matchedFields.push('applicationName');
      score += 0.15;
    }
  }

  if (applicationPage && feature.applicationPage) {
    if (feature.applicationPage.toLowerCase() === applicationPage.toLowerCase()) {
      matchedFields.push('applicationPage');
      score += 0.25;
    } else if (feature.applicationPage.toLowerCase().includes(applicationPage.toLowerCase())) {
      matchedFields.push('applicationPage');
      score += 0.1;
    }
  }

  return {
    score,
    matchedFields,
  };
}

function escapeIlikePattern(value) {
  return value.replace(/[\\%_]/g, (match) => `\\${match}`);
}

function scoreKeyboardShortcut(shortcut, { action, shortcut: shortcutQuery }) {
  let score = 0;
  const matchedFields = [];

  if (action) {
    const actionLower = shortcut.action.toLowerCase();
    const queryLower = action.toLowerCase();

    if (actionLower === queryLower) {
      matchedFields.push('action');
      score += 1.0;
    } else {
      const tokenScore = tokenSimilarity(shortcut.action, action);
      const substringScore = substringSimilarity(shortcut.action, action);
      const combined = Math.max(tokenScore, substringScore);

      if (combined > 0) {
        matchedFields.push('action');
        score += combined * 0.8;
      }
    }
  }

  if (shortcutQuery) {
    const shortcutLower = shortcut.shortcut.toLowerCase();
    const queryLower = shortcutQuery.toLowerCase();

    if (shortcutLower === queryLower) {
      matchedFields.push('shortcut');
      score += 0.9;
    } else if (shortcutLower.includes(queryLower)) {
      matchedFields.push('shortcut');
      score += 0.5;
    }
  }

  return {
    score,
    matchedFields,
  };
}

module.exports = {
  scoreFeature,
  scoreKeyboardShortcut,
  escapeIlikePattern,
};

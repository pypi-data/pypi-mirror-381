function mapFeatureRow(row) {
  if (!row) {
    return null;
  }

  return {
    id: row.id,
    surface: row.surface,
    osName: row.os_name,
    browserName: row.browser_name,
    featureKey: row.feature_key,
    description: row.description,
    featureTextExact: Array.isArray(row.feature_text_exact) ? row.feature_text_exact : [],
    uiRegionHint: row.ui_region_hint ?? null,
    center: {
      px: {
        x: row.center_x_px,
        y: row.center_y_px,
      },
      norm:
        row.center_x_norm != null && row.center_y_norm != null
          ? {
              x: row.center_x_norm,
              y: row.center_y_norm,
            }
          : null,
    },
    targetRadiusPx: row.target_radius_px ?? null,
    applicationName: row.application_name ?? null,
    applicationPage: row.application_page ?? null,
    applicationType: row.application_type ?? null,
    isActive: Boolean(row.is_active),
    version: row.version,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
}

module.exports = {
  mapFeatureRow,
};

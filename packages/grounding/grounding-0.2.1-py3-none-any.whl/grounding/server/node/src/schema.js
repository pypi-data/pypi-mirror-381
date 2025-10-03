const { z } = require('zod');
const { OS_NAME_VALUES, BROWSER_NAME_VALUES, APPLICATION_TYPE_VALUES } = require('./config');

const osNameSchema = z.enum([...OS_NAME_VALUES]);
const browserNameSchema = z.enum([...BROWSER_NAME_VALUES]);

const pixelPointSchema = z.object({
  x: z.number(),
  y: z.number(),
});

const normalizedPointSchema = z.object({
  x: z.number(),
  y: z.number(),
});

const applicationTypeSchema = z.enum([...APPLICATION_TYPE_VALUES]);

const featureOutputShape = {
  id: z.string().uuid(),
  surface: z.string(),
  osName: osNameSchema,
  browserName: browserNameSchema,
  featureKey: z.string(),
  description: z.string(),
  featureTextExact: z.array(z.string()),
  uiRegionHint: z.string().nullable(),
  center: z.object({
    px: pixelPointSchema,
    norm: normalizedPointSchema.nullish(),
  }),
  targetRadiusPx: z.number().int().positive().nullable(),
  applicationName: z.string().nullable(),
  applicationPage: z.string().nullable(),
  applicationType: applicationTypeSchema.nullable(),
  isActive: z.boolean(),
  version: z.number().int(),
  createdAt: z.string(),
  updatedAt: z.string(),
};

const featureOutputSchema = z.object(featureOutputShape);

const featureMatchSchema = featureOutputSchema.extend({
  score: z.number().optional(),
  matchedFields: z.array(z.string()).optional(),
});

const listSurfacesInputShape = {
  os: osNameSchema,
  browser: browserNameSchema,
  includeInactive: z.boolean().optional().default(false),
};

const listSurfacesInputSchema = z.object(listSurfacesInputShape);

const surfaceSummaryShape = {
  surface: z.string(),
  osName: osNameSchema,
  browserName: browserNameSchema,
  totalFeatures: z.number().int().nonnegative(),
  activeFeatures: z.number().int().nonnegative(),
  sampleFeatureKeys: z.array(z.string()),
};

const surfaceSummarySchema = z.object(surfaceSummaryShape);

const listSurfacesResultShape = {
  surfaces: z.array(surfaceSummarySchema),
};

const listSurfacesResultSchema = z.object(listSurfacesResultShape);

const getFeatureInputShape = {
  featureKey: z.string().min(1),
  os: osNameSchema.optional(),
  browser: browserNameSchema.optional(),
  surface: z.string().min(1).optional(),
  version: z.number().int().optional(),
  includeInactive: z.boolean().optional().default(false),
};

const getFeatureInputSchema = z.object(getFeatureInputShape);

const getFeatureResultShape = {
  feature: featureOutputSchema.nullable(),
  matchedCount: z.number().int().nonnegative(),
};

const getFeatureResultSchema = z.object(getFeatureResultShape);

const findFeatureInputShape = {
  os: osNameSchema,
  browser: browserNameSchema,
  surface: z.string().min(1).optional(),
  applicationName: z.string().min(1).optional(),
  applicationPage: z.string().min(1).optional(),
  description: z.string().min(2).optional(),
  featureText: z.string().min(1).optional(),
  featureKey: z.string().min(1).optional(),
  limit: z.number().int().min(1).max(50).optional().default(5),
  includeInactive: z.boolean().optional().default(false),
};

const findFeatureInputBaseSchema = z.object(findFeatureInputShape);

const findFeatureInputSchema = findFeatureInputBaseSchema.refine(
  (data) => Boolean(data.description || data.featureText || data.featureKey || data.surface || data.applicationName || data.applicationPage),
  {
    message: 'Provide at least one of description, featureText, featureKey, surface, applicationName, or applicationPage to search.',
  }
);

const findFeatureResultShape = {
  items: z.array(featureMatchSchema),
  limit: z.number().int().min(1),
  returned: z.number().int().min(0),
};

const findFeatureResultSchema = z.object(findFeatureResultShape);

const shortcutOutputShape = {
  id: z.string().uuid(),
  applicationName: z.string(),
  osName: osNameSchema,
  applicationType: applicationTypeSchema,
  action: z.string(),
  shortcut: z.string(),
  createdAt: z.string(),
};

const shortcutOutputSchema = z.object(shortcutOutputShape);

const listShortcutsInputShape = {
  applicationName: z.string().min(1),
  os: osNameSchema,
  applicationType: applicationTypeSchema.optional(),
  action: z.string().min(1).optional(),
  limit: z.number().int().min(1).max(200).optional().default(50),
};

const listShortcutsInputSchema = z.object(listShortcutsInputShape);

const listShortcutsResultShape = {
  shortcuts: z.array(shortcutOutputSchema),
  count: z.number().int().nonnegative(),
};

const listShortcutsResultSchema = z.object(listShortcutsResultShape);

const getShortcutInputShape = {
  action: z.string().min(1),
  applicationName: z.string().min(1),
  os: osNameSchema,
  applicationType: applicationTypeSchema.optional(),
};

const getShortcutInputSchema = z.object(getShortcutInputShape);

const getShortcutResultShape = {
  shortcut: shortcutOutputSchema.nullable(),
  matchedCount: z.number().int().nonnegative(),
};

const getShortcutResultSchema = z.object(getShortcutResultShape);

const shortcutMatchSchema = shortcutOutputSchema.extend({
  score: z.number().optional(),
  matchedFields: z.array(z.string()).optional(),
});

const findShortcutInputShape = {
  applicationName: z.string().min(1),
  os: osNameSchema,
  applicationType: applicationTypeSchema.optional(),
  action: z.string().min(2).optional(),
  shortcut: z.string().min(1).optional(),
  limit: z.number().int().min(1).max(50).optional().default(5),
};

const findShortcutInputBaseSchema = z.object(findShortcutInputShape);

const findShortcutInputSchema = findShortcutInputBaseSchema.refine(
  (data) => Boolean(data.action || data.shortcut),
  {
    message: 'Provide at least one of action or shortcut to search.',
  }
);

const findShortcutResultShape = {
  items: z.array(shortcutMatchSchema),
  limit: z.number().int().min(1),
  returned: z.number().int().min(0),
};

const findShortcutResultSchema = z.object(findShortcutResultShape);

module.exports = {
  osNameSchema,
  browserNameSchema,
  applicationTypeSchema,
  featureOutputSchema,
  featureMatchSchema,
  listSurfacesInputSchema,
  listSurfacesInputShape,
  surfaceSummarySchema,
  surfaceSummaryShape,
  listSurfacesResultSchema,
  listSurfacesResultShape,
  getFeatureInputSchema,
  getFeatureInputShape,
  getFeatureResultSchema,
  getFeatureResultShape,
  findFeatureInputSchema,
  findFeatureInputBaseSchema,
  findFeatureInputShape,
  findFeatureResultSchema,
  findFeatureResultShape,
  shortcutOutputSchema,
  shortcutOutputShape,
  shortcutMatchSchema,
  listShortcutsInputSchema,
  listShortcutsInputShape,
  listShortcutsResultSchema,
  listShortcutsResultShape,
  getShortcutInputSchema,
  getShortcutInputShape,
  getShortcutResultSchema,
  getShortcutResultShape,
  findShortcutInputSchema,
  findShortcutInputBaseSchema,
  findShortcutInputShape,
  findShortcutResultSchema,
  findShortcutResultShape,
};

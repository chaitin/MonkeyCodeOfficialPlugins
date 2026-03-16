---
name: preset-icon-library
description: When creating a new frontend project, analyze the product description and automatically install and configure a suitable icon library to avoid using emojis in the UI.
arguments:
  - name: projectPath
    description: Absolute path to the frontend project directory
    required: true
  - name: productDescription
    description: Brief description of the product/app type to help select the appropriate icon library
    required: false
---

# Preset Icon Library

When creating a new frontend project, automatically select and configure an appropriate icon library based on the product description.

## Core Rules (MUST FOLLOW)

1. **Single Icon Library Per Project** - Only ONE icon library allowed in a project. Never mix multiple icon libraries.

2. **Business Scenario Based Selection** - Icon style must match the business scenario:
   - Dashboard/Admin: Professional, clean, data-oriented
   - E-commerce: Clear, commerce-focused, trustworthy
   - Social/Community: Friendly, approachable, warm
   - Finance/Banking: Professional, serious, trustworthy
   - Healthcare: Clean, medical-standard, empathetic
   - Education: Modern, accessible, encouraging
   - Creative/Design: Unique, artistic, distinctive

3. **Consistent Icon Properties** - All icons must maintain:
   - Same size (e.g., 20px or 24px standard)
   - Same stroke width/line weight (e.g., 1.5px or 2px)
   - Same style (outline vs solid vs duotone)

## Icon Library Options

Based on the business scenario, select the most suitable icon library:

### 1. Comprehensive Giants (Most Recommended)

| Library | Best For | Icons | License |
|---------|----------|-------|---------|
| Lucide | Modern, clean UI, most frameworks | 1500+ | MIT |
| Font Awesome | Enterprise, maximum icon variety | 1600+ (free) | CC BY 4.0 |
| Material Symbols/Icons | Material Design, variable fonts | 2000+ | Apache 2.0 |

### 2. Designer-Friendly (Figma Friendly)

| Library | Best For | Icons | License |
|---------|----------|-------|---------|
| Tabler Icons | SaaS admin, complex dashboards | 5000+ | MIT |
| Phosphor Icons | Premium design, 6 weights/styles | 700+ | MIT |
| Heroicons | Tailwind projects, modern web | 300+ | MIT |

### 3. China-Friendly

| Library | Best For | Icons | License |
|---------|----------|-------|---------|
| iconfont | Chinese products, icon management | 10000+ | Alibaba |
| Remix Icon | Balanced, 24x24 grid design | 2000+ | Apache 2.0 |

### 4. Developer Efficiency

| Library | Best For | Icons | License |
|---------|----------|-------|---------|
| Iconify | Unified API for all icon libraries | 100000+ | MIT |

### Selection Guide by Scenario

| Business Scenario | Recommended Library | Style | Size | Stroke |
|-------------------|---------------------|-------|------|--------|
| Dashboard / Admin / SaaS | Tabler Icons | Outline | 20px | 1.5px |
| E-commerce / Shopping | Lucide / Heroicons | Outline/Solid | 20px | 1.5px |
| Social / Community | Heroicons | Outline | 20px | 1.5px |
| Finance / Banking | Lucide | Outline | 20px | 2px |
| Healthcare / Medical | Lucide / Phosphor | Outline | 20px | 1.5px |
| Education / Learning | Lucide / Remix Icon | Outline | 20px | 1.5px |
| General / Multi-purpose | Lucide | Outline | 20px | 1.5px |
| Mobile App | Heroicons / Ionicons | Solid/Outline | 24px | 1.5px |
| Dashboard with data viz | Lucide / Tabler | Outline | 16px/20px | 1.5px |
| Creative / Design | Phosphor | Duotone | 24px | 1.5px |
| Chinese Product | iconfont / Remix Icon | Outline | 20px | 1.5px |
| Enterprise/Legacy | Font Awesome | Mixed | 20px | varies |
| Multi-library needs | Iconify | Unified | varies | varies |

## Workflow

1. **Analyze the business scenario** from product description to determine the best icon library and style

2. **Check existing icon usage** - If the project already has an icon library installed, continue using it instead of adding a new one

3. **Detect the frontend framework** to determine the correct installation method

4. **Install the icon library** using the appropriate package manager

5. **Create icon configuration** with consistent size and stroke settings

6. **Provide usage guidelines** ensuring all icons follow the same standards

## Icon Configuration Standards

### Size Standards

| Usage Context | Recommended Size |
|--------------|------------------|
| Navigation menu | 20px |
| Buttons | 16px or 20px |
| Form inputs | 16px |
| Data tables | 16px |
| Cards/Widgets | 20px |
| Headers/Page titles | 24px |

### Stroke Width Standards

| Style | Recommended Stroke |
|-------|-------------------|
| Standard outline | 1.5px |
| Heavy/Emphasis | 2px |
| Subtle/Secondary | 1px |

### Implementation Example

For a React project with Lucide:

```bash
npm install lucide-react
```

## Centralized Configuration with Override Support

Create a configuration file to manage icon sizes and styles in one place, with support for per-icon overrides:

```ts
// config/icon.config.ts

export const IconSizes = {
  xs: 12,
  sm: 16,
  md: 20,
  lg: 24,
  xl: 32,
} as const;

export const IconStrokes = {
  thin: 1,
  normal: 1.5,
  bold: 2,
} as const;

export const IconConfig = {
  defaultSize: IconSizes.md,
  defaultStroke: IconStrokes.normal,
  
  // Default sizes by usage context
  sizes: {
    navigation: IconSizes.md,
    button: IconSizes.sm,
    input: IconSizes.sm,
    table: IconSizes.sm,
    card: IconSizes.md,
    heading: IconSizes.lg,
  },
  
  // Default strokes by usage context
  strokes: {
    primary: IconStrokes.normal,
    secondary: IconStrokes.thin,
    emphasis: IconStrokes.bold,
  },
  
  // Per-icon overrides (optional)
  overrides: {
    // Custom size for specific icons
    Home: { size: IconSizes.lg },
    Search: { size: IconSizes.sm },
    Loader2: { size: IconSizes.lg },
    // Custom stroke for specific icons
    AlertCircle: { stroke: IconStrokes.bold },
    // Custom both size and stroke
    Check: { size: IconSizes.xs, stroke: IconStrokes.bold },
  } as Record<string, { size?: number; stroke?: number }>,
} as const;
```

Helper function to resolve icon props with override support:

```ts
// config/icon.config.ts (continued)

type IconName = keyof typeof IconConfig.overrides;

export function getIconProps(name: IconName, contextSize: number, contextStroke: number) {
  const override = IconConfig.overrides[name];
  if (!override) {
    return { size: contextSize, strokeWidth: contextStroke };
  }
  return {
    size: override.size ?? contextSize,
    strokeWidth: override.stroke ?? contextStroke,
  };
}
```

Then use in Icons component:

```tsx
// components/Icons.tsx
import { 
  Home, User, Settings, Search, Bell, 
  Menu, X, ChevronDown, ChevronRight,
  Plus, Edit, Trash, Save, Check,
  Loader2, AlertCircle, Info, Eye,
  Dashboard, Package, Users, CreditCard,
  BarChart3, PieChart, TrendingUp, Calendar
} from 'lucide-react';
import { IconConfig, getIconProps } from '@/config/icon.config';

export const Icons = {
  Home: (props) => {
    const { size, strokeWidth } = getIconProps('Home', IconConfig.sizes.navigation, IconConfig.strokes.primary);
    return <Home size={size} strokeWidth={strokeWidth} {...props} />;
  },
  Dashboard: (props) => (
    <Dashboard size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  User: (props) => (
    <User size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Settings: (props) => (
    <Settings size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Menu: (props) => (
    <Menu size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  
  Search: (props) => {
    const { size, strokeWidth } = getIconProps('Search', IconConfig.sizes.navigation, IconConfig.strokes.primary);
    return <Search size={size} strokeWidth={strokeWidth} {...props} />;
  },
  Bell: (props) => (
    <Bell size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Plus: (props) => (
    <Plus size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  
  Edit: (props) => (
    <Edit size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Trash: (props) => (
    <Trash size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Save: (props) => (
    <Save size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Check: (props) => {
    const { size, strokeWidth } = getIconProps('Check', IconConfig.sizes.button, IconConfig.strokes.primary);
    return <Check size={size} strokeWidth={strokeWidth} {...props} />;
  },
  Eye: (props) => (
    <Eye size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  
  ChevronDown: (props) => (
    <ChevronDown size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  ChevronRight: (props) => (
    <ChevronRight size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  
  AlertCircle: (props) => {
    const { size, strokeWidth } = getIconProps('AlertCircle', IconConfig.sizes.card, IconConfig.strokes.primary);
    return <AlertCircle size={size} strokeWidth={strokeWidth} {...props} />;
  },
  Info: (props) => (
    <Info size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Loader2: (props) => {
    const { size, strokeWidth } = getIconProps('Loader2', IconConfig.sizes.card, IconConfig.strokes.primary);
    return <Loader2 size={size} strokeWidth={strokeWidth} {...props} />;
  },
  
  Package: (props) => (
    <Package size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Users: (props) => (
    <Users size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  CreditCard: (props) => (
    <CreditCard size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  BarChart3: (props) => (
    <BarChart3 size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  PieChart: (props) => (
    <PieChart size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  TrendingUp: (props) => (
    <TrendingUp size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
  Calendar: (props) => (
    <Calendar size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />
  ),
};
```

Override usage: Add entries in `IconConfig.overrides` to customize specific icons:

```ts
overrides: {
  Home: { size: IconSizes.lg },      // Custom size only
  AlertCircle: { stroke: IconStrokes.bold },  // Custom stroke only
  Check: { size: IconSizes.xs, stroke: IconStrokes.bold },  // Custom both
}
```

All icons configured with consistent size and stroke

## Output

After installing, provide the user with:

1. **Selected icon library** and business scenario rationale
2. **Centralized icon configuration file** (`icon.config.ts` or similar)
3. **Standard icon configuration** (size, stroke width)
4. **Centralized icon component** for consistent usage
5. **Usage guidelines** - enforce single library and consistent styling

## Notes

- NEVER allow mixing multiple icon libraries in one project
- ALWAYS enforce consistent icon size and stroke width across all components
- **Use centralized configuration** - create `icon.config.ts` to manage all icon sizes and strokes in one place
- If existing project has an icon library, continue using it rather than introducing new ones
- Select icon library based on business scenario - see the Selection Guide above
- Document the chosen icon library and standards in project README
- **Never use emojis in UI examples - always use the icon library instead**

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

| Business Scenario | Recommended Library | Style | Size | Stroke |
|-------------------|---------------------|-------|------|--------|
| Dashboard / Admin / SaaS | Lucide | Outline | 20px | 1.5px |
| E-commerce / Shopping | Lucide | Outline/Solid | 20px | 1.5px |
| Social / Community | Heroicons | Outline | 20px | 1.5px |
| Finance / Banking | Lucide | Outline | 20px | 2px |
| Healthcare / Medical | Lucide | Outline | 20px | 1.5px |
| Education / Learning | Lucide | Outline | 20px | 1.5px |
| General / Multi-purpose | Lucide | Outline | 20px | 1.5px |
| Mobile App | Heroicons | Solid/Outline | 24px | 1.5px |
| Dashboard with data viz | Lucide | Outline | 16px/20px | 1.5px |
| Creative / Design | Phosphor | Duotone | 24px | 1.5px |

### Popular Icon Libraries Reference

- **Lucide** - https://lucide.dev (1500+ icons, MIT license)
- **Heroicons** - https://heroicons.com (By Tailwind CSS team, MIT license)
- **Tabler Icons** - https://tabler-icons.io (1500+ icons, MIT license)
- **Phosphor Icons** - https://phosphoricons.com (700+ icons, MIT license)

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

## Centralized Configuration

Create a configuration file to manage icon sizes and styles in one place:

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
  // Override sizes by usage context
  sizes: {
    navigation: IconSizes.md,
    button: IconSizes.sm,
    input: IconSizes.sm,
    table: IconSizes.sm,
    card: IconSizes.md,
    heading: IconSizes.lg,
  },
  // Override stroke by usage context
  strokes: {
    primary: IconStrokes.normal,
    secondary: IconStrokes.thin,
    emphasis: IconStrokes.bold,
  }
} as const;
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
import { IconConfig } from '@/config/icon.config';

export const Icons = {
  Home: (props) => <Home size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Dashboard: (props) => <Dashboard size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  User: (props) => <User size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Settings: (props) => <Settings size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Menu: (props) => <Menu size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  
  Search: (props) => <Search size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Bell: (props) => <Bell size={IconConfig.sizes.navigation} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Plus: (props) => <Plus size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  
  Edit: (props) => <Edit size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Trash: (props) => <Trash size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Save: (props) => <Save size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Check: (props) => <Check size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Eye: (props) => <Eye size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  
  ChevronDown: (props) => <ChevronDown size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  ChevronRight: (props) => <ChevronRight size={IconConfig.sizes.button} strokeWidth={IconConfig.strokes.primary} {...props} />,
  
  AlertCircle: (props) => <AlertCircle size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Info: (props) => <Info size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Loader2: (props) => <Loader2 size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  
  Package: (props) => <Package size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Users: (props) => <Users size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  CreditCard: (props) => <CreditCard size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  BarChart3: (props) => <BarChart3 size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  PieChart: (props) => <PieChart size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  TrendingUp: (props) => <TrendingUp size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
  Calendar: (props) => <Calendar size={IconConfig.sizes.card} strokeWidth={IconConfig.strokes.primary} {...props} />,
};
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
- **Always use centralized configuration** - create `icon.config.ts` to manage all icon sizes and strokes in one place
- If existing project has an icon library, continue using it rather than introducing new ones
- Default to Lucide for most business scenarios unless specifically justified
- Document the chosen icon library and standards in project README

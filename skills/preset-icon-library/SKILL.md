---
name: preset-icon-library
description: "Automatically manage icon libraries - install when creating projects, add missing icons when editing. Use when: 1) any icon is needed in UI, 2) AI wants to use emoji instead of icon."
arguments:
  - name: projectPath
    description: Absolute path to the frontend project directory
    required: true
  - name: productDescription
    description: Brief description of the product/app type
    required: false
---

# Preset Icon Library

## Core Rules

1. **Business Scenario Based** - Match icon style to project type
2. **Consistent Sizing** - Same size and stroke width across all icons
3. **Add New Libraries When Needed** - If existing library lacks needed icons, add a style-compatible library

## Workflow

### Creating New Project

1. Analyze business scenario → select appropriate icon library
2. Detect frontend framework → install via npm/yarn/pnpm
3. Create centralized icon config with consistent size/stroke

### Adding Missing Icons

1. Check `package.json` for existing icon library
2. If exists: find similar icon in same library
3. If not found: install a style-compatible library, use closest match
4. Add to Icons component, never use emoji as fallback

### Icon Library Selection

| Scenario | Recommended |
|----------|-------------|
| Dashboard / Admin | Tabler Icons, Lucide |
| E-commerce | Lucide, Heroicons |
| Social / Community | Heroicons |
| Finance / Banking | Lucide |
| Healthcare | Lucide, Phosphor |
| Mobile App | Heroicons, Ionicons |
| Creative / Design | Phosphor |
| Chinese Product | iconfont, Remix Icon |
| General / Default | Lucide |

### Common Libraries

- **Lucide** - https://lucide.dev (1500+, modern, MIT)
- **Tabler Icons** - https://tabler-icons.io (5000+, MIT)
- **Heroicons** - https://heroicons.com (300+, Tailwind, MIT)
- **Phosphor** - https://phosphoricons.com (700+, premium, MIT)
- **iconfont** - https://www.iconfont.cn (10000+, Alibaba)
- **Remix Icon** - https://remixicon.com (2000+, MIT)

## Icon Configuration

Create `config/icon.config.ts`:

```ts
export const IconConfig = {
  defaultSize: 20,
  defaultStroke: 1.5,
  sizes: { navigation: 20, button: 16, card: 20, heading: 24 },
  strokes: { primary: 1.5, emphasis: 2 },
} as const;
```

Use in icons component:

```tsx
import { SomeIcon } from 'lucide-react';
import { IconConfig } from '@/config/icon.config';

export const Icons = {
  SomeIcon: (props) => <SomeIcon size={IconConfig.sizes.card} strokeWidth={IconConfig.defaultStroke} {...props} />,
};
```

## Notes

- Use centralized config for consistent sizing
- Add new style-compatible icon library when needed
- **Avoid using emojis in UI examples - always use the icon library instead**

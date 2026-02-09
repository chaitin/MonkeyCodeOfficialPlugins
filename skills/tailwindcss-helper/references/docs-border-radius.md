### Apply directional border radius (start) with Tailwind CSS

Source: https://tailwindcss.com/docs/border-radius

Tailwind CSS utilities for applying border-radius to start-side corners (logical direction). Supports predefined scales, custom properties, and arbitrary values for inline-start and block-start corners.

```css
/* Start-side directional radius */
.rounded-s-xs { border-start-start-radius: var(--radius-xs); /* 0.125rem (2px) */ border-end-start-radius: var(--radius-xs); /* 0.125rem (2px) */ }
.rounded-s-sm { border-start-start-radius: var(--radius-sm); /* 0.25rem (4px) */ border-end-start-radius: var(--radius-sm); /* 0.25rem (4px) */ }
.rounded-s-md { border-start-start-radius: var(--radius-md); /* 0.375rem (6px) */ border-end-start-radius: var(--radius-md); /* 0.375rem (6px) */ }
.rounded-s-lg { border-start-start-radius: var(--radius-lg); /* 0.5rem (8px) */ border-end-start-radius: var(--radius-lg); /* 0.5rem (8px) */ }
.rounded-s-xl { border-start-start-radius: var(--radius-xl); /* 0.75rem (12px) */ border-end-start-radius: var(--radius-xl); /* 0.75rem (12px) */ }
.rounded-s-2xl { border-start-start-radius: var(--radius-2xl); /* 1rem (16px) */ border-end-start-radius: var(--radius-2xl); /* 1rem (16px) */ }
.rounded-s-3xl { border-start-start-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-end-start-radius: var(--radius-3xl); /* 1.5rem (24px) */ }
.rounded-s-4xl { border-start-start-radius: var(--radius-4xl); /* 2rem (32px) */ border-end-start-radius: var(--radius-4xl); /* 2rem (32px) */ }
.rounded-s-none { border-start-start-radius: 0; border-end-start-radius: 0; }
.rounded-s-full { border-start-start-radius: calc(infinity * 1px); border-end-start-radius: calc(infinity * 1px); }
.rounded-s-(<custom-property>) { border-start-start-radius: var(<custom-property>); border-end-start-radius: var(<custom-property>); }
.rounded-s-[<value>] { border-start-start-radius: <value>; border-end-start-radius: <value>; }
```

--------------------------------

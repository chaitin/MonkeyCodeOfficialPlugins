### Remove Drop Shadow with Tailwind CSS Utility

Source: https://tailwindcss.com/docs/filter-drop-shadow

Use the drop-shadow-none utility class to remove an existing drop shadow from an element. The example shows how to conditionally remove drop shadows in dark mode using the dark: variant modifier.

```html
<svg class="drop-shadow-lg dark:drop-shadow-none">  <!-- ... --></svg>
```

--------------------------------

### Adjust Drop Shadow Opacity with Tailwind CSS Modifiers

Source: https://tailwindcss.com/docs/filter-drop-shadow

Use opacity modifiers (e.g., /25, /50) with drop-shadow utilities to control shadow transparency. The example shows how to apply the same drop-shadow-xl class with different opacity levels (default, 25%, 50%) to create varying shadow intensities on filled SVG elements.

```html
<svg class="fill-white drop-shadow-xl ...">...</svg>
<svg class="fill-white drop-shadow-xl/25 ...">...</svg>
<svg class="fill-white drop-shadow-xl/50 ...">...</svg>
```

--------------------------------

### Set Drop Shadow Color with Tailwind CSS Color Utilities

Source: https://tailwindcss.com/docs/filter-drop-shadow

Use color-specific drop-shadow utilities (e.g., drop-shadow-cyan-500, drop-shadow-indigo-500) combined with opacity modifiers to customize shadow colors. The example demonstrates applying colored drop shadows to SVG elements with matching fill colors and adjustable opacity.

```html
<svg class="fill-cyan-500 drop-shadow-lg drop-shadow-cyan-500/50 ...">...</svg>
<svg class="fill-indigo-500 drop-shadow-lg drop-shadow-indigo-500/50 ...">...</svg>
```

--------------------------------

### Apply Drop Shadow with Tailwind CSS Classes

Source: https://tailwindcss.com/docs/filter-drop-shadow

Use Tailwind CSS drop-shadow utility classes to add drop shadows to SVG and text elements. The example demonstrates applying different drop shadow sizes (md, lg, xl) to SVG elements. Drop shadows are particularly useful for irregular shapes where box-shadow may not work effectively.

```html
<svg class="drop-shadow-md ...">  <!-- ... --></svg>
<svg class="drop-shadow-lg ...">  <!-- ... --></svg>
<svg class="drop-shadow-xl ...">  <!-- ... --></svg>
```

--------------------------------

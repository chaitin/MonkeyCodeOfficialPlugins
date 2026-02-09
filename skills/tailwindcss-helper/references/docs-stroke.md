### Use Custom Theme Stroke Color in Tailwind CSS Markup

Source: https://tailwindcss.com/docs/stroke

This example demonstrates how to apply a custom stroke color that has been defined within the Tailwind CSS theme. After defining `--color-regal-blue` in the theme, it can be used directly in HTML markup as `stroke-regal-blue`.

```html
<svg class="stroke-regal-blue">  <!-- ... --></svg>
```

--------------------------------

### Apply Neutral Stroke Colors in Tailwind CSS

Source: https://tailwindcss.com/docs/stroke

Neutral stroke color utilities starting from stroke-neutral-50 (lightest) to stroke-neutral-200 (shown). These completely desaturated neutral tones provide maximum flexibility for achromatic stroke styling across diverse design contexts.

```css
.stroke-neutral-50 { stroke: var(--color-neutral-50); /* oklch(98.5% 0 0) */ }
.stroke-neutral-100 { stroke: var(--color-neutral-100); /* oklch(97% 0 0) */ }
.stroke-neutral-200 { stroke: var(--color-neutral-200); /* oklch(92.2% 0 0) */ }
```

--------------------------------

### Apply Custom CSS Variable Stroke Color to SVG in Tailwind CSS

Source: https://tailwindcss.com/docs/stroke

This example demonstrates how to use a CSS variable as a stroke color with the `stroke-(<custom-property>)` syntax. This is a convenient shorthand for `stroke-[var(<custom-property>)]`, enabling dynamic color changes via CSS variables.

```html
<svg class="stroke-(--my-stroke-color) ...">  <!-- ... --></svg>
```

--------------------------------

### Set SVG Stroke Color to Current Text Color with Tailwind CSS

Source: https://tailwindcss.com/docs/stroke

This example illustrates the use of the `stroke-current` utility to dynamically match an SVG's stroke color to the parent element's text color. It's particularly useful for creating interactive elements where the icon's color should adapt to its surrounding text, such as on hover states.

```html
<button class="bg-white text-pink-600 hover:bg-pink-600 hover:text-white ...">  <svg class="size-5 stroke-current ..." fill="none">    <!-- ... -->  </svg>  Download file</button>
```

--------------------------------

### Override default theme variable value

Source: https://tailwindcss.com/docs/theme

Redefine a default theme variable to change its value. This example overrides the sm breakpoint from 40rem to 30rem, affecting all sm: responsive variants.

```css
@import "tailwindcss";
@theme {
  --breakpoint-sm: 30rem;
}
```

--------------------------------

### Define Breakpoint Theme Variable

Source: https://tailwindcss.com/docs/theme

Create responsive breakpoint theme variables in the --breakpoint-* namespace to generate responsive variants. This example defines a 3xl breakpoint at 120rem that enables the 3xl: variant for responsive design.

```css
@import "tailwindcss";
@theme {
  --breakpoint-3xl: 120rem;
}
```

--------------------------------

### Share Theme Variables Across Projects in Tailwind CSS

Source: https://tailwindcss.com/docs/theme

Define theme variables in a separate CSS file and import them across multiple projects using @import. This approach works well for monorepo setups or can be published to NPM for distribution.

```css
@theme {
  --*: initial;
  --spacing: 4px;
  --font-body: Inter, sans-serif;
  --color-lagoon: oklch(0.72 0.11 221.19);
  --color-coral: oklch(0.74 0.17 40.24);
  --color-driftwood: oklch(0.79 0.06 74.59);
  --color-tide: oklch(0.49 0.08 205.88);
  --color-dusk: oklch(0.82 0.15 72.09);
}
```

```css
@import "tailwindcss";
@import "../brand/theme.css";
```

--------------------------------

### Utilize Tailwind CSS Theme Variables in HTML Arbitrary Values

Source: https://tailwindcss.com/docs/theme

This example shows how to incorporate Tailwind CSS theme variables into arbitrary values directly within HTML. It's particularly useful when combined with CSS functions like `calc()` to create dynamic and responsive designs, such as achieving concentric border radii by subtracting a fixed pixel value from a theme variable.

```html
<div class="relative rounded-xl">
  <div class="absolute inset-px rounded-[calc(var(--radius-xl)-1px)]">
    <!-- ... -->
  </div>
  <!-- ... -->
</div>
```

--------------------------------

### Retrieve Resolved Tailwind CSS Theme Variable Values in JavaScript

Source: https://tailwindcss.com/docs/theme

This JavaScript example demonstrates how to programmatically access the computed, resolved value of a CSS theme variable. By using `getComputedStyle` on `document.documentElement` and then `getPropertyValue`, you can retrieve the current value of any CSS variable defined on the root element, which is useful for dynamic calculations or logic based on your theme.

```javascript
let styles = getComputedStyle(document.documentElement);
let shadow = styles.getPropertyValue("--shadow-xl");
```

--------------------------------

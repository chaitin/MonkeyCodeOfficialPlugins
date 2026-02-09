### Use CSS Variables in CSS Modules to Improve Tailwind Performance

Source: https://tailwindcss.com/docs/compatibility

This example shows an alternative approach for CSS modules, utilizing standard CSS variables instead of Tailwind's `@apply` directive. By directly using CSS variables, Tailwind can skip processing these files, which significantly improves build performance and avoids context sharing complexities.

```css
button {  background: var(--color-blue-500);}
```

--------------------------------

### Apply color utilities with Tailwind hover states

Source: https://tailwindcss.com/docs/compatibility

Illustrates using Tailwind's predefined color palette with utility classes and hover variants instead of preprocessor color functions like darken() or lighten(). Demonstrates the recommended workflow of using a comprehensive color palette with light and dark shades.

```html
<button class="bg-indigo-500 hover:bg-indigo-600 ...">
  <!-- ... -->
</button>
```

--------------------------------

### Reference Global Styles in CSS Modules for Tailwind @apply

Source: https://tailwindcss.com/docs/compatibility

This snippet demonstrates how to explicitly import global styles (e.g., `app.css`) into a CSS module (`Button.module.css`) using `@reference`. This is necessary to ensure that Tailwind's `@apply` directive can access globally defined theme variables, as CSS modules are processed in isolation.

```css
@reference "../app.css";
button {  @apply bg-blue-500;}
```

--------------------------------

### Reference Global Styles in Vue/Svelte/Astro Components for Tailwind @apply

Source: https://tailwindcss.com/docs/compatibility

This code illustrates how to import global styles (e.g., `app.css`) into a scoped style block within a Vue component (also applicable to Svelte and Astro) using `@reference`. This ensures that Tailwind's `@apply` directive can correctly access globally defined theme variables, addressing context sharing limitations in component-scoped styles.

```vue
<template>
  <button><slot /></button>
</template>
<style scoped>
  @reference "../app.css";
  button {
    @apply bg-blue-500;
  }
</style>
```

--------------------------------

### Bundle CSS imports with Tailwind

Source: https://tailwindcss.com/docs/compatibility

Demonstrates how Tailwind automatically bundles CSS files included with @import statements without requiring separate preprocessing tools like Sass or postcss-import. The typography.css file is automatically included in the compiled output.

```css
@import "tailwindcss";
@import "./typography.css";
```

--------------------------------

### Use native CSS variables in Tailwind

Source: https://tailwindcss.com/docs/compatibility

Shows how to use native CSS variables (custom properties) in Tailwind projects without requiring a preprocessor. Modern browsers fully support CSS variables, and Tailwind relies on them internally for its configuration system.

```css
.typography {
  font-size: var(--text-base);
  color: var(--color-gray-700);
}
```

--------------------------------

### Flatten nested CSS with Tailwind

Source: https://tailwindcss.com/docs/compatibility

Demonstrates nested CSS syntax that Tailwind processes using Lightning CSS. Tailwind automatically flattens nested selectors into standard CSS that all modern browsers understand, eliminating the need for preprocessors like Sass.

```css
.typography {
  p {
    font-size: var(--text-base);
  }
  img {
    border-radius: var(--radius-lg);
  }
}
```

```css
.typography p {
  font-size: var(--text-base);
}
.typography img {
  border-radius: var(--radius-lg);
}
```

--------------------------------

### Use CSS Variables in Vue/Svelte/Astro Components for Better Tailwind Performance

Source: https://tailwindcss.com/docs/compatibility

This snippet demonstrates using globally defined CSS variables directly within a scoped style block in a Vue component (also relevant for Svelte and Astro). This method bypasses the need for `@apply`, allowing Tailwind to avoid processing the component's CSS entirely and leading to substantial improvements in build performance.

```vue
<template>
  <button><slot /></button>
</template>
<style scoped>
  button {
    background-color: var(--color-blue-500);
  }
</style>
```

--------------------------------

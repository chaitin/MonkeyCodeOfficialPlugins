### Update Tailwind CLI Commands for v4 Package

Source: https://tailwindcss.com/docs/upgrade-guide

This example illustrates the change in how to invoke the Tailwind CSS CLI in v4. The CLI now resides in the dedicated `@tailwindcss/cli` package, replacing the direct `tailwindcss` command. The second line shows the updated command for processing input and output CSS files.

```bash
npx tailwindcss -i input.css -o output.css
npx @tailwindcss/cli -i input.css -o output.css
```

--------------------------------

### Configure PostCSS for Tailwind CSS v4 Migration

Source: https://tailwindcss.com/docs/upgrade-guide

This `postcss.config.mjs` example shows a configuration during the v3 to v4 upgrade. In v4, the PostCSS plugin is `@tailwindcss/postcss`, and `postcss-import` and `autoprefixer` can often be removed as their functionalities are now handled automatically by Tailwind CSS.

```javascript
export default {
  plugins: {
    "postcss-import": {},
    tailwindcss: {},
    autoprefixer: {},
    "@tailwindcss/postcss": {},
  },
};
```

--------------------------------

### Apply Prefixed Tailwind CSS Classes in HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 introduces a new syntax for prefixes, where they act like variants and are placed at the beginning of the class name. This HTML example demonstrates how to use prefixed classes for styling elements.

```html
<div class="tw:flex tw:bg-red-500 tw:hover:bg-red-600">  <!-- ... --></div>
```

--------------------------------

### Apply Important Modifier in Tailwind CSS v4.0 HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 changes the syntax for the important modifier. Instead of placing `!` at the beginning (after variants), it should now be placed at the very end of the class name. This HTML example demonstrates the new syntax, while the old way is deprecated.

```html
<div class="flex! bg-red-500! hover:bg-red-600/50!">  <!-- ... --></div>
```

--------------------------------

### Customize Tailwind CSS v4 `container` utility with `@utility` directive

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 removes direct configuration options for the `container` utility. To customize its behavior, such as setting `margin-inline` or `padding-inline`, use the `@utility` directive within your CSS. This example demonstrates how to define custom container styles.

```css
@utility container {
  margin-inline: auto;
  padding-inline: 2rem;}
```

--------------------------------

### Retrieve Resolved CSS Variable Value in JavaScript

Source: https://tailwindcss.com/docs/upgrade-guide

If you need to programmatically access the resolved value of a Tailwind CSS theme variable in JavaScript, you can use `getComputedStyle`. This snippet demonstrates how to get the computed style of the document root and then retrieve the value of a specific CSS variable, such as `--shadow-xl`.

```JavaScript
let styles = getComputedStyle(document.documentElement);let shadow = styles.getPropertyValue("--shadow-xl");
```

--------------------------------

### Define Custom Component Utilities with Tailwind CSS v4.0 `@utility` API

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0's `@utility` API also replaces `@layer components` for defining component-like classes. This CSS example shows how to define a `.btn` component utility using the new API, which benefits from automatic sorting based on property count, allowing easier overwriting.

```css
@layer components {  .btn {    border-radius: 0.5rem;    padding: 0.5rem 1rem;    background-color: ButtonFace;  }}@utility btn {  border-radius: 0.5rem;  padding: 0.5rem 1rem;  background-color: ButtonFace;}
```

--------------------------------

### Update Tailwind CSS v3 `ring` utility to `ring-3` in v4

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 changes the default `ring` utility width from `3px` to `1px`. To maintain the v3 `3px` ring width, projects must explicitly use `ring-3` instead of just `ring`. This example demonstrates the required update for ring utilities.

```html
<input class="ring ring-blue-500" /><input class="ring-3 ring-blue-500" />
```

--------------------------------

### Animate with Tailwind CSS Variables in React using Motion

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 encourages using generated CSS variables directly instead of a `resolveConfig` function for accessing theme values in JavaScript. This example shows how to animate a React component's background color using a Tailwind CSS variable with the popular Motion library.

```JSX
<motion.div animate={{ backgroundColor: "var(--color-blue-500)" }} />
```

--------------------------------

### Update Tailwind CSS v3 shadow, radius, and blur scales to v4

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 renames default shadow, radius, and blur scales. Projects must update v3 utilities like `shadow-sm` to their v4 equivalents, such as `shadow-xs` for the smallest scale, and `shadow-sm` for the new default shadow. This example illustrates the updated utility names.

```html
<input class="shadow-sm" /><input class="shadow-xs" /><input class="shadow" /><input class="shadow-sm" />
```

--------------------------------

### Tailwind CSS v4 `space-x/y` selector change and `gap` migration

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 updates the internal CSS selector for `space-x-*` and `space-y-*` utilities for performance, changing margin application. If issues arise, it's recommended to migrate to flex or grid layouts using the `gap` utility. The examples show the CSS selector change and an HTML migration to `flex flex-col gap-4`.

```css
/* Before */.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  margin-top: 1rem;}
/* Now */.space-y-4 > :not(:last-child) {
  margin-bottom: 1rem;}
```

```html
<div class="space-y-4 p-4"><div class="flex flex-col gap-4 p-4">  <label for="name">Name</label>  <input type="text" name="name" /></div>
```

--------------------------------

### Tailwind CSS v4 gradient variant behavior and `via-none` usage

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 preserves gradient values when a variant overrides part of a gradient, unlike v3 which would reset the entire gradient. To explicitly 'unset' a three-stop gradient back to a two-stop gradient in a specific state, use `via-none`. The examples illustrate v3's resetting behavior and v4's preservation with `via-none` for explicit control.

```html
<div class="bg-gradient-to-r from-red-500 to-yellow-400 dark:from-blue-500">  <!-- ... --></div>
```

```html
<div class="bg-linear-to-r from-red-500 via-orange-400 to-yellow-400 dark:via-none dark:from-blue-500 dark:to-teal-400">  <!-- ... --></div>
```

--------------------------------

### Handle Outline-Color Transitions - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Set outline color unconditionally or explicitly for both states to avoid unintended color transitions. The transition and transition-colors utilities now include outline-color property in v4.

```html
<button class="outline-cyan-500 transition hover:outline-2"></button>
```

--------------------------------

### Update Grid and Object-Position Arbitrary Values - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Replace commas with underscores in grid-cols-*, grid-rows-*, and object-* utilities to represent spaces. Comma replacement for space compatibility with v2 is no longer supported in v4.

```html
<div class="grid-cols-[max-content_auto]"></div>
```

--------------------------------

### Update Transform Transitions - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Include individual transform properties (rotate, scale, translate) in custom transition lists instead of the generic transform property. Utilities will no longer transition if only transform is specified.

```html
<button class="transition-[opacity,scale] hover:scale-150"></button>
```

--------------------------------

### Upgrade Tailwind CSS Project using `npx @tailwindcss/upgrade`

Source: https://tailwindcss.com/docs/upgrade-guide

This command executes the Tailwind CSS upgrade tool, automating the migration of projects from v3 to v4. It handles dependency updates, configuration file migration, and template file changes. Requires Node.js 20 or higher and should be run in a new branch for safe review.

```bash
npx @tailwindcss/upgrade
```

--------------------------------

### Reset Individual Transform Properties - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Use individual property reset utilities (scale-none, rotate-none, translate-none) instead of transform-none. The transform utilities are now based on individual CSS properties rather than the transform shorthand.

```html
<button class="scale-150 focus:scale-none"></button>
```

--------------------------------

### Update CSS Variables in Arbitrary Values - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Replace square bracket syntax with parentheses for CSS variable arbitrary values in v4. This change addresses ambiguity in CSS variable parsing introduced by recent CSS updates.

```html
<div class="bg-(--brand-color)"></div>
```

--------------------------------

### Update Variant Stacking Order - HTML

Source: https://tailwindcss.com/docs/upgrade-guide

Reverse the order of stacked variants when upgrading to v4, as they now apply left to right instead of right to left. This primarily affects direct child variants (*) and typography plugin variants (prose-headings) when stacked with other variants.

```html
<ul class="py-4 first:*:pt-0 last:*:pb-0">
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

--------------------------------

### Use CSS Variables Instead of theme() Function - CSS

Source: https://tailwindcss.com/docs/upgrade-guide

Prefer CSS variables over the theme() function for theme value access. Use CSS variable names with theme() function in contexts where variables aren't supported, such as media queries.

```css
.my-class {
  background-color: var(--color-red-500);
}
```

```css
@media (width >= theme(--breakpoint-xl)) {
  /* ... */
}
```

--------------------------------

### Hover Variant Device Detection - CSS

Source: https://tailwindcss.com/docs/upgrade-guide

The hover variant now only applies on devices with hover support using @media (hover: hover). Override with custom variant if touch device hover behavior is required, though treating hover as enhancement is recommended.

```css
@media (hover: hover) {
  .hover\:underline:hover {
    text-decoration: underline;
  }
}
```

```css
@custom-variant hover (&:hover);
```

--------------------------------

### Restore Tailwind CSS v3 Dialog Margins in Preflight

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 Preflight removes default margins from `<dialog>` elements for consistency. This CSS snippet re-adds `margin: auto` to dialogs, allowing them to be centered by default as they were in v3.

```css
@layer base {  dialog {    margin: auto;  }}
```

--------------------------------

### Integrate Tailwind CSS v4 with Vite using Dedicated Plugin

Source: https://tailwindcss.com/docs/upgrade-guide

This `vite.config.ts` snippet demonstrates how to configure Vite for Tailwind CSS v4 by using the new dedicated `@tailwindcss/vite` plugin. This approach offers improved performance and a better developer experience compared to the PostCSS plugin. It imports `defineConfig` from `vite` and `tailwindcss` from `@tailwindcss/vite`.

```typescript
import { defineConfig } from "vite";import tailwindcss from "@tailwindcss/vite";export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
});
```

--------------------------------

### Import Tailwind CSS Definitions with @reference in Vue/Svelte

Source: https://tailwindcss.com/docs/upgrade-guide

In Tailwind CSS v4, stylesheets bundled separately (e.g., Vue/Svelte `<style>` blocks, CSS modules) do not automatically access global theme variables or custom utilities. Use the `@reference` directive to import these definitions without duplicating CSS, making them available for `@apply` directives.

```Vue
<template>  <h1>Hello world!</h1></template><style>  @reference "../../app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

--------------------------------

### Apply Tailwind CSS Theme Variables Directly in Vue/Svelte

Source: https://tailwindcss.com/docs/upgrade-guide

As an alternative to `@apply` for frameworks like Vue or Svelte, you can directly use Tailwind's CSS theme variables. This approach can simplify your styling and potentially improve performance by reducing the need for Tailwind to process these styles.

```Vue
<template>  <h1>Hello world!</h1></template><style>  h1 {    color: var(--text-red-500);  }</style>
```

--------------------------------

### Configure Tailwind CSS Theme Variables with Prefix

Source: https://tailwindcss.com/docs/upgrade-guide

When using a prefix in Tailwind CSS v4.0, you should configure your theme variables in CSS without the prefix. The `@import` rule with `prefix(tw)` tells Tailwind to generate CSS variables that include the prefix to avoid conflicts.

```css
@import "tailwindcss" prefix(tw);@theme {  --font-display: "Satoshi", "sans-serif";  --breakpoint-3xl: 120rem;  --color-avocado-100: oklch(0.99 0 0);  --color-avocado-200: oklch(0.98 0.04 113.22);  --color-avocado-300: oklch(0.94 0.11 115.03);  /* ... */}
```

--------------------------------

### Define Custom Utilities with Tailwind CSS v4.0 `@utility` API

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 replaces the `@layer utilities` syntax with the new `@utility` API for defining custom utility classes, leveraging native cascade layers. This CSS snippet compares the old and new methods for defining a `tab-4` utility.

```css
@layer utilities {  .tab-4 {    tab-size: 4;  }}@utility tab-4 {  tab-size: 4;}
```

--------------------------------

### Preserve Tailwind CSS v3 Placeholder Color in Preflight

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 Preflight simplifies placeholder text color to use the current text color at 50% opacity. This CSS snippet allows you to revert to the v3 behavior, making placeholder text use your configured `gray-400` color by default.

```css
@layer base {  input::placeholder,  textarea::placeholder {    color: var(--color-gray-400);  }}
```

--------------------------------

### Migrate Tailwind CSS v3 `outline` and `outline-none` utilities to v4

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 updates the `outline` utility to default `outline-width: 1px` and `outline-<number>` to `outline-style: solid`. The `outline-none` utility is renamed to `outline-hidden`, with a new `outline-none` truly setting `outline-style: none`. Projects should replace `outline outline-2` with `outline-2` and `focus:outline-none` with `focus:outline-hidden`.

```html
<input class="outline outline-2" /><input class="outline-2" />
```

```html
<input class="focus:outline-none" /><input class="focus:outline-hidden" />
```

--------------------------------

### Understand Generated CSS Variables with Tailwind CSS Prefix

Source: https://tailwindcss.com/docs/upgrade-guide

This CSS snippet illustrates how Tailwind CSS v4.0 generates CSS variables when a prefix is configured. The prefix (e.g., `--tw-`) is automatically added to theme variables to prevent naming conflicts with existing CSS variables in your project.

```css
:root {  --tw-font-display: "Satoshi", "sans-serif";  --tw-breakpoint-3xl: 120rem;  --tw-color-avocado-100: oklch(0.99 0 0);  --tw-color-avocado-200: oklch(0.98 0.04 113.22);  --tw-color-avocado-300: oklch(0.94 0.11 115.03);  /* ... */}
```

--------------------------------

### Update Tailwind CSS Ring Utility for v4.0

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4.0 changes the default `ring` utility from 3px to 1px and color from `blue-500` to `currentColor`. This snippet shows how to update existing `ring` classes to `ring-3` and explicitly add `ring-blue-500` to maintain the v3 default behavior in your HTML.

```html
<button class="focus:ring ..."><button class="focus:ring-3 ...">  <!-- ... --></button>
```

```html
<button class="focus:ring-3 focus:ring-blue-500 ...">  <!-- ... --></button>
```

--------------------------------

### Restore Tailwind CSS v3 Button Cursor Behavior in Preflight

Source: https://tailwindcss.com/docs/upgrade-guide

In Tailwind CSS v4.0, Preflight sets buttons to `cursor: default` to match browser behavior. This CSS snippet restores the v3 behavior, applying `cursor: pointer` to non-disabled buttons and elements with `role="button"`.

```css
@layer base {  button:not(:disabled),  [role="button"]:not(:disabled) {    cursor: pointer;  }}
```

--------------------------------

### Preserve Tailwind CSS v3 Ring Behavior with CSS Theme Variables

Source: https://tailwindcss.com/docs/upgrade-guide

To preserve the v3 default ring width (3px) and color (`blue-500`) in Tailwind CSS v4.0 without modifying every class, you can add these theme variables to your CSS. Note that this approach is for compatibility and not considered idiomatic v4.0 usage.

```css
@theme {  --default-ring-width: 3px;  --default-ring-color: var(--color-blue-500);}
```

--------------------------------

### Replace `@tailwind` Directives with `@import` in CSS for v4

Source: https://tailwindcss.com/docs/upgrade-guide

In Tailwind CSS v4, the traditional `@tailwind` directives (e.g., `@tailwind base;`) are no longer used. Instead, Tailwind CSS is imported directly into your CSS file using a standard CSS `@import` statement. This snippet shows both the old directives and the new import method.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
@import "tailwindcss";
```

--------------------------------

### Tailwind CSS v4 `divide-x/y` utility selector change

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 updates the internal CSS selector for `divide-x-*` and `divide-y-*` utilities to improve performance. The new selector applies border to `border-bottom-width` on all children except the last, instead of `border-top-width` on subsequent siblings. This change can affect inline elements or custom margins/paddings.

```css
/* Before */.divide-y-4 > :not([hidden]) ~ :not([hidden]) {
  border-top-width: 4px;}
/* Now */.divide-y-4 > :not(:last-child) {
  border-bottom-width: 4px;}
```

--------------------------------

### Manage Tailwind CSS v4 default border color for `border` and `divide` utilities

Source: https://tailwindcss.com/docs/upgrade-guide

Tailwind CSS v4 changes the default border color for `border-*` and `divide-*` utilities from `gray-200` to `currentColor`. Projects must explicitly specify a color (e.g., `border-gray-200`) or add a base layer CSS rule to restore the v3 default behavior for all elements.

--------------------------------

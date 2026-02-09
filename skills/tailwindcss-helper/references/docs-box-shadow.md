### Apply Different Sized Box Shadows in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/box-shadow

This example demonstrates how to apply various outer box shadow sizes to HTML elements using Tailwind CSS utility classes like `shadow-md`, `shadow-lg`, and `shadow-xl`. These classes provide pre-defined shadow styles for quick application, enhancing the visual depth of elements.

```html
<div class="shadow-md ..."></div><div class="shadow-lg ..."></div><div class="shadow-xl ..."></div>
```

--------------------------------

### Apply Responsive Box Shadows in Tailwind CSS

Source: https://tailwindcss.com/docs/box-shadow

This snippet demonstrates how to apply box shadow utilities conditionally based on screen size using responsive variants. For example, `md:shadow-lg` applies a large shadow only at medium screen sizes and above, overriding `shadow-none`.

```html
<div class="shadow-none md:shadow-lg ...">  <!-- ... --></div>
```

--------------------------------

### Set Custom Box Shadow Colors in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/box-shadow

This example illustrates how to apply specific colors to box shadows using Tailwind CSS color utilities. Classes like `shadow-cyan-500/50` allow developers to define both the color and its opacity for a shadow, enhancing visual branding. This is commonly used for interactive elements like buttons to provide visual feedback.

```html
<button class="bg-cyan-500 shadow-lg shadow-cyan-500/50 ...">Subscribe</button><button class="bg-blue-500 shadow-lg shadow-blue-500/50 ...">Subscribe</button><button class="bg-indigo-500 shadow-lg shadow-indigo-500/50 ...">Subscribe</button>
```

--------------------------------

### Apply Custom Box Shadow Values in Tailwind CSS

Source: https://tailwindcss.com/docs/box-shadow

This snippet shows how to apply custom box shadow values using arbitrary value syntax like `shadow-[<value>]`. It also demonstrates using CSS variables with the `shadow-(<custom-property>)` shorthand, which expands to `shadow-[var(<custom-property>)]`.

```html
<div class="shadow-[0_35px_35px_rgba(0,0,0,0.25)] ...">  <!-- ... --></div>
```

```html
<div class="shadow-(--my-shadow) ...">  <!-- ... --></div>
```

--------------------------------

### Define Inset Ring Colors with Tailwind CSS Variables

Source: https://tailwindcss.com/docs/box-shadow

This snippet illustrates how Tailwind CSS defines various `inset-ring-color` utilities by mapping them to CSS custom properties (`--tw-inset-ring-color`). These definitions use `var()` to reference color values, often with `oklch()` comments indicating the color space. This pattern allows for consistent and themeable ring colors across a project.

```css
--tw-inset-ring-color: var(--color-gray-900); /* oklch(21% 0.034 264.665) */
--tw-inset-ring-color: var(--color-gray-950); /* oklch(13% 0.028 261.692) */
--tw-inset-ring-color: var(--color-zinc-50); /* oklch(98.5% 0 0) */
--tw-inset-ring-color: var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */
--tw-inset-ring-color: var(--color-zinc-200); /* oklch(92% 0.004 286.32) */
--tw-inset-ring-color: var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */
--tw-inset-ring-color: var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */
--tw-inset-ring-color: var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */
--tw-inset-ring-color: var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */
--tw-inset-ring-color: var(--color-zinc-700); /* oklch(37% 0.013 285.805) */
--tw-inset-ring-color: var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */
--tw-inset-ring-color: var(--color-zinc-900); /* oklch(21% 0.006 285.885) */
--tw-inset-ring-color: var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */
--tw-inset-ring-color: var(--color-neutral-50); /* oklch(98.5% 0 0) */
--tw-inset-ring-color: var(--color-neutral-100); /* oklch(97% 0 0) */
--tw-inset-ring-color: var(--color-neutral-200); /* oklch(92.2% 0 0) */
--tw-inset-ring-color: var(--color-neutral-300); /* oklch(87% 0 0) */
--tw-inset-ring-color: var(--color-neutral-400); /* oklch(70.8% 0 0) */
--tw-inset-ring-color: var(--color-neutral-500); /* oklch(55.6% 0 0) */
--tw-inset-ring-color: var(--color-neutral-600); /* oklch(43.9% 0 0) */
--tw-inset-ring-color: var(--color-neutral-700); /* oklch(37.1% 0 0) */
--tw-inset-ring-color: var(--color-neutral-800); /* oklch(26.9% 0 0) */
--tw-inset-ring-color: var(--color-neutral-900); /* oklch(20.5% 0 0) */
--tw-inset-ring-color: var(--color-neutral-950); /* oklch(14.5% 0 0) */
--tw-inset-ring-color: var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */
--tw-inset-ring-color: var(--color-stone-100); /* oklch(97% 0.001 106.424) */
--tw-inset-ring-color: var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */
--tw-inset-ring-color: var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */
--tw-inset-ring-color: var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */
--tw-inset-ring-color: var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */
--tw-inset-ring-color: var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */
--tw-inset-ring-color: var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */
--tw-inset-ring-color: var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */
--tw-inset-ring-color: var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */
--tw-inset-ring-color: var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */
```

--------------------------------

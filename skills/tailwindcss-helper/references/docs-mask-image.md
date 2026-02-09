### Add Radial Mask with Gradient and Position in Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Creates a radial gradient mask on an image element using mask-radial utilities. The example combines mask-radial-[100%_100%] for the gradient size, mask-radial-from-75% for the gradient start, and mask-radial-at-left to position the gradient center. By default, radial masks transition from black to transparent.

```html
<div class="flex items-center gap-4">
  <img class="mask-radial-[100%_100%] mask-radial-from-75% mask-radial-at-left ..." src="/img/keyboard.png" />
  <div class="font-medium">
    <p class="font-mono text-xs text-blue-500 uppercase dark:text-blue-400">Speed</p>
    <p class="mt-2 text-base text-gray-700 dark:text-gray-300">Built for power users</p>
    <p class="mt-1 text-sm leading-relaxed text-balance text-gray-500">
      Work faster than ever with customizable keyboard shortcuts
    </p>
  </div>
</div>
```

--------------------------------

### Customize Conic Gradient Mask Start Color

Source: https://tailwindcss.com/docs/mask-image

Set the starting color of conic gradient masks using mask-conic-from-<color>, mask-conic-from-<number>, mask-conic-from-<percentage>, or mask-conic-from-[<value>] utilities. Supports custom properties and arbitrary values.

```css
.mask-conic-from-red-500 {
  mask-image: conic-gradient(from var(--tw-mask-conic-position), red var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to));
}

.mask-conic-from-50 {
  mask-image: conic-gradient(from var(--tw-mask-conic-position), black calc(var(--spacing) * 50), transparent var(--tw-mask-conic-to));
}

.mask-conic-from-50% {
  mask-image: conic-gradient(from var(--tw-mask-conic-position), black 50%, transparent var(--tw-mask-conic-to));
}
```

--------------------------------

### Remove Mask Image with Tailwind CSS `mask-none` Utility

Source: https://tailwindcss.com/docs/mask-image

This example illustrates the use of the `mask-none` utility to effectively remove any existing mask image from an HTML element. This is useful for resetting or conditionally removing mask effects.

```html
<div class="mask-none">  <!-- ... --></div>
```

--------------------------------

### Apply Image Mask with Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Use the mask-[<value>] syntax to set a custom mask image on an element. This example demonstrates applying a PNG mask image to an element with a background image, creating a masked visual effect.

```html
<div class="mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ...">  <!-- ... --></div>
```

--------------------------------

### Bottom Mask Gradient From Utilities - Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Utilities for controlling the starting point of bottom-to-transparent mask gradients. Supports percentage values, color definitions, custom properties, and arbitrary values to create fade effects from the bottom of elements.

```css
/* mask-b-from-<percentage> */
mask-image: linear-gradient(to bottom, black <percentage>, transparent var(--tw-mask-bottom-to));

/* mask-b-from-<color> */
mask-image: linear-gradient(to bottom, <color> var(--tw-mask-bottom-from), transparent var(--tw-mask-bottom-to));

/* mask-b-from-(<custom-property>) */
mask-image: linear-gradient(to bottom, black var(<custom-property>), transparent var(--tw-mask-bottom-to));

/* mask-b-from-[<value>] */
mask-image: linear-gradient(to bottom, black <value>, transparent var(--tw-mask-bottom-to));
```

--------------------------------

### Use Custom Theme Color in Tailwind CSS Mask Utility

Source: https://tailwindcss.com/docs/mask-image

This example demonstrates how to apply a mask utility using a custom color variable previously defined in the theme. Once `--color-regal-blue` is set, utilities like `mask-radial-from-regal-blue` can be directly used in HTML.

```html
<div class="mask-radial-from-regal-blue">  <!-- ... --></div>
```

--------------------------------

### Mask Radial From Gradient - Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Creates radial gradient masks with customizable start color stops using numeric spacing, percentages, colors, or custom properties. Integrates with radial-gradient shape, size, and position variables.

```css
/* Numeric spacing */
mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black calc(var(--spacing) * <number>), transparent var(--tw-mask-radial-to));
```

```css
/* Percentage */
mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <percentage>, transparent var(--tw-mask-radial-to));
```

```css
/* Color */
mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), <color> var(--tw-mask-radial-from), transparent var(--tw-mask-radial-to));
```

```css
/* Custom property */
mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(<custom-property>), transparent var(--tw-mask-radial-to));
```

```css
/* Arbitrary value */
mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <value>, transparent var(--tw-mask-radial-to));
```

--------------------------------

### Left Mask Gradient From Utilities - Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Utilities for controlling the starting point of left-to-transparent mask gradients. Supports numeric spacing, percentages, colors, custom properties, and arbitrary values to create directional fade effects from the left edge.

```css
/* mask-l-from-<number> */
mask-image: linear-gradient(to left, black calc(var(--spacing) * <number>), transparent var(--tw-mask-left-to));

/* mask-l-from-<percentage> */
mask-image: linear-gradient(to left, black <percentage>, transparent var(--tw-mask-left-to));

/* mask-l-from-<color> */
mask-image: linear-gradient(to left, <color> var(--tw-mask-left-from), transparent var(--tw-mask-left-to));

/* mask-l-from-(<custom-property>) */
mask-image: linear-gradient(to left, black var(<custom-property>), transparent var(--tw-mask-left-to));

/* mask-l-from-[<value>] */
mask-image: linear-gradient(to left, black <value>, transparent var(--tw-mask-left-to));
```

--------------------------------

### Apply Custom CSS Variable for Linear Mask in Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

This example demonstrates using a CSS variable with the `mask-linear-(<custom-property>)` syntax to apply a custom mask. This is a shorthand that automatically wraps the custom property in `var()`, simplifying the use of dynamic mask values.

```html
<div class="mask-linear-(--my-mask) ...">  <!-- ... --></div>
```

--------------------------------

### Mask X-Axis From Gradient - Tailwind CSS

Source: https://tailwindcss.com/docs/mask-image

Creates horizontal gradient masks starting from left and right edges with numeric spacing multipliers, percentages, colors, or custom properties. Applies intersect composite mode for proper mask blending.

```css
/* Numeric spacing */
mask-image: linear-gradient(to right, black calc(var(--spacing) * <number>), transparent var(--tw-mask-right-to)), linear-gradient(to left, black calc(var(--spacing) * <number>), transparent var(--tw-mask-left-to));
mask-composite: intersect;
```

```css
/* Percentage */
mask-image: linear-gradient(to right, black <percentage>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <percentage>, transparent var(--tw-mask-left-to));
mask-composite: intersect;
```

```css
/* Color */
mask-image: linear-gradient(to right, <color> var(--tw-mask-right-from), transparent var(--tw-mask-right-to)), linear-gradient(to left, <color> var(--tw-mask-left-from), transparent var(--tw-mask-left-to));
mask-composite: intersect;
```

```css
/* Custom property */
mask-image: linear-gradient(to right, black var(<custom-property>), transparent var(--tw-mask-right-to)), linear-gradient(to left, black var(<custom-property>), transparent var(--tw-mask-left-to));
mask-composite: intersect;
```

```css
/* Arbitrary value */
mask-image: linear-gradient(to right, black <value>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <value>, transparent var(--tw-mask-left-to));
mask-composite: intersect;
```

--------------------------------

### Set Radial Gradient Position with Tailwind CSS Utilities

Source: https://tailwindcss.com/docs/mask-image

Demonstrates all nine radial gradient position utilities (mask-radial-at-*) applied to background image elements. These utilities control where the center of the radial gradient mask is positioned, ranging from corners to center. Each position utility can be combined with mask-radial-from-* to customize the gradient appearance.

```html
<div class="mask-radial-at-top-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-top mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-top-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-center mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-bottom-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-bottom mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
<div class="mask-radial-at-bottom-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

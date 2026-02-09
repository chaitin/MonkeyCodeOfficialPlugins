### Apply Responsive Height with Tailwind CSS Breakpoint Variants

Source: https://tailwindcss.com/docs/height

This example illustrates how to apply different height utilities based on screen size using Tailwind CSS responsive variants. By prefixing a height utility with a breakpoint (e.g., `md:`), the utility only applies at that breakpoint and above. This is fundamental for creating adaptive layouts that look good on various devices.

```html
<div class="h-1/2 md:h-full ...">  <!-- ... --></div>
```

--------------------------------

### Set Both Width and Height with Tailwind CSS size-* Utilities

Source: https://tailwindcss.com/docs/height

This example shows how to simultaneously set both the width and height of an element using Tailwind CSS `size-*` utilities. These utilities provide a convenient way to create square or uniformly sized elements based on the spacing scale. They are useful for icons, avatars, or fixed-size containers.

```html
<div class="size-16 ...">size-16</div><div class="size-20 ...">size-20</div><div class="size-24 ...">size-24</div><div class="size-32 ...">size-32</div><div class="size-40 ...">size-40</div>
```

--------------------------------

### Set Percentage-Based Height with Tailwind CSS h-full and h-<fraction> Utilities

Source: https://tailwindcss.com/docs/height

This example illustrates how to set an element's height as a percentage of its parent using Tailwind CSS `h-full` or `h-<fraction>` utilities. These classes are ideal for responsive layouts where an element's height needs to scale relative to its container. Ensure the parent element has a defined height for these utilities to work effectively.

```html
<div class="h-full ...">h-full</div><div class="h-9/10 ...">h-9/10</div><div class="h-3/4 ...">h-3/4</div><div class="h-1/2 ...">h-1/2</div><div class="h-1/3 ...">h-1/3</div>
```

--------------------------------

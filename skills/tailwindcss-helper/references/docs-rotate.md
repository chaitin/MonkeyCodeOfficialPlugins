### Apply 3D Rotations with Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example illustrates how to apply 3D rotations to image elements using Tailwind CSS `rotate-x-<number>`, `rotate-y-<number>`, and `rotate-z-<number>` utilities. Combining these classes allows for complex transformations in 3D space.

```html
<img class="rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" /><img class="rotate-x-15 -rotate-y-30 ..." src="/img/mountains.jpg" /><img class="rotate-y-25 rotate-z-30 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Basic 2D Rotations with Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example demonstrates how to apply basic 2D rotations to image elements using Tailwind CSS `rotate-<number>` utilities. These classes rotate an element clockwise by the specified degrees.

```html
<img class="rotate-45 ..." src="/img/mountains.jpg" /><img class="rotate-90 ..." src="/img/mountains.jpg" /><img class="rotate-210 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Responsive Rotations with Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example demonstrates how to apply responsive rotation utilities using breakpoint variants like `md:`. The `md:rotate-60` class will apply a 60-degree rotation only on medium screens and above, overriding any default rotation for smaller screens.

```html
<img class="rotate-45 md:rotate-60 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Custom Rotation with CSS Variables in Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example shows how to use a CSS variable for rotation with the `rotate-(<custom-property>)` syntax. This is a shorthand for `rotate-[var(<custom-property>)]`, enabling dynamic rotation values defined elsewhere in CSS.

```html
<img class="rotate-(--my-rotation) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Custom Rotation Values with Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example demonstrates setting a custom rotation value using Tailwind CSS's arbitrary value syntax `rotate-[<value>]`. This allows for precise control over rotation, accepting any valid CSS rotation unit like radians.

```html
<img class="rotate-[3.142rad] ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Negative 2D Rotations with Tailwind CSS

Source: https://tailwindcss.com/docs/rotate

This example shows how to apply counter-clockwise 2D rotations to image elements using Tailwind CSS `-rotate-<number>` utilities. These classes rotate an element in the opposite direction by the specified degrees.

```html
<img class="-rotate-45 ..." src="/img/mountains.jpg" /><img class="-rotate-90 ..." src="/img/mountains.jpg" /><img class="-rotate-210 ..." src="/img/mountains.jpg" />
```

--------------------------------

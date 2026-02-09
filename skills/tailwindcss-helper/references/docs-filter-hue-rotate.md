### Apply responsive hue-rotate utilities in HTML

Source: https://tailwindcss.com/docs/filter-hue-rotate

Use breakpoint prefixes like md: with hue-rotate utilities to apply different hue rotation values at different screen sizes. This example applies hue-rotate-60 on small screens and hue-rotate-0 on medium screens and above.

```html
<img class="hue-rotate-60 md:hue-rotate-0" src="/img/mountains.jpg" />
```

--------------------------------

### Apply custom hue-rotate values with bracket notation in HTML

Source: https://tailwindcss.com/docs/filter-hue-rotate

Use the hue-rotate-[<value>] bracket notation syntax to apply custom hue rotation values that are not predefined in Tailwind CSS. This example demonstrates using a custom radian value (3.142rad) for precise hue rotation control.

```html
<img class="hue-rotate-[3.142rad]" src="/img/mountains.jpg" />
```

--------------------------------

### Apply negative hue-rotate values in HTML

Source: https://tailwindcss.com/docs/filter-hue-rotate

Use negative hue-rotate utility classes to apply negative hue rotation values to elements. The example shows applying negative rotations (-15, -45, -90 degrees) to image elements using class names like -hue-rotate-15, -hue-rotate-45, etc.

```html
<img class="-hue-rotate-15" src="/img/mountains.jpg" />
<img class="-hue-rotate-45" src="/img/mountains.jpg" />
<img class="-hue-rotate-90" src="/img/mountains.jpg" />
```

--------------------------------

### Apply hue-rotate filter with predefined values in HTML

Source: https://tailwindcss.com/docs/filter-hue-rotate

Use Tailwind CSS hue-rotate utility classes to rotate the hue of an element by specific degrees. The example demonstrates applying different hue rotation values (15, 90, 180, 270 degrees) to image elements using class names like hue-rotate-15, hue-rotate-90, etc.

```html
<img class="hue-rotate-15" src="/img/mountains.jpg" />
<img class="hue-rotate-90" src="/img/mountains.jpg" />
<img class="hue-rotate-180" src="/img/mountains.jpg" />
<img class="hue-rotate-270" src="/img/mountains.jpg" />
```

--------------------------------

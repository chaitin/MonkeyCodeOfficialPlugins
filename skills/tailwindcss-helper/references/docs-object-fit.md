### Applying responsive `object-fit` utilities with Tailwind CSS

Source: https://tailwindcss.com/docs/object-fit

This example demonstrates how to apply `object-fit` utilities responsively using Tailwind CSS breakpoint variants. The image will `object-contain` by default and `object-cover` on medium screens and above.

```html
<img class="object-contain md:object-cover" src="/img/mountains.jpg" />
```

--------------------------------

### Resizing to cover using Tailwind CSS `object-cover`

Source: https://tailwindcss.com/docs/object-fit

This example demonstrates how to use the `object-cover` utility in Tailwind CSS to resize an image. The content will cover the entire container, potentially cropping parts of the image to maintain its aspect ratio.

```html
<img class="h-48 w-96 object-cover ..." src="/img/mountains.jpg" />
```

--------------------------------

### Stretching content to fit container using Tailwind CSS `object-fill`

Source: https://tailwindcss.com/docs/object-fit

This example illustrates the use of the `object-fill` utility in Tailwind CSS. The image content will be stretched to completely fill the container, potentially distorting its aspect ratio.

```html
<img class="h-48 w-96 object-fill ..." src="/img/mountains.jpg" />
```

--------------------------------

### Scaling down content with Tailwind CSS `object-scale-down`

Source: https://tailwindcss.com/docs/object-fit

This example demonstrates the `object-scale-down` utility in Tailwind CSS. The image content will be displayed at its original size, but scaled down to fit the container if it's larger, preserving the aspect ratio.

```html
<img class="h-48 w-96 object-scale-down ..." src="/img/mountains.jpg" />
```

--------------------------------

### Displaying content at original size using Tailwind CSS `object-none`

Source: https://tailwindcss.com/docs/object-fit

This example shows how to use the `object-none` utility in Tailwind CSS. The image content will be displayed at its original size, ignoring the container's dimensions and potentially overflowing or being cut off.

```html
<img class="h-48 w-96 object-none ..." src="/img/mountains.jpg" />
```

--------------------------------

### Containing content within its container using Tailwind CSS `object-contain`

Source: https://tailwindcss.com/docs/object-fit

This example shows how to use the `object-contain` utility in Tailwind CSS. The image content will be scaled to fit within the container, preserving its aspect ratio, which might leave empty space.

```html
<img class="h-48 w-96 object-contain ..." src="/img/mountains.jpg" />
```

--------------------------------

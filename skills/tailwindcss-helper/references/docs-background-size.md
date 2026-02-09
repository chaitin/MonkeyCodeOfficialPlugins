### Apply custom `background-size` value in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example shows how to use arbitrary values with the `bg-size-[<value>]` syntax in Tailwind CSS to set a custom background size, such as `auto 100px`.

```html
<div class="bg-size-[auto_100px] ...">  <!-- ... --></div>
```

--------------------------------

### Apply responsive `background-size` utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example illustrates how to apply responsive `background-size` utilities in Tailwind CSS using breakpoint variants. The `bg-auto` utility is applied by default, and `md:bg-contain` is applied for medium screen sizes and above.

```html
<div class="bg-auto md:bg-contain ...">  <!-- ... --></div>
```

--------------------------------

### Apply `bg-cover` for background image fill in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example demonstrates how to use the `bg-cover` utility in Tailwind CSS to scale a background image to fill its container, potentially cropping the image. It also sets the background position to center.

```html
<div class="bg-[url(/img/mountains.jpg)] bg-cover bg-center"></div>
```

--------------------------------

### Apply custom CSS variable for `background-size` in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example demonstrates using the `bg-size-(<custom-property>)` syntax in Tailwind CSS to apply a custom CSS variable for the `background-size` property. This is a shorthand for `bg-size-[var(<custom-property>)]`.

```html
<div class="bg-size-(--my-image-size) ...">  <!-- ... --></div>
```

--------------------------------

### Apply `bg-auto` for default background image size in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example demonstrates how to use the `bg-auto` utility in Tailwind CSS to display a background image at its default size. It also sets the background position to center and prevents repetition.

```html
<div class="bg-[url(/img/mountains.jpg)] bg-auto bg-center bg-no-repeat"></div>
```

--------------------------------

### Apply `bg-contain` for background image fill without cropping in Tailwind CSS

Source: https://tailwindcss.com/docs/background-size

This example demonstrates how to use the `bg-contain` utility in Tailwind CSS to scale a background image to fit within its container without cropping or stretching. It also sets the background position to center.

```html
<div class="bg-[url(/img/mountains.jpg)] bg-contain bg-center"></div>
```

--------------------------------

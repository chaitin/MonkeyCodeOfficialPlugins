### Apply responsive mask-size utilities in HTML

Source: https://tailwindcss.com/docs/mask-size

Shows how to use responsive prefixes like `md:` with `mask-size` utilities in HTML to apply different mask sizes based on specific screen breakpoints.

```html
<div class="mask-auto md:mask-contain ...">  <!-- ... --></div>
```

--------------------------------

### Apply mask-cover utility in HTML

Source: https://tailwindcss.com/docs/mask-size

Demonstrates how to use the `mask-cover` utility class in HTML to scale a mask image until it fills the mask layer, cropping the image if necessary.

```html
<div class="mask-cover mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

### Apply mask-auto utility in HTML

Source: https://tailwindcss.com/docs/mask-size

Shows how to use the `mask-auto` utility class in HTML to display a mask image at its default size.

```html
<div class="mask-auto mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

### Apply custom mask-size value in HTML

Source: https://tailwindcss.com/docs/mask-size

Demonstrates how to use the arbitrary value syntax `mask-size-[<value>]` in HTML to set a mask image size with a completely custom value, such as `auto 100px`.

```html
<div class="mask-size-[auto_100px] ...">  <!-- ... --></div>
```

--------------------------------

### Apply mask-contain utility in HTML

Source: https://tailwindcss.com/docs/mask-size

Illustrates the use of the `mask-contain` utility class in HTML to scale a mask image to fit within its container without cropping or stretching.

```html
<div class="mask-contain mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

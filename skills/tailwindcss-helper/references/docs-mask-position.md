### Apply responsive Tailwind CSS mask-position utilities

Source: https://tailwindcss.com/docs/mask-position

This example shows how to make `mask-position` utilities responsive in Tailwind CSS using breakpoint variants. By prefixing a utility like `mask-top` with `md:`, the `mask-top` style will only apply at medium screen sizes and above, overriding the default `mask-center` at smaller screens. This enables adaptive mask positioning based on viewport size.

```html
<div class="mask-center md:mask-top ...">  <!-- ... --></div>
```

--------------------------------

### Apply Tailwind CSS mask-position utilities for basic positioning

Source: https://tailwindcss.com/docs/mask-position

This example demonstrates how to use predefined Tailwind CSS classes like `mask-top-left`, `mask-center`, and `mask-bottom-right` to control the position of an element's mask image. These utilities are applied directly to HTML `div` elements, alongside `mask-[url(...)]` and `mask-size-[...]` for defining the mask image and size.

```html
<div class="mask-top-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-center mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

### Set Tailwind CSS mask-position with custom arbitrary values

Source: https://tailwindcss.com/docs/mask-position

This example illustrates how to apply a custom `mask-position` value using Tailwind CSS's arbitrary value syntax, `mask-position-[<value>]`. This allows for highly specific positioning not covered by predefined classes, such as `center top 1rem`. The utility is applied directly to an HTML element.

```html
<div class="mask-position-[center_top_1rem] ...">  <!-- ... --></div>
```

--------------------------------

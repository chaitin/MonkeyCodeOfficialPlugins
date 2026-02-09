### Apply basic mask-mode utilities in HTML

Source: https://tailwindcss.com/docs/mask-mode

This example demonstrates the basic application of `mask-alpha` and `mask-luminance` utilities within HTML elements. It shows how to combine these mask modes with other masking properties and background images to achieve different visual effects.

```html
<div class="mask-alpha mask-r-from-black mask-r-from-50% mask-r-to-transparent bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-luminance mask-r-from-white mask-r-from-50% mask-r-to-black bg-[url(/img/mountains.jpg)] ..."></div>
```

--------------------------------

### Apply responsive mask-mode utilities in HTML

Source: https://tailwindcss.com/docs/mask-mode

This example illustrates how to apply `mask-mode` utilities conditionally based on screen size using Tailwind CSS responsive variants. The `md:mask-luminance` class ensures that the `mask-luminance` utility is only active on medium screen sizes and above, while `mask-alpha` serves as the default.

```html
<div class="mask-alpha md:mask-luminance ...">  <!-- ... --></div>
```

--------------------------------

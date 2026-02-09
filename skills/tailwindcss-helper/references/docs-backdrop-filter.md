### Apply Basic Backdrop Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/backdrop-filter

Demonstrates applying basic backdrop filters like blur and grayscale to an element's backdrop using Tailwind CSS utility classes. It shows individual filters and a combined example on background images.

```html
<div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-grayscale ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs backdrop-grayscale ..."></div></div>
```

--------------------------------

### Remove Backdrop Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/backdrop-filter

Illustrates how to remove all backdrop filters from an element using the `backdrop-filter-none` utility class. This can be applied conditionally, for example, at specific breakpoints.

```html
<div class="backdrop-blur-md backdrop-brightness-150 md:backdrop-filter-none"></div>
```

--------------------------------

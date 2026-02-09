### Apply responsive backdrop sepia with breakpoint variants

Source: https://tailwindcss.com/docs/backdrop-filter-sepia

Use breakpoint prefixes like md: to apply backdrop-sepia utilities conditionally at specific screen sizes. This example applies full sepia on small screens and removes it on medium screens and above.

```html
<div class="backdrop-sepia md:backdrop-sepia-0 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Apply backdrop sepia filter with Tailwind CSS utility classes

Source: https://tailwindcss.com/docs/backdrop-filter-sepia

Use backdrop-sepia utility classes to apply sepia filter effects to an element's backdrop. The basic backdrop-sepia class applies 100% sepia, while backdrop-sepia-<number> variants allow control over the intensity (0-100%). This example demonstrates three different sepia intensity levels applied to background images.

```html
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-sepia-0 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-sepia-50 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-sepia ..."></div>
</div>
```

--------------------------------

### Apply custom backdrop sepia value with arbitrary syntax

Source: https://tailwindcss.com/docs/backdrop-filter-sepia

Use the backdrop-sepia-[<value>] arbitrary value syntax to apply a custom sepia filter value not covered by predefined classes. This allows precise control over the sepia intensity using any valid CSS value.

```html
<div class="backdrop-sepia-[.25] ...">
  <!-- ... -->
</div>
```

--------------------------------

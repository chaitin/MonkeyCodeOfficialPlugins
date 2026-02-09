### Apply responsive marker image with breakpoint variant

Source: https://tailwindcss.com/docs/list-style-image

Prefix the list-image utility with a breakpoint variant like md: to conditionally apply the marker image only at specific screen sizes. This example removes the marker image by default and adds a checkmark image at medium screen sizes and above.

```html
<ul class="list-image-none md:list-image-[url(/img/checkmark.png)] ...">
  <!-- ... -->
</ul>
```

--------------------------------

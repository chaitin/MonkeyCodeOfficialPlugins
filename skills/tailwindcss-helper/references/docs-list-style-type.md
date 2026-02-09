### Apply responsive list-style-type utilities with breakpoint variants

Source: https://tailwindcss.com/docs/list-style-type

Use breakpoint prefixes like md: to apply list-style-type utilities conditionally at specific screen sizes. This example removes list markers on small screens and displays disc markers at medium screen sizes and above.

```html
<ul class="list-none md:list-disc ...">
  <!-- ... -->
</ul>
```

--------------------------------

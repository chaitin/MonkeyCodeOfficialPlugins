### Apply responsive mask-origin with breakpoint variants

Source: https://tailwindcss.com/docs/mask-origin

Use breakpoint prefixes like md: to apply mask-origin utilities conditionally at specific screen sizes. This example applies mask-origin-border by default and switches to mask-origin-padding at medium screen sizes and above.

```html
<div class="mask-origin-border md:mask-origin-padding ...">  <!-- ... --></div>
```

--------------------------------

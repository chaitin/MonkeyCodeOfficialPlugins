### Apply responsive mask-clip utilities with breakpoint variants

Source: https://tailwindcss.com/docs/mask-clip

Use breakpoint prefixes like md: to apply mask-clip utilities conditionally at specific screen sizes. This example applies mask-clip-border by default and switches to mask-clip-padding at medium screen sizes and above.

```html
<div class="mask-clip-border md:mask-clip-padding ...">  <!-- ... --></div>
```

--------------------------------

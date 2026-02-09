### Apply Hardware Accelerated Transforms with Tailwind CSS

Source: https://tailwindcss.com/docs/transform

Use the `transform-gpu` utility to force hardware acceleration for element transitions, potentially improving performance. Conversely, `transform-cpu` can be used to revert to CPU rendering if needed.

```html
<div class="scale-150 transform-gpu">  <!-- ... --></div>
```

--------------------------------

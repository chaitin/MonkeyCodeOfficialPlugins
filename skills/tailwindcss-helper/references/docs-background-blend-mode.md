### Responsive background blend mode with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/background-blend-mode

Apply different background blend modes at different screen sizes using Tailwind CSS breakpoint variants. Prefix blend mode utilities with breakpoint modifiers like md: to apply styles conditionally at medium screen sizes and above.

```html
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-lighten md:bg-blend-darken ...">
  <!-- ... -->
</div>
```

--------------------------------

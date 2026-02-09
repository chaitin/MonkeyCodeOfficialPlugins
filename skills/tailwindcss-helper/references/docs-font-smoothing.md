### Responsive font-smoothing with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/font-smoothing

Combine font-smoothing utilities with breakpoint variants like md: to apply different antialiasing at specific screen sizes. This example uses antialiased on mobile and switches to subpixel-antialiased at medium breakpoint and above.

```html
<p class="antialiased md:subpixel-antialiased ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

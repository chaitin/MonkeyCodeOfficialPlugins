### Responsive transform-style with breakpoint variant

Source: https://tailwindcss.com/docs/transform-style

Shows how to use responsive design with transform-style utilities by prefixing with breakpoint variants like md:. In this example, transform-3d is applied by default and switches to transform-flat at medium screen sizes and above.

```html
<div class="transform-3d md:transform-flat ...">
  <!-- ... -->
</div>
```

--------------------------------

### transform-3d and transform-flat HTML classes

Source: https://tailwindcss.com/docs/transform-style

Demonstrates the difference between transform-3d (preserves 3D space for children) and transform-flat (flattens children to 2D space). The example shows six child divs with various 3D transforms applied, comparing the visual output between 3D and flat rendering modes.

```html
<div class="size-20 transform-flat ...">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div>
</div>
<div class="size-20 transform-3d ...">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div>
</div>
```

--------------------------------

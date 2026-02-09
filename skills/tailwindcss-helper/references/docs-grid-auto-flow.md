### Basic grid-auto-flow Example - Tailwind HTML

Source: https://tailwindcss.com/docs/grid-auto-flow

Demonstrates basic usage of grid-auto-flow utilities with a 3x3 grid layout. Uses grid-flow-row-dense to control auto-placement algorithm, combined with grid-cols-3 and grid-rows-3 for grid dimensions and col-span-2 for spanning multiple columns.

```html
<div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3 ...">
  <div class="col-span-2">01</div>
  <div class="col-span-2">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

--------------------------------

### Responsive grid-auto-flow Design - Tailwind HTML

Source: https://tailwindcss.com/docs/grid-auto-flow

Shows responsive design pattern for grid-auto-flow utilities using breakpoint variants. The md: prefix applies grid-flow-row only at medium screen sizes and above, while defaulting to grid-flow-col on smaller screens.

```html
<div class="grid grid-flow-col md:grid-flow-row ...">
  <!-- ... -->
</div>
```

--------------------------------

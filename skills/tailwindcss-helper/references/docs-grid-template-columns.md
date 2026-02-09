### Apply responsive grid column utilities with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/grid-template-columns

Explains how to make grid column layouts responsive by using breakpoint variants like `md:` with Tailwind CSS utilities. This example sets a single column grid by default and switches to a 6-column grid on medium screens and above.

```html
<div class="grid grid-cols-1 md:grid-cols-6 ...">  <!-- ... --></div>
```

--------------------------------

### Define grid columns with Tailwind CSS `grid-cols-<number>` utility

Source: https://tailwindcss.com/docs/grid-template-columns

Demonstrates how to use Tailwind CSS `grid-cols-<number>` utilities to create a grid with a specified number of equally sized columns. This example creates a 4-column grid.

```html
<div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>09</div></div>
```

--------------------------------

### Implement a subgrid using Tailwind CSS `grid-cols-subgrid`

Source: https://tailwindcss.com/docs/grid-template-columns

Illustrates the use of the `grid-cols-subgrid` utility in Tailwind CSS to make a nested grid item adopt the column tracks of its parent grid. This allows for more complex grid layouts where nested elements align with the parent's grid structure.

```html
<div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>05</div>  <div class="col-span-3 grid grid-cols-subgrid gap-4">    <div class="col-start-2">06</div>  </div></div>
```

--------------------------------

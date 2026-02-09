### Apply Responsive Grid Row Utilities with Tailwind CSS

Source: https://tailwindcss.com/docs/grid-template-rows

This example shows how to apply responsive grid row utilities in Tailwind CSS using breakpoint variants like `md:`. This allows the number of grid rows to change based on screen size, enabling adaptive layouts for different devices.

```html
<div class="grid grid-rows-2 md:grid-rows-6 ...">  <!-- ... --></div>
```

--------------------------------

### Implement Subgrid with Tailwind CSS `grid-rows-subgrid`

Source: https://tailwindcss.com/docs/grid-template-rows

This example shows how to use the `grid-rows-subgrid` utility in Tailwind CSS to make a nested grid item adopt the row tracks defined by its parent. This allows for more complex grid layouts where child elements align with the parent's grid.

```html
<div class="grid grid-flow-col grid-rows-4 gap-4">  <div>01</div>  <!-- ... -->  <div>05</div>  <div class="row-span-3 grid grid-rows-subgrid gap-4">    <div class="row-start-2">06</div>  </div>  <div>07</div>  <!-- ... -->  <div>10</div></div>
```

--------------------------------

### Specify Grid Rows with Tailwind CSS `grid-rows-<number>`

Source: https://tailwindcss.com/docs/grid-template-rows

This example demonstrates how to use Tailwind CSS `grid-rows-<number>` utilities to create a grid with a specified number of equally sized rows. The `grid-rows-4` class sets up a grid with four rows.

```html
<div class="grid grid-flow-col grid-rows-4 gap-4">  <div>01</div>  <!-- ... -->  <div>09</div></div>
```

--------------------------------

### Set Custom Grid Row Values with Tailwind CSS `grid-rows-[<value>]`

Source: https://tailwindcss.com/docs/grid-template-rows

This example illustrates how to use the `grid-rows-[<value>]` syntax in Tailwind CSS to define grid rows with completely custom sizes. This allows for flexible grid layouts beyond the predefined number-based utilities.

```html
<div class="grid-rows-[200px_minmax(900px,1fr)_100px] ...">  <!-- ... --></div>
```

--------------------------------

### Set Grid Rows with CSS Variables using Tailwind CSS `grid-rows-(<custom-property>)`

Source: https://tailwindcss.com/docs/grid-template-rows

This example demonstrates how to use the `grid-rows-(<custom-property>)` syntax in Tailwind CSS to define grid rows using a CSS variable. This provides a convenient shorthand for `grid-rows-[var(<custom-property>)]`, automatically applying the `var()` function.

```html
<div class="grid-rows-(--my-grid-rows) ...">  <!-- ... --></div>
```

--------------------------------

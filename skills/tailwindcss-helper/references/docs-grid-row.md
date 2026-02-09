### Starting and ending grid lines with row-start and row-end

Source: https://tailwindcss.com/docs/grid-row

Use row-start-<number> and row-end-<number> utilities to position elements at specific grid lines. These can be combined with row-span utilities to create precise grid layouts with elements starting and ending at nth grid positions.

```html
<div class="grid grid-flow-col grid-rows-3 gap-4">
  <div class="row-span-2 row-start-2 ...">01</div>
  <div class="row-span-2 row-end-3 ...">02</div>
  <div class="row-start-1 row-end-4 ...">03</div>
</div>
```

--------------------------------

### Spanning rows with row-span utilities

Source: https://tailwindcss.com/docs/grid-row

Use row-span-<number> utilities to make an element span multiple rows in a CSS Grid layout. The example demonstrates a 3-row grid where the first element spans all 3 rows, the second spans 2 columns, and the third spans 2 columns and 2 rows.

```html
<div class="grid grid-flow-col grid-rows-3 gap-4">
  <div class="row-span-3 ...">01</div>
  <div class="col-span-2 ...">02</div>
  <div class="col-span-2 row-span-2 ...">03</div>
</div>
```

--------------------------------

### Custom grid-row values with bracket notation

Source: https://tailwindcss.com/docs/grid-row

Use bracket notation like row-[<value>], row-span-[<value>], row-start-[<value>], and row-end-[<value>] to apply completely custom CSS values. Supports arbitrary values for advanced grid configurations.

```html
<div class="row-[span_16_/_span_16] ...">
  <!-- ... -->
</div>
```

--------------------------------

### CSS custom properties with row utilities

Source: https://tailwindcss.com/docs/grid-row

Use the row-(<custom-property>) syntax as shorthand for row-[var(<custom-property>)] to reference CSS custom properties. The var() function is automatically applied, enabling dynamic grid row configurations.

```html
<div class="row-(--my-rows) ...">
  <!-- ... -->
</div>
```

--------------------------------

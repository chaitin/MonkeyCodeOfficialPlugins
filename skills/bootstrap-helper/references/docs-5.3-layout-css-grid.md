### Column Start Alignment with CSS Grid

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Utilize start classes like `.g-start-2` in conjunction with column classes (e.g., `.g-col-3`) to define the starting column for grid items. These classes correspond to the `grid-column-start` CSS property, with values starting from 1.

```html
<div class="grid text-center">
  <div class="g-col-3 g-start-2">.g-col-3 .g-start-2</div>
  <div class="g-col-4 g-start-6">.g-col-4 .g-start-6</div>
</div>
```

--------------------------------

### Bootstrap Grid: Adding Rows and Customizing Placement

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Demonstrates how to define the number of rows and control column placement within those rows using CSS variables and grid positioning. This example sets 3 rows and 3 columns.

```html
<div class="grid text-center" style="--bs-rows: 3; --bs-columns: 3;">
  <div>Auto-column</div>
  <div class="g-start-2" style="grid-row: 2">Auto-column</div>
  <div class="g-start-3" style="grid-row: 3">Auto-column</div>
</div>
```

--------------------------------

### Bootstrap Grid: Customizing Columns and Gaps

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Shows how to adjust both the number of columns and the gap size between grid items using CSS variables. This example sets 4 columns and a large gap.

```html
<div class="grid text-center" style="--bs-columns: 4; --bs-gap: 5rem;">
  <div class="g-col-2">.g-col-2</div>
  <div class="g-col-2">.g-col-2</div>
</div>
```

--------------------------------

### Bootstrap Grid: Customizing Columns with CSS Variables

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Demonstrates how to customize the number of columns in a grid using the `--bs-columns` CSS variable. This example sets the grid to have 3 columns.

```html
<div class="grid text-center" style="--bs-columns: 3;">
  <div>Auto-column</div>
  <div>Auto-column</div>
  <div>Auto-column</div>
</div>
```

--------------------------------

### Bootstrap Grid: Auto Columns Example

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Demonstrates how grid items automatically size to one column when no specific column classes are applied. This is the default behavior for immediate children of a `.grid` container.

```html
<div class="grid text-center">
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
  <div>1</div>
</div>
```

--------------------------------

### Bootstrap Grid: Modifying Vertical Gaps

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Shows how to specifically adjust the vertical gap between grid rows using the `row-gap` property. This example sets the vertical gap to 0.

```html
<div class="grid text-center" style="row-gap: 0;">
  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-6">.g-col-6</div>

  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-6">.g-col-6</div>
</div>
```

--------------------------------

### Bootstrap Grid: Customizing Columns and Gaps (Mixed Widths)

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Illustrates customizing the number of columns and gap size while using mixed column widths. This example uses 10 columns and a 1rem gap with `.g-col-6` and `.g-col-4` classes.

```html
<div class="grid text-center" style="--bs-columns: 10; --bs-gap: 1rem;">
  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-4">.g-col-4</div>
</div>
```

--------------------------------

### Customize Bootstrap Sass Grid with HTML Example

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Demonstrates how to customize the Bootstrap Sass Grid by setting CSS variables for column count and gap size directly in HTML. This allows for dynamic adjustments without recompiling Sass.

```html
<div class="grid text-center" style="--bs-columns: 18; --bs-gap: .5rem;">
  <div style="grid-column: span 14;">14 columns</div>
  <div class="g-col-4">.g-col-4</div>
</div>
```

--------------------------------

### Two Column Layout with CSS Grid

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Create a simple two-column layout that spans all viewports using the `.grid` and `.g-col-6` classes. This demonstrates a basic responsive setup where each column occupies half the available width.

```html
<div class="grid text-center">
  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-6">.g-col-6</div>
</div>
```

--------------------------------

### Bootstrap Grid: Customizing Horizontal and Vertical Gaps

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Illustrates how to set different horizontal and vertical gaps using the `--bs-gap` CSS variable with a pair of values. This example sets a small vertical gap and a larger horizontal gap.

```html
<div class="grid text-center" style="--bs-gap: .25rem 1rem;">
  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-6">.g-col-6</div>

  <div class="g-col-6">.g-col-6</div>
  <div class="g-col-6">.g-col-6</div>
</div>
```

--------------------------------

### Responsive Columns with CSS Grid

Source: https://getbootstrap.com/docs/5.3/layout/css-grid

Implement responsive column layouts by combining viewport-specific classes like `.g-col-6` and `.g-col-md-4`. This allows the layout to adapt across different screen sizes, starting with two columns and expanding to three on medium viewports and above.

```html
<div class="grid text-center">
  <div class="g-col-6 g-col-md-4">.g-col-6 .g-col-md-4</div>
  <div class="g-col-6 g-col-md-4">.g-col-6 .g-col-md-4</div>
  <div class="g-col-6 g-col-md-4">.g-col-6 .g-col-md-4</div>
</div>
```

--------------------------------

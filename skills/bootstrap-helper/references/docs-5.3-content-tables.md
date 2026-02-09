### Bootstrap Striped and Hoverable Table

Source: https://getbootstrap.com/docs/5.3/content/tables

An example of a Bootstrap table that combines striped rows with hoverable rows for enhanced readability and interactivity. This uses both `.table-striped` and `.table-hover` classes.

```html
<table class="table table-striped table-hover">
  ...
</table>
```

--------------------------------

### Bootstrap Bordered Table

Source: https://getbootstrap.com/docs/5.3/content/tables

An example of a Bootstrap table with borders applied to all sides of the table and its cells using the `.table-bordered` class. This provides a clear visual separation for table content.

```html
<table class="table table-bordered">
  ...
</table>
```

--------------------------------

### Bootstrap Table: Nesting Tables

Source: https://getbootstrap.com/docs/5.3/content/tables

Explains how Bootstrap handles nested tables, noting that border styles, active styles, and table variants are not inherited. The example shows a nested table within a larger table structure. Bootstrap's CSS uses a child combinator (`>`) to prevent style leakage to nested tables.

```html
<table class="table table-striped table-bordered">
  <thead>
    ...
  </thead>
  <tbody>
    ...
    <tr>
      <td colspan="4">
        <table class="table mb-0">
          ...
        </table>
      </td>
    </tr>
    ...
  </tbody>
</table>
```

--------------------------------

### Bootstrap Table: Small Tables

Source: https://getbootstrap.com/docs/5.3/content/tables

Shows how to make Bootstrap tables more compact using the `.table-sm` class. This class reduces the cell padding by half, resulting in a smaller, more condensed table. It is applicable to both light and dark table themes.

```html
<table class="table table-sm">
  ...
</table>
```

```html
<table class="table table-dark table-sm">
  ...
</table>
```

--------------------------------

### Bootstrap Table Variants and Row/Cell Coloring

Source: https://getbootstrap.com/docs/5.3/content/tables

Demonstrates how to apply contextual classes to color entire tables, specific rows, or individual cells. These classes include `.table-primary`, `.table-secondary`, `.table-success`, `.table-danger`, `.table-warning`, `.table-info`, `.table-light`, and `.table-dark`. These styles are purely CSS-based.

```html
<!-- On tables -->
<table class="table-primary">...</table>
<table class="table-secondary">...</table>
<table class="table-success">...</table>
<table class="table-danger">...</table>
<table class="table-warning">...</table>
<table class="table-info">...</table>
<table class="table-light">...</table>
<table class="table-dark">...</table>

<!-- On rows -->
<tr class="table-primary">...</tr>
<tr class="table-secondary">...</tr>
<tr class="table-success">...</tr>
<tr class="table-danger">...</tr>
<tr class="table-warning">...</tr>
<tr class="table-info">...</tr>
<tr class="table-light">...</tr>
<tr class="table-dark">...</tr>

<!-- On cells (td or th) -->
<tr>
  <td class="table-primary">...</td>
  <td class="table-secondary">...</td>
  <td class="table-success">...</td>
  <td class="table-danger">...</td>
  <td class="table-warning">...</td>
  <td class="table-info">...</td>
  <td class="table-light">...</td>
  <td class="table-dark">...</td>
</tr>
```

--------------------------------

### Bootstrap Responsive Table

Source: https://getbootstrap.com/docs/5.3/content/tables

Demonstrates how to make Bootstrap tables horizontally scrollable across all viewports using the `.table-responsive` wrapper class.

```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>
```

--------------------------------

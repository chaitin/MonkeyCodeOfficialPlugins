### Bootstrap Row Columns Examples (HTML)

Source: https://getbootstrap.com/docs/5.3/layout/grid

Demonstrates how to use responsive `.row-cols-*` classes on a parent `.row` to control the number of columns displayed. These classes provide a shortcut for creating basic grid and card layouts.

```html
<div class="container text-center">
  <div class="row row-cols-2">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

```html
<div class="container text-center">
  <div class="row row-cols-3">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

```html
<div class="container text-center">
  <div class="row row-cols-auto">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

```html
<div class="container text-center">
  <div class="row row-cols-4">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

```html
<div class="container text-center">
  <div class="row row-cols-4">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col-6">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

```html
<div class="container text-center">
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
  </div>
</div>
```

--------------------------------

### Basic Grid Layout Example (HTML)

Source: https://getbootstrap.com/docs/5.3/layout/grid

This HTML snippet demonstrates a basic Bootstrap grid layout with a container, a row, and three equal-width columns. It utilizes predefined Bootstrap classes to create a responsive structure that centers content.

```html
<div class="container text-center">
  <div class="row">
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Grid Nesting Example (HTML)

Source: https://getbootstrap.com/docs/5.3/layout/grid

Illustrates how to nest columns within existing columns by adding a new `.row` and `.col-sm-*` classes. Nested rows should have columns that sum up to 12 or fewer.

```html
<div class="container text-center">
  <div class="row">
    <div class="col-sm-3">
      Level 1: .col-sm-3
    </div>
    <div class="col-sm-9">
      <div class="row">
        <div class="col-8 col-sm-6">
          Level 2: .col-8 .col-sm-6
        </div>
        <div class="col-4 col-sm-6">
          Level 2: .col-4 .col-sm-6
        </div>
      </div>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap: Responsive Grid Classes - Mix and Match

Source: https://getbootstrap.com/docs/5.3/layout/grid

Provides examples of combining different Bootstrap grid classes across various breakpoints to create complex responsive layouts. This allows columns to stack, resize, or maintain fixed widths as needed on different devices.

```html
<div class="container text-center">
  <!-- Stack the columns on mobile by making one full-width and the other half-width -->
  <div class="row">
    <div class="col-md-8">.col-md-8</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  </div>

  <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
  <div class="row">
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  </div>

  <!-- Columns are always 50% wide, on mobile and desktop -->
  <div class="row">
    <div class="col-6">.col-6</div>
    <div class="col-6">.col-6</div>
  </div>
</div>
```

--------------------------------

### Bootstrap Grid Layout HTML Structure

Source: https://getbootstrap.com/docs/5.3/layout/grid

The HTML structure corresponding to the Sass mixin example, showing how div elements with specific classes are used to create the grid layout.

```html
<div class="example-container">
  <div class="example-row">
    <div class="example-content-main">Main content</div>
    <div class="example-content-secondary">Secondary content</div>
  </div>
</div>
```

--------------------------------

### Bootstrap: Variable Width Content Columns

Source: https://getbootstrap.com/docs/5.3/layout/grid

Shows how to size columns based on their natural content width using `col-{breakpoint}-auto` classes. This is useful for elements that should take up only the space they need, allowing other columns to adjust accordingly. The example includes centering content with `justify-content-md-center`.

```html
<div class="container text-center">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap: Responsive Grid Classes - All Breakpoints

Source: https://getbootstrap.com/docs/5.3/layout/grid

Demonstrates using `.col` and `.col-*` classes for layouts that remain consistent across all device sizes, from extra-small to extra-large. It shows how to create rows with equally divided columns or specify widths for particular columns.

```html
<div class="container text-center">
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col-8">col-8</div>
    <div class="col-4">col-4</div>
  </div>
</div>
```

--------------------------------

### Bootstrap: Create Equal-Width Columns

Source: https://getbootstrap.com/docs/5.3/layout/grid

Demonstrates how to create columns that automatically share equal width within a row. This is achieved by using the `.col` class without any specific width indicators, allowing Bootstrap's flexbox grid to distribute space evenly. Applicable to all device sizes.

```html
<div class="container text-center">
  <div class="row">
    <div class="col">
      1 of 2
    </div>
    <div class="col">
      2 of 2
    </div>
  </div>
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col">
      2 of 3
    </div>
    <div class="col">
      3 of 3
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap: Responsive Grid Classes - Stacked to Horizontal

Source: https://getbootstrap.com/docs/5.3/layout/grid

Illustrates how to create a grid that stacks vertically on smaller screens and becomes horizontal at the small breakpoint (`sm`). This is achieved using `.col-sm-*` classes, allowing for a mobile-first responsive design approach.

```html
<div class="container text-center">
  <div class="row">
    <div class="col-sm-8">col-sm-8</div>
    <div class="col-sm-4">col-sm-4</div>
  </div>
  <div class="row">
    <div class="col-sm">col-sm</div>
    <div class="col-sm">col-sm</div>
    <div class="col-sm">col-sm</div>
  </div>
</div>
```

--------------------------------

### Bootstrap Grid Layout with Mixins (Sass)

Source: https://getbootstrap.com/docs/5.3/layout/grid

Demonstrates creating a two-column layout using Bootstrap's Sass mixins. It defines container, row, and column styles, including responsive adjustments for different screen sizes.

```scss
.example-container {
  @include make-container();
  // Make sure to define this width after the mixin to override
  // `width: 100%` generated by `make-container()`
  width: 800px;
}

.example-row {
  @include make-row();
}

.example-content-main {
  @include make-col-ready();

  @include media-breakpoint-up(sm) {
    @include make-col(6);
  }
  @include media-breakpoint-up(lg) {
    @include make-col(8);
  }
}

.example-content-secondary {
  @include make-col-ready();

  @include media-breakpoint-up(sm) {
    @include make-col(6);
  }
  @include media-breakpoint-up(lg) {
    @include make-col(4);
  }
}
```

--------------------------------

### Customizing Bootstrap Grid Tiers (Sass)

Source: https://getbootstrap.com/docs/5.3/layout/grid

Illustrates how to customize the responsive breakpoints and container maximum widths for the Bootstrap grid system. This allows for a custom number of grid tiers tailored to specific design needs.

```scss
$grid-breakpoints: (
  xs: 0,
  sm: 480px,
  md: 768px,
  lg: 1024px
);

$container-max-widths: (
  sm: 420px,
  md: 720px,
  lg: 960px
);
```

--------------------------------

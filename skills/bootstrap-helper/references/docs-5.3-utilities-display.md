### Bootstrap HTML: Inline Display Example

Source: https://getbootstrap.com/docs/5.3/utilities/display

Demonstrates how to use the `d-inline` class to make elements display as inline. This example shows two inline elements with different background colors.

```html
<div class="d-inline p-2 text-bg-primary">d-inline</div>
<div class="d-inline p-2 text-bg-dark">d-inline</div>
```

--------------------------------

### Bootstrap HTML: Responsive Hiding Example

Source: https://getbootstrap.com/docs/5.3/utilities/display

Shows how to hide elements on specific screen sizes using Bootstrap's responsive display utilities. This example demonstrates hiding an element on large screens and larger, and hiding it on screens smaller than large.

```html
<div class="d-lg-none">hide on lg and wider screens</div>
<div class="d-none d-lg-block">hide on screens smaller than lg</div>
```

--------------------------------

### Bootstrap HTML: Print Display Examples

Source: https://getbootstrap.com/docs/5.3/utilities/display

Demonstrates how to control element display specifically for printing using Bootstrap's print display utility classes. This includes examples for hiding on print, showing only on print, and hiding on screen while showing on print.

```html
<div class="d-print-none">Screen Only (Hide on print only)</div>
<div class="d-none d-print-block">Print Only (Hide on screen only)</div>
<div class="d-none d-lg-block d-print-block">Hide up to large on screen, but always show on print</div>
```

--------------------------------

### Bootstrap HTML: Block Display Example

Source: https://getbootstrap.com/docs/5.3/utilities/display

Illustrates the use of the `d-block` class to make elements display as block-level. This example uses `span` elements to show block display behavior with different background colors.

```html
<span class="d-block p-2 text-bg-primary">d-block</span>
<span class="d-block p-2 text-bg-dark">d-block</span>
```

--------------------------------

### Bootstrap SCSS: Display Utilities API Configuration

Source: https://getbootstrap.com/docs/5.3/utilities/display

This SCSS code snippet shows the configuration for display utilities within Bootstrap's utilities API. It defines properties like responsiveness, print support, the CSS property, class prefix, and supported values.

```scss
"display": (
  responsive: true,
  print: true,
  property: display,
  class: d,
  values: inline inline-block block grid inline-grid table table-row table-cell flex inline-flex none
),
```

--------------------------------

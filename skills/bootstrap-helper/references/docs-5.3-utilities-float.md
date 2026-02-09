### Sass Utilities API for Floats

Source: https://getbootstrap.com/docs/5.3/utilities/float

Shows the configuration for Bootstrap's float utilities within the Sass `_utilities.scss` file. This demonstrates how the `float` property is defined with responsive options and specific values like `start`, `end`, and `none`.

```scss
"float": (
  responsive: true,
  property: float,
  values: (
    start: left,
    end: right,
    none: none,
  )
),
```

--------------------------------

### Responsive Float Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/float

Illustrates how to use responsive variations of Bootstrap's float utility classes (e.g., `.float-sm-end`, `.float-md-end`) to control element alignment at specific viewport sizes. These classes allow for dynamic layout adjustments across different devices.

```html
<div class="float-sm-end">Float end on viewports sized SM (small) or wider</div><br>
<div class="float-md-end">Float end on viewports sized MD (medium) or wider</div><br>
<div class="float-lg-end">Float end on viewports sized LG (large) or wider</div><br>
<div class="float-xl-end">Float end on viewports sized XL (extra large) or wider</div><br>
<div class="float-xxl-end">Float end on viewports sized XXL (extra extra large) or wider</div><br>
```

--------------------------------

### Basic Float Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/float

Demonstrates the basic usage of Bootstrap's float utility classes (`.float-start`, `.float-end`, `.float-none`) to control element alignment. These classes apply the CSS `float` property and are ready to use in HTML.

```html
<div class="float-start">Float start on all viewport sizes</div><br>
<div class="float-end">Float end on all viewport sizes</div><br>
<div class="float-none">Don’t float on all viewport sizes</div>
```

--------------------------------

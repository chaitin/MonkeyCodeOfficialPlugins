### Bootstrap Viewport Sizing Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/sizing

Provides examples of Bootstrap utility classes for setting element dimensions relative to the viewport. Includes `min-vw-100`, `min-vh-100`, `vw-100`, and `vh-100` for minimum and full viewport width/height.

```html
<div class="min-vw-100">Min-width 100vw</div>
<div class="min-vh-100">Min-height 100vh</div>
<div class="vw-100">Width 100vw</div>
<div class="vh-100">Height 100vh</div>
```

--------------------------------

### Bootstrap Sizing Utilities SCSS Configuration

Source: https://getbootstrap.com/docs/5.3/utilities/sizing

The SCSS source code defining Bootstrap's sizing utilities via the utilities API. This configuration file (`_utilities.scss`) specifies properties, classes, and values for width, max-width, viewport-width, height, and max-height.

```scss
"width": (
  "property": width,
  "class": w,
  "values": (
    25: 25%,
    50: 50%,
    75: 75%,
    100: 100%,
    auto: auto
  )
),
"max-width": (
  "property": max-width,
  "class": mw,
  "values": (100: 100%)
),
"viewport-width": (
  "property": width,
  "class": vw,
  "values": (100: 100vw)
),
"min-viewport-width": (
  "property": min-width,
  "class": min-vw,
  "values": (100: 100vw)
),
"height": (
  "property": height,
  "class": h,
  "values": (
    25: 25%,
    50: 50%,
    75: 75%,
    100: 100%,
    auto: auto
  )
),
"max-height": (
  "property": max-height,
  "class": mh,
  "values": (100: 100%)
),
"viewport-height": (
  "property": height,
  "class": vh,
  "values": (100: 100vh)
),
"min-viewport-height": (
  "property": min-height,
  "class": min-vh,
  "values": (100: 100vh)
),
```

--------------------------------

### Bootstrap Width Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/sizing

Demonstrates how to use Bootstrap's predefined width utility classes (w-25, w-50, w-75, w-100, w-auto) to set element widths. These classes are derived from the utility API in `_utilities.scss`.

```html
<div class="w-25 p-3">Width 25%</div>
<div class="w-50 p-3">Width 50%</div>
<div class="w-75 p-3">Width 75%</div>
<div class="w-100 p-3">Width 100%</div>
<div class="w-auto p-3">Width auto</div>
```

--------------------------------

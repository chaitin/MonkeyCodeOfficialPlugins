### Add, Remove, and Modify Utilities with map-merge()

Source: https://getbootstrap.com/docs/5.3/utilities/api

Illustrates a comprehensive customization of the utilities map using `map-merge()`. This example demonstrates removing a utility ('width'), making an existing utility ('border') responsive, and adding a new utility ('cursor') with its properties and values.

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

$utilities: map-merge(
  $utilities,
  (
    // Remove the `width` utility
    "width": null,
    // Make an existing utility responsive
    "border": map-merge(
      map-get($utilities, "border"),
      ( responsive: true ),
    ),
    // Add new utilities
    "cursor": (
      property: cursor,
      class: cursor,
      responsive: true,
      values: auto pointer grab,
    )
  )
);

@import "bootstrap/scss/utilities/api";

```

--------------------------------

### Rename Bootstrap Utility Classes with Sass

Source: https://getbootstrap.com/docs/5.3/utilities/api

Demonstrates how to rename existing Bootstrap utility classes using the Utilities API. This example renames the `margin-start` utilities (e.g., `.ms-*`) to `.ml-*`.

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

$utilities: map-merge(
  $utilities,
  (
    "margin-start": map-merge(
      map-get($utilities, "margin-start"),
      ( class: ml ),
    ),
  )
);

@import "bootstrap/scss/utilities/api";

```

--------------------------------

### Enable Responsive Variations for Bootstrap Utilities with Sass

Source: https://getbootstrap.com/docs/5.3/utilities/api

Shows how to enable responsive variations for Bootstrap utilities that are not responsive by default, using `map-merge` on the `$utilities` map. This example makes the `border` utility responsive.

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

$utilities: map-merge(
  $utilities,
  (
    "border": map-merge(
      map-get($utilities, "border"),
      ( responsive: true )
    ),
  )
);

@import "bootstrap/scss/utilities/api";

```

--------------------------------

### Add Custom Bootstrap Utilities with Sass

Source: https://getbootstrap.com/docs/5.3/utilities/api

Explains how to add new custom utility classes to Bootstrap using `map-merge` on the `$utilities` variable. This example adds a responsive `cursor` utility with specific values.

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

$utilities: map-merge(
  $utilities,
  (
    "cursor": (
      property: cursor,
      class: cursor,
      responsive: true,
      values: auto pointer grab,
    )
  )
);

@import "bootstrap/scss/utilities/api";

```

--------------------------------

### Override Bootstrap Utilities with Sass

Source: https://getbootstrap.com/docs/5.3/utilities/api

Demonstrates how to override existing Bootstrap utilities by redefining them within the `$utilities` Sass map. This example shows how to add responsive overflow utility classes.

```scss
$utilities: (
  "overflow": (
    responsive: true,
    property: overflow,
    values: visible hidden scroll auto,
  ),
);
```

--------------------------------

### Generate Visibility Utilities with Sass (Null Class)

Source: https://getbootstrap.com/docs/5.3/utilities/api

This Sass example shows how to generate visibility utility classes where the class name is directly derived from the value key when `class: null`. It generates `.visible` and `.invisible` classes.

```sass
$utilities: (
  "visibility": (
    property: visibility,
    class: null,
    values: (
      visible: visible,
      invisible: hidden,
    )
  )
);

```

--------------------------------

### Generate Responsive Utilities Across Breakpoints

Source: https://getbootstrap.com/docs/5.3/utilities/api

Setting the `responsive` boolean option to `true` generates responsive utility classes for all defined breakpoints. These utilities, like `.opacity-md-25`, allow for style adjustments at different screen sizes.

```scss
$utilities: (
  "opacity": (
    property: opacity,
    responsive: true,
    values: (
      0: 0,
      25: .25,
      50: .5,
      75: .75,
      100: 1
    )
  )
);
```

--------------------------------

### Generate Local CSS Variables for Utility Rulesets

Source: https://getbootstrap.com/docs/5.3/utilities/api

Use the `local-vars` option to define Sass map that generates local CSS variables within a utility class's ruleset. This requires careful consumption of these variables in the generated CSS. The example shows setting `--bs-bg-opacity` for `.bg-*` utilities.

```scss
$utilities: (
  "background-color": (
    property: background-color,
    class: bg,
    local-vars: (
      "bg-opacity": 1
    ),
    values: map-merge(
      $utilities-bg-colors,
      (
        "transparent": transparent
      )
    )
  )
);
```

--------------------------------

### Generate Print-Specific Utility Classes

Source: https://getbootstrap.com/docs/5.3/utilities/api

The `print` option enables the generation of utility classes that are exclusively applied within the `@media print` media query. This allows for distinct styling when content is printed, as demonstrated with the `.opacity-print-*` classes.

```scss
$utilities: (
  "opacity": (
    property: opacity,
    print: true,
    values: (
      0: 0,
      25: .25,
      50: .5,
      75: .75,
      100: 1
    )
  )
);
```

--------------------------------

### Utility API Configuration

Source: https://getbootstrap.com/docs/5.3/utilities/api

This section explains the configuration options for the Utility API, which uses Sass maps to define utility classes.

```APIDOC
## Utility API Configuration

The Utility API allows for the generation of utility classes using Sass maps and functions. The core of this API is the `$utilities` map, which can be extended with your custom configurations.

--------------------------------

### Generate Pseudo-Class Variations with States Option

Source: https://getbootstrap.com/docs/5.3/utilities/api

The `state` option in the Utilities API generates pseudo-class variations for utilities. By providing a state like `:hover` or `:focus`, class names are created that apply styles only when that pseudo-class is active. Multiple pseudo-classes can be specified using a space-separated list.

```scss
$utilities: (
  "opacity": (
    property: opacity,
    class: opacity,
    state: hover,
    values: (
      0: 0,
      25: .25,
      50: .5,
      75: .75,
      100: 1
    )
  )
);
```

--------------------------------

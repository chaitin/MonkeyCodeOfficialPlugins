### Set Border Width using Bootstrap Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/borders

Provides examples of how to set the width of borders on an element using Bootstrap's `.border-*` width utility classes, ranging from 1 to 5.

```html
<span class="border border-1"></span>
<span class="border border-2"></span>
<span class="border border-3"></span>
<span class="border border-4"></span>
<span class="border border-5"></span>
```

--------------------------------

### Add or Remove Borders using Bootstrap Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/borders

Demonstrates how to use Bootstrap's border utility classes to add borders to all sides or specific sides (top, end, bottom, start) of an element. It also shows how to remove borders using the `.border-0` class.

```html
<span class="border"></span>
<span class="border-top"></span>
<span class="border-end"></span>
<span class="border-bottom"></span>
<span class="border-start"></span>

<span class="border border-0"></span>
<span class="border border-top-0"></span>
<span class="border border-end-0"></span>
<span class="border border-bottom-0"></span>
<span class="border border-start-0"></span>
```

--------------------------------

### Control Border Opacity with Bootstrap Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/borders

Explains how to adjust the alpha transparency of borders using Bootstrap's `.border-opacity` utilities. It shows examples of default opacity and reduced opacity levels (75%, 50%, 25%, 10%) applied via utility classes or inline styles by overriding the `--bs-border-opacity` CSS variable.

```html
<div class="border border-success p-2 mb-2">This is default success border</div>
<div class="border border-success p-2" style="--bs-border-opacity: .5;">This is 50% opacity success border</div>

<div class="border border-success p-2 mb-2">This is default success border</div>
<div class="border border-success p-2 mb-2 border-opacity-75">This is 75% opacity success border</div>
<div class="border border-success p-2 mb-2 border-opacity-50">This is 50% opacity success border</div>
<div class="border border-success p-2 mb-2 border-opacity-25">This is 25% opacity success border</div>
<div class="border border-success p-2 border-opacity-10">This is 10% opacity success border</div>
```

--------------------------------

### Apply Border Radius with Sass Mixins (SCSS)

Source: https://getbootstrap.com/docs/5.3/utilities/borders

These Sass mixins allow for the application of border-radius to elements. They leverage variables like `$enable-rounded` and `$border-radius` for customization and support fallback values. The mixins target general border-radius as well as specific sides (top, bottom, start, end).

```scss
@mixin border-radius($radius: $border-radius, $fallback-border-radius: false) {
  @if $enable-rounded {
    border-radius: valid-radius($radius);
  } @else if $fallback-border-radius != false {
    border-radius: $fallback-border-radius;
  }
}

@mixin border-top-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-top-left-radius: valid-radius($radius);
    border-top-right-radius: valid-radius($radius);
  }
}

@mixin border-end-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-top-right-radius: valid-radius($radius);
    border-bottom-right-radius: valid-radius($radius);
  }
}

@mixin border-bottom-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-bottom-right-radius: valid-radius($radius);
    border-bottom-left-radius: valid-radius($radius);
  }
}

@mixin border-start-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-top-left-radius: valid-radius($radius);
    border-bottom-left-radius: valid-radius($radius);
  }
}

@mixin border-top-start-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-top-left-radius: valid-radius($radius);
  }
}

@mixin border-top-end-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-top-right-radius: valid-radius($radius);
  }
}

@mixin border-bottom-end-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-bottom-right-radius: valid-radius($radius);
  }
}

@mixin border-bottom-start-radius($radius: $border-radius) {
  @if $enable-rounded {
    border-bottom-left-radius: valid-radius($radius);
  }
}
```

--------------------------------

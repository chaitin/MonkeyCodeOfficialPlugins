### Bootstrap Sass Mixin for Creating Custom Containers

Source: https://getbootstrap.com/docs/5.3/layout/containers

Create your own custom containers using Bootstrap's Sass mixin. The `make-container` mixin sets the width, padding, and margins for a container element.

```scss
// Source mixin
@mixin make-container($padding-x: $container-padding-x) {
  width: 100%;
  padding-right: $padding-x;
  padding-left: $padding-x;
  margin-right: auto;
  margin-left: auto;
}

// Usage
.custom-container {
  @include make-container();
}

```

--------------------------------

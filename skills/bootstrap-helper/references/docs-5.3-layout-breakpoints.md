### Bootstrap Sass Media Query Mixins for Responsive Layouts

Source: https://getbootstrap.com/docs/5.3/layout/breakpoints

Illustrates the usage of Bootstrap's Sass mixins to apply styles based on minimum viewport widths. These mixins abstract the media query logic, allowing for cleaner and more maintainable responsive design code.

```scss
// Source mixins

// No media query necessary for xs breakpoint as it’s effectively `@media (min-width: 0) { ... }`
@include media-breakpoint-up(sm) { ... }
@include media-breakpoint-up(md) { ... }
@include media-breakpoint-up(lg) { ... }
@include media-breakpoint-up(xl) { ... }
@include media-breakpoint-up(xxl) { ... }

// Usage

// Example: Hide starting at `min-width: 0`, and then show at the `sm` breakpoint
.custom-class {
  display: none;
}
@include media-breakpoint-up(sm) {
  .custom-class {
    display: block;
  }
}
```

--------------------------------

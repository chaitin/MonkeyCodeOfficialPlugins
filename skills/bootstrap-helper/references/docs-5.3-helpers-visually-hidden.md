### SCSS: Use visually hidden mixins

Source: https://getbootstrap.com/docs/5.3/helpers/visually-hidden

Shows how to use the SCSS mixins `@include visually-hidden` and `@include visually-hidden-focusable` to apply the visually hidden styles. This allows for more flexible integration into custom SCSS structures, providing the same accessibility benefits.

```scss
// Usage as a mixin

.visually-hidden-title {
  @include visually-hidden;
}

.skip-navigation {
  @include visually-hidden-focusable;
}
```

--------------------------------

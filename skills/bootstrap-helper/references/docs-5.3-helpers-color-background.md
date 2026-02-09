### Apply Color and Background Utilities to Cards (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/color-background

Illustrates the application of Bootstrap's text and background color utilities to the `.card` component. This example demonstrates how to set a background color for the entire card and ensure readable text within its header and body.

```html
<div class="card text-bg-primary mb-3" style="max-width: 18rem;">
  <div class="card-header">Header</div>
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
  </div>
</div>
<div class="card text-bg-info mb-3" style="max-width: 18rem;">
  <div class="card-header">Header</div>
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
  </div>
</div>
```

--------------------------------

### Use Color and Background Utilities on Badges (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/color-background

Shows how to integrate Bootstrap's text and background color utilities with the `.badge` component. This allows for quick styling of badges with appropriate text contrast against their background.

```html
<span class="badge text-bg-primary">Primary</span>
<span class="badge text-bg-info">Info</span>
```

--------------------------------

### Apply Text and Background Colors with Contrast (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/color-background

Demonstrates how to apply contrasting text colors to background colors using Bootstrap's `.text-bg-*` utility classes. These classes automatically determine a suitable foreground color for a given background. This utility relies on Bootstrap's Sass `color-contrast()` function.

```html
<div class="text-bg-primary p-3">Primary with contrasting color</div>
<div class="text-bg-secondary p-3">Secondary with contrasting color</div>
<div class="text-bg-success p-3">Success with contrasting color</div>
<div class="text-bg-danger p-3">Danger with contrasting color</div>
<div class="text-bg-warning p-3">Warning with contrasting color</div>
<div class="text-bg-info p-3">Info with contrasting color</div>
<div class="text-bg-light p-3">Light with contrasting color</div>
<div class="text-bg-dark p-3">Dark with contrasting color</div>
```

--------------------------------

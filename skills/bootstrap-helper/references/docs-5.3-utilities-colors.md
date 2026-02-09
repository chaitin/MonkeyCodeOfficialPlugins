### Bootstrap Text Color CSS Variable Example (CSS)

Source: https://getbootstrap.com/docs/5.3/utilities/colors

Illustrates the CSS implementation of a Bootstrap text color utility, showing how CSS variables are used to manage color and opacity. This example focuses on `.text-primary`.

```css
.text-primary {
  --bs-text-opacity: 1;
  color: rgba(var(--bs-primary-rgb), var(--bs-text-opacity)) !important;
}
```

--------------------------------

### Bootstrap Text Opacity Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/colors

Demonstrates using predefined Bootstrap text opacity utility classes (`.text-opacity-*`) to apply specific transparency levels to text elements. These classes leverage CSS variables for real-time adjustments.

```html
<div class="text-primary">This is default primary text</div>
<div class="text-primary text-opacity-75">This is 75% opacity primary text</div>
<div class="text-primary text-opacity-50">This is 50% opacity primary text</div>
<div class="text-primary text-opacity-25">This is 25% opacity primary text</div>
```

--------------------------------

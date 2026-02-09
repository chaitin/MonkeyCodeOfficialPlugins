### Basic Ratio Example (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/ratio

Demonstrates how to use the `.ratio` class with a predefined aspect ratio (16x9) to embed a YouTube video. The child element (iframe) is automatically sized by the parent `.ratio` class.

```html
<div class="ratio ratio-16x9">
  <iframe src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0" title="YouTube video" allowfullscreen></iframe>
</div>
```

--------------------------------

### Responsive Custom Aspect Ratio (SCSS)

Source: https://getbootstrap.com/docs/5.3/helpers/ratio

Provides an SCSS example demonstrating how to apply a custom aspect ratio (2x1) at a specific breakpoint (medium and up) while maintaining a default ratio (4x3) otherwise. This uses Bootstrap's media query mixins.

```scss
.ratio-4x3 {
  @include media-breakpoint-up(md) {
    --bs-aspect-ratio: 50%; // 2x1
  }
}
```

--------------------------------

### Predefined Aspect Ratios (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/ratio

Shows examples of using different predefined aspect ratio modifier classes like `ratio-1x1`, `ratio-4x3`, `ratio-16x9`, and `ratio-21x9`. Each class sets a specific aspect ratio for the content within the `.ratio` container.

```html
<div class="ratio ratio-1x1">
  <div>1x1</div>
</div>
<div class="ratio ratio-4x3">
  <div>4x3</div>
</div>
<div class="ratio ratio-16x9">
  <div>16x9</div>
</div>
<div class="ratio ratio-21x9">
  <div>21x9</div>
</div>
```

--------------------------------

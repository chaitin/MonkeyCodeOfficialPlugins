### Styling Unstyled Lists with Tailwind CSS Utilities

Source: https://tailwindcss.com/docs/preflight

This HTML example demonstrates how to apply styling to an unstyled list using Tailwind CSS utility classes. The `list-inside` and `list-disc` classes are used to add disc-style bullets positioned inside the list items.

```html
<ul class="list-inside list-disc">
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

--------------------------------

### Overriding Block Display for Images with Tailwind CSS Utility

Source: https://tailwindcss.com/docs/preflight

This HTML example demonstrates how to override Preflight's default `display: block` for images. By adding the `inline` utility class, an image can be explicitly set to `display: inline`, allowing for different layout behaviors.

```html
<img class="inline" src="..." alt="..." />
```

--------------------------------

### Overriding Image Width Constraint with Tailwind CSS Utility

Source: https://tailwindcss.com/docs/preflight

This HTML example shows how to override Preflight's default image width constraint using the `max-w-none` utility class. This allows an image to exceed its parent's width if necessary, bypassing the `max-width: 100%` rule.

```html
<img class="max-w-none" src="..." alt="..." />
```

--------------------------------

### Resetting Default Margins and Padding with Preflight CSS

Source: https://tailwindcss.com/docs/preflight

This CSS rule, part of Tailwind's Preflight, resets the `margin` and `padding` to `0` for all elements and pseudo-elements. This ensures a consistent starting point by removing browser-default spacing and preventing accidental reliance on user-agent stylesheets.

```css
*,::after,::before,::backdrop,::file-selector-button {
  margin: 0;
  padding: 0;
}
```

--------------------------------

### Apply source() Modifier to Tailwind CSS Utilities Import (CSS)

Source: https://tailwindcss.com/docs/preflight

This example demonstrates how to apply the `source()` modifier to the `utilities.css` import in Tailwind CSS. The `source(none)` modifier specifically affects source detection for generated utilities, allowing control over how source maps or other source-related features behave in the build process.

```CSS
@layer theme, base, components, utilities;
@import "tailwindcss/theme.css" layer(theme);
@import "tailwindcss/utilities.css" layer(utilities);
@import "tailwindcss/utilities.css" layer(utilities) source(none);
```

--------------------------------

### Apply prefix(tw) Modifier to Tailwind CSS Theme and Utilities Imports (CSS)

Source: https://tailwindcss.com/docs/preflight

This example demonstrates applying the `prefix(tw)` modifier to both `theme.css` and `utilities.css` imports in Tailwind CSS. This modifier adds a custom prefix (e.g., `tw-`) to all generated utility classes and theme variables, effectively preventing naming conflicts with existing CSS in a project.

```CSS
@layer theme, base, components, utilities;
@import "tailwindcss/theme.css" layer(theme);
@import "tailwindcss/utilities.css" layer(utilities);
@import "tailwindcss/theme.css" layer(theme) prefix(tw);
@import "tailwindcss/utilities.css" layer(utilities) prefix(tw);
```

--------------------------------

### Overriding Preflight Border Reset for Third-Party Libraries in CSS

Source: https://tailwindcss.com/docs/preflight

This CSS example demonstrates how to override Preflight's default border reset for specific elements, such as those within a third-party library like Google Maps. By placing custom styles within the `@layer base` directive, it ensures that elements like `google-map *` regain their original border styles.

```css
@layer base {
  .google-map * {
    border-style: none;
  }
}
```

--------------------------------

### Unstyling Default List Elements with Preflight CSS

Source: https://tailwindcss.com/docs/preflight

This CSS snippet from Preflight removes default list styling, setting `list-style` to `none` for ordered, unordered, and menu lists. This ensures lists start without bullets or numbers, allowing for custom styling using Tailwind utilities.

```css
ol,ul,menu {
  list-style: none;
}
```

--------------------------------

### Constraining Images and Videos to Parent Width with Preflight CSS

Source: https://tailwindcss.com/docs/preflight

This CSS rule from Preflight ensures that images and videos are responsive by default. It sets `max-width: 100%` and `height: auto`, constraining them to their parent's width while preserving their intrinsic aspect ratio and preventing overflow.

```css
img,video {
  max-width: 100%;
  height: auto;
}
```

--------------------------------

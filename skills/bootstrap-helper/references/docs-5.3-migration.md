### Instantiate Bootstrap Plugins with CSS Selectors (JavaScript)

Source: https://getbootstrap.com/docs/5.3/migration

Demonstrates how to create new instances of Bootstrap JavaScript plugins by passing a CSS selector as the first argument. This allows for more flexible initialization compared to requiring a DOM element.

```javascript
const modal = new bootstrap.Modal('#myModal')
const dropdown = new bootstrap.Dropdown('[data-bs-toggle="dropdown"]')
```

--------------------------------

### Customize Bootstrap Text and Background Colors with Opacity Utilities

Source: https://getbootstrap.com/docs/5.3/migration

Bootstrap's `.text-*` and `.bg-*` utilities are now built with CSS variables and `rgba()` color values. Use the new text opacity and background opacity utilities to easily customize the transparency of these elements.

```html
<p class="text-primary">This is a primary text.</p>
<p class="text-primary-emphasis">This is a primary emphasis text.</p>
<p class="text-primary-50">This is a primary text with 50% opacity.</p>

<div class="bg-success">This is a success background.</div>
<div class="bg-success-emphasis">This is a success emphasis background.</div>
<div class="bg-success-50">This is a success background with 50% opacity.</div>
```

--------------------------------

### Create Layouts with Bootstrap Stack and Vertical Rule Helpers

Source: https://getbootstrap.com/docs/5.3/migration

Use Bootstrap's new stack helpers (`.hstack` for horizontal, `.vstack` for vertical) to quickly apply multiple flexbox properties for custom layouts. Add vertical dividers similar to `<hr>` elements using the `.vr` helper.

```html
<div class="hstack gap-3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="p-2">Third item</div>
</div>

<div class="vr"></div>

<div class="vstack gap-3">
  <div>First item</div>
  <div>Second item</div>
  <div>Third item</div>
</div>
```

--------------------------------

### Implement Bootstrap's New Placeholder Component

Source: https://getbootstrap.com/docs/5.3/migration

Utilize Bootstrap's new placeholder component to display temporary blocks of content, indicating that something is still loading. This component helps manage user expectations during loading states.

```html
<span class="placeholder col-6"></span>
```

--------------------------------

### Add Offcanvas Drawers to Bootstrap Navbars

Source: https://getbootstrap.com/docs/5.3/migration

Update Bootstrap navbars to support offcanvas drawers by using the responsive `.navbar-expand-*` classes and including the necessary offcanvas markup. This allows for collapsible side content within the navbar.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Offcanvas</h5>
        <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>
```

--------------------------------

### Customizing Sass Maps in Bootstrap Build

Source: https://getbootstrap.com/docs/5.3/migration

This snippet demonstrates how to customize Sass maps in a Bootstrap CSS build, specifically showing how to merge custom theme colors and override default maps. It requires the Bootstrap Sass files and assumes a standard build process.

```scss
// Functions come first
@import "functions";

// Optional variable overrides here
+ $custom-color: #df711b;
+ $custom-theme-colors: (
+   "custom": $custom-color
+ );

// Variables come next
@import "variables";

+ // Optional Sass map overrides here
+ $theme-colors: map-merge($theme-colors, $custom-theme-colors);
+
+ // Followed by our default maps
+ @import "maps";
+
// Rest of our imports
@import "mixins";
@import "utilities";
@import "root";
@import "reboot";
// etc

```

--------------------------------

### Bootstrap 5.0.0 Dependencies and Compiler Changes

Source: https://getbootstrap.com/docs/5.3/migration

Bootstrap 5.0.0 dropped jQuery as a dependency and upgraded from Popper v1.x to Popper v2.x. It also replaced Libsass with Dart Sass as the Sass compiler and migrated from Jekyll to Hugo for documentation building.

--------------------------------

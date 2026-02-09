### Bootstrap Dropdown Alignment Examples

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Demonstrates various dropdown alignment options in Bootstrap. Includes default, right-aligned, large alignments, dropstart, dropend, and dropup configurations. These examples utilize Bootstrap's CSS classes for styling and positioning.

```html
<div class="btn-group">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Right-aligned menu
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
    Left-aligned, right-aligned lg
  </button>
  <ul class="dropdown-menu dropdown-menu-lg-end">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
    Right-aligned, left-aligned lg
  </button>
  <ul class="dropdown-menu dropdown-menu-end dropdown-menu-lg-start">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group dropstart">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropstart
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group dropend">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropend
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropup
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>
```

--------------------------------

### Bootstrap Dropstart Dropdowns

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Illustrates how to create dropdown menus that trigger to the left of an element using the `.dropstart` class. Provides examples for both default and split button configurations.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Dropstart</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Default dropstart button -->
<div class="btn-group dropstart">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropstart
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>

<!-- Split dropstart button -->
<div class="btn-group dropstart">
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropstart</span>
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
  <button type="button" class="btn btn-secondary">
    Split dropstart
  </button>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

--------------------------------

### Bootstrap Dropdown Menu Text Example

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Demonstrates how to include freeform text within a Bootstrap dropdown menu. This example uses standard paragraph elements and applies Bootstrap's text and spacing utilities for formatting and constraining width.

```html
<div class="dropdown-menu p-4 text-body-secondary" style="max-width: 200px;">
  <p>
    Some example text that’s free-flowing within the dropdown menu.
  </p>
  <p class="mb-0">
    And this is more example text.
  </p>
</div>
```

--------------------------------

### Bootstrap Dropend Dropdowns

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Demonstrates how to create dropdown menus that trigger to the right of an element using the `.dropend` class. Includes examples for both default and split button configurations.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Dropend</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Default dropend button -->
<div class="btn-group dropend">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropend
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>

<!-- Split dropend button -->
<div class="btn-group dropend">
  <button type="button" class="btn btn-secondary">
    Split dropend
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropend</span>
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

--------------------------------

### Bootstrap Dropdown Positioning with Offset and Reference

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This snippet illustrates how to control the positioning of Bootstrap dropdowns. The 'Offset' example uses `data-bs-offset` to adjust the dropdown's position relative to its parent. The 'Reference Toggle Dropdown' example uses `data-bs-reference="parent"` to align the dropdown with its parent button group.

```html
<div class="d-flex">
  <div class="dropdown me-1">
    <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-offset="10,20">
      Offset
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
    </ul>
  </div>
  <div class="btn-group">
    <button type="button" class="btn btn-secondary">Reference</button>
    <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false" data-bs-reference="parent">
      <span class="visually-hidden">Toggle Dropdown</span>
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="#">Separated link</a></li>
    </ul>
  </div>
</div>
```

--------------------------------

### Bootstrap Dropdown Menu Header Example

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Shows how to add a header to a Bootstrap dropdown menu to label sections of actions. This uses the `dropdown-header` class for the header element.

```html
<ul class="dropdown-menu">
  <li><h6 class="dropdown-header">Dropdown header</h6></li>
  <li><a class="dropdown-item" href="#">Action</a></li>
  <li><a class="dropdown-item" href="#">Another action</a></li>
</ul>
```

--------------------------------

### Default and Split Dropup Buttons HTML

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Provides HTML examples for creating both standard and split dropup dropdown buttons. The `.dropup` class on the parent element positions the dropdown menu above the button. Useful for space-constrained interfaces.

```html
<!-- Default dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropup
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>

<!-- Split dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary">
    Split dropup
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>
```

--------------------------------

### Bootstrap Dropdown Menu Divider Example

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Illustrates how to use a divider to separate groups of related menu items in a Bootstrap dropdown. The `dropdown-divider` class is applied to an `<hr>` element.

```html
<ul class="dropdown-menu">
  <li><a class="dropdown-item" href="#">Action</a></li>
  <li><a class="dropdown-item" href="#">Another action</a></li>
  <li><a class="dropdown-item" href="#">Something else here</a></li>
  <li><hr class="dropdown-divider"></li>
  <li><a class="dropdown-item" href="#">Separated link</a></li>
</ul>
```

--------------------------------

### Bootstrap Dropdown Form Example

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This snippet demonstrates how to embed a form directly within a Bootstrap dropdown menu. It includes input fields for email and password, a remember me checkbox, and a sign-in button. Margin and padding utilities are used for spacing.

```html
<div class="dropdown-menu">
  <form class="px-4 py-3">
    <div class="mb-3">
      <label for="exampleDropdownFormEmail1" class="form-label">Email address</label>
      <input type="email" class="form-control" id="exampleDropdownFormEmail1" placeholder="email@example.com">
    </div>
    <div class="mb-3">
      <label for="exampleDropdownFormPassword1" class="form-label">Password</label>
      <input type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Password">
    </div>
    <div class="mb-3">
      <div class="form-check">
        <input type="checkbox" class="form-check-input" id="dropdownCheck">
        <label class="form-check-label" for="dropdownCheck">
          Remember me
        </label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Sign in</button>
  </form>
  <div class="dropdown-divider"></div>
  <a class="dropdown-item" href="#">New around here? Sign up</a>
  <a class="dropdown-item" href="#">Forgot password?</a>
</div>
```

--------------------------------

### Dark Dropdown in Navbar HTML

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Illustrates integrating a dark dropdown menu within a dark Bootstrap navbar. This example shows the structure for a navigation bar with a dropdown component that adopts dark styling.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
      <ul class="navbar-nav">
        <li class="nav-item dropdown">
          <button class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </button>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Dropdown with Link Trigger (HTML)

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This example shows how to create a Bootstrap dropdown using an anchor (<a>) tag as the toggle. It includes the `role="button"` attribute for better accessibility with screen readers. Similar to the button version, it requires Bootstrap's CSS and JavaScript.

```html
<div class="dropdown">
  <a class="btn btn-secondary dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown link
  </a>

  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

--------------------------------

### Bootstrap Dropdown Auto Close HTML Examples

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Demonstrates various Bootstrap dropdown configurations using the `data-bs-auto-close` attribute to control when the dropdown menu closes. Options include 'true' (default), 'inside', 'outside', and 'false' for manual closing.

```html
<div class="btn-group">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="true" aria-expanded="false">
    Default dropdown
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="inside" aria-expanded="false">
    Clickable inside
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false">
    Clickable outside
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>

<div class="btn-group">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="false" aria-expanded="false">
    Manual close
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
    <li><a class="dropdown-item" href="#">Menu item</a></li>
  </ul>
</div>
```

--------------------------------

### Bootstrap Large Split Button Dropdown (HTML)

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This example shows how to create a large-sized split button dropdown in Bootstrap. It utilizes the `.btn-lg` class on both the main and toggle buttons, along with the standard split button structure. The dropdown menu content is indicated by `...` for brevity.

```html
<div class="btn-group">
  <button class="btn btn-secondary btn-lg" type="button">
    Large split button
  </button>
  <button type="button" class="btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    ...
  </ul>
</div>
```

--------------------------------

### Bootstrap Dropdown Caret Sass Mixins

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Provides Sass mixins for generating CSS-based caret icons used to indicate dropdown interactivity. These mixins define the border properties for different caret directions (up, down, end, start) and a main `caret` mixin to apply them with customizable size and alignment. Found in `scss/mixins/_caret.scss`.

```scss
@mixin caret-down($width: $caret-width) {
  border-top: $width solid;
  border-right: $width solid transparent;
  border-bottom: 0;
  border-left: $width solid transparent;
}

@mixin caret-up($width: $caret-width) {
  border-top: 0;
  border-right: $width solid transparent;
  border-bottom: $width solid;
  border-left: $width solid transparent;
}

@mixin caret-end($width: $caret-width) {
  border-top: $width solid transparent;
  border-right: 0;
  border-bottom: $width solid transparent;
  border-left: $width solid;
}

@mixin caret-start($width: $caret-width) {
  border-top: $width solid transparent;
  border-right: $width solid;
  border-bottom: $width solid transparent;
}

@mixin caret(
  $direction: down,
  $width: $caret-width,
  $spacing: $caret-spacing,
  $vertical-align: $caret-vertical-align
) {
  @if $enable-caret {
    &::after {
      display: inline-block;
      margin-left: $spacing;
      vertical-align: $vertical-align;
      content: "";
      @if $direction == down {
        @include caret-down($width);
      } @else if $direction == up {
        @include caret-up($width);
      } @else if $direction == end {
        @include caret-end($width);
      }
    }

    @if $direction == start {
      &::after {
        display: none;
      }

      &::before {
        display: inline-block;
        margin-right: $spacing;
        vertical-align: $vertical-align;
        content: "";
        @include caret-start($width);
      }
    }

    &:empty::after {
      margin-left: 0;
    }
  }
}

```

--------------------------------

### Bootstrap Dropdown Menu Items

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Shows how to structure dropdown menu items using either `<a>` or `<button>` elements. Also demonstrates creating non-interactive text items with `.dropdown-item-text`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Dropdown Menu Items</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Dropdown with button items -->
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown
  </button>
  <ul class="dropdown-menu">
    <li><button class="dropdown-item" type="button">Action</button></li>
    <li><button class="dropdown-item" type="button">Another action</button></li>
    <li><button class="dropdown-item" type="button">Something else here</button></li>
  </ul>
</div>

<br><br>

<!-- Dropdown with link and text items -->
<ul class="dropdown-menu">
  <li><span class="dropdown-item-text">Dropdown item text</span></li>
  <li><a class="dropdown-item" href="#">Action</a></li>
  <li><a class="dropdown-item" href="#">Another action</a></li>
  <li><a class="dropdown-item" href="#">Something else here</a></li>
</ul>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

--------------------------------

### Bootstrap Dropdown with Form Trigger

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This example shows a Bootstrap dropdown that reveals a form when the toggle button is clicked. The form is placed inside the dropdown menu and uses Bootstrap's grid and form classes for layout and styling. The `data-bs-auto-close="outside"` attribute prevents the dropdown from closing when clicking inside the form.

```html
<div class="dropdown">
  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
    Dropdown form
  </button>
  <form class="dropdown-menu p-4">
    <div class="mb-3">
      <label for="exampleDropdownFormEmail2" class="form-label">Email address</label>
      <input type="email" class="form-control" id="exampleDropdownFormEmail2" placeholder="email@example.com">
    </div>
    <div class="mb-3">
      <label for="exampleDropdownFormPassword2" class="form-label">Password</label>
      <input type="password" class="form-control" id="exampleDropdownFormPassword2" placeholder="Password">
    </div>
    <div class="mb-3">
      <div class="form-check">
        <input type="checkbox" class="form-check-input" id="dropdownCheck2">
        <label class="form-check-label" for="dropdownCheck2">
          Remember me
        </label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Sign in</button>
  </form>
</div>
```

--------------------------------

### Dropdown Options

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Explore the various configuration options available for the Bootstrap Dropdown plugin, which can be set via data attributes or JavaScript.

```APIDOC
## Dropdown Options

--------------------------------

### Configure Dropdown with popperConfig (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

Demonstrates how to customize the Popper.js configuration for a Bootstrap dropdown. This allows for fine-grained control over the dropdown's positioning and behavior. The `popperConfig` function receives the default configuration and should return a new or modified configuration object.

```javascript
const dropdown = new bootstrap.Dropdown(element, {
  popperConfig(defaultBsPopperConfig) {
    // const newPopperConfig = {...}
    // use defaultBsPopperConfig if needed...
    // return newPopperConfig
  }
})
```

--------------------------------

### Initialize Bootstrap Dropdowns with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/dropdowns

This JavaScript code snippet demonstrates how to initialize Bootstrap dropdowns programmatically. It selects all elements with the class `.dropdown-toggle` and creates a new `bootstrap.Dropdown` instance for each, allowing for JavaScript-based control over dropdowns.

```javascript
const dropdownElementList = document.querySelectorAll('.dropdown-toggle')
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl))
```

--------------------------------

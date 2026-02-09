### Offcanvas Placement Examples (HTML)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

These HTML snippets showcase different placement options for Bootstrap's offcanvas component: top, right, and bottom. Each example includes a button to trigger the offcanvas and the corresponding offcanvas element with basic content.

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasTop" aria-controls="offcanvasTop">Toggle top offcanvas</button>

<div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvasTop" aria-labelledby="offcanvasTopLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasTopLabel">Offcanvas top</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    ...
  </div>
</div>
```

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Toggle right offcanvas</button>

<div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasRightLabel">Offcanvas right</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    ...
  </div>
</div>
```

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom">Toggle bottom offcanvas</button>

<div class="offcanvas offcanvas-bottom" tabindex="-1" id="offcanvasBottom" aria-labelledby="offcanvasBottomLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasBottomLabel">Offcanvas bottom</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body small">
    ...
  </div>
</div>
```

--------------------------------

### Bootstrap Offcanvas Live Demo with Triggers (HTML)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

This example shows how to trigger an Offcanvas component using either a link with an `href` attribute or a button with a `data-bs-target` attribute. Both methods require `data-bs-toggle="offcanvas"`. It also includes an example of a dropdown within the offcanvas body.

```html
<a class="btn btn-primary" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button" aria-controls="offcanvasExample">
  Link with href
</a>
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample">
  Button with data-bs-target
</button>

<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasExampleLabel">Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <div>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </div>
    <div class="dropdown mt-3">
      <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
        Dropdown button
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
      </ul>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Dark Offcanvas Example (Deprecated)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Illustrates how to create a dark-themed offcanvas. This example uses `.text-bg-dark` on the offcanvas element and `.btn-close-white` for the close button. Note: Dark variants are deprecated in v5.3.0; use `data-bs-theme="dark"` instead.

```html
<div class="offcanvas offcanvas-start show text-bg-dark" tabindex="-1" id="offcanvasDark" aria-labelledby="offcanvasDarkLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasDarkLabel">Offcanvas</h5>
    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvasDark" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>Place offcanvas content here.</p>
  </div>
</div>
```

--------------------------------

### Offcanvas Instance Creation

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Demonstrates how to create a new instance of the Offcanvas component using its constructor.

```APIDOC
## Offcanvas Instance Creation

--------------------------------

### Bootstrap Offcanvas Component Example (HTML)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

This snippet demonstrates a basic Offcanvas component in Bootstrap. It includes a header with a close button and a body for content. The `.show` class is applied to make it visible by default. It's designed to be a reusable sidebar element.

```html
<div class="offcanvas offcanvas-start show" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasLabel">Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.
  </div>
</div>
```

--------------------------------

### Create Bootstrap Offcanvas Instance (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Demonstrates how to create a new instance of the Bootstrap Offcanvas component using its constructor. This is typically done by selecting the target DOM element. The constructor accepts an optional options object for customization.

```javascript
const bsOffcanvas = new bootstrap.Offcanvas('#myOffcanvas')
```

--------------------------------

### Initialize Bootstrap Offcanvas with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Demonstrates how to manually initialize the Bootstrap offcanvas component using JavaScript. It selects all elements with the class `.offcanvas` and creates new `bootstrap.Offcanvas` instances for each, allowing programmatic control.

```javascript
const offcanvasElementList = document.querySelectorAll('.offcanvas')
const offcanvasList = [...offcanvasElementList].map(offcanvasEl => new bootstrap.Offcanvas(offcanvasEl))

```

--------------------------------

### Bootstrap Offcanvas with Scrolling and Backdrop

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

This example shows an offcanvas that enables both body scrolling and displays a visible backdrop. The `data-bs-scroll="true"` attribute allows the page to scroll, and the absence of `data-bs-backdrop="false"` means the default backdrop behavior (which is typically visible) is active.

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">Enable both scrolling & backdrop</button>

<div class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">Backdrop with scrolling</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>Try scrolling the rest of the page to see this option in action.</p>
  </div>
</div>
```

--------------------------------

### Bootstrap Offcanvas with Body Scrolling Example

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Demonstrates an offcanvas component that allows the rest of the page content to scroll while the offcanvas is open. It uses Bootstrap's data attributes for toggling and configuration. The `data-bs-scroll="true"` attribute enables body scrolling, and `data-bs-backdrop="false"` disables the backdrop.

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScrolling" aria-controls="offcanvasScrolling">Enable body scrolling</button>

<div class="offcanvas offcanvas-start" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasScrolling" aria-labelledby="offcanvasScrollingLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasScrollingLabel">Offcanvas with body scrolling</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>Try scrolling the rest of the page to see this option in action.</p>
  </div>
</div>
```

--------------------------------

### Offcanvas Methods

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Details the available methods for interacting with an Offcanvas instance, such as showing, hiding, toggling, disposing, and retrieving instances.

```APIDOC
## Offcanvas Methods

--------------------------------

### Dismiss Offcanvas Button (Outside)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

An example of a dismiss button placed outside the offcanvas element. It requires both `data-bs-dismiss="offcanvas"` and `data-bs-target` attributes to specify which offcanvas to close. This method does not fully adhere to ARIA dialog patterns.

```html
<button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#my-offcanvas" aria-label="Close"></button>

```

--------------------------------

### Dismiss Offcanvas Button (Inside)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

An example of a dismiss button placed inside the offcanvas element. It uses the `data-bs-dismiss="offcanvas"` attribute to trigger the JavaScript functionality for closing the offcanvas. The `btn-close` class provides default styling.

```html
<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>

```

--------------------------------

### Bootstrap Responsive Offcanvas Classes

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

Lists the available responsive offcanvas classes in Bootstrap, such as `.offcanvas-sm`, `.offcanvas-md`, etc. These classes allow an offcanvas to be hidden below a specified breakpoint and behave normally above it. To implement, replace the base `.offcanvas` class with a responsive variant.

```html
<!-- Example usage for a large breakpoint -->
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasResponsive" aria-controls="offcanvasResponsive">
  Toggle responsive offcanvas
</button>

<div class="offcanvas offcanvas-lg offcanvas-start" tabindex="-1" id="offcanvasResponsive" aria-labelledby="offcanvasResponsiveLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasResponsiveLabel">Responsive Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>This offcanvas is visible on large screens and up.</p>
  </div>
</div>
```

--------------------------------

### Responsive Offcanvas Toggle (HTML)

Source: https://getbootstrap.com/docs/5.3/components/offcanvas

This HTML snippet demonstrates how to create a responsive offcanvas component that is only visible on large screens and above. It includes a button to toggle the offcanvas and the offcanvas element itself with content.

```html
<button class="btn btn-primary d-lg-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasResponsive" aria-controls="offcanvasResponsive">Toggle offcanvas</button>

<div class="alert alert-info d-none d-lg-block">Resize your browser to show the responsive offcanvas toggle.</div>

<div class="offcanvas-lg offcanvas-end" tabindex="-1" id="offcanvasResponsive" aria-labelledby="offcanvasResponsiveLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasResponsiveLabel">Responsive offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvasResponsive" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p class="mb-0">This is content within an <code>.offcanvas-lg</code>.</p>
  </div>
</div>
```

--------------------------------

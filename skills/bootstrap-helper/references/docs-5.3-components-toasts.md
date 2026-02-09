### Bootstrap Live Toast Example with JavaScript Initialization

Source: https://getbootstrap.com/docs/5.3/components/toasts

This example shows how to create a live toast that can be shown on demand using a button click. It includes the necessary HTML for the button and the toast container, along with JavaScript to initialize the toast and handle its display. The toast is positioned in the lower right corner using Bootstrap utility classes.

```html
<button type="button" class="btn btn-primary" id="liveToastBtn">Show live toast</button>

<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="..." class="rounded me-2" alt="...">
      <strong class="me-auto">Bootstrap</strong>
      <small>11 mins ago</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
  </div>
</div>
```

```javascript
const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
  })
}
```

--------------------------------

### Get or Create Toast Instance with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/toasts

Shows how to get a Bootstrap toast instance or create a new one if it doesn't exist using the static `getOrCreateInstance` method. This is a convenient way to ensure you have a toast instance to work with.

```javascript
const myToastEl = document.getElementById('myToastEl');
const myToast = bootstrap.Toast.getOrCreateInstance(myToastEl);
```

--------------------------------

### Toast with Close Button and Autohide Disabled (HTML)

Source: https://getbootstrap.com/docs/5.3/components/toasts

Provides an example of a toast component configured with `data-bs-autohide="false"`, requiring a close button for user dismissal. This example includes standard toast header elements and the toast body content.

```html
<div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-bs-autohide="false">
  <div class="toast-header">
    <img src="..." class="rounded me-2" alt="...">
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
  <div class="toast-body">
    Hello, world! This is a toast message.
  </div>
</div>
```

--------------------------------

### Get Toast Instance with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/toasts

Demonstrates how to retrieve an existing Bootstrap toast instance associated with a DOM element using the static `getInstance` method. This is useful for interacting with an already initialized toast.

```javascript
const myToastEl = document.getElementById('myToastEl');
const myToast = bootstrap.Toast.getInstance(myToastEl);
```

--------------------------------

### Customizing Bootstrap Toasts: Simple Layout

Source: https://getbootstrap.com/docs/5.3/components/toasts

Shows how to create a simplified toast by removing the default header and using flex utilities for layout. This example uses Bootstrap Icons for a custom hide icon and adjusts alignment.

```html
<div class="toast align-items-center" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
    <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>
```

--------------------------------

### Customizing Bootstrap Toasts: With Actions

Source: https://getbootstrap.com/docs/5.3/components/toasts

Illustrates adding custom controls and components within a toast, such as action buttons. This example includes a primary action button and a secondary close button, along with a top border for separation.

```html
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-body">
    Hello, world! This is a toast message.
    <div class="mt-2 pt-2 border-top">
      <button type="button" class="btn btn-primary btn-sm">Take action</button>
      <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="toast">Close</button>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Toasts: Color Schemes with Utilities

Source: https://getbootstrap.com/docs/5.3/components/toasts

Demonstrates how to apply custom color schemes to toasts using Bootstrap's background and color utilities. This example uses `.text-bg-primary` for the toast background and `.btn-close-white` for the close button, removing the default border with `.border-0`.

```html
<div class="toast align-items-center text-bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>
```

--------------------------------

### Handle Toast Hidden Event with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/toasts

Provides an example of how to listen for the `hidden.bs.toast` event using JavaScript. This event fires after the toast has been completely hidden from the user, allowing for post-hide actions.

```javascript
const myToastEl = document.getElementById('myToast');
myToastEl.addEventListener('hidden.bs.toast', () => {
  // do something...
});
```

--------------------------------

### Initialize Bootstrap Toasts with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/toasts

Shows how to initialize Bootstrap toast components using JavaScript. It selects all elements with the class `.toast` and creates new `bootstrap.Toast` instances, optionally passing configuration options.

```javascript
const toastElList = document.querySelectorAll('.toast')
const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl, option))
```

--------------------------------

### Toast Options

Source: https://getbootstrap.com/docs/5.3/components/toasts

Explore the available options for configuring Bootstrap toasts, including how to set them via data attributes and JavaScript.

```APIDOC
## Toast Options

--------------------------------

### Stacking Toasts with Bootstrap Toast Container

Source: https://getbootstrap.com/docs/5.3/components/toasts

Demonstrates how to stack multiple toasts vertically by wrapping them in a `.toast-container`. This container automatically adds spacing between toasts. No specific JavaScript dependencies are required for basic stacking.

```html
<div class="toast-container position-static">
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="..." class="rounded me-2" alt="...">
      <strong class="me-auto">Bootstrap</strong>
      <small class="text-body-secondary">just now</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      See? Just like this.
    </div>
  </div>

  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="..." class="rounded me-2" alt="...">
      <strong class="me-auto">Bootstrap</strong>
      <small class="text-body-secondary">2 seconds ago</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      Heads up, toasts will stack automatically
    </div>
  </div>
</div>
```

--------------------------------

### Toast Methods

Source: https://getbootstrap.com/docs/5.3/components/toasts

Understand the available JavaScript methods for programmatically controlling Bootstrap toasts, such as showing, hiding, and checking their visibility.

```APIDOC
## Toast Methods

--------------------------------

### Toast Accessibility with aria-live and aria-atomic (HTML)

Source: https://getbootstrap.com/docs/5.3/components/toasts

Demonstrates how to make toasts accessible to screen readers by using `aria-live` and `aria-atomic` attributes. It ensures that toast content changes are announced and treated as a single unit. The live region must exist before the toast is generated.

```html
<div class="toast" role="alert" aria-live="polite" aria-atomic="true" data-bs-delay="10000">
  <div role="alert" aria-live="assertive" aria-atomic="true">...</div>
</div>
```

--------------------------------

### Configure Toast Options via Data Attributes

Source: https://getbootstrap.com/docs/5.3/components/toasts

Illustrates how to configure Bootstrap toast options using data attributes. Option names in camelCase (e.g., `customClass`) should be converted to kebab-case (e.g., `custom-class`) when used as data attributes (e.g., `data-bs-custom-class`).

```html
<div data-bs-animation="true" data-bs-autohide="false" data-bs-delay="5000">...</div>
```

--------------------------------

### Configure Toast with JSON Data Attribute

Source: https://getbootstrap.com/docs/5.3/components/toasts

Explains how to use the experimental `data-bs-config` attribute to pass configuration options as a JSON string to a Bootstrap toast. Individual data attributes can override values set within `data-bs-config`.

```html
<div data-bs-config='{"delay":0, "title":123}' data-bs-title="456">...</div>
```

--------------------------------

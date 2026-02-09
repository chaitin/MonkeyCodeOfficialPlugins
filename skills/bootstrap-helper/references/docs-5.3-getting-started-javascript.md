### Initialize Bootstrap tooltips with jQuery

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Shows how to initialize Bootstrap tooltips using jQuery, assuming Bootstrap detects jQuery in the `window` object. This example covers both default initialization and initialization with custom configuration options like `boundary` and `customClass`.

```javascript
// to enable tooltips with the default configuration
$('[data-bs-toggle="tooltip"]').tooltip()

// to initialize tooltips with given configuration
$('[data-bs-toggle="tooltip"]').tooltip({
  boundary: 'clippingParents',
  customClass: 'myClass'
})
```

--------------------------------

### Initialize Bootstrap Modal with Default and Custom Options

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Shows how to instantiate a Bootstrap modal component using its constructor. It covers initialization with default settings and with a custom configuration object, such as disabling keyboard interaction.

```javascript
const myModalEl = document.querySelector('#myModal')
const modal = new bootstrap.Modal(myModalEl) // initialized with defaults

const configObject = { keyboard: false }
const modal1 = new bootstrap.Modal(myModalEl, configObject) // initialized with no keyboard
```

--------------------------------

### Execute Action After Bootstrap Collapse Transition Completes

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

This example shows how to perform an action after a Bootstrap collapse component has finished its expansion transition by listening to the 'shown.bs.collapse' event.

```javascript
const myCollapseEl = document.querySelector('#myCollapse')

myCollapseEl.addEventListener('shown.bs.collapse', event => {
  // Action to execute once the collapsible area is expanded
})
```

--------------------------------

### Plugin Instance Methods

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Details the static methods `getInstance` and `getOrCreateInstance` for retrieving or creating plugin instances associated with DOM elements.

```APIDOC
## GET /websites/getbootstrap/plugin/instance/{elementId}

--------------------------------

### Get Bootstrap Plugin Instance using getInstance

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Demonstrates how to retrieve an existing instance of a Bootstrap plugin, like Popover, associated with a specific DOM element using the static `getInstance` method.

```javascript
bootstrap.Popover.getInstance(myPopoverEl)
```

--------------------------------

### Get or Create Bootstrap Plugin Instance using getOrCreateInstance

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Illustrates the use of `getOrCreateInstance` to obtain a Bootstrap plugin instance for a DOM element. If no instance exists, it creates a new one, optionally using a provided configuration object.

```javascript
bootstrap.Popover.getOrCreateInstance(myPopoverEl, configObject)
```

--------------------------------

### Using Bootstrap as an ES Module in the Browser

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

This example demonstrates how to use Bootstrap's JavaScript as an ES module directly in the browser. It requires including the 'es-module-shims' script and defining an 'importmap' to resolve module names to their respective CDN paths. This approach is useful for modern browsers that support ES modules.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <title>Hello, modularity!</title>
  </head>
  <body>
    <h1>Hello, modularity!</h1>
    <button id="popoverButton" type="button" class="btn btn-primary btn-lg" data-bs-toggle="popover" title="ESM in Browser" data-bs-content="Bang!">Custom popover</button>

    <script async src="https://cdn.jsdelivr.net/npm/es-module-shims@1/dist/es-module-shims.min.js" crossorigin="anonymous"></script>
    <script type="importmap">
    {
      "imports": {
        "@popperjs/core": "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/esm/popper.min.js",
        "bootstrap": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.esm.min.js"
      }
    }
    </script>
    <script type="module">
      import * as bootstrap from 'bootstrap'

      new bootstrap.Popover(document.getElementById('popoverButton'))
    </script>
  </body>
</html>

```

--------------------------------

### Modify default plugin settings in Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Shows how to change the default configuration for any Bootstrap plugin by directly modifying its `Constructor.Default` object. This example illustrates setting the `keyboard` option for the modal plugin to `false`.

```javascript
// changes default for the modal plugin’s `keyboard` option to false
bootstrap.Modal.Default.keyboard = false
```

--------------------------------

### Bootstrap Carousel Slide Transition and Ignored Calls

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Demonstrates controlling Bootstrap Carousel slides programmatically. It highlights that calling a method like `to()` on a transitioning component will be ignored, ensuring transitions complete before new ones start.

```javascript
const myCarouselEl = document.querySelector('#myCarousel')
const carousel = bootstrap.Carousel.getInstance(myCarouselEl) // Retrieve a Carousel instance

myCarouselEl.addEventListener('slid.bs.carousel', event => {
  carousel.to('2') // Will slide to the slide 2 as soon as the transition to slide 1 is finished
})

carousel.to('1') // Will start sliding to the slide 1 and returns to the caller
carousel.to('2') // !! Will be ignored, as the transition to the slide 1 is not finished !!
```

--------------------------------

### Initialize Bootstrap Components with CSS Selectors

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

This snippet shows how Bootstrap plugin constructors can accept either a DOM element or a valid CSS selector as their first argument for initialization. It covers Modal, Dropdown, Offcanvas, and Alert.

```javascript
const modal = new bootstrap.Modal('#myModal')
const dropdown = new bootstrap.Dropdown('[data-bs-toggle="dropdown"]')
const offcanvas = bootstrap.Offcanvas.getInstance('#myOffcanvas')
const alert = bootstrap.Alert.getOrCreateInstance('#myAlert')
```

--------------------------------

### Modal Plugin - Dispose Method

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Demonstrates the correct usage of the `dispose` method for modal instances, emphasizing its asynchronous nature and proper event listener placement.

```APIDOC
## POST /websites/getbootstrap/modal/dispose

--------------------------------

### Plugin Static Properties

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Lists the static properties `NAME` and `VERSION` available on Bootstrap plugin constructors, providing the plugin's name and version number.

```APIDOC
## GET /websites/getbootstrap/plugin/static-properties/{pluginName}

--------------------------------

### Initializing Bootstrap Toasts with ES Modules

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

This JavaScript snippet shows how to initialize Bootstrap's Toast component when using it as an ES module. It iterates through all elements with the class 'toast' and creates a new Toast instance for each, assuming the 'bootstrap.esm.min.js' file is accessible.

```javascript
import { Toast } from 'bootstrap.esm.min.js'

Array.from(document.querySelectorAll('.toast'))
  .forEach(toastNode => new Toast(toastNode))

```

--------------------------------

### Sanitizer Configuration

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Details Bootstrap's built-in content sanitizer for preventing XSS attacks in tooltip and popover components, including default allowed tags and attributes, and how to customize the allowlist or provide a custom sanitizer function.

```APIDOC
## POST /websites/getbootstrap/sanitizer/configure

--------------------------------

### Correctly dispose of Bootstrap modal instance

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Demonstrates the correct way to dispose of a Bootstrap modal instance by listening for the `shown.bs.hidden` event. This ensures the asynchronous nature of `hide()` is handled, preventing incorrect results.

```javascript
const myModal = document.querySelector('#myModal')
myModal.hide() // it is asynchronous

myModal.addEventListener('shown.bs.hidden', event => {
  myModal.dispose()
})
```

--------------------------------

### Trigger Bootstrap tooltip method with jQuery

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Demonstrates how to trigger specific methods of Bootstrap components, such as the `show` method for tooltips, using jQuery. This allows for programmatic control over component behavior after initialization.

```javascript
// to trigger the `show` method
$('#myTooltip').tooltip('show')
```

--------------------------------

### Plugin Default Settings

Source: https://getbootstrap.com/docs/5.3/getting-started/javascript

Explains how to modify the default configuration options for any Bootstrap plugin by directly accessing and altering the `Constructor.Default` object.

```APIDOC
## PUT /websites/getbootstrap/plugin/default-settings

--------------------------------

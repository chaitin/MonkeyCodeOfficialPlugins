### Get or Create Bootstrap Popover Instance and Set Content (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/popovers

Demonstrates how to retrieve an existing Bootstrap Popover instance or create a new one using `getOrCreateInstance`. It also shows how to update the popover's content dynamically using the `setContent` method, which accepts an object mapping selectors to new content.

```javascript
const popover = bootstrap.Popover.getOrCreateInstance('#example') // Returns a Bootstrap popover instance

popover.setContent({
  '.popover-header': 'another title',
  '.popover-body': 'another content'
})
```

--------------------------------

### Using Popper.js Configuration

Source: https://getbootstrap.com/docs/5.3/components/popovers

How to use a function with `popperConfig` to customize Popper.js configurations for popovers.

```APIDOC
## Using Popper.js Configuration

--------------------------------

### Configuring Popover Options with JavaScript (Bootstrap)

Source: https://getbootstrap.com/docs/5.3/components/popovers

Illustrates how to initialize and configure Bootstrap Popovers using JavaScript. Options can be passed as an object during initialization. This method provides more flexibility and allows for dynamic configuration.

```javascript
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl, {
  container: 'body',
  delay: {
    show: 500,
    hide: 100
  }
}))
```

--------------------------------

### Popover Methods

Source: https://getbootstrap.com/docs/5.3/components/popovers

This section outlines the various methods available to control Bootstrap popovers programmatically. All methods are asynchronous and return before the transition completes.

```APIDOC
## Popover Methods

--------------------------------

### Initialize All Popovers with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/popovers

This JavaScript snippet demonstrates how to initialize all popovers on a page by selecting elements with the `data-bs-toggle="popover"` attribute. It requires the `bootstrap.js` library and `Popper.js` (or `bootstrap.bundle.min.js`).

```javascript
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
```

--------------------------------

### Popover Configuration Options

Source: https://getbootstrap.com/docs/5.3/components/popovers

Configuration options for the Bootstrap Popover component, including sanitization, templates, and triggers.

```APIDOC
## Popover Configuration Options

--------------------------------

### Initialize Bootstrap Popover with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/popovers

Demonstrates how to initialize a Bootstrap popover using JavaScript. It requires a target HTML element and an options object to configure the popover's behavior.

```javascript
const exampleEl = document.getElementById('example')
const popover = new bootstrap.Popover(exampleEl, options)

```

--------------------------------

### Handle Bootstrap Popover Hidden Event (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/popovers

Provides an example of how to listen for the `hidden.bs.popover` event using `addEventListener`. This event fires after a popover has been completely hidden, allowing for custom actions to be performed once the popover is no longer visible.

```javascript
const myPopoverTrigger = document.getElementById('myPopover')
myPopoverTrigger.addEventListener('hidden.bs.popover', () => {
  // do something...
})
```

--------------------------------

### Popover Events

Source: https://getbootstrap.com/docs/5.3/components/popovers

This section details the events that are fired during the lifecycle of a Bootstrap popover, allowing for custom actions based on popover state changes.

```APIDOC
## Popover Events

--------------------------------

### Initialize Dismissible Popover with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/popovers

This JavaScript code initializes a popover with the 'focus' trigger for dismissible behavior. It selects elements with the class '.popover-dismiss' and configures them to disappear when focus is lost.

```javascript
const popover = new bootstrap.Popover('.popover-dismiss', {
  trigger: 'focus'
})

```

--------------------------------

### Configure Popover with Popper.js Configuration Function (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/popovers

Demonstrates how to initialize a Bootstrap Popover and provide a custom configuration function for Popper.js. This function allows modification of the default Popper.js configuration, enabling advanced positioning and behavior customization. The `defaultBsPopperConfig` object can be used as a base for the new configuration.

```javascript
const popover = new bootstrap.Popover(element, {
  popperConfig(defaultBsPopperConfig) {
    // const newPopperConfig = {...}
    // use defaultBsPopperConfig if needed...
    // return newPopperConfig
  }
})
```

--------------------------------

### Initialize Popover with Custom Container (Body)

Source: https://getbootstrap.com/docs/5.3/components/popovers

This JavaScript snippet shows how to initialize a Bootstrap popover and specify a custom container for its HTML output. Setting `container: 'body'` is recommended to avoid rendering issues with complex components like input groups or button groups.

```javascript
const popover = new bootstrap.Popover('.example-popover', {
  container: 'body'
})
```

--------------------------------

### Create Dismissible Popover on Next Click (HTML)

Source: https://getbootstrap.com/docs/5.3/components/popovers

This HTML shows how to create a popover that dismisses when the user clicks an element other than the popover trigger. It requires using an `<a>` tag with a `tabindex` and setting the `data-bs-trigger` attribute to 'focus'.

```html
<a tabindex="0" class="btn btn-lg btn-danger" role="button" data-bs-toggle="popover" data-bs-trigger="focus" data-bs-title="Dismissible popover" data-bs-content="And here’s some amazing content. It’s very engaging. Right?">Dismissible popover</a>

```

--------------------------------

### Configuring Popover Options with Data Attributes (Bootstrap)

Source: https://getbootstrap.com/docs/5.3/components/popovers

Demonstrates how to configure Bootstrap Popover options using HTML data attributes. Option names are converted from camelCase to kebab-case for data attributes. The `data-bs-config` attribute allows for JSON string configuration, with individual data attributes overriding `data-bs-config` values.

```html
<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-title="Popover title" data-bs-content="This is the popover content. It's very engaging.">Click to toggle popover</button>

<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-custom-class="beautifier" data-bs-delay='{"show": 500, "hide": 100}'>Click to toggle popover</button>

<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-config='{"animation":true, "delay":100}'>Click to toggle popover</button>
```

--------------------------------

### Implement Custom Popover with HTML

Source: https://getbootstrap.com/docs/5.3/components/popovers

This HTML snippet demonstrates how to apply custom popover styling using the 'data-bs-custom-class' attribute. It configures a button to trigger a popover with a specific title and content, applying the 'custom-popover' class for visual customization.

```html
<button type="button" class="btn btn-secondary"
        data-bs-toggle="popover" data-bs-placement="right"
        data-bs-custom-class="custom-popover"
        data-bs-title="Custom popover"
        data-bs-content="This popover is themed via CSS variables.">
  Custom popover
</button>

```

--------------------------------

### Bootstrap Popover HTML Structure

Source: https://getbootstrap.com/docs/5.3/components/popovers

This HTML snippet shows a basic button configured to trigger a Bootstrap popover. It utilizes `data-bs-toggle`, `data-bs-title`, and `data-bs-content` attributes to define the popover's behavior and content. The `btn` and `btn-lg` classes are Bootstrap utility classes for styling.

```html
<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-title="Popover title" data-bs-content="And here’s some amazing content. It’s very engaging. Right?">Click to toggle popover</button>
```

--------------------------------

### Bootstrap Popover Sass Variables

Source: https://getbootstrap.com/docs/5.3/components/popovers

Defines Sass variables for customizing the appearance of Bootstrap popovers. These variables control aspects like font size, background color, maximum width, border, shadow, and padding for both the popover body and header.

```scss
$popover-font-size:                 $font-size-sm;
$popover-bg:                        var(--#{$prefix}body-bg);
$popover-max-width:                 276px;
$popover-border-width:              var(--#{$prefix}border-width);
$popover-border-color:              var(--#{$prefix}border-color-translucent);
$popover-border-radius:             var(--#{$prefix}border-radius-lg);
$popover-inner-border-radius:       calc(#{$popover-border-radius} - #{$popover-border-width}); // stylelint-disable-line function-disallowed-list
$popover-box-shadow:                var(--#{$prefix}box-shadow);

$popover-header-font-size:          $font-size-base;
$popover-header-bg:                 var(--#{$prefix}secondary-bg);
$popover-header-color:              $headings-color;
$popover-header-padding-y:          .5rem;
$popover-header-padding-x:          $spacer;

$popover-body-color:                var(--#{$prefix}body-color);
$popover-body-padding-y:            $spacer;
$popover-body-padding-x:            $spacer;

$popover-arrow-width:               1rem;
$popover-arrow-height:              .5rem;

```

--------------------------------

### Initialize Popover within Modal with Custom Container

Source: https://getbootstrap.com/docs/5.3/components/popovers

This JavaScript snippet demonstrates initializing a Bootstrap popover within a modal dialog, ensuring the popover is appended to the modal's body. This is crucial for popovers containing interactive elements to maintain focusability within the modal's trap focus.

```javascript
const popover = new bootstrap.Popover('.example-popover', {
  container: '.modal-body'
})
```

--------------------------------

### Popover CSS Variables Definition (SCSS)

Source: https://getbootstrap.com/docs/5.3/components/popovers

This SCSS code defines the local CSS variables used for Bootstrap popovers, enabling real-time customization. It sets variables for z-index, max-width, font size, background, borders, padding, and arrow dimensions, with Sass customization also supported.

```scss
--#{$prefix}popover-zindex: #{$zindex-popover};
--#{$prefix}popover-max-width: #{$popover-max-width};
@include rfs($popover-font-size, --#{$prefix}popover-font-size);
--#{$prefix}popover-bg: #{$popover-bg};
--#{$prefix}popover-border-width: #{$popover-border-width};
--#{$prefix}popover-border-color: #{$popover-border-color};
--#{$prefix}popover-border-radius: #{$popover-border-radius};
--#{$prefix}popover-inner-border-radius: #{$popover-inner-border-radius};
--#{$prefix}popover-box-shadow: #{$popover-box-shadow};
--#{$prefix}popover-header-padding-x: #{$popover-header-padding-x};
--#{$prefix}popover-header-padding-y: #{$popover-header-padding-y};
@include rfs($popover-header-font-size, --#{$prefix}popover-header-font-size);
--#{$prefix}popover-header-color: #{$popover-header-color};
--#{$prefix}popover-header-bg: #{$popover-header-bg};
--#{$prefix}popover-body-padding-x: #{$popover-body-padding-x};
--#{$prefix}popover-body-padding-y: #{$popover-body-padding-y};
--#{$prefix}popover-body-color: #{$popover-body-color};
--#{$prefix}popover-arrow-width: #{$popover-arrow-width};
--#{$prefix}popover-arrow-height: #{$popover-arrow-height};
--#{$prefix}popover-arrow-border: var(--#{$prefix}popover-border-color);


```

--------------------------------

### Customize Popover Appearance with CSS Variables (SCSS)

Source: https://getbootstrap.com/docs/5.3/components/popovers

This SCSS code defines a custom class to override default popover styles using CSS variables. It scopes the customization to elements with the 'custom-popover' class, allowing for targeted theming of popover width, borders, header, and padding.

```scss
.custom-popover {
  --bs-popover-max-width: 200px;
  --bs-popover-border-color: var(--bd-violet-bg);
  --bs-popover-header-bg: var(--bd-violet-bg);
  --bs-popover-header-color: var(--bs-white);
  --bs-popover-body-padding-x: 1rem;
  --bs-popover-body-padding-y: .5rem;
}

```

--------------------------------

### Bootstrap Popover Placement Options

Source: https://getbootstrap.com/docs/5.3/components/popovers

This HTML snippet demonstrates how to configure Bootstrap popovers for different directions: top, right, bottom, and left. It uses the `data-bs-placement` attribute to control the popover's position relative to the trigger element. The `data-bs-container="body"` attribute ensures the popover is appended to the body.

```html
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="top" data-bs-content="Top popover">
  Popover on top
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="right" data-bs-content="Right popover">
  Popover on right
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-content="Bottom popover">
  Popover on bottom
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="left" data-bs-content="Left popover">
  Popover on left
</button>
```

--------------------------------

### Enable Popover on Disabled Button (HTML)

Source: https://getbootstrap.com/docs/5.3/components/popovers

This HTML snippet provides a workaround for triggering popovers on disabled elements. It wraps a disabled button in a `<span>` with `tabindex="0"` and sets `data-bs-toggle="popover"` on the span, allowing interaction via hover and focus.

```html
<span class="d-inline-block" tabindex="0" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-content="Disabled popover">
  <button class="btn btn-primary" type="button" disabled>Disabled button</button>
</span>

```

--------------------------------

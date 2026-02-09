### Description

This section explains how to provide a custom configuration for Popper.js when initializing a Bootstrap Popover. This allows for advanced positioning and behavior customization.

--------------------------------

### Method

N/A (Configuration)

--------------------------------

### Endpoint

N/A (Component configuration)

--------------------------------

### Parameters

#### Options
- **popperConfig** (function) - A function that receives the default Popper.js configuration and should return a custom configuration object. This function is called with its `this` reference set to the element that the popover is attached to.

--------------------------------

### Request Example

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

### Response

N/A

```

--------------------------------

### Description

Provides methods for interacting with Bootstrap tab instances, such as disposing, getting, or creating instances, and showing tabs. All API methods are asynchronous and start a transition.

--------------------------------

### Method

JavaScript API Methods

--------------------------------

### Endpoint

N/A (Client-side interaction)

--------------------------------

### Parameters

#### Static Methods
- **`bootstrap.Tab.getInstance(element)`** (static): Returns the tab instance associated with a DOM element.
- **`bootstrap.Tab.getOrCreateInstance(element)`** (static): Returns the tab instance associated with a DOM element or creates a new one.

#### Instance Methods
- **`dispose()`**: Destroys an element's tab instance.
- **`show()`**: Selects the given tab and shows its associated pane. Returns to the caller before the tab pane has actually been shown.

--------------------------------

### Request Example

```javascript
// Get an existing instance
const tabInstance = bootstrap.Tab.getInstance(document.getElementById('myTab'));

// Create a new instance
const newTabInstance = new bootstrap.Tab(document.querySelector('button[data-bs-target="#messages"]'));

// Show a tab
newTabInstance.show();

// Dispose an instance
// tabInstance.dispose();
```

--------------------------------

### Response

#### Success Response (UI Update / Instance Object)
- The `show()` method returns void but triggers a UI update.
- `getInstance` and `getOrCreateInstance` return a `Tab` instance object.

#### Response Example
N/A
```

--------------------------------

### Description

Provides methods to control popover behavior, such as showing, hiding, enabling, disabling, and updating popovers.

--------------------------------

### Methods

- **`disable()`**: Removes the ability for an element’s popover to be shown.
- **`dispose()`**: Hides and destroys an element’s popover. Removes stored data on the DOM element.
- **`enable()`**: Gives an element’s popover the ability to be shown. Popovers are enabled by default.
- **`getInstance(element)`**: _Static_ method. Returns the popover instance associated with a DOM element.
- **`getOrCreateInstance(element, option)`**: _Static_ method. Returns the popover instance associated with a DOM element, or creates a new one if not initialized.
- **`hide()`**: Hides an element’s popover. Returns before the popover has actually been hidden.
- **`setContent(content)`**: Allows changing the popover’s content after initialization. Accepts an object where keys are selectors and values are content.
- **`show()`**: Reveals an element’s popover. Returns before the popover has actually been shown.
- **`toggle()`**: Toggles an element’s popover. Returns before the popover has actually been shown or hidden.
- **`toggleEnabled()`**: Toggles the ability for an element’s popover to be shown or hidden.
- **`update()`**: Updates the position of an element’s popover.

--------------------------------

### Request Example

```javascript
// Get or create an instance
const popover = bootstrap.Popover.getOrCreateInstance('#example');

// Set new content
popover.setContent({
  '.popover-header': 'New Title',
  '.popover-body': 'New Content'
});
```

--------------------------------

### Response

Methods return to the caller as soon as the transition is started, but before it ends. A method call on a transitioning component will be ignored.
```

--------------------------------

### Description

Creates a new instance of the Bootstrap Offcanvas component for a given element.

--------------------------------

### Method

`constructor`

--------------------------------

### Endpoint

N/A (JavaScript constructor)

--------------------------------

### Parameters

#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

--------------------------------

### Request Example

```javascript
const bsOffcanvas = new bootstrap.Offcanvas('#myOffcanvas')
```

--------------------------------

### Response

#### Success Response (200)
N/A (Returns an Offcanvas instance)

#### Response Example
```javascript
// Offcanvas instance object
```
```

--------------------------------

### Description

This section details the available configuration options for the Bootstrap Popover component. These options can be set via JavaScript or data attributes.

--------------------------------

### Method

N/A (Configuration options)

--------------------------------

### Endpoint

N/A (Component configuration)

--------------------------------

### Parameters

#### Options
- **sanitize** (boolean) - `true` - Enable content sanitization. If true, the `template`, `content` and `title` options will be sanitized. **Exercise caution when disabling content sanitization.**
- **sanitizeFn** (null, function) - `null` - Provide an alternative content sanitization function. This can be useful if you prefer to use a dedicated library to perform sanitization.
- **selector** (string, false) - `false` - If a selector is provided, popover objects will be delegated to the specified targets. This is used to also apply popovers to dynamically added DOM elements.
- **template** (string) - `'<div class="popover" role="tooltip"><div class="popover-arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div></div>'` - Base HTML to use when creating the popover. The popover’s `title` will be injected into the `.popover-header`. The popover’s `content` will be injected into the `.popover-body`. `.popover-arrow` will become the popover’s arrow. The outermost wrapper element should have the `.popover` class and `role="tooltip"`.
- **title** (string, element, function) - `''` - The popover title. If a function is given, it will be called with its `this` reference set to the element that the popover is attached to.
- **trigger** (string) - `'click'` - How popover is triggered: click, hover, focus, manual. You may pass multiple triggers; separate them with a space. `'manual'` indicates that the popover will be triggered programmatically.

#### Data attributes for individual popovers
Options for individual popovers can alternatively be specified through the use of data attributes, as explained above.

--------------------------------

### Request Example

N/A

--------------------------------

### Response

N/A

```

--------------------------------

### Description

Provides static methods to retrieve or create plugin instances associated with a specific DOM element.

--------------------------------

### Method

`getInstance(element)`
`getOrCreateInstance(element, options)`

--------------------------------

### Endpoint

`bootstrap.PluginName.getInstance(document.getElementById('elementId'))`
`bootstrap.PluginName.getOrCreateInstance(document.getElementById('elementId'), { option: 'value' })`

--------------------------------

### Parameters

#### Path Parameters
- **elementId** (string) - Required - The ID of the DOM element to associate with the plugin instance.

#### Query Parameters
- **element** (HTMLElement) - Required - The DOM element to get or create the instance for.
- **options** (object) - Optional - Configuration options to use when creating a new instance.

--------------------------------

### Request Example

```javascript
const modalElement = document.getElementById('myModal')
const modalInstance = bootstrap.Modal.getInstance(modalElement) // Gets existing instance

const newModalInstance = bootstrap.Modal.getOrCreateInstance(modalElement, { keyboard: false }) // Gets or creates instance
```

--------------------------------

### Response

#### Success Response (200)
- **instance** (object) - The plugin instance associated with the element.

#### Response Example
```json
{
  "instance": "[Plugin Instance Object]"
}
```
```

--------------------------------

### Description

Events are fired at certain points in the popover’s lifecycle. You can use JavaScript to listen for and execute custom actions on these events.

--------------------------------

### Events

- **`hide.bs.popover`**: Fired immediately when the `hide` instance method is called.
- **`hidden.bs.popover`**: Fired when the popover has finished being hidden (waits for CSS transitions).
- **`inserted.bs.popover`**: Fired after `show.bs.popover` when the popover template has been added to the DOM.
- **`show.bs.popover`**: Fired immediately when the `show` instance method is called.
- **`shown.bs.popover`**: Fired when the popover has been made visible (waits for CSS transitions).

--------------------------------

### Request Example

```javascript
const myPopoverTrigger = document.getElementById('myPopover');
myPopoverTrigger.addEventListener('hidden.bs.popover', () => {
  // do something after popover is hidden
  console.log('Popover hidden!');
});
```

--------------------------------

### Response

Event listeners receive an `Event` object. Some events may provide additional data in their `detail` property.
```

--------------------------------

### Description

Use `data-bs-toggle="button"` to enable toggle functionality on button elements. For pre-toggled buttons, ensure the `.active` class and `aria-pressed="true"` are manually applied for accessibility.

--------------------------------

### HTML Examples

**Standard Buttons:**
```html
<p class="d-inline-flex gap-1">
  <button type="button" class="btn" data-bs-toggle="button">Toggle button</button>
  <button type="button" class="btn active" data-bs-toggle="button" aria-pressed="true">Active toggle button</button>
  <button type="button" class="btn" disabled data-bs-toggle="button">Disabled toggle button</button>
</p>
<p class="d-inline-flex gap-1">
  <button type="button" class="btn btn-primary" data-bs-toggle="button">Toggle button</button>
  <button type="button" class="btn btn-primary active" data-bs-toggle="button" aria-pressed="true">Active toggle button</button>
  <button type="button" class="btn btn-primary" disabled data-bs-toggle="button">Disabled toggle button</button>
</p>
```

**Toggle Links:**
```html
<p class="d-inline-flex gap-1">
  <a href="#" class="btn" role="button" data-bs-toggle="button">Toggle link</a>
  <a href="#" class="btn active" role="button" data-bs-toggle="button" aria-pressed="true">Active toggle link</a>
  <a class="btn disabled" aria-disabled="true" role="button" data-bs-toggle="button">Disabled toggle link</a>
</p>
<p class="d-inline-flex gap-1">
  <a href="#" class="btn btn-primary" role="button" data-bs-toggle="button">Toggle link</a>
  <a href="#" class="btn btn-primary active" role="button" data-bs-toggle="button" aria-pressed="true">Active toggle link</a>
  <a class="btn btn-primary disabled" aria-disabled="true" role="button" data-bs-toggle="button">Disabled toggle link</a>
</p>
```
```

--------------------------------

### Description

Use `data-bs-toggle="collapse"` and `data-bs-target` to control collapsible elements. Add `collapse` class to the collapsible element, and `show` class to make it default open.

--------------------------------

### Usage

```html
<button type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample">Button with data attributes</button>
<div class="collapse" id="collapseExample">...
</div>
```

--------------------------------

### Accordion Behavior

Add `data-bs-parent="#selector"` to elements for accordion-like group management.

## JavaScript Initialization

--------------------------------

### Description

Manually enable the Collapse component using JavaScript.

--------------------------------

### Method

```javascript
const collapseElementList = document.querySelectorAll('.collapse')
const collapseList = [...collapseElementList].map(collapseEl => new bootstrap.Collapse(collapseEl))
```

## Options

--------------------------------

### Description

Options can be passed via data attributes (kebab-case) or JavaScript (camelCase). `data-bs-config` can house a JSON string for multiple configurations, with individual data attributes overriding `data-bs-config` values.

--------------------------------

### Data Attributes

- `data-bs-animation` (string) - Example: `data-bs-animation="{value}"`
- `data-bs-custom-class` (string) - Example: `data-bs-custom-class="beautifier"`
- `data-bs-config` (JSON string) - Example: `data-bs-config='{"delay":0, "title":123}'`

--------------------------------

### JavaScript Options

- `parent` (selector, DOM element) - `null` - If provided, closes other collapsible elements under the parent when this one is shown.
- `toggle` (boolean) - `true` - Toggles the collapsible element on invocation.

--------------------------------

### Example (JavaScript Constructor)

```javascript
const bsCollapse = new bootstrap.Collapse('#myCollapse', {
  toggle: false
})
```
```

--------------------------------

### Description

Provides methods to control the visibility and state of an Offcanvas component, as well as manage its lifecycle and retrieve instances.

--------------------------------

### Methods

#### `dispose`
- **Description**: Destroys an element's offcanvas instance and removes associated event listeners.
- **Returns**: `void`

#### `getInstance` (Static)
- **Description**: Retrieves the Offcanvas instance associated with a given DOM element.
- **Parameters**:
  - **element** (`HTMLElement`) - The DOM element to get the instance from.
- **Returns**: `Offcanvas | null` - The Offcanvas instance or null if none is found.

#### `getOrCreateInstance` (Static)
- **Description**: Retrieves the Offcanvas instance associated with a given DOM element, or creates a new one if it doesn't exist.
- **Parameters**:
  - **element** (`HTMLElement`) - The DOM element to get or create the instance for.
  - **options** (`object`, optional) - Configuration options for the new instance if created.
- **Returns**: `Offcanvas` - The existing or newly created Offcanvas instance.

#### `hide`
- **Description**: Hides the offcanvas element. Returns before the element is fully hidden.
- **Returns**: `void`

#### `show`
- **Description**: Shows the offcanvas element. Returns before the element is fully shown.
- **Returns**: `void`

#### `toggle`
- **Description**: Toggles the visibility of the offcanvas element. Returns before the state change is complete.
- **Returns**: `void`

--------------------------------

### Request Example

```javascript
const myOffcanvas = bootstrap.Offcanvas.getOrCreateInstance('#myOffcanvas');
myOffcanvas.show();

const anotherOffcanvas = bootstrap.Offcanvas.getInstance(document.getElementById('anotherOffcanvas'));
if (anotherOffcanvas) {
  anotherOffcanvas.hide();
}
```

--------------------------------

### Response

#### Success Response (200)
N/A (Methods do not return data in the response body)

#### Response Example
```javascript
// No response body for method calls
```
```

--------------------------------

### Description

Enable tabbable tabs using JavaScript. Each tab can be activated individually or in groups.

--------------------------------

### Method

JavaScript API

--------------------------------

### Endpoint

N/A (Client-side interaction)

--------------------------------

### Parameters

#### JavaScript Methods
- **`new bootstrap.Tab(element)`**: Creates a new Tab instance for the given element.
- **`bootstrap.Tab.getInstance(element)`**: Gets the Tab instance associated with a DOM element.
- **`bootstrap.Tab.getOrCreateInstance(element)`**: Gets the Tab instance or creates a new one if it doesn't exist.
- **`tabInstance.show()`**: Selects the given tab and shows its associated pane. Returns before the tab pane is fully shown.

--------------------------------

### Request Example

```javascript
// Activate all tabs
const triggerTabList = document.querySelectorAll('#myTab button');
triggerTabList.forEach(triggerEl => {
  triggerEl.addEventListener('click', event => {
    event.preventDefault();
    const tabTrigger = new bootstrap.Tab(triggerEl);
    tabTrigger.show();
  });
});

// Activate a specific tab by target
const triggerEl = document.querySelector('#myTab button[data-bs-target="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show();
```

--------------------------------

### Response

#### Success Response (UI Update)
- No explicit response body, UI updates to show the selected tab content.

#### Response Example
N/A
```

--------------------------------

### Description

This section outlines the various options available for configuring Bootstrap tooltips. Options can be set via JavaScript or data attributes.

--------------------------------

### Method

N/A (Configuration Options)

--------------------------------

### Endpoint

N/A (Configuration Options)

--------------------------------

### Parameters

#### Options
- **allowList** (object) - Default value - An object containing allowed tags and attributes. Those not explicitly allowed will be removed by the content sanitizer. Exercise caution when adding to this list.
- **animation** (boolean) - `true` - Apply a CSS fade transition to the tooltip.
- **boundary** (string, element) - `'clippingParents'` - Overflow constraint boundary of the tooltip. By default, it’s `'clippingParents'` and can accept an HTMLElement reference (via JavaScript only).
- **container** (string, element, false) - `false` - Appends the tooltip to a specific element. Example: `container: 'body'`.
- **customClass** (string, function) - `''` - Add classes to the tooltip when it is shown. Can be a string of space-separated classes or a function returning a string.
- **delay** (number, object) - `0` - Delay showing and hiding the tooltip (ms). Can be a number for both or an object `{ "show": 500, "hide": 150 }`.
- **fallbackPlacements** (array) - `['top', 'right', 'bottom', 'left']` - Define fallback placements by providing a list of placements in array (in order of preference).
- **html** (boolean) - `false` - Allow HTML in the tooltip. If true, HTML tags in the tooltip’s `title` will be rendered. If false, `innerText` property will be used.
- **offset** (array, string, function) - `[0, 6]` - Offset of the tooltip relative to its target. Can be an array, a comma-separated string, or a function.
- **placement** (string, function) - `'top'` - How to position the tooltip: auto, top, bottom, left, right. Can also be a function.
- **popperConfig** (null, object, function) - `null` - To change Bootstrap’s default Popper config. Can be an object or a function that returns a configuration object.

--------------------------------

### Request Example

N/A (Configuration Options)

--------------------------------

### Response

N/A (Configuration Options)
```

--------------------------------

### Description

Destroys an element's modal instance, removing stored data from the DOM element. It's crucial to call this after the modal has been fully hidden.

--------------------------------

### Method

`dispose()`

--------------------------------

### Endpoint

`myModal.dispose()`

--------------------------------

### Parameters

None

--------------------------------

### Request Example

```javascript
const myModal = document.querySelector('#myModal')
myModal.hide() // it is asynchronous

myModal.addEventListener('shown.bs.hidden', event => {
  myModal.dispose()
})
```

--------------------------------

### Response

#### Success Response (204)
No content is returned upon successful disposal.

#### Response Example
None
```

--------------------------------

### Description

Retrieves static properties of Bootstrap plugins, including their registered name and version.

--------------------------------

### Method

Static property access

--------------------------------

### Endpoint

`bootstrap.PluginName.NAME`
`bootstrap.PluginName.VERSION`

--------------------------------

### Parameters

#### Path Parameters
- **pluginName** (string) - Required - The name of the Bootstrap plugin (e.g., 'Modal', 'Tooltip').

--------------------------------

### Request Example

```javascript
const modalName = bootstrap.Modal.NAME // 'modal'
const modalVersion = bootstrap.Modal.VERSION // '5.3.0'
```

--------------------------------

### Response

#### Success Response (200)
- **NAME** (string) - The name of the plugin.
- **VERSION** (string) - The version of the plugin.

#### Response Example
```json
{
  "NAME": "modal",
  "VERSION": "5.3.0"
}
```
```

--------------------------------

### Key Options for Utility Configuration:

- **`property`** (Required): Specifies the CSS property to be targeted. Can be a string or an array of strings.
- **`values`** (Required): Defines the values for the property. Can be a list or a map. If a map is used, the keys determine the class names (unless `class: null`), and the values are the CSS values.
- **`class`** (Optional): Sets a custom prefix for the generated class names. Defaults to the property name or the first property name if `property` is an array. If set to `null`, classes are generated based on the keys of the `values` map.
- **`css-var`** (Optional): If `true`, generates CSS variables instead of standard CSS rules. Defaults to `false`.
- **`css-variable-name`** (Optional): Allows for a custom un-prefixed name for CSS variables.
- **`local-vars`** (Optional): A map of local CSS variables to include within the generated rulesets.
- **`state`** (Optional): A list of pseudo-class variants (e.g., `:hover`, `:focus`) to generate.
- **`responsive`** (Optional): If `true`, generates responsive variants of the utility classes. Defaults to `false`.
- **`rfs`** (Optional): If `true`, enables fluid rescaling with RFS (Responsive Font Size). Defaults to `false`.
- **`print`** (Optional): If `true`, generates utility classes specifically for printing. Defaults to `false`.
- **`rtl`** (Optional): If `true`, ensures the utility is kept in Right-to-Left (RTL) context. Defaults to `true`.

--------------------------------

### Example: Opacity Utility

```scss
$utilities: (
  "opacity": (
    property: opacity,
    values: (
      0: 0,
      25: .25,
      50: .5,
      75: .75,
      100: 1,
    )
  )
);
```

This configuration generates the following CSS:

```css
.opacity-0 { opacity: 0; }
.opacity-25 { opacity: .25; }
.opacity-50 { opacity: .5; }
.opacity-75 { opacity: .75; }
.opacity-100 { opacity: 1; }
```

--------------------------------

### Example: Text Decoration Utility

```scss
$utilities: (
  "text-decoration": (
    property: text-decoration,
    values: none underline line-through
  )
);
```

This configuration generates the following CSS:

```css
.text-decoration-none { text-decoration: none !important; }
.text-decoration-underline { text-decoration: underline !important; }
.text-decoration-line-through { text-decoration: line-through !important; }
```

--------------------------------

### Example: Custom Class Prefix (Opacity)

```scss
$utilities: (
  "opacity": (
    property: opacity,
    class: o, // Custom prefix
    values: (
      0: 0,
      25: .25,
      50: .5,
      75: .75,
      100: 1,
    )
  )
);
```

This configuration generates the following CSS:

```css
.o-0 { opacity: 0 !important; }
.o-25 { opacity: .25 !important; }
.o-50 { opacity: .5 !important; }
.o-75 { opacity: .75 !important; }
.o-100 { opacity: 1 !important; }
```

--------------------------------

### Example: `class: null` for Visibility Utility

```scss
$utilities: (
  "visibility": (
    property: visibility,
    class: null, // Generates classes based on values map keys
    values: (
      visible: visible,
      invisible: hidden,
    )
  )
);
```

This configuration generates the following CSS:

```css
.visible { visibility: visible !important; }
.invisible { visibility: hidden !important; }
```
```

--------------------------------

### Description

Options can be passed via data attributes or JavaScript. For data attributes, append the option name to `data-bs-` and convert camelCase to kebab-case (e.g., `data-bs-custom-class`). The `data-bs-config` attribute allows for a JSON string of configurations, which can be overridden by individual data attributes.

--------------------------------

### Available Options

| Name | Type | Default | Description |
|---|---|---|---|
| `animation` | boolean | `true` | Apply a CSS fade transition to the toast. |
| `autohide` | boolean | `true` | Automatically hide the toast after the delay. |
| `delay` | number | `5000` | Delay in milliseconds before hiding the toast. |

--------------------------------

### Data Attribute Example

```html
<div class="toast" data-bs-animation="true" data-bs-autohide="false" data-bs-delay="10000">...</div>
```

--------------------------------

### `data-bs-config` Example

```html
<div class="toast" data-bs-config='{"delay": 5000, "autohide": true}'>...</div>
```

--------------------------------

### Configuration Merging

The final configuration is a merge of `data-bs-config`, individual `data-bs-` attributes, and JavaScript object properties, with later values overriding earlier ones.
```

--------------------------------

### Configuration Options

| Name | Type | Default | Description |
|---|---|---|---|
| `parent` | selector, DOM element | `null` | If parent is provided, then all collapsible elements under the specified parent will be closed when this collapsible item is shown. (similar to traditional accordion behavior - this is dependent on the `card` class). The attribute has to be set on the target collapsible area. |
| `toggle` | boolean | `true` | Toggles the collapsible element on invocation. |
```

--------------------------------

### Description

Dropdown options can be configured using data attributes (kebab-case) or JavaScript objects. Data attributes override `data-bs-config`, and both override JavaScript object configurations.

--------------------------------

### Available Options

| Name           | Type                           | Default       | Description
```

--------------------------------

### Description

All API methods are asynchronous and start a transition. They return to the caller as soon as the transition is started, but before it ends. Calling a method on a transitioning component will be ignored.

--------------------------------

### Methods

| Method | Description |
|---|---|
| `dispose()` | Hides an element’s toast. The toast remains on the DOM but won’t show anymore. |
| `getInstance(element)` | _Static_ method to get the toast instance associated with a DOM element. |
| `getOrCreateInstance(element)` | _Static_ method to get the toast instance associated with a DOM element, or create a new one if it wasn’t initialized. |
| `hide()` | Hides an element’s toast. Returns to the caller before the toast has actually been hidden. Must be called manually if `autohide` is `false`. |
| `isShown()` | Returns a boolean indicating the toast’s visibility state. |
| `show()` | Reveals an element’s toast. Returns to the caller before the toast has actually been shown. Must be called manually to show the toast. |

--------------------------------

### Example Usage

**Getting an instance:**
```javascript
const myToastEl = document.getElementById('myToastEl');
const myToast = bootstrap.Toast.getInstance(myToastEl);
```

**Showing a toast:**
```javascript
myToast.show();
```

**Hiding a toast:**
```javascript
myToast.hide();
```
```

--------------------------------

### Description

Configures Bootstrap's content sanitizer for components like tooltips and popovers to prevent XSS attacks. Allows customization of the default allowlist or replacement with a custom sanitization function.

--------------------------------

### Method

Direct property assignment or function assignment

--------------------------------

### Endpoint

`bootstrap.Tooltip.Default.allowList`
`bootstrap.Tooltip.Default.sanitizeFn`

--------------------------------

### Parameters

#### Request Body
- **allowList** (object) - Optional - An object defining the HTML tags and attributes allowed during sanitization. Can be modified by pushing new elements or regex patterns.
- **sanitizeFn** (function) - Optional - A custom function to perform content sanitization. It should accept the HTML content as a string and return the sanitized string.

--------------------------------

### Request Example

```javascript
// Add 'table' element to the default allowlist
const myDefaultAllowList = bootstrap.Tooltip.Default.allowList
myDefaultAllowList.table = []

// Replace sanitizer with DOMPurify
const yourTooltipEl = document.querySelector('#yourTooltip')
const tooltip = new bootstrap.Tooltip(yourTooltipEl, {
  sanitizeFn(content) {
    return DOMPurify.sanitize(content)
  }
})
```

--------------------------------

### Response

#### Success Response (200)
Indicates that the sanitizer configuration has been updated.

#### Response Example
```json
{
  "message": "Sanitizer configuration updated successfully."
}
```
```

--------------------------------

### Description

Activate tab or pill navigation without JavaScript by using `data-bs-toggle="tab"` or `data-bs-toggle="pill"` on elements within `.nav-tabs` or `.nav-pills`.

--------------------------------

### Method

HTML Attributes

--------------------------------

### Endpoint

N/A (Client-side interaction)

--------------------------------

### Parameters

#### HTML Attributes
- **data-bs-toggle** (string) - Required - Set to `"tab"` or `"pill"` to enable tab functionality.
- **data-bs-target** (string) - Required - Specifies the `id` of the tab pane to be shown.

--------------------------------

### Request Example

```html
<button class="nav-link" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab">Profile</button>
```

--------------------------------

### Response

#### Success Response (UI Update)
- No explicit response body, UI updates to show the selected tab content.

#### Response Example
N/A
```

--------------------------------

### Description

Allows modification of the default configuration settings for Bootstrap plugins. Changes made to the `Constructor.Default` object will affect all future instances of that plugin.

--------------------------------

### Method

Direct property assignment

--------------------------------

### Endpoint

`bootstrap.PluginName.Default.optionName = newValue`

--------------------------------

### Parameters

#### Query Parameters
- **optionName** (string) - Required - The name of the default option to modify.
- **newValue** (any) - Required - The new value to assign to the option.

--------------------------------

### Request Example

```javascript
// Changes default for the modal plugin’s `keyboard` option to false
bootstrap.Modal.Default.keyboard = false
```

--------------------------------

### Response

#### Success Response (200)
Indicates that the default settings have been updated.

#### Response Example
```json
{
  "message": "Default settings updated successfully."
}
```
```

--------------------------------

### Description

All API methods are asynchronous and start a transition. They return to the caller as soon as the transition is started, but before it ends. Method calls on transitioning components are ignored.

--------------------------------

### Constructor

Activates your content as a collapsible element. Accepts an optional options `object`.

--------------------------------

### Available Methods

- **`dispose()`**
  - Description: Destroys an element’s collapse. (Removes stored data on the DOM element)

- **`getInstance(element)`** (Static method)
  - Description: Returns the collapse instance associated with a DOM element.
  - Usage: `bootstrap.Collapse.getInstance(element)`

- **`getOrCreateInstance(element)`** (Static method)
  - Description: Returns a collapse instance associated with a DOM element or creates a new one.
  - Usage: `bootstrap.Collapse.getOrCreateInstance(element)`

- **`hide()`**
  - Description: Hides a collapsible element. Returns before the element is actually hidden.

- **`show()`**
  - Description: Shows a collapsible element. Returns before the element is actually shown.

- **`toggle()`**
  - Description: Toggles a collapsible element to shown or hidden. Returns before the state change is complete.
```

--------------------------------

### Via data attributes

Use data attributes to easily control the position of the carousel. `data-bs-slide` accepts the keywords `prev` or `next`, which alters the slide position relative to its current position. Alternatively, use `data-bs-slide-to` to pass a raw slide index to the carousel `data-bs-slide-to="2"`, which shifts the slide position to a particular index beginning with `0`.

--------------------------------

### Via JavaScript

Call carousel manually with:

```javascript
const carousel = new bootstrap.Carousel('#myCarousel')
```

--------------------------------

### Options

As options can be passed via data attributes or JavaScript, you can append an option name to `data-bs-`, as in `data-bs-animation="{value}"`. Make sure to change the case type of the option name from “ _camelCase_ ” to “ _kebab-case_ ” when passing the options via data attributes. For example, use `data-bs-custom-class="beautifier"` instead of `data-bs-customClass="beautifier"`.

As of Bootstrap 5.2.0, all components support an **experimental** reserved data attribute `data-bs-config` that can house simple component configuration as a JSON string. When an element has `data-bs-config='{"delay":0, "title":123}'` and `data-bs-title="456"` attributes, the final `title` value will be `456` and the separate data attributes will override values given on `data-bs-config`. In addition, existing data attributes are able to house JSON values like `data-bs-delay='{"show":0,"hide":150}'`.

The final configuration object is the merged result of `data-bs-config`, `data-bs-`, and `js object` where the latest given key-value overrides the others.

| Name | Type | Default | Description |
|---|---|---|---|
| `interval` | number | `5000` | The amount of time to delay between automatically cycling an item. |
| `keyboard` | boolean | `true` | Whether the carousel should react to keyboard events. |
| `pause` | string, boolean | `"hover"` | If set to `"hover"`, pauses the cycling of the carousel on `mouseenter` and resumes the cycling of the carousel on `mouseleave`. If set to `false`, hovering over the carousel won’t pause it. On touch-enabled devices, when set to `"hover"`, cycling will pause on `touchend` (once the user finished interacting with the carousel) for two intervals, before automatically resuming. This is in addition to the mouse behavior. |
| `ride` | string, boolean | `false` | If set to `true`, autoplays the carousel after the user manually cycles the first item. If set to `"carousel"`, autoplays the carousel on load. |
| `touch` | boolean | `true` | Whether the carousel should support left/right swipe interactions on touchscreen devices. |
| `wrap` | boolean | `true` | Whether the carousel should cycle continuously or have hard stops. |
```

--------------------------------

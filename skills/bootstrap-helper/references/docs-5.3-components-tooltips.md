### Bootstrap Tooltip Placement Examples (HTML)

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Demonstrates how to create tooltips with different placement directions (top, right, bottom, left) using Bootstrap's data attributes. It also shows how to enable HTML content within tooltips.

```html
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top">
  Tooltip on top
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="right" data-bs-title="Tooltip on right">
  Tooltip on right
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="Tooltip on bottom">
  Tooltip on bottom
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="left" data-bs-title="Tooltip on left">
  Tooltip on left
</button>

<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-html="true" data-bs-title="<em>Tooltip</em> <u>with</u> <b>HTML</b>">
  Tooltip with HTML
</button>
```

--------------------------------

### Bootstrap Tooltip HTML Structure Example

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Illustrates the required HTML markup for a Bootstrap tooltip using data attributes and the generated DOM structure that the plugin creates. It emphasizes accessibility by recommending focusable elements.

```html
<!-- HTML to write -->
<a href="#" data-bs-toggle="tooltip" data-bs-title="Some tooltip text!">Hover over me</a>

<!-- Generated markup by the plugin -->
<div class="tooltip bs-tooltip-auto" role="tooltip">
  <div class="tooltip-arrow"></div>
  <div class="tooltip-inner">
    Some tooltip text!
  </div>
</div>
```

--------------------------------

### Get Tooltip Instance and Use setContent Method

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Shows how to retrieve an existing Bootstrap tooltip instance using `getInstance` and then utilize the `setContent` method to dynamically update the tooltip's content. The `setContent` method accepts an object mapping selectors within the tooltip template to new content.

```javascript
const tooltip = bootstrap.Tooltip.getInstance('#example') // Returns a Bootstrap tooltip instance

// setContent example
tooltip.setContent({ '.tooltip-inner': 'another title' })
```

--------------------------------

### Configure Tooltip Options with JavaScript (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Illustrates how to initialize and configure Bootstrap tooltips using JavaScript. Options can be passed as an object during instantiation. This method provides direct control over all available tooltip configurations.

```javascript
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, {
  animation: true,
  customClass: 'my-custom-class',
  delay: {
    show: 500,
    hide: 100
  },
  offset: [0, 6],
  placement: 'top',
  popperConfig: null
}))
```

--------------------------------

### Initialize Tooltip with Popper.js Configuration

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Demonstrates how to initialize a Bootstrap tooltip and customize its Popper.js configuration using the `popperConfig` option. This allows for advanced positioning and behavior adjustments.

```javascript
const tooltip = new bootstrap.Tooltip(element, {
  popperConfig(defaultBsPopperConfig) {
    // const newPopperConfig = {...}
    // use defaultBsPopperConfig if needed...
    // return newPopperConfig
  }
})
```

--------------------------------

### Initialize Bootstrap Tooltip via JavaScript

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Shows how to instantiate a Bootstrap tooltip using JavaScript. It involves selecting an element by its ID and creating a new `bootstrap.Tooltip` instance, optionally with configuration options.

```javascript
const exampleEl = document.getElementById('example')
const tooltip = new bootstrap.Tooltip(exampleEl, options)
```

--------------------------------

### Initialize All Tooltips with JavaScript

Source: https://getbootstrap.com/docs/5.3/components/tooltips

This JavaScript snippet demonstrates how to initialize all tooltips on a page by selecting elements with the `data-bs-toggle="tooltip"` attribute. It uses the `bootstrap.Tooltip` class to create new tooltip instances.

```javascript
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
```

--------------------------------

### Custom Tooltip Styling with CSS Variables

Source: https://getbootstrap.com/docs/5.3/components/tooltips

This example demonstrates how to customize the appearance of tooltips using CSS variables. A custom class (`custom-tooltip`) is applied to the tooltip trigger element, and CSS variables like `--bs-tooltip-bg` and `--bs-tooltip-color` are overridden within the scope of this custom class.

```css
.custom-tooltip {
  --bs-tooltip-bg: var(--bd-violet-bg);
  --bs-tooltip-color: var(--bs-white);
}
```

--------------------------------

### Bootstrap Tooltip Event Handling in JavaScript

Source: https://getbootstrap.com/docs/5.3/components/tooltips

This snippet demonstrates how to get a Bootstrap tooltip instance, add an event listener for the 'hidden.bs.tooltip' event, and manually trigger the tooltip's hide method. It requires the Bootstrap JavaScript library and a DOM element with a tooltip initialized.

```javascript
const myTooltipEl = document.getElementById('myTooltip')
const tooltip = bootstrap.Tooltip.getOrCreateInstance(myTooltipEl)

myTooltipEl.addEventListener('hidden.bs.tooltip', () => {
  // do something...
})

tooltip.hide()

```

--------------------------------

### Tooltip Configuration Options

Source: https://getbootstrap.com/docs/5.3/components/tooltips

This section outlines the various options available for configuring Bootstrap tooltips. Options can be set via JavaScript or data attributes.

```APIDOC
## Tooltip Configuration Options

--------------------------------

### Configure Tooltip Options with Data Attributes (HTML)

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Demonstrates how to configure Bootstrap tooltip options using HTML data attributes. Options are appended to `data-bs-` and require camelCase to kebab-case conversion. The experimental `data-bs-config` attribute allows for JSON string configurations, with individual data attributes overriding `data-bs-config` values.

```html
<button type="button" class="btn btn-lg btn-danger" id="example" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-custom-class="beautifier" data-bs-delay='{"show":500,"hide":100}' data-bs-config='{"animation":true, "title":"My Tooltip"}'>
  Custom configuration
</button>
```

--------------------------------

### Bootstrap Tooltip Boundary Option (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/tooltips

Demonstrates how to configure the `boundary` option for Bootstrap tooltips using JavaScript. This option allows overriding the default clipping behavior, useful when tooltips are within scrollable containers.

```javascript
const tooltip = new bootstrap.Tooltip('#example', {
  boundary: document.body // or document.querySelector('#boundary')
})
```

--------------------------------

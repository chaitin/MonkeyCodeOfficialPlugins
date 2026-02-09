### JavaScript Initialization

Source: https://getbootstrap.com/docs/5.3/components/accordion

Manually enable the collapse functionality on multiple elements using JavaScript.

```APIDOC
## Via JavaScript

Enable manually with:

```javascript
const accordionCollapseElementList = document.querySelectorAll('#myAccordion .collapse')
const accordionCollapseList = [...accordionCollapseElementList].map(accordionCollapseEl => new bootstrap.Collapse(accordionCollapseEl))
```
```

--------------------------------

### Collapse Methods

Source: https://getbootstrap.com/docs/5.3/components/accordion

Interact with the collapse component using its available methods. All methods are asynchronous and return before the transition completes.

```APIDOC
## Methods

**All API methods are asynchronous and start a transition.** They return to the caller as soon as the transition is started, but before it ends. In addition, a method call on a transitioning component will be ignored. Learn more in our JavaScript docs.

Activates your content as a collapsible element. Accepts an optional options `object`.

You can create a collapse instance with the constructor, for example:

```javascript
const bsCollapse = new bootstrap.Collapse('#myCollapse', {
  toggle: false
})
```

| Method | Description |
|---|---|
| `dispose` | Destroys an element’s collapse. (Removes stored data on the DOM element) |
| `getInstance` | Static method which allows you to get the collapse instance associated to a DOM element, you can use it like this: `bootstrap.Collapse.getInstance(element)`. |
| `getOrCreateInstance` | Static method which returns a collapse instance associated to a DOM element or create a new one in case it wasn’t initialized. You can use it like this: `bootstrap.Collapse.getOrCreateInstance(element)`. |
| `hide` | Hides a collapsible element. **Returns to the caller before the collapsible element has actually been hidden** (e.g., before the `hidden.bs.collapse` event occurs). |
| `show` | Shows a collapsible element. **Returns to the caller before the collapsible element has actually been shown** (e.g., before the `shown.bs.collapse` event occurs). |
| `toggle` | Toggles a collapsible element to shown or hidden. **Returns to the caller before the collapsible element has actually been shown or hidden** (i.e. before the `shown.bs.collapse` or `hidden.bs.collapse` event occurs). |
```

--------------------------------

### Bootstrap Collapse Plugin Usage with Data Attributes

Source: https://getbootstrap.com/docs/5.3/components/accordion

Demonstrates how to use Bootstrap's collapse plugin with data attributes to create collapsible elements. This method requires adding specific attributes to HTML elements to control their visibility.

```html
<button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Link with href
</button>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Some placeholder content for the collapse component. This content will be revealed or hidden.
  </div>
</div>

<button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
  Toggle width collapse
</button>
<div style="min-height: 120px;">
  <div class="collapse collapse-horizontal" id="collapseWidthExample">
    <div class="card card-body" style="width: 300px;">
      This is some placeholder content for a horizontal collapse. It's hidden by default and shown when the button is clicked.
    </div>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-bs-target
  </button>
</p>
<div style="height: 0px;">
  <div class="collapse multi-collapse" id="multiCollapseExample1">...
  </div>
  <div class="collapse multi-collapse" id="multiCollapseExample2">...
  </div>
</div>

```

--------------------------------

### Collapse Options

Source: https://getbootstrap.com/docs/5.3/components/accordion

Configure the behavior of the collapse component using data attributes or JavaScript options. Options can be passed via `data-bs-config` or individual `data-bs-*` attributes, with individual attributes overriding `data-bs-config`.

```APIDOC
## Options

As options can be passed via data attributes or JavaScript, you can append an option name to `data-bs-`, as in `data-bs-animation="{value}"`. Make sure to change the case type of the option name from “ _camelCase_ ” to “ _kebab-case_ ” when passing the options via data attributes. For example, use `data-bs-custom-class="beautifier"` instead of `data-bs-customClass="beautifier"`.

As of Bootstrap 5.2.0, all components support an **experimental** reserved data attribute `data-bs-config` that can house simple component configuration as a JSON string. When an element has `data-bs-config='{"delay":0, "title":123}'` and `data-bs-title="456"` attributes, the final `title` value will be `456` and the separate data attributes will override values given on `data-bs-config`. In addition, existing data attributes are able to house JSON values like `data-bs-delay='{"show":0,"hide":150}'`.

--------------------------------

### Collapse Events

Source: https://getbootstrap.com/docs/5.3/components/accordion

Listen for events triggered by the collapse component to execute custom logic during different stages of the collapse lifecycle.

```APIDOC
## Events

Bootstrap’s collapse class exposes a few events for hooking into collapse functionality.

| Event type | Description |
|---|---|
| `hide.bs.collapse` | This event is fired immediately when the `hide` method has been called. |
| `hidden.bs.collapse` | This event is fired when a collapse element has been hidden from the user (will wait for CSS transitions to complete). |
| `show.bs.collapse` | This event fires immediately when the `show` instance method is called. |
| `shown.bs.collapse` | This event is fired when a collapse element has been made visible to the user (will wait for CSS transitions to complete). |

```javascript
const myCollapsible = document.getElementById('myCollapsible')
myCollapsible.addEventListener('hidden.bs.collapse', event => {
  // do something...
})
```
```

--------------------------------

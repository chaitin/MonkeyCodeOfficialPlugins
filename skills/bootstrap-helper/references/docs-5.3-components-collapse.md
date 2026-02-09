### Basic Collapse Example (HTML)

Source: https://getbootstrap.com/docs/5.3/components/collapse

Demonstrates how to use the collapse plugin with both link and button triggers. The `.collapse` class hides content, `.collapsing` is applied during transitions, and `.collapse.show` displays content. Requires Bootstrap's JavaScript.

```html
<p class="d-inline-flex gap-1">
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-bs-target
  </button>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
  </div>
</div>
```

--------------------------------

### Horizontal Collapse Example (HTML)

Source: https://getbootstrap.com/docs/5.3/components/collapse

Shows how to implement horizontal collapsing by adding the `.collapse-horizontal` class and setting a `width` on the immediate child element. This transitions the `width` instead of `height`. Requires Bootstrap's JavaScript.

```html
<p>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
    Toggle width collapse
  </button>
</p>
<div style="min-height: 120px;">
  <div class="collapse collapse-horizontal" id="collapseWidthExample">
    <div class="card card-body" style="width: 300px;">
      This is some placeholder content for a horizontal collapse. It’s hidden by default and shown when triggered.
    </div>
  </div>
</div>
```

--------------------------------

### Initialize Bootstrap Collapse via JavaScript

Source: https://getbootstrap.com/docs/5.3/components/collapse

This snippet shows how to select all elements with the class 'collapse' and initialize them as Bootstrap collapse instances. It uses `document.querySelectorAll` to get a NodeList of elements and then maps over them to create new `bootstrap.Collapse` objects. This is useful for enabling collapse functionality on multiple elements simultaneously.

```javascript
const collapseElementList = document.querySelectorAll('.collapse')
const collapseList = [...collapseElementList].map(collapseEl => new bootstrap.Collapse(collapseEl))
```

--------------------------------

### Collapse Initialization and Usage

Source: https://getbootstrap.com/docs/5.3/components/collapse

This section details how to use the Collapse component via data attributes and JavaScript, including configuration options.

```APIDOC
## Data Attributes

--------------------------------

### Handle Bootstrap Collapse Hidden Event

Source: https://getbootstrap.com/docs/5.3/components/collapse

This example illustrates how to listen for the `hidden.bs.collapse` event on a specific collapsible element. When the collapse element is fully hidden (after CSS transitions complete), the provided event listener function is executed. This allows you to trigger custom actions or update your application's state after a collapse has been hidden.

```javascript
const myCollapsible = document.getElementById('myCollapsible')
myCollapsible.addEventListener('hidden.bs.collapse', event => {
  // do something...
})
```

--------------------------------

### Collapse Methods

Source: https://getbootstrap.com/docs/5.3/components/collapse

Details on the available methods for controlling the Collapse component programmatically.

```APIDIDOC
## Methods

--------------------------------

### Create Bootstrap Collapse Instance with Options

Source: https://getbootstrap.com/docs/5.3/components/collapse

This code demonstrates how to create a new Bootstrap collapse instance programmatically using the `bootstrap.Collapse` constructor. It targets a specific element with the ID 'myCollapse' and initializes it with the `toggle` option set to `false`, preventing it from toggling immediately upon creation. This allows for more fine-grained control over the collapse behavior.

```javascript
const bsCollapse = new bootstrap.Collapse('#myCollapse', {
  toggle: false
})
```

--------------------------------

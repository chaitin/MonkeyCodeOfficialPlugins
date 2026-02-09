### Handle Tab Shown Event (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/list-group

This example demonstrates how to listen for the `shown.bs.tab` event, which fires after a new tab has been activated. It provides access to the newly activated tab (`event.target`) and the previously active tab (`event.relatedTarget`).

```javascript
const tabElms = document.querySelectorAll('a[data-bs-toggle="list"]')
tabElms.forEach(tabElm => {
  tabElm.addEventListener('shown.bs.tab', event => {
    event.target // newly activated tab
    event.relatedTarget // previous active tab
  })
})
```

--------------------------------

### Initialize Bootstrap Tab Instance (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/list-group

You can create a new tab instance using the `bootstrap.Tab` constructor, passing a CSS selector for the tab element. This method is asynchronous and returns control to the caller immediately after the transition starts.

```javascript
const bsTab = new bootstrap.Tab('#myTab')
```

--------------------------------

### Bootstrap Horizontal List Group

Source: https://getbootstrap.com/docs/5.3/components/list-group

Displays list group items horizontally using the `.list-group-horizontal` class. This example shows the base horizontal layout.

```html
<ul class="list-group list-group-horizontal">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
```

--------------------------------

### Bootstrap Numbered List Group

Source: https://getbootstrap.com/docs/5.3/components/list-group

Creates a numbered list group using the `.list-group-numbered` class. Numbers are generated via CSS for better placement and customization. This example uses an `<ol>` element for semantic correctness.

```html
<ol class="list-group list-group-numbered">
  <li class="list-group-item">A list item</li>
  <li class="list-group-item">A list item</li>
  <li class="list-group-item">A list item</li>
</ol>
```

--------------------------------

### Bootstrap List Group Tab Structure (HTML)

Source: https://getbootstrap.com/docs/5.3/components/list-group

This HTML structure demonstrates the basic setup for a list group that functions as tabs. It includes a list group for navigation and a tab content area for displaying pane content. Ensure Bootstrap's CSS is included for proper styling.

```html
<div class="row">
  <div class="col-4">
    <div class="list-group" id="list-tab" role="tablist">
      <a class="list-group-item list-group-item-action active" id="list-home-list" data-bs-toggle="list" href="#list-home" role="tab" aria-controls="list-home">Home</a>
      <a class="list-group-item list-group-item-action" id="list-profile-list" data-bs-toggle="list" href="#list-profile" role="tab" aria-controls="list-profile">Profile</a>
      <a class="list-group-item list-group-item-action" id="list-messages-list" data-bs-toggle="list" href="#list-messages" role="tab" aria-controls="list-messages">Messages</a>
      <a class="list-group-item list-group-item-action" id="list-settings-list" data-bs-toggle="list" href="#list-settings" role="tab" aria-controls="list-settings">Settings</a>
    </div>
  </div>
  <div class="col-8">
    <div class="tab-content" id="nav-tabContent">
      <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">...</div>
      <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">...</div>
      <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">...</div>
      <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">...</div>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap List Group with Radio Buttons

Source: https://getbootstrap.com/docs/5.3/components/list-group

This example shows how to implement radio buttons within Bootstrap list group items. It uses the 'form-check-input' and 'form-check-label' classes for styling and ensures that radio buttons within the same group share the same 'name' attribute for proper functionality. Accessibility is maintained through label association.

```html
<ul class="list-group">
  <li class="list-group-item">
    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="firstRadio" checked>
    <label class="form-check-label" for="firstRadio">First radio</label>
  </li>
  <li class="list-group-item">
    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="secondRadio">
    <label class="form-check-label" for="secondRadio">Second radio</label>
  </li>
  <li class="list-group-item">
    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="thirdRadio">
    <label class="form-check-label" for="thirdRadio">Third radio</label>
  </li>
</ul>
```

--------------------------------

### Bootstrap List Group Item Variants (HTML)

Source: https://getbootstrap.com/docs/5.3/components/list-group

Demonstrates how to apply contextual background and color variants to list group items using Bootstrap's predefined classes. These classes provide distinct styling for different states or categories of list items.

```html
<ul class="list-group">
  <li class="list-group-item">A simple default list group item</li>
  
  <li class="list-group-item list-group-item-primary">A simple primary list group item</li>
  <li class="list-group-item list-group-item-secondary">A simple secondary list group item</li>
  <li class="list-group-item list-group-item-success">A simple success list group item</li>
  <li class="list-group-item list-group-item-danger">A simple danger list group item</li>
  <li class="list-group-item list-group-item-warning">A simple warning list group item</li>
  <li class="list-group-item list-group-item-info">A simple info list group item</li>
  <li class="list-group-item list-group-item-light">A simple light list group item</li>
  <li class="list-group-item list-group-item-dark">A simple dark list group item</li>
</ul>
```

--------------------------------

### Bootstrap List Group Action Variants (HTML)

Source: https://getbootstrap.com/docs/5.3/components/list-group

Shows how to style list group items as actions for anchor (`<a>`) or button (`<button>`) elements using the `.list-group-item-action` class in conjunction with contextual variants. Includes hover styles and demonstrates the `.active` state for indicating selection.

```html
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action">A simple default list group item</a>
  
  <a href="#" class="list-group-item list-group-item-action list-group-item-primary">A simple primary list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-secondary">A simple secondary list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-success">A simple success list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-danger">A simple danger list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-warning">A simple warning list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-info">A simple info list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-light">A simple light list group item</a>
  <a href="#" class="list-group-item list-group-item-action list-group-item-dark">A simple dark list group item</a>
</div>
```

--------------------------------

### Basic List Group HTML

Source: https://getbootstrap.com/docs/5.3/components/list-group

Demonstrates the fundamental structure of a Bootstrap list group using an unordered list and 'list-group' class. Each list item requires the 'list-group-item' class.

```html
<ul class="list-group">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
  <li class="list-group-item">A fourth item</li>
  <li class="list-group-item">And a fifth one</li>
</ul>
```

--------------------------------

### Actionable List Group Items with Links HTML

Source: https://getbootstrap.com/docs/5.3/components/list-group

Illustrates creating actionable list group items using anchor tags (`<a>`). The '.list-group-item-action' class enables hover, focus, and active states. A disabled item is shown using '.disabled' and 'aria-disabled="true"'.

```html
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
    The current link item
  </a>
  <a href="#" class="list-group-item list-group-item-action">A second link item</a>
  <a href="#" class="list-group-item list-group-item-action">A third link item</a>
  <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
  <a href="#" class="list-group-item list-group-item-action disabled" aria-disabled="true">A disabled link item</a>
</div>
```

--------------------------------

### Bootstrap List Group with Actionable Items

Source: https://getbootstrap.com/docs/5.3/components/list-group

This snippet shows a basic Bootstrap list group where each item is an anchor tag, making it actionable. It includes styling for active states and different content layouts within list items. No external JavaScript dependencies are required for this basic structure.

```html
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small>3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small>And some small print.</small>
  </a>
  <a href="#" class="list-group-item list-group-item-action">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </a>
  <a href="#" class="list-group-item list-group-item-action">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </a>
</div>
```

--------------------------------

### Bootstrap Responsive Horizontal List Groups

Source: https://getbootstrap.com/docs/5.3/components/list-group

Demonstrates responsive horizontal list groups that adapt to different screen sizes using variants like `.list-group-horizontal-sm`, `.list-group-horizontal-md`, etc. These variants control the breakpoint at which the list group becomes horizontal.

```html
<ul class="list-group list-group-horizontal-sm">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
<ul class="list-group list-group-horizontal-md">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
<ul class="list-group list-group-horizontal-lg">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
<ul class="list-group list-group-horizontal-xl">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
<ul class="list-group list-group-horizontal-xxl">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
```

--------------------------------

### Actionable List Group Items with Buttons HTML

Source: https://getbootstrap.com/docs/5.3/components/list-group

Demonstrates creating actionable list group items using button elements (`<button>`). Similar to links, '.list-group-item-action' is used. The 'disabled' attribute is shown for disabling buttons.

```html
<div class="list-group">
  <button type="button" class="list-group-item list-group-item-action active" aria-current="true">
    The current button
  </button>
  <button type="button" class="list-group-item list-group-item-action">A second button item</button>
  <button type="button" class="list-group-item list-group-item-action">A third button item</button>
  <button type="button" class="list-group-item list-group-item-action">A fourth button item</button>
  <button type="button" class="list-group-item list-group-item-action" disabled>A disabled button item</button>
</div>
```

--------------------------------

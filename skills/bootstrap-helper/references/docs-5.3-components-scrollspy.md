### Bootstrap Scrollspy Navigation Example

Source: https://getbootstrap.com/docs/5.3/components/scrollspy

This example demonstrates how to implement Bootstrap's Scrollspy component. It includes a navigation bar with dropdowns and a scrollable content area. The `data-bs-spy` and `data-bs-target` attributes are crucial for linking the navigation to the scrollable content, enabling the highlighting of active links as the user scrolls. The `data-bs-smooth-scroll` attribute provides a smooth scrolling experience.

```html
<nav id="navbar-example2" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Navbar</a>
  <ul class="nav nav-pills">
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading1">First</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading2">Second</a>
    </li>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#scrollspyHeading3">Third</a></li>
        <li><a class="dropdown-item" href="#scrollspyHeading4">Fourth</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#scrollspyHeading5">Fifth</a></li>
      </ul>
    </li>
  </ul>
</nav>
<div data-bs-spy="scroll" data-bs-target="#navbar-example2" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  <h4 id="scrollspyHeading1">First heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading2">Second heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading3">Third heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading4">Fourth heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading5">Fifth heading</h4>
  <p>...</p>
</div>
```

--------------------------------

### Bootstrap Scrollspy with Simple Anchors

Source: https://getbootstrap.com/docs/5.3/components/scrollspy

This example shows Scrollspy used with basic anchor `<a>` elements, not limited to navigation components. Similar to the list group example, it uses `data-bs-spy='scroll'` on a scrollable container and `data-bs-target` to link to the anchor IDs. The `data-bs-offset` attribute can be used to adjust the scroll offset.

```html
<div class="row">
  <div class="col-4">
    <div id="simple-list-example" class="d-flex flex-column gap-2 simple-list-example-scrollspy text-center">
      <a class="p-1 rounded" href="#simple-list-item-1">Item 1</a>
      <a class="p-1 rounded" href="#simple-list-item-2">Item 2</a>
      <a class="p-1 rounded" href="#simple-list-item-3">Item 3</a>
      <a class="p-1 rounded" href="#simple-list-item-4">Item 4</a>
      <a class="p-1 rounded" href="#simple-list-item-5">Item 5</a>
    </div>
  </div>
  <div class="col-8">
    <div data-bs-spy="scroll" data-bs-target="#simple-list-example" data-bs-offset="0" data-bs-smooth-scroll="true" class="scrollspy-example" tabindex="0">
      <h4 id="simple-list-item-1">Item 1</h4>
      <p>...</p>
      <h4 id="simple-list-item-2">Item 2</h4>
      <p>...</p>
      <h4 id="simple-list-item-3">Item 3</h4>
      <p>...</p>
      <h4 id="simple-list-item-4">Item 4</h4>
      <p>...</p>
      <h4 id="simple-list-item-5">Item 5</h4>
      <p>...</p>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Scrollspy HTML Structure

Source: https://getbootstrap.com/docs/5.3/components/scrollspy

Example HTML structure for implementing Bootstrap Scrollspy using data attributes. The `data-bs-spy` attribute is applied to the element to be spied on, and `data-bs-target` points to the navigation element.

```html
<body data-bs-spy="scroll" data-bs-target="#navbar-example">
  ...
  <div id="navbar-example">
    <ul class="nav nav-tabs" role="tablist">
      ...
    </ul>
  </div>
  ...
</body>
```

--------------------------------

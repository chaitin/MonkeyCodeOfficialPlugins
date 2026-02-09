### Pass Options via JavaScript (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/modal

Demonstrates how to initialize a modal with specific options set via JavaScript. This example disables the keyboard escape key to close the modal, overriding the default behavior.

```javascript
const myModal = new bootstrap.Modal('#myModal', {
  keyboard: false
})
```

--------------------------------

### Add Popover and Tooltip in Bootstrap Modal

Source: https://getbootstrap.com/docs/5.3/components/modal

This code shows how to include interactive elements like popovers and tooltips within a Bootstrap modal. The example demonstrates a button that triggers a popover and links that display tooltips on hover. Bootstrap automatically dismisses these elements when the modal is closed.

```html
<div class="modal-body">
  <h2 class="fs-5">Popover in a modal</h2>
  <p>This <button class="btn btn-secondary" data-bs-toggle="popover" title="Popover title" data-bs-content="Popover body content is set in this attribute.">button</button> triggers a popover on click.</p>
  <hr>
  <h2 class="fs-5">Tooltips in a modal</h2>
  <p><a href="#" data-bs-toggle="tooltip" title="Tooltip">This link</a> and <a href="#" data-bs-toggle="tooltip" title="Tooltip">that link</a> have tooltips on hover.</p>
</div>
```

--------------------------------

### Static Bootstrap Modal Structure (HTML)

Source: https://getbootstrap.com/docs/5.3/components/modal

This HTML code provides a static structure for a Bootstrap modal. It includes the necessary container elements for the modal dialog, content, header, body, and footer. The header contains a title and a dismiss button, while the footer has close and save buttons. This example is useful for understanding the basic layout before adding dynamic behavior.

```html
<div class="modal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

```

--------------------------------

### Create Scrollable Modal Body with Bootstrap

Source: https://getbootstrap.com/docs/5.3/components/modal

This example demonstrates how to create a modal where the content within the modal body scrolls independently of the page. This is achieved by adding the `modal-dialog-scrollable` class to the `.modal-dialog` element. It's useful for modals with a large amount of content that needs to fit within the viewport.

```html
<div class="modal-dialog modal-dialog-scrollable">
  ...
</div>
```

--------------------------------

### Initialize Modal via JavaScript (JavaScript)

Source: https://getbootstrap.com/docs/5.3/components/modal

Initializes a Bootstrap modal instance using JavaScript. This allows for programmatic control and passing configuration options. The modal can be selected by its ID or a CSS selector.

```javascript
const myModal = new bootstrap.Modal(document.getElementById('myModal'), options)
// or
const myModalAlternative = new bootstrap.Modal('#myModal', options)
```

--------------------------------

### Bootstrap Grid Layout in Modal Body

Source: https://getbootstrap.com/docs/5.3/components/modal

Demonstrates how to use Bootstrap's grid system (columns and rows) to create responsive layouts within the modal body. This snippet showcases various column classes like col-md-4, ms-auto, and nested rows for complex arrangements.

```html
<div class="modal-body">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4">.col-md-4</div>
      <div class="col-md-4 ms-auto">.col-md-4 .ms-auto</div>
    </div>
    <div class="row">
      <div class="col-md-3 ms-auto">.col-md-3 .ms-auto</div>
      <div class="col-md-2 ms-auto">.col-md-2 .ms-auto</div>
    </div>
    <div class="row">
      <div class="col-md-6 ms-auto">.col-md-6 .ms-auto</div>
    </div>
    <div class="row">
      <div class="col-sm-9">
        Level 1: .col-sm-9
        <div class="row">
          <div class="col-8 col-sm-6">
            Level 2: .col-8 .col-sm-6
          </div>
          <div class="col-4 col-sm-6">
            Level 2: .col-4 .col-sm-6
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Responsive Fullscreen Modals

Source: https://getbootstrap.com/docs/5.3/components/modal

Generates responsive fullscreen modal styles using Sass loops and media queries based on defined breakpoints. This allows modals to occupy the full viewport on smaller screens.

```scss
@each $breakpoint in map-keys($grid-breakpoints) {
  $infix: breakpoint-infix($breakpoint, $grid-breakpoints);
  $postfix: if($infix != "", $infix + "-down", "");

  @include media-breakpoint-down($breakpoint) {
    .modal-fullscreen#{$postfix} {
      width: 100vw;
      max-width: none;
      height: 100%;
      margin: 0;

      .modal-content {
        height: 100%;
        border: 0;
        @include border-radius(0);
      }

      .modal-header,
      .modal-footer {
        @include border-radius(0);
      }

      .modal-body {
        overflow-y: auto;
      }
    }
  }
}

```

--------------------------------

### Live Bootstrap Modal Demo with Trigger Button (HTML)

Source: https://getbootstrap.com/docs/5.3/components/modal

This HTML snippet demonstrates a live Bootstrap modal, including the button to trigger its display and the modal's structure itself. The button uses 'data-bs-toggle' and 'data-bs-target' attributes to link to the modal. The modal includes a fade animation and is configured with ARIA attributes for accessibility. It features a header with a title and dismiss button, a body, and a footer with action buttons.

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

```

--------------------------------

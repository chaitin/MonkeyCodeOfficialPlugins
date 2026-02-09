### Bootstrap Input Group Basic Examples

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Demonstrates various ways to use Bootstrap's input group component with text or buttons on one or both sides of input fields and textareas. Includes examples for vanity URLs and currency inputs.

```html
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient’s username" aria-label="Recipient’s username" aria-describedby="basic-addon2">
  <span class="input-group-text" id="basic-addon2">@example.com</span>
</div>

<div class="mb-3">
  <label for="basic-url" class="form-label">Your vanity URL</label>
  <div class="input-group">
    <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4">
  </div>
  <div class="form-text" id="basic-addon4">Example help text goes outside the input group.</div>
</div>

<div class="input-group mb-3">
  <span class="input-group-text">$
  </span>
  <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
  <span class="input-group-text">.00</span>
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Username" aria-label="Username">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Server" aria-label="Server">
</div>

<div class="input-group">
  <span class="input-group-text">With textarea</span>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>
```

--------------------------------

### Bootstrap Input Group Sizing Examples

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Demonstrates how to apply sizing to entire input groups using `.input-group-sm`, default sizing, and `.input-group-lg`. Note that individual element sizing within the group is not supported.

```html
<div class="input-group input-group-sm mb-3">
  <span class="input-group-text" id="inputGroup-sizing-sm">Small</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">
</div>

<div class="input-group mb-3">
  <span class="input-group-text" id="inputGroup-sizing-default">Default</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
</div>

<div class="input-group input-group-lg">
  <span class="input-group-text" id="inputGroup-sizing-lg">Large</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
</div>
```

--------------------------------

### Bootstrap Input Group with Multiple Addons

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Shows how to use multiple addons in an input group, which can be combined with checkbox or radio input variations. This example includes currency symbols and decimal values.

```html
<div class="input-group mb-3">
  <span class="input-group-text">$</span>
  <span class="input-group-text">0.00</span>
  <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
</div>

<div class="input-group">
  <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
  <span class="input-group-text">$</span>
  <span class="input-group-text">0.00</span>
</div>
```

--------------------------------

### Bootstrap Input Group Border Radius Example

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Illustrates how border-radius styles are applied only to the first and last children of an input group. This example shows a hidden input that does not affect the border-radius.

```html
<div class="input-group">
  <span class="input-group-text" id="visible-addon">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="visible-addon">
  <input type="text" class="form-control d-none" placeholder="Hidden input" aria-label="Hidden input" aria-describedby="visible-addon">
</div>
```

--------------------------------

### Bootstrap Input Group Wrapping Example

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Shows how to disable the default wrapping behavior of input groups by applying the `.flex-nowrap` class. This is useful for ensuring input groups remain on a single line.

```html
<div class="input-group flex-nowrap">
  <span class="input-group-text" id="addon-wrapping">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">
</div>
```

--------------------------------

### Bootstrap Input Group with Dropdown Button (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/input-group

This snippet shows how to create an input group with a dropdown button. It includes examples of the dropdown positioned to the left and right of the input field, as well as a configuration with two dropdown buttons.

```html
<div class="input-group mb-3">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with dropdown button">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" aria-label="Text input with dropdown button">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>

<div class="input-group">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action before</a></li>
    <li><a class="dropdown-item" href="#">Another action before</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with 2 dropdown buttons">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>
```

--------------------------------

### Bootstrap Segmented Button Group with Dropdown (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/input-group

This snippet demonstrates how to create segmented button groups within an input group, featuring a primary action button and a dropdown toggle. Examples include the segmented button group positioned before and after the input field.

```html
<div class="input-group mb-3">
  <button type="button" class="btn btn-outline-secondary">Action</button>
  <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with segmented dropdown button">
</div>

<div class="input-group">
  <input type="text" class="form-control" aria-label="Text input with segmented dropdown button">
  <button type="button" class="btn btn-outline-secondary">Action</button>
  <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>
```

--------------------------------

### Bootstrap Input Group with Button Addons

Source: https://getbootstrap.com/docs/5.3/forms/input-group

Demonstrates various configurations of input groups with button addons. Buttons can be placed before or after the input field, and multiple buttons can be used.

```html
<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button" id="button-addon1">Button</button>
  <input type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient’s username" aria-label="Recipient’s username" aria-describedby="button-addon2">
  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
</div>

<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <input type="text" class="form-control" placeholder="" aria-label="Example text with two button addons">
</div>

<div class="input-group">
  <input type="text" class="form-control" placeholder="Recipient’s username" aria-label="Recipient’s username with two button addons">
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <button class="btn btn-outline-secondary" type="button">Button</button>
</div>
```

--------------------------------

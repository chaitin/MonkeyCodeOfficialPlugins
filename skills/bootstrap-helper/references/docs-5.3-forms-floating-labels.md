### Bootstrap Floating Input Group HTML

Source: https://getbootstrap.com/docs/5.3/forms/floating-labels

Illustrates the integration of Bootstrap's floating labels with input groups. This example shows how to combine a text prefix (like '@') with a floating input field for usernames. It also covers handling form validation feedback within input groups.

```html
<div class="input-group mb-3">
  <span class="input-group-text">@</span>
  <div class="form-floating">
    <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Username">
    <label for="floatingInputGroup1">Username</label>
  </div>
</div>
<div class="input-group has-validation">
  <span class="input-group-text">@</span>
  <div class="form-floating is-invalid">
    <input type="text" class="form-control is-invalid" id="floatingInputGroup2" placeholder="Username" required>
    <label for="floatingInputGroup2">Username</label>
  </div>
  <div class="invalid-feedback">
    Please choose a username.
  </div>
</div>
```

--------------------------------

### Floating Labels for Textareas in Bootstrap HTML

Source: https://getbootstrap.com/docs/5.3/forms/floating-labels

Provides examples of using floating labels with Bootstrap's `<textarea>` elements. By default, textareas match input height. Custom heights can be set using explicit `height` CSS, not the `rows` attribute.

```html
<div class="form-floating">
  <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
  <label for="floatingTextarea">Comments</label>
</div>
```

```html
<div class="form-floating">
  <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
  <label for="floatingTextarea2">Comments</label>
</div>
```

--------------------------------

### Bootstrap Floating Form Layout HTML

Source: https://getbootstrap.com/docs/5.3/forms/floating-labels

Shows how to structure forms using Bootstrap's grid system alongside floating labels. This example places form elements, including text inputs and select dropdowns, within column classes for responsive layout. It ensures proper alignment and spacing.

```html
<div class="row g-2">
  <div class="col-md">
    <div class="form-floating">
      <input type="email" class="form-control" id="floatingInputGrid" placeholder="name@example.com" value="mdo@example.com">
      <label for="floatingInputGrid">Email address</label>
    </div>
  </div>
  <div class="col-md">
    <div class="form-floating">
      <select class="form-select" id="floatingSelectGrid">
        <option selected>Open this select menu</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
      <label for="floatingSelectGrid">Works with selects</label>
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Floating Plaintext Input HTML

Source: https://getbootstrap.com/docs/5.3/forms/floating-labels

Demonstrates how to use Bootstrap's `.form-control-plaintext` class with floating labels for displaying readonly text. This is useful for toggling between editable inputs and static text without altering page layout. It shows examples for both empty and pre-filled inputs.

```html
<div class="form-floating mb-3">
  <input type="email" readonly class="form-control-plaintext" id="floatingEmptyPlaintextInput" placeholder="name@example.com">
  <label for="floatingEmptyPlaintextInput">Empty input</label>
</div>
<div class="form-floating mb-3">
  <input type="email" readonly class="form-control-plaintext" id="floatingPlaintextInput" placeholder="name@example.com" value="name@example.com">
  <label for="floatingPlaintextInput">Input with value</label>
</div>
```

--------------------------------

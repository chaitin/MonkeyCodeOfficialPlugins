### Bootstrap File Input Examples

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Provides examples for various file input configurations in Bootstrap, including default, multiple file selection, disabled state, and small/large sizing. These examples showcase the flexibility of Bootstrap's form controls for file uploads.

```html
<div class="mb-3">
  <label for="formFile" class="form-label">Default file input example</label>
  <input class="form-control" type="file" id="formFile">
</div>
<div class="mb-3">
  <label for="formFileMultiple" class="form-label">Multiple files input example</label>
  <input class="form-control" type="file" id="formFileMultiple" multiple>
</div>
<div class="mb-3">
  <label for="formFileDisabled" class="form-label">Disabled file input example</label>
  <input class="form-control" type="file" id="formFileDisabled" disabled>
</div>
<div class="mb-3">
  <label for="formFileSm" class="form-label">Small file input example</label>
  <input class="form-control form-control-sm" id="formFileSm" type="file">
</div>
<div>
  <label for="formFileLg" class="form-label">Large file input example</label>
  <input class="form-control form-control-lg" id="formFileLg" type="file">
</div>
```

--------------------------------

### Bootstrap Datalist Example

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Demonstrates the use of datalists in Bootstrap for creating input fields with predefined options that support autocompletion. This example shows a search input where users can type to filter options like city names.

```html
<label for="exampleDataList" class="form-label">Datalist example</label>
<input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
<datalist id="datalistOptions">
  <option value="San Francisco">
  <option value="New York">
  <option value="Seattle">
  <option value="Los Angeles">
  <option value="Chicago">
</datalist>
```

--------------------------------

### Basic Form Controls Example (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Demonstrates the basic structure for email input and textarea form controls using Bootstrap classes. Includes labels and input fields.

```html
<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>
```

--------------------------------

### Inline Form Text Example (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Demonstrates how to use inline form text with Bootstrap's `.form-text` class on a `<span>` element. This provides concise, on-the-fly help text associated with an input.

```html
<div class="row g-3 align-items-center">
  <div class="col-auto">
    <label for="inputPassword6" class="col-form-label">Password</label>
  </div>
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
  <div class="col-auto">
    <span id="passwordHelpInline" class="form-text">
      Must be 8-20 characters long.
    </span>
  </div>
</div>
```

--------------------------------

### Disabled Form Controls (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Provides examples of disabled input fields. The `disabled` attribute prevents user interaction, including typing and focusing, and visually grays out the input.

```html
<input class="form-control" type="text" placeholder="Disabled input" aria-label="Disabled input example" disabled>
<input class="form-control" type="text" value="Disabled readonly input" aria-label="Disabled input example" disabled readonly>
```

--------------------------------

### Form Control Sizing (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Illustrates how to apply different sizing classes (.form-control-lg, .form-control-sm) to input fields for visual adjustments. Shows large, default, and small input sizes.

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

--------------------------------

### Form Text with Help Block (HTML)

Source: https://getbootstrap.com/docs/5.3/forms/form-control

Shows how to associate block-level form text with an input using `aria-describedby`. This is crucial for accessibility, providing context for password requirements.

```html
<label for="inputPassword5" class="form-label">Password</label>
<input type="password" id="inputPassword5" class="form-control" aria-describedby="passwordHelpBlock">
<div id="passwordHelpBlock" class="form-text">
  Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
</div>
```

--------------------------------

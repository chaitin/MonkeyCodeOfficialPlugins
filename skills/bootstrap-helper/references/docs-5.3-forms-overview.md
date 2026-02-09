### Basic Form Example with Bootstrap

Source: https://getbootstrap.com/docs/5.3/forms/overview

Demonstrates a standard HTML form using Bootstrap classes for styling input fields, labels, checkboxes, and a submit button. It includes basic form validation feedback and help text.

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

--------------------------------

### Form Accessibility Techniques in HTML

Source: https://getbootstrap.com/docs/5.3/forms/overview

Demonstrates various HTML techniques for providing accessible names to form controls, including using `<label>`, `.visually-hidden` class, `aria-labelledby`, `title` attribute, and `aria-label`. It also mentions the fallback behavior of the `placeholder` attribute.

```html
<label for="username">Username</label>
<input type="text" id="username">

<label for="email" class="visually-hidden">Email Address</label>
<input type="email" id="email">

<label id="password-label">Password</label>
<input type="password" aria-labelledby="password-label">

<input type="text" title="Enter your search query">

<input type="text" aria-label="Search">

<input type="text" placeholder="Enter your username">

```

--------------------------------

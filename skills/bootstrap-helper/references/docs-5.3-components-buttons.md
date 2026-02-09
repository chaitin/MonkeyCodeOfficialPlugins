### Toggle Button States

Source: https://getbootstrap.com/docs/5.3/components/buttons

Demonstrates how to use `data-bs-toggle="button"` to create toggleable buttons and links. Includes examples for active and disabled states, and the necessary ARIA attributes.

```APIDOC
## Toggle Button States

--------------------------------

### Bootstrap Button JavaScript Methods

Source: https://getbootstrap.com/docs/5.3/components/buttons

Provides examples of using Bootstrap's JavaScript API to control button instances. Covers creating a new instance, retrieving existing instances, and programmatically toggling button states. This allows for dynamic manipulation of button behavior.

```javascript
const bsButton = new bootstrap.Button('#myButton')

// Method to destroy an element's button instance
// bsButton.dispose()

// Static method to get an existing button instance
// bootstrap.Button.getInstance(element)

// Static method to get or create a button instance
// bootstrap.Button.getOrCreateInstance(element)

// Method to toggle the push state of a button
// bsButton.toggle()

// Example: Toggling all buttons on the page
document.querySelectorAll('.btn').forEach(buttonElement => {
  const button = bootstrap.Button.getOrCreateInstance(buttonElement)
  button.toggle()
})
```

--------------------------------

### Bootstrap Button Sizes

Source: https://getbootstrap.com/docs/5.3/components/buttons

Shows how to adjust the size of Bootstrap buttons using predefined classes like `.btn-lg` for larger buttons and `.btn-sm` for smaller ones. It also includes an example of custom sizing using CSS variables.

```html
<button type="button" class="btn btn-primary btn-lg">Large button</button>
<button type="button" class="btn btn-secondary btn-lg">Large button</button>

<button type="button" class="btn btn-primary btn-sm">Small button</button>
<button type="button" class="btn btn-secondary btn-sm">Small button</button>

<button type="button" class="btn btn-primary"
        style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">
  Custom button
</button>
```

--------------------------------

### Toggle Button States with HTML

Source: https://getbootstrap.com/docs/5.3/components/buttons

Demonstrates how to create toggleable buttons using the `data-bs-toggle="button"` attribute. Includes examples for default, primary, active, and disabled states for both button and link elements. Ensure `aria-pressed` is set for accessibility on pre-toggled buttons.

```html
<p class="d-inline-flex gap-1">
  <button type="button" class="btn" data-bs-toggle="button">Toggle button</button>
  <button type="button" class="btn active" data-bs-toggle="button" aria-pressed="true">Active toggle button</button>
  <button type="button" class="btn" disabled data-bs-toggle="button">Disabled toggle button</button>
</p>
<p class="d-inline-flex gap-1">
  <button type="button" class="btn btn-primary" data-bs-toggle="button">Toggle button</button>
  <button type="button" class="btn btn-primary active" data-bs-toggle="button" aria-pressed="true">Active toggle button</button>
  <button type="button" class="btn btn-primary" disabled data-bs-toggle="button">Disabled toggle button</button>
</p>

<p class="d-inline-flex gap-1">
  <a href="#" class="btn" role="button" data-bs-toggle="button">Toggle link</a>
  <a href="#" class="btn active" role="button" data-bs-toggle="button" aria-pressed="true">Active toggle link</a>
  <a class="btn disabled" aria-disabled="true" role="button" data-bs-toggle="button">Disabled toggle link</a>
</p>
<p class="d-inline-flex gap-1">
  <a href="#" class="btn btn-primary" role="button" data-bs-toggle="button">Toggle link</a>
  <a href="#" class="btn btn-primary active" role="button" data-bs-toggle="button" aria-pressed="true">Active toggle link</a>
  <a class="btn btn-primary disabled" aria-disabled="true" role="button" data-bs-toggle="button">Disabled toggle link</a>
</p>
```

--------------------------------

### Custom Bootstrap Button Variant (SCSS)

Source: https://getbootstrap.com/docs/5.3/components/buttons

Shows an example of creating a custom button variant (`.btn-bd-primary`) by reassigning Bootstrap's CSS variables. This SCSS code demonstrates how to define specific styles for color, background, borders, and hover/active states using a mix of CSS and Sass variables for unique button appearances.

```scss
.btn-bd-primary {
  --bs-btn-font-weight: 600;
  --bs-btn-color: var(--bs-white);
  --bs-btn-bg: var(--bd-violet-bg);
  --bs-btn-border-color: var(--bd-violet-bg);
  --bs-btn-hover-color: var(--bs-white);
  --bs-btn-hover-bg: #{shade-color($bd-violet, 10%)};
  --bs-btn-hover-border-color: #{shade-color($bd-violet, 10%)};
  --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
  --bs-btn-active-color: var(--bs-btn-hover-color);
  --bs-btn-active-bg: #{shade-color($bd-violet, 20%)};
  --bs-btn-active-border-color: #{shade-color($bd-violet, 20%)};
}
```

--------------------------------

### Responsive Block Buttons

Source: https://getbootstrap.com/docs/5.3/components/buttons

Creates responsive block buttons that stack vertically on smaller screens and become horizontally aligned on medium screens and up, using `.d-grid`, `.d-md-block`, and `gap-2` utilities.

```html
<div class="d-grid gap-2 d-md-block">
  <button class="btn btn-primary" type="button">Button</button>
  <button class="btn btn-primary" type="button">Button</button>
</div>
```

--------------------------------

### Bootstrap Button Tags and Roles

Source: https://getbootstrap.com/docs/5.3/components/buttons

Illustrates how Bootstrap button classes can be applied to various HTML elements like `<a>`, `<button>`, and `<input>`. It also highlights the importance of `role="button"` for accessibility when using `<a>` tags for button-like actions.

```html
<a class="btn btn-primary" href="#" role="button">Link</a>
<button class="btn btn-primary" type="submit">Button</button>
<input class="btn btn-primary" type="button" value="Input">
<input class="btn btn-primary" type="submit" value="Submit">
<input class="btn btn-primary" type="reset" value="Reset">
```

--------------------------------

### Create Stacked Block Buttons

Source: https://getbootstrap.com/docs/5.3/components/buttons

Generates vertically stacked, full-width buttons using the `.d-grid` and `gap-2` utility classes. This provides a responsive layout for button groups.

```html
<div class="d-grid gap-2">
  <button class="btn btn-primary" type="button">Button</button>
  <button class="btn btn-primary" type="button">Button</button>
</div>
```

--------------------------------

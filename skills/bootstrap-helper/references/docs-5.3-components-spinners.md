### Bootstrap Spinners in Buttons (HTML)

Source: https://getbootstrap.com/docs/5.3/components/spinners

Provides examples of integrating Bootstrap spinners within button elements to indicate an ongoing action. It shows variations with spinner-only text and combined spinner and button text.

```html
<button class="btn btn-primary" type="button" disabled>
  <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
  <span class="visually-hidden" role="status">Loading...</span>
</button>
<button class="btn btn-primary" type="button" disabled>
  <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
  <span role="status">Loading...</span>
</button>
```

```html
<button class="btn btn-primary" type="button" disabled>
  <span class="spinner-grow spinner-grow-sm" aria-hidden="true"></span>
  <span class="visually-hidden" role="status">Loading...</span>
</button>
<button class="btn btn-primary" type="button" disabled>
  <span class="spinner-grow spinner-grow-sm" aria-hidden="true"></span>
  <span role="status">Loading...</span>
</button>
```

--------------------------------

### Spinner with Text using Flexbox HTML

Source: https://getbootstrap.com/docs/5.3/components/spinners

This example shows how to align a Bootstrap spinner next to text using flexbox utilities (`.d-flex`, `.align-items-center`, `.ms-auto`). It creates a common loading indicator pattern where text precedes the spinner. Accessibility attributes are included.

```html
<div class="d-flex align-items-center">
  <strong role="status">Loading...</strong>
  <div class="spinner-border ms-auto" aria-hidden="true"></div>
</div>
```

--------------------------------

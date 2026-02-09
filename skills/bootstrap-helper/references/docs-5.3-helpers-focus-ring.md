### Basic Focus Ring Example (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/focus-ring

Demonstrates the basic application of the `.focus-ring` class to an anchor tag, replacing the default outline with a custom focus ring style. This is the simplest way to apply the focus ring effect.

```html
<a href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2">
  Custom focus ring
</a>
```

--------------------------------

### Themed Focus Ring Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/focus-ring

Demonstrates the use of `.focus-ring-*` utility classes to apply different theme colors to the focus ring. This provides a quick way to style focus rings based on Bootstrap's color palette.

```html
<p><a href="#" class="d-inline-flex focus-ring focus-ring-primary py-1 px-2 text-decoration-none border rounded-2">Primary focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-secondary py-1 px-2 text-decoration-none border rounded-2">Secondary focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-success py-1 px-2 text-decoration-none border rounded-2">Success focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-danger py-1 px-2 text-decoration-none border rounded-2">Danger focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-warning py-1 px-2 text-decoration-none border rounded-2">Warning focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-info py-1 px-2 text-decoration-none border rounded-2">Info focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-light py-1 px-2 text-decoration-none border rounded-2">Light focus</a></p>
<p><a href="#" class="d-inline-flex focus-ring focus-ring-dark py-1 px-2 text-decoration-none border rounded-2">Dark focus</a></p>
```

--------------------------------

### Customizing Focus Ring Offset and Blur (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/focus-ring

Illustrates how to adjust the focus ring's offset (X and Y) and blur using CSS variables. This provides more advanced control over the visual appearance of the focus ring.

```html
<a href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" style="--bs-focus-ring-x: 10px; --bs-focus-ring-y: 10px; --bs-focus-ring-blur: 4px">
  Blurry offset focus ring
</a>
```

--------------------------------

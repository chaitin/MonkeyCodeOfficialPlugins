### Icon Link with Bootstrap Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/helpers/icon-link

Applies Bootstrap's link utilities to an icon link for enhanced styling. This example uses `.link-success`, `.link-underline-success`, and `.link-underline-opacity-25` to modify the link's color and underline appearance, demonstrating utility-based customization.

```html
<a class="icon-link icon-link-hover link-success link-underline-success link-underline-opacity-25" href="#">
  Icon link
  <svg xmlns="http://www.w3.org/2000/svg" class="bi" viewBox="0 0 16 16" aria-hidden="true">
    <path d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
  </svg>
</a>
```

--------------------------------

### Customizing Icon Link Color on Hover (HTML/CSS)

Source: https://getbootstrap.com/docs/5.3/helpers/icon-link

Customizes the hover color of an icon link by overriding the `--bs-link-hover-color-rgb` CSS variable. This allows for specific color choices on hover, using an RGB value for precise control. The example sets a green hover color.

```html
<a class="icon-link icon-link-hover" style="--bs-link-hover-color-rgb: 25, 135, 84;" href="#">
  Icon link
  <svg xmlns="http://www.w3.org/2000/svg" class="bi" viewBox="0 0 16 16" aria-hidden="true">
    <path d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
  </svg>
</a>
```

--------------------------------

### Responsive box-decoration-break with breakpoint variant

Source: https://tailwindcss.com/docs/box-decoration-break

Combine box-decoration-break utilities with Tailwind breakpoint variants to apply different rendering behavior at specific screen sizes. Use the md: prefix to apply box-decoration-slice only at medium screen sizes and above.

```html
<div class="box-decoration-clone md:box-decoration-slice ...">
  <!-- Content -->
</div>
```

--------------------------------

### Apply box-decoration-clone utility in HTML

Source: https://tailwindcss.com/docs/box-decoration-break

Use the box-decoration-clone class to render element fragments as distinct blocks. This utility applies box-decoration-break: clone to the element, causing background, border, and padding properties to be rendered independently on each line.

```html
<span class="box-decoration-clone bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">
  Hello<br />
  World
</span>
```

--------------------------------

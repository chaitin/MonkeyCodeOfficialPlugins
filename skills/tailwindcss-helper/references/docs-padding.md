### Basic Padding Utility - Tailwind CSS

Source: https://tailwindcss.com/docs/padding

Apply uniform padding to all sides of an element using the p-<number> utility class. The padding value is calculated using the --spacing theme variable multiplied by the specified number.

```html
<div class="p-8 ...">p-8</div>
```

--------------------------------

### Responsive Padding Design - Tailwind CSS

Source: https://tailwindcss.com/docs/padding

Apply different padding values at different breakpoints using breakpoint prefixes like md:. This enables responsive design patterns that adapt padding based on screen size.

```html
<div class="py-4 md:py-8 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Logical Padding Properties - Tailwind CSS

Source: https://tailwindcss.com/docs/padding

Use ps-* (padding-inline-start) and pe-* (padding-inline-end) utilities for bidirectional text support. These logical properties automatically adjust based on text direction (LTR or RTL).

```html
<div>
  <div dir="ltr">
    <div class="ps-8 ...">ps-8</div>
    <div class="pe-8 ...">pe-8</div>
  </div>
  <div dir="rtl">
    <div class="ps-8 ...">ps-8</div>
    <div class="pe-8 ...">pe-8</div>
  </div>
</div>
```

--------------------------------

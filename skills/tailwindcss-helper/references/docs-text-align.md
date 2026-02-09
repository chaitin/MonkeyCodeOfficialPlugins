### Logical text alignment with text-start and text-end utilities

Source: https://tailwindcss.com/docs/text-align

Apply logical text alignment using text-start and text-end utilities, which automatically map to left or right based on text direction. Useful for multilingual content and RTL (right-to-left) languages like Arabic.

```html
<div dir="rtl" lang="ar">
  <p class="text-end">فبدأت بالسير نحو الماء...</p>
</div>
```

--------------------------------

### Responsive text alignment with breakpoint variants

Source: https://tailwindcss.com/docs/text-align

Apply text-align utilities responsively using breakpoint prefixes like md:. This allows different text alignment at different screen sizes, enabling adaptive layouts for various devices.

```html
<p class="text-left md:text-center ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Applying responsive list-style-position utilities in HTML

Source: https://tailwindcss.com/docs/list-style-position

This example illustrates how to apply `list-style-position` utilities responsively using breakpoint variants. By prefixing a utility with `md:`, the `list-inside` style will only be applied at medium screen sizes and above, allowing for adaptive list layouts.

```html
<ul class="list-outside md:list-inside ...">  <!-- ... --></ul>
```

--------------------------------

### Applying list-style-position utilities in HTML

Source: https://tailwindcss.com/docs/list-style-position

This example demonstrates how to use the `list-inside` and `list-outside` classes on `<ul>` elements to control the positioning of list markers relative to the list item's text. It shows how these classes affect the indentation and alignment of bullet points or numbers.

```html
<ul class="list-inside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul><ul class="list-outside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul>
```

--------------------------------

### Implementing responsive text wrapping with Tailwind CSS

Source: https://tailwindcss.com/docs/text-wrap

This example illustrates how to apply text wrapping utilities responsively using breakpoint variants. By prefixing a utility like `text-pretty` with `md:`, the `text-balance` style will only be applied on medium screen sizes and above, allowing for adaptive text layout across different devices.

```html
<h1 class="text-pretty md:text-balance ...">  <!-- ... --></h1>
```

--------------------------------

### Balancing text wrapping with Tailwind CSS `text-balance`

Source: https://tailwindcss.com/docs/text-wrap

This example showcases the `text-balance` utility, which distributes text evenly across each line for improved readability. It is particularly effective for headings and short blocks of text, as browsers typically limit balancing to content around 6 lines or less for performance reasons.

```html
<article>  <h3 class="text-balance">Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

--------------------------------

### Allowing text to wrap with Tailwind CSS `text-wrap`

Source: https://tailwindcss.com/docs/text-wrap

This example demonstrates the use of the `text-wrap` utility class to allow text to wrap onto multiple lines. It ensures that overflowing text breaks at logical points, fitting within its container. This is the default browser behavior but can be explicitly set.

```html
<article class="text-wrap">  <h3>Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

--------------------------------

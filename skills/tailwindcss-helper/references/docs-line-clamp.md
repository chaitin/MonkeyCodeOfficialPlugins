### Responsive line-clamp with breakpoint variants

Source: https://tailwindcss.com/docs/line-clamp

Demonstrates responsive design using line-clamp utilities with breakpoint prefixes. This example applies line-clamp-3 on mobile screens and line-clamp-4 on medium screens and above using the md: variant.

```html
<div class="line-clamp-3 md:line-clamp-4 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Undo line clamping with line-clamp-none

Source: https://tailwindcss.com/docs/line-clamp

Shows how to use the line-clamp-none utility to remove previously applied line clamping. This example demonstrates responsive design by applying line-clamp-3 on mobile and line-clamp-none on large screens using the lg: breakpoint variant.

```html
<p class="line-clamp-3 lg:line-clamp-none">
  <!-- ... -->
</p>
```

--------------------------------

### Basic line-clamp HTML example

Source: https://tailwindcss.com/docs/line-clamp

Demonstrates using the line-clamp-3 utility class to truncate a paragraph to 3 lines. The utility applies -webkit-line-clamp: 3 along with necessary display and overflow properties to achieve text truncation in a typical article layout.

```html
<article>
  <time>Mar 10, 2020</time>
  <h2>Boost your conversion rate</h2>
  <p class="line-clamp-3">
    Nulla dolor velit adipisicing duis excepteur esse in duis nostrud occaecat mollit incididunt deserunt sunt. Ut ut
    sunt laborum ex occaecat eu tempor labore enim adipisicing minim ad. Est in quis eu dolore occaecat excepteur fugiat
    dolore nisi aliqua fugiat enim ut cillum. Labore enim duis nostrud eu. Est ut eiusmod consequat irure quis deserunt
    ex. Enim laboris dolor magna pariatur. Dolor et ad sint voluptate sunt elit mollit officia ad enim sit consectetur
    enim.
  </p>
  <div>
    <img src="/img/lindsay.jpg" />
    Lindsay Walton
  </div>
</article>
```

--------------------------------

### Custom line-clamp value with bracket notation

Source: https://tailwindcss.com/docs/line-clamp

Demonstrates using the line-clamp-[<value>] syntax to set a custom number of lines based on arbitrary values. This allows for dynamic line clamping using calc() expressions or other custom CSS values not covered by the default utility classes.

```html
<p class="line-clamp-[calc(var(--characters)/100)] ...">
  Lorem ipsum dolor sit amet...
</p>
```

--------------------------------

### Custom line-clamp with CSS custom property

Source: https://tailwindcss.com/docs/line-clamp

Shows the line-clamp-(<custom-property>) syntax as a shorthand for line-clamp-[var(<custom-property>)]. This approach automatically wraps the custom property in the var() function, allowing for cleaner syntax when using CSS variables to control line clamping.

```html
<p class="line-clamp-(--my-line-count) ...">
  Lorem ipsum dolor sit amet...
</p>
```

--------------------------------

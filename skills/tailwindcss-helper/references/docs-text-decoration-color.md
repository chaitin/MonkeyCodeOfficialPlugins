### Implement Responsive Text Decoration Colors with Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-color

This snippet demonstrates how to apply different text decoration colors based on screen size using responsive variants. By prefixing a utility with a breakpoint (e.g., `md:decoration-blue-400`), the color will only be applied at that specific screen size and above, allowing for adaptive designs.

```html
<p class="underline decoration-sky-600 md:decoration-blue-400 ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply Basic Text Decoration Colors with Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-color

This example demonstrates how to use standard Tailwind CSS color utilities like `decoration-sky-500` and `decoration-pink-500` to set the text decoration color for `<a>` elements. These classes apply predefined colors from the Tailwind palette to the `text-decoration-color` CSS property.

```html
<p>  I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings  at <a class="underline decoration-sky-500">My Company, Inc</a>. Outside  of work, I like to <a class="underline decoration-pink-500">watch pod-racing</a>  and have <a class="underline decoration-indigo-500">light-saber</a> fights.</p>
```

--------------------------------

### Apply Text Decoration Color on Hover State with Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-color

This example illustrates how to change the text decoration color specifically on hover. By prefixing a color utility with `hover:` (e.g., `hover:decoration-pink-500`), the specified color will only be applied to the `text-decoration-color` property when the element is in its hover state.

```html
<p>The <a href="..." class="underline hover:decoration-pink-500 ...">quick brown fox</a> jumps over the lazy dog.</p>
```

--------------------------------

### Utilize Custom Theme Color for Text Decoration in Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-color

This example demonstrates how to apply a custom color, previously defined in your Tailwind CSS theme, to an element's text decoration. By using the `decoration-` prefix followed by your custom color's name (e.g., `decoration-regal-blue`), you can easily integrate custom branding into your design.

```html
<p class="decoration-regal-blue">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Set Custom Hex Text Decoration Color in Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-color

This example shows how to apply a completely custom text decoration color using an arbitrary hex value. The `decoration-[<value>]` syntax allows you to specify any valid CSS color value directly, such as `decoration-[#50d71e]`, which will be applied to the `text-decoration-color` property.

```html
<p class="decoration-[#50d71e] ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

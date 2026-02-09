### Apply Numeric Text Decoration Thickness with Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-thickness

This example demonstrates how to use Tailwind CSS `decoration-<number>` utilities to set a fixed pixel thickness for text decorations. It shows `decoration-1`, `decoration-2`, and `decoration-4` classes applied to `underline` elements.

```html
<p class="underline decoration-1">The quick brown fox...</p><p class="underline decoration-2">The quick brown fox...</p><p class="underline decoration-4">The quick brown fox...</p>
```

--------------------------------

### Apply CSS Variable for Text Decoration Thickness in Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-thickness

This example shows how to use a CSS variable to define text decoration thickness with Tailwind CSS. It utilizes the `decoration-(length:<custom-property>)` syntax, which automatically wraps the custom property in `var()`.

```html
<p class="decoration-(length:--my-decoration-thickness) ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply Responsive Text Decoration Thickness with Tailwind CSS

Source: https://tailwindcss.com/docs/text-decoration-thickness

This snippet demonstrates how to make text decoration thickness responsive using Tailwind CSS breakpoint variants. The `md:decoration-4` class applies a thickness of 4px only on medium screens and larger.

```html
<p class="underline md:decoration-4 ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

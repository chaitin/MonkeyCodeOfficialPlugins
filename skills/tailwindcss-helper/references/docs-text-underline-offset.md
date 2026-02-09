### Apply Responsive Underline Offset in Tailwind CSS

Source: https://tailwindcss.com/docs/text-underline-offset

This example illustrates how to apply a `text-underline-offset` utility conditionally at different screen sizes using responsive prefixes. By adding a breakpoint variant like `md:`, the utility `md:underline-offset-4` will only apply the specified offset on medium screens and above.

```html
<p class="underline md:underline-offset-4 ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply Basic Underline Offset in Tailwind CSS

Source: https://tailwindcss.com/docs/text-underline-offset

This example demonstrates how to use predefined `underline-offset-<number>` utilities like `underline-offset-1`, `underline-offset-2`, `underline-offset-4`, and `underline-offset-8` to control the offset of a text underline in HTML. These classes apply a fixed pixel offset to the underline.

```html
<p class="underline underline-offset-1">The quick brown fox...</p><p class="underline underline-offset-2">The quick brown fox...</p><p class="underline underline-offset-4">The quick brown fox...</p><p class="underline underline-offset-8">The quick brown fox...</p>
```

--------------------------------

### Apply Custom Underline Offset Value in Tailwind CSS

Source: https://tailwindcss.com/docs/text-underline-offset

This example shows how to set a custom text underline offset using arbitrary values with the `underline-offset-[<value>]` syntax. This allows for precise control over the offset by specifying any valid CSS length unit, such as `underline-offset-[3px]`.

```html
<p class="underline-offset-[3px] ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply Underline Offset with CSS Variable in Tailwind CSS

Source: https://tailwindcss.com/docs/text-underline-offset

This example demonstrates using a CSS custom property (variable) to define the underline offset with the `underline-offset-(<custom-property>)` syntax, like `underline-offset-(--my-underline-offset)`. This shorthand automatically wraps the custom property in `var()` for dynamic styling.

```html
<p class="underline-offset-(--my-underline-offset) ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

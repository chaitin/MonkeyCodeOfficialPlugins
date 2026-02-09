### Apply Responsive Caret Colors with Tailwind CSS

Source: https://tailwindcss.com/docs/caret-color

This example demonstrates how to use responsive prefixes, such as `md:`, with caret color utilities. It allows the caret color to change based on screen sizes, applying `caret-rose-500` by default and `caret-lime-600` on medium screens and above.

```html
<textarea class="caret-rose-500 md:caret-lime-600 ..."></textarea>
```

--------------------------------

### Set Custom Caret Color with Hex Value in Tailwind CSS

Source: https://tailwindcss.com/docs/caret-color

This example illustrates the use of Tailwind's arbitrary value syntax `caret-[<value>]` to set a custom caret color. A hex code, like `#50d71e`, is directly embedded in the class name to apply a specific color not available in the default palette.

```html
<textarea class="caret-[#50d71e] ..."></textarea>
```

--------------------------------

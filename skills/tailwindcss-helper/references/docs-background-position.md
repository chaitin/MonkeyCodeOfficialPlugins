### Apply Tailwind CSS background-position utilities for basic positioning

Source: https://tailwindcss.com/docs/background-position

This example demonstrates how to use predefined Tailwind CSS classes like `bg-center`, `bg-right`, and `bg-top-left` to control the position of an element's background image. These utilities map directly to common `background-position` values.

```html
<div class="bg-[url(/img/mountains.jpg)] bg-top-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-top"></div><div class="bg-[url(/img/mountains.jpg)] bg-top-right"></div><div class="bg-[url(/img/mountains.jpg)] bg-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-center"></div><div class="bg-[url(/img/mountains.jpg)] bg-right"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom-right"></div>
```

--------------------------------

### Apply background-position using CSS variables in Tailwind CSS

Source: https://tailwindcss.com/docs/background-position

This example shows how to use the `bg-position-(<custom-property>)` syntax in Tailwind CSS to set the `background-position` based on a CSS variable. This is a shorthand for `bg-position-[var(<custom-property>)]`, providing dynamic positioning.

```html
<div class="bg-position-(--my-bg-position) ...">  <!-- ... --></div>
```

--------------------------------

### Apply responsive background-position utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/background-position

This snippet demonstrates how to make `background-position` responsive using Tailwind CSS breakpoint variants. By prefixing a utility like `bg-top` with `md:`, the positioning will only apply at medium screen sizes and above, adapting the layout for different devices.

```html
<div class="bg-center md:bg-top ...">  <!-- ... --></div>
```

--------------------------------

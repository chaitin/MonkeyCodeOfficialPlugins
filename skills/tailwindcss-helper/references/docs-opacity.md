### Apply Tailwind CSS Opacity Responsively with Breakpoint Variants

Source: https://tailwindcss.com/docs/opacity

This example shows how to use breakpoint variants, such as `md:`, to apply opacity utilities only at specific screen sizes and above, enabling responsive design for element transparency.

```html
<button class="opacity-50 md:opacity-100 ...">  <!-- ... --></button>
```

--------------------------------

### Set Tailwind CSS Opacity with Custom CSS Variables

Source: https://tailwindcss.com/docs/opacity

This example demonstrates using the `opacity-(<custom-property>)` syntax to apply opacity based on a CSS custom property, like `--my-opacity`. This is a shorthand for `opacity-[var(<custom-property>)]`.

```html
<button class="opacity-(--my-opacity) ...">  <!-- ... --></button>
```

--------------------------------

### Apply Tailwind CSS Opacity Conditionally with Variants

Source: https://tailwindcss.com/docs/opacity

This example shows how to use a variant, such as `disabled:*`, to apply an opacity utility only when a specific condition is met. Here, an input field has reduced opacity when disabled.

```html
<input class="opacity-100 disabled:opacity-75 ..." type="text" />
```

--------------------------------

### Set Tailwind CSS Opacity with Custom Numeric Values

Source: https://tailwindcss.com/docs/opacity

This example illustrates how to use the `opacity-[<value>]` syntax to apply a completely custom numeric opacity value to an HTML element, such as `opacity-[.67]`.

```html
<button class="opacity-[.67] ...">  <!-- ... --></button>
```

--------------------------------

### Apply Tailwind CSS Opacity Utilities for Basic Elements

Source: https://tailwindcss.com/docs/opacity

This example demonstrates how to use `opacity-<number>` utilities like `opacity-100`, `opacity-75`, `opacity-50`, and `opacity-25` to set the transparency of HTML button elements in Tailwind CSS.

```html
<button class="bg-indigo-500 opacity-100 ..."></button><button class="bg-indigo-500 opacity-75 ..."></button><button class="bg-indigo-500 opacity-50 ..."></button><button class="bg-indigo-500 opacity-25 ..."></button>
```

--------------------------------

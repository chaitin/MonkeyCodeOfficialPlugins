### Apply Brightness Filters with Tailwind CSS and CSS Variables

Source: https://tailwindcss.com/docs/filter-brightness

This example illustrates applying brightness filters using CSS variables in Tailwind CSS with the `brightness-(<custom-property>)` syntax. This shorthand automatically wraps the custom property in `var()`, enabling dynamic brightness control via CSS variables for more flexible styling.

```html
<img class="brightness-(--my-brightness) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Basic Brightness Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-brightness

This example demonstrates how to apply standard brightness filters to an image using Tailwind CSS utility classes like `brightness-50`, `brightness-100`, `brightness-125`, and `brightness-200`. These classes control the element's brightness level, where `brightness-100` represents normal brightness.

```html
<img class="brightness-50 ..." src="/img/mountains.jpg" /><img class="brightness-100 ..." src="/img/mountains.jpg" /><img class="brightness-125 ..." src="/img/mountains.jpg" /><img class="brightness-200 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Responsive Brightness Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-brightness

This code demonstrates how to apply brightness filters conditionally based on screen size using Tailwind CSS responsive variants. By prefixing utilities like `brightness-110` with `md:brightness-150`, the brightness changes only at medium screen sizes and above, adapting to different viewports.

```html
<img class="brightness-110 md:brightness-150 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Custom Brightness Filters with Tailwind CSS Arbitrary Values

Source: https://tailwindcss.com/docs/filter-brightness

This snippet shows how to use arbitrary values for brightness filters in Tailwind CSS with the `brightness-[<value>]` syntax. It allows setting a precise, custom brightness level, such as `brightness-[1.75]` for 175% brightness, providing fine-grained control.

```html
<img class="brightness-[1.75] ..." src="/img/mountains.jpg" />
```

--------------------------------

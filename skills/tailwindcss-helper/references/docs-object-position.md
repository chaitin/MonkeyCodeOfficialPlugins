### Apply object-position utilities in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/object-position

This example demonstrates how to use various Tailwind CSS `object-position` utility classes like `object-top-left`, `object-center`, and `object-bottom-right` to control the positioning of a replaced element's content within its container. These classes directly map to standard CSS `object-position` values.

```html
<img class="size-24 object-top-left ..." src="/img/mountains.jpg" /><img class="size-24 object-top ..." src="/img/mountains.jpg" /><img class="size-24 object-top-right ..." src="/img/mountains.jpg" /><img class="size-24 object-left ..." src="/img/mountains.jpg" /><img class="size-24 object-center ..." src="/img/mountains.jpg" /><img class="size-24 object-right ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-left ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-right ..." src="/img/mountains.jpg" />
```

--------------------------------

### Set object-position using CSS variable in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/object-position

This example shows how to apply a custom `object-position` using a CSS variable with Tailwind CSS's `object-(<custom-property>)` syntax. This shorthand automatically wraps the custom property in `var()`, enabling dynamic positioning controlled by CSS variables.

```html
<img class="object-(--my-object) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply responsive object-position in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/object-position

This snippet demonstrates how to make `object-position` utilities responsive using Tailwind CSS breakpoint variants. By prefixing a utility with `md:`, the `object-top` class will only apply at medium screen sizes and above, overriding the default `object-center` for smaller screens.

```html
<img class="object-center md:object-top ..." src="/img/mountains.jpg" />
```

--------------------------------

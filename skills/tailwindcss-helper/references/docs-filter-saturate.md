### Apply Basic Saturation Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-saturate

This example demonstrates how to use Tailwind CSS's built-in `saturate-<number>` utility classes to apply different levels of saturation to an image. These classes provide predefined saturation percentages for quick application.

```html
<img class="saturate-50 ..." src="/img/mountains.jpg" /><img class="saturate-100 ..." src="/img/mountains.jpg" /><img class="saturate-150 ..." src="/img/mountains.jpg" /><img class="saturate-200 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Use CSS Variables for Saturation with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-saturate

This example shows how to dynamically apply saturation using a CSS custom property with Tailwind CSS's `saturate-(<custom-property>)` syntax. This shorthand automatically wraps the custom property in `var()` for flexible styling.

```html
<img class="saturate-(--my-saturation) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Responsive Saturation Filters with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-saturate

This snippet demonstrates how to use Tailwind CSS's responsive prefixes, such as `md:`, to apply different saturation levels based on screen size. This allows for adaptive designs where filter effects change at specific breakpoints.

```html
<img class="saturate-50 md:saturate-150 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Custom Saturation Values with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-saturate

This snippet illustrates how to use Tailwind CSS's arbitrary value syntax, `saturate-[<value>]`, to apply a completely custom saturation level to an element. This allows for fine-grained control beyond the predefined utility classes.

```html
<img class="saturate-[.25] ..." src="/img/mountains.jpg" />
```

--------------------------------

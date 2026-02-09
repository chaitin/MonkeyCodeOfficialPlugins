### Apply responsive sepia filters to images with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/filter-sepia

Demonstrates how to apply sepia filters conditionally based on screen size using responsive prefixes like `md:`. This example applies a full sepia filter by default and removes it (`md:sepia-0`) on medium screens and above, allowing for adaptive designs.

```html
<img class="sepia md:sepia-0 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply basic sepia filters to images with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-sepia

Demonstrates applying different levels of sepia filters (none, 50%, 100%) to image elements using Tailwind CSS utility classes like `sepia-0`, `sepia-50`, and `sepia`. These classes directly map to `filter: sepia(0%)`, `filter: sepia(50%)`, and `filter: sepia(100%)` respectively.

```html
<img class="sepia-0" src="/img/mountains.jpg" /><img class="sepia-50" src="/img/mountains.jpg" /><img class="sepia" src="/img/mountains.jpg" />
```

--------------------------------

### Apply custom sepia filter values using Tailwind CSS arbitrary values

Source: https://tailwindcss.com/docs/filter-sepia

Illustrates using Tailwind CSS's arbitrary value syntax `sepia-[<value>]` to apply a precise, custom sepia filter amount. For instance, `sepia-[.25]` sets the sepia filter to 25%.

```html
<img class="sepia-[.25] ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply sepia filter using CSS custom properties in Tailwind CSS

Source: https://tailwindcss.com/docs/filter-sepia

Shows how to apply a sepia filter using a CSS custom property with the `sepia-(<custom-property>)` syntax. This is a convenient shorthand for `sepia-[var(<custom-property>)]`, automatically wrapping the custom property in `var()`.

```html
<img class="sepia-(--my-sepia) ..." src="/img/mountains.jpg" />
```

--------------------------------

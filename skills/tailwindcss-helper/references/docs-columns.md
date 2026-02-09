### Apply responsive column layouts with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/columns

This example illustrates how to use responsive breakpoint variants like `sm:` with column utilities in Tailwind CSS. This allows column layouts to adapt to different screen sizes, providing an optimal user experience across devices. Input is an HTML `div` with `columns-<number>` and `gap-<width>` classes prefixed with breakpoint variants, resulting in a responsive multi-column layout.

```html
<div class="columns-2 gap-4 sm:columns-3 sm:gap-8 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

--------------------------------

### Specify column gap with Tailwind CSS

Source: https://tailwindcss.com/docs/columns

This example illustrates how to use `gap-<width>` utilities in conjunction with column utilities to specify the spacing between columns in Tailwind CSS. This allows for precise control over the visual separation of content. Input is an HTML `div` with both `columns-<number>` and `gap-<width>` classes, producing a multi-column layout with defined spacing.

```html
<div class="columns-3 gap-8 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

--------------------------------

### Use custom Tailwind CSS column utility in HTML

Source: https://tailwindcss.com/docs/columns

This example shows how to apply a custom column utility, previously defined in the Tailwind CSS theme configuration, to an HTML element. This demonstrates the integration of custom theme settings into the markup. Input is an HTML `div` with the custom `columns-4xs` class, applying the custom column width.

```html
<div class="columns-4xs">  <!-- ... --></div>
```

--------------------------------

### Apply custom column width using arbitrary values in Tailwind CSS

Source: https://tailwindcss.com/docs/columns

This example demonstrates how to use the `columns-[<value>]` arbitrary value syntax in Tailwind CSS to set a completely custom column width. This provides maximum flexibility for unique layout requirements. Input is an HTML `div` with a `columns-[<value>]` class, where `<value>` can be any valid CSS width.

```html
<div class="columns-[30vw] ...">  <!-- ... --></div>
```

--------------------------------

### Customize Tailwind CSS column utilities in theme configuration

Source: https://tailwindcss.com/docs/columns

This example demonstrates how to customize the fixed-width column utilities in Tailwind CSS by defining custom CSS variables within the `@theme` block. This allows developers to extend or modify the default column sizes to match project-specific design systems. The output is a new custom utility like `columns-4xs` available for use in HTML.

```css
@theme {  --container-4xs: 14rem; }
```

--------------------------------

### Set ideal column width with Tailwind CSS

Source: https://tailwindcss.com/docs/columns

This example shows how to use `columns-<size>` utilities like `columns-xs` or `columns-3xs` in Tailwind CSS to define an ideal column width for content. The number of columns dynamically adjusts to prevent them from becoming too narrow. Input is an HTML `div` with a `columns-<size>` class, resulting in a responsive multi-column layout.

```html
<div class="columns-3xs ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

--------------------------------

### Apply fixed number of columns with Tailwind CSS

Source: https://tailwindcss.com/docs/columns

This example demonstrates how to use `columns-<number>` utilities in Tailwind CSS to set a fixed number of columns for content within an HTML element. The column width automatically adjusts to fit the specified number of columns. Input is an HTML `div` with a `columns-<number>` class, and the output is a multi-column layout.

```html
<div class="columns-3 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

--------------------------------

### Apply custom column width using CSS variables in Tailwind CSS

Source: https://tailwindcss.com/docs/columns

This example shows how to use the `columns-(<custom-property>)` syntax in Tailwind CSS to apply a custom column width defined by a CSS variable. This is a shorthand for `columns-[var(<custom-property>)]`, promoting reusability and maintainability. Input is an HTML `div` with a `columns-(--my-columns)` class, referencing a CSS variable.

```html
<div class="columns-(--my-columns) ...">  <!-- ... --></div>
```

--------------------------------

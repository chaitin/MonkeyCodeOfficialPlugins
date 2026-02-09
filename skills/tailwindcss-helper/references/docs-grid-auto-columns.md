### Apply responsive grid-auto-columns utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/grid-auto-columns

This example illustrates how to apply `grid-auto-columns` utilities responsively using breakpoint variants like `md:`, allowing different column sizing based on screen size.

```html
<div class="grid grid-flow-col auto-cols-max md:auto-cols-min ...">  <!-- ... --></div>
```

--------------------------------

### Apply basic grid-auto-columns utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/grid-auto-columns

This example demonstrates how to use Tailwind CSS utilities like `auto-cols-max` to control the size of implicitly-created grid columns within a `grid` and `grid-flow-col` layout.

```html
<div class="grid auto-cols-max grid-flow-col">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Set custom grid-auto-columns value in Tailwind CSS

Source: https://tailwindcss.com/docs/grid-auto-columns

This example shows how to use the arbitrary value syntax `auto-cols-[<value>]` to set a custom size for implicitly-created grid columns, such as `minmax(0,2fr)`.

```html
<div class="auto-cols-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

--------------------------------

### Apply grid-auto-columns with CSS variables in Tailwind CSS

Source: https://tailwindcss.com/docs/grid-auto-columns

This example demonstrates using the `auto-cols-(<custom-property>)` syntax to apply a CSS variable as the value for `grid-auto-columns`, which is a shorthand for `auto-cols-[var(<custom-property>)]`.

```html
<div class="auto-cols-(--my-auto-cols) ...">  <!-- ... --></div>
```

--------------------------------

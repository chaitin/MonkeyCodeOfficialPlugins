### Apply flex-basis using percentage fractions in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Shows how to set the initial size of flex items using Tailwind CSS `basis-<fraction>` utilities, which represent percentage-based widths. This example uses `basis-1/3` and `basis-2/3`.

```html
<div class="flex flex-row">  <div class="basis-1/3">01</div>  <div class="basis-2/3">02</div></div>
```

--------------------------------

### Apply flex-basis using spacing scale in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Demonstrates how to set the initial size of flex items using Tailwind CSS `basis-<number>` utilities, which are based on the predefined spacing scale. This example uses `basis-64` and `basis-128` to illustrate different widths.

```html
<div class="flex flex-row">  <div class="basis-64">01</div>  <div class="basis-64">02</div>  <div class="basis-128">03</div></div>
```

--------------------------------

### Apply flex-basis using container scale in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Illustrates setting the initial size of flex items using Tailwind CSS `basis-<size>` utilities, which are derived from the container scale. This example showcases `basis-3xs`, `basis-2xs`, `basis-xs`, and `basis-sm`.

```html
<div class="flex flex-row">  <div class="basis-3xs">01</div>  <div class="basis-2xs">02</div>  <div class="basis-xs">03</div>  <div class="basis-sm">04</div></div>
```

--------------------------------

### Apply responsive flex-basis utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Shows how to apply responsive `flex-basis` utilities using breakpoint variants like `md:`. This allows the initial size of flex items to change based on screen size, adapting for different viewports.

```html
<div class="flex flex-row">  <div class="basis-1/4 md:basis-1/3">01</div>  <div class="basis-1/4 md:basis-1/3">02</div>  <div class="basis-1/2 md:basis-1/3">03</div></div>
```

--------------------------------

### Apply flex-basis with custom arbitrary values in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Demonstrates how to set a custom `flex-basis` value using Tailwind CSS's arbitrary value syntax `basis-[<value>]`. This allows for precise control over the flex item's initial size with any valid CSS value.

```html
<div class="basis-[30vw] ...">  <!-- ... --></div>
```

--------------------------------

### Use custom container basis utility in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Shows how to apply a custom `basis-4xs` utility in HTML after it has been defined in the Tailwind CSS theme configuration. This demonstrates the usage of a newly added container scale value.

```html
<div class="basis-4xs">  <!-- ... --></div>
```

--------------------------------

### Apply flex-basis with custom CSS variables in Tailwind CSS

Source: https://tailwindcss.com/docs/flex-basis

Illustrates setting `flex-basis` using a custom CSS variable with the `basis-(<custom-property>)` syntax. This is a shorthand for `basis-[var(<custom-property>)]`, providing flexibility for dynamic sizing.

```html
<div class="basis-(--my-basis) ...">  <!-- ... --></div>
```

--------------------------------

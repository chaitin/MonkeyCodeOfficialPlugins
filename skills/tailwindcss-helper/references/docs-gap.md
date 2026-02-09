### Apply responsive gap in Tailwind CSS

Source: https://tailwindcss.com/docs/gap

Explains how to use responsive prefixes like `md:` with `gap` utilities to apply different gap values based on screen sizes, for example, `md:gap-6`.

```html
<div class="grid gap-4 md:gap-6 ...">  <!-- ... --></div>
```

--------------------------------

### Apply custom gap value in Tailwind CSS

Source: https://tailwindcss.com/docs/gap

Shows how to use arbitrary value syntax like `gap-[<value>]` to set a completely custom gap size, for example, `gap-[10vw]`.

```html
<div class="gap-[10vw] ...">  <!-- ... --></div>
```

--------------------------------

### Apply uniform gap in Tailwind CSS Grid

Source: https://tailwindcss.com/docs/gap

Demonstrates how to use `gap-<number>` utilities like `gap-4` to set a uniform gap between both rows and columns in a Tailwind CSS grid layout.

```html
<div class="grid grid-cols-2 gap-4">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

--------------------------------

### Apply custom gap using CSS variable in Tailwind CSS

Source: https://tailwindcss.com/docs/gap

Demonstrates the `gap-(<custom-property>)` syntax to apply a gap based on a CSS variable, which is a shorthand for `gap-[var(<custom-property>)]`.

```html
<div class="gap-(--my-gap) ...">  <!-- ... --></div>
```

--------------------------------

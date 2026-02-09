### Apply justify-items-end and justify-items-end-safe to grid items in HTML

Source: https://tailwindcss.com/docs/justify-items

These snippets illustrate the use of `justify-items-end` and `justify-items-end-safe` utility classes to align grid items to the end of their inline axis. The `safe` variant provides a fallback to the start of the container when space is insufficient, preventing content overflow. Both examples use a `grid grid-flow-col` container.

```html
<div class="grid grid-flow-col justify-items-end ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

```html
<div class="grid grid-flow-col justify-items-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Apply justify-items-center and justify-items-center-safe to grid items in HTML

Source: https://tailwindcss.com/docs/justify-items

These snippets show how to use `justify-items-center` and `justify-items-center-safe` utility classes to center grid items along their inline axis. Similar to the end variants, the `safe` variant ensures items align to the start if centering would cause overflow. Both examples use a `grid grid-flow-col` container.

```html
<div class="grid grid-flow-col justify-items-center ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

```html
<div class="grid grid-flow-col justify-items-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Apply responsive justify-items utilities in HTML

Source: https://tailwindcss.com/docs/justify-items

This snippet illustrates how to apply `justify-items` utilities conditionally based on screen size using responsive prefixes like `md:`. The grid items will start aligned by default and center align on medium screens and above, demonstrating Tailwind's responsive design capabilities.

```html
<div class="grid justify-items-start md:justify-items-center ...">  <!-- ... --></div>
```

--------------------------------

### Apply justify-items-start to grid items in HTML

Source: https://tailwindcss.com/docs/justify-items

This snippet demonstrates how to use the `justify-items-start` utility class in Tailwind CSS to align grid items to the start of their inline axis. It applies the class to a `div` element acting as a grid container, with child `div` elements as grid items.

```html
<div class="grid justify-items-start ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

--------------------------------

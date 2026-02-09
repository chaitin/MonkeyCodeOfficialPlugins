### Align items to start of main axis with Tailwind CSS `justify-start`

Source: https://tailwindcss.com/docs/justify-content

This example demonstrates how to use the `justify-start` utility class in Tailwind CSS to align flex items to the beginning of the container's main axis. It ensures content is pushed to the start, useful for left-aligned layouts in LTR contexts.

```html
<div class="flex justify-start ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Distribute items with space between using Tailwind CSS `justify-between`

Source: https://tailwindcss.com/docs/justify-content

This example demonstrates the `justify-between` utility, which distributes flex items along the main axis with equal space between them. The first item is at the start, and the last item is at the end of the container.

```html
<div class="flex justify-between ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Apply responsive justify-content with Tailwind CSS breakpoint variants

Source: https://tailwindcss.com/docs/justify-content

This example illustrates how to apply `justify-content` utilities responsively using Tailwind CSS breakpoint variants. The `md:justify-between` class ensures that items are justified to the start by default, but switch to space-between alignment on medium screens and above.

```html
<div class="flex justify-start md:justify-between ...">  <!-- ... --></div>
```

--------------------------------

### Align items to end of main axis with Tailwind CSS `justify-end` and `justify-end-safe`

Source: https://tailwindcss.com/docs/justify-content

These examples show how to use `justify-end` and `justify-end-safe` to align flex items to the end of the container's main axis. Similar to `justify-center-safe`, `justify-end-safe` ensures items align to the start if space is limited, preventing overflow.

```html
<div class="flex justify-end ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

```html
<div class="flex justify-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

--------------------------------

### Distribute items with space around using Tailwind CSS `justify-around`

Source: https://tailwindcss.com/docs/justify-content

This example uses the `justify-around` utility to distribute flex items with equal space around each item. This means there's half the space at the ends compared to the space between items.

```html
<div class="flex justify-around ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Stretch items to fill space with Tailwind CSS `justify-stretch`

Source: https://tailwindcss.com/docs/justify-content

This example demonstrates the `justify-stretch` utility, which allows auto-sized content items to expand and fill the available space along the container's main axis. It's particularly useful for grid layouts where items need to stretch.

```html
<div class="grid grid-cols-[4rem_auto_4rem] justify-stretch ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Distribute items with space evenly using Tailwind CSS `justify-evenly`

Source: https://tailwindcss.com/docs/justify-content

This example showcases the `justify-evenly` utility, which distributes flex items such that there is equal space around each item, including the space at the ends of the container. This results in visually balanced spacing across all items.

```html
<div class="flex justify-evenly ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Reset justify-content to normal with Tailwind CSS `justify-normal`

Source: https://tailwindcss.com/docs/justify-content

This example uses the `justify-normal` utility to reset the `justify-content` property to its default behavior. It packs content items in their default position, effectively removing any explicit `justify-content` alignment.

```html
<div class="flex justify-normal ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

--------------------------------

### Center items along main axis with Tailwind CSS `justify-center` and `justify-center-safe`

Source: https://tailwindcss.com/docs/justify-content

These examples illustrate the use of `justify-center` and `justify-center-safe` utilities to center flex items along the main axis. `justify-center-safe` provides a fallback to `flex-start` when space is insufficient, preventing content overflow issues.

```html
<div class="flex justify-center ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

```html
<div class="flex justify-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

--------------------------------

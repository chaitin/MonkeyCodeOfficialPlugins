### Apply responsive align-items utilities in Tailwind CSS HTML

Source: https://tailwindcss.com/docs/align-items

This example demonstrates how to apply `align-items` utilities responsively using Tailwind CSS breakpoint variants. By prefixing utilities like `md:items-center`, the alignment changes only at medium screen sizes and above, allowing for adaptive layouts.

```html
<div class="flex items-stretch md:items-center ...">  <!-- ... --></div>
```

--------------------------------

### Align items to the cross-start with items-start in HTML

Source: https://tailwindcss.com/docs/align-items

This snippet illustrates the `items-start` utility, which aligns flex items to the beginning of the container's cross axis. This is useful for positioning content at the top in a column layout or left in a row layout.

```html
<div class="flex items-start ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

--------------------------------

### Align items to the cross-end with items-end in HTML

Source: https://tailwindcss.com/docs/align-items

This example uses the `items-end` utility to align flex items to the end of the container's cross axis. This positions content at the bottom in a column layout or right in a row layout.

```html
<div class="flex items-end ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

--------------------------------

### Apply items-stretch for cross-axis stretching in HTML

Source: https://tailwindcss.com/docs/align-items

This example demonstrates the use of the `items-stretch` utility in Tailwind CSS. It causes flex items to stretch and fill the entire available space along the container's cross axis, ensuring consistent height or width based on the flex direction.

```html
<div class="flex items-stretch ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

--------------------------------

### Align items by text baseline with items-baseline in HTML

Source: https://tailwindcss.com/docs/align-items

The `items-baseline` utility is demonstrated here, aligning flex items such that all of their baselines align along the container's cross axis. This is particularly useful for ensuring text within different elements lines up correctly.

```html
<div class="flex items-baseline ...">  <div class="pt-2 pb-6">01</div>  <div class="pt-8 pb-12">02</div>  <div class="pt-12 pb-4">03</div></div>
```

--------------------------------

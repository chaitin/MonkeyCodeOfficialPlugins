### Apply responsive border width with breakpoint variants

Source: https://tailwindcss.com/docs/border-width

Prefix border-width utilities with breakpoint variants like md: to apply the utility only at medium screen sizes and above. This example applies a 2px border by default and 4px top border on medium screens.

```html
<div class="border-2 md:border-t-4 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Set custom border width with bracket notation

Source: https://tailwindcss.com/docs/border-width

Use the border-[<value>] syntax to apply a completely custom border width value that isn't available in the default Tailwind scale. This example sets a border width of 2vw.

```html
<div class="border-[2vw] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Add borders between child elements with divide utilities

Source: https://tailwindcss.com/docs/border-width

Use divide-x and divide-y utilities to add borders between child elements in a grid or flex layout. The example shows a 3-column grid with vertical dividers using divide-x-4.

```html
<div class="grid grid-cols-3 divide-x-4">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

--------------------------------

### Logical property border-width utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/border-width

Use logical border utilities (border-s for start, border-e for end) to create direction-aware layouts that adapt to text direction (LTR/RTL). These map to border-inline-start-width and border-inline-end-width CSS properties, automatically adjusting left/right based on dir attribute.

```html
<div dir="ltr">
  <div class="border-s-4 ..."></div>
</div>
<div dir="rtl">
  <div class="border-s-4 ..."></div>
</div>
```

--------------------------------

### Reverse divide direction for reversed flex layouts

Source: https://tailwindcss.com/docs/border-width

Use divide-x-reverse or divide-y-reverse utilities when elements are in reverse order (using flex-row-reverse or flex-col-reverse) to ensure borders appear on the correct side of each element.

```html
<div class="flex flex-col-reverse divide-y-4 divide-y-reverse divide-gray-200">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

--------------------------------

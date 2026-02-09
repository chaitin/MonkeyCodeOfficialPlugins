### Explicitly setting sort order with numeric classes

Source: https://tailwindcss.com/docs/order

Use order-<number> utilities to render flex and grid items in a different order than they appear in the document. This example demonstrates reordering three items using order-1, order-2, and order-3 classes.

```html
<div class="flex justify-between ...">
  <div class="order-3 ...">01</div>
  <div class="order-1 ...">02</div>
  <div class="order-2 ...">03</div>
</div>
```

--------------------------------

### Responsive order utility with breakpoint variants

Source: https://tailwindcss.com/docs/order

Prefix an order utility with a breakpoint variant like md: to apply the utility only at specific screen sizes, enabling responsive reordering across different device sizes.

```html
<div class="order-first md:order-last ...">
  <!-- ... -->
</div>
```

--------------------------------

### Ordering items first or last with utility classes

Source: https://tailwindcss.com/docs/order

Use order-first and order-last utilities to render flex and grid items at the beginning or end of the layout, regardless of their position in the DOM.

```html
<div class="flex justify-between ...">
  <div class="order-last ...">01</div>
  <div class="...">02</div>
  <div class="order-first ...">03</div>
</div>
```

--------------------------------

### Using custom arbitrary values for order

Source: https://tailwindcss.com/docs/order

Use the order-[<value>] syntax to set the order based on a completely custom value, allowing for complex expressions and calculations.

```html
<div class="order-[min(var(--total-items),10)] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Using CSS custom properties with order utility

Source: https://tailwindcss.com/docs/order

Use the order-(<custom-property>) syntax as shorthand for order-[var(<custom-property>)], which automatically wraps the custom property in the var() function.

```html
<div class="order-(--my-order) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Using negative order values

Source: https://tailwindcss.com/docs/order

Prefix the class name with a dash to convert the order value to a negative number, enabling reverse ordering or positioning items before default-ordered items.

```html
<div class="-order-1">
  <!-- ... -->
</div>
```

--------------------------------

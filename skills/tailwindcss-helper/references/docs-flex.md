### flex-initial Utility Example

Source: https://tailwindcss.com/docs/flex

Shows how to use flex-initial to allow flex items to shrink but not grow, while respecting their initial size. Items 02 and 03 will shrink if needed but won't expand beyond their defined widths.

```html
<div class="flex">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-initial ...">02</div>
  <div class="w-32 flex-initial ...">03</div>
</div>
```

--------------------------------

### Basic flex-1 Utility Example

Source: https://tailwindcss.com/docs/flex

Demonstrates using flex-1 utility class to allow flex items to grow and shrink proportionally. The example shows a flex container with three items where items 02 and 03 use flex-1 to share available space equally while item 01 remains fixed width with flex-none.

```html
<div class="flex">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-1 ...">02</div>
  <div class="w-32 flex-1 ...">03</div>
</div>
```

--------------------------------

### flex-auto Utility Example

Source: https://tailwindcss.com/docs/flex

Demonstrates flex-auto utility which allows flex items to grow and shrink while accounting for their initial size. Items 02 and 03 will expand or contract based on available space.

```html
<div class="flex ...">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-64 flex-auto ...">02</div>
  <div class="w-32 flex-auto ...">03</div>
</div>
```

--------------------------------

### flex-none Utility Example

Source: https://tailwindcss.com/docs/flex

Shows how to use flex-none to prevent flex items from growing or shrinking. Items 01 and 02 maintain their fixed widths regardless of container size, while item 03 with flex-1 takes remaining space.

```html
<div class="flex ...">
  <div class="w-14 flex-none ...">01</div>
  <div class="w-32 flex-none ...">02</div>
  <div class="flex-1 ...">03</div>
</div>
```

--------------------------------

### Custom flex Value with Bracket Notation

Source: https://tailwindcss.com/docs/flex

Demonstrates using the flex-[<value>] syntax to apply custom flex shorthand values not covered by standard utilities. This example uses flex-[3_1_auto] to set custom grow, shrink, and basis values.

```html
<div class="flex-[3_1_auto] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Responsive flex Utility with Breakpoint Variant

Source: https://tailwindcss.com/docs/flex

Demonstrates responsive design using breakpoint variants with flex utilities. The flex-none class applies at small screen sizes, then switches to flex-1 at medium screen sizes and above using the md: variant.

```html
<div class="flex-none md:flex-1 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Custom flex Property with CSS Variable

Source: https://tailwindcss.com/docs/flex

Shows how to use the flex-(<custom-property>) syntax to reference CSS custom properties. This automatically wraps the custom property in the var() function for cleaner syntax.

```html
<div class="flex-(--my-flex) ...">
  <!-- ... -->
</div>
```

--------------------------------

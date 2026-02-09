### justify-self with responsive breakpoints

Source: https://tailwindcss.com/docs/justify-self

Apply justify-self utilities conditionally at different screen sizes using breakpoint prefixes like md:, lg:, etc. This example changes alignment from start on mobile to end on medium screens and above.

```html
<div class="justify-self-start md:justify-self-end ...">
  <!-- ... -->
</div>
```

--------------------------------

### justify-self-start - Align grid item to inline start

Source: https://tailwindcss.com/docs/justify-self

Aligns a grid item to the start of its inline axis within the grid area. Useful for positioning items at the beginning of their grid cell.

```html
<div class="grid justify-items-stretch ...">
  <!-- ... -->
  <div class="justify-self-start ...">02</div>
  <!-- ... -->
</div>
```

--------------------------------

### justify-self-center - Center grid item on inline axis

Source: https://tailwindcss.com/docs/justify-self

Centers a grid item along the center of its inline axis. The justify-self-center-safe variant will align to the start if insufficient space is available, preventing content overflow.

```html
<div class="grid justify-items-stretch ...">
  <!-- ... -->
  <div class="justify-self-center ...">02</div>
  <!-- ... -->
</div>
```

```html
<div class="grid justify-items-stretch ...">
  <!-- ... -->
  <div class="justify-self-center-safe ...">02</div>
  <!-- ... -->
</div>
```

--------------------------------

### justify-self-end - Align grid item to inline end

Source: https://tailwindcss.com/docs/justify-self

Aligns a grid item to the end of its inline axis within the grid area. The justify-self-end-safe variant will align to the start if insufficient space is available to prevent overflow.

```html
<div class="grid justify-items-stretch ...">
  <!-- ... -->
  <div class="justify-self-end ...">02</div>
  <!-- ... -->
</div>
```

```html
<div class="grid justify-items-stretch ...">
  <!-- ... -->
  <div class="justify-self-end-safe ...">02</div>
  <!-- ... -->
</div>
```

--------------------------------

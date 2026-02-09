### Apply responsive min-height utilities in HTML

Source: https://tailwindcss.com/docs/min-height

Prefix min-height utilities with breakpoint variants like md: to apply the utility only at specific screen sizes. This example applies min-h-0 by default and min-h-full at medium screen sizes and above.

```html
<div class="h-24 min-h-0 md:min-h-full ...">
  <!-- ... -->
</div>
```

--------------------------------

### Apply min-height with percentage-based utilities in HTML

Source: https://tailwindcss.com/docs/min-height

Use min-h-full or min-h-<fraction> utilities like min-h-1/2, min-h-3/4, and min-h-9/10 to set percentage-based minimum heights. These utilities calculate the minimum height as a fraction of 100%.

```html
<div class="min-h-full ...">min-h-full</div>
<div class="min-h-9/10 ...">min-h-9/10</div>
<div class="min-h-3/4 ...">min-h-3/4</div>
<div class="min-h-1/2 ...">min-h-1/2</div>
<div class="min-h-1/3 ...">min-h-1/3</div>
```

--------------------------------

### Apply min-height with custom arbitrary values in HTML

Source: https://tailwindcss.com/docs/min-height

Use the min-h-[<value>] syntax to set minimum height with completely custom CSS values. This allows any valid CSS measurement to be applied directly without predefined utility classes.

```html
<div class="min-h-[220px] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Apply min-height with custom CSS properties in HTML

Source: https://tailwindcss.com/docs/min-height

Use the min-h-(<custom-property>) syntax as shorthand for min-h-[var(<custom-property>)] to reference custom CSS properties. This automatically wraps the custom property in the var() function.

```html
<div class="min-h-(--my-min-height) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Apply min-height with spacing scale utilities in HTML

Source: https://tailwindcss.com/docs/min-height

Use min-h-<number> utilities like min-h-24, min-h-48, min-h-64, and min-h-80 to set fixed minimum heights based on Tailwind's spacing scale. Each utility applies min-height using the --spacing theme variable multiplied by the specified number.

```html
<div class="h-20 ...">
  <div class="min-h-80 ...">min-h-80</div>
  <div class="min-h-64 ...">min-h-64</div>
  <div class="min-h-48 ...">min-h-48</div>
  <div class="min-h-40 ...">min-h-40</div>
  <div class="min-h-32 ...">min-h-32</div>
  <div class="min-h-24 ...">min-h-24</div>
</div>
```

--------------------------------

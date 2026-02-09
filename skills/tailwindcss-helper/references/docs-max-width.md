### Container utility with responsive breakpoints in HTML

Source: https://tailwindcss.com/docs/max-width

Use the container utility to set maximum width matching the min-width of the current breakpoint, enabling fixed-width design for specific screen sizes. Combine with mx-auto for centering and px-<number> for horizontal padding, as the container utility does not auto-center or include built-in padding.

```html
<div class="container">  <!-- ... --></div>
<div class="container mx-auto px-4">  <!-- ... --></div>
```

--------------------------------

### Basic max-width with spacing scale in HTML

Source: https://tailwindcss.com/docs/max-width

Apply fixed maximum widths using numeric utilities based on the spacing scale. The max-w-<number> utilities set max-width to calc(var(--spacing) * <number>). Combine with w-full to allow elements to shrink below the maximum width on smaller viewports.

```html
<div class="w-full max-w-96 ...">max-w-96</div>
<div class="w-full max-w-80 ...">max-w-80</div>
<div class="w-full max-w-64 ...">max-w-64</div>
<div class="w-full max-w-48 ...">max-w-48</div>
<div class="w-full max-w-40 ...">max-w-40</div>
<div class="w-full max-w-32 ...">max-w-32</div>
<div class="w-full max-w-24 ...">max-w-24</div>
```

--------------------------------

### Custom max-width values with bracket notation in HTML

Source: https://tailwindcss.com/docs/max-width

Use the max-w-[<value>] syntax to apply arbitrary custom maximum width values not covered by predefined utilities. This allows pixel-perfect sizing for specific design requirements.

```html
<div class="max-w-[220px] ...">  <!-- ... --></div>
```

--------------------------------

### Percentage-based max-width with fractions in HTML

Source: https://tailwindcss.com/docs/max-width

Use fractional utilities like max-w-1/2, max-w-3/4, and max-w-9/10 to set percentage-based maximum widths. These utilities calculate max-width as calc(<fraction> * 100%), allowing responsive width constraints relative to the parent container.

```html
<div class="w-full max-w-9/10 ...">max-w-9/10</div>
<div class="w-full max-w-3/4 ...">max-w-3/4</div>
<div class="w-full max-w-1/2 ...">max-w-1/2</div>
<div class="w-full max-w-1/3 ...">max-w-1/3</div>
```

--------------------------------

### Responsive max-width with breakpoint variants in HTML

Source: https://tailwindcss.com/docs/max-width

Prefix max-width utilities with breakpoint variants like md:, lg:, or xl: to apply different maximum widths at specific screen sizes. This enables responsive design patterns where element constraints adapt to viewport dimensions.

```html
<div class="max-w-sm md:max-w-lg ...">  <!-- ... --></div>
```

--------------------------------

### Custom max-width with CSS variables in HTML

Source: https://tailwindcss.com/docs/max-width

Use the max-w-(<custom-property>) syntax as shorthand for max-w-[var(<custom-property>)] to reference CSS custom properties. This automatically wraps the custom property in the var() function for cleaner, more maintainable code.

```html
<div class="max-w-(--my-max-width) ...">  <!-- ... --></div>
```

--------------------------------

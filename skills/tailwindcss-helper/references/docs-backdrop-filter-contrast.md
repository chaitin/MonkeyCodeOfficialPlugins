### Apply responsive backdrop contrast with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/backdrop-filter-contrast

Use breakpoint variants like md: to apply backdrop-contrast utilities only at specific screen sizes. This example applies backdrop-contrast-125 by default and backdrop-contrast-150 at medium screen sizes and above.

```html
<div class="backdrop-contrast-125 md:backdrop-contrast-150 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Set custom backdrop contrast value with bracket notation

Source: https://tailwindcss.com/docs/backdrop-filter-contrast

Use the backdrop-contrast-[<value>] syntax to apply a completely custom backdrop contrast value that isn't available as a predefined utility class.

```html
<div class="backdrop-contrast-[.25] ...">
  <!-- ... -->
</div>
```

--------------------------------

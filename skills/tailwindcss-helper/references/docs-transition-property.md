### Custom transition-property with bracket notation

Source: https://tailwindcss.com/docs/transition-property

Uses the transition-[<value>] syntax to apply custom CSS property values for transitions. This example transitions the height property specifically, allowing fine-grained control over which properties animate.

```html
<button class="transition-[height] ...">  <!-- ... --></button>
```

--------------------------------

### Responsive transition-property with breakpoint variant

Source: https://tailwindcss.com/docs/transition-property

Uses the md: breakpoint variant to conditionally apply transition utilities at medium screen sizes and above. This example applies no transition by default and enables all transitions on medium and larger screens.

```html
<button class="transition-none md:transition-all ...">  <!-- ... --></button>
```

--------------------------------

### Apply custom contrast value with bracket notation

Source: https://tailwindcss.com/docs/filter-contrast

Use the contrast-[<value>] syntax to set contrast with completely custom values not covered by predefined utilities. This allows arbitrary contrast values to be applied directly.

```html
<img class="contrast-[.25] ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply responsive contrast filter with breakpoint variants

Source: https://tailwindcss.com/docs/filter-contrast

Prefix contrast utilities with breakpoint variants like md: to apply different contrast levels at specific screen sizes. This enables responsive contrast adjustments across different device widths.

```html
<img class="contrast-125 md:contrast-150 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply contrast filter using CSS custom properties

Source: https://tailwindcss.com/docs/filter-contrast

Use the contrast-(<custom-property>) syntax as shorthand for contrast-[var(<custom-property>)] to reference CSS variables. This automatically wraps the custom property in the var() function.

```html
<img class="contrast-(--my-contrast) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply contrast filter with predefined Tailwind utilities

Source: https://tailwindcss.com/docs/filter-contrast

Use predefined contrast utility classes like contrast-50, contrast-100, contrast-125, and contrast-200 to apply specific contrast levels to images and elements. These utilities generate filter: contrast() CSS with percentage values.

```html
<img class="contrast-50 ..." src="/img/mountains.jpg" />
<img class="contrast-100 ..." src="/img/mountains.jpg" />
<img class="contrast-125 ..." src="/img/mountains.jpg" />
<img class="contrast-200 ..." src="/img/mountains.jpg" />
```

--------------------------------

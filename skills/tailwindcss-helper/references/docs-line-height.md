### Custom line-height values with bracket notation in Tailwind CSS

Source: https://tailwindcss.com/docs/line-height

Use leading-[<value>] syntax to apply arbitrary line-height values not covered by default utilities. This example sets a custom line-height of 1.5 using bracket notation.

```html
<p class="leading-[1.5] ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Responsive line-height with breakpoint variants in Tailwind CSS

Source: https://tailwindcss.com/docs/line-height

Prefix line-height utilities with breakpoint variants like md: to apply different line heights at specific screen sizes. This example uses leading-5 on mobile and leading-6 on medium screens and above.

```html
<p class="leading-5 md:leading-6 ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Combined font-size and line-height with Tailwind CSS

Source: https://tailwindcss.com/docs/line-height

Use text-<size>/<number> utilities to set both font size and line height simultaneously. This example demonstrates three different line-height values (6, 7, 8) applied to text-base font size using Tailwind CSS classes.

```html
<p class="text-base/6 ...">So I started to walk into the water...</p>
<p class="text-base/7 ...">So I started to walk into the water...</p>
<p class="text-base/8 ...">So I started to walk into the water...</p>
```

--------------------------------

### Independent line-height with leading utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/line-height

Use leading-<number> utilities to set line height independently of font size. This example applies different leading values (6, 7, 8) to paragraphs with text-sm font size, allowing flexible control over line spacing.

```html
<p class="text-sm leading-6">So I started to walk into the water...</p>
<p class="text-sm leading-7">So I started to walk into the water...</p>
<p class="text-sm leading-8">So I started to walk into the water...</p>
```

--------------------------------

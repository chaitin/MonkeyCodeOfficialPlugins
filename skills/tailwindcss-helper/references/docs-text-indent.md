### Apply responsive text indentation with breakpoint variants

Source: https://tailwindcss.com/docs/text-indent

Prefix text-indent utilities with breakpoint variants like md: to apply different indentation values at different screen sizes. This example applies indent-4 on small screens and indent-8 on medium screens and above.

```html
<p class="indent-4 md:indent-8 ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply custom text indentation values with bracket notation

Source: https://tailwindcss.com/docs/text-indent

Use the indent-[<value>] syntax to set text indentation with completely custom values not in the default scale. This allows arbitrary CSS values like percentages, pixels, or other units to be applied directly.

```html
<p class="indent-[50%] ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply text indentation with indent utility classes

Source: https://tailwindcss.com/docs/text-indent

Use indent-<number> utilities to set the amount of empty space before text in a block. The indent-8 class applies an 8-unit indentation based on the spacing scale. This is useful for formatting paragraphs and improving readability.

```html
<p class="indent-8">So I started to walk into the water...</p>
```

--------------------------------

### Apply custom text indentation with CSS variables

Source: https://tailwindcss.com/docs/text-indent

Use the indent-(<custom-property>) syntax as shorthand for indent-[var(<custom-property>)] to reference CSS custom properties. This automatically wraps the custom property in the var() function.

```html
<p class="indent-(--my-indentation) ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

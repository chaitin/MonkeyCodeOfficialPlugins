### Apply Responsive Accent Color with Breakpoint Variant

Source: https://tailwindcss.com/docs/accent-color

Use the accent-color utility with breakpoint prefixes to apply different accent colors at specific screen sizes. This example applies accent-black by default and switches to accent-pink-500 at medium screen sizes and above using the md: variant.

```html
<input class="accent-black md:accent-pink-500 ..." type="checkbox" />
```

--------------------------------

### Use Custom Theme Color in Markup

Source: https://tailwindcss.com/docs/accent-color

Apply custom theme colors defined in your theme configuration directly in your HTML markup using the generated utility classes. This example uses the accent-regal-blue utility created from the custom theme variable.

```html
<input class="accent-regal-blue" type="checkbox" />
```

--------------------------------

### Customize Theme Colors with CSS Variables

Source: https://tailwindcss.com/docs/accent-color

Define custom color values in your Tailwind theme using CSS custom properties (--color-*). This creates new utility classes that can be used throughout your project. The example defines a custom regal-blue color that becomes available as the accent-regal-blue utility.

```css
@theme {
  --color-regal-blue: #243c5a;
}
```

--------------------------------

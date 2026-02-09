### Apply Text Shadow Color Utilities - Tailwind CSS HTML

Source: https://tailwindcss.com/docs/text-shadow

HTML examples demonstrating how to apply Tailwind CSS text-shadow color utility classes to elements. Each class applies a specific color from the palette to the text shadow. Classes follow the naming convention text-shadow-[color]-[shade] where shade ranges from 50 to 950.

```html
<p class="text-shadow-yellow-100">Yellow 100 text shadow</p>
<p class="text-shadow-yellow-500">Yellow 500 text shadow</p>
<p class="text-shadow-yellow-900">Yellow 900 text shadow</p>
<p class="text-shadow-lime-200">Lime 200 text shadow</p>
<p class="text-shadow-lime-600">Lime 600 text shadow</p>
<p class="text-shadow-green-300">Green 300 text shadow</p>
<p class="text-shadow-green-700">Green 700 text shadow</p>
<p class="text-shadow-emerald-400">Emerald 400 text shadow</p>
<p class="text-shadow-emerald-800">Emerald 800 text shadow</p>
<p class="text-shadow-teal-100">Teal 100 text shadow</p>

```

--------------------------------

### Apply Custom Text Shadow Utility in Markup

Source: https://tailwindcss.com/docs/text-shadow

Use the custom text shadow utility defined in the theme configuration. Once `text-shadow-xl` is defined via theme variables, it can be applied directly to HTML elements as a utility class.

```html
<p class="text-shadow-xl">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply Responsive Text Shadow with Breakpoint Variant

Source: https://tailwindcss.com/docs/text-shadow

Use the `md:` breakpoint variant to apply text shadow utilities only at medium screen sizes and above. This demonstrates responsive design in Tailwind CSS where utilities are conditionally applied based on screen width.

```html
<p class="text-shadow-none md:text-shadow-lg ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

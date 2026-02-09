### Apply responsive font-stretch utilities in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/font-stretch

This example shows how to make `font-stretch` utilities responsive by prefixing them with breakpoint variants, such as `md:font-stretch-expanded`. This allows the font width to change based on screen size, adapting the design for different devices as explained in the variants documentation.

```html
<div class="font-stretch-normal md:font-stretch-expanded ...">  <!-- ... --></div>
```

--------------------------------

### Apply percentage-based font-stretch in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/font-stretch

This example shows how to use Tailwind CSS `font-stretch-<percentage>` utilities, such as `font-stretch-50%`, `font-stretch-100%`, and `font-stretch-150%`, to set the font face width using specific percentage values. This provides fine-grained control over font stretching for fonts that support it.

```html
<p class="font-stretch-50%">The quick brown fox...</p><p class="font-stretch-100%">The quick brown fox...</p><p class="font-stretch-150%">The quick brown fox...</p>
```

--------------------------------

### Apply basic font-stretch utilities in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/font-stretch

This example demonstrates how to use predefined Tailwind CSS `font-stretch` utility classes like `font-stretch-extra-condensed`, `font-stretch-condensed`, `font-stretch-normal`, `font-stretch-expanded`, and `font-stretch-extra-expanded` to control the width of text elements. These classes apply to fonts that have multiple width variations available, otherwise the browser selects the closest match.

```html
<p class="font-stretch-extra-condensed">The quick brown fox...</p><p class="font-stretch-condensed">The quick brown fox...</p><p class="font-stretch-normal">The quick brown fox...</p><p class="font-stretch-expanded">The quick brown fox...</p><p class="font-stretch-extra-expanded">The quick brown fox...</p>
```

--------------------------------

### Apply CSS variable for font-stretch in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/font-stretch

This example demonstrates how to use the `font-stretch-(<custom-property>)` syntax in Tailwind CSS to apply a font width defined by a CSS variable. This is a shorthand for `font-stretch-[var(<custom-property>)]`, enabling dynamic font stretching based on CSS custom properties.

```html
<p class="font-stretch-(--my-font-width) ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply custom font-stretch values in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/font-stretch

This example illustrates the use of Tailwind CSS's arbitrary value syntax `font-stretch-[<value>]` to apply a completely custom font width, such as `font-stretch-[66.66%]`. This allows for highly specific styling not covered by predefined classes.

```html
<p class="font-stretch-[66.66%] ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

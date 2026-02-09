### Apply Responsive Clears with Tailwind CSS Breakpoint Variants

Source: https://tailwindcss.com/docs/clear

This example illustrates how to apply `clear` utilities conditionally based on screen size using Tailwind CSS responsive variants. By prefixing `clear-none` with `md:`, the `clear-none` utility will only take effect at medium screen sizes and above, while `clear-left` is applied by default. This allows for flexible layout adjustments across different devices.

```html
<p class="clear-left md:clear-none ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Disable Clears with Tailwind CSS `clear-none` Utility

Source: https://tailwindcss.com/docs/clear

This snippet demonstrates how to reset any applied clears on an HTML element using the `clear-none` utility class in Tailwind CSS. It is typically used to override previous clear properties, ensuring the element does not break its layout due to floating elements. The example shows `clear-none` applied to a paragraph element within an article containing floated images.

```html
<article>  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/snow-mountains.jpg" />  <p class="clear-none ...">Maybe we can live without libraries...</p></article>
```

--------------------------------

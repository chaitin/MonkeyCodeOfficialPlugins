### Combine Multiple Numeric Font Variants with Tailwind CSS

Source: https://tailwindcss.com/docs/font-variant-numeric

The `font-variant-numeric` utilities are composable, allowing you to combine multiple variants for specific typographic needs. This example demonstrates using `slashed-zero` and `tabular-nums` together for financial figures.

```html
<dl class="...">  <dt class="...">Subtotal</dt>  <dd class="text-right slashed-zero tabular-nums ...">$100.00</dd>  <dt class="...">Tax</dt>  <dd class="text-right slashed-zero tabular-nums ...">$14.50</dd>  <dt class="...">Total</dt>  <dd class="text-right slashed-zero tabular-nums ...">$114.50</dd></dl>
```

--------------------------------

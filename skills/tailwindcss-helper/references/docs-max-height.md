### Set Percentage-Based Maximum Height with Tailwind CSS

Source: https://tailwindcss.com/docs/max-height

This HTML example illustrates how to use Tailwind CSS `max-h-<fraction>` utilities to apply percentage-based maximum heights to elements. It shows various fractional values like `max-h-1/2` and `max-h-3/4`, along with `max-h-full`, within a parent container.

```html
<div class="h-96 ...">  <div class="h-full max-h-9/10 ...">max-h-9/10</div>  <div class="h-full max-h-3/4 ...">max-h-3/4</div>  <div class="h-full max-h-1/2 ...">max-h-1/2</div>  <div class="h-full max-h-1/4 ...">max-h-1/4</div>  <div class="h-full max-h-full ...">max-h-full</div></div>
```

--------------------------------

### Apply Custom CSS Variable Maximum Height with Tailwind CSS

Source: https://tailwindcss.com/docs/max-height

This HTML example shows how to use the `max-h-(<custom-property>)` syntax in Tailwind CSS to set a maximum height based on a CSS variable. It automatically wraps the custom property in `var()` for convenience.

```html
<div class="max-h-(--my-max-height) ...">  <!-- ... --></div>
```

--------------------------------

### Implement Responsive Maximum Height with Tailwind CSS

Source: https://tailwindcss.com/docs/max-height

This HTML snippet illustrates how to apply responsive maximum height utilities in Tailwind CSS using breakpoint prefixes. It sets a default `max-h-full` and then overrides it with `max-h-screen` for medium screen sizes and above.

```html
<div class="h-48 max-h-full md:max-h-screen ...">  <!-- ... --></div>
```

--------------------------------

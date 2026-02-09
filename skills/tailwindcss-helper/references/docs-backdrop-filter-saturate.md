### Apply backdrop saturation with Tailwind CSS utilities

Source: https://tailwindcss.com/docs/backdrop-filter-saturate

Use backdrop-saturate-<number> utilities to control backdrop saturation levels. Available classes include backdrop-saturate-50, backdrop-saturate-100, backdrop-saturate-125, and backdrop-saturate-200. Each utility applies the corresponding saturate percentage to the backdrop-filter CSS property.

```html
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-saturate-50 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-saturate-125 ..."></div>
</div>
<div class="bg-[url(/img/mountains.jpg)]">
  <div class="bg-white/30 backdrop-saturate-200 ..."></div>
</div>
```

--------------------------------

### Reference CSS custom properties for backdrop saturation

Source: https://tailwindcss.com/docs/backdrop-filter-saturate

Use the backdrop-saturate-(<custom-property>) syntax to reference CSS custom properties for backdrop saturation values. This is shorthand for backdrop-saturate-[var(<custom-property>)] and automatically wraps the value in the var() function.

```html
<div class="backdrop-saturate-(--my-backdrop-saturation) ...">
  <!-- ... -->
</div>
```

--------------------------------

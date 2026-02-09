### Apply responsive perspective-origin utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/perspective-origin

This snippet shows how to make `perspective-origin` utilities responsive by prefixing them with breakpoint variants like `md:`. It demonstrates applying `perspective-origin-center` by default and overriding it with `perspective-origin-bottom-left` from medium screens and up, adapting the perspective origin based on screen size.

```html
<div class="perspective-origin-center md:perspective-origin-bottom-left ...">
  <!-- ... --></div>
```

--------------------------------

### Apply Tailwind CSS perspective-origin utilities for basic positioning

Source: https://tailwindcss.com/docs/perspective-origin

This snippet demonstrates how to use predefined Tailwind CSS classes like `perspective-origin-top-left` and `perspective-origin-bottom-right` to control the vanishing point of a 3D perspective on HTML elements. It shows two `div` containers, each with a different perspective origin applied to illustrate the effect.

```html
<div class="size-20 perspective-near perspective-origin-top-left ...">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 perspective-near perspective-origin-bottom-right …">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

--------------------------------

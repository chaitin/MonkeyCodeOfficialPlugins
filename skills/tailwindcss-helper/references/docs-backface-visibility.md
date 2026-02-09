### Apply Responsive backface-visibility Utility in HTML

Source: https://tailwindcss.com/docs/backface-visibility

This example shows how to apply the `backface-hidden` utility responsively using Tailwind CSS. The `md:backface-hidden` class ensures that the backface is hidden only on medium screen sizes and above, while it remains visible by default or on smaller screens.

```html
<div class="backface-visible md:backface-hidden ...">
  <!-- ... -->
</div>
```

--------------------------------

### Apply backface-visibility Utilities in HTML

Source: https://tailwindcss.com/docs/backface-visibility

This example demonstrates how to use Tailwind CSS `backface-hidden` and `backface-visible` utilities on HTML elements. It shows two sets of elements, simulating a 3D cube, where one set hides the backface when rotated away, and the other keeps it visible, illustrating the visual difference.

```html
<div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-hidden ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-hidden ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-hidden ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-hidden ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-hidden ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-hidden ...">6</div></div><div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-visible ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-visible ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-visible ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-visible ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-visible ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-visible ...">6</div></div>
```

--------------------------------

### Apply Responsive Transform Origin in Tailwind CSS

Source: https://tailwindcss.com/docs/transform-origin

Explains how to apply `transform-origin` utilities conditionally based on screen size using responsive prefixes like `md:`. This allows for different origin points to be set for elements at various breakpoints, adapting to responsive layouts.

```html
<img class="origin-center md:origin-top ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Transform Origin with CSS Variable in Tailwind CSS

Source: https://tailwindcss.com/docs/transform-origin

Shows how to use the `origin-(<custom-property>)` syntax to set the `transform-origin` based on a CSS variable. This is a convenient shorthand for `origin-[var(<custom-property>)]`, promoting reusability and dynamic styling.

```html
<img class="origin-(--my-transform-origin) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Negative Scale Transforms with Tailwind CSS

Source: https://tailwindcss.com/docs/scale

Demonstrates how to use negative scale utilities such as `-scale-<number>`, `-scale-x-<number>`, or `-scale-y-<number>` to mirror and scale down elements.

```html
<img class="-scale-x-75 ..." src="/img/mountains.jpg" /><img class="-scale-100 ..." src="/img/mountains.jpg" /><img class="-scale-y-125 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Basic Scale Transforms with Tailwind CSS

Source: https://tailwindcss.com/docs/scale

Demonstrates how to use `scale-<number>` utilities like `scale-75`, `scale-100`, and `scale-125` to scale an element uniformly by a percentage of its original size.

```html
<img class="scale-75 ..." src="/img/mountains.jpg" /><img class="scale-100 ..." src="/img/mountains.jpg" /><img class="scale-125 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Custom Scale Values with Tailwind CSS

Source: https://tailwindcss.com/docs/scale

Explains how to use arbitrary values with `scale-[<value>]` for precise scaling, and how to use CSS variables with `scale-(<custom-property>)` as a shorthand for `scale-[var(<custom-property>)]`.

```html
<img class="scale-[1.7] ..." src="/img/mountains.jpg" />
```

```html
<img class="scale-(--my-scale) ..." src="/img/mountains.jpg" />
```

--------------------------------

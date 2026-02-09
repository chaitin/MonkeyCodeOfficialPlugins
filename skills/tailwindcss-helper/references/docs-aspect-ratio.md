### Apply responsive aspect ratios using Tailwind CSS variants

Source: https://tailwindcss.com/docs/aspect-ratio

Explains how to use responsive variants like `md:` to apply different aspect ratios based on screen size. This example shows an `<iframe>` that is `aspect-video` by default and transitions to `aspect-square` on medium screens and above.

```html
<iframe class="aspect-video md:aspect-square ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

--------------------------------

### Use a custom aspect ratio utility defined in Tailwind CSS theme

Source: https://tailwindcss.com/docs/aspect-ratio

Shows how to apply a custom aspect ratio utility, previously defined in the Tailwind CSS theme, to an HTML element. This example uses the `aspect-retro` utility on an `<iframe>` to apply the custom 4/3 ratio.

```html
<iframe class="aspect-retro" src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

--------------------------------

### Define a custom aspect ratio utility in Tailwind CSS theme

Source: https://tailwindcss.com/docs/aspect-ratio

Illustrates how to customize the Tailwind CSS theme by defining a new aspect ratio utility using the `--aspect-*` theme variables. This example creates an `aspect-retro` utility with a 4/3 ratio, making it available for use in markup.

```css
@theme {  --aspect-retro: 4 / 3; }
```

--------------------------------

### Set a custom aspect ratio with arbitrary values in Tailwind CSS

Source: https://tailwindcss.com/docs/aspect-ratio

Shows how to use the `aspect-[<value>]` syntax to define a completely custom aspect ratio using an arbitrary value, such as a CSS `calc()` function. This provides flexibility beyond predefined ratios for unique layout requirements.

```html
<img class="aspect-[calc(4*3+1)/3] ..." src="/img/villas.jpg" />
```

--------------------------------

### Apply a custom aspect ratio using a CSS variable in Tailwind CSS

Source: https://tailwindcss.com/docs/aspect-ratio

Demonstrates applying an aspect ratio using a CSS variable with the `aspect-(<custom-property>)` shorthand syntax. This is equivalent to `aspect-[var(<custom-property>)]`, allowing for dynamic aspect ratio control via CSS variables.

```html
<img class="aspect-(--my-aspect-ratio) ..." src="/img/villas.jpg" />
```

--------------------------------

### Apply a specific aspect ratio to an element using Tailwind CSS

Source: https://tailwindcss.com/docs/aspect-ratio

Demonstrates how to use `aspect-<ratio>` utilities, such as `aspect-3/2`, to set a fixed aspect ratio on an HTML element like an image. The `object-cover` class is also included to show how the image content fits within the defined aspect ratio.

```html
<img class="aspect-3/2 object-cover ..." src="/img/villas.jpg" />
```

--------------------------------

### Apply a 16:9 video aspect ratio to an iframe using Tailwind CSS

Source: https://tailwindcss.com/docs/aspect-ratio

Illustrates the use of the `aspect-video` utility to apply a common 16:9 aspect ratio to an `<iframe>` element. This ensures that embedded videos maintain their correct proportions, preventing distortion.

```html
<iframe class="aspect-video ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

--------------------------------

### Apply responsive background-clip utilities in HTML (Tailwind CSS)

Source: https://tailwindcss.com/docs/background-clip

Shows how to apply `background-clip` utilities conditionally based on screen size using responsive prefixes like `md:` in Tailwind CSS. This enables developers to implement different background clipping behaviors on various breakpoints, facilitating adaptive and responsive web design.

```html
<div class="bg-clip-border md:bg-clip-padding ...">  <!-- ... --></div>
```

--------------------------------

### Apply basic background-clip utilities in HTML (Tailwind CSS)

Source: https://tailwindcss.com/docs/background-clip

Demonstrates the use of `bg-clip-border`, `bg-clip-padding`, and `bg-clip-content` utilities to define the bounding box for an element's background in Tailwind CSS. These utilities control how the background extends relative to the element's border, padding, or content area, allowing precise control over background visibility.

```html
<div class="border-4 bg-indigo-500 bg-clip-border p-3"></div><div class="border-4 bg-indigo-500 bg-clip-padding p-3"></div><div class="border-4 bg-indigo-500 bg-clip-content p-3"></div>
```

--------------------------------

### Crop background to text shape in HTML (Tailwind CSS)

Source: https://tailwindcss.com/docs/background-clip

Illustrates how to use the `bg-clip-text` utility to crop an element's background to match the shape of the text. This is typically combined with gradient backgrounds and `text-transparent` to create visually striking text with gradient fills, enhancing design aesthetics.

```html
<p class="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-5xl font-extrabold text-transparent ...">  Hello world</p>
```

--------------------------------

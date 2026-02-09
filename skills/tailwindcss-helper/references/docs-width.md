### Apply Percentage-Based Widths with Tailwind CSS `w-<fraction>` Utilities

Source: https://tailwindcss.com/docs/width

This example illustrates how to use Tailwind CSS `w-full` or `w-<fraction>` utilities to assign percentage-based widths to elements. It shows various fractional widths like `w-1/2`, `w-2/5`, `w-1/3`, `w-1/4`, `w-1/5`, and `w-1/6` within a flex container to demonstrate responsive layout capabilities.

```html
<div class="flex ...">  <div class="w-1/2 ...">w-1/2</div>  <div class="w-1/2 ...">w-1/2</div></div><div class="flex ...">  <div class="w-2/5 ...">w-2/5</div>  <div class="w-3/5 ...">w-3/5</div></div><div class="flex ...">  <div class="w-1/3 ...">w-1/3</div>  <div class="w-2/3 ...">w-2/3</div></div><div class="flex ...">  <div class="w-1/4 ...">w-1/4</div>  <div class="w-3/4 ...">w-3/4</div></div><div class="flex ...">  <div class="w-1/5 ...">w-1/5</div>  <div class="w-4/5 ...">w-4/5</div></div><div class="flex ...">  <div class="w-1/6 ...">w-1/6</div>  <div class="w-5/6 ...">w-5/6</div></div><div class="w-full ...">w-full</div>
```

--------------------------------

### Set Widths Based on Container Scale with Tailwind CSS Utilities

Source: https://tailwindcss.com/docs/width

This example demonstrates how to apply fixed widths to elements using Tailwind CSS utilities like `w-sm` and `w-xl`, which are based on a predefined container scale. These utilities provide consistent sizing relative to common container breakpoints.

```html
<div class="w-xl ...">w-xl</div><div class="w-lg ...">w-lg</div><div class="w-md ...">w-md</div><div class="w-sm ...">w-sm</div><div class="w-xs ...">w-xs</div><div class="w-2xs ...">w-2xs</div><div class="w-3xs ...">w-3xs</div>
```

--------------------------------

### Match Viewport Width with Tailwind CSS `w-screen` Utility

Source: https://tailwindcss.com/docs/width

This example shows how to use the Tailwind CSS `w-screen` utility to make an element span the entire width of the viewport. It also mentions `w-lvw`, `w-svw`, and `w-dvw` for matching large, small, or dynamic viewports, respectively, providing flexible viewport-relative sizing.

```html
<div class="w-screen">  <!-- ... --></div>
```

--------------------------------

### Set Fixed Width with Tailwind CSS `w-<number>` Utilities

Source: https://tailwindcss.com/docs/width

This example demonstrates how to use Tailwind CSS `w-<number>` utilities to set an element's width based on a predefined spacing scale. These utilities apply a fixed width, calculated from a base spacing variable, to HTML `div` elements.

```html
<div class="w-96 ...">w-96</div><div class="w-80 ...">w-80</div><div class="w-64 ...">w-64</div><div class="w-48 ...">w-48</div><div class="w-40 ...">w-40</div><div class="w-32 ...">w-32</div><div class="w-24 ...">w-24</div>
```

--------------------------------

### Reset Element Width Conditionally with Tailwind CSS `w-auto`

Source: https://tailwindcss.com/docs/width

This example demonstrates how to use the Tailwind CSS `w-auto` utility to reset an element's width under specific conditions, such as at a particular breakpoint. Here, `md:w-auto` ensures the width is `auto` on medium screens and above, overriding `w-full`.

```html
<div class="w-full md:w-auto">  <!-- ... --></div>
```

--------------------------------

### Apply Responsive Width Utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/width

This snippet demonstrates how to make width utilities responsive using breakpoint variants like `md:`. This allows an element's width to change based on screen size, applying `w-1/2` by default and `w-full` from medium screens upwards.

```html
<div class="w-1/2 md:w-full ...">  <!-- ... --></div>
```

--------------------------------

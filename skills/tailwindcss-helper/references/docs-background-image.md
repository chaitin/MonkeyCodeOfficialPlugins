### Apply Responsive Gradient Utilities with Breakpoint Variants

Source: https://tailwindcss.com/docs/background-image

Prefix background-image utilities with breakpoint variants like md: to apply gradients only at specific screen sizes. This enables responsive design patterns where gradient colors or styles change based on viewport width.

```html
<div class="from-purple-400 md:from-yellow-500 ...">  <!-- ... --></div>
```

--------------------------------

### Create Conic Gradient Backgrounds with Tailwind CSS

Source: https://tailwindcss.com/docs/background-image

Use bg-conic and bg-conic-<angle> utilities with color stop utilities to create conic gradients. Supports angle variants and color stop positioning for circular gradient effects.

```html
<div class="size-24 rounded-full bg-conic from-blue-600 to-sky-400 to-50%"></div>
<div class="size-24 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600"></div>
<div class="size-24 rounded-full bg-conic/decreasing from-violet-700 via-lime-300 to-violet-700"></div>
```

--------------------------------

### Create Radial Gradient Backgrounds with Tailwind CSS

Source: https://tailwindcss.com/docs/background-image

Use bg-radial and bg-radial-[<position>] utilities with color stop utilities to create radial gradients. Supports positioning syntax and percentage-based color stop placement for precise gradient control.

```html
<div class="size-18 rounded-full bg-radial from-pink-400 from-40% to-fuchsia-700"></div>
<div class="size-18 rounded-full bg-radial-[at_50%_75%] from-sky-200 via-blue-400 to-indigo-900 to-90%"></div>
<div class="size-18 rounded-full bg-radial-[at_25%_25%] from-white to-zinc-900 to-75%"></div>
```

--------------------------------

### Create Linear Gradient Backgrounds with Tailwind CSS

Source: https://tailwindcss.com/docs/background-image

Use directional utilities like bg-linear-to-r, bg-linear-to-t, and angle-based variants combined with color stop utilities (from-*, via-*, to-*) to create linear gradients. Supports 8 directional variants and custom angles.

```html
<div class="h-14 bg-linear-to-r from-cyan-500 to-blue-500"></div>
<div class="h-14 bg-linear-to-t from-sky-500 to-indigo-500"></div>
<div class="h-14 bg-linear-to-bl from-violet-500 to-fuchsia-500"></div>
<div class="h-14 bg-linear-65 from-purple-500 to-pink-500"></div>
```

--------------------------------

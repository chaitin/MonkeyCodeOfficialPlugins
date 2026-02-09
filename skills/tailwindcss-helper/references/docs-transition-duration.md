### Apply predefined transition durations with Tailwind CSS

Source: https://tailwindcss.com/docs/transition-duration

This example demonstrates how to set standard transition durations using Tailwind CSS utilities like `duration-150`, `duration-300`, and `duration-700`. These classes apply a `transition-duration` CSS property in milliseconds to elements, enabling smooth visual changes upon interaction.

```html
<button class="transition duration-150 ease-in-out ...">Button A</button><button class="transition duration-300 ease-in-out ...">Button B</button><button class="transition duration-700 ease-in-out ...">Button C</button>
```

--------------------------------

### Apply responsive transition durations with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/transition-duration

This example shows how to make transition durations responsive using Tailwind CSS breakpoint variants. The `md:duration-150` class applies a 150ms duration only at medium screen sizes and above, while `duration-0` acts as a default for smaller screens, enabling adaptive UI behavior.

```html
<button class="duration-0 md:duration-150 ...">  <!-- ... --></button>
```

--------------------------------

### Set custom transition duration values with Tailwind CSS arbitrary values

Source: https://tailwindcss.com/docs/transition-duration

This example illustrates using arbitrary value syntax `duration-[<value>]` to apply highly specific or multiple transition durations. The `duration-[1s,15s]` class directly sets the `transition-duration` CSS property to `1s, 15s`, allowing for flexible control beyond predefined scales.

```html
<button class="duration-[1s,15s] ...">  <!-- ... --></button>
```

--------------------------------

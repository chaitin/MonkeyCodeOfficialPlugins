### Responsive Animation with Breakpoint Variants

Source: https://tailwindcss.com/docs/animation

Shows how to use breakpoint prefixes like `md:` to conditionally apply animations at specific screen sizes. In this example, the animation is disabled by default but enabled at medium screen sizes and above.

```html
<div class="animate-none md:animate-spin ...">
  <!-- ... -->
</div>
```

--------------------------------

### Customize Animation Theme with CSS Variables

Source: https://tailwindcss.com/docs/animation

Demonstrates how to define custom animations in the theme configuration using `--animate-*` CSS variables and `@keyframes`. This creates reusable animation utilities that can be applied throughout the project.

```css
@theme {
  --animate-wiggle: wiggle 1s ease-in-out infinite;
  @keyframes wiggle {
    0%,
    100% {
      transform: rotate(-3deg);
    }
    50% {
      transform: rotate(3deg);
    }
  }
}
```

--------------------------------

### Use Custom Themed Animation in Markup

Source: https://tailwindcss.com/docs/animation

Shows how to use a custom animation utility that was defined in the theme configuration. Once defined, custom animations can be used like any built-in animation utility.

```html
<div class="animate-wiggle">
  <!-- ... -->
</div>
```

--------------------------------

### Custom Animation with Arbitrary Values

Source: https://tailwindcss.com/docs/animation

Shows how to use the `animate-[<value>]` syntax to apply completely custom animation values directly in markup. This allows for one-off animations without requiring theme customization.

```html
<div class="animate-[wiggle_1s_ease-in-out_infinite] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Custom Animation with CSS Variables

Source: https://tailwindcss.com/docs/animation

Demonstrates using the `animate-(<custom-property>)` syntax to reference custom CSS variables for animations. This is shorthand for `animate-[var(<custom-property>)]` and automatically wraps the variable in the `var()` function.

```html
<div class="animate-(--my-animation) ...">
  <!-- ... -->
</div>
```

--------------------------------

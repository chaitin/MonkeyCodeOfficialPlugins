### transition-delay with motion-reduce variant

Source: https://tailwindcss.com/docs/transition-delay

HTML example showing how to use the motion-reduce variant to conditionally disable transition delays for users who prefer reduced motion. The motion-reduce:delay-0 class overrides the delay-300 utility when reduced motion is preferred.

```html
<button type="button" class="delay-300 motion-reduce:delay-0 ...">  <!-- ... --></button>
```

--------------------------------

### transition-delay with custom CSS property

Source: https://tailwindcss.com/docs/transition-delay

HTML example using the delay-(<custom-property>) syntax to reference a custom CSS property for the transition delay. This is shorthand for delay-[var(<custom-property>)] and automatically wraps the value with the var() function.

```html
<button class="delay-(--my-delay) ...">  <!-- ... --></button>
```

--------------------------------

### transition-delay with custom arbitrary value

Source: https://tailwindcss.com/docs/transition-delay

HTML markup demonstrating the delay-[<value>] syntax for setting completely custom transition delay values. Allows specifying arbitrary CSS values that don't match predefined utility classes.

```html
<button class="delay-[1s,250ms] ...">  <!-- ... --></button>
```

--------------------------------

### transition-delay with responsive breakpoint variant

Source: https://tailwindcss.com/docs/transition-delay

HTML markup showing how to use responsive variants with transition-delay utilities. The md: prefix applies delay-300 only at medium screen sizes and above, while delay-150 applies at all smaller breakpoints.

```html
<button class="delay-150 md:delay-300 ...">  <!-- ... --></button>
```

--------------------------------

### Basic transition-delay HTML markup with Tailwind classes

Source: https://tailwindcss.com/docs/transition-delay

HTML markup demonstrating basic usage of Tailwind's transition-delay utilities on button elements. Uses delay-150, delay-300, and delay-700 classes combined with transition, duration, and ease utilities to create staggered animation delays on hover.

```html
<button class="transition delay-150 duration-300 ease-in-out ...">Button A</button>
<button class="transition delay-300 duration-300 ease-in-out ...">Button B</button>
<button class="transition delay-700 duration-300 ease-in-out ...">Button C</button>
```

--------------------------------

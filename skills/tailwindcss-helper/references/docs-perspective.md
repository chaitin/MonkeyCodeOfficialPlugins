### Responsive Perspective Design with Breakpoint Variants

Source: https://tailwindcss.com/docs/perspective

Demonstrates how to apply different perspective utilities at different screen sizes using breakpoint prefixes like md:. This example applies perspective-midrange by default and switches to perspective-dramatic at medium screen sizes and above.

```html
<div class="perspective-midrange md:perspective-dramatic ...">
  <!-- ... -->
</div>
```

--------------------------------

### Basic Perspective Transform with Tailwind CSS

Source: https://tailwindcss.com/docs/perspective

Demonstrates how to use perspective utilities like perspective-dramatic and perspective-normal to control 3D depth. The example shows a container with six child elements rotated in 3D space to visualize the perspective effect. This creates a visual comparison of how different perspective values affect the appearance of 3D-transformed elements.

```html
<div class="size-20 perspective-dramatic ...">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div>
</div>
<div class="size-20 perspective-normal ...">
  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>
  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>
  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>
  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>
  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>
  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div>
</div>
```

--------------------------------

### Use Custom Perspective Theme Utility in Markup

Source: https://tailwindcss.com/docs/perspective

Demonstrates how to use a custom perspective utility class that was defined in the theme configuration. After adding --perspective-remote to the theme, the perspective-remote class becomes available for use on HTML elements.

```html
<div class="perspective-remote">
  <!-- ... -->
</div>
```

--------------------------------

### Custom Perspective with CSS Variables

Source: https://tailwindcss.com/docs/perspective

Shows how to use the perspective-(<custom-property>) syntax to reference custom CSS variables for perspective values. This is shorthand for perspective-[var(<custom-property>)] and automatically wraps the custom property in the var() function.

```html
<div class="perspective-(--my-perspective) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Custom Perspective Value with Arbitrary Values

Source: https://tailwindcss.com/docs/perspective

Demonstrates using the perspective-[<value>] syntax to apply custom perspective values not included in the predefined utility classes. This allows for precise control over the perspective distance by specifying any valid CSS value directly in the class name.

```html
<div class="perspective-[750px] ...">
  <!-- ... -->
</div>
```

--------------------------------

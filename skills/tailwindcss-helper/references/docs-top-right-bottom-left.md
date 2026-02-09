### Tailwind CSS `start` Utilities for Inline Start Placement

Source: https://tailwindcss.com/docs/top-right-bottom-left

These utilities control the `inset-inline-start` CSS property, setting the logical start position of an element within its inline direction. They offer options for numeric, fractional, pixel, full percentage, auto, custom property, and arbitrary values, including negative variants.

```css
/* start-<number> */
inset-inline-start: calc(var(--spacing) * <number>);
```

```css
/* -start-<number> */
inset-inline-start: calc(var(--spacing) * -<number>);
```

```css
/* start-<fraction> */
inset-inline-start: calc(<fraction> * 100%);
```

```css
/* -start-<fraction> */
inset-inline-start: calc(<fraction> * -100%);
```

```css
/* start-px */
inset-inline-start: 1px;
```

```css
/* -start-px */
inset-inline-start: -1px;
```

```css
/* start-full */
inset-inline-start: 100%;
```

```css
/* -start-full */
inset-inline-start: -100%;
```

```css
/* start-auto */
inset-inline-start: auto;
```

```css
/* start-(<custom-property>) */
inset-inline-start: var(<custom-property>);
```

```css
/* start-[<value>] */
inset-inline-start: <value>;
```

--------------------------------

### Apply Responsive Positioning with Breakpoint Variants in Tailwind CSS

Source: https://tailwindcss.com/docs/top-right-bottom-left

Shows how to use breakpoint prefixes like md: with positioning utilities to apply different position values at different screen sizes. Enables responsive design by conditionally applying positioning utilities at specific breakpoints.

```HTML
<div class="top-4 md:top-6 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Use Logical Properties for Directional Positioning in Tailwind CSS

Source: https://tailwindcss.com/docs/top-right-bottom-left

Demonstrates using start-<number> and end-<number> utilities for logical positioning that adapts to text direction. Automatically maps to left/right based on whether the document is left-to-right (LTR) or right-to-left (RTL).

```HTML
<div dir="ltr">
  <div class="relative size-32 ...">
    <div class="absolute start-0 top-0 size-14 ..."></div>
  </div>
  <div>
    <div dir="rtl">
      <div class="relative size-32 ...">
        <div class="absolute start-0 top-0 size-14 ..."></div>
      </div>
      <div></div>
    </div>
  </div>
</div>
```

--------------------------------

### Tailwind CSS `inset` Utilities for All Sides

Source: https://tailwindcss.com/docs/top-right-bottom-left

These utilities apply to the `inset` CSS property, which is a shorthand for `top`, `right`, `bottom`, and `left`. They support numeric, fractional, pixel, full percentage, auto, custom property, and arbitrary values, including negative variants.

```css
/* inset-<number> */
inset: calc(var(--spacing) * <number>);
```

```css
/* -inset-<number> */
inset: calc(var(--spacing) * -<number>);
```

```css
/* inset-<fraction> */
inset: calc(<fraction> * 100%);
```

```css
/* -inset-<fraction> */
inset: calc(<fraction> * -100%);
```

```css
/* inset-px */
inset: 1px;
```

```css
/* -inset-px */
inset: -1px;
```

```css
/* inset-full */
inset: 100%;
```

```css
/* -inset-full */
inset: -100%;
```

```css
/* inset-auto */
inset: auto;
```

```css
/* inset-(<custom-property>) */
inset: var(<custom-property>);
```

```css
/* inset-[<value>] */
inset: <value>;
```

--------------------------------

### Set Custom Position Values in Tailwind CSS

Source: https://tailwindcss.com/docs/top-right-bottom-left

Demonstrates using arbitrary value syntax with square brackets and CSS custom properties for positioning. Allows complete control over position values using inset-[<value>], top-[<value>], and inset-(<custom-property>) syntax.

```HTML
<div class="inset-[3px] ...">
  <!-- ... -->
</div>
```

```HTML
<div class="inset-(--my-position) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Position Elements with Top, Right, Bottom, Left Utilities in Tailwind CSS

Source: https://tailwindcss.com/docs/top-right-bottom-left

Demonstrates basic positioning using Tailwind CSS utilities to pin elements to corners, span edges, and fill parent containers. Uses absolute positioning with top-0, right-0, bottom-0, left-0, and inset utilities to achieve various layout patterns.

```HTML
<!-- Pin to top left corner -->
<div class="relative size-32 ...">
  <div class="absolute top-0 left-0 size-16 ...">01</div>
</div>
<!-- Span top edge -->
<div class="relative size-32 ...">
  <div class="absolute inset-x-0 top-0 h-16 ...">02</div>
</div>
<!-- Pin to top right corner -->
<div class="relative size-32 ...">
  <div class="absolute top-0 right-0 size-16 ...">03</div>
</div>
<!-- Span left edge -->
<div class="relative size-32 ...">
  <div class="absolute inset-y-0 left-0 w-16 ...">04</div>
</div>
<!-- Fill entire parent -->
<div class="relative size-32 ...">
  <div class="absolute inset-0 ...">05</div>
</div>
<!-- Span right edge -->
<div class="relative size-32 ...">
  <div class="absolute inset-y-0 right-0 w-16 ...">06</div>
</div>
<!-- Pin to bottom left corner -->
<div class="relative size-32 ...">
  <div class="absolute bottom-0 left-0 size-16 ...">07</div>
</div>
<!-- Span bottom edge -->
<div class="relative size-32 ...">
  <div class="absolute inset-x-0 bottom-0 h-16 ...">08</div>
</div>
<!-- Pin to bottom right corner -->
<div class="relative size-32 ...">
  <div class="absolute right-0 bottom-0 size-16 ...">09</div>
</div>
```

--------------------------------

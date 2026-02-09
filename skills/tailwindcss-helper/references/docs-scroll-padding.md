### Using logical scroll-padding properties in HTML

Source: https://tailwindcss.com/docs/scroll-padding

Shows how to use scroll-ps and scroll-pe utilities with logical properties that adapt to text direction. The example demonstrates the same utility class applied to both left-to-right and right-to-left text directions.

```html
<div dir="ltr">
  <div class="snap-x scroll-ps-6 ...">
    <!-- ... -->
  </div>
</div>
<div dir="rtl">
  <div class="snap-x scroll-ps-6 ...">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Basic scroll-padding with directional utilities in HTML

Source: https://tailwindcss.com/docs/scroll-padding

Demonstrates using scroll-pt, scroll-pr, scroll-pb, and scroll-pl utilities to set scroll offset on a snap container. The example shows a horizontally scrollable grid of images with left padding applied using the scroll-pl-6 class.

```html
<div class="snap-x scroll-pl-6 ...">
  <div class="snap-start ...">
    <img src="/img/vacation-01.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-02.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-03.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-04.jpg" />
  </div>
  <div class="snap-start ...">
    <img src="/img/vacation-05.jpg" />
  </div>
</div>
```

--------------------------------

### Apply scroll-padding with responsive breakpoint variant in Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-padding

Use breakpoint variants to apply scroll-padding utilities at specific screen sizes. The example shows applying `scroll-p-8` at default sizes and `scroll-p-0` at medium screens and above using the `md:` variant. This allows responsive adjustment of scroll padding behavior across different device sizes.

```html
<div class="scroll-p-8 md:scroll-p-0 ...">  <!-- ... --></div>
```

--------------------------------

### Custom scroll-padding values in HTML

Source: https://tailwindcss.com/docs/scroll-padding

Shows two methods for applying custom scroll padding values: using arbitrary values with square bracket syntax and using CSS custom properties with parentheses syntax. Both approaches allow complete flexibility beyond predefined spacing scales.

```html
<div class="scroll-pl-[24rem] ...">
  <!-- ... -->
</div>

<div class="scroll-pl-(--my-scroll-padding) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Negative scroll-padding values in HTML

Source: https://tailwindcss.com/docs/scroll-padding

Demonstrates how to apply negative scroll padding by prefixing the class name with a dash. This converts the utility value to a negative number for reverse scroll offset effects.

```html
<div class="-scroll-ps-6 snap-x ...">
  <!-- ... -->
</div>
```

--------------------------------

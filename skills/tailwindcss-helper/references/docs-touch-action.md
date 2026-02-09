### Responsive touch-action with Breakpoint Variants HTML

Source: https://tailwindcss.com/docs/touch-action

Shows how to use responsive design patterns with touch-action utilities by combining breakpoint prefixes. This example applies touch-pan-x at mobile sizes and switches to touch-auto at medium screen sizes and above using the md: breakpoint variant.

```html
<div class="touch-pan-x md:touch-auto ...">
  <!-- ... -->
</div>
```

--------------------------------

### Basic touch-action Utilities HTML

Source: https://tailwindcss.com/docs/touch-action

Demonstrates how to apply touch-action utilities to control scrolling and zooming behavior on touchscreen devices. The example shows four different containers with varying touch behaviors: auto (default), none (disabled), pan-x (horizontal panning), and pan-y (vertical panning). Each container includes an oversized image to demonstrate the touch interaction differences.

```html
<div class="h-48 w-full touch-auto overflow-auto ...">
  <img class="h-auto w-[150%] max-w-none" src="..." />
</div>
<div class="h-48 w-full touch-none overflow-auto ...">
  <img class="h-auto w-[150%] max-w-none" src="..." />
</div>
<div class="h-48 w-full touch-pan-x overflow-auto ...">
  <img class="h-auto w-[150%] max-w-none" src="..." />
</div>
<div class="h-48 w-full touch-pan-y overflow-auto ...">
  <img class="h-auto w-[150%] max-w-none" src="..." />
</div>
```

--------------------------------

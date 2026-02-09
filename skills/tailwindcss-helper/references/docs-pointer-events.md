### Controlling pointer events for elements in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/pointer-events

This example demonstrates how to use Tailwind CSS `pointer-events-auto` and `pointer-events-none` utilities. The `pointer-events-none` class makes an element ignore pointer events like clicks and hovers, while `pointer-events-auto` restores the default browser behavior. This is shown with two search input setups, one where the overlay icon is interactive and another where it is not.

```html
<div class="relative ...">  <div class="pointer-events-auto absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div><div class="relative ...">  <div class="pointer-events-none absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div>
```

--------------------------------

### Conditionally restoring pointer events in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/pointer-events

This example illustrates how to use Tailwind CSS responsive utilities to conditionally restore pointer events. An element is initially set to `pointer-events-none`, but `md:pointer-events-auto` overrides this behavior on medium screens and above, allowing interaction based on viewport size.

```html
<div class="pointer-events-none md:pointer-events-auto ...">  <!-- ... --></div>
```

--------------------------------

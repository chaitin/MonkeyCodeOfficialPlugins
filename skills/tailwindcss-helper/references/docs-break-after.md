### break-after Basic Example with Columns

Source: https://tailwindcss.com/docs/break-after

Demonstrates using break-after-column utility to control column breaks in a multi-column layout. The break-after-column class forces a column break after the specified paragraph element within a two-column container.

```html
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-after-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

--------------------------------

### break-after Responsive Design with Breakpoint Variant

Source: https://tailwindcss.com/docs/break-after

Shows how to apply break-after utilities responsively using breakpoint prefixes. The md: prefix applies break-after-auto only at medium screen sizes and above, while break-after-column applies at all screen sizes.

```html
<div class="break-after-column md:break-after-auto ...">
  <!-- ... -->
</div>
```

--------------------------------

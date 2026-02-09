### Responsive transition-behavior with Breakpoint Variant

Source: https://tailwindcss.com/docs/transition-behavior

Shows how to apply transition-behavior utilities responsively using breakpoint prefixes. The example uses md: prefix to apply transition-normal at medium screen sizes and above, while using transition-discrete at smaller breakpoints.

```html
<button class="transition-discrete md:transition-normal ...">
  <!-- ... -->
</button>
```

--------------------------------

### Basic transition-behavior HTML Example

Source: https://tailwindcss.com/docs/transition-behavior

Demonstrates the use of transition-discrete utility to create fade-out transitions on elements that change from hidden to visible states. Uses Tailwind CSS classes with peer selectors and checkbox interactions to control visibility and opacity transitions.

```html
<label class="peer ...">
  <input type="checkbox" checked />
</label>
<button class="hidden transition-all not-peer-has-checked:opacity-0 peer-has-checked:block ...">
  I hide
</button>
<label class="peer ...">
  <input type="checkbox" checked />
</label>
<button class="hidden transition-all transition-discrete not-peer-has-checked:opacity-0 peer-has-checked:block ...">
  I fade out
</button>
```

--------------------------------

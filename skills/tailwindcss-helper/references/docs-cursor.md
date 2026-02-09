### Apply Responsive Cursor Styles with Tailwind CSS

Source: https://tailwindcss.com/docs/cursor

Explains how to make cursor styles responsive using Tailwind CSS breakpoint variants. By prefixing a `cursor` utility with a breakpoint like `md:`, the cursor style will only apply at that screen size and above, enabling adaptive UI behavior.

```html
<button class="cursor-not-allowed md:cursor-auto ...">  <!-- ... --></button>
```

--------------------------------

### Apply Basic Cursor Styles with Tailwind CSS

Source: https://tailwindcss.com/docs/cursor

Demonstrates how to apply standard cursor styles like `cursor-pointer`, `cursor-progress`, and `cursor-not-allowed` to HTML button elements using Tailwind CSS utility classes. These classes control the visual feedback when a user hovers over an element.

```html
<button class="cursor-pointer ...">Submit</button><button class="cursor-progress ...">Saving...</button><button class="cursor-not-allowed ..." disabled>Confirm</button>
```

--------------------------------

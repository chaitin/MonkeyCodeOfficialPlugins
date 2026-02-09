### Applying Responsive Flex Grow Utilities with Tailwind CSS Breakpoints

Source: https://tailwindcss.com/docs/flex-grow

This example illustrates how to use responsive design with Tailwind CSS `flex-grow` utilities by prefixing them with breakpoint variants like `md:`. This allows applying different grow behaviors based on screen sizes, such as `grow` by default and `grow-0` on medium screens and above.

```html
<div class="grow md:grow-0 ...">  <!-- ... --></div>
```

--------------------------------

### Setting Custom Flex Grow Values with Tailwind CSS `grow-[<value>]` Syntax

Source: https://tailwindcss.com/docs/flex-grow

This example shows how to use the arbitrary value syntax `grow-[<value>]` in Tailwind CSS to apply a completely custom flex grow factor. This allows for precise control over an item's growth behavior using any valid CSS value.

```html
<div class="grow-[25vw] ...">  <!-- ... --></div>
```

--------------------------------

### Allowing Flex Items to Grow with Tailwind CSS `grow` Utility

Source: https://tailwindcss.com/docs/flex-grow

This example demonstrates how to use the `grow` utility in Tailwind CSS to make a flex item expand and fill any available space within its flex container. It shows a basic flex layout where one item is allowed to grow while others maintain their fixed size.

```html
<div class="flex ...">  <div class="size-14 flex-none ...">01</div>  <div class="size-14 grow ...">02</div>  <div class="size-14 flex-none ...">03</div></div>
```

--------------------------------

### Proportionally Growing Flex Items with Tailwind CSS `grow-<number>` Utilities

Source: https://tailwindcss.com/docs/flex-grow

This example illustrates the use of `grow-<number>` utilities, such as `grow-3` and `grow-7`, to make flex items grow proportionally based on a specified growth factor. This allows items to distribute available space relative to each other within a flex container.

```html
<div class="flex ...">  <div class="size-14 grow-3 ...">01</div>  <div class="size-14 grow-7 ...">02</div>  <div class="size-14 grow-3 ...">03</div></div>
```

--------------------------------

### Applying CSS Variables for Flex Grow with Tailwind CSS `grow-(<custom-property>)`

Source: https://tailwindcss.com/docs/flex-grow

This example demonstrates the `grow-(<custom-property>)` syntax in Tailwind CSS, which is a shorthand for `grow-[var(<custom-property>)]`. It allows applying a custom flex grow factor defined by a CSS variable, enhancing reusability and dynamic styling.

```html
<div class="grow-(--my-grow) ...">  <!-- ... --></div>
```

--------------------------------

### Preventing Flex Items from Growing with Tailwind CSS `grow-0` Utility

Source: https://tailwindcss.com/docs/flex-grow

This example demonstrates how to use the `grow-0` utility in Tailwind CSS to explicitly prevent a flex item from growing, even when other items are allowed to expand. It ensures that the specified item maintains its initial size.

```html
<div class="flex ...">  <div class="size-14 grow ...">01</div>  <div class="size-14 grow-0 ...">02</div>  <div class="size-14 grow ...">03</div></div>
```

--------------------------------

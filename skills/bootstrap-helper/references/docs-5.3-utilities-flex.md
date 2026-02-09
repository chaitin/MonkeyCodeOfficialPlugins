### Control Flex Item Growth with flex-grow Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Shows how to use `.flex-grow-*` utilities to allow flex items to expand and fill available space. The example demonstrates an item taking up all possible space while others maintain their required dimensions. Responsive variations are supported.

```html
<div class="d-flex">
  <div class="p-2 flex-grow-1">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Third flex item</div>
</div>
```

--------------------------------

### Control Flex Item Shrinking with flex-shrink Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Illustrates the use of `.flex-shrink-*` utilities to enable flex items to reduce their size when necessary. The example shows an item shrinking to wrap its content, making space for another item with a fixed width. Responsive variations are available.

```html
<div class="d-flex">
  <div class="p-2 w-100">Flex item</div>
  <div class="p-2 flex-shrink-1">Flex item</div>
</div>
```

--------------------------------

### Align Flex Items with align-self Utilities (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Demonstrates how to use `align-self` utilities to individually align flex items along the cross axis. Available options include start, end, center, baseline, and stretch. Responsive variations are also supported.

```html
<div class="align-self-start">Aligned flex item</div>
<div class="align-self-end">Aligned flex item</div>
<div class="align-self-center">Aligned flex item</div>
<div class="align-self-baseline">Aligned flex item</div>
<div class="align-self-stretch">Aligned flex item</div>
```

--------------------------------

### Control Flex Item Spacing with Auto Margins (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Demonstrates how auto margins can be used with flexbox to control item positioning. Examples include default spacing, pushing items to the right using `.me-auto`, and pushing items to the left using `.ms-auto`. Responsive variations are not explicitly shown but implied by Bootstrap's utility system.

```html
<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="me-auto p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="ms-auto p-2">Flex item</div>
</div>
```

--------------------------------

### Align Items with Bootstrap Flexbox Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/flex

These utilities control the alignment of flex items along the cross axis of a flex container. They are used in conjunction with `.d-flex` and support alignment options such as start, end, center, baseline, and stretch. Responsive variants are also provided for different breakpoints.

```html
<div class="d-flex align-items-start">...</div>
<div class="d-flex align-items-end">...</div>
<div class="d-flex align-items-center">...</div>
<div class="d-flex align-items-baseline">...</div>
<div class="d-flex align-items-stretch">...</div>
```

--------------------------------

### Justify Content with Bootstrap Flexbox Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/flex

These utilities allow you to control the alignment of flex items along the main axis of a flex container. They can be applied to elements with the `.d-flex` class and accept values like start, end, center, between, around, and evenly. Responsive variations are available for different screen sizes.

```html
<div class="d-flex justify-content-start">...</div>
<div class="d-flex justify-content-end">...</div>
<div class="d-flex justify-content-center">...</div>
<div class="d-flex justify-content-between">...</div>
<div class="d-flex justify-content-around">...</div>
<div class="d-flex justify-content-evenly">...</div>
```

--------------------------------

### Bootstrap Media Object Component

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Shows how to recreate the media object component using Bootstrap's flex utilities. This allows for flexible and customizable layouts where an image or other media is placed next to textual content.

```html
<div class="d-flex">
  <div class="flex-shrink-0">
    <img src="..." alt="...">
  </div>
  <div class="flex-grow-1 ms-3">
    This is some content from a media component. You can replace this with any content and adjust it as needed.
  </div>
</div>
```

```html
<div class="d-flex align-items-center">
  <div class="flex-shrink-0">
    <img src="..." alt="...">
  </div>
  <div class="flex-grow-1 ms-3">
    This is some content from a media component. You can replace this with any content and adjust it as needed.
  </div>
</div>
```

--------------------------------

### Enable Flexbox Container (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Demonstrates how to create a flexbox container using Bootstrap's `d-flex` class. This transforms direct children into flex items, allowing for easier layout management. The `p-2` class adds padding for visual spacing.

```html
<div class="d-flex p-2">I'm a flexbox container!</div>
```

--------------------------------

### Flex Item Wrapping with flex-wrap Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Illustrates how to control the wrapping behavior of flex items within a flex container. The `.flex-nowrap` class prevents wrapping, `.flex-wrap` enables wrapping to the next line, and `.flex-wrap-reverse` wraps items in the opposite direction. Responsive variations are available for different screen sizes.

```html
<div class="d-flex flex-nowrap">
  ...
</div>

<div class="d-flex flex-wrap">
  ...
</div>

<div class="d-flex flex-wrap-reverse">
  ...
</div>
```

--------------------------------

### Enable Inline Flexbox Container (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/flex

Shows how to create an inline flexbox container using Bootstrap's `d-inline-flex` class. This allows the container to flow with text while its children are treated as flex items. Padding is applied with `p-2`.

```html
<div class="d-inline-flex p-2">I'm an inline flexbox container!</div>
```

--------------------------------

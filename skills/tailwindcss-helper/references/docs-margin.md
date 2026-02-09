### Responsive Margin Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example showing responsive margin utilities with breakpoint variants (md:) to apply different margin values at specific screen sizes.

```html
<div class="mt-4 md:mt-8 ...">
  <!-- ... -->
</div>
```

--------------------------------

### Logical Properties Margin Utilities HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating logical margin properties (ms-, me-) for margin-inline-start and margin-inline-end with bidirectional support (LTR and RTL).

```html
<div>
  <div dir="ltr">
    <div class="ms-8 ...">ms-8</div>
    <div class="me-8 ...">me-8</div>
  </div>
  <div dir="rtl">
    <div class="ms-8 ...">ms-8</div>
    <div class="me-8 ...">me-8</div>
  </div>
</div>
```

--------------------------------

### Space Reverse Direction Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating space-x-reverse utility combined with flex-row-reverse to apply spacing to the correct side of reversed child elements.

```html
<div class="flex flex-row-reverse space-x-4 space-x-reverse ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

--------------------------------

### Custom CSS Property Margin HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating margin utilities with custom CSS properties using m-(<custom-property>) syntax for dynamic spacing values.

```html
<div class="m-(--my-margin) ...">
  <!-- ... -->
</div>
```

--------------------------------

### Basic Margin Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating basic margin utility usage with m-8 class to apply equal margin on all sides of an element.

```html
<div class="m-8 ...">m-8</div>
```

--------------------------------

### Vertical Margin Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating vertical margin utility (my-) for controlling top and bottom margins of an element.

```html
<div class="my-8 ...">my-8</div>
```

--------------------------------

### Horizontal Margin Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example demonstrating horizontal margin utility (mx-) for controlling left and right margins of an element.

```html
<div class="mx-8 ...">mx-8</div>
```

--------------------------------

### Custom Margin Value HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example showing custom margin values using bracket notation (m-[<value>]) to set arbitrary margin values not in the default scale.

```html
<div class="m-[5px] ...">
  <!-- ... -->
</div>
```

--------------------------------

### Space Between Children Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example showing space-x utility for adding consistent horizontal spacing between flex child elements.

```html
<div class="flex space-x-4 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

--------------------------------

### Directional Margin Utilities HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example showing directional margin utilities (mt-, mr-, mb-, ml-) applied to individual elements for controlling margin on specific sides.

```html
<div class="mt-6 ...">mt-6</div>
<div class="mr-4 ...">mr-4</div>
<div class="mb-8 ...">mb-8</div>
<div class="ml-2 ...">ml-2</div>
```

--------------------------------

### Negative Margin Utility HTML Example

Source: https://tailwindcss.com/docs/margin

HTML example showing negative margin usage with -mt-8 class to apply negative top margin, useful for overlapping elements.

```html
<div class="h-16 w-36 bg-sky-400 opacity-20 ..."></div>
<div class="-mt-8 bg-sky-300 ...">-mt-8</div>
```

--------------------------------

### Space Y Arbitrary Value Margin CSS Implementation

Source: https://tailwindcss.com/docs/margin

CSS implementation for vertical spacing with arbitrary custom values. Supports any CSS value through bracket notation with directional control.

```css
& > :not(:last-child) {
  --tw-space-y-reverse: 0;
  margin-block-start: calc(<value> * var(--tw-space-y-reverse));
  margin-block-end: calc(<value> * calc(1 - var(--tw-space-y-reverse)));
}
```

--------------------------------

### Space X Reverse Direction CSS Implementation

Source: https://tailwindcss.com/docs/margin

CSS implementation for reversing horizontal spacing direction. Sets --tw-space-x-reverse to 1 to flip spacing to the opposite side of child elements.

```css
& > :not(:last-child) {
  --tw-space-x-reverse: 1;
}
```

--------------------------------

### Space Y Custom Property Margin CSS Implementation

Source: https://tailwindcss.com/docs/margin

CSS implementation for vertical spacing using custom CSS properties. Allows dynamic spacing values through CSS variables with calc() for directional computation.

```css
& > :not(:last-child) {
  --tw-space-y-reverse: 0;
  margin-block-start: calc(var(<custom-property>) * var(--tw-space-y-reverse));
  margin-block-end: calc(var(<custom-property>) * calc(1 - var(--tw-space-y-reverse)));
}
```

--------------------------------

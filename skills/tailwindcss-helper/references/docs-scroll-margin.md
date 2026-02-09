### Apply Responsive Scroll Margin with Breakpoint Variants

Source: https://tailwindcss.com/docs/scroll-margin

Prefix scroll-margin utilities with breakpoint variants like `md:` to apply different scroll margin values at specific screen sizes. In this example, the element has `scroll-m-8` on mobile and `scroll-m-0` at medium breakpoint and above.

```html
<div class="scroll-m-8 md:scroll-m-0 ...">  <!-- ... --></div>
```

--------------------------------

### Apply Basic Scroll Margin in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-margin

This example demonstrates how to apply basic scroll margin utilities like `scroll-ml-6` and `scroll-mt-6` to elements within a snap container in HTML. These classes control the offset around snapped items, ensuring proper spacing when scrolling.

```html
<div class="snap-x ...">
  <div class="snap-start scroll-ml-6 ...">
    <img src="/img/vacation-01.jpg"/>
  </div>
  <div class="snap-start scroll-ml-6 ...">
    <img src="/img/vacation-02.jpg"/>
  </div>
  <div class="snap-start scroll-ml-6 ...">
    <img src="/img/vacation-03.jpg"/>
  </div>
  <div class="snap-start scroll-ml-6 ...">
    <img src="/img/vacation-04.jpg"/>
  </div>
  <div class="snap-start scroll-ml-6 ...">
    <img src="/img/vacation-05.jpg"/>
  </div>
</div>
```

--------------------------------

### Apply Logical Scroll Margin Properties in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-margin

This example illustrates the use of logical scroll margin properties like `scroll-ms-6` and `scroll-me-6` in HTML. These utilities set `scroll-margin-inline-start` and `scroll-margin-inline-end`, which adapt to the text direction (LTR/RTL) for flexible and internationalized layout control.

```html
<div dir="ltr">
  <div class="snap-x ...">
    <div class="snap-start scroll-ms-6 ...">
      <img src="/img/vacation-01.jpg"/>
    </div>
    <!-- ... -->
  </div>
</div><div dir="rtl">
  <div class="snap-x ...">
    <div class="snap-start scroll-ms-6 ...">
      <img src="/img/vacation-01.jpg"/>
    </div>
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Apply Negative Scroll Margin in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-margin

This example shows how to use negative scroll margin values in HTML by prefixing Tailwind CSS utility classes, such as `-scroll-ml-6`, with a dash. This allows for a negative offset around snapped items, pulling them closer to the snap position.

```html
<div class="snap-start -scroll-ml-6 ...">
  <!-- ... --></div>
```

--------------------------------

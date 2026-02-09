### Bootstrap Column Wrapping Example

Source: https://getbootstrap.com/docs/5.3/layout/columns

Demonstrates how columns automatically wrap to a new line when their total width exceeds 12 units within a single row. This behavior ensures that content remains organized even with more than 12 columns.

```html
<div class="container">
  <div class="row">
    <div class="col-9">.col-9</div>
    <div class="col-4">.col-4<br>Since 9 + 4 = 13 &gt; 12, this 4-column-wide div gets wrapped onto a new line as one contiguous unit.</div>
    <div class="col-6">.col-6<br>Subsequent columns continue along the new line.</div>
  </div>
</div>
```

--------------------------------

### Customizing Bootstrap Order Utilities with Sass

Source: https://getbootstrap.com/docs/5.3/layout/columns

Provides an example of how to extend Bootstrap's utility API by modifying the `$utilities` Sass map to add custom `.order-*` classes. This allows for greater control over ordering options beyond the default set.

```scss
$utilities: map-merge(
  $utilities,
  (
    "order": map-merge(
      map-get($utilities, "order"),
      (
        values: map-merge(
          map-get(map-get($utilities, "order"), "values"),
          (
            6: 6, // Add a new `.order-{breakpoint}-6` utility
            last: 7 // Change the `.order-{breakpoint}-last` utility to use the next number
          )
        ),
      ),
    ),
  )
);
```

--------------------------------

### Bootstrap Responsive Column Break with d-none d-md-block

Source: https://getbootstrap.com/docs/5.3/layout/columns

Shows how to create responsive column breaks using a combination of `w-100` and display utilities (`d-none`, `d-md-block`). This allows columns to wrap only at specific breakpoints, enhancing layout adaptability.

```html
<div class="container text-center">
  <div class="row">
    <div class="col-6 col-sm-4">.col-6 .col-sm-4</div>
    <div class="col-6 col-sm-4">.col-6 .col-sm-4</div>

    <!-- Force next columns to break to new line at md breakpoint and up -->
    <div class="w-100 d-none d-md-block"></div>

    <div class="col-6 col-sm-4">.col-6 .col-sm-4</div>
    <div class="col-6 col-sm-4">.col-6 .col-sm-4</div>
  </div>
</div>
```

--------------------------------

### Bootstrap Order Classes for Visual Reordering

Source: https://getbootstrap.com/docs/5.3/layout/columns

Demonstrates the use of Bootstrap's responsive `.order-*` classes to control the visual order of elements within a grid row. This allows for flexible content arrangement independent of the DOM order.

```html
<div class="container text-center">
  <div class="row">
    <div class="col">
      First in DOM, no order applied
    </div>
    <div class="col order-5">
      Second in DOM, with a larger order
    </div>
    <div class="col order-1">
      Third in DOM, with an order of 1
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Margin Utilities for Spacing

Source: https://getbootstrap.com/docs/5.3/layout/columns

Leverage margin utilities like `.ms-auto` and `.me-auto` to manage spacing between flex items, including columns. These utilities are particularly useful for pushing content to the edges or creating space within rows. They work across different breakpoints.

```html
<div class="container text-center">
  <div class="row">
    <div class="col-md-4">.col-md-4</div>
    <div class="col-md-4 ms-auto">.col-md-4 .ms-auto</div>
  </div>
  <div class="row">
    <div class="col-md-3 ms-md-auto">.col-md-3 .ms-md-auto</div>
    <div class="col-md-3 ms-md-auto">.col-md-3 .ms-md-auto</div>
  </div>
  <div class="row">
    <div class="col-auto me-auto">.col-auto .me-auto</div>
    <div class="col-auto">.col-auto</div>
  </div>
</div>
```

--------------------------------

### Bootstrap Order-First and Order-Last Classes

Source: https://getbootstrap.com/docs/5.3/layout/columns

Illustrates the usage of `.order-first` and `.order-last` utility classes for setting an element's order to the lowest (`-1`) or highest (`6`) respectively. These classes provide convenient ways to position elements at the beginning or end of a flex container.

```html
<div class="container text-center">
  <div class="row">
    <div class="col order-last">
      First in DOM, ordered last
    </div>
    <div class="col">
      Second in DOM, unordered
    </div>
    <div class="col order-first">
      Third in DOM, ordered first
    </div>
  </div>
</div>
```

--------------------------------

### Bootstrap Responsive Floated Images with Clearfix

Source: https://getbootstrap.com/docs/5.3/layout/columns

Create responsive floated images within Bootstrap layouts by combining column classes, float utilities, and margin utilities. Use the `.clearfix` wrapper to ensure proper content flow around the floated element, especially when text content is shorter than the image.

```html
<div class="clearfix">
  <img src="..." class="col-md-6 float-md-end mb-3 ms-md-3" alt="...">

  <p>
    A paragraph of placeholder text. We’re using it here to show the use of the clearfix class. We’re adding quite a few meaningless phrases here to demonstrate how the columns interact here with the floated image.
  </p>

  <p>
    As you can see the paragraphs gracefully wrap around the floated image. Now imagine how this would look with some actual content in here, rather than just this boring placeholder text that goes on and on, but actually conveys no tangible information at. It simply takes up space and should not really be read.
  </p>

  <p>
    And yet, here you are, still persevering in reading this placeholder text, hoping for some more insights, or some hidden easter egg of content. A joke, perhaps. Unfortunately, there’s none of that here.
  </p>
</div>
```

--------------------------------

### Bootstrap Stack Example: Inline Form

Source: https://getbootstrap.com/docs/5.3/helpers/stacks

Illustrates creating an inline form layout using `.hstack`. This example combines input fields and buttons, using `.me-auto` on the input for spacing and a vertical rule (`.vr`) to separate action buttons.

```html
<div class="hstack gap-3">
  <input class="form-control me-auto" type="text" placeholder="Add your item here..." aria-label="Add your item here...">
  <button type="button" class="btn btn-secondary">Submit</button>
  <div class="vr"></div>
  <button type="button" class="btn btn-outline-danger">Reset</button>
</div>
```

--------------------------------

### Bootstrap Stack Example: Vertical Buttons

Source: https://getbootstrap.com/docs/5.3/helpers/stacks

Provides an example of using `.vstack` to arrange buttons vertically. This snippet also incorporates column utilities (`col-md-5`) and margin auto (`mx-auto`) for centering and controlling the width of the button group.

```html
<div class="vstack gap-2 col-md-5 mx-auto">
  <button type="button" class="btn btn-secondary">Save changes</button>
  <button type="button" class="btn btn-outline-secondary">Cancel</button>
</div>
```

--------------------------------

### Bootstrap Vertical Stack (.vstack) Example

Source: https://getbootstrap.com/docs/5.3/helpers/stacks

Demonstrates how to use the `.vstack` class to create a vertical layout. Items within the stack take up full width by default. The `.gap-*` utility class is used to add space between stacked items.

```html
<div class="vstack gap-3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</div>
```

--------------------------------

### Bootstrap Horizontal Stack (.hstack) Example

Source: https://getbootstrap.com/docs/5.3/helpers/stacks

Illustrates the use of the `.hstack` class for creating horizontal layouts. Stacked items are vertically centered and only take up necessary width. Spacing is managed using `.gap-*` utilities.

```html
<div class="hstack gap-3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</div>
```

--------------------------------

### Bootstrap Horizontal Stack with Margin Spacer

Source: https://getbootstrap.com/docs/5.3/helpers/stacks

Shows how to use horizontal margin utilities like `.ms-auto` within an `.hstack` to create dynamic spacing and push elements apart. This is useful for aligning items to opposite sides of the container.

```html
<div class="hstack gap-3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="p-2">Third item</div>
</div>
```

--------------------------------

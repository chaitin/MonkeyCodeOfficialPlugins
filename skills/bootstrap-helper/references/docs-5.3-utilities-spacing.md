### HTML Example: Using column-gap Utility

Source: https://getbootstrap.com/docs/5.3/utilities/spacing

This HTML snippet demonstrates how to apply the 'column-gap' utility class to a grid container to control the horizontal space between its direct children. It utilizes Bootstrap's grid system and spacing utilities.

```html
<div style="grid-template-columns: 1fr 1fr;" class="d-grid gap-0 column-gap-3">
  <div class="p-2">Grid item 1</div>
  <div class="p-2">Grid item 2</div>
  <div class="p-2">Grid item 3</div>
  <div class="p-2">Grid item 4</div>
</div>
```

--------------------------------

### Row Gap Utility for Grid Layout (HTML)

Source: https://getbootstrap.com/docs/5.3/utilities/spacing

This HTML example illustrates the use of Bootstrap's `.row-gap-3` utility for controlling vertical spacing between grid items. Combined with `.d-grid` and `.gap-0`, it specifically targets the row gap while maintaining zero column gap.

```html
<div style="grid-template-columns: 1fr 1fr;" class="d-grid gap-0 row-gap-3">
  <div class="p-2">Grid item 1</div>
  <div class="p-2">Grid item 2</div>
  <div class="p-2">Grid item 3</div>
  <div class="p-2">Grid item 4</div>
</div>
```

--------------------------------

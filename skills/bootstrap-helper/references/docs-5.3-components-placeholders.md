### Bootstrap Placeholder Example: Card Component

Source: https://getbootstrap.com/docs/5.3/components/placeholders

Demonstrates how to use Bootstrap's placeholder classes to create a loading state for a card component. This example shows a standard card and its placeholder equivalent, maintaining similar dimensions.

```html
<div class="card">
  <img src="..." class="card-img-top" alt="...">

  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<div class="card" aria-hidden="true">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title placeholder-glow">
      <span class="placeholder col-6"></span>
    </h5>
    <p class="card-text placeholder-glow">
      <span class="placeholder col-7"></span>
      <span class="placeholder col-4"></span>
      <span class="placeholder col-4"></span>
      <span class="placeholder col-6"></span>
      <span class="placeholder col-8"></span>
    </p>
    <a class="btn btn-primary disabled placeholder col-6" aria-disabled="true"></a>
  </div>
</div>
```

--------------------------------

### Bootstrap Placeholder Usage: Basic and Button

Source: https://getbootstrap.com/docs/5.3/components/placeholders

Illustrates the fundamental usage of Bootstrap placeholders, showing how to create a placeholder element with a specified width and how to apply placeholder styles to a disabled button.

```html
<p aria-hidden="true">
  <span class="placeholder col-6"></span>
</p>

<a class="btn btn-primary disabled placeholder col-4" aria-disabled="true"></a>
```

--------------------------------

### Bootstrap Placeholder Animations

Source: https://getbootstrap.com/docs/5.3/components/placeholders

Demonstrates how to add visual animations to Bootstrap placeholders to enhance the perception of active loading. This is achieved using the `.placeholder-glow` or `.placeholder-wave` classes.

```html
<p class="placeholder-glow">
  <span class="placeholder col-12"></span>
</p>

<p class="placeholder-wave">
  <span class="placeholder col-12"></span>
</p>
```

--------------------------------

### Bootstrap Placeholder Width Customization

Source: https://getbootstrap.com/docs/5.3/components/placeholders

Demonstrates various methods for customizing the width of Bootstrap placeholders. This includes using grid column classes, width utility classes, and inline styles.

```html
<span class="placeholder col-6"></span>
<span class="placeholder w-75"></span>
<span class="placeholder" style="width: 25%;"></span>
```

--------------------------------

### Integrate Masonry with Bootstrap Grid and Cards

Source: https://getbootstrap.com/docs/5.3/examples/masonry

This example demonstrates how to combine Bootstrap's responsive grid system with Masonry for dynamic card layouts. By adding the `data-masonry` attribute to a Bootstrap `.row` element, Masonry will automatically initialize and manage the positioning of its child elements, typically Bootstrap cards.

```html
<div class="row" data-masonry='{"percentPosition": true }'>
  <div class="col-md-4">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title that wraps to a new line</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">Last updated 3 mins ago</small>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">Last updated 3 mins ago</small>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This card has a regular title and short paragraph of text below it.</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">Last updated 3 mins ago</small>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is another card with title and supporting text below. This card has some additional content to make it slightly taller overall.</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">Last updated 3 mins ago</small>
      </div>
    </div>
  </div>
</div>
```

--------------------------------

### Include Masonry JavaScript Plugin via CDN

Source: https://getbootstrap.com/docs/5.3/examples/masonry

This snippet shows how to include the Masonry JavaScript plugin using a CDN. It's essential for enabling Masonry's layout capabilities. Ensure this script is loaded before your custom JavaScript that initializes Masonry.

```html
<script src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D" crossorigin="anonymous" async></script>
```

--------------------------------

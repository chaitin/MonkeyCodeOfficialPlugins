### Card with Stretched Links (Positioning Issues) - Bootstrap HTML

Source: https://getbootstrap.com/docs/5.3/helpers/stretched-link

Demonstrates scenarios where `.stretched-link` might not work as expected due to CSS `position` or `transform` properties applied to the link or its ancestors. This example shows a link that won't stretch due to `position: relative` on the link itself, and another stretched over only a `p`-tag due to a transform.

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card with stretched links</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
    <p class="card-text">
      <a href="#" class="stretched-link text-danger" style="position: relative;">Stretched link will not work here, because <code>position: relative</code> is added to the link</a>
    </p>
    <p class="card-text bg-body-tertiary" style="transform: rotate(0);">
      This <a href="#" class="text-warning stretched-link">stretched link</a> will only be spread over the <code>p</code>-tag, because a transform is applied to it.
    </p>
  </div>
</div>
```

--------------------------------

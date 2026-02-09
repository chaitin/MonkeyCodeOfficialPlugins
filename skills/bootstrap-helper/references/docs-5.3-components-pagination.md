### Bootstrap Pagination with Icons and ARIA Attributes

Source: https://getbootstrap.com/docs/5.3/components/pagination

This example demonstrates how to use icons (like arrows) for pagination links instead of text. It emphasizes the importance of `aria-label` attributes for screen reader support, ensuring accessibility when visual text is replaced by symbols.

```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
```

--------------------------------

### Large and Small Bootstrap Pagination Sizing

Source: https://getbootstrap.com/docs/5.3/components/pagination

This section provides examples of how to adjust the size of the pagination component. The `.pagination-lg` class is used for larger pagination, while `.pagination-sm` is used for smaller pagination, allowing for visual customization.

```html
<nav aria-label="...">
  <ul class="pagination pagination-lg">
    <li class="page-item active" >
      <a class="page-link" aria-current="page">1</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
  </ul>
</nav>
```

```html
<nav aria-label="...">
  <ul class="pagination pagination-sm">
    <li class="page-item active">
      <a class="page-link" aria-current="page">1</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
  </ul>
</nav>
```

--------------------------------

### Disabled Bootstrap Pagination Item

Source: https://getbootstrap.com/docs/5.3/components/pagination

This example shows how to disable a pagination item using the `.disabled` class. It includes adding `tabindex="-1"` to disabled links for proper keyboard navigation and accessibility, and demonstrates using a `<span>` for non-interactive disabled items.

```html
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active">
      <a class="page-link" href="#" aria-current="page">2</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

```html
<li class="page-item disabled">
  <span class="page-link">Previous</span>
</li>
```

--------------------------------

### Basic Bootstrap Pagination HTML Structure

Source: https://getbootstrap.com/docs/5.3/components/pagination

This snippet shows the fundamental HTML structure for creating a Bootstrap pagination component. It uses a `<nav>` element for accessibility and an unordered list (`<ul>`) with pagination items (`<li class="page-item">`) and links (`<a class="page-link">`).

```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```

--------------------------------

### Center Align Pagination with HTML

Source: https://getbootstrap.com/docs/5.3/components/pagination

Demonstrates how to center-align a Bootstrap pagination component using the `.justify-content-center` flexbox utility. This HTML snippet shows a standard pagination structure with navigation links.

```html
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

--------------------------------

### End Align Pagination with HTML

Source: https://getbootstrap.com/docs/5.3/components/pagination

Illustrates how to right-align a Bootstrap pagination component using the `.justify-content-end` flexbox utility. This HTML snippet presents a typical pagination layout.

```html
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-end">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

--------------------------------

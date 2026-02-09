### Bootstrap Navbar Example

Source: https://getbootstrap.com/docs/5.3/components/navbar

A complete example of a responsive, light-themed Bootstrap navbar that collapses at the 'lg' breakpoint. It includes brand, navigation links, dropdowns, and a search form. This snippet demonstrates the integration of various Bootstrap utility classes for styling and layout.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar Brand Examples

Source: https://getbootstrap.com/docs/5.3/components/navbar

Demonstrates how to use the `.navbar-brand` class in Bootstrap for both links and headings. The first example shows a brand as a link within a container, while the second uses a span with `.navbar-brand` and `.h1` for a heading-like appearance.

```html
<!-- As a link -->
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
  </div>
</nav>

<!-- As a heading -->
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <span class="navbar-brand mb-0 h1">Navbar</span>
  </div>
</nav>
```

--------------------------------

### Default Navbar Placement (HTML)

Source: https://getbootstrap.com/docs/5.3/components/navbar

A basic example of a Bootstrap navbar without any specific placement utilities. This navbar will follow the normal document flow.

```html
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Default</a>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar with Text and Navigation

Source: https://getbootstrap.com/docs/5.3/components/navbar

An example of a Bootstrap navbar combining navigation links, a brand, and text. This demonstrates the integration of multiple components and the use of collapse functionality for responsiveness.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar w/ text</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
      </ul>
      <span class="navbar-text">
        Navbar text with an inline element
      </span>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar with Form Buttons

Source: https://getbootstrap.com/docs/5.3/components/navbar

Demonstrates the inclusion of various button types within a Bootstrap navbar form. This example also highlights the use of vertical alignment utilities for elements of different sizes.

```html
<nav class="navbar bg-body-tertiary">
  <form class="container-fluid justify-content-start">
    <button class="btn btn-outline-success me-2" type="button">Main button</button>
    <button class="btn btn-sm btn-outline-secondary" type="button">Smaller button</button>
  </form>
</nav>
```

--------------------------------

### Bootstrap Navbar with Brand and Search Form

Source: https://getbootstrap.com/docs/5.3/components/navbar

Shows a Bootstrap navbar containing both a brand link and a search form. This example illustrates how to combine different elements within the navbar structure using flexbox.

```html
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">Navbar</a>
    <form class="d-flex" role="search">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
</nav>
```

--------------------------------

### Navbar with Vertical Scrolling (HTML)

Source: https://getbootstrap.com/docs/5.3/components/navbar

Example of a Bootstrap navbar with vertical scrolling enabled for its content using the `.navbar-nav-scroll` class. The scroll height can be customized using CSS variables.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar scroll</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarScroll">
      <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Link</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar with Hidden Brand Toggler

Source: https://getbootstrap.com/docs/5.3/components/navbar

Demonstrates a Bootstrap navbar where the brand is hidden at smaller breakpoints and the toggler is on the left. This example uses standard Bootstrap classes for navigation, collapse, and forms.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <a class="navbar-brand" href="#">Hidden brand</a>
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Dark Navbar Color Scheme

Source: https://getbootstrap.com/docs/5.3/components/navbar

Demonstrates applying a dark color scheme to a Bootstrap navbar using the `data-bs-theme="dark"` attribute. This example uses a dark background and a border.

```html
<nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
  <!-- Navbar content -->
</nav>
```

--------------------------------

### Navbar with Responsive Container (HTML)

Source: https://getbootstrap.com/docs/5.3/components/navbar

Shows how to use responsive containers (e.g., `.container-md`) inside a Bootstrap navbar to adjust the content width at different viewport sizes.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-md">
    <a class="navbar-brand" href="#">Navbar</a>
  </div>
</nav>
```

--------------------------------

### Sticky Top Navbar Placement (HTML)

Source: https://getbootstrap.com/docs/5.3/components/navbar

Shows how to create a Bootstrap navbar that sticks to the top of the viewport after scrolling past it, using the `sticky-top` class. It remains in the normal document flow until it reaches the top.

```html
<nav class="navbar sticky-top bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Sticky top</a>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar with Image

Source: https://getbootstrap.com/docs/5.3/components/navbar

Replace the default text in the `.navbar-brand` with an `<img>` tag to display an image. Ensure the image source and alt text are correctly set.

```html
<nav class="navbar bg-body-tertiary">
  <div class="container">
    <a class="navbar-brand" href="#">
      <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24">
    </a>
  </div>
</nav>
```

--------------------------------

### Navbar with Container (HTML)

Source: https://getbootstrap.com/docs/5.3/components/navbar

Demonstrates how to wrap a Bootstrap navbar within a container to center it on the page. An inner container is also used to control the width of the navbar's content.

```html
<div class="container">
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
    </div>
  </nav>
</div>
```

--------------------------------

### Basic Offcanvas Navbar HTML Structure

Source: https://getbootstrap.com/docs/5.3/components/navbar

This HTML structure demonstrates a basic offcanvas navbar. It utilizes Bootstrap's offcanvas component and navbar classes to create a collapsible navigation sidebar. No specific JavaScript dependencies are explicitly shown, but Bootstrap's JavaScript is implied for functionality.

```html
<nav class="navbar bg-body-tertiary fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Offcanvas navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Offcanvas</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
        </ul>
        <form class="d-flex mt-3" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </div>
</nav>
```

--------------------------------

### Bootstrap Navbar with Image and Text

Source: https://getbootstrap.com/docs/5.3/components/navbar

Combine an image and text within the `.navbar-brand` for a more descriptive brand element. Use utility classes like `.d-inline-block` and `.align-text-top` on the image for proper alignment.

```html
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
      Bootstrap
    </a>
  </div>
</nav>
```

--------------------------------

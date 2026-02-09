### Include Bootstrap CSS and JS via CDN

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

This code demonstrates how to integrate Bootstrap into an HTML page using CDN links. It includes the Bootstrap CSS in the `<head>` and the JavaScript bundle (with Popper) before the closing `</body>` tag. This setup enables all of Bootstrap's features.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>

```

--------------------------------

### Basic HTML Structure for Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

This snippet shows the fundamental HTML structure required for a Bootstrap page. It includes the necessary meta tags for viewport settings and a basic heading. This serves as the foundation before adding Bootstrap's CSS and JavaScript.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>

```

--------------------------------

### Include Bootstrap JS and Popper Separately

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

This snippet shows how to include Bootstrap's JavaScript and Popper.js separately. This is useful if you don't need features like dropdowns, popovers, or tooltips, allowing for a slightly smaller file size. Ensure Popper is included before Bootstrap's main JS.

```html
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.min.js" integrity="sha384-G/EV+4j2dNv+tEPo3++6LCgdCROaejBqfUeNjuKAiuXbjrxilcCdDz6ZAVfHWe1Y" crossorigin="anonymous"></script>

```

--------------------------------

### Viewport Meta Tag for Responsive Design in Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

To ensure proper rendering and touch zooming across all devices, Bootstrap utilizes a mobile-first strategy. Include this responsive viewport meta tag in the `<head>` of your HTML.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">

```

--------------------------------

### HTML5 Doctype Declaration for Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

Bootstrap requires the HTML5 doctype for correct and complete styling. This declaration should be the very first line in your HTML document.

```html
<!doctype html>
<html lang="en">
  ...
</html>

```

--------------------------------

### Overriding Box-sizing for Specific Selectors in Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/introduction

Bootstrap sets the global `box-sizing` to `border-box` for simpler CSS sizing. If you need to revert to `content-box` for a specific element and its descendants, use this CSS snippet.

```css
.selector-for-some-widget {
  box-sizing: content-box;
}

```

--------------------------------

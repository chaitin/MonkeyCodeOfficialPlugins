### Add npm Start Script (package.json)

Source: https://getbootstrap.com/docs/5.3/getting-started/vite

This JSON snippet shows how to add a 'start' script to your `package.json` file. This script is used to run the Vite development server, allowing you to preview your project locally.

```json
{
  // ...
  "scripts": {
    "start": "vite",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ...
}
```

--------------------------------

### Vite HTML Entry Point (src/index.html)

Source: https://getbootstrap.com/docs/5.3/getting-started/vite

This HTML file serves as the entry point for Vite. It includes meta tags for character set and viewport, links to the main JavaScript file, and basic Bootstrap elements to verify CSS loading.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap w/ Vite</title>
    <script type="module" src="./js/main.js"></script>
  </head>
  <body>
    <div class="container py-4 px-3 mx-auto">
      <h1>Hello, Bootstrap and Vite!</h1>
      <button class="btn btn-primary">Primary button</button>
    </div>
  </body>
</html>
```

--------------------------------

### Configure Vite (vite.config.js)

Source: https://getbootstrap.com/docs/5.3/getting-started/vite

This JavaScript configuration file sets up Vite for a Bootstrap project. It defines the root directory for source files, the output directory for builds, and the development server port. It also includes optional settings to silence Sass deprecation warnings.

```javascript
import { resolve } from 'path'

export default {
  root: resolve(__dirname, 'src'),
  build: {
    outDir: '../dist'
  },
  server: {
    port: 8080
  },
  // Optional: Silence Sass deprecation warnings. See note below.
  css: {
     preprocessorOptions: {
        scss: {
          silenceDeprecations: [
            'import',
            'mixed-decls',
            'color-functions',
            'global-builtin',
          ],
        },
     },
  },
}
```

--------------------------------

### Import Bootstrap JS and CSS (src/js/main.js)

Source: https://getbootstrap.com/docs/5.3/getting-started/vite

This JavaScript file imports the custom SCSS file and all of Bootstrap's JavaScript. Popper.js is automatically imported by Bootstrap. Individual plugin imports are also shown as an alternative for smaller bundle sizes.

```javascript
// Import our custom CSS
import '../scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

// You can also import JavaScript plugins individually as needed to keep bundle sizes down:
// import Alert from 'bootstrap/js/dist/alert';

// or, specify which plugins you need:
// import { Tooltip, Toast, Popover } from 'bootstrap';

```

--------------------------------

### Import Bootstrap CSS (src/scss/styles.scss)

Source: https://getbootstrap.com/docs/5.3/getting-started/vite

This SCSS file imports all of Bootstrap's CSS. This is the primary way to include Bootstrap's styling in your project when using Sass.

```scss
// Import all of Bootstrap's CSS
@import "bootstrap/scss/bootstrap";
```

--------------------------------

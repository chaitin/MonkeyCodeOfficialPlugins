### Start Parcel Development Server

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Executes the 'start' npm script to launch the Parcel development server. This command compiles the project assets and makes the application accessible locally for development.

```bash
npm start
```

--------------------------------

### Add Parcel npm Start Script

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Adds a 'start' script to the 'package.json' file. This script uses Parcel to serve the 'src/index.html' file, specifying the public URL and output directory for the compiled assets.

```json
{
   // ...
   "scripts": {
     "start": "parcel serve src/index.html --public-url / --dist-dir dist",
     "test": "echo \"Error: no test specified\" && exit 1"
   },
   // ...
}
```

--------------------------------

### Create Project Structure

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Creates the necessary directories and files for the project structure, including 'src', 'src/js', 'src/scss', 'src/index.html', 'src/js/main.js', and 'src/scss/styles.scss'.

```bash
mkdir {src,src/js,src/scss}
touch src/index.html src/js/main.js src/scss/styles.scss
```

--------------------------------

### Install Bootstrap and Popper.js

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Installs Bootstrap and Popper.js, a required dependency for Bootstrap's dropdowns, popovers, and tooltips, using npm. Popper.js handles the positioning of these components.

```bash
npm i --save bootstrap @popperjs/core
```

--------------------------------

### Create Project Folder and Initialize npm

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Creates a new project directory named 'my-project' and initializes npm within it using the '-y' flag for default settings. This is the first step in setting up a new project.

```bash
mkdir my-project && cd my-project
npm init -y
```

--------------------------------

### Install Parcel Development Dependency

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Installs Parcel as a development dependency using npm. Parcel is a zero-configuration web bundler that automatically detects and installs necessary transformers like Sass.

```bash
npm i --save-dev parcel
```

--------------------------------

### Configure Parcel HTML Entry Point

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

Sets up the main HTML file for the Parcel project. It includes basic HTML structure, links to the SCSS stylesheet, and imports the main JavaScript module. This file serves as the entry point for Parcel.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap w/ Parcel</title>
    <link rel="stylesheet" href="scss/styles.scss">
    <script type="module" src="js/main.js"></script>
  </head>
  <body>
    <div class="container py-4 px-3 mx-auto">
      <h1>Hello, Bootstrap and Parcel!</h1>
      <button class="btn btn-primary">Primary button</button>
    </div>
  </body>
</html>
```

--------------------------------

### Import Individual Bootstrap JS Plugins

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

This demonstrates how to import individual Bootstrap JavaScript plugins, such as Alert, Tooltip, Toast, and Popover, into your `main.js` file. This approach helps reduce the overall bundle size by only including necessary components.

```javascript
import Alert from 'bootstrap/js/dist/alert'

// or, specify which plugins you need:
import { Tooltip, Toast, Popover } from 'bootstrap'

```

--------------------------------

### Import Bootstrap JavaScript in JS

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

This snippet imports all of Bootstrap's JavaScript into your `main.js` file. Popper.js is automatically imported as a dependency. This method includes all Bootstrap JavaScript functionality.

```javascript
// Import all of Bootstrap’s JS
import * as bootstrap from 'bootstrap'

```

--------------------------------

### Configure Sass Deprecation Warnings

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

This configuration file, `.sassrc.js`, silences specific Sass deprecation warnings that may appear when using the latest versions of Dart Sass with Bootstrap. This is an optional step to clean up build output.

```javascript
module.exports = {
  silenceDeprecations: ['import', 'mixed-decls', 'color-functions', 'global-builtin']
}

```

--------------------------------

### Import Bootstrap CSS in Sass

Source: https://getbootstrap.com/docs/5.3/getting-started/parcel

This snippet imports all of Bootstrap's CSS source Sass into your `styles.scss` file. Ensure you have a Sass compiler configured in your Parcel project. This is the primary method for including Bootstrap's styling.

```scss
// Import all of Bootstrap’s CSS
@import "bootstrap/scss/bootstrap";

```

--------------------------------

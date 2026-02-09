### Importing Specific Bootstrap Sass Parts

Source: https://getbootstrap.com/docs/5.3/customize/sass

Provides an example of importing only the necessary parts of Bootstrap's Sass files. This approach is recommended for smaller projects or when specific components are needed, optimizing build times and file sizes. It outlines the recommended order of imports, starting with functions and variables.

```scss
// Custom.scss
// Option B: Include parts of Bootstrap

// 1. Include functions first (so you can manipulate colors, SVGs, calc, etc)
@import "../node_modules/bootstrap/scss/functions";

// 2. Include any default variable overrides here

// 3. Include remainder of required Bootstrap stylesheets (including any separate color mode stylesheets)
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/variables-dark";

// 4. Include any default map overrides here

// 5. Include remainder of required parts
@import "../node_modules/bootstrap/scss/maps";
@import "../node_modules/bootstrap/scss/mixins";
@import "../node_modules/bootstrap/scss/root";

// 6. Include any other optional stylesheet partials as desired; list below is not inclusive of all available stylesheets
@import "../node_modules/bootstrap/scss/utilities";
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/type";
@import "../node_modules/bootstrap/scss/images";
@import "../node_modules/bootstrap/scss/containers";
@import "../node_modules/bootstrap/scss/grid";
@import "../node_modules/bootstrap/scss/helpers";
// ...

// 7. Optionally include utilities API last to generate classes based on the Sass map in `_utilities.scss`
@import "../node_modules/bootstrap/scss/utilities/api";

// 8. Add additional custom code here

```

--------------------------------

### Compiling Sass with the Sass CLI

Source: https://getbootstrap.com/docs/5.3/customize/sass

Demonstrates how to install the Sass CLI globally and then use it to watch your custom Sass file for changes and compile it into a CSS file. This is a common method for compiling Sass during development.

```bash
# Install Sass globally
npm install -g sass

# Watch your custom Sass for changes and compile it to CSS
sass --watch ./scss/custom.scss ./css/custom.css

```

--------------------------------

### Bootstrap Sass File Structure Example (Manual Download)

Source: https://getbootstrap.com/docs/5.3/customize/sass

Illustrates a project file structure when Bootstrap's source files are downloaded manually, without a package manager. It emphasizes keeping Bootstrap's files separate from your own project's assets.

```tree
your-project/
├── scss/
│   └── custom.scss
├── bootstrap/
│   ├── js/
│   └── scss/
└── index.html
```

--------------------------------

### Bootstrap Sass File Structure Example

Source: https://getbootstrap.com/docs/5.3/customize/sass

Demonstrates a typical project file structure when using Bootstrap's Sass files with a package manager like npm. It shows the location of custom Sass files and Bootstrap's source files.

```tree
your-project/
├── scss/
│   └── custom.scss
└── node_modules/
    └── bootstrap/
        ├── js/
        └── scss/
└── index.html
```

--------------------------------

### Importing All of Bootstrap Sass

Source: https://getbootstrap.com/docs/5.3/customize/sass

Shows how to import all of Bootstrap's Sass files into your custom stylesheet. This method includes all variables, mixins, and components, allowing for easy customization of default variables.

```scss
// Custom.scss
// Option A: Include all of Bootstrap

// Include any default variable overrides here (though functions won’t be available)

@import "../node_modules/bootstrap/scss/bootstrap";

// Then add additional custom code here

```

--------------------------------

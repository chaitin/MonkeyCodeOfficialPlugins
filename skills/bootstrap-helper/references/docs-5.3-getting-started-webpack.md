### Start Webpack Development Server (npm)

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Command to initiate the Webpack development server. This command, defined in the 'start' script of `package.json`, compiles the project and serves it locally, enabling hot reloading for rapid development.

```bash
npm start

```

--------------------------------

### Install Webpack Development Dependencies

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Installs core Webpack, the command-line interface, a development server, and a plugin for managing HTML files. These are development-only dependencies.

```bash
npm i --save-dev webpack webpack-cli webpack-dev-server html-webpack-plugin

```

--------------------------------

### Install Bootstrap and Popper

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Installs Bootstrap for UI components and Popper.js for positioning dropdowns, popovers, and tooltips. Popper can be omitted if these components are not used.

```bash
npm i --save bootstrap @popperjs/core

```

--------------------------------

### Initialize npm Project

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Creates a new project folder and initializes npm with default settings, avoiding interactive prompts. This is the first step in setting up a new project.

```bash
mkdir my-project && cd my-project
npm init -y

```

--------------------------------

### Create Project Structure

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Creates the necessary directories and files for the project, including source folders for JavaScript and SCSS, an HTML file, and the Webpack configuration file.

```bash
mkdir {src,src/js,src/scss}
touch src/index.html src/js/main.js src/scss/styles.scss webpack.config.js

```

--------------------------------

### Install Sass and Webpack Loaders

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Installs necessary dependencies for processing Sass files and CSS, including Sass compiler, CSS loader, PostCSS loader, and Autoprefixer. These are development dependencies.

```bash
npm i --save-dev autoprefixer css-loader postcss-loader sass sass-loader style-loader

```

--------------------------------

### Install mini-css-extract-plugin for Webpack

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Installs the mini-css-extract-plugin as a development dependency using npm. This plugin is used to extract CSS into separate files from the JavaScript bundle.

```bash
npm install --save-dev mini-css-extract-plugin
```

--------------------------------

### Define npm Scripts for Webpack (package.json)

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Adds scripts to the `package.json` file for managing the project with Webpack. Includes a 'start' script to run the development server and a 'build' script for production compilation.

```json
{
  // ...
  "scripts": {
    "start": "webpack serve",
    "build": "webpack build --mode=production",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ...
}

```

--------------------------------

### Import Bootstrap JavaScript

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Loads Bootstrap's CSS and imports all of its JavaScript into the main application file (`src/js/main.js`). Popper.js is automatically imported via Bootstrap. This example shows how to import all JS.

```javascript
// Import our custom CSS
import '../scss/styles.scss'

// Import all of Bootstrap’s JS
import * as bootstrap from 'bootstrap'

```

--------------------------------

### Create HTML Template (src/index.html)

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Provides the basic HTML structure for the web page. This file serves as the template for HtmlWebpackPlugin, and it includes elements to display Bootstrap styling and content, ready to be populated by bundled JavaScript.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap w/ Webpack</title>
  </head>
  <body>
    <div class="container py-4 px-3 mx-auto">
      <h1>Hello, Bootstrap and Webpack!</h1>
      <button class="btn btn-primary">Primary button</button>
    </div>
  </body>
</html>

```

--------------------------------

### Configure Webpack Settings (webpack.config.js)

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Sets up the Webpack configuration file. It defines the development mode, entry point for JavaScript, output directory for compiled code, development server behavior (including hot reloading), and integrates HtmlWebpackPlugin for HTML templating.

```javascript
'use strict'

const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: './src/js/main.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  devServer: {
    static: path.resolve(__dirname, 'dist'),
    port: 8080,
    hot: true
  },
  plugins: [
    new HtmlWebpackPlugin({ template: './src/index.html' })
  ]
}
```

--------------------------------

### Include Extracted CSS in HTML

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Adds a link tag to the dist/index.html file to include the generated main.css file. This ensures that the extracted CSS is applied to the webpage.

```html
--- a/dist/index.html
+++ b/dist/index.html
@@ -3,6 +3,7 @@
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
+    <link rel="stylesheet" href="./main.css">
     <title>Bootstrap w/ Webpack</title>
   </head>
   <body>
 
```

--------------------------------

### Configure Webpack to Extract CSS with mini-css-extract-plugin

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Modifies the webpack.config.js file to include the mini-css-extract-plugin and configure the scss rule to use mini-css-extract-plugin.loader instead of style-loader. This separates CSS into its own file.

```javascript
--- a/webpack.config.js
+++ b/webpack.config.js
@@ -3,6 +3,7 @@
 const path = require('path')
 const autoprefixer = require('autoprefixer')
 const HtmlWebpackPlugin = require('html-webpack-plugin')
+const miniCssExtractPlugin = require('mini-css-extract-plugin')
 
 module.exports = {
   mode: 'development',
@@ -17,7 +18,8 @@ module.exports = {
     hot: true
   },
   plugins: [
-    new HtmlWebpackPlugin({ template: './src/index.html' })
+    new HtmlWebpackPlugin({ template: './src/index.html' }),
+    new miniCssExtractPlugin()
   ],
   module: {
     rules: [
@@ -25,8 +27,8 @@ module.exports = {
         test: /\.(scss)$/,
         use: [
           {
-            // Adds CSS to the DOM by injecting a `<style>` tag
-            loader: 'style-loader'
+            // Extracts CSS for each JS file that includes CSS
+            loader: miniCssExtractPlugin.loader
           },
           {
 
```

--------------------------------

### Configure Webpack Loaders for Bootstrap

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Sets up the necessary loaders in `webpack.config.js` to process SCSS files, including style-loader, css-loader, postcss-loader (for Autoprefixer), and sass-loader. This configuration is essential for compiling Bootstrap's Sass.

```javascript
'use strict'

const path = require('path')
const autoprefixer = require('autoprefixer')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: './src/js/main.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  devServer: {
    static: path.resolve(__dirname, 'dist'),
    port: 8080,
    hot: true
  },
  plugins: [
    new HtmlWebpackPlugin({ template: './src/index.html' })
  ],
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            // Adds CSS to the DOM by injecting a `<style>` tag
            loader: 'style-loader'
          },
          {
            // Interprets `@import` and `url()` like `import/require()` and will resolve them
            loader: 'css-loader'
          },
          {
            // Loader for webpack to process CSS with PostCSS
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  autoprefixer
                ]
              }
            }
          },
          {
            // Loads a SASS/SCSS file and compiles it to CSS
            loader: 'sass-loader',
            options: {
              sassOptions: {
                // Optional: Silence Sass deprecation warnings. See note below.
                silenceDeprecations: [
                  'mixed-decls',
                  'color-functions',
                  'global-builtin',
                  'import'
                ]
              }
            }
          }
        ]
      }
    ]
  }
}

```

--------------------------------

### Configure Webpack to Extract SVG Files

Source: https://getbootstrap.com/docs/5.3/getting-started/webpack

Adds a new rule to webpack.config.js to handle SVG files. It uses Webpack's asset modules feature to extract inline SVG data URIs into separate resource files, preventing Content Security Policy issues.

```javascript
--- a/webpack.config.js
+++ b/webpack.config.js
@@ -23,6 +23,14 @@ module.exports = {
   },
   module: {
     rules: [
+      {
+        mimetype: 'image/svg+xml',
+        scheme: 'data',
+        type: 'asset/resource',
+        generator: {
+          filename: 'icons/[hash].svg'
+        }
+      },
       {
         test: /\.(scss)$/,
         use: [
 
```

--------------------------------

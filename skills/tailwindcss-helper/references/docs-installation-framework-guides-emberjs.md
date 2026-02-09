### Create a new Ember.js project

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Initializes a new Ember.js project using `ember-cli` with Embroider enabled and no welcome page. After creation, it changes the current directory into the newly created project.

```Terminal
npx ember-cli new my-project --embroider --no-welcome
cd my-project
```

--------------------------------

### Import application CSS file into Ember.js main application file

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Modifies `./app/app.js` to import the `./app/app.css` file. This ensures that the main application CSS, including the imported Tailwind CSS, is loaded when the Ember.js application starts.

```javascript
import Application from '@ember/application';import Resolver from 'ember-resolver';import loadInitializers from 'ember-load-initializers';import config from 'my-project/config/environment';import 'my-project/app.css';export default class App extends Application {  modulePrefix = config.modulePrefix;  podModulePrefix = config.podModulePrefix;  Resolver = Resolver;}loadInitializers(App, config.modulePrefix);
```

--------------------------------

### Apply Tailwind CSS classes in an Ember.js Handlebars template

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Demonstrates how to use Tailwind CSS utility classes within an Ember.js Handlebars template (`application.hbs`). This example applies text size, font weight, and underline styles to an `<h1>` element, showcasing basic Tailwind usage.

```handlebars
{{page-title "MyProject"}}<h1 class="text-3xl font-bold underline">  Hello world!</h1>{{outlet}}
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies via npm

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Installs `tailwindcss`, `@tailwindcss/postcss`, `postcss`, and `postcss-loader` as project dependencies using npm. These packages are essential for integrating Tailwind CSS with PostCSS in an Ember.js application's build process.

```Terminal
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

--------------------------------

### Add Tailwind CSS PostCSS plugin configuration

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Creates a `postcss.config.mjs` file at the project root to define PostCSS plugins. This configuration adds `@tailwindcss/postcss` to the plugin list, enabling Tailwind CSS processing during the build.

```javascript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
}
```

--------------------------------

### Enable PostCSS support in Ember CLI build configuration

Source: https://tailwindcss.com/docs/installation/framework-guides/emberjs

Modifies the `ember-cli-build.js` file to configure Webpack within Embroider to process `.css` files using `postcss-loader`. This step ensures that PostCSS can transform CSS files in the Ember.js build pipeline, allowing Tailwind CSS to function correctly.

```javascript
'use strict';const EmberApp = require('ember-cli/lib/broccoli/ember-app');module.exports = function (defaults) {  const app = new EmberApp(defaults, {    // Add options here  });  const { Webpack } = require('@embroider/webpack');  return require('@embroider/compat').compatBuild(app, Webpack, {    skipBabel: [      {        package: 'qunit',      },    ],    packagerOptions: {      webpackConfig: {        module: {          rules: [            {              test: /\.css$/i,              use: ['postcss-loader'],            },          ],
        },
      },
    },
  });
};
```

--------------------------------

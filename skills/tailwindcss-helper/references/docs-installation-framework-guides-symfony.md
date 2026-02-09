### Create a new Symfony web application project

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Initializes a new Symfony project with webapp features. This command uses the Symfony CLI to set up a basic project structure, then navigates into the newly created project directory.

```Terminal
symfony new --webapp my-project
cd my-project
```

--------------------------------

### Install Webpack Encore for asset management in Symfony

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Removes default Symfony UX components and installs Webpack Encore, along with `symfony/ux-turbo` and `symfony/stimulus-bundle`, to handle asset compilation and management within the Symfony project.

```Terminal
composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundle
composer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle
```

--------------------------------

### Integrate compiled CSS and use Tailwind classes in Twig template

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Demonstrates how to include the compiled CSS in a Symfony Twig template (`base.html.twig`) using `encore_entry_link_tags`. It also shows an example of using Tailwind's utility classes (`text-3xl font-bold underline`) to style an HTML element.

```html
<!doctype html><html>  <head>    <meta charset="utf-8" />    <meta      name="viewport"      content="width=device-width, initial-scale=1.0"    />    {% block stylesheets %}      {{ encore_entry_link_tags('app') }}    {% endblock %}  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```

--------------------------------

### Configure PostCSS plugins with Tailwind CSS in postcss.config.mjs

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Creates a `postcss.config.mjs` file to define PostCSS plugins. This configuration adds `@tailwindcss/postcss` to the plugin list, allowing Tailwind CSS to be processed by PostCSS.

```javascript
export default {  plugins: {    "@tailwindcss/postcss": {},  },};
```

--------------------------------

### Enable PostCSS Loader in webpack.config.js for Symfony Encore

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Configures Webpack Encore to enable PostCSS processing. This line should be added to your `webpack.config.js` file to ensure that PostCSS plugins, including Tailwind CSS, are applied during asset compilation.

```javascript
Encore  .enablePostCssLoader();
```

--------------------------------

### Import Tailwind CSS and configure source in app.css

Source: https://tailwindcss.com/docs/installation/framework-guides/symfony

Adds an `@import` statement to `app.css` to include Tailwind CSS. The `@source not "../../public";` directive is used to prevent recompilation loops in watch mode by ignoring the public directory.

```css
@import "tailwindcss";@source not "../../public";
```

--------------------------------

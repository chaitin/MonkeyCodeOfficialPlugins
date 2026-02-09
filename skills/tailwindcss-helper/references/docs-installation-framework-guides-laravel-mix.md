### Start Laravel Mix build process with watch mode

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/mix

Run the npm watch command to start the build process in watch mode. This automatically recompiles your CSS and JavaScript whenever files change during development.

```bash
npm run watch
```

--------------------------------

### Install Tailwind CSS npm dependencies

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/mix

Install the required npm packages for Tailwind CSS integration with Laravel. This command installs @tailwindcss/postcss, tailwindcss, and postcss as dependencies for your project.

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

--------------------------------

### Use Tailwind CSS utility classes in Laravel Blade template

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/mix

Include the compiled CSS file in your Blade template's head section and apply Tailwind utility classes to HTML elements. This example demonstrates basic styling with text size, font weight, and text decoration utilities.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="{{ asset('css/app.css') }}" rel="stylesheet" />
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  </body>
</html>
```

--------------------------------

### Configure Tailwind CSS in Laravel Mix webpack.mix.js

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/mix

Add Tailwind CSS as a PostCSS plugin in your webpack.mix.js configuration file. This processes your CSS files through Tailwind's PostCSS plugin during the build process.

```javascript
mix
  .js("resources/js/app.js", "public/js")
  .postCss("resources/css/app.css", "public/css", [
    require("@tailwindcss/postcss")
  ]);
```

--------------------------------

### Import Tailwind CSS and configure content scanning

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/mix

Add Tailwind CSS import and @source directives to your main CSS file to enable Tailwind to scan your project files for utility class usage. This ensures only used styles are included in the final CSS output.

```css
@import "tailwindcss";
@source '../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php';
@source '../../storage/framework/views/*.php';
@source '../**/*.blade.php';
@source '../**/*.js';
```

--------------------------------

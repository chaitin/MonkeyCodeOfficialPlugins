### Basic HTML structure with Tailwind CSS styling

Source: https://tailwindcss.com/docs/installation/using-postcss

This HTML example demonstrates a basic document structure, including the necessary `<link>` tag to reference the compiled CSS. It showcases how to apply Tailwind's utility classes, such as `text-3xl`, `font-bold`, and `underline`, directly to HTML elements for styling.

```html
<!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/dist/styles.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

--------------------------------

### Configure Tailwind CSS PostCSS plugin in JavaScript

Source: https://tailwindcss.com/docs/installation/using-postcss

This JavaScript configuration snippet for `postcss.config.mjs` adds `@tailwindcss/postcss` to your PostCSS plugins. This step ensures that Tailwind CSS processes your stylesheets during the build, enabling its utility-first approach.

```javascript
export default {  plugins: {    "@tailwindcss/postcss": {},  }}
```

--------------------------------

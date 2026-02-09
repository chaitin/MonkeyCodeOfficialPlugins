### Start Parcel development server

Source: https://tailwindcss.com/docs/installation/framework-guides/parcel

Run the Parcel build process with the entry point specified as src/index.html. This command starts the development server and watches for file changes to rebuild the project automatically.

```bash
npx parcel src/index.html
```

--------------------------------

### Create Parcel project with npm

Source: https://tailwindcss.com/docs/installation/framework-guides/parcel

Initialize a new Parcel project by creating a project directory, initializing npm, installing Parcel as a dev dependency, and creating the source directory structure. This sets up the basic project layout needed for Tailwind CSS integration.

```bash
mkdir my-project
cd my-project
npm init -y
npm install parcel
mkdir src
touch src/index.html
```

--------------------------------

### Create HTML template with Tailwind CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/parcel

Set up an index.html file that links to the compiled CSS file and demonstrates Tailwind utility classes. This template includes proper meta tags for responsive design and applies Tailwind classes to style content.

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="./index.css" type="text/css" rel="stylesheet" />
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  </body>
</html>
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies

Source: https://tailwindcss.com/docs/installation/framework-guides/parcel

Install the @tailwindcss/postcss package and its peer dependencies via npm. This provides the necessary Tailwind CSS framework and PostCSS plugin for processing Tailwind directives.

```bash
npm install tailwindcss @tailwindcss/postcss
```

--------------------------------

### Configure PostCSS for Tailwind CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/parcel

Create a .postcssrc configuration file in the project root to enable the @tailwindcss/postcss plugin. This file tells PostCSS to process Tailwind CSS directives during the build process.

```json
{
  "plugins": {
    "@tailwindcss/postcss": {}
  }
}
```

--------------------------------

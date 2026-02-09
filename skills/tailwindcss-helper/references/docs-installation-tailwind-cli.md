### Include compiled Tailwind CSS in HTML and use utility classes

Source: https://tailwindcss.com/docs/installation/tailwind-cli

This HTML snippet demonstrates how to link the compiled `output.css` file in your document's `<head>` section. It also shows a basic example of using Tailwind's utility classes (e.g., `text-3xl`, `font-bold`, `underline`) to style an `<h1>` element.

```html
<!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="./output.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

--------------------------------

### Install Tailwind CSS and CLI via npm

Source: https://tailwindcss.com/docs/installation/tailwind-cli

This command installs the core Tailwind CSS library and the Tailwind CLI tool as development dependencies in your project. It's the first step to get the necessary packages for building your CSS.

```Terminal
npm install tailwindcss @tailwindcss/cli
```

--------------------------------

### Run Tailwind CLI to build CSS with watch mode

Source: https://tailwindcss.com/docs/installation/tailwind-cli

Execute the Tailwind CLI to scan your source files for utility classes, process your input CSS, and generate the final output CSS file. The `--watch` flag keeps the process running, automatically recompiling your CSS whenever changes are detected in your source files.

```Terminal
npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

--------------------------------

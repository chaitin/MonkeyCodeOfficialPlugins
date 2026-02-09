### Create a new Vite project using npm

Source: https://tailwindcss.com/docs/index

This command initializes a new Vite project in the current directory. It uses `npm create vite@latest` to scaffold a modern web project, setting up the basic file structure and dependencies. The `cd my-project` command then navigates into the newly created project directory.

```Shell
npm create vite@latest my-project
cd my-project
```

--------------------------------

### Configure Tailwind CSS Vite plugin in vite.config.ts

Source: https://tailwindcss.com/docs/index

This configuration snippet adds the `@tailwindcss/vite` plugin to the Vite build process. By importing `defineConfig` from `vite` and `tailwindcss` from `@tailwindcss/vite`, it enables Tailwind CSS to process class names found in project files and generate the corresponding CSS. This setup is crucial for Tailwind's JIT (Just-In-Time) compilation.

```TypeScript
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

--------------------------------

### Basic HTML structure with Tailwind CSS classes

Source: https://tailwindcss.com/docs/index

This HTML snippet demonstrates how to include the compiled CSS and apply Tailwind's utility classes to style elements. The `<link>` tag points to the generated stylesheet, and classes like `text-3xl`, `font-bold`, and `underline` are used directly on the `<h1>` element to apply styling. This shows the final integration of Tailwind CSS into an application's UI.

```HTML
<!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/src/style.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

--------------------------------

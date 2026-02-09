### Create Vite Project with npm

Source: https://tailwindcss.com/docs/installation/using-vite

Initialize a new Vite project using Create Vite. This command creates a new project directory and navigates into it for subsequent setup steps.

```bash
npm create vite@latest my-project
cd my-project
```

--------------------------------

### Use Tailwind CSS Utility Classes in HTML

Source: https://tailwindcss.com/docs/installation/using-vite

Apply Tailwind CSS utility classes to HTML elements for styling. This example demonstrates using text-3xl, font-bold, and underline classes to style a heading element.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/src/style.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Configure Tailwind CSS Vite Plugin

Source: https://tailwindcss.com/docs/installation/using-vite

Add the @tailwindcss/vite plugin to the Vite configuration file. This enables Tailwind CSS processing during the build process for frameworks like Laravel, SvelteKit, React Router, Nuxt, and SolidJS.

```typescript
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

--------------------------------

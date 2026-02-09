### Create a new Nuxt.js project using npm

Source: https://tailwindcss.com/docs/installation/framework-guides/nuxt

This command initializes a fresh Nuxt.js project named 'my-project' in the current directory. It then navigates into the newly created project folder, preparing the environment for further setup and dependency installation.

```Terminal
npm create nuxt my-project
cd my-project
```

--------------------------------

### Apply Tailwind CSS classes in a Vue component template

Source: https://tailwindcss.com/docs/installation/framework-guides/nuxt

This example demonstrates how to directly apply Tailwind's utility classes within the `<template>` section of a Vue component, specifically in `app.vue`. It shows styling an `<h1>` element with `text-3xl`, `font-bold`, and `underline` classes, illustrating the direct application of Tailwind for rapid UI development.

```vue
<template>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></template>
```

--------------------------------

### Globally link main.css in nuxt.config.ts for Nuxt

Source: https://tailwindcss.com/docs/installation/framework-guides/nuxt

This update to `nuxt.config.ts` adds the path to your `main.css` file to the global `css` array. By doing so, Nuxt automatically includes your Tailwind CSS styles across all pages and components of your application, ensuring consistent styling.

```typescript
import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
});
```

--------------------------------

### Configure Tailwind CSS Vite Plugin in nuxt.config.ts

Source: https://tailwindcss.com/docs/installation/framework-guides/nuxt

This configuration snippet adds the `@tailwindcss/vite` plugin to the `vite.plugins` array within your `nuxt.config.ts` file. It ensures that Tailwind CSS is properly recognized and processed by Vite, which Nuxt uses for its build system, allowing for correct compilation of Tailwind utilities.

```typescript
import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
});
```

--------------------------------

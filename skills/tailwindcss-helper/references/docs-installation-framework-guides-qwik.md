### Create a new Qwik project using npm

Source: https://tailwindcss.com/docs/installation/framework-guides/qwik

This command initializes a new Qwik project named 'my-project' using the latest Qwik starter template. After creation, it navigates into the project directory, preparing for further setup.

```Terminal
npm create qwik@latest empty my-project
cd my-project
```

--------------------------------

### Apply Tailwind CSS classes in a Qwik component

Source: https://tailwindcss.com/docs/installation/framework-guides/qwik

This example demonstrates how to use Tailwind CSS utility classes directly within a Qwik component's JSX. It applies `text-3xl`, `font-bold`, and `underline` classes to an `<h1>` element, styling the text.

```typescript
import { component$ } from '@builder.io/qwik'

export default component$(() => {
  return (
    <h1 class="text-3xl font-bold underline">
      Hello World!
    </h1>
  )
})
```

--------------------------------

### Configure Tailwind CSS Vite plugin in vite.config.ts

Source: https://tailwindcss.com/docs/installation/framework-guides/qwik

This configuration snippet integrates the `@tailwindcss/vite` plugin into the Vite build process for your Qwik project. It ensures that Tailwind CSS is correctly recognized and processed by Vite, enabling its utility classes in your application.

```typescript
import { defineConfig } from 'vite'import { qwikVite } from "@builder.io/qwik/optimizer";import { qwikCity } from "@builder.io/qwik-city/vite";// …import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({ command, mode }): UserConfig => {
  return {
    plugins: [
      tailwindcss(),
      qwikCity(),
      qwikVite(),
      tsconfigPaths(),
    ],
    // …
  }
})
```

--------------------------------

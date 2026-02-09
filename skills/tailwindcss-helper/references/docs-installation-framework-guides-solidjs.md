### Create new SolidJS project with Vite template

Source: https://tailwindcss.com/docs/installation/framework-guides/solidjs

Initializes a new SolidJS project using `npx degit` with the SolidJS Vite template. This command sets up the basic project structure and navigates into the new directory, preparing for development.

```Terminal
npx degit solidjs/templates/js my-project
cd my-project
```

--------------------------------

### Apply Tailwind CSS utility classes in SolidJS `App.jsx` component

Source: https://tailwindcss.com/docs/installation/framework-guides/solidjs

Demonstrates how to use Tailwind CSS utility classes directly within a SolidJS component's JSX to style elements. This example applies text size, font weight, and underline styles to an `<h1>` tag, showcasing basic usage.

```JSX
export default function App() {
  return (
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  )}

```

--------------------------------

### Configure Vite plugin for Tailwind CSS in SolidJS `vite.config.ts`

Source: https://tailwindcss.com/docs/installation/framework-guides/solidjs

Modifies the `vite.config.ts` file to include the `@tailwindcss/vite` plugin, enabling Tailwind CSS processing within the Vite build pipeline. It also configures the SolidJS plugin and server settings for development.

```TypeScript
import { defineConfig } from 'vite';import solidPlugin from 'vite-plugin-solid';import tailwindcss from '@tailwindcss/vite';export default defineConfig({
  plugins: [
    tailwindcss(),
    solidPlugin(),
  ],
  server: {
    port: 3000,
  },
  build: {
    target: 'esnext',
  },
});
```

--------------------------------

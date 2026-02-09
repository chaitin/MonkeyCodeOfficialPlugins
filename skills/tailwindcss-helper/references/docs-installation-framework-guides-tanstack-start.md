### Create TanStack Start Project

Source: https://tailwindcss.com/docs/installation/framework-guides/tanstack-start

Initialize a new TanStack Start project using Create Start App. This command creates a new project directory and installs all necessary dependencies for a TanStack Start application.

```bash
npx create-start-app@latest my-project
cd my-project
```

--------------------------------

### Link CSS File in Root Route

Source: https://tailwindcss.com/docs/installation/framework-guides/tanstack-start

Import the compiled CSS file in your root route component using the ?url query parameter. This ensures the stylesheet is loaded globally for all pages in your TanStack Start application.

```typescript
// other imports...
import appCss from '../styles.css?url'

export const Route = createRootRoute({
  head: () => ({
    meta: [
      // your meta tags and site config
    ],
    links: [{ rel: 'stylesheet', href: appCss }],
    // other head config
  }),
  component: RootComponent,
})
```

--------------------------------

### Configure Vite Plugin for Tailwind CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/tanstack-start

Add the @tailwindcss/vite plugin to your Vite configuration file. This plugin must be placed before other plugins in the plugins array to ensure proper CSS processing and integration with TanStack Start.

```typescript
import { tanstackStart } from '@tanstack/react-start/plugin/vite';
import { defineConfig } from 'vite';
import tsConfigPaths from 'vite-tsconfig-paths';
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
    tanstackStart(),
    tsConfigPaths(),
  ]
});
```

--------------------------------

### Use Tailwind CSS Utility Classes in Components

Source: https://tailwindcss.com/docs/installation/framework-guides/tanstack-start

Apply Tailwind CSS utility classes to HTML elements in your React components. This example demonstrates using text sizing, font weight, and text decoration utilities to style a heading.

```typescript
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({ 
  component: App,
})

function App() {
  return (
    <h1 class="text-3xl font-bold underline">
      Hello World!
    </h1>
  )
}
```

--------------------------------

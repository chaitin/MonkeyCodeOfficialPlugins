### Create a new React Router project using npx

Source: https://tailwindcss.com/docs/installation/framework-guides/react-router

This command initializes a new React Router project with the specified name and then navigates into the newly created project directory. It's the essential first step for setting up a new application.

```Terminal
npx create-react-router@latest my-project
cd my-project
```

--------------------------------

### Configure Vite to use Tailwind CSS and React Router plugins

Source: https://tailwindcss.com/docs/installation/framework-guides/react-router

This configuration file (`vite.config.ts`) integrates the `@tailwindcss/vite` and `@react-router/dev/vite` plugins into the Vite build process. It ensures that both Tailwind CSS processing and React Router development tools are properly set up for the project.

```typescript
import { reactRouter } from "@react-router/dev/vite";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    tailwindcss(),
    reactRouter(),
    tsconfigPaths(),
  ],
});
```

--------------------------------

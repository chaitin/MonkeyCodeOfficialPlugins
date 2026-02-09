### Start Development Build Process

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/vite

Run the npm development script to start the Vite build process. This watches for file changes and recompiles your CSS with Tailwind utilities in real-time during development.

```bash
npm run dev
```

--------------------------------

### Create New Laravel Project

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/vite

Initialize a new Laravel project using the Laravel installer and navigate to the project directory. This sets up the basic Laravel application structure needed for Tailwind CSS integration.

```bash
laravel new my-project
cd my-project
```

--------------------------------

### Install Tailwind CSS and Vite Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/vite

Install the Tailwind CSS package and the @tailwindcss/vite plugin along with their peer dependencies using npm. This provides the necessary tools to integrate Tailwind CSS into your Laravel project.

```bash
npm install tailwindcss @tailwindcss/vite
```

--------------------------------

### Configure Vite Plugin for Tailwind CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/laravel/vite

Add the @tailwindcss/vite plugin to your Vite configuration file. This enables Tailwind CSS processing during the build process and allows Vite to handle CSS compilation with Tailwind utilities.

```typescript
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
    // …
  ],
})
```

--------------------------------

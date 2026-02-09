### Start Development Server

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Run the npm run dev command to start the Astro development server. This compiles your project and enables hot module reloading for real-time development.

```bash
npm run dev
```

--------------------------------

### Create Astro Project with npm

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Initialize a new Astro project using the create-astro command-line tool. This sets up the basic project structure and configuration files needed for an Astro application.

```bash
npm create astro@latest my-project
cd my-project
```

--------------------------------

### Use Tailwind CSS Utility Classes in Astro Component

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Import the global CSS file in an Astro component and apply Tailwind utility classes to HTML elements. This example demonstrates basic text styling with Tailwind's text-3xl, font-bold, and underline utilities.

```astro
---
import "../styles/global.css";
---

<h1 class="text-3xl font-bold underline">
  Hello world!
</h1>
```

--------------------------------

### Install Tailwind CSS and Vite Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Install the @tailwindcss/vite plugin and Tailwind CSS as npm dependencies. The @tailwindcss/vite package provides the necessary integration between Tailwind CSS and Astro's Vite build tool.

```bash
npm install tailwindcss @tailwindcss/vite
```

--------------------------------

### Import Tailwind CSS in Global Stylesheet

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Create a global CSS file at ./src/styles/global.css and import Tailwind CSS using the @import directive. This loads all Tailwind utility classes and base styles into your project.

```css
@import "tailwindcss";
```

--------------------------------

### Configure Tailwind CSS Vite Plugin in Astro

Source: https://tailwindcss.com/docs/installation/framework-guides/astro

Add the @tailwindcss/vite plugin to the Vite configuration in the astro.config.mjs file. This enables Tailwind CSS processing during the build process and development server.

```javascript
// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
});
```

--------------------------------

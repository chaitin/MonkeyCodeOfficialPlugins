### Start Development Server

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Run the npm dev script to start the AdonisJS development server with Vite. This enables hot module replacement and automatic CSS compilation with Tailwind CSS.

```bash
npm run dev
```

--------------------------------

### Create AdonisJS Project

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Initialize a new AdonisJS project using the Create AdonisJS CLI tool with the web kit. This command scaffolds a complete AdonisJS application structure ready for Tailwind CSS integration.

```bash
npm init adonisjs@latest my-project -- --kit=web
cd my-project
```

--------------------------------

### Install Tailwind CSS and Vite Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Install the Tailwind CSS package and the @tailwindcss/vite plugin along with peer dependencies. These packages enable Tailwind CSS processing through the Vite build tool.

```bash
npm install tailwindcss @tailwindcss/vite
```

--------------------------------

### Use Tailwind CSS in AdonisJS Edge Template

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Include the compiled CSS file in the HTML head using @vite helper and apply Tailwind utility classes to HTML elements. This example demonstrates basic Tailwind styling with text size, font weight, and text decoration utilities.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    @vite(['resources/css/app.css', 'resources/js/app.js'])
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

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Add the @tailwindcss/vite plugin to the Vite configuration file. This integrates Tailwind CSS processing into the AdonisJS build pipeline alongside the AdonisJS Vite plugin.

```typescript
import { defineConfig } from 'vite'
import adonisjs from '@adonisjs/vite/client'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
    adonisjs({
      // …
    }),
  ],
})
```

--------------------------------

### Import Tailwind CSS and Configure Source Scanning

Source: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

Add @import directive to import Tailwind CSS styles and use @source directive to specify the views directory for utility class scanning. This enables Tailwind to detect and generate only used utility classes.

```css
@import "tailwindcss";
@source "../views";
```

--------------------------------

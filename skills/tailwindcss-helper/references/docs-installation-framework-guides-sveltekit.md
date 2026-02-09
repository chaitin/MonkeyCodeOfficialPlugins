### Create SvelteKit Project

Source: https://tailwindcss.com/docs/installation/framework-guides/sveltekit

Initialize a new SvelteKit project using the official scaffolding tool. This command creates the project directory structure and installs base dependencies required for a SvelteKit application.

```bash
npx sv create my-project
cd my-project
```

--------------------------------

### Use Tailwind CSS Utility Classes

Source: https://tailwindcss.com/docs/installation/framework-guides/sveltekit

Apply Tailwind CSS utility classes to HTML elements and use the @reference directive in style blocks to access Tailwind's theme tokens. This example demonstrates text styling and accessing theme colors for global styles.

```svelte
<h1 class="text-3xl font-bold underline">
  Hello world!
</h1>

<style lang="postcss">
  @reference "tailwindcss";
  :global(html) {
    background-color: theme(--color-gray-100);
  }
</style>
```

--------------------------------

### Import CSS in SvelteKit Layout

Source: https://tailwindcss.com/docs/installation/framework-guides/sveltekit

Create a root layout component (+layout.svelte) and import the app.css file. This ensures Tailwind CSS styles are available throughout the entire SvelteKit application and all child routes.

```svelte
<script>
  let { children } = $props();
  import "../app.css";
</script>

{@render children()}
```

--------------------------------

### Configure Tailwind CSS Vite Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/sveltekit

Add the @tailwindcss/vite plugin to the Vite configuration file. This enables Tailwind CSS processing during the build and development processes alongside SvelteKit's plugin.

```typescript
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    tailwindcss(),
    sveltekit(),
  ],
});
```

--------------------------------

### Example React Component Using Tailwind CSS Classes

Source: https://tailwindcss.com/docs/installation/framework-guides/rspack/react

Provides a simple React component (`App.jsx`) demonstrating the use of Tailwind CSS utility classes to style an `<h1>` element. This shows how to apply Tailwind styles directly within JSX.

```jsx
export default function App() {  return (    <h1 className="text-3xl font-bold underline">      Hello world!    </h1>  )}
```

--------------------------------

### Create Rspack Project using npm CLI

Source: https://tailwindcss.com/docs/installation/framework-guides/rspack/react

Initializes a new Rspack project using the Rspack CLI. This is the first step before integrating Tailwind CSS and sets up the basic project structure.

```Terminal
npm create rspack@latest
```

--------------------------------

### Install Tailwind CSS and PostCSS Dependencies

Source: https://tailwindcss.com/docs/installation/framework-guides/rspack/react

Installs Tailwind CSS, its PostCSS plugin, PostCSS itself, and the PostCSS loader as development dependencies. These packages are essential for processing Tailwind CSS with Rspack.

```Terminal
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

--------------------------------

### Configure PostCSS to Use Tailwind CSS Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/rspack/react

Creates a `postcss.config.mjs` file in the project root to define PostCSS plugins. This configuration adds the `@tailwindcss/postcss` plugin, enabling Tailwind CSS processing for your styles.

```javascript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

--------------------------------

### Configure Rspack to Use PostCSS Loader for CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/rspack/react

Modifies the `rspack.config.ts` file to enable the PostCSS loader for processing CSS files. This ensures that PostCSS plugins, including Tailwind CSS, are applied during the Rspack build process.

```typescript
export default defineConfig({  // ...  module: {    rules: [      {        test: /\.css$/,        use: ["postcss-loader"],        type: "css",      },      // ...    ],  },})
```

--------------------------------

### Create a New Next.js Project with TypeScript and ESLint

Source: https://tailwindcss.com/docs/installation/framework-guides/nextjs

Initialize a new Next.js application using `create-next-app`, configuring it with TypeScript and ESLint, and then navigate into the newly created project directory.

```Terminal
npx create-next-app@latest my-project --typescript --eslint --app
cd my-project
```

--------------------------------

### Configure PostCSS for Tailwind CSS in Next.js

Source: https://tailwindcss.com/docs/installation/framework-guides/nextjs

Create a `postcss.config.mjs` file in the project root and add the `@tailwindcss/postcss` plugin to the PostCSS configuration, enabling Tailwind CSS processing for your styles.

```javascript
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};export default config;
```

--------------------------------

### Apply Tailwind CSS Classes in a Next.js React Component

Source: https://tailwindcss.com/docs/installation/framework-guides/nextjs

Demonstrate how to use Tailwind's utility classes directly within a React component, such as `page.tsx`, to style HTML elements with responsive and pre-defined styles.

```tsx
export default function Home() {
  return (
    <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
  )
}
```

--------------------------------

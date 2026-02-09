### Start Meteor Development Server

Source: https://tailwindcss.com/docs/installation/framework-guides/meteor

Run the Meteor development server using npm start. This initiates the build process and watches for file changes, compiling Tailwind CSS utilities automatically.

```bash
npm run start
```

--------------------------------

### Create Meteor Project with CLI

Source: https://tailwindcss.com/docs/installation/framework-guides/meteor

Initialize a new Meteor project using the Meteor command-line interface. This creates the project directory structure and installs core Meteor dependencies.

```bash
npx meteor create my-project
cd my-project
```

--------------------------------

### Use Tailwind Utility Classes in React Component

Source: https://tailwindcss.com/docs/installation/framework-guides/meteor

Apply Tailwind CSS utility classes to React components using the className attribute. This example demonstrates styling a heading with text size, font weight, and text decoration utilities.

```javascript
export const App = () => (
  <h1 className="text-3xl font-bold underline">
    Hello world!
  </h1>
)
```

--------------------------------

### Install Tailwind CSS and Dependencies via npm

Source: https://tailwindcss.com/docs/installation/framework-guides/meteor

Install Tailwind CSS packages including @tailwindcss/postcss and required peer dependencies (postcss and postcss-load-config) into the Meteor project.

```bash
npm install tailwindcss @tailwindcss/postcss postcss postcss-load-config
```

--------------------------------

### Configure PostCSS Plugins for Tailwind

Source: https://tailwindcss.com/docs/installation/framework-guides/meteor

Create a postcss.config.mjs file in the project root to register the @tailwindcss/postcss plugin. This enables PostCSS to process Tailwind directives during the build process.

```javascript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

--------------------------------

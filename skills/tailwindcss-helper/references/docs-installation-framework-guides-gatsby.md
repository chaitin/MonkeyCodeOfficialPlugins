### Start Gatsby Development Server

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Run the gatsby develop command to start the development server and build process. This compiles your Tailwind CSS and watches for changes.

```bash
gatsby develop
```

--------------------------------

### Create Gatsby Project with CLI

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Initialize a new Gatsby project using the Gatsby CLI tool. This creates a basic project structure and installs core Gatsby dependencies.

```bash
gatsby new my-project
cd my-project
```

--------------------------------

### Import Tailwind CSS in Global Styles

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Create a global CSS file at ./src/styles/global.css and import the Tailwind CSS framework using the @import directive.

```css
@import "tailwindcss";
```

--------------------------------

### Use Tailwind Utility Classes in React Components

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Apply Tailwind CSS utility classes to JSX elements using the className attribute. This example demonstrates styling a heading with text size, font weight, and underline utilities.

```javascript
export default function IndexPage() {
  return (
    <Layout>
      <h1 className="text-3xl font-bold underline">
        Hello world!
      </h1>
    </Layout>
  )
}
```

--------------------------------

### Configure PostCSS Plugins

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Create a postcss.config.js file at the project root and add the @tailwindcss/postcss plugin to enable Tailwind CSS processing through PostCSS.

```javascript
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

--------------------------------

### Install Tailwind CSS and Dependencies

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Install Tailwind CSS PostCSS plugin, core Tailwind package, PostCSS, and the Gatsby PostCSS plugin using npm. These are required peer dependencies for Tailwind CSS integration.

```bash
npm install @tailwindcss/postcss tailwindcss postcss gatsby-plugin-postcss
```

--------------------------------

### Import Global CSS in Gatsby Browser

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Create a gatsby-browser.js file at the project root and import the global CSS file to ensure styles are applied across all pages.

```javascript
import './src/styles/global.css';
```

--------------------------------

### Enable Gatsby PostCSS Plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/gatsby

Configure the gatsby-plugin-postcss in the gatsby-config.js file to enable PostCSS processing in your Gatsby build pipeline.

```javascript
module.exports = {
  plugins: [
    'gatsby-plugin-postcss',
    // ...
  ],
}
```

--------------------------------

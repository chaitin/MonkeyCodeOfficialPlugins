### Start Angular development server

Source: https://tailwindcss.com/docs/installation/framework-guides/angular

Execute this command in your terminal to start the Angular development server. This compiles your application and serves it locally, allowing you to view changes in your browser.

```Terminal
ng serve
```

--------------------------------

### Create new Angular project using Angular CLI

Source: https://tailwindcss.com/docs/installation/framework-guides/angular

This command initializes a new Angular project named 'my-project' with CSS as the default styling preprocessor. After creation, it navigates into the newly created project directory.

```Terminal
ng new my-project --style css
cd my-project
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies via npm

Source: https://tailwindcss.com/docs/installation/framework-guides/angular

This command installs `tailwindcss`, `@tailwindcss/postcss`, and `postcss` as project dependencies. The `--force` flag is included to help resolve potential peer dependency conflicts during installation.

```Terminal
npm install tailwindcss @tailwindcss/postcss postcss --force
```

--------------------------------

### Configure PostCSS to use Tailwind CSS plugin

Source: https://tailwindcss.com/docs/installation/framework-guides/angular

Create a `.postcssrc.json` file in your project's root directory. This JSON configuration instructs PostCSS to use the `@tailwindcss/postcss` plugin, enabling Tailwind CSS processing for your stylesheets.

```JSON
{
  "plugins": {
    "@tailwindcss/postcss": {}
  }
}
```

--------------------------------

### Apply Tailwind CSS utility classes in Angular component template

Source: https://tailwindcss.com/docs/installation/framework-guides/angular

This HTML snippet demonstrates how to use Tailwind CSS utility classes directly within an Angular component template. Classes like `text-3xl`, `font-bold`, and `underline` are applied to style an `<h1>` element.

```HTML
<h1 class="text-3xl font-bold underline">  Hello world!</h1>
```

--------------------------------

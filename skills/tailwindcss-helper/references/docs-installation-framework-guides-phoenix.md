### Start Phoenix server with Tailwind CSS build

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Run the `mix phx.server` command to start your Phoenix development server. This will also trigger the configured Tailwind CSS build process, compiling your styles and making them available in your application.

```bash
mix phx.server
```

--------------------------------

### Create a new Phoenix project

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Initialize a new Phoenix application from scratch. This command sets up the basic project structure and necessary files, preparing the environment for further configuration.

```bash
mix phx.new myproject
cd myproject
```

--------------------------------

### Install Tailwind CSS standalone CLI

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Execute the `mix tailwind.install` command to download the standalone Tailwind CSS CLI executable. This command fetches the necessary binary for Tailwind to function within your Phoenix project.

```bash
mix tailwind.install
```

--------------------------------

### Apply Tailwind CSS utility classes in Phoenix template

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Demonstrates how to use Tailwind's utility classes directly within your Phoenix HTML templates. This example applies text size, font weight, and underline styles to an `<h1>` element.

```html
<h1 class="text-3xl font-bold underline">
  Hello world!</h1>
```

--------------------------------

### Configure Tailwind CSS plugin in Phoenix

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Configure the Tailwind plugin in `config/config.exs` to specify the desired Tailwind CSS version and define the input/output paths for your stylesheets. This setup directs where Tailwind should read your source CSS and where to output the compiled CSS.

```elixir
config :tailwind,
  version: "4.1.10",
  myproject: [
    args: ~w(
      --input=assets/css/app.css
      --output=priv/static/assets/app.css
    ),
    cd: Path.expand("..", __DIR__)
  ]
```

--------------------------------

### Enable Tailwind CSS watcher in Phoenix development

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Add the Tailwind watcher to your `config/dev.exs` file. This configuration enables live reloading of your CSS during development, automatically recompiling Tailwind styles whenever changes are detected.

```elixir
watchers: [
  # Start the esbuild watcher by calling Esbuild.install_and_run(:default, args)
  esbuild: {Esbuild, :install_and_run, [:myproject, ~w(--sourcemap=inline --watch)]},
  tailwind: {Tailwind, :install_and_run, [:myproject, ~w(--watch)]}
]
```

--------------------------------

### Update Phoenix deployment script for Tailwind CSS

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Modify the `assets.deploy` alias in `mix.exs` to include the Tailwind CSS build step for production deployments. This ensures that your CSS is minified and prepared correctly when deploying your Phoenix application.

```elixir
defp aliases do  [
    # …
    "assets.deploy": [
      "tailwind myproject --minify",
      "esbuild myproject --minify",
      "phx.digest"
    ]
  ]end
```

--------------------------------

### Add Tailwind plugin dependency in Phoenix

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Add the official Tailwind plugin to your Phoenix project's dependencies. This entry in `mix.exs` ensures the plugin is available during development, allowing Phoenix to manage Tailwind CSS integration.

```elixir
defp deps do  [
    # …
    {:tailwind, "~> 0.3", runtime: Mix.env() == :dev},
  ]end
```

--------------------------------

### Remove default CSS import from Phoenix JavaScript

Source: https://tailwindcss.com/docs/installation/framework-guides/phoenix

Remove the default CSS import line from `assets/js/app.js`. Since Tailwind is now handling your styling pipeline, this default import is no longer needed and can be safely removed to avoid conflicts or redundant processing.

```javascript
// Remove this line if you add your own CSS build pipeline (e.g postcss).import "../css/app.css"
```

--------------------------------

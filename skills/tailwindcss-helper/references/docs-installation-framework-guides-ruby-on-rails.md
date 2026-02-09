### Start Development Build Process

Source: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

Run the development server with the Tailwind CSS build process. This command starts both the Rails server and watches for CSS changes.

```bash
./bin/dev
```

--------------------------------

### Create New Rails Project

Source: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

Initialize a new Ruby on Rails project using the Rails command line interface. This creates the project directory structure and installs default dependencies.

```bash
rails new my-project
cd my-project
```

--------------------------------

### Apply Tailwind Utility Classes in ERB Template

Source: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

Use Tailwind CSS utility classes in Rails ERB templates to style HTML elements. This example demonstrates applying text sizing, font weight, and text decoration utilities to a heading element.

```erb
<h1 class="text-3xl font-bold underline">
  Hello world!
</h1>
```

--------------------------------

### Install Tailwind CSS Rails Gem

Source: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

Add the tailwindcss-rails gem to your Gemfile and run the install command to configure Tailwind CSS in your Rails project. This sets up necessary configuration files and build scripts.

```bash
bundle add tailwindcss-rails
./bin/rails tailwindcss:install
```

--------------------------------

### Sort Tailwind CSS Classes with Prettier Plugin (HTML)

Source: https://tailwindcss.com/docs/editor-setup

This example demonstrates the effect of the official Prettier plugin for Tailwind CSS, which automatically reorders utility classes in HTML markup according to recommended best practices. It shows a 'before' state with unsorted classes and an 'after' state with the classes reordered for consistency, improving readability and maintainability.

```html
<!-- Before --><button class="text-white px-4 sm:px-8 py-2 sm:py-3 bg-sky-700 hover:bg-sky-800">Submit</button><!-- After --><button class="bg-sky-700 px-4 py-2 text-white hover:bg-sky-800 sm:px-8 sm:py-3">Submit</button>
```

--------------------------------

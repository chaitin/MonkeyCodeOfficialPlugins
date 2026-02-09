### Applying Tailwind CSS Color Utilities in a Notification Component (HTML)

Source: https://tailwindcss.com/docs/colors

This example illustrates the application of various Tailwind CSS color utilities like `bg-*`, `border-*`, and `text-*` within a complex UI component, specifically a notification card. It demonstrates how to style backgrounds, borders, and text with specific colors to create a visually appealing element.

```html
<div class="flex items-center gap-4 rounded-lg bg-white p-6 shadow-md outline outline-black/5 dark:bg-gray-800">  <span class="inline-flex shrink-0 rounded-full border border-pink-300 bg-pink-100 p-2 dark:border-pink-300/10 dark:bg-pink-400/10">    <svg class="size-6 stroke-pink-700 dark:stroke-pink-500"><!-- ... --></svg>  </span>  <div>    <p class="text-gray-700 dark:text-gray-400">      <span class="font-medium text-gray-950 dark:text-white">Tom Watson</span> mentioned you in      <span class="font-medium text-gray-950 dark:text-white">Logo redesign</span>    </p>    <time class="mt-1 block text-gray-500" datetime="9:37">9:37am</time>  </div></div>
```

--------------------------------

### Using Arbitrary Opacity Values and CSS Variables with Tailwind CSS Colors (HTML)

Source: https://tailwindcss.com/docs/colors

This example showcases advanced opacity control in Tailwind CSS, allowing for arbitrary percentage values (e.g., `bg-pink-500/[71.37%]`) and dynamic opacity using CSS variables (e.g., `bg-cyan-400/(--my-alpha-value)`). This provides maximum flexibility for color transparency.

```html
<div class="bg-pink-500/[71.37%]"><!-- ... --></div><div class="bg-cyan-400/(--my-alpha-value)"><!-- ... --></div>
```

--------------------------------

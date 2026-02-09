### Creating a responsive profile card with Tailwind CSS

Source: https://tailwindcss.com/docs/styling-with-utility-classes

This HTML snippet illustrates building a responsive profile card component using Tailwind CSS utility classes. It includes an image, text, and a button, demonstrating responsive design with `sm:` variants, hover, and active states for the button.

```html
<div class="flex flex-col gap-2 p-8 sm:flex-row sm:items-center sm:gap-6 sm:py-4 ...">  <img class="mx-auto block h-24 rounded-full sm:mx-0 sm:shrink-0" src="/img/erin-lindford.jpg" alt="" />  <div class="space-y-2 text-center sm:text-left">    <div class="space-y-0.5">      <p class="text-lg font-semibold text-black">Erin Lindford</p>      <p class="font-medium text-gray-500">Product Engineer</p>    </div>    <button class="border-purple-200 text-purple-600 hover:border-transparent hover:bg-purple-600 hover:text-white active:bg-purple-700 ...">      Message    </button>  </div></div>
```

--------------------------------

### Complex Arbitrary Grid Values in Tailwind CSS

Source: https://tailwindcss.com/docs/styling-with-utility-classes

HTML example showing inline styles for complex CSS grid template columns with calculations and CSS variables. Demonstrates when arbitrary values are too complicated to express as Tailwind class names and require direct style attribute application.

```html
<div class="grid-[2fr_max(0,var(--gutter-width))_calc(var(--gutter-width)+10px)]">
  <div style="grid-template-columns: 2fr max(0, var(--gutter-width)) calc(var(--gutter-width) + 10px)">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Generated CSS for Tailwind CSS Arbitrary Variants

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Provides the simplified CSS output for the arbitrary variant example. This clarifies how Tailwind compiles complex arbitrary selectors, such as sibling and attribute selectors, into standard CSS rules.

```CSS
div > [data-active] + span {  color: var(--color-blue-600);}
```

--------------------------------

### Apply responsive styles with Tailwind breakpoint prefixes

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Use breakpoint prefixes like sm:, md:, lg: to apply utilities only at specific screen sizes. The sm: prefix applies styles at 40rem and above by default, enabling mobile-first responsive design patterns.

```html
<div class="grid grid-cols-2 sm:grid-cols-3">
  <!-- ... -->
</div>
```

```css
.sm\:grid-cols-3 {
  @media (width >= 40rem) {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

--------------------------------

### Example React Component Using Tailwind CSS Classes (JSX)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Provides a React/JSX component demonstrating how Tailwind CSS classes are dynamically applied based on component props. This illustrates Tailwind's build-time scanning process, where it identifies potential class names in project files to generate the necessary CSS.

```JSX
export default function Button({ size, children }) {  let sizeClasses = {    md: "px-4 py-2 rounded-md text-base",    lg: "px-5 py-3 rounded-lg text-lg"  }[size];  return (    <button type="button" className={`font-bold ${sizeClasses}`}>      {children}    </button>  );}
```

--------------------------------

### Apply Multiple Tailwind CSS Variants for Complex Styling (HTML)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Shows an HTML example of applying multiple Tailwind CSS variants (dark mode, large breakpoint, data attribute, hover) to a single element. This demonstrates how to combine various conditions to create highly specific and conditional styles.

```HTML
<button class="dark:lg:data-current:hover:bg-indigo-600 ...">  <!-- ... --></button>
```

--------------------------------

### Generated CSS for Multiple Tailwind CSS Variants

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Provides the simplified CSS output corresponding to the complex Tailwind CSS variants applied in the HTML example. This clarifies how Tailwind compiles multi-variant classes into standard CSS rules, including media queries and attribute selectors.

```CSS
@media (prefers-color-scheme: dark) and (width >= 64rem) {  button[data-current]:hover {    background-color: var(--color-indigo-600);  }}
```

--------------------------------

### CSS stylesheet demonstrating utility class conflict resolution

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Shows the CSS rules for conflicting flex and grid utilities, demonstrating that the .grid class defined later in the stylesheet will take precedence over .flex, resulting in display: grid being applied.

```css
.flex {
  display: flex;
}

.grid {
  display: grid;
}
```

--------------------------------

### Generated CSS for Tailwind CSS `group-hover` Variant

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Shows the simplified CSS output for the `group-hover` variant example. This illustrates how Tailwind translates the `group-hover` utility into standard CSS `:hover` selectors targeting both the parent and child elements.

```CSS
@media (hover: hover) {  a:hover span {    text-decoration-line: underline;  }}
```

--------------------------------

### Define Custom Grid Columns with Tailwind CSS Arbitrary Values (HTML)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Illustrates how to leverage Tailwind CSS's arbitrary value syntax to create a complex, custom grid column definition. This approach is beneficial for implementing layouts that require specific, non-standard column tracks not covered by default theme values.

```HTML
<div class="grid grid-cols-[24rem_2.5rem_minmax(0,1fr)]">  <!-- ... --></div>
```

--------------------------------

### Styling a basic card component with Tailwind CSS

Source: https://tailwindcss.com/docs/styling-with-utility-classes

This HTML snippet demonstrates how to create a simple card component using various Tailwind CSS utility classes. It showcases layout, sizing, background, shadow, and text styling for a 'ChitChat' message card, including dark mode support.

```html
<div class="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">  <img class="size-12 shrink-0" src="/img/logo.svg" alt="ChitChat Logo" />  <div>    <div class="text-xl font-medium text-black dark:text-white">ChitChat</div>    <p class="text-gray-500 dark:text-gray-400">You have a new message!</p>  </div></div>
```

--------------------------------

### Repeated Avatar List with Utility Classes in HTML

Source: https://tailwindcss.com/docs/styling-with-utility-classes

HTML markup showing a contributors section with multiple avatar images using repeated Tailwind utility classes. Demonstrates the duplication problem when the same utility class patterns appear multiple times in static markup.

```html
<div>
  <div class="flex items-center space-x-2 text-base">
    <h4 class="font-semibold text-slate-900">Contributors</h4>
    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>
  </div>
  <div class="mt-3 flex -space-x-2 overflow-hidden">
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt="" />
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
  </div>
  <div class="mt-3 text-sm font-medium">
    <a href="#" class="text-blue-500">+ 198 others</a>
  </div>
</div>
```

--------------------------------

### Tailwind important modifier for forcing utility class precedence

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Shows how to use the ! suffix on Tailwind utility classes to force them to take effect by adding !important to the CSS declaration. This example demonstrates bg-red-500! overriding bg-teal-500 through increased specificity.

```html
<div class="bg-teal-500 bg-red-500!">
  <!-- ... -->
</div>
```

--------------------------------

### Multi-cursor editing for duplicated Tailwind classes in HTML

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Demonstrates a navigation bar with repeated Tailwind utility classes applied to multiple anchor elements. This pattern shows how multi-cursor editing can be used to quickly select and modify identical class lists across similar elements within a single file.

```html
<nav class="flex justify-center space-x-4">
  <a href="/dashboard" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">
    Home
  </a>
  <a href="/team" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">
    Team
  </a>
  <a href="/projects" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">
    Projects
  </a>
  <a href="/reports" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">
    Reports
  </a>
</nav>
```

--------------------------------

### Custom CSS button component with Tailwind theme variables

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Demonstrates creating a custom CSS class for a button component using Tailwind's @layer directive and CSS custom properties for theme consistency. This approach is suitable for simple components in templating languages where creating a full template partial would be excessive.

```css
@import "tailwindcss";

@layer components {
  .btn-primary {
    border-radius: calc(infinity * 1px);
    background-color: var(--color-violet-500);
    padding-inline: --spacing(5);
    padding-block: --spacing(2);
    font-weight: var(--font-weight-semibold);
    color: var(--color-white);
    box-shadow: var(--shadow-md);
    &:hover {
      @media (hover: hover) {
        background-color: var(--color-violet-700);
      }
    }
  }
}
```

--------------------------------

### Dynamic Button Styling with Inline Styles in React

Source: https://tailwindcss.com/docs/styling-with-utility-classes

React component demonstrating inline styles for dynamic color values from props combined with Tailwind utility classes. Accepts buttonColor and textColor as dynamic props to style a button element while maintaining responsive design through utility classes.

```jsx
export function BrandedButton({ buttonColor, textColor, children }) {
  return (
    <button
      style={{
        backgroundColor: buttonColor,
        color: textColor,
      }}
      className="rounded-md px-3 py-1.5 font-medium"
    >
      {children}
    </button>
  );
}
```

--------------------------------

### Apply Arbitrary Background Color with Tailwind CSS (HTML)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Demonstrates how to use Tailwind CSS's arbitrary value syntax to apply a specific, non-theme-defined background color to an HTML element. This is useful for one-off styling requirements that fall outside the configured color palette.

```HTML
<button class="bg-[#316ff6] ...">  Sign in with Facebook</button>
```

--------------------------------

### Avatar List with Loop to Eliminate Duplication in Svelte

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Svelte component using an each loop to render avatar images dynamically, eliminating utility class duplication. The class list is written once and applied to each iteration, solving the duplication problem through component logic.

```svelte
<div>
  <div class="flex items-center space-x-2 text-base">
    <h4 class="font-semibold text-slate-900">Contributors</h4>
    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>
  </div>
  <div class="mt-3 flex -space-x-2 overflow-hidden">
    {#each contributors as user}
      <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src={user.avatarUrl} alt={user.handle} />
    {/each}
  </div>
  <div class="mt-3 text-sm font-medium">
    <a href="#" class="text-blue-500">+ 198 others</a>
  </div>
</div>
```

--------------------------------

### Use CSS `calc()` with Tailwind CSS Arbitrary Values (HTML)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Shows how to embed CSS `calc()` functions directly within Tailwind CSS arbitrary values. This enables dynamic calculations within utility classes, allowing for flexible sizing and positioning even when referencing theme values.

```HTML
<div class="max-h-[calc(100dvh-(--spacing(6)))]">  <!-- ... --></div>
```

--------------------------------

### CSS Variables with Dynamic Values and Tailwind Utilities

Source: https://tailwindcss.com/docs/styling-with-utility-classes

React component using inline styles to set CSS custom properties from dynamic sources, then referencing those variables with Tailwind utility classes. Enables dynamic theming while maintaining utility-first styling approach.

```jsx
export function BrandedButton({ buttonColor, buttonColorHover, textColor, children }) {
  return (
    <button
      style={{
        "--bg-color": buttonColor,
        "--bg-color-hover": buttonColorHover,
        "--text-color": textColor,
      }}
      className="bg-(--bg-color) text-(--text-color) hover:bg-(--bg-color-hover) ..."
    >
      {children}
    </button>
  );
}
```

--------------------------------

### React conditional styling to avoid conflicting Tailwind classes

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Demonstrates best practice for handling conditional styling in React by using ternary operators to apply only one class at a time, preventing conflicting utility classes from being added to the same element.

```jsx
export function Example({ gridLayout }) {
  return <div className={gridLayout ? "grid" : "flex"}>{/* ... */}</div>;
}
```

--------------------------------

### Prefix all Tailwind CSS classes and variables (CSS)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

This snippet illustrates how to add a custom prefix to all Tailwind CSS generated classes and CSS variables. This helps prevent naming conflicts with existing class names in a project. It displays the `@import` syntax in `app.css` and the compiled CSS showing the `tw:` prefix applied to classes and variables.

```css
@import "tailwindcss" prefix(tw);
```

```css
@layer theme {
  :root {
    --tw-color-red-500: oklch(0.637 0.237 25.331);
  }}
@layer utilities {
  .tw\:text-red-500 {
    color: var(--tw-color-red-500);
  }}
```

--------------------------------

### Stack multiple Tailwind variants for combined conditions

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Combine multiple state variants like hover: and disabled: to apply styles only when all conditions are met. This enables precise control over element styling across different interactive states.

```html
<button class="bg-sky-500 disabled:hover:bg-sky-500 ...">Save changes</button>
```

--------------------------------

### Set Custom CSS Variables with Tailwind CSS Arbitrary Values (HTML)

Source: https://tailwindcss.com/docs/styling-with-utility-classes

Explains how to define and apply custom CSS variables using Tailwind CSS's arbitrary value syntax. This feature allows for dynamic styling and responsive adjustments of CSS variables directly within HTML classes.

```HTML
<div class="[--gutter-width:1rem] lg:[--gutter-width:2rem]">  <!-- ... --></div>
```

--------------------------------

### React component with Tailwind CSS for reusable card styling

Source: https://tailwindcss.com/docs/styling-with-utility-classes

A React functional component that encapsulates vacation card styling using Tailwind utility classes. This approach eliminates style duplication across multiple files by creating a single source of truth for component styles that can be easily updated in one location.

```jsx
export function VacationCard({ img, imgAlt, eyebrow, title, pricing, url }) {
  return (
    <div>
      <img className="rounded-lg" src={img} alt={imgAlt} />
      <div className="mt-4">
        <div className="text-xs font-bold text-sky-500">{eyebrow}</div>
        <div className="mt-1 font-bold text-gray-700">
          <a href={url} className="hover:underline">
            {title}
          </a>
        </div>
        <div className="mt-2 text-sm text-gray-600">{pricing}</div>
      </div>
    </div>
  );
}
```

--------------------------------

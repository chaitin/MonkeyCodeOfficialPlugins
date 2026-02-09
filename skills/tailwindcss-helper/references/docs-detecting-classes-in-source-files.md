### Correct Prop Mapping for Static Class Names in JSX

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This JSX example shows the recommended way to handle dynamic classes with props. By mapping prop values to complete, static class strings, Tailwind can correctly identify and generate the necessary CSS utilities at build time.

```jsx
function Button({ color, children }) {
  const colorVariants = {
    blue: "bg-blue-600 hover:bg-blue-500",
    red: "bg-red-600 hover:bg-red-500",
  };
  return <button className={`${colorVariants[color]} ...`}>{children}</button>;
}
```

--------------------------------

### Advanced Prop Mapping for Varied Class Names in JSX

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This JSX example expands on prop mapping, demonstrating how different prop values can correspond to distinct sets of complete Tailwind classes, including varied color shades and text colors. This ensures all classes are statically detectable by Tailwind's scanning process.

```jsx
function Button({ color, children }) {
  const colorVariants = {
    blue: "bg-blue-600 hover:bg-blue-500 text-white",
    red: "bg-red-500 hover:bg-red-400 text-white",
    yellow: "bg-yellow-300 hover:bg-yellow-400 text-black",
  };
  return <button className={`${colorVariants[color]} ...`}>{children}</button>;
}
```

--------------------------------

### Setting Tailwind's Base Path for Source Detection in CSS

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This CSS example shows how to define a custom base path for Tailwind's source detection using the `source()` function within the `@import` statement. This can be beneficial when working with monorepos or complex project structures where the build command runs from a different directory than the project root.

```css
@import "tailwindcss" source("../src");
```

--------------------------------

### Safelist Utilities with Variants in Tailwind CSS

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

Generate classes with multiple variants using @source inline() with variant prefixes in braces. This example generates the underline class with hover and focus variants for responsive styling.

```css
@import "tailwindcss";
@source inline("{hover:,focus:,}underline");
```

--------------------------------

### Correct Dynamic Class Name Usage in HTML

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This HTML example demonstrates the correct approach for dynamic class names. By ensuring the full class names (`text-red-600` or `text-green-600`) are present as complete strings, Tailwind can properly detect and generate the corresponding CSS.

```html
<div class="{{ error ? 'text-red-600' : 'text-green-600' }}"></div>
```

--------------------------------

### Safelist Utilities with Ranges in Tailwind CSS

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

Use brace expansion with ranges to generate multiple classes at once. This example generates all red background colors from 50 to 950 with hover variants using range syntax {100..900..100}.

```css
@import "tailwindcss";
@source inline("{hover:,}bg-red-{50,{100..900..100},950}");
```

--------------------------------

### Explicitly Exclude Classes in Tailwind CSS

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

Use @source not inline() to prevent specific classes from being generated, even if they are detected in source files. This example excludes red background utilities and their hover and focus variants.

```css
@import "tailwindcss";
@source not inline("{hover:,focus:,}bg-red-{50,{100..900..100},950}");
```

--------------------------------

### Incorrect Dynamic Class Name Construction in HTML

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This HTML example shows an incorrect way to construct class names dynamically. Tailwind cannot detect partial class names like `text-{{ error ? 'red' : 'green' }}-600` because it scans for complete, static class strings, not parsed logic.

```html
<div class="text-{{ error ? 'red' : 'green' }}-600"></div>
```

--------------------------------

### Example JSX Component with Tailwind Classes

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This JSX code demonstrates a React component that uses Tailwind CSS classes. Tailwind scans such files as plain text to identify utility classes for CSS generation, making sure the CSS output is minimal and efficient.

```jsx
export function Button({ color, children }) {
  const colors = {
    black: "bg-black text-white",
    blue: "bg-blue-500 text-white",
    white: "bg-white text-black",
  };
  return (
    <button className={`${colors[color]} rounded-full px-2 py-1.5 font-sans text-sm/6 font-medium shadow`}>
      {children}
    </button>
  );
}
```

--------------------------------

### Incorrect Dynamic Class Name Construction with Props in JSX

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This JSX example illustrates an anti-pattern where class names are dynamically constructed using props. Tailwind cannot reliably detect classes like `bg-${color}-600` because it doesn't parse the JavaScript logic to infer the full class names.

```jsx
function Button({ color, children }) {
  return <button className={`bg-${color}-600 hover:bg-${color}-500 ...`}>{children}</button>;
}
```

--------------------------------

### Registering Additional Tailwind Source Paths in CSS

Source: https://tailwindcss.com/docs/detecting-classes-in-source-files

This CSS snippet demonstrates how to use `@source` to explicitly register additional directories for Tailwind to scan for classes. This is particularly useful for including external libraries or files that might otherwise be ignored by default, such as those in `node_modules`.

```css
@import "tailwindcss";
@source "../node_modules/@acmecorp/ui-lib";
```

--------------------------------

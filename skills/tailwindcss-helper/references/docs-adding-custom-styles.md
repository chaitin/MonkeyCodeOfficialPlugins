### Apply Arbitrary Values with Responsive Modifiers in Tailwind CSS HTML

Source: https://tailwindcss.com/docs/adding-custom-styles

Shows how to combine arbitrary values with Tailwind's responsive modifiers. This example demonstrates applying different arbitrary `top` values based on screen sizes, such as `lg:top-[344px]`.

```html
<div class="top-[117px] lg:top-[344px]">
  <!-- ... -->
</div>
```

--------------------------------

### Use Simple Custom Utilities in HTML (HTML)

Source: https://tailwindcss.com/docs/adding-custom-styles

Shows how to apply a custom utility class, defined with `@utility`, directly in HTML. These custom utilities behave like built-in Tailwind utilities and can be combined with variants.

```html
<div class="content-auto">  <!-- ... --></div>
```

--------------------------------

### Apply Arbitrary CSS Properties with Modifiers in Tailwind CSS HTML

Source: https://tailwindcss.com/docs/adding-custom-styles

Shows how to combine arbitrary CSS properties with Tailwind's interactive modifiers. This example demonstrates changing a custom CSS property, like `mask-type`, on hover.

```html
<div class="[mask-type:luminance] hover:[mask-type:alpha]">
  <!-- ... -->
</div>
```

--------------------------------

### Combine Value Types with Multiple Arguments in CSS Utilities

Source: https://tailwindcss.com/docs/adding-custom-styles

Demonstrates how the `--value()` function can accept multiple arguments, resolving them from left to right. This provides a concise way to support various value types (theme, bare, arbitrary) without needing separate declarations, and allows for transformations like converting an integer to a percentage.

```css
@theme {
  --tab-size-github: 8;
}@utility tab-* {
  tab-size: --value(--tab-size-*, integer, [integer]);
}
```

```css
@utility opacity-* {
  opacity: calc(--value(integer) * 1%);
  opacity: --value(--opacity-*, [percentage]);
}
```

--------------------------------

### Use Simple Custom Utilities with Variants in HTML (HTML)

Source: https://tailwindcss.com/docs/adding-custom-styles

Demonstrates that custom utilities defined with `@utility` automatically support Tailwind's variants (e.g., `hover:`). This allows for responsive and interactive custom styling.

```html
<div class="hover:content-auto">  <!-- ... --></div>
```

--------------------------------

### Combine Value Types with Multiple Declarations in CSS Utilities

Source: https://tailwindcss.com/docs/adding-custom-styles

Explains how to use multiple `--value()` declarations within a single `@utility` rule to support theme, bare, and arbitrary values simultaneously. Declarations that fail to resolve for a given utility are simply omitted from the output.

```css
@theme {
  --tab-size-github: 8;
}@utility tab-* {
  tab-size: --value([integer]);
  tab-size: --value(integer);
  tab-size: --value(--tab-size-*);
}
```

```css
@utility opacity-* {
  opacity: --value([percentage]);
  opacity: calc(--value(integer) * 1%);
  opacity: --value(--opacity-*);
}
```

--------------------------------

### Define Functional Custom Utilities with `@utility` and `--value()` (CSS)

Source: https://tailwindcss.com/docs/adding-custom-styles

Explains how to create functional custom utilities that accept arguments (e.g., `tab-*`) using the `@utility` directive and the special `--value()` function. This enables dynamic utility values based on user input.

```css
@utility tab-* {
  tab-size: --value(--tab-size-*);
}
```

--------------------------------

### Define Simple Custom Utilities with `@utility` (CSS)

Source: https://tailwindcss.com/docs/adding-custom-styles

Explains how to create simple custom utility classes (e.g., `content-auto`) using the `@utility` directive. This allows extending Tailwind with specific CSS properties not included by default, which are automatically added to the `utilities` layer.

```css
@utility content-auto {
  content-visibility: auto;
}
```

--------------------------------

### Support Literal Utility Values in Tailwind CSS Utilities

Source: https://tailwindcss.com/docs/adding-custom-styles

Shows how to use the `--value('literal')` syntax to allow specific literal string values for a utility. This enables the creation of utilities like `tab-inherit`, `tab-initial`, or `tab-unset`.

```css
@utility tab-* {
  tab-size: --value("inherit", "initial", "unset");
}
```

--------------------------------

### Define Custom Tailwind CSS Variants Using Shorthand Syntax

Source: https://tailwindcss.com/docs/adding-custom-styles

Presents a shorthand syntax for defining custom variants when complex nesting or `@slot` usage is not required. This simplifies the variant declaration for straightforward conditions.

```css
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

--------------------------------

### Import Tailwind CSS and Add Custom Styles (CSS)

Source: https://tailwindcss.com/docs/adding-custom-styles

Demonstrates how to import Tailwind CSS into a stylesheet and define custom CSS rules alongside it. This allows for integrating project-specific styles that are not covered by Tailwind's utility classes.

```css
@import "tailwindcss";
.my-custom-style {  /* ... */}
```

--------------------------------

### Override Component Classes with Utility Classes (HTML)

Source: https://tailwindcss.com/docs/adding-custom-styles

Demonstrates how utility classes can be used to override specific styles defined within a component class. This showcases Tailwind's flexibility, allowing fine-grained control over component appearance.

```html
<!-- Will look like a card, but with square corners --><div class="card rounded-none">  <!-- ... --></div>
```

--------------------------------

### Define Complex Custom Utilities with Nesting (CSS)

Source: https://tailwindcss.com/docs/adding-custom-styles

Illustrates how to create more complex custom utility classes (e.g., `scrollbar-hidden`) using CSS nesting within the `@utility` directive. This is useful for utilities that involve pseudo-elements or multiple declarations.

```css
@utility scrollbar-hidden {
  &::-webkit-scrollbar {
    display: none;
  }
}
```

--------------------------------

### Support Fraction Values in CSS Utilities using `ratio` Data Type

Source: https://tailwindcss.com/docs/adding-custom-styles

Demonstrates how to handle fraction values in utilities by using the `ratio` data type with `--value()`. This signals Tailwind to treat the value and modifier as a single unit, enabling utilities like `aspect-3/4` or `aspect-[7/9]`.

```css
@utility aspect-* {
  aspect-ratio: --value(--aspect-ratio-*, ratio, [ratio]);
}
```

--------------------------------

### Apply Arbitrary Values for Direct Styling in Tailwind CSS HTML

Source: https://tailwindcss.com/docs/adding-custom-styles

Illustrates applying arbitrary CSS values directly within Tailwind classes using square bracket notation. This enables precise, on-the-fly styling for properties like `top` that fall outside predefined design tokens.

```html
<div class="top-[117px]">
  <!-- ... -->
</div>
```

--------------------------------

### Support Negative Values in Tailwind CSS Utilities

Source: https://tailwindcss.com/docs/adding-custom-styles

Explains how to register separate positive and negative utilities using `--value()` and `--spacing()` functions to handle negative values. This involves applying transformations like multiplying by `-1` for negative variants.

```css
@utility inset-* {
  inset: --spacing(--value(integer));
  inset: --value([percentage], [length]);
}@utility -inset-* {
  inset: --spacing(--value(integer) * -1);
  inset: calc(--value([percentage], [length]) * -1);
}
```

--------------------------------

### Load Legacy Tailwind CSS Plugin with @plugin Directive (CSS)

Source: https://tailwindcss.com/docs/functions-and-directives

The `@plugin` directive enables loading legacy JavaScript-based Tailwind CSS plugins directly from CSS. It accepts either a package name (e.g., `@tailwindcss/typography`) or a local file path to the plugin. This facilitates integrating existing v3.x plugins into a v4.0 setup.

```css
@plugin "@tailwindcss/typography";
```

--------------------------------

### Access Tailwind Theme Values with theme() Function (CSS)

Source: https://tailwindcss.com/docs/functions-and-directives

The `theme()` function provides a way to access Tailwind CSS theme values using dot notation within your CSS. For example, `theme(spacing.12)` retrieves the value for `spacing.12`. This function is deprecated, and the recommended approach for accessing theme values is to use CSS theme variables instead.

```css
.my-element {  margin: theme(spacing.12);}
```

--------------------------------

### Generate spacing values with --spacing() function

Source: https://tailwindcss.com/docs/functions-and-directives

Use the --spacing() function to generate spacing values based on your theme configuration. This function is useful in arbitrary values and calc() expressions for dynamic spacing calculations.

```CSS
.my-element {
  margin: --spacing(4);
}
```

```CSS
.my-element {
  margin: calc(var(--spacing) * 4);
}
```

```HTML
<div class="py-[calc(--spacing(4)-1px)]">
  <!-- ... -->
</div>
```

--------------------------------

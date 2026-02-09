### Use CSS Custom Property for Border Spacing in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/border-spacing

This HTML example illustrates the use of a CSS custom property for border spacing via the `border-spacing-(<custom-property>)` syntax. This is a convenient shorthand for `border-spacing-[var(<custom-property>)]`, enabling dynamic spacing control.

```html
<table class="border-spacing-(--my-border-spacing) ...">  <!-- ... --></table>
```

--------------------------------

### Apply Basic Border Spacing to HTML Tables with Tailwind CSS

Source: https://tailwindcss.com/docs/border-spacing

This HTML example demonstrates applying `border-spacing-<number>` utilities like `border-spacing-2` to control the space between table cell borders. It requires the `border-separate` class on the table to take effect, along with standard border classes for visibility.

```html
<table class="border-separate border-spacing-2 border border-gray-400 dark:border-gray-500">  <thead>    <tr>      <th class="border border-gray-300 dark:border-gray-600">State</th>      <th class="border border-gray-300 dark:border-gray-600">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Indiana</td>      <td class="border border-gray-300 dark:border-gray-700">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Ohio</td>      <td class="border border-gray-300 dark:border-gray-700">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Michigan</td>      <td class="border border-gray-300 dark:border-gray-700">Detroit</td>    </tr>  </tbody></table>
```

--------------------------------

### Customize Tailwind CSS Spacing Theme Variable for Border Spacing

Source: https://tailwindcss.com/docs/border-spacing

This CSS example shows how to customize the `--spacing` theme variable within a `@theme` block. Modifying this variable affects all `border-spacing-<number>` utilities, allowing for global adjustment of the spacing scale in your Tailwind CSS configuration.

```css
@theme {
  --spacing: 1px;
}
```

--------------------------------

### Apply Responsive Border Spacing in HTML with Tailwind CSS

Source: https://tailwindcss.com/docs/border-spacing

This HTML snippet demonstrates how to implement responsive border spacing using Tailwind CSS breakpoint variants. By prefixing utilities like `md:border-spacing-4`, different spacing values can be applied based on screen size, ensuring adaptability across devices.

```html
<table class="border-spacing-2 md:border-spacing-4 ...">  <!-- ... --></table>
```

--------------------------------

### Apply Tailwind CSS `appearance` Utilities Responsively

Source: https://tailwindcss.com/docs/appearance

This example demonstrates how to apply `appearance` utilities conditionally based on screen size using responsive variants. By prefixing `appearance-none` with `md:`, the default styling is removed only on medium screens and above, while `appearance-auto` is applied by default.

```html
<select class="appearance-auto md:appearance-none ...">  <!-- ... --></select>
```

--------------------------------

### Remove Default Browser Styling with Tailwind CSS `appearance-none`

Source: https://tailwindcss.com/docs/appearance

This example demonstrates how to use the `appearance-none` utility class in Tailwind CSS to reset the default browser-specific styling on HTML form elements like `<select>`. It is commonly used when creating custom form components to provide a consistent look across different browsers.

```html
<select>  <option>Yes</option>  <option>No</option>  <option>Maybe</option></select><div class="grid">  <select class="col-start-1 row-start-1 appearance-none bg-gray-50 dark:bg-gray-800 ...">    <option>Yes</option>    <option>No</option>    <option>Maybe</option>  </select>  <svg class="pointer-events-none col-start-1 row-start-1 ...">    <!-- ... -->  </svg></div>
```

--------------------------------

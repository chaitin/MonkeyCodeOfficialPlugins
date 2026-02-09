### Apply Responsive Visibility with Tailwind CSS Breakpoints

Source: https://tailwindcss.com/docs/visibility

This HTML example demonstrates how to apply responsive visibility using Tailwind CSS breakpoint variants. The element is `visible` by default, but the `md:invisible` class makes it invisible on medium (md) screen sizes and above, allowing for adaptive layouts based on screen dimensions.

```html
<div class="visible md:invisible ...">  <!-- ... --></div>
```

--------------------------------

### Collapse Table Row with Tailwind CSS `collapse` Utility

Source: https://tailwindcss.com/docs/visibility

This HTML table example shows how to use the `collapse` utility class to hide a table row (`<tr>`) or column. Unlike `display: none`, `collapse` hides the element without impacting the layout or size of other table rows and columns, making it suitable for dynamically toggling table visibility.

```html
<table>  <thead>    <tr>      <th>Invoice #</th>      <th>Client</th>      <th>Amount</th>    </tr>  </thead>  <tbody>    <tr>      <td>#100</td>      <td>Pendant Publishing</td>      <td>$2,000.00</td>    </tr>    <tr class="collapse">      <td>#101</td>      <td>Kruger Industrial Smoothing</td>      <td>$545.00</td>    </tr>    <tr>      <td>#102</td>      <td>J. Peterman</td>      <td>$10,000.25</td>    </tr>  </tbody></table>
```

--------------------------------

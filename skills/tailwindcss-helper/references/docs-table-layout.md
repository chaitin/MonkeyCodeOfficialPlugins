### Apply automatic table column sizing with Tailwind CSS `table-auto`

Source: https://tailwindcss.com/docs/table-layout

This example demonstrates how to use the `table-auto` utility class in Tailwind CSS to automatically size table columns based on their content. This is useful for tables where column widths should adapt dynamically to the data.

```html
<table class="table-auto">  <thead>    <tr>      <th>Song</th>      <th>Artist</th>      <th>Year</th>    </tr>  </thead>  <tbody>    <tr>      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>      <td>Malcolm Lockyer</td>      <td>1961</td>    </tr>    <tr>      <td>Witchy Woman</td>      <td>The Eagles</td>      <td>1972</td>    </tr>    <tr>      <td>Shining Star</td>      <td>Earth, Wind, and Fire</td>      <td>1975</td>    </tr>  </tbody></table>
```

--------------------------------

### Apply responsive table layout with Tailwind CSS breakpoints

Source: https://tailwindcss.com/docs/table-layout

This example illustrates how to apply `table-layout` utilities conditionally based on screen size using Tailwind CSS responsive variants. The `md:table-fixed` class ensures the table layout becomes fixed on medium screens and larger, while remaining `table-auto` by default.

```html
<div class="table-auto md:table-fixed ...">  <!-- ... --></div>
```

--------------------------------

### Apply fixed table column widths with Tailwind CSS `table-fixed`

Source: https://tailwindcss.com/docs/table-layout

This example shows how to use the `table-fixed` utility class in Tailwind CSS to enforce fixed column widths, ignoring cell content. This is useful for maintaining consistent table layouts, especially when combined with explicit column width settings.

```html
<table class="table-fixed">  <thead>    <tr>      <th>Song</th>      <th>Artist</th>      <th>Year</th>    </tr>  </thead>  <tbody>    <tr>      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>      <td>Malcolm Lockyer</td>      <td>1961</td>    </tr>    <tr>      <td>Witchy Woman</td>      <td>The Eagles</td>      <td>1972</td>    </tr>    <tr>      <td>Shining Star</td>      <td>Earth, Wind, and Fire</td>      <td>1975</td>    </tr>  </tbody></table>
```

--------------------------------

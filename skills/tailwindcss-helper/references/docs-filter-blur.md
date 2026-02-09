### Apply responsive blur filters in Tailwind CSS

Source: https://tailwindcss.com/docs/filter-blur

Use breakpoint prefixes like md: to apply blur utilities conditionally at specific screen sizes. This example applies no blur by default and blur-lg on medium screens and above, enabling responsive design patterns.

```html
<img class="blur-none md:blur-lg ..." src="/img/mountains.jpg" />
```

--------------------------------

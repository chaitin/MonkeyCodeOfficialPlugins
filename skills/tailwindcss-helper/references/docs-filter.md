### Apply responsive filter utilities with breakpoints

Source: https://tailwindcss.com/docs/filter

Shows how to use breakpoint variants like md: to apply filter utilities only at specific screen sizes. This example applies blur-sm at small sizes and removes filters at medium breakpoints and above.

```html
<img class="blur-sm md:filter-none ..." src="/img/mountains.jpg" />
```

--------------------------------

### Remove all filters with filter-none utility

Source: https://tailwindcss.com/docs/filter

Shows how to use the filter-none utility to remove all filters applied to an element. This example demonstrates removing filters at medium breakpoints and above using the md: responsive variant.

```html
<img class="blur-md brightness-150 invert md:filter-none" src="/img/mountains.jpg" />
```

--------------------------------

### Apply filter utilities on hover state

Source: https://tailwindcss.com/docs/filter

Demonstrates using the hover: variant prefix with filter utilities to conditionally apply filters only when an element is hovered. This example removes filters on hover using the hover:filter-none utility.

```html
<img class="blur-sm hover:filter-none ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply custom CSS variable filters

Source: https://tailwindcss.com/docs/filter

Shows how to use the filter-(<custom-property>) syntax as shorthand for filter-[var(<custom-property>)] to reference CSS custom properties. The syntax automatically wraps the custom property in the var() function.

```html
<img class="filter-(--my-filter) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply blur and grayscale filters with Tailwind CSS

Source: https://tailwindcss.com/docs/filter

Demonstrates how to use Tailwind filter utilities like blur-xs and grayscale to apply visual effects to images. Multiple filter utilities can be combined on a single element to create complex visual effects.

```html
<img class="blur-xs" src="/img/mountains.jpg" />
<img class="grayscale" src="/img/mountains.jpg" />
<img class="blur-xs grayscale" src="/img/mountains.jpg" />
```

--------------------------------

### Apply custom filter values with bracket notation

Source: https://tailwindcss.com/docs/filter

Demonstrates using the filter-[<value>] syntax to apply completely custom filter values, such as SVG filter references. This allows for advanced filtering beyond the predefined Tailwind utilities.

```html
<img class="filter-[url('filters.svg#filter-id')] ..." src="/img/mountains.jpg" />
```

--------------------------------

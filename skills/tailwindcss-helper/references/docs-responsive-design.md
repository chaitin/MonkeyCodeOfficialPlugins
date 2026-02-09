### Apply Responsive Utility Variants with Breakpoint Prefixes

Source: https://tailwindcss.com/docs/responsive-design

Demonstrates how to use breakpoint prefixes (sm:, md:, lg:, xl:, 2xl:) to conditionally apply utility classes at different screen sizes. The example shows an image element that changes width based on breakpoint: 16 units by default, 32 on medium screens, and 48 on large screens.

```html
<!-- Width of 16 by default, 32 on medium screens, and 48 on large screens -->
<img class="w-16 md:w-32 lg:w-48" src="..." />
```

--------------------------------

### Build Responsive Marketing Component with Tailwind CSS

Source: https://tailwindcss.com/docs/responsive-design

Complete example of a responsive marketing card component that uses a stacked layout on small screens and a side-by-side flex layout on medium screens and larger. Demonstrates mobile-first approach with unprefixed utilities and responsive prefixes for layout changes, image sizing, and text styling.

```html
<div class="mx-auto max-w-md overflow-hidden rounded-xl bg-white shadow-md md:max-w-2xl">
  <div class="md:flex">
    <div class="md:shrink-0">
      <img
        class="h-48 w-full object-cover md:h-full md:w-48"
        src="/img/building.jpg"
        alt="Modern building architecture"
      />
    </div>
    <div class="p-8">
      <div class="text-sm font-semibold tracking-wide text-indigo-500 uppercase">Company retreats</div>
      <a href="#" class="mt-1 block text-lg leading-tight font-medium text-black hover:underline">
        Incredible accommodation for your team
      </a>
      <p class="mt-2 text-gray-500">
        Looking to take your team away on a retreat to enjoy awesome food and take in some sunshine? We have a list of
        places to do just that.
      </p>
    </div>
  </div>
</div>
```

--------------------------------

### Apply Tailwind CSS utilities at a single breakpoint

Source: https://tailwindcss.com/docs/responsive-design

This HTML example shows how to target a single breakpoint by combining a responsive variant with the `max-*` variant of the *next* breakpoint. For instance, `md:max-lg:flex` will apply the `flex` utility only at the `md` breakpoint, before `lg` takes effect.

```html
<div class="md:max-lg:flex">  <!-- ... --></div>
```

--------------------------------

### Implement basic Tailwind CSS container queries

Source: https://tailwindcss.com/docs/responsive-design

This HTML example shows how to use Tailwind CSS container queries. Mark a parent element with `@container` to make it a query container, then apply responsive styles to its children using variants like `@md` based on the container's width, not the viewport.

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Correct Mobile-First Responsive Styling Pattern

Source: https://tailwindcss.com/docs/responsive-design

Demonstrates the correct mobile-first approach in Tailwind CSS. Use unprefixed utilities to target mobile devices, then override them at larger breakpoints using responsive prefixes. This example centers text on mobile and left-aligns it on screens 640px and wider.

```html
<!-- This will center text on mobile, and left align it on screens 640px and wider -->
<div class="text-center sm:text-left"></div>
```

--------------------------------

### Apply custom Tailwind CSS breakpoints in HTML

Source: https://tailwindcss.com/docs/responsive-design

After defining custom breakpoints in your Tailwind CSS theme, this HTML example demonstrates how to use them as utility prefixes (e.g., `xs:grid-cols-2`, `3xl:grid-cols-6`) directly in your markup to apply styles at those custom sizes.

```html
<div class="grid xs:grid-cols-2 3xl:grid-cols-6">  <!-- ... --></div>
```

--------------------------------

### Remove all default Tailwind CSS breakpoints and define custom ones

Source: https://tailwindcss.com/docs/responsive-design

This CSS example demonstrates how to completely reset all default Tailwind CSS breakpoints using `--breakpoint-*: initial` and then define a new, custom set of breakpoints from scratch. This provides full control over your project's responsive breakpoints.

```css
@import "tailwindcss";@theme {  --breakpoint-*: initial;  --breakpoint-tablet: 40rem;  --breakpoint-laptop: 64rem;  --breakpoint-desktop: 80rem;}
```

--------------------------------

### Target specific ranges with Tailwind CSS container queries

Source: https://tailwindcss.com/docs/responsive-design

This HTML example illustrates how to target a specific range for container queries by stacking a regular container query variant with a max-width variant (e.g., `@sm:@max-md`). This applies styles only when the container's width falls within the defined range.

```html
<div class="@container">
  <div class="flex flex-row @sm:@max-md:flex-col">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Incorrect Mobile-First Responsive Styling Pattern

Source: https://tailwindcss.com/docs/responsive-design

Demonstrates the incorrect approach when targeting mobile screens in Tailwind CSS. Using sm: prefix will only apply styles at 640px and wider, not on small screens. This example shows text-center being applied only on medium screens and above, missing mobile styling.

```html
<!-- This will only center text on screens 640px and wider, not on small screens -->
<div class="sm:text-center"></div>
```

--------------------------------

### Apply Arbitrary Container Query Values in HTML

Source: https://tailwindcss.com/docs/responsive-design

This HTML snippet illustrates the use of arbitrary values for container queries in Tailwind CSS. It allows developers to define one-off container query breakpoints, such as `@min-[475px]`, directly within the HTML class attribute without modifying the theme configuration. This is useful for specific responsive adjustments that don't warrant a global theme addition.

```html
<div class="@container">  <div class="flex flex-col @min-[475px]:flex-row">    <!-- ... -->  </div></div>
```

--------------------------------

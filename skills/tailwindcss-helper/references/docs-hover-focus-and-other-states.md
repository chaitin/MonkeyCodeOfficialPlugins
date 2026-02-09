### Apply Styles for Element Initial Render or Display Transition (Tailwind CSS HTML)

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example uses the `starting` variant to define the initial appearance of an element when it is first rendered in the DOM or transitions from `display: none` to visible. This is particularly useful for smooth entry animations or transitions.

```html
<div>
  <button popovertarget="my-popover">Check for updates</button>
  <div popover id="my-popover" class="opacity-0 starting:open:opacity-0 ...">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Style Popovers in Open State

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use the open variant with the :popover-open pseudo-class to conditionally style popover elements. This example changes opacity from 0 to 100 when the popover is opened.

```html
<div>
  <button popovertarget="my-popover">Open Popover</button>
  <div popover id="my-popover" class="opacity-0 open:opacity-100 ...">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Applying Tailwind CSS Arbitrary Variants with Space Selectors

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Demonstrates how to use underscores in arbitrary variants to represent spaces in CSS selectors, allowing for targeting descendant elements. This example applies a top margin to all `p` elements within the parent element where the class is applied.

```html
<div class="[&_p]:mt-4">
  <p>Lorem ipsum...</p>
  <ul>
    <li>
      <p>Lorem ipsum...</p>
    </li>
    <!-- ... -->
  </ul>
</div>
```

--------------------------------

### Conditional Styling for Print Media (Tailwind CSS HTML)

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example demonstrates the `print` variant, which applies styles exclusively when the document is being printed. It allows for hiding elements from printouts or displaying print-specific content.

```html
<div>
  <article class="print:hidden">
    <h1>My Secret Pizza Recipe</h1>
    <p>This recipe is a secret, and must not be shared with anyone</p>
    <!-- ... -->
  </article>
  <div class="hidden print:block">Are you seriously trying to print this? It's secret!</div>
</div>
```

--------------------------------

### Use Custom Data Variants in HTML

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Apply custom data-* variants created in your configuration to conditionally style elements. This example uses the data-checked variant to underline elements with matching data-ui attributes.

```html
<div data-ui="checked active" class="data-checked:underline">
  <!-- ... -->
</div>
```

--------------------------------

### Create visual effects with ::before pseudo-element

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use the `before` variant to create decorative background effects behind text. This example creates a skewed pink background behind the word 'annoyed' in a blockquote using absolute positioning and transform utilities.

```html
<blockquote class="text-center text-2xl font-semibold text-gray-900 italic dark:text-white">
  When you look
  <span class="relative inline-block before:absolute before:-inset-1 before:block before:-skew-y-3 before:bg-pink-500">
    <span class="relative text-white dark:text-gray-950">annoyed</span>
  </span>
  all the time, people think that you're busy.
</blockquote>
```

--------------------------------

### Stacking Tailwind CSS Arbitrary and Built-in Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Shows that arbitrary variants can be combined with built-in Tailwind CSS variants or other arbitrary variants for complex conditional styling. This example applies a `cursor-grabbing` style when an element with `is-dragging` is also in an active state.

```html
<ul role="list">
  {#each items as item}
    <li class="[&.is-dragging]:active:cursor-grabbing">{item}</li>
  {/each}
</ul>
```

--------------------------------

### Style Details Elements in Open State

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use the open variant to conditionally apply styles when a <details> or <dialog> element is in an open state. This example applies border and background styles when the details element is open.

```html
<details class="border border-transparent open:border-black/10 open:bg-gray-100 ..." open>
  <summary class="text-sm leading-6 font-semibold text-gray-900 select-none">Why do they call it Ovaltine?</summary>
  <div class="mt-3 text-sm leading-6 text-gray-600">
    <p>The mug is round. The jar is round. They should call it Roundtine.</p>
  </div>
</details>
```

--------------------------------

### Style Elements Based on Data Attribute Existence

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use the data-* variant to apply styles when a data attribute exists, regardless of its value. This example applies a purple border when the data-active attribute is present on an element.

```html
<!-- Will apply -->
<div data-active class="border border-gray-300 data-active:border-purple-500">
  <!-- ... -->
</div>
<!-- Will not apply -->
<div class="border border-gray-300 data-active:border-purple-500">
  <!-- ... -->
</div>
```

--------------------------------

### Replace pseudo-elements with real HTML elements for simplicity

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use actual HTML elements instead of ::before and ::after pseudo-elements for better readability and less code. This example achieves the same visual effect as the pseudo-element version but with explicit span elements.

```html
<blockquote class="text-center text-2xl font-semibold text-gray-900 italic">
  When you look
  <span class="relative">
    <span class="absolute -inset-1 block -skew-y-3 bg-pink-500" aria-hidden="true"></span>
    <span class="relative text-white">annoyed</span>
  </span>
  all the time, people think that you're busy.
</blockquote>
```

--------------------------------

### Style ::before and ::after pseudo-elements

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use `before` and `after` variants to style pseudo-elements. Tailwind automatically adds `content: ''` by default. This example shows adding a required asterisk to a label using the `after` variant with custom content.

```html
<label>
  <span class="text-gray-700 after:ml-0.5 after:text-red-500 after:content-['*'] ...">
    Email
  </span>
  <input type="email" name="email" class="..." placeholder="you@example.com" />
</label>
```

--------------------------------

### Style Elements Based on Data Attribute Values

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use arbitrary data-* variants with square brackets to apply styles based on specific data attribute values. This example applies padding-8 only when data-size equals 'large'.

```html
<!-- Will apply -->
<div data-size="large" class="data-[size=large]:p-8">
  <!-- ... -->
</div>
<!-- Will not apply -->
<div data-size="medium" class="data-[size=large]:p-8">
  <!-- ... -->
</div>
```

--------------------------------

### Apply Styles Based on CSS Property Support Shorthand (Tailwind CSS HTML)

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example demonstrates a shorthand for the `supports-[...]` variant, where only the CSS property name is specified to check for its support. This is useful for applying styles like `backdrop-filter` only when the browser supports it, providing a fallback otherwise.

```html
<div class="bg-black/75 supports-backdrop-filter:bg-black/25 supports-backdrop-filter:backdrop-blur ...">
  <!-- ... -->
</div>
```

--------------------------------

### Create Custom Data Attribute Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Define custom data-* variants in your Tailwind CSS configuration for frequently used data attributes. This example creates a data-checked variant that targets elements with data-ui containing 'checked'.

```css
@import "tailwindcss";
@custom-variant data-checked (&[data-ui~="checked"]);
```

--------------------------------

### Use Arbitrary ARIA Variants with Square Brackets

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Generate one-off ARIA variants on the fly using square bracket notation for complex ARIA attributes with specific values. This example applies different background images to table headers based on aria-sort values.

```html
<table>
  <thead>
    <tr>
      <th aria-sort="ascending" class="aria-[sort=ascending]:bg-[url('/img/down-arrow.svg')] aria-[sort=descending]:bg-[url('/img/up-arrow.svg')]">
        Invoice #
      </th>
      <!-- ... -->
    </tr>
  </thead>
  <!-- ... -->
</table>
```

--------------------------------

### Apply Container Queries with Tailwind CSS `@md` Variant

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example illustrates how to use container queries in Tailwind CSS with variants like `@md` to style elements based on the width of their parent container, rather than the viewport. It shows how to change flex direction based on container width.

```html
<div class="@container">  <div class="flex flex-col @md:flex-row">    <!-- ... -->  </div></div>
```

--------------------------------

### Apply Directional Styles with RTL and LTR Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use rtl and ltr variants to conditionally apply styles for right-to-left and left-to-right layouts. This example applies left margin in LTR mode and right margin in RTL mode for multi-directional layouts.

```html
<div class="group flex items-center">
  <img class="h-12 w-12 shrink-0 rounded-full" src="..." alt="" />
  <div class="ltr:ml-3 rtl:mr-3">
    <p class="text-gray-700 group-hover:text-gray-900 ...">...</p>
    <p class="text-gray-500 group-hover:text-gray-700 ...">...</p>
  </div>
</div>
```

--------------------------------

### Style Dialog Backdrops with Tailwind CSS `backdrop` Variant

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example illustrates how to style the backdrop of a native `<dialog>` element using the `backdrop` variant in Tailwind CSS. It applies a background color to the overlay that appears behind an behind an open dialog.

```html
<dialog class="backdrop:bg-gray-50">  <form method="dialog">    <!-- ... -->  </form></dialog>
```

--------------------------------

### Using Tailwind CSS Arbitrary Variants for Custom Selectors

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Explains how to use arbitrary variants in Tailwind CSS to apply custom selector logic directly in HTML. This example changes the cursor to `grabbing` when an element has the `is-dragging` class, providing highly specific conditional styling.

```html
<ul role="list">
  {#each items as item}
    <li class="[&.is-dragging]:cursor-grabbing">{item}</li>
  {/each}
</ul>
```

--------------------------------

### Differentiate multiple peers with named peer variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use `peer/{name}` class to give peers unique names and style based on specific peer state using `peer-{state}/{name}` variants. This example demonstrates a radio button group where different content blocks display based on which radio option is selected.

```html
<fieldset>
  <legend>Published status</legend>
  <input id="draft" class="peer/draft" type="radio" name="status" checked />
  <label for="draft" class="peer-checked/draft:text-sky-500">Draft</label>
  <input id="published" class="peer/published" type="radio" name="status" />
  <label for="published" class="peer-checked/published:text-sky-500">Published</label>
  <div class="hidden peer-checked/draft:block">Drafts are only visible to administrators.</div>
  <div class="hidden peer-checked/published:block">Your post will be publicly visible on your site.</div>
</fieldset>
```

--------------------------------

### Target Parent Elements with Group ARIA Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use group-aria-* variants to style child elements based on ARIA attributes of their parent. This example rotates an SVG icon based on the parent th element's aria-sort attribute.

```html
<table>
  <thead>
    <tr>
      <th aria-sort="ascending" class="group">
        Invoice #
        <svg class="group-aria-[sort=ascending]:rotate-0 group-aria-[sort=descending]:rotate-180"><!-- ... --></svg>
      </th>
      <!-- ... -->
    </tr>
  </thead>
  <!-- ... -->
</table>
```

--------------------------------

### Apply Tailwind CSS `odd` and `even` variants to table rows

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example illustrates how to use the `odd:` and `even:` variants to apply alternating background colors to table rows, improving readability. It includes support for dark mode by defining separate `dark:odd:` and `dark:even:` styles, making it easy to create visually distinct rows without manual conditional logic.

```html
<table>  <!-- ... -->  <tbody>    {#each people as person}      <!-- Use different background colors for odd and even rows -->      <tr class="odd:bg-white even:bg-gray-50 dark:odd:bg-gray-900/50 dark:even:bg-gray-950">        <td>{person.name}</td>        <td>{person.title}</td>        <td>{person.email}</td>      </tr>    {/each}  </tbody></table>
```

--------------------------------

### Style File Input Buttons with Tailwind CSS `file` Variant

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example shows how to customize the appearance of the 'Choose File' button within an `<input type="file">` element using the `file` variant in Tailwind CSS. It applies styling for margin, border, background, padding, font, and hover states.

```html
<input type="file" class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500 ..."/>
```

--------------------------------

### Create Custom ARIA Variants in Tailwind CSS

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Define custom ARIA variants for non-standard or complex ARIA attributes using @custom-variant. This example creates variants for aria-sort with ascending and descending values to style table headers based on sort direction.

```css
@custom-variant aria-asc (&[aria-sort="ascending"]);
@custom-variant aria-desc (&[aria-sort="descending"]);
```

--------------------------------

### Tailwind CSS Special State Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Variants for styling special element states including inert (non-interactive), has-[] (parent selector), in-[] (ancestor selector), open (popover/details), supports-[] (CSS feature queries), and starting-style (starting animation state).

```css
/* Inert state */
&:is([inert], [inert] *)

/* Has selector */
&:has(...)

/* In selector (ancestor) */
:where(...) &

/* Open state (popover/details) */
&:is([open], :popover-open, :open)

/* CSS supports query */
@supports (…)

/* Starting style */
@starting-style
```

--------------------------------

### Conditional Styling Based on Viewport Orientation (Tailwind CSS HTML)

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example illustrates using `portrait` and `landscape` variants to apply different styles based on the viewport's orientation. It can be used to hide content or display messages prompting users to rotate their device for an optimal experience.

```html
<div>
  <div class="portrait:hidden">
    <!-- ... -->
  </div>
  <div class="landscape:hidden">
    <p>This experience is designed to be viewed in landscape. Please rotate your device to view the site.</p>
  </div>
</div>
```

--------------------------------

### Style Active Text Selection with Tailwind CSS `selection` Variant

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example demonstrates how to customize the background and text color of actively selected text using the `selection` variant in Tailwind CSS. The `selection` variant is inheritable and can be applied to parent elements or even the `<body>` for site-wide consistency.

```html
<div class="selection:bg-fuchsia-300 selection:text-fuchsia-900">  <p>    So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my    way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all    living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.  </p></div>
```

```html
<html>  <head>    <!-- ... -->  </head>  <body class="selection:bg-pink-300">    <!-- ... -->  </body></html>
```

--------------------------------

### Style element based on sibling state with peer variant

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Mark a sibling element with the `peer` class and use `peer-*` variants to style target elements based on sibling state. This example shows an email input with validation feedback that appears when the input is invalid, enabling patterns like floating labels without JavaScript.

```html
<form>
  <label class="block">
    <span class="...">Email</span>
    <input type="email" class="peer ..." />
    <p class="invisible peer-invalid:visible ...">Please provide a valid email address.</p>
  </label>
</form>
```

--------------------------------

### Apply Tailwind CSS `disabled` and `invalid` variants to form inputs

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example showcases how to style form input elements based on their state using `invalid:`, `focus:`, and `disabled:` variants. It provides visual feedback for validation errors, focus states, and disabled inputs, enhancing user experience and reducing the need for complex JavaScript-based styling logic.

```html
<input  type="text"  value="tbone"  disabled  class="invalid:border-pink-500 invalid:text-pink-600 focus:border-sky-500 focus:outline focus:outline-sky-500 focus:invalid:border-pink-500 focus:invalid:outline-pink-500 disabled:border-gray-200 disabled:bg-gray-50 disabled:text-gray-500 disabled:shadow-none dark:disabled:border-gray-700 dark:disabled:bg-gray-800/20 ..."/>
```

--------------------------------

### Create arbitrary peer variants with custom selectors

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Use `peer-[selector]` syntax to create one-off peer variants with custom CSS selectors. The `&` character marks where `.peer` should be positioned in the final selector for precise control over the CSS combinator.

```html
<form>
  <label for="email">Email:</label>
  <input id="email" name="email" type="email" class="is-dirty peer" required />
  <div class="peer-[.is-dirty]:peer-required:block hidden">This field is required.</div>
</form>
```

```html
<div>
  <input type="text" class="peer" />
  <div class="hidden peer-[:nth-of-type(3)_&]:block">
    <!-- ... -->
  </div>
</div>
```

--------------------------------

### Apply Tailwind CSS `group-has-*` variant for styling based on descendant state

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This example illustrates the `group-has-*` variant, which allows styling an element within a `group` based on the state or content of a descendant element. Here, an SVG icon is conditionally displayed (`group-has-[a]:block`) if the parent `div` (marked with `group`) contains an `<a>` tag descendant, enabling complex conditional styling within component groups.

```html
<div class="group ...">  <img src="..." />  <h4>Spencer Sharp</h4>  <svg class="hidden group-has-[a]:block ..."><!-- ... --></svg>  <p>Product Designer at <a href="...">planeteria.tech</a></p></div>
```

--------------------------------

### Style interactive states with hover, focus, and active variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Shows how to use hover, focus, and active variants together to style different interactive states. Includes focus outline styling with offset and color customization.

```html
<button class="bg-violet-500 hover:bg-violet-600 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500 active:bg-violet-700 ...">
  Save changes
</button>
```

--------------------------------

### Using Tailwind CSS Arbitrary Variants for At-Rules

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Illustrates the use of arbitrary variants to embed CSS at-rules like `@media` or `@supports` directly in HTML. This enables conditional styling based on browser feature support or media queries, providing flexible responsive designs.

```html
<div class="flex [@supports(display:grid)]:grid">
  <!-- ... -->
</div>
```

--------------------------------

### Apply Responsive Grid Layouts with Tailwind CSS Breakpoints

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This snippet demonstrates how to create responsive grid layouts using Tailwind CSS's built-in responsive variants like `md` and `lg`. It shows how to define different column counts for mobile, medium, and large screen sizes.

```html
<div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6">  <!-- ... --></div>
```

--------------------------------

### Apply Styles Based on Pointing Device Accuracy (Tailwind CSS HTML)

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

This snippet demonstrates how to use `pointer-coarse` to apply styles specifically for less accurate pointing devices, such as touchscreens. This is useful for increasing target sizes on touch-enabled devices to improve usability.

```html
<fieldset aria-label="Choose a memory option">
  <div class="flex items-center justify-between">
    <div>RAM</div>
    <a href="#"> See performance specs </a>
  </div>
  <div class="mt-4 grid grid-cols-6 gap-2 pointer-coarse:mt-6 pointer-coarse:grid-cols-3 pointer-coarse:gap-4">
    <label class="p-2 pointer-coarse:p-4 ...">
      <input type="radio" name="memory-option" value="4 GB" className="sr-only" />
      <span>4 GB</span>
    </label>
    <!-- ... -->
  </div>
</fieldset>
```

--------------------------------

### Tailwind CSS Container Query Variants

Source: https://tailwindcss.com/docs/hover-focus-and-other-states

Variants for styling elements based on container width using container queries. Includes predefined container sizes (@3xs through @7xl) and custom container queries using @min-[] and @max-[] syntax for responsive container-based layouts.

```css
/* 3XS container (16rem and up) */
@container (width >= 16rem)

/* 2XS container (18rem and up) */
@container (width >= 18rem)

/* XS container (20rem and up) */
@container (width >= 20rem)

/* Small container (24rem and up) */
@container (width >= 24rem)

/* Medium container (28rem and up) */
@container (width >= 28rem)

/* Large container (32rem and up) */
@container (width >= 32rem)

/* XL container (36rem and up) */
@container (width >= 36rem)

/* 2XL container (42rem and up) */
@container (width >= 42rem)

/* 3XL container (48rem and up) */
@container (width >= 48rem)

/* 4XL container (56rem and up) */
@container (width >= 56rem)

/* 5XL container (64rem and up) */
@container (width >= 64rem)

/* 6XL container (72rem and up) */
@container (width >= 72rem)

/* 7XL container (80rem and up) */
@container (width >= 80rem)

/* Custom minimum container query */
@container (width >= ...)

/* Max 3XS container (below 16rem) */
@container (width < 16rem)

/* Max 2XS container (below 18rem) */
@container (width < 18rem)

/* Max XS container (below 20rem) */
@container (width < 20rem)

/* Max small container (below 24rem) */
@container (width < 24rem)

/* Max medium container (below 28rem) */
@container (width < 28rem)

/* Max large container (below 32rem) */
@container (width < 32rem)

/* Max XL container (below 36rem) */
@container (width < 36rem)

/* Max 2XL container (below 42rem) */
@container (width < 42rem)

/* Max 3XL container (below 48rem) */
@container (width < 48rem)

/* Max 4XL container (below 56rem) */
@container (width < 56rem)

/* Max 5XL container (below 64rem) */
@container (width < 64rem)

/* Max 6XL container (below 72rem) */
@container (width < 72rem)

/* Max 7XL container (below 80rem) */
@container (width < 80rem)

/* Custom maximum container query */
@container (width < ...)
```

--------------------------------

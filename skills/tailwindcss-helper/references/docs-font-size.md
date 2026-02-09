### Set font-size with line-height modifiers in HTML

Source: https://tailwindcss.com/docs/font-size

Combine font-size utilities with line-height modifiers using the syntax text-[size]/[line-height] to control both properties simultaneously. For example, text-sm/6, text-sm/7, and text-sm/8 set different line-height values for the same font size.

```html
<p class="text-sm/6 ...">So I started to walk into the water...</p>
<p class="text-sm/7 ...">So I started to walk into the water...</p>
<p class="text-sm/8 ...">So I started to walk into the water...</p>
```

--------------------------------

### Define Custom Font Size Utility in Tailwind CSS Theme

Source: https://tailwindcss.com/docs/font-size

These CSS snippets demonstrate how to define a custom font size utility, `--text-tiny`, within the Tailwind CSS `@theme` directive. The first example shows a basic font size definition, while the second extends it to include `line-height`, `letter-spacing`, and `font-weight` for comprehensive styling. This allows for consistent and reusable typography across your project.

```css
@theme {  --text-tiny: 0.625rem; }
```

```css
@theme {  --text-tiny: 0.625rem;  --text-tiny--line-height: 1.5rem;   --text-tiny--letter-spacing: 0.125rem;   --text-tiny--font-weight: 500; }
```

--------------------------------

### Apply responsive font-size utilities in HTML

Source: https://tailwindcss.com/docs/font-size

Use breakpoint prefixes like md:, lg:, etc. to apply font-size utilities at specific screen sizes. This enables responsive typography that adapts to different viewport widths.

```html
<p class="text-sm md:text-base ...">Lorem ipsum dolor sit amet...</p>
```

--------------------------------

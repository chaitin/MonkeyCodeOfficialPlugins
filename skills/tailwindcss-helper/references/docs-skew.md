### Responsive skew transform with breakpoint variants

Source: https://tailwindcss.com/docs/skew

Apply skew utilities conditionally at different screen sizes using breakpoint prefixes like md:. Allows base skew value to change at medium breakpoint and above, enabling responsive design patterns.

```html
<img class="skew-3 md:skew-12 ..." src="/img/mountains.jpg" />
```

--------------------------------

### Basic skew transform on both axes

Source: https://tailwindcss.com/docs/skew

Apply skew transformation to both X and Y axes using predefined utility classes. The skew-<number> utilities apply skewX() and skewY() transforms with degree values. Supports positive values (skew-3, skew-6, skew-12) for standard skewing.

```html
<img class="skew-3 ..." src="/img/mountains.jpg" />
<img class="skew-6 ..." src="/img/mountains.jpg" />
<img class="skew-12 ..." src="/img/mountains.jpg" />
```

--------------------------------

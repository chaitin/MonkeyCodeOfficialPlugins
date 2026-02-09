### Apply Custom Grayscale Values and CSS Variables with Tailwind CSS

Source: https://tailwindcss.com/docs/filter-grayscale

This HTML snippet illustrates how to apply custom grayscale values using Tailwind CSS's arbitrary value syntax, such as `grayscale-[0.5]`. It also demonstrates using CSS variables with the `grayscale-(<custom-property>)` syntax for dynamic control over the grayscale effect. This provides flexibility beyond predefined utility classes.

```html
<img class="grayscale-[0.5] ..." src="/img/mountains.jpg" />
```

```html
<img class="grayscale-(--my-grayscale) ..." src="/img/mountains.jpg" />
```

--------------------------------

### Apply Basic Grayscale Filters to Images using Tailwind CSS

Source: https://tailwindcss.com/docs/filter-grayscale

This HTML snippet demonstrates the application of standard grayscale utility classes in Tailwind CSS to control the visual effect on images. It showcases `grayscale-0`, `grayscale-25`, `grayscale-50`, and `grayscale` to apply different levels of grayscale. These utilities directly map to `filter: grayscale()` CSS properties.

```html
<img class="grayscale-0 ..." src="/img/mountains.jpg" /><img class="grayscale-25 ..." src="/img/mountains.jpg" /><img class="grayscale-50 ..." src="/img/mountains.jpg" /><img class="grayscale ..." src="/img/mountains.jpg" />
```

--------------------------------

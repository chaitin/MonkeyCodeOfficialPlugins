### Restoring forced colors with Tailwind CSS

Source: https://tailwindcss.com/docs/forced-color-adjust

This example illustrates how to use the `forced-color-adjust-auto` utility class in HTML to make an element adhere to colors enforced by forced color modes. It also shows how to combine it with `forced-color-adjust-none` and responsive variants to conditionally apply or revert the behavior.

```html
<form>  <fieldset class="forced-color-adjust-none lg:forced-color-adjust-auto ...">    <legend>Choose a color:</legend>    <select class="hidden lg:block">      <option value="White">White</option>      <option value="Gray">Gray</option>      <option value="Black">Black</option>    </select>    <div class="lg:hidden">      <label>        <input class="sr-only" type="radio" name="color-choice" value="White" />        <!-- ... -->      </label>      <!-- ... -->    </div>  </fieldset></form>
```

--------------------------------

### Applying forced-color-adjust responsively with Tailwind CSS

Source: https://tailwindcss.com/docs/forced-color-adjust

This example demonstrates how to apply `forced-color-adjust` utilities conditionally based on screen size using responsive variants in Tailwind CSS. Here, `forced-color-adjust-none` is applied by default, and `forced-color-adjust-auto` is applied on medium screens and above.

```html
<div class="forced-color-adjust-none md:forced-color-adjust-auto ...">  <!-- ... --></div>
```

--------------------------------

### Opting out of forced colors with Tailwind CSS

Source: https://tailwindcss.com/docs/forced-color-adjust

This example demonstrates how to use the `forced-color-adjust-none` utility class in HTML to prevent an element from adhering to forced color modes. This is particularly useful for components where a limited color palette would degrade usability, such as product color choosers.

```html
<form>  <img src="/img/shirt.jpg" />  <div>    <h3>Basic Tee</h3>    <h3>$35</h3>    <fieldset>      <legend class="sr-only">Choose a color</legend>      <div class="forced-color-adjust-none ...">        <label>          <input class="sr-only" type="radio" name="color-choice" value="White" />          <span class="sr-only">White</span>          <span class="size-6 rounded-full border border-black/10 bg-white"></span>        </label>        <!-- ... -->      </div>    </fieldset>  </div></form>
```

--------------------------------

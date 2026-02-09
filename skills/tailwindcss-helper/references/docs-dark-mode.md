### Activate Tailwind CSS Dark Mode Manually with HTML Class

Source: https://tailwindcss.com/docs/dark-mode

This HTML example demonstrates how to activate dark mode styles when the `dark` variant has been overridden to respond to a `.dark` class. By adding the `dark` class to the `<html>` element, all `dark:` prefixed utilities within the document will be applied.

```html
<html class="dark">  <body>    <div class="bg-white dark:bg-black">      <!-- ... -->    </div>  </body></html>
```

--------------------------------

### Add Play CDN Script to HTML

Source: https://tailwindcss.com/docs/installation/play-cdn

Add the Tailwind CSS Play CDN script tag to the HTML head element to enable Tailwind utility classes without any build step. This method is designed for development purposes only and not recommended for production use. Allows immediate styling of content using Tailwind's utility classes.

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  </body>
</html>
```

--------------------------------

### Configure Custom Tailwind CSS Theme with Play CDN

Source: https://tailwindcss.com/docs/installation/play-cdn

Use the Play CDN with custom CSS by adding a style tag with type="text/tailwindcss" to define theme variables and custom styles. This approach supports all of Tailwind's CSS features including theme customization, allowing developers to extend the default color palette and other design tokens directly in HTML.

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style type="text/tailwindcss">
      @theme {
        --color-clifford: #da373d;
      }
    </style>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline text-clifford">
      Hello world!
    </h1>
  </body>
</html>
```

--------------------------------

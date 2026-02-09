### Use responsive white-space utility with breakpoint prefix

Source: https://tailwindcss.com/docs/white-space

Prefix a white-space utility with a breakpoint variant like md: to apply the utility only at medium screen sizes and above. This enables different whitespace behavior across responsive breakpoints.

```html
<p class="whitespace-pre md:whitespace-normal ...">  Lorem ipsum dolor sit amet...</p>
```

--------------------------------

### Apply whitespace-pre utility in HTML

Source: https://tailwindcss.com/docs/white-space

Use the whitespace-pre class to preserve newlines and spaces within an element exactly as written. Text will not wrap and requires overflow handling for long content.

```html
<p class="overflow-auto whitespace-pre">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

--------------------------------

### Apply whitespace-pre-line utility in HTML

Source: https://tailwindcss.com/docs/white-space

Use the whitespace-pre-line class to preserve newlines but collapse spaces within an element. Text wraps normally at word boundaries while maintaining line breaks.

```html
<p class="whitespace-pre-line">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

--------------------------------

### Apply whitespace-pre-wrap utility in HTML

Source: https://tailwindcss.com/docs/white-space

Use the whitespace-pre-wrap class to preserve newlines and spaces within an element while allowing normal text wrapping. Spaces and line breaks are maintained as written.

```html
<p class="whitespace-pre-wrap">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

--------------------------------

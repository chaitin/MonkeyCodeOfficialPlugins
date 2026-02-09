### Range Input with Output Value Display (HTML & JS)

Source: https://getbootstrap.com/docs/5.3/forms/range

Provides an example of displaying the current value of a range input in real-time using an `<output>` element and a small JavaScript snippet. The script updates the output text as the range value changes.

```html
<label for="range4" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="100" value="50" id="range4">
<output for="range4" id="rangeValue" aria-hidden="true"></output>

<script>
  // This is an example script, please modify as needed
  const rangeInput = document.getElementById('range4');
  const rangeOutput = document.getElementById('rangeValue');

  // Set initial value
  rangeOutput.textContent = rangeInput.value;

  rangeInput.addEventListener('input', function() {
    rangeOutput.textContent = this.value;
  });
</script>
```

--------------------------------

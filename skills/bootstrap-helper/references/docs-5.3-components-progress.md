### Bootstrap Progress Bar Basic Structure and Examples

Source: https://getbootstrap.com/docs/5.3/components/progress

Demonstrates the fundamental HTML structure for Bootstrap progress bars, including wrapper and inner elements, accessibility attributes, and various examples showing different progress values from 0% to 100%.

```html
<div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 0%"></div>
</div>
<div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 25%"></div>
</div>
<div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 50%"></div>
</div>
<div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 75%"></div>
</div>
<div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 100%"></div>
</div>
```

--------------------------------

### Bootstrap Stacked Progress Bars

Source: https://getbootstrap.com/docs/5.3/components/progress

Illustrates how to create a stacked progress bar by nesting multiple `.progress` elements within a `.progress-stacked` container. The width styling must be applied to the individual `.progress` elements in this configuration.

```html
<div class="progress-stacked">
  <div class="progress" role="progressbar" aria-label="Segment one" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100" style="width: 15%">
    <div class="progress-bar"></div>
  </div>
  <div class="progress" role="progressbar" aria-label="Segment two" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" style="width: 30%">
    <div class="progress-bar bg-success"></div>
  </div>
  <div class="progress" role="progressbar" aria-label="Segment three" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
    <div class="progress-bar bg-info"></div>
  </div>
</div>
```

--------------------------------

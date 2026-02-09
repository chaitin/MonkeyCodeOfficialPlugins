### Bootstrap Position Utility Examples

Source: https://getbootstrap.com/docs/5.3/utilities/position

Demonstrates how to use Bootstrap's position utility classes to create visually distinct components such as mail counts, markers with icons, and alert badges. These examples showcase the flexibility of positioning elements relative to their parent containers.

```html
<button type="button" class="btn btn-primary position-relative">
  Mails <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill text-bg-secondary">+99 <span class="visually-hidden">unread messages</span></span>
</button>

<div class="position-relative py-2 px-4 text-bg-secondary border border-secondary rounded-pill">
  Marker <svg width="1em" height="1em" viewBox="0 0 16 16" class="position-absolute top-100 start-50 translate-middle mt-1" fill="var(--bs-secondary)" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M7.247 11.14L2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/></svg>
</div>

<button type="button" class="btn btn-primary position-relative">
  Alerts <span class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-2"><span class="visually-hidden">unread messages</span></span>
</button>
```

```html
<div class="position-relative m-4">
  <div class="progress" role="progressbar" aria-label="Progress" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" style="height: 1px;">
    <div class="progress-bar" style="width: 50%"></div>
  </div>
  <button type="button" class="position-absolute top-0 start-0 translate-middle btn btn-sm btn-primary rounded-pill" style="width: 2rem; height:2rem;">1</button>
  <button type="button" class="position-absolute top-0 start-50 translate-middle btn btn-sm btn-primary rounded-pill" style="width: 2rem; height:2rem;">2</button>
  <button type="button" class="position-absolute top-0 start-100 translate-middle btn btn-sm btn-secondary rounded-pill" style="width: 2rem; height:2rem;">3</button>
</div>
```

--------------------------------

### Bootstrap Edge Positioning Utilities

Source: https://getbootstrap.com/docs/5.3/utilities/position

Arrange elements precisely using edge positioning utilities. The format is `{property}-{position}`, where property can be top, start, bottom, or end, and position can be 0, 50, or 100. More values can be added via Sass variables.

```html
<div class="position-relative">
  <div class="position-absolute top-0 start-0"></div>
  <div class="position-absolute top-0 end-0"></div>
  <div class="position-absolute top-50 start-50"></div>
  <div class="position-absolute bottom-50 end-50"></div>
  <div class="position-absolute bottom-0 start-0"></div>
  <div class="position-absolute bottom-0 end-0"></div>
</div>
```

--------------------------------

### Bootstrap Sass Position Utilities API

Source: https://getbootstrap.com/docs/5.3/utilities/position

Illustrates the configuration for position-related utilities within Bootstrap's Sass utilities API. It defines properties and values for 'position', 'top', 'bottom', 'start', 'end', and 'translate-middle', enabling customization and generation of CSS classes.

```scss
"position": (
  property: position,
  values: static relative absolute fixed sticky
),
"top": (
  property: top,
  values: $position-values
),
"bottom": (
  property: bottom,
  values: $position-values
),
"start": (
  property: left,
  class: start,
  values: $position-values
),
"end": (
  property: right,
  class: end,
  values: $position-values
),
"translate-middle": (
  property: transform,
  class: translate-middle,
  values: (
    null: translate(-50%, -50%),
    x: translateX(-50%),
    y: translateY(-50%)
  )
),
```

--------------------------------

### Bootstrap Sass Position Values

Source: https://getbootstrap.com/docs/5.3/utilities/position

Defines the default Sass map for position utility values in Bootstrap. This map, `$position-values`, is used to generate the responsive position utilities like top, bottom, start, and end, allowing for values of 0, 50%, and 100%.

```scss
$position-values: (
  0: 0,
  50: 50%,
  100: 100%
);
```

--------------------------------

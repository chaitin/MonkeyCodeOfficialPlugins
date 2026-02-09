### Positioned Bootstrap Badges (HTML)

Source: https://getbootstrap.com/docs/5.3/components/badge

Illustrates using Bootstrap utility classes to position badges in the corner of links or buttons, useful for indicators like unread messages or alerts. Includes examples with and without counts.

```html
<button type="button" class="btn btn-primary position-relative">
  Inbox
  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
    99+
    <span class="visually-hidden">unread messages</span>
  </span>
</button>

<button type="button" class="btn btn-primary position-relative">
  Profile
  <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
    <span class="visually-hidden">New alerts</span>
  </span>
</button>
```

--------------------------------

### Bootstrap Badge Background Colors (HTML)

Source: https://getbootstrap.com/docs/5.3/components/badge

Provides examples of applying different background colors to badges using Bootstrap's `.text-bg-{color}` helper classes. It also mentions the older method of pairing `.text-{color}` and `.bg-{color}`.

```html
<span class="badge text-bg-primary">Primary</span>
<span class="badge text-bg-secondary">Secondary</span>
<span class="badge text-bg-success">Success</span>
<span class="badge text-bg-danger">Danger</span>
<span class="badge text-bg-warning">Warning</span>
<span class="badge text-bg-info">Info</span>
<span class="badge text-bg-light">Light</span>
<span class="badge text-bg-dark">Dark</span>
```

--------------------------------

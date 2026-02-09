### Apply `snap-normal` for skipping scroll snap stops in Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-snap-stop

This example illustrates the use of the `snap-normal` utility, which allows a scroll container to skip past potential scroll snap positions. This provides a smoother, less restrictive scrolling experience for the user, letting them scroll freely without being forced to stop at every snap point.

```html
<div class="snap-x ...">  <div class="snap-center snap-normal ...">    <img src="/img/vacation-01.jpg" />  </div>  <div class="snap-center snap-normal ...">    <img src="/img/vacation-02.jpg" />  </div>  <div class="snap-center snap-normal ...">    <img src="/img/vacation-03.jpg" />  </div>  <div class="snap-center snap-normal ...">    <img src="/img/vacation-04.jpg" />  </div>  <div class="snap-center snap-normal ...">    <img src="/img/vacation-05.jpg" />  </div>  <div class="snap-center snap-normal ...">    <img src="/img/vacation-06.jpg" />  </div></div>
```

--------------------------------

### Apply `snap-always` for forced scroll snap stops in Tailwind CSS

Source: https://tailwindcss.com/docs/scroll-snap-stop

This example demonstrates how to use the `snap-always` utility with `snap-mandatory` to ensure a scroll container always stops at a snap position before allowing the user to scroll further. It's typically applied to child elements within a scroll-snap container to create a carousel-like effect.

```html
<div class="snap-x snap-mandatory ...">  <div class="snap-center snap-always ...">    <img src="/img/vacation-01.jpg" />  </div>  <div class="snap-center snap-always ...">    <img src="/img/vacation-02.jpg" />  </div>  <div class="snap-center snap-always ...">    <img src="/img/vacation-03.jpg" />  </div>  <div class="snap-center snap-always ...">    <img src="/img/vacation-04.jpg" />  </div>  <div class="snap-center snap-always ...">    <img src="/img/vacation-05.jpg" />  </div>  <div class="snap-center snap-always ...">    <img src="/img/vacation-06.jpg" />  </div></div>
```

--------------------------------

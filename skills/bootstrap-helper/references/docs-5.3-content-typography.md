### Description List Alignment Example (HTML)

Source: https://getbootstrap.com/docs/5.3/content/typography

Illustrates aligning terms and descriptions horizontally using Bootstrap's grid system classes (`.col-sm-*`). Includes examples of text truncation with `.text-truncate` and nesting description lists.

```html
<dl class="row">
  <dt class="col-sm-3">Description lists</dt>
  <dd class="col-sm-9">A description list is perfect for defining terms.</dd>

  <dt class="col-sm-3">Term</dt>
  <dd class="col-sm-9">
    <p>Definition for the term.</p>
    <p>And some more placeholder definition text.</p>
  </dd>

  <dt class="col-sm-3">Another term</dt>
  <dd class="col-sm-9">This definition is short, so no extra paragraphs or anything.</dd>

  <dt class="col-sm-3 text-truncate">Truncated term is truncated</dt>
  <dd class="col-sm-9">This can be useful when space is tight. Adds an ellipsis at the end.</dd>

  <dt class="col-sm-3">Nesting</dt>
  <dd class="col-sm-9">
    <dl class="row">
      <dt class="col-sm-4">Nested definition list</dt>
      <dd class="col-sm-8">I heard you like definition lists. Let me put a definition list inside your definition list.</dd>
    </dl>
  </dd>
</dl>
```

--------------------------------

### Inline List Example (HTML)

Source: https://getbootstrap.com/docs/5.3/content/typography

Shows how to display list items horizontally using the `.list-inline` and `.list-inline-item` classes. This combination removes bullets and adds light margins for an inline layout.

```html
<ul class="list-inline">
  <li class="list-inline-item">This is a list item.</li>
  <li class="list-inline-item">And another one.</li>
  <li class="list-inline-item">But they’re displayed inline.</li>
</ul>
```

--------------------------------

### Unstyled List Example (HTML)

Source: https://getbootstrap.com/docs/5.3/content/typography

Demonstrates how to remove default list styling and margins using the `.list-unstyled` class. This class only affects immediate children, requiring nested lists to be styled separately if needed.

```html
<ul class="list-unstyled">
  <li>This is a list.</li>
  <li>It appears completely unstyled.</li>
  <li>Structurally, it’s still a list.</li>
  <li>However, this style only applies to immediate child elements.</li>
  <li>Nested lists:
    <ul>
      <li>are unaffected by this style</li>
      <li>will still show a bullet</li>
      <li>and have appropriate left margin</li>
    </ul>
  </li>
  <li>This may still come in handy in some situations.</li>
</ul>
```

--------------------------------

### Bootstrap Lead Paragraph HTML Example

Source: https://getbootstrap.com/docs/5.3/content/typography

Demonstrates how to make a paragraph stand out using Bootstrap's `.lead` utility class. This class increases the font size and line height of the paragraph, making it more prominent.

```html
<p class="lead">
  This is a lead paragraph. It stands out from regular paragraphs.
</p>
```

--------------------------------

### Implementing Basic Blockquotes

Source: https://getbootstrap.com/docs/5.3/content/typography

Demonstrates the basic structure for creating blockquotes using the `<blockquote class="blockquote">` element. This is used for quoting content from another source.

```html
<blockquote class="blockquote">
  <p>A well-known quote, contained in a blockquote element.</p>
</blockquote>
```

--------------------------------

### Displaying Abbreviations with Tooltips

Source: https://getbootstrap.com/docs/5.3/content/typography

Shows how to use the HTML `<abbr>` element to display abbreviations and acronyms. The `title` attribute provides the expanded version, which appears on hover. The `.initialism` class applies a slightly smaller font size.

```html
<p><abbr title="attribute">attr</abbr></p>
<p><abbr title="HyperText Markup Language" class="initialism">HTML</abbr></p>
```

--------------------------------

### Styling Inline Text Elements with HTML Tags

Source: https://getbootstrap.com/docs/5.3/content/typography

Demonstrates how to use semantic HTML5 tags for common inline text styling, such as highlighting, deletion, additions, underlining, small print, bold, and italics. These tags provide semantic meaning to the text.

```html
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
```

--------------------------------

### Blockquotes with Attribution

Source: https://getbootstrap.com/docs/5.3/content/typography

Illustrates how to add attribution to a blockquote. This involves wrapping the blockquote in a `<figure>` and using a `<figcaption class="blockquote-footer">` for the source, with the source work enclosed in `<cite>`.

```html
<figure>
  <blockquote class="blockquote">
    <p>A well-known quote, contained in a blockquote element.</p>
  </blockquote>
  <figcaption class="blockquote-footer">
    Someone famous in <cite title="Source Title">Source Title</cite>
  </figcaption>
</figure>
```

--------------------------------

### Styling Inline Text Elements with Bootstrap Classes

Source: https://getbootstrap.com/docs/5.3/content/typography

Provides Bootstrap classes that replicate the styling of common inline HTML5 elements. These classes can be used as an alternative to semantic tags when only styling is required.

```html
<p class="mark">This text is marked.</p>
<p class="small">This text is small print.</p>
<p class="text-decoration-underline">This text is underlined.</p>
<p class="text-decoration-line-through">This text is struck through.</p>
```

--------------------------------

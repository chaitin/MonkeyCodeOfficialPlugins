---
name: slides
description: Turn a presentation brief into a 16:9 HTML deck and export it to a high-fidelity image-based PPTX, followed by a mandatory HTML/PPTX fidelity audit.
---

# Slides

Use for presentations from requirements through `.pptx`. The supported default is a **high-fidelity, non-editable whole-slide render**. Do not claim that arbitrary HTML becomes editable PowerPoint objects.

## Workflow

1. Clarify audience, presentation goal, duration/slide count, source facts, brand assets, language, and delivery context. Do not invent metrics or citations.
2. Create a concise story: opening claim, evidence/progression, decision or call to action. One primary message per slide; keep body copy presentation-sized.
3. Build a self-contained 16:9 HTML deck. Every page MUST be one `<section class="slide">`; use exactly one section per PPTX slide, in DOM order. Set slides to `width: 1600px; height: 900px; overflow: hidden`. Resolve local assets relative to the HTML file; avoid network dependencies. Include print-safe backgrounds, explicit fonts/fallbacks, and reduced-motion behavior.
4. Preview all slides at 1600×900. Check clipping, contrast, hierarchy, repeated layouts, missing assets, and factual consistency.
5. Export using the bundled renderer:

   ```bash
   python3 scripts/export_html_to_pptx.py deck.html deck.pptx
   ```

   The exporter uses Playwright/Chromium to screenshot each `section.slide` and `python-pptx` to place one PNG edge-to-edge on each 13.333×7.5 inch slide. It stages the PPTX and `<deck>.pptx.fidelity.json` together and restores any previous pair if installation fails. The manifest records the source, canvas, slide count, and per-slide SHA-256 evidence. It checks dependencies and reports actionable installation guidance, but never installs anything itself. If dependencies are absent, ask before installing from the bundled `scripts/requirements.txt`, then install Chromium explicitly with `python3 -m playwright install chromium`; do not silently mutate the user's environment.
6. **Mandatory gate:** invoke `pptx-html-fidelity-audit` after every export. Run its extraction and layout verification, compare the HTML and PPTX slide count/content visually, record the audit table, correct any critical/high drift, re-export, and re-audit. Do not call the deck complete until the audit passes or remaining blockers are explicitly reported.

## Fidelity and editability contract

Whole-slide PNG rendering preserves browser layout, CSS, gradients, SVG, and web typography much more faithfully than reconstructing arbitrary DOM as native PowerPoint shapes, but slide content is not editable. The HTML remains the editable source. This package intentionally provides no generic `--editable` mode: reliable editable export requires a constrained component/schema mapper and explicit per-element semantics. Offer such a mode only if a future implementation clearly documents its supported subset and fails on unsupported HTML.

## Deliverables

Return the brief/story assumptions, source HTML path, PPTX path, slide count, export command/output, fidelity-audit report and commands, non-editable-mode disclosure, font/asset substitutions, and unresolved issues.

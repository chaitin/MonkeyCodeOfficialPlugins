---
name: image-refinement
description: Refine an existing still image while preserving explicit invariants and validating a genuine local output.
visibility: internal
owner: design-flow
---

# Image Refinement

Use when the user supplies an existing image and asks for a bounded edit, correction, cleanup, or variant.

## Workflow

1. Require an authorized source image plus requested changes, preservation constraints, exclusions, target format, intended use, and acceptance criteria. Resolve ambiguity where an edit could destroy an invariant.
2. Inspect the source's real format, dimensions, aspect ratio, transparency/animation requirements, composition, and visible defects.
3. Read `references/color.md` for palette/color work and `references/anti-ai-slop.md` when stylistic regeneration could introduce generic artifacts.
4. Use only the available `image.image_to_image` capability; state concretely what must change and what must remain. Do not assume a vendor, model, endpoint, CLI, or runtime.
5. Save to an authorized workspace location without overwriting the source unless explicitly requested. Confirm that the result exists, is non-empty, decodes as the requested real image type, preserves required content and composition, and contains no new crop, watermark, unrelated logo, accidental text, or generation defect.
6. Compare the result against every declared invariant. Report validation performed and any limitation truthfully; never substitute a placeholder or claim an unavailable image exists.

If the request asks for several alternatives followed by card selection, route it through `image-generation`'s three-direction `DesignSelectCards` protocol rather than inventing an implicit selection flow here.

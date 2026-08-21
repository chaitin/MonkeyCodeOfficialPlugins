---
name: design-refinement
description: Audit and improve an existing Web or mobile interface while preserving declared intent, content, and working behavior.
visibility: internal
owner: design-flow
---

# Design Refinement

Use for an existing implemented interface. Prefer bounded, evidence-based changes over wholesale rewrites.

## Workflow

1. Read the relevant files, running product when available, tokens, components, tests, screenshots, and design guidance.
2. Establish pain points, invariants, desired change level, target platforms, and acceptance criteria. Preserve navigation, data behavior, forms, content, and public component contracts unless the user authorizes change.
3. Audit hierarchy, typography, spacing, color, density, responsiveness, accessibility, interaction feedback, and state coverage. Separate blocking defects from subjective opportunities and tie findings to concrete files or rendered evidence.
4. Resolve visual authority in order: explicit user direction; user-specified design-system path; workspace `DESIGN.md`; established repository conventions; documented defaults. Read the winner.
5. Plan the smallest coherent edit set. For a bounded refinement, proceed with the relevant platform skill. For a wholesale new visual direction, invoke `web-design-art-direction` and do not implement until `DesignSelectCards` returns a user selection.
6. Verify preserved behavior, target widths/devices, navigation, forms, focus/accessibility, overflow, states, and repository tests. Report only checks actually run.

## Selected-preview fidelity passes

When refinement follows the first implementation of a selected design direction, treat the selected preview as the visual authority while preserving the brief and working behavior. Require its local path, the target viewport or device frame, and a rendered screenshot of the real implementation; do not refine from memory or prose alone.

Prioritize bounded passes in this order:

1. Correct structure and proportion: page architecture, section and container dimensions, grid, alignment, reading path, focal placement, and media crop.
2. Correct typography, spacing, and color: type hierarchy, line length, rhythm, whitespace, semantic palette, contrast, borders, radii, and elevation.
3. Correct remaining high-impact details: icon and control sizing, decorative treatment, component states, and responsive discrepancies that materially affect the selected direction.

After each pass, run the interface and re-capture it in the same frame, compare it with the selected preview, and update the mismatch list. Do not spend a pass reproducing distorted generated-image lettering, impossible raster artifacts, or details that would break accessibility or behavior. Respect the orchestration's pass limit and report any remaining fidelity gap explicitly.

## Rendered quality gate

Never pass a design from source inspection or because it merely opens. Audit rendered screenshots with their viewport, device-pixel ratio, and browser zoom recorded. For Web, cover representative desktop, tablet, and mobile widths and explicitly exercise 75%, 100%, and 125% zoom. For mobile, cover the declared target device plus representative narrow and wide frames.

Treat these as blockers that cannot be averaged away:

- horizontal overflow or clipped, overlapping, or unreachable primary content;
- an accidental fixed-width layout that fails to expand or reflow;
- content-width utilization below 60% of the viewport;
- left/right outer-whitespace asymmetry above 15% of viewport width;
- missing required content, interaction, or state;
- inaccessible primary navigation, action, focus path, or contrast.

A metric may be exempt only when the winning visual authority explicitly requires that composition, the evidence names that rule, and neighboring frames demonstrate that it remains intentional rather than a breakpoint failure.

After all blockers pass, score 100 points:

- layout, hierarchy, and proportion: 25;
- responsive and zoom stability: 20;
- typography, spacing, and color: 20;
- content density and whitespace balance: 15;
- accessibility and interaction: 10;
- required states and content integrity: 10.

Require at least 80/100 overall and 60% of the available points in every category. Evidence must include screenshot paths, frame metadata, measured values when browser/DOM tooling is available, clearly labeled visual estimates otherwise, category scores, total score, blockers, and the audit attempt. A failed check must lead to a bounded correction and a fresh capture in the same frames; never reuse a pre-fix score.

## Craft references

Read the applicable local references before auditing or editing:

- `references/typography.md`
- `references/color.md`
- `references/anti-ai-slop.md`
- `references/accessibility-baseline.md`
- `references/state-coverage.md`

Use `visual-design-foundations` for system-level hierarchy and tokens, `frontend-design` and optionally `web-component-design` for Web, or `react-native-design` for React Native/mobile.

## Impeccable/taste refinement pass

Apply these as contextual audit rules, not as a separate redesign or a default aesthetic:

1. State a one-line design read (surface, audience, intended character, and existing system). Preserve brand assets and choose one coherent palette, radius logic, icon family, type scale, and copy register.
2. Remove templated AI tells unless explicit direction requires them: purposeless purple/blue glow, centered hero plus three equal cards, cards/pills around everything, repeated eyebrow labels and section layouts, fake precision, fake product screenshots, decorative effects, and vague adjective-heavy copy. Cards and elevation must communicate hierarchy.
3. Audit visible copy, CTA intent, and content density. Do not invent metrics. Keep one label per CTA intent, prevent desktop CTA/nav wrapping, and prefer a focused message over filler. Preserve user-provided content unless copy changes are authorized; report recommended copy separately otherwise.
4. Test every multi-column section's explicit mobile collapse. Avoid `h-screen` mobile instability, clipped display italics, accidental fixed widths, and hero content whose primary action falls outside the initial representative viewport.
5. Cover loading, empty, error, disabled, focus, hover, and active states. Labels remain outside inputs; primary controls, placeholders, helper/error text, and focus rings meet applicable contrast requirements.
6. Add motion only when it communicates hierarchy, feedback, state, or spatial continuity. Keep it restrained, performant, interruptible, and reduced-motion safe; delete motion whose only rationale is decoration.
7. Prefer a few decisive fixes over broad cosmetic churn. Finish with a runnable artifact and fresh rendered evidence, not only a critique list.

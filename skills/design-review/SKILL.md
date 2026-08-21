---
name: design-review
description: Audit and safely improve a rendered interface with evidence, scored findings, bounded fixes, and before/after verification.
---

# Design Review

Use on an implemented interface. This is an executable review-and-fix workflow, not a catalogue pointer.

## Inputs and safety

Identify the requested surface, user goal, target viewports, visual authority (`DESIGN.md`, selected preview, design system, or established product conventions), and invariants. Inspect the running UI and relevant source. Preserve behavior, content, contracts, and unrelated work. Never claim visual evidence from source inspection alone.

## Audit and score

Capture the same representative desktop, tablet, and mobile frames before and after changes. Record viewport, DPR, zoom, route/state, and screenshot path. Exercise focus/keyboard flow and loading, empty, error, disabled, hover, and active states when applicable.

Block immediately on clipped/unreachable content, horizontal overflow, broken primary action/navigation, missing required state, inaccessible focus/contrast, or a layout that fails to reflow. Then score 100 points:

- hierarchy, layout, and proportion: 25
- typography, spacing, color, and visual consistency: 20
- responsive behavior and zoom stability: 20
- interaction feedback and state coverage: 15
- accessibility: 15
- content integrity and polish: 5

Passing requires no blocker, at least 80/100 overall, and at least 60% in every category. Each deduction must cite rendered evidence and, where identifiable, `file:line`.

## Fix loop

1. Rank findings as `MUST_FIX`, `SHOULD_FIX`, or `POLISH`; distinguish measurable defects from taste preferences.
2. Plan the smallest coherent fixes. Do not redesign unless authorized.
3. Apply one bounded batch at a time. Do not commit unless asked; if commits are requested, keep them atomic.
4. Run relevant tests and recapture identical frames. A stale pre-fix capture cannot prove success.
5. Repeat for remaining `MUST_FIX` items. Stop and report constraints rather than concealing an unresolved blocker.

## Required output

Provide: scope and authority; before captures; a findings table (`severity | category | evidence | file:line | correction`); category scores and total; edits made; validation commands and exact outcomes; after captures; remaining risks; and `PASS` or `BLOCK`. Include side-by-side before/after paths when available. Approval is earned only by fresh rendered evidence.

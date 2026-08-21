---
name: frontend-design
description: Implement distinctive, production-grade Web interfaces after requirements and any required visual-direction selection are settled.
visibility: internal
owner: design-flow
---

# Frontend Design

Use for websites, landing pages, dashboards, application screens, HTML/CSS artifacts, and framework components. Ship working code with a clear visual thesis and product-specific detail.

## Entry condition

Implementation may begin after `design-flow` resolves one of its authorized paths: a selected catalog template, a selected generated direction, a clarified visual brief after the user skips or cannot use both recommendation mechanisms, or a bounded refinement that preserves the existing direction. Read the corresponding authority before editing. An open selection request or explicit cancellation is never authorization.

## Workflow

1. Read the brief, selected template `DESIGN.md`, selected direction, or clarified visual thesis as applicable, plus the repository framework, tokens, components, assets, tests, screenshots, and design guidance. Retain a selected preview path and target viewport only when a generated direction was selected. Preserve explicit brand and system rules.
2. Translate the chosen direction into an implementable system: semantic tokens, finite type scale, layout/grid, spacing rhythm, media treatment, component states, and responsive transformations. Re-typeset critical text; do not embed preview-image text as UI.
3. Build the real interface rather than a poster. Include expected controls, navigation, realistic content, and loading, empty, error, populated/success, disabled, hover, focus, active, and edge states as applicable.
4. Prefer repository conventions and existing dependencies. Use semantic markup, keyboard-accessible controls, visible focus, robust text fit, sensible contrast, and reduced-motion behavior. Centralize repeated values through the project's token mechanism.
5. Keep one describable visual idea. Remove ungrounded gradients, glass panels, decorative blobs, card spam, generic SaaS structure, emoji icons, and fabricated proof unless established brand language requires them.
6. Verify real mobile and desktop widths, overflow, long/localized text, interaction states, keyboard use, accessibility, and the project's build/test/lint path. Preserve behavior and report checks actually run.

## Mandatory fidelity handoff

For an interface implemented from a selected preview, the initial code pass must produce a rendered screenshot from the running interface at the selected target viewport and artifact frame. Compare that screenshot with the selected preview, produce a concrete prioritized mismatch list, and invoke `design-refinement` before final completion. Re-capture after refinement so the final report is based on rendered evidence rather than source inspection alone.

If the interface cannot be run or captured, report the blocker and unverified result. The agent must not claim completion after only writing code or passing a build. Do not use the preview as a background, copy distorted preview text literally, or sacrifice behavior and accessibility for superficial pixel matching.

Use `web-component-design` when reusable component APIs or framework composition are in scope. Use `visual-design-foundations` when establishing or revising tokens.

## Craft references

Read the references applicable to the artifact before implementation and self-review:

- `references/typography.md` for type scale, line height, tracking, and text measure.
- `references/color.md` for semantic palette and accent discipline.
- `references/anti-ai-slop.md` for the must-fix critique pass.
- `references/accessibility-baseline.md` for accessibility acceptance criteria.
- `references/state-coverage.md` for interactive and data-state coverage.

## Source and license

Adapted from Open Design's `frontend-design` skill, which identifies Anthropic's official skill as its upstream. See `LICENSE.txt` in this directory for the preserved Apache License 2.0 terms supplied with the source.

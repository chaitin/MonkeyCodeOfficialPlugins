---
name: design-generation
description: Turn requirements into a grounded brief and implementation constraints for a new Web or mobile interface without relying on templates.
visibility: internal
owner: design-flow
---

# Design Generation

Use for a new interface before art direction or implementation. This skill defines the product and design problem; it does not recommend templates, generate selection cards, or write implementation code.

## Workflow

1. Inspect the authorized workspace for the framework, tokens, components, brand assets, screenshots, `DESIGN.md`, and technical constraints.
2. Establish audience, primary job, target surface, content shape, required actions, emotional register, responsive/device requirements, meaningful states, and acceptance criteria.
3. Ask only for missing decisions that materially change the design. Use small focused rounds. Never fabricate a brand name, claim, price, metric, testimonial, or customer. With permission, mark unknown content explicitly as placeholder or sample.
4. Resolve visual authority in order: explicit user direction; user-specified design-system path; workspace `DESIGN.md`; established repository tokens and components; documented defaults. Read the winning source and do not override it with generic taste.
5. Produce a concise brief for the next skill: real content, information hierarchy, primary action, navigation, state inventory, platform, viewport/device assumptions, assets, visual constraints, and verification criteria.

## Craft references

Read only the references needed for this request, but do not skip a relevant rule set:

- `references/typography.md` for type hierarchy, line length, and responsive scaling.
- `references/color.md` for palette roles, accents, and contrast-aware use.
- `references/anti-ai-slop.md` before proposing a visual direction.
- `references/accessibility-baseline.md` for Web or native accessibility requirements.
- `references/state-coverage.md` for data, form, loading, error, empty, success, and edge cases.

## Handoff

For a new interface, hand the grounded brief back to `design-flow`. It first offers applicable template recommendations. A selected template continues through visual foundations and the design prototype; a template skip may proceed to `web-design-art-direction` when image generation is available; if both recommendation paths are skipped or unavailable, ask the remaining material design questions and create the prototype from the clarified brief. Explicit cancellation still stops.

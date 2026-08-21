---
name: web-design-art-direction
description: Generate three materially different, implementation-ready interface direction images and let the user select, refresh, skip, or cancel before handoff.
visibility: internal
owner: design-flow
---

# Product Design Art Direction

Use after `design-flow` has confirmed a callable text-to-image MCP for a new Web or mobile interface, or for a wholesale redesign that needs competing concepts. Output exactly three core product preview images for selection—not implementation code, a mood board, component sheet, or section-by-section collage.

## Non-negotiable outcome

- Ground all three directions in the same brief, content, information architecture, platform, and constraints.
- Make directions materially different in composition, typography, density, media treatment, and emphasis. Recoloring one layout is not sufficient.
- Generate one image per direction with an available image-generation tool, wait for each task to complete, and persist three real local image files under `.ohmyagent/design/` in the authorized workspace.
- Follow the active Workflow step's selection protocol: visual cards when available, `AskUserQuestion` when cards are unavailable, or a documented automatic recommendation when neither interaction tool exists.
- Do not implement or edit product code while generation or the selection request is active. Generation or validation failure returns control to `design-flow` for template recommendation; cancellation stops.

## 1. Ground and constrain the brief

Identify product, audience, primary job, required content/actions/states, brand position, target platform, target viewport/aspect ratio, implementation stack, and available assets. Read real repository tokens, components, brand assets, screenshots, and workspace `DESIGN.md` when present. Do not invent brands, claims, prices, metrics, awards, testimonials, or customer logos; use visibly labeled placeholders only when authorized.

Resolve visual authority in this order: explicit user/brand direction; user-specified design system; workspace `DESIGN.md`; established repository patterns; local craft guidance. Read the winner and preserve its identity.

## 2. Read craft guidance on demand

Before prompts, read the local references relevant to the brief:

- `references/typography.md` for hierarchy and readable type behavior.
- `references/color.md` for role-based palette, accents, and contrast.
- `references/anti-ai-slop.md` for the required critique pass.
- `references/accessibility-baseline.md` for interaction and contrast implications visible in the concept.
- `references/state-coverage.md` when the product fetches, transforms, or accepts data.

Use `visual-design-foundations` when direction depends on establishing tokens, spacing, or hierarchy.

## 3. Create three substantive directions

Give each direction a short thesis and compare it on all axes below before prompting:

| Axis | Required distinction |
| --- | --- |
| Composition | Different architecture, focal placement, grid, and reading path |
| Typography | Different justified display/body relationship, scale, weight, and rhythm |
| Density | Purposeful airy, balanced, or information-rich treatment |
| Media | Different grounded treatment such as documentary, cutout, product macro, diagram, illustration, or type-led |
| Emphasis | Different brand-compatible accent/action strategy, not arbitrary recoloring |

Directions must remain feasible in the declared stack. Avoid habitual left-copy/right-image heroes, card spam, bento-by-default, glowing dashboards, generic analytics, unearned gradients/glass, floating decoration, emoji icons, fake proof, and vague “revolutionary” copy unless established brand language specifically requires an element.

## 4. Use the correct artifact frame

Choose exactly one protocol from the requested platform. The preview is front-on with all outer artifact edges visible, no crop, no collage, no perspective device/browser mockup.

| Artifact | Required complete preview | Default ratio |
| --- | --- | --- |
| Web landing/marketing page | Entire zoomed-out page from header/navigation through required sections, final CTA, and footer | `9:16` |
| Web app/dashboard | Complete primary desktop workspace with navigation chrome, main work area, primary controls, and meaningful state | `16:9` |
| React Native/mobile app | One complete primary mobile screen with app navigation, main task, primary action, and meaningful state | `9:16` |

Respect a user ratio only if it still shows the complete artifact without cropping. Each prompt must say `single product image, front-on, all outer edges visible, no crop, no collage` and include the corresponding completeness requirement.

## 5. Prompt and preflight

Each complete prompt specifies artifact/platform/ratio, grounded product context, direction thesis, composition and reading order, typography, role-based palette, media subject and treatment, exact major content labels, states, implementation cues, and exclusions.

Before generation, require each prompt to score at least 4/5 for philosophy, hierarchy, execution, specificity, and restraint. Compare the set again; revise if any two remain substantially similar. Critical UI copy will be re-typeset during implementation, so do not treat distorted generated glyphs as source text.

## 6. Generate, persist, and validate

For each direction:

1. Call the available real `image.text_to_image` MCP capability with the complete prompt, then query the task until it reports completion. Do not assume a vendor, model, endpoint, CLI, or runtime.
2. After the generation task returns its result URL, call `DesignSavePreview` with that URL and a distinct workspace-relative `.ohmyagent/design/<direction>.png` (or matching `.jpg`/`.jpeg`/`.gif`) path. Call it once per direction; it creates parent directories and validates the downloaded image. Do not call `DesignSelectCards` unless every save succeeds.
3. Use only the successfully saved local files returned by `DesignSavePreview`; each must decode as a real PNG, JPEG, or GIF, not a URL stub, metadata file, renamed payload, SVG, or WebP.
4. Ensure the long edge is at most 2400 px and aim for less than 1 MiB without unacceptable quality loss. Preserve aspect ratio and complete canvas; never crop to meet limits.
5. Visually inspect artifact completeness, hierarchy, orientation, content roles, implementation feasibility, brand constraints, unwanted logos/watermarks/text, and substantive difference from the other directions.

A failed candidate is ineligible. If three valid candidates cannot be produced after any bounded retry offered by the host, call `Workflow complete_step` with non-empty evidence and outcome `template` so template recommendation can continue.

## 7. Selection gate

Use only the protocol declared by the active Workflow step:

- **Visual cards:** Invoke `DesignSelectCards` in direction mode with exactly three accepted local images and `select`, `next`, `skip`, and `cancel` enabled. For every item, set `preview.type` to `workspace` and pass `preview.path` as a forward-slash workspace-relative path such as `.ohmyagent/design/editorial-craft.png`, not an absolute path, `file://` URL, remote URL, or path prefixed with the workspace root. Include stable ID, direction name, local path, thesis, composition, typography, density, media treatment, emphasis, and implementation risk. Do not manually complete the step after the tool result.
- **Question fallback:** Call `AskUserQuestion` exactly as instructed by the Workflow step. Map `Direction 1`, `Direction 2`, and `Direction 3` to the three persisted candidates and put each direction's identifying details in its option description. Use `More actions` for refresh, template fallback, and cancellation. If a free-text result causes no automatic transition, interpret only an unambiguous answer and complete the declared matching manual outcome; ask again when ambiguous.
- **Automatic fallback:** Compare all three accepted candidates, choose the strongest against the brief, write the complete choice and rationale to `.ohmyagent/design/SELECTED-DIRECTION.md`, then complete the step with outcome `selected`. Do not pretend that the user selected it.

On generation or validation failure, use only `Workflow complete_step` with outcome `template`; the active step determines whether template recommendation remains interactive or selects its strongest candidate automatically.

## Attribution and license

Adapted from Open Design `skills/imagegen-frontend-web/SKILL.md` and `skills/taste-skill/SKILL.md` at commit `cc226e640a76863c5478be758af905d5c03c9c75`, with host-specific template and packaging protocols removed and Web/mobile framing retained. The supplied source terms are preserved in `LICENSE` beside this file.

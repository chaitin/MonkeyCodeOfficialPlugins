---
name: image-generation
description: Generate and validate three materially different still-image directions from a text brief, then present the real local files for user selection.
visibility: internal
owner: design-flow
---

# Image Generation

Use for standalone text-to-image work, not interface implementation previews. The result must be three genuine image alternatives presented through `DesignSelectCards`.

## Workflow

1. Ground one shared brief: purpose, audience, subject, composition, aspect ratio, style, palette, required text, exclusions, source/rights constraints, and intended use. Do not invent factual claims or brands.
2. Define exactly three materially different directions. Vary composition, viewpoint or spatial structure, medium/image treatment, lighting, and visual hierarchy as appropriate. A palette swap, seed change, or tiny prompt edit is not a direction.
3. Read `references/color.md` when palette or contrast matters and `references/anti-ai-slop.md` when the request could fall into generic generated imagery.
4. For each direction, call the `image.text_to_image` MCP capability once with a complete standalone prompt. Do not assume or name a vendor, model, endpoint, CLI, or runtime.
5. Persist each returned image under the authorized workspace's `.ohmyagent/design/` directory with a stable direction-specific filename. Never save outside the authorized workspace.
6. Validate every candidate before presentation:
   - the local file exists, is non-empty, and decodes as a real PNG, JPEG, or GIF (not a renamed payload, SVG, WebP, metadata stub, or prose placeholder);
   - the long edge is at most 2400 px;
   - target file size is under 1 MiB whenever achievable without unacceptable quality loss; report when it cannot be met;
   - the complete intended composition is present with no cropping, clipped subject, clipped outer artifact edge, watermark, unrelated logo, or dangerous text defect;
   - orientation, content, and direction match the brief.
7. If resizing or encoding is needed, preserve aspect ratio and the complete canvas. Never crop or satisfy limits by clipping content.
8. Invoke `DesignSelectCards` with exactly three valid local image cards. For every card, set `preview.type` to `workspace` and pass `preview.path` as a forward-slash workspace-relative path such as `.ohmyagent/design/direction-one.png`, not an absolute path, `file://` URL, remote URL, or path prefixed with the workspace root. Each card also includes a stable ID, direction name, concise thesis, and meaningful differences.

## Hard stop

If any generation/download/persistence/validation step fails and three valid candidates cannot be produced, report the failure or offer a bounded retry. If `DesignSelectCards` fails, is canceled, or returns no explicit selection, stop. Never fabricate a candidate or choose on the user's behalf. This skill does not implement an interface before or after selection.

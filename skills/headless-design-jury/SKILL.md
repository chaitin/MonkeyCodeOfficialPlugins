---
name: headless-design-jury
description: Run a bounded, tool-mediated five-agent read-only design jury over the current design run, fixing MUST_FIX findings for at most three rounds.
visibility: internal
owner: design-flow
---

# Headless Design Jury

Use as a quality gate for an existing design artifact. Operate only in the **current `RUN_DIRECTORY`** established by the caller. Never allocate another version, fall back to the design root, or inspect/write another run.

## Five read-only subreviews

For each round, invoke exactly five independent Agent subreview tasks. Give every reviewer the same brief, target artifact and rendered evidence paths inside `RUN_DIRECTORY`, and explicit read-only constraints: no file edits, no shell/git writes, no commits, no tool that mutates state.

1. **Designer** — user goal, information architecture, hierarchy, composition, responsive behavior, interaction, and states.
2. **Critic** — coherence, distinctiveness, anti-slop, craft defects, unsupported decoration, and evidence quality.
3. **Brand** — brand fit, visual language, assets, tone, consistency, and differentiation.
4. **Accessibility** — semantics, keyboard/focus, contrast, readable content, reduced motion, and target size.
5. **Copy** — message hierarchy, clarity, CTA intent, labels, factual integrity, density, and voice.

Require each Agent to return exactly one review object with its exact role name, a `score` from 0–10, a non-empty `summary`, and evidence-backed `findings`. Map finding severity exactly to `must_fix`, `should_fix`, or `nice_to_have`; include artifact/screenshot path and `file:line` in `evidence` where available. A reviewer does not edit and does not calculate a composite.

## Tool-mediated round protocol

1. Confirm `RUN_DIRECTORY` and fresh rendered evidence. If either is unavailable, stop rather than jury from memory.
2. Launch the five read-only Agent subreviews. Keep their reports independent; do not let one reviewer prime another.
3. Call `DesignJurySubmit` **once for the round** with the five raw reports and required run/round metadata. Do this every round.
4. Treat the tool response as authoritative for the round decision and composite. **Never calculate, reconstruct, override, or trust a reviewer/self-reported composite.** Do not average scores yourself.
5. If the tool returns any accepted `MUST_FIX`, apply only those bounded corrections in the product/artifact using the normal editing tools, then run relevant checks and capture fresh evidence in the same frames.
6. Repeat with five new read-only Agent subreviews and another `DesignJurySubmit` call. A passing round is terminal only while `prototype.html` is unchanged; if the downstream prototype quality gate revises the artifact, submit the next Jury round against the changed prototype hash.

Run at most **three rounds total**. Stop early only when `DesignJurySubmit` reports no accepted `MUST_FIX` and a passing decision. After round three, stop even if blocked; do not conceal or downgrade remaining `MUST_FIX` items.

## Report

Treat `RUN_DIRECTORY/critique/run.json` as the commit marker and authoritative state. The matching `round-N.json`, `events.jsonl`, and `summary.md` are derived reports written in the same locked submission; if a tool call reports a persistence failure, rely on `run.json` and retry rather than presenting uncommitted files. Report each round's five reviewer outputs, fixes, fresh evidence, tests, final tool-issued decision/composite, and unresolved risk. Clearly state when the tool is unavailable; do not substitute a self-scored verdict.

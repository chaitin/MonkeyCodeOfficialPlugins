---
name: plan-design-review
description: Produce a senior-design review plan with dimension scores, explicit quality targets, anti-slop checks, and prioritized acceptance criteria before UI work is merged.
---

# Plan Design Review

Use to review a design proposal, implementation plan, prototype, or rendered UI before implementation/merge. This skill reports and plans corrections; it does not edit files unless the user separately authorizes implementation.

## Procedure

1. Establish the brief, audience, task, platform/viewports, constraints, design authority, and evidence available. Label any dimension that cannot be judged from current evidence; never invent a rendered result.
2. Inspect actual artifacts: plan/design files, existing system/tokens/components, runnable UI, and screenshots. Check consistency with product conventions and preservation requirements.
3. Rate every dimension from 0–10 with a concrete reason and evidence:
   - user-goal clarity and information architecture
   - hierarchy and composition
   - typography and readability
   - color, contrast, and material treatment
   - spacing, density, and rhythm
   - responsive/adaptive strategy
   - interaction, motion, and state coverage
   - accessibility and content integrity
   - distinctiveness and brand fit
4. For each dimension state **what a 10 looks like for this specific product**, not a generic ideal. Overall score is the arithmetic mean of scored dimensions; unscored dimensions are listed separately, never silently treated as zero or ten.
5. Run an anti-slop pass. Flag unjustified purple/blue glow, generic centered hero plus three equal cards, excessive pills/rounded containers, repeated eyebrow labels or section layouts, decorative gradients, invented metrics, fake screenshots, vague marketing copy, inconsistent radius/palette, and motion without communicative purpose. Context and explicit brand direction override heuristics.
6. Convert findings to a sequenced plan. `MUST_FIX` covers usability, accessibility, missing states/content, broken responsiveness, and plan contradictions. `SHOULD_FIX` covers material craft gaps. `OPTIONAL` is subjective polish. Give acceptance evidence for every item.

## Gate and output

Recommend `PASS` only when there are no `MUST_FIX` items, the mean is at least 8.0, and no scored dimension is below 6. Otherwise return `REVISE`; return `INSUFFICIENT_EVIDENCE` when key artifacts are absent.

Output: context/evidence; dimension table (`score | evidence | what 10 looks like | gap`); anti-slop findings; prioritized plan (`priority | action | owner/file | acceptance evidence`); dependencies/risks; and gate. Do not average away accessibility or functional blockers.

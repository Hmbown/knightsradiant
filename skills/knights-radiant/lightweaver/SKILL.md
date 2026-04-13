---
name: lightweaver
description: Make the system legible and honest through names, docs, and API shape.
category: knights-radiant
---

# Lightweaver

Make the system legible and honest through names, docs, and API shape.

## Invoke when

Follow `agents/06-lightweaver/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/06-lightweaver/AGENTS.md`.
2. Use the local order procedures under `agents/06-lightweaver/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce the full legibility packet defined in `agents/06-lightweaver/AGENTS.md`.

At minimum, include:
- audience identification (name who reads this surface and what task they are performing — always do this first, before naming anything)
- revised interface or naming description
- one happy-path example
- one failure-path example (audit failure names with the same rigor as success names — error states deserve honest, specific language)
- guarantees/non-guarantees
- suggested simplifications or renames

Do not omit required output items from the canonical output contract, even if you summarize elsewhere.

## Hand-off

- Normal: Truthwatcher
- Exception: Elsecaller

## Local doctrine

- Order doc: `agents/06-lightweaver/AGENTS.md`
- Local skill index: `agents/06-lightweaver/skills/SKILL.md`

## Example invocation

"Use lightweaver for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

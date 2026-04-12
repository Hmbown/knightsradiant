---
name: elsecaller
description: Plan the structure, compare alternatives, and choose boundaries deliberately.
category: knights-radiant
---

# Elsecaller

Plan the structure, compare alternatives, and choose boundaries deliberately.

## Invoke when

Follow `agents/07-elsecaller/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/07-elsecaller/AGENTS.md`.
2. Use the local order procedures under `agents/07-elsecaller/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce a architecture packet that includes:
- ADR
- constraints
- options considered
- migration/rollback notes

## Hand-off

- Normal: Willshaper
- Exception: Lightweaver

## Local doctrine

- Order doc: `agents/07-elsecaller/AGENTS.md`
- Local skill index: `agents/07-elsecaller/skills/SKILL.md`

## Example invocation

"Use elsecaller for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

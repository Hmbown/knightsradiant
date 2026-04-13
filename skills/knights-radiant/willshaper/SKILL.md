---
name: willshaper
description: Shape the repo, build, and scaffolding so the paved road is the right road.
category: knights-radiant
---

# Willshaper

Shape the repo, build, and scaffolding so the paved road is the right road.

## Invoke when

Follow `agents/08-willshaper/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/08-willshaper/AGENTS.md`.
2. Use the local order procedures under `agents/08-willshaper/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce a scaffolding packet that includes:
- files created
- runtime bridge artifacts if stateful transition is needed (feature flags, adapters, migration jobs — each with removal condition)
- build/test wiring
- setup checklist
- explicit TODOs (name the receiving order)
- verification steps

## Hand-off

- Normal: Stoneward
- Exception: Elsecaller

## Local doctrine

- Order doc: `agents/08-willshaper/AGENTS.md`
- Local skill index: `agents/08-willshaper/skills/SKILL.md`

## Example invocation

"Use willshaper for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

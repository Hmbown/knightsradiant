---
name: dustbringer
description: Delete what is dead, split what is overgrown, and pay down structural debt.
category: knights-radiant
---

# Dustbringer

Delete what is dead, split what is overgrown, and pay down structural debt.

## Invoke when

Follow `agents/03-dustbringer/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/03-dustbringer/AGENTS.md`.
2. Use the local order procedures under `agents/03-dustbringer/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce the full simplification packet defined in `agents/03-dustbringer/AGENTS.md`.

At minimum, include:
- deletion ledger
- usage evidence (specify the type: telemetry data, code grep, dependency graph, or interviews; name the source)
- characterization tests added
- simplification patch summary
- migration choreography if the deletion requires phased rollout (phases, rollback triggers, observability for each phase)
- migration notes or tombstones
- residual risk list

Do not omit required output items from the canonical output contract, even if you summarize elsewhere.

## Hand-off

- Normal: Skybreaker
- Exception: Elsecaller

## Local doctrine

- Order doc: `agents/03-dustbringer/AGENTS.md`
- Local skill index: `agents/03-dustbringer/skills/SKILL.md`

## Example invocation

"Use dustbringer for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

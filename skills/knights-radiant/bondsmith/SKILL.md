---
name: bondsmith
description: Unite systems, teams, and dependencies without hiding the seams.
category: knights-radiant
---

# Bondsmith

Unite systems, teams, and dependencies without hiding the seams.

## Invoke when

Follow `agents/10-bondsmith/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/10-bondsmith/AGENTS.md`.
2. Use the local order procedures under `agents/10-bondsmith/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce the full integration packet defined in `agents/10-bondsmith/AGENTS.md`.

At minimum, include:
- participants and interfaces
- compatibility matrix
- observability contract: which signals must exist before each phase advances, who owns the dashboards, and what alert thresholds gate the next step
- rollout sequence
- migration/backfill/rollback notes
- integration tests added or required
- ownership and coordination checklist
- Elsecaller escalation trigger: if the compatibility matrix requires more than N adapters, or if the coordination overhead exceeds the value of preserving the current boundary, stop and redesign

Do not omit required output items from the canonical output contract, even if you summarize elsewhere.

## Hand-off

- Normal: Lightweaver
- Exception: Elsecaller

## Local doctrine

- Order doc: `agents/10-bondsmith/AGENTS.md`
- Local skill index: `agents/10-bondsmith/skills/SKILL.md`

## Example invocation

"Use bondsmith for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

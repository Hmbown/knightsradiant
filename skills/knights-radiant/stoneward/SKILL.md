---
name: stoneward
description: Hold the load-bearing core: reliability, capacity, performance, failure budgets.
category: knights-radiant
---

# Stoneward

Hold the load-bearing core: reliability, capacity, performance, failure budgets.

## Invoke when

Follow `agents/09-stoneward/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/09-stoneward/AGENTS.md`.
2. Use the local order procedures under `agents/09-stoneward/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce the full load-bearing packet defined in `agents/09-stoneward/AGENTS.md`.

At minimum, include:
- critical scenarios
- baseline behavior / benchmark notes
- characterization tests added
- failure modes covered
- kill-switch contract: the operational lever that reverts the change under pressure, its mechanism (feature flag, config, DNS, etc.), and confirmation that it works without a deploy
- risk notes and follow-ups
- regression guard plan

Do not omit required output items from the canonical output contract, even if you summarize elsewhere.

## Hand-off

- Normal: Bondsmith
- Exception: Truthwatcher

## Local doctrine

- Order doc: `agents/09-stoneward/AGENTS.md`
- Local skill index: `agents/09-stoneward/skills/SKILL.md`

## Example invocation

"Use stoneward for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

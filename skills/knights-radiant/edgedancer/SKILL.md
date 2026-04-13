---
name: edgedancer
description: Cover the forgotten paths: edge cases, error recovery, accessibility, slow paths.
category: knights-radiant
---

# Edgedancer

Cover the forgotten paths: edge cases, error recovery, accessibility, slow paths.

## Invoke when

Follow `agents/04-edgedancer/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/04-edgedancer/AGENTS.md`.
2. Use the local order procedures under `agents/04-edgedancer/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce the full edge-path packet defined in `agents/04-edgedancer/AGENTS.md`.

At minimum, include:
- edge-case matrix (include time horizon: immediate, hours, days, weeks)
- coverage present vs missing
- highest-risk forgotten paths
- a11y findings if relevant
- recovery-path tests to add
- operational recovery notes (rollback runbook entries, on-call guidance) if the edge case is production-facing
- patch recommendations

Do not omit required output items from the canonical output contract, even if you summarize elsewhere.

## Hand-off

- Normal: Dustbringer
- Exception: Truthwatcher

## Local doctrine

- Order doc: `agents/04-edgedancer/AGENTS.md`
- Local skill index: `agents/04-edgedancer/skills/SKILL.md`

## Example invocation

"Use edgedancer for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

---
name: windrunner
description: Protect the team and the users; make risky changes safe to land.
category: knights-radiant
---

# Windrunner

Protect the team and the users; make risky changes safe to land.

## Invoke when

Follow `agents/01-windrunner/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/01-windrunner/AGENTS.md`.
2. Use the local order procedures under `agents/01-windrunner/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce a reviewer-ready safety packet that includes:
- blast radius summary
- guardrails present/missing
- rollout plan
- rollback plan
- watchpoints

## Hand-off

- Normal: Maintainer for merge; Bondsmith for coordinated rollout
- Exception: Truthwatcher

## Local doctrine

- Order doc: `agents/01-windrunner/AGENTS.md`
- Local skill index: `agents/01-windrunner/skills/SKILL.md`

## Example invocation

"Use windrunner for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

---
name: skybreaker
description: Turn expectations into enforceable law: lint, types, contracts, CI.
category: knights-radiant
---

# Skybreaker

Turn expectations into enforceable law: lint, types, contracts, CI.

## Invoke when

Follow `agents/02-skybreaker/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/02-skybreaker/AGENTS.md`.
2. Use the local order procedures under `agents/02-skybreaker/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce an enforcement packet that includes:
- invariant statement
- enforcement mechanism
- enforcement lifetime (permanent rule or sunset rule with expiry condition)
- exception policy
- CI or lint changes

## Hand-off

- Normal: Windrunner
- Exception: Bondsmith

## Local doctrine

- Order doc: `agents/02-skybreaker/AGENTS.md`
- Local skill index: `agents/02-skybreaker/skills/SKILL.md`

## Example invocation

"Use skybreaker for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

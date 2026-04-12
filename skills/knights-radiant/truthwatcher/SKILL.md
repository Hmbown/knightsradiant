---
name: truthwatcher
description: See what is real: instrumentation, debugging, traces, and root-cause analysis.
category: knights-radiant
---

# Truthwatcher

See what is real: instrumentation, debugging, traces, and root-cause analysis.

## Invoke when

Follow `agents/05-truthwatcher/AGENTS.md` for the canonical decision criteria.

## Inputs required

- task statement
- relevant repo or diff context
- current constraints and risk level
- any prior hand-off artifact from the previous order

## Procedure

1. Read the canonical order doc at `agents/05-truthwatcher/AGENTS.md`.
2. Use the local order procedures under `agents/05-truthwatcher/skills/`.
3. Keep the work inside this order's stance until its artifact is complete.
4. Hand off only after the artifact is explicit enough for the next order to inherit.

## Output shape

Produce a evidence packet that includes:
- symptom statement
- timeline
- hypothesis tree
- verification signals

## Hand-off

- Normal: Edgedancer
- Exception: Stoneward

## Local doctrine

- Order doc: `agents/05-truthwatcher/AGENTS.md`
- Local skill index: `agents/05-truthwatcher/skills/SKILL.md`

## Example invocation

"Use truthwatcher for this task and produce the required artifact before proposing the next order."

## Usage rule

Do not combine this with multiple other active order skills unless you are explicitly routing or handing off. One order should own the work at a time.

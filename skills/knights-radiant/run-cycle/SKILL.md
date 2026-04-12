---
name: run-cycle
description: Choose a Knights Radiant cycle and hand-off sequence for greenfield, triage, refactor, or small-task work.
category: knights-radiant
---

# Run Cycle

Use this skill when the task needs not just one lens, but an intentional order of scrutiny.

## Inputs required

- task statement
- work type: greenfield, triage, refactor, or ordinary small task
- known constraints, deadlines, and risk level

## Procedure

1. Determine the work type:
   - greenfield feature or subsystem
   - bug triage or incident response
   - refactor or cleanup
   - ordinary small task
2. Select the cycle from `CYCLE.md`.
3. Name the required hand-off artifact for the first order before starting.
4. Keep one active order at a time; the next order inherits the artifact, not a blank prompt.
5. Stop early when the minimum viable cycle is enough.

## Output shape

Return a cycle packet with:
- selected cycle
- ordered list of active orders
- first baton owner
- required hand-off artifact for the current step
- stop condition for the cycle
- expected final deliverable

## Default small-task triplet

Lightweaver → Skybreaker → Windrunner

## Example invocation

"Use run-cycle for: 'we have a flaky billing webhook, unclear root cause, and a hotfix window tomorrow morning.'"

## Shared docs

Read `CYCLE.md` and `IDEALS.md` in this repo before running the cycle.

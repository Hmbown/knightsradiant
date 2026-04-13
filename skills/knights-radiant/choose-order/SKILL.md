---
name: choose-order
description: Choose the correct Knights Radiant order for the task before starting execution.
category: knights-radiant
---

# Choose Order

Use this skill when the work is underspecified in method but clear in goal, and the main question is which single engineering lens should own the baton first.

**choose-order vs run-cycle:** choose-order picks the narrowest first lens for the immediate constraint. run-cycle picks a fuller sequence when the task needs multiple lenses. On the same task, they may give different answers — choose-order says "start here," run-cycle says "walk this path." That divergence is intentional, not a bug.

## Inputs required

- task statement
- whether the work is new design, bug triage, refactor, enforcement, rollout, integration, or reliability work
- constraints if already known

## Procedure

1. Classify the task as new design, bug triage, refactor, risky rollout, enforcement, reliability, integration, naming, observability, accessibility, or scaffolding.
2. Pick the narrowest order that names the real constraint:
   - Elsecaller for architecture and irreversible choices
   - Willshaper for repo shape and scaffolding
   - Stoneward for reliability, load, and performance core
   - Bondsmith for integration and multi-system choreography
   - Lightweaver for naming, docs, and truthful surfaces
   - Truthwatcher for evidence, instrumentation, and debugging
   - Edgedancer for edge cases, recovery, and accessibility
   - Dustbringer for deletion and simplification
   - Skybreaker for machine-enforced rules
   - Windrunner for blast radius, rollout, and rollback
3. If the task is small, choose the minimum viable cycle from `CYCLE.md` instead of forcing all ten.
4. Load only the chosen order skill and keep prior hand-off artifacts in context.

## Output shape

Return a routing packet with:
- recommended order
- why this order fits best
- artifact to produce
- likely next order if the work continues
- source docs to consult
- minimum viable alternative if the full order feels too heavy

## Example invocation

"Use choose-order for: 'we need to split our reporting worker into separate batch and realtime paths without wrecking ops.'"

## Shared docs

- `README.md`
- `CYCLE.md`
- `IDEALS.md`

## Source-of-truth order docs

See `agents/` in this repo for each order's `AGENTS.md` and local `skills/` folder.

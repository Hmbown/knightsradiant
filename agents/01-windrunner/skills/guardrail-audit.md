# Guardrail Audit

Inspect a change for missing safety mechanisms and fail-safe defaults.

## When to invoke

- A change crosses trust boundaries or persistence boundaries.
- Someone asks whether a feature "fails safe."
- The PR modifies defaults, permissions, retries, rate limits, migrations, or operator controls.

## Inputs required

- Diff or design note
- Entry points and trust boundaries affected
- Existing config flags, environment controls, and runtime safeguards
- Relevant operational constraints such as batch size, timeout budget, or rollback window

## Procedure

1. Enumerate entrypoints, stateful operations, external calls, and permission boundaries touched by the change.
2. Check validation, authentication, authorization, size limits, retries, timeouts, rate limits, and circuit breakers where they should exist.
3. Inspect defaults and fallback paths for fail-open behavior, silent drops, or hidden side effects.
4. Confirm that any migration, backfill, or background job is chunked, resumable, observable, and stoppable.
5. Verify there is at least one operator control: flag, kill switch, concurrency knob, drain path, or rollout gate.
6. Return a pass or fail assessment with concrete remediation steps and the minimal code or config changes needed.

## Output shape

- Safety surface summary
- Guardrail checklist with pass, fail, or not applicable
- Highest-risk gaps
- Minimal remediation patch list
- Residual risks after remediation

# Forgotten Paths

Surface the untested or unloved branches around a real workflow.

## When to invoke

- A feature has a clear happy path but weak recovery behavior.
- A bug appears only under unusual timing, state, or permissions.
- Reviewers keep asking "what happens when...?"

## Inputs required

- Description of the main user or system flow
- Relevant personas, permission levels, or environments
- Known failure conditions or incident hints
- Current tests for the flow, if any

## Procedure

1. Write the primary flow in a short sequence of states or steps.
2. Enumerate adjacent edge conditions: missing input, invalid input, duplicate submission, slow dependency, partial failure, stale state, permission mismatch, offline or degraded conditions.
3. Check which conditions have coverage in code, tests, and user-facing messaging.
4. Prioritize the edge cases by plausibility, user harm, and reversibility.
5. Reproduce or simulate the highest-risk gaps and propose the smallest fixes that improve recovery.
6. Add regression tests for the chosen cases and note any unresolved branches explicitly.

## Output shape

- Edge-case matrix
- Existing coverage vs missing coverage
- Highest-risk forgotten paths
- Fix recommendations
- Regression tests to add

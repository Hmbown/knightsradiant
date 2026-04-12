# Dustbringer Skills

Dustbringer skills remove weight without collapsing the building. Use them when simplification means less code, fewer layers, and fewer states, not a prettier explanation of the same mess.

## Available skills

- [`scorched-earth-refactor.md`](./scorched-earth-refactor.md) — delete dead or redundant structure while preserving observable behavior.
- [`deprecation-burn.md`](./deprecation-burn.md) — retire old interfaces or features with telemetry, migration, and a removal threshold.

## Usage contract

1. Prefer deletion to replacement when behavior is already covered elsewhere.
2. Prove non-use or preserve behavior with characterization tests before cutting.
3. Record what was removed and why, so the history is legible.
4. Escalate to Elsecaller if simplification becomes a boundary or architecture problem.

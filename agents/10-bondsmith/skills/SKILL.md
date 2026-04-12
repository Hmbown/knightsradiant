# Bondsmith Skills

Bondsmith skills align components that must move together. Use them when integration, dependency drift, or cross-boundary rollout is the real source of risk.

## Available skills

- [`dependency-unity.md`](./dependency-unity.md) — rationalize versions, shared libraries, and dependency graph sprawl.
- [`integration-bridge.md`](./integration-bridge.md) — stage multi-component changes so old and new pieces remain compatible during rollout.

## Usage contract

1. Enumerate participating systems and owners explicitly.
2. Prefer compatibility windows over lockstep deploy assumptions.
3. Make seams visible: versioning, translation, ownership, and rollback.
4. Escalate to Elsecaller when coordination work is masking a boundary design problem.

# Scorched-Earth Refactor

Remove dead or redundant layers while preserving the behavior that still matters.

## When to invoke

- The codebase has wrapper stacks, pass-through services, or duplicate utility layers.
- A module exists mostly to preserve historical structure.
- The simplest safe fix is to delete or collapse code.

## Inputs required

- Candidate files, modules, or services to remove
- Search results, call sites, or runtime usage evidence
- Current tests and coverage around the affected behavior
- Ownership or consumer information, if known

## Procedure

1. Inventory the candidate structure and map its call sites, imports, consumers, and side effects.
2. Prove whether each part is dead, redundant, or still load-bearing using search, tests, logs, traffic data, or build references.
3. Add characterization tests around the behavior that must remain after the cut.
4. Group removal into the smallest safe slices, starting from the deepest or most redundant layer.
5. Delete the slice, rerun build and tests, and compare runtime or bundle behavior where relevant.
6. Leave tombstones in docs or changelogs when the removal affects developers or operators.

## Output shape

- Deletion ledger
- Characterization tests added
- Simplification patch summary
- Residual risks or unknown consumers
- Tombstone or migration note

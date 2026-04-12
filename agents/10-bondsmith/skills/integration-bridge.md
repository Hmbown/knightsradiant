# Integration Bridge

Stage a cross-component change so the system remains compatible while it moves.

## When to invoke

- A schema, event, or API change spans producers and consumers.
- A rollout needs multiple repos or services to change in sequence.
- A local fix is harmless alone but dangerous when deployed out of order.

## Inputs required

- Participating components or repos
- Interface changes involved
- Deployment constraints and environment topology
- Test or staging environments available
- Known rollback requirements

## Procedure

1. List the participating components, owners, and the exact interfaces between them.
2. Build a compatibility matrix showing which versions of each component can safely talk to which others.
3. Design a rollout sequence that preserves backward or forward compatibility for as long as needed.
4. Add integration or end-to-end tests that exercise the important mixed-version states, not just the final state.
5. Write migration, backfill, cutover, and rollback steps with clear stop points.
6. Produce the coordination checklist and call out any periods of temporary dual-write, dual-read, or adapter use.

## Output shape

- Participants and interfaces
- Compatibility matrix
- Rollout sequence
- Integration tests added or required
- Migration and rollback notes
- Coordination checklist

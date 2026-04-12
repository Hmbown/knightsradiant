# Contract Binding

Lock an interface with schemas, compatibility tests, and versioned expectations.

## When to invoke

- An API, event payload, database contract, or SDK surface is changing.
- A producer and consumer are maintained by different teams or services.
- A bug came from mismatched assumptions at a boundary.

## Inputs required

- Current and proposed interface definitions
- Producer examples and consumer expectations
- Versioning rules or deprecation policy
- Test environment or fixtures for both sides of the contract

## Procedure

1. Enumerate the contract surface: fields, types, ordering guarantees, defaults, error semantics, and version markers.
2. Capture real request, response, or event examples from both producer and consumer perspectives.
3. Define or update schemas, generated types, or contract fixtures to represent the interface explicitly.
4. Add positive and negative tests that exercise valid, invalid, old, and new payloads.
5. Build a compatibility matrix for old and new producers against old and new consumers.
6. Gate the interface in CI and produce migration notes for any breaking or soft-breaking change.

## Output shape

- Contract summary
- Compatibility matrix
- Schema or type artifacts
- Contract tests added
- Breaking-change notes
- Migration or deprecation guidance

# Naming Truth

Rename symbols, modules, routes, or concepts so they match actual responsibility.

## When to invoke

- A name keeps causing confusion in code review or onboarding.
- One term refers to multiple concepts, or multiple terms refer to one concept.
- The code says one thing and the docs say another.

## Inputs required

- Symbols, files, routes, or concepts under review
- Current call sites and neighboring vocabulary
- Domain language from product, ops, or users
- Appetite for breaking renames versus alias periods

## Procedure

1. Infer the real responsibility of the target from implementation, tests, and call sites.
2. List the current vocabulary around it and note collisions, ambiguity, or historical residue.
3. Generate candidate names at the right level of abstraction: not too generic, not too implementation-specific.
4. Choose a rename set that improves truth while keeping migration cost proportionate.
5. Apply the rename across code, tests, docs, logs, and user-facing strings where the concept appears.
6. Document any residual ambiguity that remains because the underlying design still needs future work.

## Output shape

- Current term and actual responsibility
- Naming collisions or lies
- Candidate names with tradeoffs
- Recommended rename plan
- Migration scope
- Residual ambiguity notes

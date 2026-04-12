# API Illumination

Make a public interface legible through examples, guarantees, and truthful terminology.

## When to invoke

- A new API, CLI, SDK, or config surface is being designed.
- Existing documentation leaves callers confused.
- The interface technically works but teaches the wrong mental model.

## Inputs required

- Current interface definition or code
- Target audience and primary use cases
- Existing docs, examples, or onboarding notes
- Known constraints, defaults, limits, and error semantics

## Procedure

1. Identify the audience's top tasks and describe them in user language rather than implementation language.
2. Enumerate the interface surface: entities, actions, required inputs, optional inputs, outputs, and error cases.
3. Rewrite names, descriptions, and examples around those tasks, keeping jargon only where it is essential and accurate.
4. Add one or two realistic examples that show the happy path and at least one failure or edge case.
5. State the guarantees and non-guarantees explicitly: defaults, units, versioning, idempotency, ordering, rate limits, and expected errors.
6. Cross-check the docs against code and tests so the surface is honest, not merely elegant.

## Output shape

- Audience and task summary
- Revised interface description
- Happy-path example
- Failure-path example
- Guarantees and non-guarantees
- Suggested simplifications or renames

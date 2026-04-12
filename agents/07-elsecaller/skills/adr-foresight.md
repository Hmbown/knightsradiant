# ADR Foresight

Produce a real architectural decision record with options, tradeoffs, and rollout consequences.

## When to invoke

- The team must choose a subsystem shape, data store, boundary, concurrency model, or vendor.
- An implementation ticket is hiding a structural choice.
- People keep debating architecture verbally without leaving a durable decision record.

## Inputs required

- Problem statement
- Constraints and non-goals
- Quality attributes that matter most: latency, cost, reliability, ownership, compliance, etc.
- Existing system context and likely migration constraints

## Procedure

1. State the decision in one sentence and separate it from adjacent but out-of-scope debates.
2. Capture the constraints, quality attributes, and future changes that the decision must tolerate.
3. Generate two to four viable options, including at least one conservative option and one more ambitious one if both are plausible.
4. Evaluate each option against the stated constraints and quality attributes, noting tradeoffs honestly rather than averaging them away.
5. Choose the recommended option and explain why the rejected options lost.
6. Add rollout, migration, rollback, and open questions so the ADR can drive implementation instead of just documenting opinion.

## Output shape

- ADR title and status
- Context and constraints
- Options considered
- Decision and rationale
- Consequences
- Migration and rollback notes
- Open questions

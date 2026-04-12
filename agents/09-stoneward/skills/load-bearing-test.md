# Load-Bearing Test

Characterize and protect the workflows or libraries the rest of the system depends on.

## When to invoke

- A shared library or critical workflow is changing.
- A fix touches retries, idempotency, transactions, queues, or caches.
- The team needs to know whether the core still behaves under stress or partial failure.

## Inputs required

- Target workflow or module
- Known incident history or risk assumptions
- Current tests and baseline behavior
- Relevant dependencies and failure modes

## Procedure

1. Identify the load-bearing scenarios: the state transitions or requests that would cause outsized harm if they broke.
2. Capture current behavior with characterization tests before making changes.
3. Add failure-mode cases: duplicate delivery, timeout, retry, stale read, partial dependency failure, or out-of-order events as appropriate.
4. Assert correctness properties explicitly, such as idempotency, ordering, fallback behavior, and recovery after restart.
5. Run the tests under representative parallelism or batching where concurrency matters.
6. Gate the workflow in CI and document any remaining risk the tests still do not cover.

## Output shape

- Critical scenarios
- Characterization tests added
- Failure modes covered
- Gaps still uncovered
- Risk notes and follow-ups

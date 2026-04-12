# Telemetry Weave

Add observability that answers real questions without flooding the system with noise.

## When to invoke

- A critical path is hard to debug or monitor.
- A migration or rollout needs watchpoints.
- The team lacks enough context to reason about a dark code path.

## Inputs required

- Code area or workflow to instrument
- The questions telemetry must answer
- Current observability stack
- Cardinality, privacy, and cost constraints

## Procedure

1. Write the decision questions first, such as "which dependency dominates latency?" or "which retry path duplicates work?"
2. Map the workflow into key events, state transitions, and external calls worth observing.
3. Choose the right signal for each question: structured log, counter, histogram, trace span, or event.
4. Add stable correlation identifiers and low-cardinality dimensions; avoid raw payloads, PII, and uncontrolled label sets.
5. Verify the instrumentation in development or staging so the emitted data is readable and actually useful.
6. Produce a small dashboard or alert outline tied directly to the original questions.

## Output shape

- Telemetry questions
- Instrumentation plan
- Code changes to add signals
- Cardinality and privacy notes
- Dashboard or alert outline
- Follow-up questions still unanswered

# Root-Cause Vision

Narrow an incident, regression, or flaky failure to its most likely cause with an explicit evidence chain.

## When to invoke

- A bug has multiple plausible causes.
- An incident timeline is murky.
- A test is flaky and the team keeps applying symptom-level fixes.

## Inputs required

- Symptom description
- Time window and relevant logs, traces, or metrics
- Recent changes, deploys, or config shifts
- Reproduction status, if known

## Procedure

1. Freeze the symptom in concrete terms: what failed, what should have happened, who observed it, and which system boundary noticed it first.
2. Build a timeline of relevant events: deploys, traffic changes, retries, queue growth, dependency errors, configuration changes, or user actions.
3. Cluster evidence by correlation: request IDs, tenants, versions, regions, hosts, or other stable dimensions.
4. Generate a short hypothesis list and actively disqualify each one with specific missing or conflicting evidence.
5. Name the most probable cause, confidence level, and the minimum next experiment or check that would confirm it.
6. Propose the fix and the post-fix signals that would prove the issue is actually resolved.

## Output shape

- Symptom statement
- Timeline
- Evidence summary
- Hypothesis tree
- Most likely cause with confidence
- Confirming next step
- Fix and verification signals

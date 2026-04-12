# PR Shield

Turn a risky change into a reviewer-ready safety packet.

## When to invoke

- The diff touches auth, billing, migrations, concurrency, background jobs, or shared libraries.
- Reviewers need to understand blast radius quickly.
- The author says "it's safe" but the proof is scattered across code, tests, and tribal knowledge.

## Inputs required

- Diff or branch under review
- Affected modules, services, or environments
- Current tests and any staging evidence
- Rollout constraints, feature flags, or maintenance windows
- Known incident history or SLOs, if relevant

## Procedure

1. Read the diff and mark the change surface by entrypoint, state transition, and dependency.
2. Identify failure domains: correctness, data integrity, security, latency, operator load, and downstream consumers.
3. List protections already present in code or ops: flags, validation, idempotency, retries, timeouts, alerts, circuit breakers, and rollback hooks.
4. Call out missing protections and propose the smallest additions that materially reduce blast radius.
5. Produce a reviewer map: hotspots, invariants to verify, tests that matter, and specific questions that must be answered before merge.
6. Produce rollout steps, watch metrics, abort conditions, and rollback steps with named owners where possible.

## Output shape

- One-paragraph change summary
- Blast radius map
- Guardrails present
- Guardrails missing
- Reviewer checklist
- Rollout plan
- Rollback plan
- Open risks and owners

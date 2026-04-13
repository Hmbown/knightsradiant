# Artifact Excerpts: What Good Output Looks Like

This file is deliberately partial. It is not a full simulation of a session. It is a set of hand-off excerpts so contributors and users can see the expected level of specificity.

## 1. Risky migration: auth sessions to a new store

Task:
- Split auth sessions into a new store without locking users out.

Recommended path:
- Elsecaller → Bondsmith → Skybreaker → Windrunner

### Elsecaller excerpt — architecture packet

#### ADR title/status
- ADR-007: Phase auth-session storage from monolith-owned Redis access to a dedicated session service
- Status: proposed

#### Context and constraints
- Current login/session lookups are served directly by the monolith.
- Forced logout is unacceptable during migration.
- Rollback must be possible without a deploy.
- Support and on-call need a clear answer for which system is authoritative in each phase.

#### Options considered
- Option A: big-bang cutover to the new session service
- Option B: phased dual-read with delayed write-primary switch
- Rejected: Option A. It reduces transitional complexity on paper, but makes rollback and user-session continuity materially worse under live traffic.

#### Decision and rationale
- Adopt phased dual-read first.
- Keep the monolith-compatible read path alive until parity metrics and invalid-session rates prove the new service is safe to trust as primary.

#### Affected parties
- auth API owners
- session cleanup job owners
- support/on-call
- every logged-in user

#### Migration/rollback notes
- Phase 1: dual-read, old store remains authoritative.
- Phase 2: canary write-primary for a bounded cohort.
- Rollback: flip authority back to the old store, keep new-store reads dark, preserve token verification parity.

#### Open questions
- How long can dual-read remain operationally acceptable before write amplification becomes too noisy?

### Bondsmith excerpt — integration packet

#### Participants and interfaces
- monolith auth middleware
- new session service
- old session store
- metrics/dashboard ownership

#### Compatibility matrix
| Producer version | Consumer version | Compatible? | Notes |
|---|---|---|---|
| monolith-old | old store | yes | current baseline |
| monolith-old | new service via bridge | yes | required for migration overlap |
| monolith-new | old store rollback path | yes | must stay valid until cutover completes |
| monolith-new | new service primary | yes | final state |

#### Observability contract
- Read parity dashboard exists before any write-primary cohort is enabled.
- Invalid-session rate alert is owned by the auth team.
- Login latency and token-validation error thresholds gate phase advancement.

#### Rollout sequence
1. Ship dual-read code dark.
2. Enable parity metrics.
3. Validate parity for one business cycle.
4. Enable write-primary for canary cohort.
5. Expand cohort only if metrics stay inside thresholds.

### Skybreaker excerpt — enforcement packet

#### Invariant statement
- No migration phase may advance unless the required parity and invalid-session metrics are configured and visible.

#### Enforcement mechanism chosen
- CI contract test for migration config
- config schema requiring metric names and thresholds before write-primary mode is valid

#### Enforcement lifetime
- sunset rule; remove only after the old-store rollback path is intentionally retired

#### Exception policy
- Emergency override requires named owner, expiration, and incident ticket reference.

### Windrunner excerpt — merge-safety packet

#### Change summary
- Introduces phased migration support for session lookup/write authority.

#### Reviewer hotspots
- auth middleware phase switch
- cache invalidation
- rollback path for canary write-primary cohort

#### Watch metrics
- invalid-session rate
- login latency p95
- token verification mismatch count

#### Abort conditions and threshold calibration notes
- Abort if invalid-session rate rises above agreed baseline tolerance for 10 minutes.
- Abort if login latency exceeds the calibrated p95 threshold during canary traffic.
- If baseline is missing, establish it before enabling cohort traffic.

#### Rollback steps
1. Disable write-primary mode.
2. Restore old store authority.
3. Confirm token verification parity.
4. Keep new-store reads dark until incident review completes.

## 2. API cleanup: confusing webhook config surface

Task:
- The webhook client works, but public config is confusing and contract drift keeps reappearing.

Recommended path:
- Lightweaver → Skybreaker → Windrunner

### Lightweaver excerpt — legibility packet

#### Audience identification
- operator configuring webhook delivery
- reviewer checking whether public config docs match runtime behavior

#### Revised interface or naming description
- Rename `retry_mode` to `delivery_retry_policy`.
- Split `timeout` into `connect_timeout_ms` and `response_timeout_ms`.
- Replace vague `strict=true` with `signature_verification=required`.

#### Happy-path example
```yaml
webhook:
  url: https://example.com/hook
  signature_verification: required
  connect_timeout_ms: 1000
  response_timeout_ms: 3000
  delivery_retry_policy: exponential
```

#### Failure-path example
- If signature verification is disabled in a production environment, validation must fail with a message that names the unsafe field directly.

#### Guarantees/non-guarantees
- Guarantees: retry policy names map to real runtime behavior.
- Non-guarantees: changing timeout fields does not imply upstream queue backpressure handling.

### Skybreaker excerpt — enforcement packet

#### Invariant statement
- Public webhook config examples, schema, and runtime field names must match exactly.

#### Enforcement mechanism chosen
- schema validation test
- docs/example fixture test that loads the published config examples

#### Rollout severity plan
- fail CI on new drift
- warn only for deprecated aliases during the deprecation window

### Windrunner excerpt — merge-safety packet

#### Blast radius map
- public docs
- operator configuration files
- reviewer expectations
- upgrade notes for deprecated field names

#### Open risks and owners
- Risk: users may still have old `timeout` fields in saved configs.
- Owner: maintainers must document the alias window and removal date.

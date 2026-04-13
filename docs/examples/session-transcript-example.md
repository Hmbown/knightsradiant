# Example: What a Session Looks Like

User:
- We need to split auth sessions into a new store without locking users out.

Hermes with `choose-order`:
- Recommended order: Elsecaller
- Why: the hardest constraint is the irreversible boundary decision, not the rollout mechanics yet.
- Artifact to produce first: architecture packet (migration ADR, constraints, rejected option, affected parties, rollback notes).
- Likely next order: Bondsmith

Elsecaller artifact excerpt:
- Decision: keep session read compatibility in the monolith during phase 1, move authoritative writes behind a new session service, and defer full ownership transfer until read-path metrics prove parity.
- Rejected option: big-bang cutover to the new store on first deploy. Rejected because rollback would require dual data repair under live auth traffic.
- Affected parties: auth API, background cleanup jobs, session store operators, support/on-call, every signed-in user.
- Open question: how long can dual-read remain acceptable before write amplification becomes operationally noisy?

Hermes hand-off:
- Next order: Bondsmith
- Baton carried forward: the ADR above, especially the chosen compatibility window and rejected big-bang cutover.

Bondsmith artifact excerpt:
- Compatibility matrix: old API ↔ old store, old API ↔ new store via bridge, new API ↔ old store during rollback, new API ↔ new store after cutover.
- Observability gate: do not advance to write-primary mode until read parity, login latency, and invalid-session rates stay inside thresholds for one full business cycle.

Hermes hand-off:
- Next order: Skybreaker
- Baton carried forward: the compatibility matrix and phase-advance thresholds.

Skybreaker artifact excerpt:
- Invariant: every session token lookup must declare which store is authoritative for that phase.
- Enforcement: CI contract test plus a config schema that forbids enabling write-primary mode without dual-read metrics configured.

Hermes hand-off:
- Next order: Windrunner

Windrunner artifact excerpt:
- Reviewer hotspots: auth middleware, cache invalidation, migration job rollback path.
- Abort condition: invalid-session rate rises more than the agreed threshold above baseline for 10 minutes.
- Rollback: return write authority to the old store, keep new-store reads dark, verify token issuance parity before resuming traffic shifts.

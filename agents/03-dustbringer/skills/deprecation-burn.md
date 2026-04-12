# Deprecation Burn

Retire an old API, feature, or compatibility path with telemetry and a staged removal plan.

## When to invoke

- Two versions of the same interface are being maintained.
- A feature flag or legacy endpoint has outlived its purpose.
- The team wants a clean removal instead of indefinite coexistence.

## Inputs required

- Target to deprecate
- Known consumers and ownership
- Replacement path
- Versioning or support policy
- Telemetry sources or ability to add them

## Procedure

1. Identify the deprecated surface and enumerate current consumers or usage paths.
2. Add deprecation markers in code, docs, CLI output, or API responses where appropriate.
3. Instrument usage so the team can tell when the old path is still active and by whom.
4. Provide a replacement path, including examples, shims, or codemods when the migration is mechanical.
5. Define a removal threshold and date: zero traffic, named team sign-off, or version boundary.
6. Remove the deprecated path only after the threshold is met or the deadline is deliberately enforced.

## Output shape

- Deprecation summary
- Consumer list and usage evidence
- Replacement guidance
- Warning or telemetry patch
- Removal threshold and timeline
- Final deletion checklist

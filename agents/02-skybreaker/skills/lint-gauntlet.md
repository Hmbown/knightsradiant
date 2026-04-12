# Lint Gauntlet

Convert a recurring correctness or style problem into machine-enforced policy.

## When to invoke

- The same review comment appears across multiple PRs.
- A bug class is statically detectable.
- The repo has conventions that are too important to leave informal.

## Inputs required

- Representative violations or bug examples
- Current language tooling and CI stack
- Desired invariant and any legitimate exceptions
- Tolerance for auto-fix versus warn-only rollout

## Procedure

1. State the invariant in one sentence and attach the concrete failure mode it prevents.
2. Collect at least a few real examples from the repo so the rule is grounded in actual code.
3. Choose the enforcement layer: compiler, type checker, linter, formatter, generated code check, or CI policy.
4. Implement the rule or configuration, including an auto-fix or codemod where safe.
5. Run the rule across the repo, classify false positives, and narrow the rule until it matches the intended behavior.
6. Roll it out with a severity plan: advisory, warning, or blocking, and document the suppression policy.

## Output shape

- Rule statement
- Enforcement mechanism chosen
- Config or code diff
- False-positive notes
- Rollout severity plan
- Exception or suppression policy

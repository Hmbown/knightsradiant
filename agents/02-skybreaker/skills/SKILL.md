# Skybreaker Skills

Skybreaker skills turn soft expectations into hard checks. Use them when a failure mode should stop depending on memory, good taste, or manual review.

## Available skills

- [`lint-gauntlet.md`](./lint-gauntlet.md) — codify a recurring style, safety, or structural rule in lint, types, or CI.
- [`contract-binding.md`](./contract-binding.md) — define and enforce producer-consumer contracts with schemas, compatibility checks, and tests.

## Usage contract

1. Name the invariant before choosing the tool.
2. Prefer the narrowest enforceable mechanism that catches the real failure class.
3. Minimize permanent exemptions; if one exists, make it explicit and reviewable.
4. Escalate to Bondsmith when compatibility spans teams or repos and needs choreography, not just enforcement.

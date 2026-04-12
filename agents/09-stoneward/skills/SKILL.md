# Stoneward Skills

Stoneward skills characterize and harden the core. Use them when reliability, capacity, or performance must be proven under strain instead of assumed from light local testing.

## Available skills

- [`load-bearing-test.md`](./load-bearing-test.md) — protect critical workflows and shared modules with characterization and failure-mode tests.
- [`perf-bulwark.md`](./perf-bulwark.md) — find and fix real bottlenecks with representative benchmarks and regression guards.

## Usage contract

1. Define the critical path before measuring or optimizing.
2. Use workloads that resemble production shape, not toy benchmarks.
3. Prefer correctness and recoverability over impressive but fragile speed.
4. Escalate to Truthwatcher when the system is still too dark to identify the real bottleneck.

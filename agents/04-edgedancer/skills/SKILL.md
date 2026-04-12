# Edgedancer Skills

Edgedancer skills make neglected paths explicit and testable. Use them when the system needs to remember users, states, and conditions the happy path leaves behind.

## Available skills

- [`forgotten-paths.md`](./forgotten-paths.md) — surface and prioritize untested or under-modeled edge conditions.
- [`a11y-sweep.md`](./a11y-sweep.md) — run a practical accessibility review of changed UI or workflow code.

## Usage contract

1. Start from a real flow or incident, not a generic fear.
2. Enumerate edge conditions concretely: permissions, state, latency, input, device, assistive tech.
3. Prefer fixes that improve recovery and clarity, not just more branches.
4. Escalate to Truthwatcher when the state transition cannot yet be observed or reproduced.

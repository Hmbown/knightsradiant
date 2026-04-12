# Scaffold Rite

Create a new package, service, job, or CLI that matches the repo's actual conventions.

## When to invoke

- A new module or service is needed.
- Engineers keep hand-rolling the same boilerplate differently.
- The team wants a repeatable starting point without pretending the work is done.

## Inputs required

- Target artifact type: package, service, worker, job, CLI, etc.
- Language, framework, and repo conventions
- Required interfaces, dependencies, or ownership metadata
- Expected test and build integration points

## Procedure

1. Inspect the closest good exemplar already in the repo and identify the conventions worth copying.
2. Generate the minimal directory structure, source files, tests, config, README, and ownership markers needed for the artifact to exist honestly.
3. Wire build, lint, and test targets into the existing tooling instead of inventing parallel entrypoints.
4. Add placeholder code only where it clarifies extension points; leave explicit TODOs rather than fake-complete logic.
5. Verify the scaffold from a clean checkout or clean workspace context.
6. Document how future instances should use the scaffold and what not to edit blindly.

## Output shape

- Scaffold summary
- Files created
- Build and test wiring
- Explicit TODOs
- Verification steps
- Follow-up tasks

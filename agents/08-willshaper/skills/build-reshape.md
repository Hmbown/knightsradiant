# Build Reshape

Simplify the build graph and project structure so development becomes faster and more predictable.

## When to invoke

- CI is slow or inconsistent.
- Local setup diverges from CI or production behavior.
- The repo layout makes ownership, build boundaries, or task entrypoints unclear.

## Inputs required

- Build and CI configuration
- Current project layout
- Build timings or pain points, if available
- Package managers, workspace tools, and cache mechanisms in use

## Procedure

1. Map the current build graph, task entrypoints, and where time is spent.
2. Identify repeated config, unnecessary serialization, stale targets, and places where generated artifacts are mixed with source.
3. Consolidate configuration where it is truly shared and split targets where locality will improve caching and comprehension.
4. Introduce or improve caching, incremental execution, and clear entrypoints without hiding behavior behind magical wrappers.
5. Validate the revised structure from a clean checkout and compare local and CI behavior.
6. Document the before-and-after graph, expected gains, and any adoption risks.

## Output shape

- Current pain summary
- Proposed build and layout changes
- Before-and-after build graph notes
- Expected gains
- Risks and migration steps
- Verification checklist

# Dependency Unity

Rationalize the dependency graph so shared code and versions stop fighting each other.

## When to invoke

- Multiple versions of the same dependency coexist without intent.
- Shared utility libraries are drifting or duplicating each other.
- A monorepo or multi-repo system has dependency churn that keeps breaking integration.

## Inputs required

- Package manifests and lockfiles
- Module or service boundaries
- Current version policy, if any
- Known dependency conflicts or incident history

## Procedure

1. Inventory direct and transitive dependencies across the participating modules or repos.
2. Group dependencies by role: runtime-critical, build-only, testing, shared utility, framework, and infrastructure.
3. Identify duplicate libraries, conflicting versions, diamond dependencies, and places where shared code has become an unowned dumping ground.
4. Decide for each conflict whether to converge, isolate, replace, or remove.
5. Update manifests and lockfiles in the smallest coherent slices, running compatibility tests as each slice lands.
6. Record ownership and upgrade cadence so the graph stays understandable after the cleanup.

## Output shape

- Dependency matrix
- Conflicts and duplication summary
- Convergence or isolation plan
- Patch summary
- Ownership and upgrade notes
- Remaining risks

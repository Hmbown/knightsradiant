# System Cartography

Map boundaries, dependencies, and the flows that matter.

## When to invoke

- The repo or service graph is unfamiliar.
- Incidents or changes keep crossing unexpected boundaries.
- A refactor needs a map before anyone proposes a new shape.

## Inputs required

- Repo tree, manifests, service list, or architectural notes
- Known runtime components: databases, queues, caches, external APIs
- Key workflows or request paths
- Ownership hints, if available

## Procedure

1. Inventory the major modules, services, packages, jobs, and data stores.
2. Trace the main request or event flows end to end, including ingress, state changes, and external dependencies.
3. Mark build-time versus run-time dependencies and note where they differ.
4. Identify ownership boundaries, hidden coupling, circular dependencies, and chokepoints.
5. Summarize the system in markdown form: adjacency list, layered map, or flow-oriented outline.
6. Highlight candidate seams where work could be isolated or simplified safely.

## Output shape

- Component inventory
- Primary flow map
- Dependency and ownership notes
- Hidden-coupling risks
- Candidate seams or refactor boundaries

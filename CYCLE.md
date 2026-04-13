# Rotation Protocol

A cycle is serialized perspective. Each order asks a different class of question and produces a hand-off artifact that constrains the next order's work. The point is not to make ten agents touch everything. The point is to avoid letting one lens dominate the whole effort.

Use one active order at a time. The current order may read prior artifacts, but it should not overwrite them casually. If a hand-off artifact is wrong, the receiving order should say why and either repair it or route the work through the exception path.

## Choosing how to enter

Two routing skills exist with different purposes:

- **choose-order** picks the narrowest single order that names the real constraint. Use it when you need one focused lens.
- **run-cycle** picks a fuller staged sequence when the task needs multiple lenses in order. Use it when the work spans multiple concerns, including risky migrations that need architecture, choreography, enforcement, and rollout protection.

On the same task, they may recommend different starting orders. That divergence is intentional: choose-order optimizes for "what matters most right now," run-cycle optimizes for "what sequence covers the full scope."

## Order modes

Some orders operate in more than one mode depending on timing:

- **Windrunner** has a *prospective shield* mode (before code is written) and a *retrospective shield* mode (reviewing an existing diff).
- **Truthwatcher** has a *diagnostic mode* (investigating a bug or incident) and a *pre-mortem mode* (defining what failure would look like before a risky change ships).

Both modes produce the same output contract for their order. The difference is timing, not rigor.

## Default forward cycle for greenfield work

### 1. Elsecaller
Start here because greenfield mistakes are usually decision mistakes, not typing mistakes. Elsecaller identifies the irreversible choices, compares viable shapes, and makes boundaries explicit before code starts accreting around assumptions.  
**Hand-off artifact:** ADR, system map, explicit constraints, non-goals, and open questions.

### 2. Willshaper
Move next to the ground truth of building: repo shape, module skeletons, build targets, service templates, task runners, and local setup. Willshaper turns architecture into a paved road so later work follows conventions instead of improvising them.  
**Hand-off artifact:** scaffold patch, build/bootstrap plan, directory layout, and setup checklist.

### 3. Stoneward
Harden the core before the feature set sprawls. Stoneward identifies critical paths, expected load, reliability assumptions, and the modules that other work will lean on.  
**Hand-off artifact:** load-bearing test plan, baseline benchmarks, failure assumptions, and performance or reliability budgets.

### 4. Bondsmith
Once the pieces exist, unify them. Bondsmith defines the contracts between modules and services, the dependency strategy, version boundaries, and rollout order so the system can change as one coherent whole.  
**Hand-off artifact:** compatibility matrix, dependency plan, interface notes, and integration checkpoints.

### 5. Lightweaver
Now make the surface truthful before it calcifies. Lightweaver rewrites names, public API shape, docs, examples, and configuration language so the system says what it actually does.  
**Hand-off artifact:** API guide, naming decisions, usage examples, and doc patch.

### 6. Truthwatcher
Before the code is stressed in the wild, make it observable. Truthwatcher ensures that incidents, regressions, and unknown behavior can be interrogated with evidence instead of guesswork.  
**Hand-off artifact:** telemetry plan, instrumentation patch, debug questions, and alert or dashboard outline.

### 7. Edgedancer
After the happy path is visible, walk the paths people forget. Edgedancer tests the error modes, empty states, retries, accessibility flows, slow networks, and low-frequency conditions that the main design never advertises.  
**Hand-off artifact:** edge-case matrix, a11y findings, recovery-path test list, and patch recommendations.

### 8. Dustbringer
Only now is it safe to delete aggressively. Dustbringer removes redundant layers, dead flags, stale adapters, and duplicate abstractions exposed by the prior steps.  
**Hand-off artifact:** deletion plan, simplification patch, migration notes, and tombstones for removed behavior.

### 9. Skybreaker
Once the real shape is known, encode the law. Skybreaker turns conventions and discovered invariants into lints, types, schemas, contract tests, and CI gates so they stop living in reviewer memory.  
**Hand-off artifact:** lint or contract rules, CI changes, exception policy, and regression gates.

### 10. Windrunner
End with the protective pass. Windrunner packages blast radius, rollout order, rollback steps, reviewer hotspots, and watch metrics so the change can land without heroics.  
**Hand-off artifact:** PR shield, rollout checklist, rollback plan, watchpoints, and risk note.

## Triage cycle for an incoming bug

### 1. Truthwatcher
Bug work starts with evidence. Truthwatcher freezes the symptom, reconstructs the timeline, narrows the hypothesis set, and avoids wasting time on fixes to stories nobody has verified.  
**Hand-off artifact:** incident note, reproduction status, hypothesis tree, and likely fault domain.

### 2. Edgedancer
Next, expand the symptom into the forgotten variants: permissions, retries, stale state, race windows, accessibility flows, empty inputs, and low-traffic routes. Bugs often hide in the branch nobody thought counted.  
**Hand-off artifact:** repro matrix across edge conditions, missing coverage list, and user-impact notes.

### 3. Stoneward
Now isolate the load-bearing risk. Stoneward decides whether the bug threatens correctness, capacity, durability, latency, or shared libraries, then writes the tests that prove the break and protect the core while fixing it.  
**Hand-off artifact:** failing characterization test, risk severity, and safety budget for the fix.

### 4. Dustbringer
Once the weak structure is exposed, remove it. Dustbringer deletes redundant logic, obsolete fallback layers, or tangled pathways that made the bug possible in the first place.  
**Hand-off artifact:** simplification patch, removed paths ledger, and migration notes if behavior moved.

### 5. Skybreaker
Then encode the lesson. Skybreaker adds the type rule, schema check, contract test, or lint gate that prevents the same bug class from slipping back in.  
**Hand-off artifact:** regression guard, enforcement diff, and explicit exception policy.

### 6. Windrunner
Finish with safe landing. Windrunner decides release order, backport strategy, rollback conditions, user or on-call communication, and what to watch after deploy.  
**Hand-off artifact:** hotfix packet, release note, blast radius summary, and rollback steps.

## Refactor cycle

### 1. Lightweaver
Refactors should begin by naming the lie. Lightweaver identifies misleading APIs, overburdened abstractions, rotten docs, and vocabulary drift so the cleanup aims at the truth instead of mere style.  
**Hand-off artifact:** current-vs-intended terminology map, API truth table, and doc debt list.

### 2. Elsecaller
Once the confusion is named, decide the new shape. Elsecaller compares alternative structures, picks boundaries, and records which moves are reversible and which are not.  
**Hand-off artifact:** refactor ADR, target architecture, migration phases, and non-goals.

### 3. Dustbringer
Then do the cutting. Dustbringer collapses dead layers, removes duplicate logic, retires obsolete routes, and reduces the system to fewer moving parts.  
**Hand-off artifact:** deletion plan, simplification patch, and staged removal checklist.

### 4. Bondsmith
Refactors often break at the seams, so Bondsmith re-stitches the interfaces. It coordinates dependency order, contract compatibility, and multi-module migration so the cleanup does not strand consumers.  
**Hand-off artifact:** bridge plan, compatibility matrix, dependency updates, and rollout order.

### 5. Skybreaker
After the new shape lands, codify it. Skybreaker makes the cleaner structure enforceable so the repo cannot quietly drift back to the old habits.  
**Hand-off artifact:** lint rules, contract tests, schema updates, and CI protections.

### 6. Stoneward
End by proving the refactor did not weaken the core. Stoneward compares before and after on latency, throughput, memory, failure handling, and reliability on the critical path.  
**Hand-off artifact:** benchmark comparison, characterization results, and unresolved risk list.

## Risky migration cycle

### 1. Elsecaller
Start by naming the irreversible choice. Risky migrations fail when a team treats a boundary change as a mere implementation detail. Elsecaller writes the migration ADR, compares at least one reversible alternative, and makes rollback constraints explicit before any phased rollout starts.  
**Hand-off artifact:** migration ADR, affected parties, compatibility constraints, and rollback assumptions.

### 2. Bondsmith
Once the target shape is chosen, choreograph the overlap period. Bondsmith defines who talks to whom in each phase, what remains backward-compatible, how backfills and bridges behave, and which signals must be green before the next phase can begin.  
**Hand-off artifact:** compatibility matrix, observability gates, rollout sequence, and migration/backfill notes.

### 3. Skybreaker
Before traffic shifts, encode the law. Skybreaker turns migration assumptions into contract tests, config/schema guards, and CI checks so the phased plan cannot drift silently in implementation.  
**Hand-off artifact:** enforcement packet, phase-advance rule, exception policy, and severity plan.

### 4. Windrunner
Finish by making the landing survivable. Windrunner packages blast radius, reviewer hotspots, abort thresholds, watch metrics, and rollback steps so the migration can move without requiring heroics from on-call.  
**Hand-off artifact:** merge-safety packet, rollout order, rollback plan, and open risks/owners.

## Minimum viable cycle

When ten orders are overkill, do not fake thoroughness. Run three lenses:

1. **A framer** — choose the one that best defines the problem.
   - Elsecaller for new design work
   - Truthwatcher for bugs
   - Lightweaver for refactors or API cleanup
2. **A builder or enforcer** — choose the order that makes the change real.
   - Willshaper for structure and scaffolding
   - Dustbringer for simplification and deletion
   - Skybreaker for encoded invariants
   - Stoneward for reliability-critical core paths
3. **A protector** — finish with Windrunner.

If you want one default small-task triplet for ordinary repo work, use **Lightweaver → Skybreaker → Windrunner**: make the change legible, encode its invariants, then make it safe to land.

## Exception hand-off graph

Exception paths are not failures of the framework. They are the designed route for "I cannot finish this order honestly because the real blocker lives elsewhere."

- **Elsecaller → Lightweaver** when the architecture dispute is actually a language problem and the system surface is still lying.
- **Willshaper → Elsecaller** when scaffolding is being asked to carry unresolved architecture.
- **Stoneward → Truthwatcher** when reliability concerns are still mostly speculation and need evidence first.
- **Bondsmith → Elsecaller** when coordination overhead or adapter count suggests the boundary itself is wrong.
- **Lightweaver → Elsecaller** when naming confusion is downstream of structural confusion.
- **Truthwatcher → Stoneward** when the evidence now points to a load-bearing reliability problem that needs characterization tests and kill-switch planning.
- **Edgedancer → Truthwatcher** when a forgotten path cannot be reproduced or observed well enough to reason about safely.
- **Dustbringer → Elsecaller** when deletion pressure reveals an unresolved boundary decision rather than mere residue.
- **Skybreaker → Bondsmith** when the invariant spans multiple systems and needs coordinated ownership.
- **Windrunner → Truthwatcher** when risk cannot yet be quantified because the necessary signals do not exist.

## Anti-patterns

Skipping an order creates a predictable blind spot. Skip Elsecaller and you get local implementation without a durable shape. Skip Lightweaver and you freeze misleading names and APIs into place. Skip Truthwatcher and incidents become folklore. Skip Edgedancer and users discover the unhappy paths for you. Skip Dustbringer and every cycle leaves more residue than it removes. Skip Skybreaker and rules survive only as reviewer memory. Skip Windrunner and the merge depends on heroics.

Running orders in parallel without synthesis is just as bad. You get architecture with no rollout story, docs for APIs whose contracts are still unstable, deletion before edge-path review, or observability stitched onto names that are about to change. One order should own the baton at a time. The artifact is the baton.

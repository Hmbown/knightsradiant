# Rotation Protocol

A cycle is serialized perspective. Each order asks a different class of question and produces a hand-off artifact that constrains the next order's work. The point is not to make ten agents touch everything. The point is to avoid letting one lens dominate the whole effort.

Use one active order at a time. The current order may read prior artifacts, but it should not overwrite them casually. If a hand-off artifact is wrong, the receiving order should say why and either repair it or route the work through the exception path.

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

## Anti-patterns

Skipping an order creates a predictable blind spot. Skip Elsecaller and you get local implementation without a durable shape. Skip Lightweaver and you freeze misleading names and APIs into place. Skip Truthwatcher and incidents become folklore. Skip Edgedancer and users discover the unhappy paths for you. Skip Dustbringer and every cycle leaves more residue than it removes. Skip Skybreaker and rules survive only as reviewer memory. Skip Windrunner and the merge depends on heroics.

Running orders in parallel without synthesis is just as bad. You get architecture with no rollout story, docs for APIs whose contracts are still unstable, deletion before edge-path review, or observability stitched onto names that are about to change. One order should own the baton at a time. The artifact is the baton.

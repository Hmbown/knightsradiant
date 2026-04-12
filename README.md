# Knights Radiant for Hermes

Knights Radiant is a public-facing Hermes profile + skill pack for structured engineering work.

It treats software work as a rotation of lenses rather than a single all-purpose persona. Each order represents a disciplined engineering stance: architecture, scaffolding, reliability, integration, naming, observability, edge cases, simplification, enforcement, and rollout safety.

The theme is mnemonic. The value is practical: a forced perspective shift catches blind spots that a single coding persona, reviewer, or engineer will routinely miss.

GitHub:
- https://github.com/Hmbown/knightsradiant

## What you get

- a reusable Hermes profile template under `profiles/knights-radiant/`
- a Hermes-loadable skill pack under `skills/knights-radiant/`
- canonical order docs under `agents/NN-order/AGENTS.md`
- local order subskills under `agents/NN-order/skills/`
- shared doctrine in `CYCLE.md` and `IDEALS.md`
- artifact templates under `templates/`
- examples under `docs/examples/`

## The ten orders

| Order | Primary engineering stance | One-line role |
|---|---|---|
| Windrunner | rollout safety | Protect the team and the users; make risky changes safe to land. |
| Skybreaker | enforcement | Turn expectations into enforceable law: lint, types, contracts, CI. |
| Dustbringer | simplification | Delete what is dead, split what is overgrown, and pay down structural debt. |
| Edgedancer | edge-path coverage | Cover forgotten paths: edge cases, recovery, accessibility, slow paths. |
| Truthwatcher | observability | See what is real: instrumentation, debugging, traces, and root-cause analysis. |
| Lightweaver | legibility | Make the system legible and honest through names, docs, and API shape. |
| Elsecaller | architecture | Plan the structure, compare alternatives, and choose boundaries deliberately. |
| Willshaper | scaffolding | Shape the repo, build, and scaffolding so the paved road is the right road. |
| Stoneward | reliability core | Hold the load-bearing core: reliability, capacity, performance, failure budgets. |
| Bondsmith | integration | Unite systems, teams, and dependencies without hiding the seams. |

## Install

### Prerequisites

- Hermes installed and working (`hermes --help`)
- an existing usable Hermes profile to clone from
- `python3` available on PATH
- macOS/Linux shell environment with `bash`

### Fast path: install the profile

```bash
git clone https://github.com/Hmbown/knightsradiant.git
cd knightsradiant
./install.sh
```

That creates a `knights-radiant` Hermes profile by cloning your active Hermes profile, then patches it to:
- set high reasoning effort
- install the Knights Radiant SOUL/persona
- add this repo's `skills/` directory as an external skill dir
- set the default display personality to `radiant`

Start it with:

```bash
hermes --profile knights-radiant
```

### Install under a custom profile name

```bash
./install.sh my-radiant-profile
```

### Skill-pack-only path

If you do not want a dedicated profile, add this repo's `skills/` directory to an existing Hermes profile:

```yaml
skills:
  external_dirs:
    - /absolute/path/to/knightsradiant/skills
```

Then restart Hermes or begin a fresh session and load:
- `choose-order`
- `run-cycle`
- one active order at a time, such as `elsecaller` or `windrunner`

## Verify install

After installation:

```bash
hermes --profile knights-radiant skills list | grep -E 'choose-order|run-cycle|windrunner|elsecaller'
```

Expected outcome:
- the profile exists
- the repo skill directory is attached
- Knights Radiant skills are discoverable

## How to use it

1. Read `CYCLE.md` and pick the cycle that matches the work.
2. Use `choose-order` if the first lens is unclear.
3. Use `run-cycle` when the task needs an intentional sequence rather than a single lens.
4. Load one active order at a time.
5. Produce that order's hand-off artifact before rotating.
6. Keep the previous artifact in context for the next order.

## Routing matrix

| If the task is mainly about... | Start with | Expected artifact |
|---|---|---|
| new subsystem shape or irreversible decisions | Elsecaller | ADR + system map + constraints |
| repo structure, generators, bootstrap, build paths | Willshaper | scaffold patch + setup checklist |
| hot paths, retries, correctness under strain | Stoneward | characterization tests + budgets |
| multi-service compatibility or rollout ordering | Bondsmith | compatibility matrix + rollout sequence |
| confusing names, docs, CLI/API shape | Lightweaver | naming decisions + API guide |
| incident triage, debugging, observability | Truthwatcher | incident note + telemetry plan |
| edge cases, retries, accessibility, recovery | Edgedancer | edge-case matrix + recovery test list |
| stale abstractions, dead code, compatibility residue | Dustbringer | deletion ledger + migration notes |
| turning norms into enforceable checks | Skybreaker | lint/contract rule + CI gate |
| blast radius, rollback, watchpoints | Windrunner | rollout packet + rollback plan |

## Three concrete examples

### Bug triage
Input:
- "Users occasionally get duplicate shipment records after retry storms."

Recommended path:
- Truthwatcher → Edgedancer → Stoneward

Artifacts:
- incident note
- edge-condition repro matrix
- failing characterization test and safety budget

### Risky migration
Input:
- "We need to split auth sessions into a new store without locking users out."

Recommended path:
- Elsecaller → Bondsmith → Windrunner

Artifacts:
- migration ADR
- compatibility matrix and rollout sequence
- rollback checklist and watchpoints

### API cleanup
Input:
- "The webhook client works, but the public config surface is confusing and reviewers keep catching contract drift."

Recommended path:
- Lightweaver → Skybreaker → Windrunner

Artifacts:
- naming/API clarification patch
- enforceable schema/contract gate
- reviewer-ready safety packet

## Repository layout

- `README.md` — package overview, install, and operating notes
- `CYCLE.md` — rotation protocol and hand-off logic
- `IDEALS.md` — shared engineering ethics inherited by every order
- `agents/NN-order/AGENTS.md` — canonical order definitions
- `agents/NN-order/skills/*.md` — recurring local procedures for that order
- `skills/knights-radiant/` — Hermes entrypoint skills
- `profiles/knights-radiant/` — profile template, installer, and SOUL
- `templates/` — artifact templates for ADRs, matrices, plans, and checklists
- `docs/examples/` — example task flows and outputs

## Doc hierarchy

- top-level docs = shared model and install story
- `agents/` = source of truth for how each order behaves
- `skills/knights-radiant/` = Hermes entrypoints and routing layer
- `agents/*/skills/` = local reusable procedures for the active order
- `templates/` = copyable output shapes and hand-off artifacts

## Updating

If you installed via clone + `./install.sh`:

```bash
cd knightsradiant
git pull
```

What updates immediately:
- skill-pack content in `skills/` referenced from the repo path
- shared docs and templates in the repo

What does not update automatically:
- copied profile files already written into `~/.hermes/profiles/<name>/`, especially `SOUL.md`

If profile-level behavior changes materially, rerun the installer into a fresh profile name or manually compare the repo's profile files against your installed profile.

## Uninstall

Remove the created profile:

```bash
hermes profile delete knights-radiant
```

If you used the skill-pack-only path, remove the repo path from your profile's `skills.external_dirs` list.

## When not to use Knights Radiant

Do not force the framework onto tiny throwaway tasks, one-line fixes, or work where the output does not benefit from structured review. The minimum viable cycle is better than theatrical thoroughness.

## Caveat

This project is experimental by design. If the output feels theatrical but does not improve decisions, tests, docs, observability, integration quality, or rollout safety, strip the theme and keep the discipline.

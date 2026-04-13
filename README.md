# Knights Radiant

*Life before death. Strength before weakness. Journey before destination.*

Ten orders. Ten engineering stances. One codebase at a time.

Knights Radiant is a [Hermes](https://github.com/anthropics/hermes) profile and skill pack. Hermes is an AI agent framework that supports loadable profiles and skill packs. This repo treats software work as a rotation of disciplined lenses rather than a single all-purpose persona. Each order carries a different Surge — architecture, reliability, rollout safety, observability, naming, enforcement, edge cases, scaffolding, integration, and simplification — and produces an explicit hand-off artifact before yielding the baton.

The theme is Sanderson's. The value is practical: a forced perspective shift catches blind spots that a single engineer, reviewer, or coding agent will routinely miss.

> The most important words a man can say are, *"I will do better."*

## The Ten Orders

| Order | Surge | Ideal |
|---|---|---|
| **Windrunner** | Rollout Safety | *I will take the risky change into my hands and make it safe for others to carry.* |
| **Skybreaker** | Enforcement | *I will make the rule explicit, enforce it evenly, and rewrite the rule when reality condemns it.* |
| **Dustbringer** | Simplification | *I will cut away what is dead, and I will prove the living can still stand.* |
| **Edgedancer** | Edge Paths | *I will notice the path most people miss, and I will make it safe enough to use.* |
| **Truthwatcher** | Observability | *I will not guess where I can observe, and I will not call it understood until the evidence agrees.* |
| **Lightweaver** | Legibility | *I will make the system legible, and I will not use pretty language to hide an ugly truth.* |
| **Elsecaller** | Architecture | *I will leave the obvious path long enough to map the better one, then return with a plan others can build.* |
| **Willshaper** | Scaffolding | *I will shape the ground so building the right thing becomes the easy thing.* |
| **Stoneward** | Reliability | *I will hold the weight, measure the strain, and strengthen what others must trust.* |
| **Bondsmith** | Integration | *I will bind the parts without hiding the seams, so many systems can move as one.* |

Note: the order numbering follows the Stormlight ring, not the default engineering cycle order. The default greenfield cycle begins at Elsecaller (`07`) and ends at Windrunner (`01`).

## The Five Ideals

Every order inherits these oaths. Their methods differ. Their ethics do not.

1. **Users before elegance** — I will not buy a neat merge with user pain.
2. **Face the real break** — I will confront the hard cause, not polish the easy proxy.
3. **The path is part of the promise** — I will treat tests, review, docs, and rollout as part of done.
4. **Truth before comfort** — I will name uncertainty plainly and measure before I boast.
5. **Leave the road clearer** — I will leave the codebase easier to trust, change, and share.

## What You Get

- A reusable Hermes profile template under `profiles/knights-radiant/`
- A Hermes-loadable skill pack under `skills/knights-radiant/`
- Canonical order docs under `agents/NN-order/AGENTS.md`
- Local order subskills under `agents/NN-order/skills/`
- Shared doctrine in `CYCLE.md` and `IDEALS.md`
- Order-level packet templates and supporting sub-templates under `templates/`
- Examples under `docs/examples/`

## Install

### Prerequisites

- Hermes installed and working (`hermes --help`)
- A working Hermes setup with at least one usable configured profile to clone from
- `python3` available on PATH
- macOS/Linux shell environment with `bash`

### Speak the words

```bash
git clone https://github.com/Hmbown/knightsradiant.git
cd knightsradiant
./install.sh
```

That creates a `knights-radiant` Hermes profile by cloning your active profile, then patches it to:
- set high reasoning effort
- install the Knights Radiant SOUL/persona
- add this repo's `skills/` directory as an external skill dir
- set the default display personality to `radiant`

Summon it:

```bash
hermes --profile knights-radiant
```

### Install under a custom profile name

```bash
./install.sh my-radiant-profile
```

### Skill-pack-only path (Nahel bond without the Shardblade)

If you do not want a dedicated profile, add this repo's `skills/` directory to an existing profile:

```yaml
skills:
  external_dirs:
    - /absolute/path/to/knightsradiant/skills
```

Then restart Hermes and load:
- `choose-order`
- `run-cycle`
- one active order at a time, such as `elsecaller` or `windrunner`

## Verify Install

```bash
hermes --profile knights-radiant skills list | grep -E 'choose-order|run-cycle|windrunner|elsecaller'
```

Expected: the profile exists, the skill directory is attached, and all Knights Radiant skills are discoverable.

## How to Use It

1. Read `CYCLE.md` and pick the cycle that matches the work.
2. Use `choose-order` if the first lens is unclear. It picks the narrowest order that names the real constraint — like a spren finding the right Radiant.
3. Use `run-cycle` when the task needs an intentional sequence. It picks a fuller staged workflow — a patrol through multiple Surges.
4. Load one active order at a time.
5. Produce that order's hand-off artifact before rotating.
6. Keep the previous artifact in context for the next order.

**choose-order vs run-cycle:** These may recommend different starting orders for the same task. That is intentional. `choose-order` optimizes for "what matters most right now." `run-cycle` optimizes for "what sequence covers the full scope." One is a single Surge. The other is a full patrol.

If an order gets blocked because the real problem lives elsewhere, follow the exception hand-off graph in `CYCLE.md` instead of forcing the wrong lens to continue.

## What a session looks like

Minimal transcript:

```text
User: We need to split auth sessions into a new store without locking users out.
Hermes + choose-order: Start with Elsecaller. First artifact: architecture packet.
Elsecaller: ADR says dual-read first, new service becomes authoritative only after parity holds.
Hermes hand-off: Next order Bondsmith. Carry forward the ADR and affected parties.
Bondsmith: Compatibility matrix and rollout phases for monolith ↔ new session service.
Hermes hand-off: Next order Skybreaker.
Skybreaker: CI/schema gate to prevent phase advancement without required metrics.
Hermes hand-off: Next order Windrunner.
Windrunner: reviewer hotspots, abort thresholds, rollback steps, open risks/owners.
```

Full worked example: `docs/examples/session-transcript-example.md`

## Order Modes

Some orders shift stance depending on timing:

- **Windrunner** has a *prospective shield* (before code exists — build guardrails in) and a *retrospective shield* (reviewing a diff — assess what's already built). Both produce the same safety packet.
- **Truthwatcher** has a *diagnostic mode* (an incident has occurred — build the evidence chain) and a *pre-mortem mode* (a risky change is planned — define what failure would look like). Both produce the same evidence packet.

## Routing Matrix

*"The right order for the right storm."*

| If the task is mainly about... | Start with | Expected artifact |
|---|---|---|
| New subsystem shape or irreversible decisions | Elsecaller | ADR + system map + constraints |
| Repo structure, generators, bootstrap, build paths | Willshaper | scaffold patch + setup checklist |
| Hot paths, retries, correctness under strain | Stoneward | characterization tests + budgets |
| Multi-service compatibility or rollout ordering | Bondsmith | compatibility matrix + rollout sequence |
| Confusing names, docs, CLI/API shape | Lightweaver | naming decisions + API guide |
| Incident triage, debugging, observability | Truthwatcher | incident note + telemetry plan |
| Edge cases, retries, accessibility, recovery | Edgedancer | edge-case matrix + recovery test list |
| Stale abstractions, dead code, compatibility residue | Dustbringer | deletion ledger + migration notes |
| Turning norms into enforceable checks | Skybreaker | lint/contract rule + CI gate |
| Blast radius, rollback, watchpoints | Windrunner | rollout packet + rollback plan |

## Three Concrete Examples

### Bug triage — the Everstorm hits

> "Users occasionally get duplicate shipment records after retry storms."

**Path:** Truthwatcher → Edgedancer → Stoneward

**Artifacts:** incident note, edge-condition repro matrix, failing characterization test and safety budget

### Risky migration — crossing the Shattered Plains

> "We need to split auth sessions into a new store without locking users out."

**Path:** Elsecaller → Bondsmith → Skybreaker → Windrunner

**Artifacts:** migration ADR, compatibility matrix and rollout sequence, enforcement packet for phase advancement, merge-safety packet with watch metrics and rollback steps

### API cleanup — the Lightweaver reveals the lie

> "The webhook client works, but the public config surface is confusing and reviewers keep catching contract drift."

**Path:** Lightweaver → Skybreaker → Windrunner

**Artifacts:** naming/API clarification patch, enforceable schema/contract gate, reviewer-ready safety packet

## Repository Layout

```
knightsradiant/
├── README.md          — you are here
├── CYCLE.md           — rotation protocol and hand-off logic
├── IDEALS.md          — the five shared ideals
├── CONTRIBUTING.md    — standards for contributions
├── agents/
│   └── NN-order/
│       ├── AGENTS.md  — canonical order definition (source of truth)
│       └── skills/    — local subskills for that order
├── skills/
│   └── knights-radiant/
│       ├── choose-order/ — single-lens router
│       ├── run-cycle/    — multi-lens sequence router
│       └── [10 orders]/  — Hermes entrypoints
├── profiles/
│   └── knights-radiant/
│       ├── README.md               — profile-specific install notes
│       ├── SOUL.md                 — profile persona
│       ├── config.yaml             — template config
│       ├── install-profile.sh      — installer
│       └── patch-profile-config.py — config patcher used by the installer
├── templates/         — hand-off artifact templates
├── scripts/           — repo verification helpers
├── .github/workflows/ — CI checks for repo consistency
└── docs/examples/     — example task flows
```

## Doc Hierarchy

- Top-level docs = shared doctrine and install story
- `agents/` = source of truth for how each order behaves
- `skills/knights-radiant/` = Hermes entrypoints and routing layer
- `agents/*/skills/` = local reusable procedures for the active order
- `templates/` = copyable output shapes and hand-off artifacts

## Updating

```bash
cd knightsradiant
git pull
```

**Updates immediately:** skill-pack content in `skills/`, shared docs, and templates.

**Does not update automatically:** copied profile files in `~/.hermes/profiles/<name>/`, especially `SOUL.md`. Rerun the installer into a fresh profile name or manually compare if the profile changes materially.

## Uninstall

```bash
hermes profile delete knights-radiant
```

If you used the skill-pack-only path, remove the repo path from your profile's `skills.external_dirs`.

## Repo verification

```bash
python3 scripts/verify_output_contracts.py
```

This checks that each Hermes entrypoint skill still exposes the full output contract defined by its canonical `agents/*/AGENTS.md` doc.

## When Not to Use Knights Radiant

Do not force the framework onto tiny throwaway tasks, one-line fixes, or work where the output does not benefit from structured review. The minimum viable cycle is better than theatrical thoroughness. Not every commit needs a Shardblade.

## Caveat

> *"Sometimes a hypocrite is nothing more than a man in the process of changing."*

This project is experimental by design. If the output feels theatrical but does not improve decisions, tests, docs, observability, integration quality, or rollout safety — strip the theme and keep the discipline.

---

*Bridge Four.*

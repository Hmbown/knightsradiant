# Knights Radiant profile template

This profile is intended to be created by cloning a working Hermes profile and then applying only the Knights Radiant-specific changes.

Prerequisite: you need a working Hermes installation with at least one configured profile that `hermes profile create --clone` can copy.

## Why clone first

- preserves provider/auth setup already known to work
- avoids shipping secrets in this repo
- keeps your existing tool enablement unless you intentionally change it
- makes the profile safer to install on top of an already-working Hermes environment

## Install

From a local clone of the GitHub repo:

```bash
git clone https://github.com/Hmbown/knightsradiant.git
cd knightsradiant
./install.sh
```

Or from repo root if already cloned:

```bash
./profiles/knights-radiant/install-profile.sh
```

Optional custom profile name:

```bash
./profiles/knights-radiant/install-profile.sh my-radiant-profile
```

## What the installer changes

- clones your active Hermes profile
- replaces the cloned `SOUL.md` with the Knights Radiant persona
- ensures `agent.reasoning_effort: high`
- ensures `display.personality: radiant`
- adds this repo's `skills/` directory to `skills.external_dirs`
- injects a `radiant` personality prompt if missing

## Verification

After install:

```bash
hermes --profile knights-radiant skills list | grep -E 'choose-order|run-cycle|elsecaller|windrunner'
```

## Failure modes

- `hermes` not on PATH
- `python3` not on PATH
- target profile already exists
- your active Hermes profile cannot be cloned
- repo path moved after installation, breaking the configured external skill directory

## Updating

`git pull` updates repo-hosted skills immediately because the profile points at the repo's `skills/` directory.

If the profile template itself changes, compare:
- `profiles/knights-radiant/SOUL.md`
- `profiles/knights-radiant/config.yaml`

against your installed profile and either patch manually or reinstall to a fresh profile name.

# Contributing

Thanks for contributing to Knights Radiant.

## Project standard

This repo should be:
- useful to a real Hermes operator
- respectful to the source material without turning into cosplay
- explicit about inputs, outputs, and hand-off artifacts
- practical enough that another engineer can use it under time pressure

## What good contributions look like

Good changes usually improve one of these:
- install UX
- skill discoverability
- artifact templates
- routing clarity
- order completeness and consistency
- example quality
- GitHub/project hygiene

## Content standards

### For every Hermes skill
Include, when relevant:
- invoke when
- inputs required
- procedure
- output shape
- example invocation
- when not to use it
- next hand-off target

### For every order doc
Maintain these sections:
- ideal
- stance
- modes (if the order operates differently depending on timing or context)
- what this order looks for
- what it refuses to do
- output contract (each output item should be specific enough that two different engineers would produce structurally similar artifacts)
- hand-off protocol
- failure mode

## Tone standard

Keep the order names and mnemonic structure.
Do not write in character. Do not make the repo feel like roleplay.
Use plain engineering prose in bodies. One memorable line is fine; pages of flourish are not.

## Local verification

Run before opening a PR:

```bash
bash -n install.sh
bash -n profiles/knights-radiant/install-profile.sh
python3 scripts/verify_output_contracts.py
python3 - <<'PY'
from pathlib import Path
root = Path('.')
assert (root / 'README.md').exists()
assert (root / 'skills' / 'knights-radiant').exists()
assert (root / 'profiles' / 'knights-radiant').exists()
print('basic repo checks passed')
PY
```

## Pull request checklist

- docs updated if behavior changed
- install flow checked if profile/install files changed
- no stale placeholder paths introduced
- examples still match real repo paths
- change improves operator usefulness, not just theme density

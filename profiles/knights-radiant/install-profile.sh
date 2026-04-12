#!/usr/bin/env bash
set -euo pipefail

PROFILE_NAME="${1:-knights-radiant}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
TARGET_DIR="$HOME/.hermes/profiles/$PROFILE_NAME"
TARGET_CONFIG="$TARGET_DIR/config.yaml"
TARGET_SOUL="$TARGET_DIR/SOUL.md"

fail() {
  echo "error: $*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail "$1 is required but not on PATH"
}

require_cmd hermes
require_cmd python3

[ -d "$REPO_ROOT" ] || fail "repo root not found: $REPO_ROOT"
[ -d "$SKILLS_DIR" ] || fail "skills dir not found: $SKILLS_DIR"
[ -f "$REPO_ROOT/profiles/knights-radiant/SOUL.md" ] || fail "profile SOUL missing"
[ ! -d "$TARGET_DIR" ] || fail "profile already exists: $TARGET_DIR"

echo "== Knights Radiant profile install =="
echo "repo root:      $REPO_ROOT"
echo "skills dir:     $SKILLS_DIR"
echo "target profile: $PROFILE_NAME"
echo "target dir:     $TARGET_DIR"
echo

hermes profile create "$PROFILE_NAME" --clone
cp "$REPO_ROOT/profiles/knights-radiant/SOUL.md" "$TARGET_SOUL"

python3 - "$TARGET_CONFIG" "$SKILLS_DIR" <<'PY'
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
skills_dir = str(Path(sys.argv[2]).resolve())
text = config_path.read_text()
lines = text.splitlines()

# Remove stale placeholder path if present.
lines = [line for line in lines if line.strip() != '- REPO_ROOT/skills']

if not any(line.startswith('agent:') for line in lines):
    lines += ['', 'agent:']
if not any(line.startswith('display:') for line in lines):
    lines += ['', 'display:']
if not any(line.startswith('skills:') for line in lines):
    lines += ['', 'skills:', '  external_dirs:']

# Helper to ensure a line exists immediately after a section start if missing anywhere.
def ensure_under(section, key_line):
    global lines
    if any(line.strip().startswith(key_line.strip()) for line in lines):
        return
    for i, line in enumerate(lines):
        if line == section:
            lines.insert(i + 1, key_line)
            return

ensure_under('agent:', '  tool_use_enforcement: auto')
ensure_under('agent:', '  reasoning_effort: high')
ensure_under('display:', '  personality: radiant')

# Ensure personalities block exists.
if not any(line.strip() == 'personalities:' for line in lines):
    for i, line in enumerate(lines):
        if line == 'agent:':
            lines.insert(i + 1, '  personalities:')
            break

# Ensure radiant personality exists.
if not any(line.strip().startswith('radiant:') for line in lines):
    for i, line in enumerate(lines):
        if line.strip() == 'personalities:':
            block = [
                '    radiant: >-',
                '      You are Knights Radiant for engineering work. Choose the correct order,',
                '      use one active order at a time, and produce explicit hand-off artifacts.',
            ]
            lines[i + 1:i + 1] = block
            break

# Ensure external_dirs block exists.
if not any(line.strip() == 'external_dirs:' for line in lines):
    for i, line in enumerate(lines):
        if line == 'skills:':
            lines.insert(i + 1, '  external_dirs:')
            break

skill_line = f'    - {skills_dir}'
if skill_line not in lines:
    for i, line in enumerate(lines):
        if line.strip() == 'external_dirs:':
            lines.insert(i + 1, skill_line)
            break

# Normalize duplicates for the main skills dir while preserving order.
seen = set()
normalized = []
for line in lines:
    if line.strip().startswith('- '):
        if line in seen:
            continue
        seen.add(line)
    normalized.append(line)

config_path.write_text('\n'.join(normalized) + '\n')
PY

python3 - "$TARGET_CONFIG" "$SKILLS_DIR" <<'PY'
import sys
from pathlib import Path

config = Path(sys.argv[1]).read_text()
skills_dir = str(Path(sys.argv[2]).resolve())
if f'    - {skills_dir}' not in config:
    raise SystemExit('configured skills dir missing from profile config')
if 'REPO_ROOT/skills' in config:
    raise SystemExit('stale REPO_ROOT/skills placeholder still present')
if 'personality: radiant' not in config:
    raise SystemExit('radiant display personality missing')
if 'reasoning_effort: high' not in config:
    raise SystemExit('high reasoning effort missing')
PY

echo
echo "install complete"
echo "verify with: hermes --profile $PROFILE_NAME skills list | grep -E 'choose-order|run-cycle|windrunner|elsecaller'"
echo "start with:   hermes --profile $PROFILE_NAME"

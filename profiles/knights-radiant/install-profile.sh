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

python3 "$REPO_ROOT/profiles/knights-radiant/patch-profile-config.py" "$TARGET_CONFIG" "$SKILLS_DIR"

echo
echo "install complete"
echo "verify with: hermes --profile $PROFILE_NAME skills list | grep -E 'choose-order|run-cycle|windrunner|elsecaller'"
echo "start with:   hermes --profile $PROFILE_NAME"

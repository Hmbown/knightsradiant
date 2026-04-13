#!/usr/bin/env python3

"""Normalize a Hermes profile config for Knights Radiant installation."""

from __future__ import annotations

import sys
from pathlib import Path

RADIANT_BLOCK = [
    '    radiant: >-',
    '      You are Knights Radiant for engineering work. Choose the correct order,',
    '      use one active order at a time, and produce explicit hand-off artifacts.',
]


def is_top_level_key(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not line.startswith((' ', '\t', '#')) and not stripped.startswith('- ')


def next_top_level_index(lines: list[str], start: int) -> int:
    for idx in range(start, len(lines)):
        if is_top_level_key(lines[idx]):
            return idx
    return len(lines)


def ensure_section(lines: list[str], name: str) -> tuple[int, int]:
    header = f'{name}:'
    for idx, line in enumerate(lines):
        if line == header:
            return idx, next_top_level_index(lines, idx + 1)
    if lines and lines[-1] != '':
        lines.append('')
    lines.append(header)
    idx = len(lines) - 1
    return idx, len(lines)


def set_section_scalar(lines: list[str], section: str, key: str, value: str) -> None:
    start, end = ensure_section(lines, section)
    prefix = f'  {key}:'
    indices = [idx for idx in range(start + 1, end) if lines[idx].startswith(prefix)]
    desired = f'  {key}: {value}'
    if indices:
        lines[indices[0]] = desired
        for idx in reversed(indices[1:]):
            del lines[idx]
    else:
        lines.insert(start + 1, desired)


def block_end(lines: list[str], start: int, limit: int, indent: int) -> int:
    limit = min(limit, len(lines))
    for idx in range(start + 1, limit):
        stripped = lines[idx].strip()
        if stripped and not lines[idx].startswith(' ' * (indent + 1)):
            return idx
    return limit


def sync_personalities(lines: list[str]) -> None:
    start, end = ensure_section(lines, 'agent')
    header = '  personalities:'
    header_indices = [idx for idx in range(start + 1, end) if lines[idx] == header]

    other_entries: list[list[str]] = []
    insert_at = end
    if header_indices:
        insert_at = header_indices[0]
        for header_idx in header_indices:
            sub_end = block_end(lines, header_idx, end, indent=2)
            idx = header_idx + 1
            while idx < sub_end:
                line = lines[idx]
                if line.startswith('    ') and not line.startswith('      '):
                    entry_end = block_end(lines, idx, sub_end, indent=4)
                    entry = lines[idx:entry_end]
                    if not line.strip().startswith('radiant:'):
                        other_entries.append(entry)
                    idx = entry_end
                else:
                    idx += 1
        for header_idx in reversed(header_indices):
            sub_end = block_end(lines, header_idx, end, indent=2)
            del lines[header_idx:sub_end]
    consolidated = [header, *RADIANT_BLOCK]
    for entry in other_entries:
        consolidated.extend(entry)
    lines[insert_at:insert_at] = consolidated


def sync_external_dirs(lines: list[str], skills_dir: str) -> None:
    start, end = ensure_section(lines, 'skills')
    header = '  external_dirs:'
    header_indices = [idx for idx in range(start + 1, end) if lines[idx] == header or lines[idx].startswith(f'{header} ')]

    items: list[str] = []
    insert_at = end
    if header_indices:
        insert_at = header_indices[0]
        for header_idx in header_indices:
            sub_end = block_end(lines, header_idx, end, indent=2)
            for line in lines[header_idx + 1:sub_end]:
                stripped = line.strip()
                if stripped.startswith('- '):
                    item = stripped[2:]
                    if item != 'REPO_ROOT/skills' and item not in items:
                        items.append(item)
        for header_idx in reversed(header_indices):
            sub_end = block_end(lines, header_idx, end, indent=2)
            del lines[header_idx:sub_end]
    if skills_dir not in items:
        items.append(skills_dir)
    consolidated = [header, *[f'    - {item}' for item in items]]
    lines[insert_at:insert_at] = consolidated


def validate(lines: list[str], skills_dir: str) -> None:
    agent_start, agent_end = ensure_section(lines, 'agent')
    display_start, display_end = ensure_section(lines, 'display')
    skills_start, skills_end = ensure_section(lines, 'skills')

    agent_reasoning = [line for line in lines[agent_start + 1:agent_end] if line.startswith('  reasoning_effort:')]
    if agent_reasoning != ['  reasoning_effort: high']:
        raise SystemExit('agent.reasoning_effort did not normalize to high')

    agent_enforcement = [line for line in lines[agent_start + 1:agent_end] if line.startswith('  tool_use_enforcement:')]
    if agent_enforcement != ['  tool_use_enforcement: auto']:
        raise SystemExit('agent.tool_use_enforcement did not normalize to auto')

    display_personality = [line for line in lines[display_start + 1:display_end] if line.startswith('  personality:')]
    if display_personality != ['  personality: radiant']:
        raise SystemExit('display.personality did not normalize to radiant')

    personality_headers = [idx for idx in range(agent_start + 1, agent_end) if lines[idx] == '  personalities:']
    if len(personality_headers) != 1:
        raise SystemExit('agent.personalities block is missing or duplicated')
    personality_block = lines[personality_headers[0] + 1:block_end(lines, personality_headers[0], agent_end, indent=2)]
    if not any(line.strip().startswith('radiant:') for line in personality_block):
        raise SystemExit('radiant personality missing from agent.personalities')

    external_headers = [idx for idx in range(skills_start + 1, skills_end) if lines[idx] == '  external_dirs:']
    if len(external_headers) != 1:
        raise SystemExit('skills.external_dirs block is missing or duplicated')
    external_block = lines[external_headers[0] + 1:block_end(lines, external_headers[0], skills_end, indent=2)]
    expected_line = f'    - {skills_dir}'
    if expected_line not in external_block:
        raise SystemExit('configured skills dir missing from skills.external_dirs')
    if any('REPO_ROOT/skills' in line for line in external_block):
        raise SystemExit('stale REPO_ROOT/skills placeholder still present')


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit('usage: patch-profile-config.py <config_path> <skills_dir>')

    config_path = Path(sys.argv[1])
    skills_dir = str(Path(sys.argv[2]).resolve())
    lines = config_path.read_text().splitlines()
    lines = [line for line in lines if line.strip() != '- REPO_ROOT/skills']

    set_section_scalar(lines, 'agent', 'reasoning_effort', 'high')
    set_section_scalar(lines, 'agent', 'tool_use_enforcement', 'auto')
    set_section_scalar(lines, 'display', 'personality', 'radiant')
    sync_personalities(lines)
    sync_external_dirs(lines, skills_dir)
    validate(lines, skills_dir)

    config_path.write_text('\n'.join(lines) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ORDER_MAP = {
    '01-windrunner': 'windrunner',
    '02-skybreaker': 'skybreaker',
    '03-dustbringer': 'dustbringer',
    '04-edgedancer': 'edgedancer',
    '05-truthwatcher': 'truthwatcher',
    '06-lightweaver': 'lightweaver',
    '07-elsecaller': 'elsecaller',
    '08-willshaper': 'willshaper',
    '09-stoneward': 'stoneward',
    '10-bondsmith': 'bondsmith',
}


def parse_bullets(text: str, start_header: str, end_header: str):
    if start_header not in text or end_header not in text:
        raise ValueError(f'missing section between {start_header!r} and {end_header!r}')
    section = text.split(start_header, 1)[1].split(end_header, 1)[0]
    return [line.strip()[2:].strip() for line in section.splitlines() if line.strip().startswith('- ')]


def main() -> int:
    failures = []
    for agent_dir, skill_name in ORDER_MAP.items():
        agent_path = ROOT / 'agents' / agent_dir / 'AGENTS.md'
        skill_path = ROOT / 'skills' / 'knights-radiant' / skill_name / 'SKILL.md'
        agent_text = agent_path.read_text()
        skill_text = skill_path.read_text()

        agent_bullets = parse_bullets(agent_text, '## Output contract', '## Tools & skills')
        skill_bullets = parse_bullets(skill_text, 'At minimum, include:', 'Do not omit required output items from the canonical output contract, even if you summarize elsewhere.')

        if agent_bullets != skill_bullets:
            failures.append((agent_dir, agent_bullets, skill_bullets))

    if failures:
        print('Output contract drift detected:')
        for agent_dir, agent_bullets, skill_bullets in failures:
            print(f'\n- {agent_dir}')
            print('  AGENTS.md:')
            for bullet in agent_bullets:
                print(f'    - {bullet}')
            print('  SKILL.md:')
            for bullet in skill_bullets:
                print(f'    - {bullet}')
        return 1

    print('Output contract consistency check passed for all order skills.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

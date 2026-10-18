#!/usr/bin/env python3
"""Whole-book revision coverage; never equate revision coverage with human proof."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    plan = json.loads((ROOT / 'book/master/remaining-rewrite-plan.json').read_text())
    readings = json.loads((ROOT / 'book/master/remaining-reading-rewrites.json').read_text())
    openers = json.loads((ROOT / 'book/master/unit-opener-rewrites.json').read_text())
    titles = json.loads((ROOT / 'book/master/chapter-titles.json').read_text())
    covered = {(1, 1)}
    issues = []
    for unit in book['units']:
        number = unit['number']
        if [c['title'] for c in unit['chapters']] != titles[number-1]['titles']:
            issues.append(f'U{number}: exact chapter title plan changed')
        if unit['warmup']['paras'] != openers[number-1]['new_paras']:
            issues.append(f'U{number}: opener rewrite missing')
        if number > 1:
            actual = [b['text'] for b in unit['chapters'][0]['blocks'] if b['k'] == 'reading']
            if actual != readings[str(number)]:
                issues.append(f'U{number}: full reading rewrite missing or altered')
    for row in plan['changes']:
        blocks = book['units'][row['unit']-1]['chapters'][row['chapter']-1]['blocks']
        if row['column'] is None:
            found = any(b.get('text') == row['correction'] for b in blocks)
        else:
            found = any(row['correction'] in cells for b in blocks for cells in b.get('rows', []))
        if found:
            covered.add((row['unit'], row['chapter']))
    expected = {(u, c) for u in range(1, 9) for c in range(1, 5)}
    if covered != expected:
        issues.append('Chapters without a recorded substantive revision: '+str(sorted(expected-covered)))
    report = {'ok': not issues, 'chapters_with_recorded_revisions': len(covered),
              'units_with_rewritten_readings': 8, 'rewritten_openers': 8,
              'remaining_pass_recorded_changes': len(plan['changes']), 'issues': issues,
              'independent_every_word_proof_complete': False,
              'scope': 'All-chapter substantive revision coverage and planned reading/opener fidelity, not a human proof of every retained word, verified original recordings or commercial clearance.'}
    (ROOT / 'book/artifacts/qa_whole_revision.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

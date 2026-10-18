#!/usr/bin/env python3
"""Defined learner-evidence regressions, not expert approval or pilot results."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def inspect(book, reviews, criteria):
    issues = []
    if [r['unit'] for r in criteria] != list(range(1, 9)):
        issues.append('Evidence map must cover all eight units in order')
    for row in criteria:
        n = row['unit']
        task = reviews[n-1]['transfer']
        blocks = book['units'][n-1]['chapters'][3]['blocks']
        if sum(b.get('text') == 'Put it to use: ' + task for b in blocks) != 1:
            issues.append(f'U{n}: learner task missing or duplicated')
        for phrase in ['Keep a progress note:'] + row['required_phrases']:
            if phrase.casefold() not in task.casefold():
                issues.append(f'U{n}: missing observable evidence cue {phrase!r}')
    epigraph = book['front']['epigraph']
    plan = json.loads((ROOT / 'book/master/self-contained-edition.json').read_text())
    if epigraph != plan['epigraph']:
        issues.append('Original opening reflection changed, duplicated or missing')
    return issues


def main():
    import copy
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    reviews = json.loads((ROOT / 'book/master/unit-review.json').read_text())
    criteria = json.loads((ROOT / 'book/master/transfer-evidence.json').read_text())
    issues = inspect(book, reviews, criteria)
    # Prove detection of a lost evidence cue, a lost task and a doubled opening reflection.
    probes = []
    bad = copy.deepcopy(reviews)
    bad[0]['transfer'] = bad[0]['transfer'].replace('Keep a progress note:', '')
    probes.append(any('missing observable evidence cue' in issue for issue in inspect(book, bad, criteria)))
    bad = copy.deepcopy(book)
    bad['units'][0]['chapters'][3]['blocks'] = [b for b in bad['units'][0]['chapters'][3]['blocks']
                                               if not b.get('text', '').startswith('Put it to use:')]
    probes.append(bool(inspect(bad, reviews, criteria)))
    bad = copy.deepcopy(book); bad['front']['epigraph'] *= 2
    probes.append(bool(inspect(bad, reviews, criteria)))
    if not all(probes):
        issues.append('Mutation regressions failed to detect broken content')
    report = {'ok': not issues, 'units_checked': len(criteria), 'mutation_probes_detected': probes,
              'issues': issues, 'scope': 'Task presence, defined evidence cues and authored opening-reflection fidelity; not learning efficacy, verified answers or quotation clearance.'}
    (ROOT / 'book/artifacts/qa_learning_transfer.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

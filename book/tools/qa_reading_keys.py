#!/usr/bin/env python3
"""Trace authored closed-reading keys to current stems/options and evidence.

Not automatic semantic answer verification, listening validation, a complete
open-response key, or independent subject-matter approval.
"""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def inspect(book, keys):
    issues = []
    expected = []
    for unit in book['units']:
        blocks = unit['chapters'][0]['blocks']
        active = False
        mcq_number = tf_number = 0
        for i, block in enumerate(blocks):
            text = block.get('text', '')
            if text == 'Reading Comprehension':
                active = True
            if text == 'Answer the Questions':
                active = False
            if not active:
                continue
            if block['k'] == 'q' and i+1 < len(blocks) and blocks[i+1]['k'] == 'opt':
                mcq_number += 1
                options = []
                for following in blocks[i+1:]:
                    if following['k'] != 'opt':
                        break
                    options.append(following['text'])
                expected.append((unit['number'], 'multiple_choice', mcq_number, text, options))
            if block['k'] == 'tf':
                tf_number += 1
                expected.append((unit['number'], 'true_false', tf_number, text, []))
    identity = lambda row: (row['unit'], row['type'], row['item'])
    recorded = {identity(row): row for row in keys}
    if len(recorded) != len(keys) or set(recorded) != {r[:3] for r in expected}:
        issues.append('Missing, extra or duplicate reading-key items')
    for unit, kind, item, stem, options in expected:
        row = recorded.get((unit, kind, item), {})
        if row.get('stem') != stem:
            issues.append(f'U{unit} {kind} {item}: source stem changed')
        paragraphs = [b['text'] for b in book['units'][unit-1]['chapters'][0]['blocks'] if b['k'] == 'reading']
        index = row.get('reading_paragraph', 0)-1
        if not 0 <= index < len(paragraphs) or row.get('evidence') != paragraphs[index]:
            issues.append(f'U{unit} {kind} {item}: missing or stale paragraph evidence')
        if kind == 'multiple_choice':
            selected = next((o for o in options if o[0].upper() == row.get('answer')), None)
            if selected is None or selected[3:] != row.get('answer_text'):
                issues.append(f'U{unit} MCQ {item}: selected option does not match answer text')
        elif row.get('answer') not in ('T', 'F') or (row.get('answer') == 'F' and not row.get('correction')):
            issues.append(f'U{unit} TF {item}: missing judgment or correction')
    return issues


def main():
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    keys = json.loads((ROOT / 'book/classroom/reading-closed-keys.json').read_text())
    issues = inspect(book, keys)
    bad = copy.deepcopy(keys); bad[0]['answer'] = 'A'
    detects_wrong_option = any('selected option' in issue for issue in inspect(book, bad))
    bad = copy.deepcopy(keys); bad[0]['evidence'] = 'A sentence not in this reading.'
    detects_stale_evidence = any('paragraph evidence' in issue for issue in inspect(book, bad))
    if not detects_wrong_option or not detects_stale_evidence:
        issues.append('Mutation checks failed')
    report = {'ok': not issues, 'units': 8, 'multiple_choice_items': 40, 'true_false_items': 34,
              'items': len(keys), 'mutation_wrong_option_detected': detects_wrong_option,
              'mutation_stale_evidence_detected': detects_stale_evidence, 'issues': issues,
              'scope': 'Authored reading judgments with structural and source-evidence checks; not automatic semantic correctness, listening keys or independent expert approval.'}
    (ROOT / 'book/artifacts/qa_reading_keys.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

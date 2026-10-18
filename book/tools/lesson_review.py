"""Guarded lesson-structure repairs and explicitly authored learner practice.

Called on freshly reconstructed source only. All changes are logged outside
reader-facing exports. Exact source titles remain the responsibility of parse.py.
"""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def select(blocks, text):
    matches = [i for i, block in enumerate(blocks) if block.get('text') == text]
    if len(matches) != 1:
        raise ValueError(f'Lesson repair must match exactly once: {text!r} ({len(matches)} matches)')
    return matches[0]


def apply_repairs(book, log):
    repairs = json.loads((ROOT / 'book/master/structural-repairs.json').read_text())
    for repair in repairs:
        blocks = book['units'][repair['unit']-1]['chapters'][repair['chapter']-1]['blocks']
        operation = repair['operation']
        original = repair.get('text', repair.get('anchor', repair.get('expected_tail')))
        if operation == 'set_kind':
            target = blocks[select(blocks, repair['text'])]
            if target['k'] != repair['old_kind']:
                raise ValueError(f'Lesson repair kind drift: {repair}')
            target['k'] = repair['new_kind']
            correction = f"{target['text']} ({repair['new_kind']})"
        elif operation == 'move_before':
            target = blocks.pop(select(blocks, repair['text']))
            blocks.insert(select(blocks, repair['anchor']), target)
            correction = f"{target['text']} (before {repair['anchor']})"
        elif operation in ('insert_before', 'insert_after'):
            at = select(blocks, repair['anchor']) + (operation == 'insert_after')
            blocks[at:at] = deepcopy(repair['blocks'])
            correction = ' / '.join(x['text'] for x in repair['blocks'])
        elif operation == 'split':
            at = select(blocks, repair['text'])
            blocks[at:at+1] = deepcopy(repair['blocks'])
            correction = ' / '.join(x['text'] for x in repair['blocks'])
        elif operation == 'append':
            if blocks[-1].get('text') != repair['expected_tail']:
                raise ValueError(f'Lesson repair tail drift: {repair}')
            if any(b.get('text') == 'Conclusion' for b in blocks):
                raise ValueError('Refusing to add an already-present conclusion')
            blocks.extend(deepcopy(repair['blocks']))
            correction = ' / '.join(x['text'] for x in repair['blocks'])
        else:
            raise ValueError(f'Unknown lesson repair operation: {operation}')
        log(f"U{repair['unit']} Ch{repair['chapter']} · lesson-structure review",
            original, correction, repair['reason'], 'guarded structural repair')

    reviews = json.loads((ROOT / 'book/master/unit-review.json').read_text())
    if [review['unit'] for review in reviews] != list(range(1, 9)):
        raise ValueError('Unit review must cover all eight units in order')
    for unit, review in zip(book['units'], reviews):
        blocks = unit['chapters'][3]['blocks']
        additions = [
            {'k': 'sub', 'text': 'Sources Used'},
            {'k': 'instr', 'text': 'List the author or organization, title, and date for each source. Add a page number or link when available.'},
            {'k': 'sec', 'text': 'Reflect and Try Again'},
            {'k': 'instr', 'text': 'Ask a partner: Was my main point clear? Did my evidence support it? Where did you need clarification? Revise one passage and say it again.'},
            {'k': 'p', 'text': 'Check your progress: ' + review['check']},
            {'k': 'p', 'text': 'Put it to use: ' + review['transfer']},
        ]
        blocks.extend(additions)
        for block in additions:
            log(f"U{unit['number']} Ch4 · learner review and transfer", '(new learner practice)',
                block['text'], 'Connect the presentation to source attribution, feedback, revision, and a unit-specific real-life task.',
                'new learner-facing practice')


def apply_opener_rewrites(book, log):
    """Make each opener an explicit, low-disclosure preparation task."""
    plan = json.loads((ROOT / 'book/master/unit-opener-rewrites.json').read_text())
    if [row['unit'] for row in plan] != list(range(1, 9)):
        raise ValueError('Opener plan must cover all eight units')
    for row in plan:
        warmup = book['units'][row['unit']-1]['warmup']
        if warmup['paras'] != row['original_paras']:
            raise ValueError('Unit opener paragraph drift')
        warmup['paras'] = row['new_paras']
        log(f"U{row['unit']} opener", ' / '.join(row['original_paras']),
            ' / '.join(row['new_paras']), 'Give preparation, interaction and privacy choices without altering the unit title.')
        for edit in row['question_edits']:
            matches = [r for r in warmup['table']['rows'] if r[0] == edit['original']]
            if len(matches) != 1:
                raise ValueError('Opener question drift')
            matches[0][0] = edit['correction']
            log(f"U{row['unit']} opener question", edit['original'], edit['correction'],
                'Remove the false choice between cognitive and emotional skills.')

#!/usr/bin/env python3
"""Render book.json as a reviewable outline."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
book = json.load(open(os.path.join(ROOT, 'book/artifacts/book.json'), encoding='-8'.replace('-8','utf-8')))

KSYM = {'sec':'##', 'sub':'###', 'subsub':'####', 'sec?':'##?',
        'instr':'i:', 'p':'p ', 'reading':'R ', 'q':'q ', 'opt':'o ', 'tf':'t ',
        'fill':'f ', 'pair':'pr', 'note':'n ', 'readingtitle':'RT', 'mediatitle':'MT',
        'table':'TB', 'warmup':'WU'}

def block_line(b):
    k = b.get('k')
    if k == 'table':
        role = b['role']
        r0 = b['rows'][0] if b['rows'] else []
        return f"TB[{role}] {len(b['rows'])}x{len(r0)} {(' | '.join(c[:18] for c in r0[:3]))!r}"
    s = KSYM.get(k, k)
    txt = b.get('text', '')[:95]
    img = f" <img:{b['img']}>" if b.get('img') else ''
    return f"{s} {txt}{img}"

def emit(f, s):
    f.write(s + '\n')

out = open(os.path.join(ROOT, 'book/artifacts/review.txt'), 'w', encoding='utf-8')
u_from, u_to = 1, 8
if len(sys.argv) > 1:
    u_from = u_to = int(sys.argv[1])
for u in book['units']:
    if not (u_from <= u['number'] <= u_to):
        continue
    emit(out, f"===== UNIT {u['number']}: {u['title']}  [img {u.get('image')}]")
    w = u.get('warmup', {})
    for p in w.get('paras', []):
        emit(out, f"  WU p {p[:90]}")
    if w.get('table'):
        emit(out, f"  WU {block_line(w['table'])}")
    for c in u['chapters']:
        emit(out, f"  --- Chapter {c['number']}: {c['title']}")
        for b in c['blocks']:
            emit(out, f"    {block_line(b)}")
out.close()
print('written review.txt')

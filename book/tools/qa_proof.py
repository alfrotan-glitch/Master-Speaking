#!/usr/bin/env python3
"""qa_proof.py — page-by-page proof pass over the final print PDF.

For every page: folio presence/zone (main matter), text-bounds inside the
type area, no clipping at page edges, image bboxes inside type area,
per-page census (words, images, headings). Emits a compact per-page table
and flags anomalies. Writes book/artifacts/qa_proof.json.
"""
import json, os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')

PAGE_W, PAGE_H = 504.0, 720.0
# asymmetric gutter: recto frame 59.04-452.16, verso frame 51.84-444.96
RECTO = (59.04, 452.16)
VERSO = (51.84, 444.96)
Y0, Y1 = 57.6, 662.4          # type area vertical bounds
HEAD_ZONE = 45.0              # running heads live above this
TOL = 2.5                     # pt tolerance

d = pymupdf.open(PDF)
issues = []
rows = []

_qp = json.load(open(os.path.join(ROOT, 'book/artifacts/qa_print.json')))
_raw_units = (_qp.get('units') or _qp.get('unit_pages') or {}) if _qp else {}
_unit_pages = {}
for k, v in _raw_units.items():
    try:
        _unit_pages[v] = int(str(k).split('-')[-1])
    except ValueError:
        pass
main_start = (_qp or {}).get('main_start', 11)

for pno in range(len(d)):
    pg = d[pno]
    page = pno + 1
    ptype = 'front' if page < main_start else (
        'unit-opener' if page in _unit_pages else 'body')
    words = pg.get_text('words')
    nwords = len(words)
    nimg = len(pg.get_image_info())        # actually drawn, not inherited res
    rect = pg.rect
    if abs(rect.width - PAGE_W) > .5 or abs(rect.height - PAGE_H) > .5:
        issues.append(f'p{page}: page size {rect.width}x{rect.height}')

    # parity-dependent type area; running heads (y1 < HEAD_ZONE) exempt
    X0, X1 = RECTO if page % 2 == 1 else VERSO
    body_words = [w for w in words if w[3] > HEAD_ZONE and w[1] < 655]
    head_words = [w for w in words if w[3] <= HEAD_ZONE]
    xs0 = [w[0] for w in body_words]
    xs1 = [w[2] for w in body_words]
    ys0 = [w[1] for w in body_words]
    ys1 = [w[3] for w in body_words]
    bx0 = min(xs0) if xs0 else None
    bx1 = max(xs1) if xs1 else None
    by0 = min(ys0) if ys0 else None
    by1 = max(ys1) if ys1 else None

    # running heads must not cross side margins either
    for w in head_words:
        if w[0] < X0 - TOL or w[2] > X1 + TOL:
            issues.append(f'p{page}: running head outside margins: {w[4]!r}')

    if bx0 is not None and bx0 < X0 - TOL:
        issues.append(f'p{page}: text starts x={bx0:.1f} < left margin {X0}')
    if bx1 is not None and bx1 > X1 + TOL:
        issues.append(f'p{page}: text ends x={bx1:.1f} > right margin {X1}')
    if by0 is not None and by0 < Y0 - TOL:
        issues.append(f'p{page}: text top y={by0:.1f} above top margin {Y0}')
    if by1 is not None and by1 > Y1 + TOL:
        issues.append(f'p{page}: text bottom y={by1:.1f} below text area {Y1}')

    # images inside type area
    for img in pg.get_image_info():
        b = img['bbox']
        if b[0] < X0 - 3 or b[2] > X1 + 3 or b[3] > Y1 + 8:
            issues.append(f'p{page}: image bbox {tuple(round(v,1) for v in b)} outside type area')

    # folio check for main matter
    folio = None
    for w in words:
        if w[1] > 665:
            try:
                folio = int(w[4])
            except ValueError:
                pass
    if ptype in ('body', 'unit-opener'):
        expect = page - (main_start - 1)
        if folio != expect:
            issues.append(f'p{page}: folio {folio} != expected {expect}')
    else:
        if folio is not None and ptype == 'front' and page not in (9, 10):
            issues.append(f'p{page}: unexpected folio {folio} in front matter')

    # blank page? (a completely empty verso directly before a recto unit
    # opener is the standard print convention and is intentional)
    if nwords == 0 and nimg == 0:
        next_is_opener = (page + 1) in _unit_pages
        if not next_is_opener:
            issues.append(f'p{page}: BLANK page (not an intentional verso '
                          f'before a recto unit opener)')

    # text-line overlap detection (visual defect proxy): lines that overlap
    # vertically >40% AND horizontally >2pt while not sharing a baseline
    lines = []
    for b in pg.get_text('dict')['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            x0l, y0l, x1l, y1l = l['bbox']
            if y0l < HEAD_ZONE or y0l > 655:      # skip heads & folios
                continue
            lines.append(l['bbox'])
    for a in range(len(lines)):
        for b2 in range(a + 1, len(lines)):
            A, B = lines[a], lines[b2]
            ix = min(A[2], B[2]) - max(A[0], B[0])
            iy = min(A[3], B[3]) - max(A[1], B[1])
            if ix > 2 and iy > 0.45 * min(A[3] - A[1], B[3] - B[1]):
                # same-line different columns can legitimately overlap x;
                # only flag when y-centers differ (stacked collision)
                ca, cb = (A[1] + A[3]) / 2, (B[1] + B[3]) / 2
                if abs(ca - cb) > 2.5:
                    issues.append(
                        f'p{page}: overlapping text lines '
                        f'{tuple(round(v,1) for v in A)} / {tuple(round(v,1) for v in B)}')

    # opener pages must carry the right unit title
    if ptype == 'unit-opener':
        expect_unit = _unit_pages[page]
        TITLES = {1: 'The Power of Communication', 2: 'The Art of Goal Setting',
                  3: 'Emotional Intelligence', 4: 'Money and Happiness',
                  5: 'Living with AI', 6: 'Marriage', 7: 'Globalization',
                  8: 'Lingua Franca'}
        t = ' '.join(pg.get_text().split()).lower()
        if TITLES[expect_unit].lower() not in t or f'unit {expect_unit}' not in t:
            issues.append(f'p{page}: unit opener missing expected title')

    rows.append({'page': page, 'type': ptype, 'words': nwords, 'images': nimg,
                 'folio': folio,
                 'bounds': [round(v, 1) if v is not None else None
                            for v in (bx0, bx1, by0, by1)]})

report = {'pages': len(d), 'rows': rows, 'issues': issues, 'ok': not issues}
open(os.path.join(ROOT, 'book/artifacts/qa_proof.json'), 'w').write(
    json.dumps(report, indent=1))
print(f'{len(d)} pages proofed, {len(issues)} issues')
for i in issues[:80]:
    print(' ', i)
print('OK' if not issues else 'ISSUES PRESENT')
sys.exit(1 if issues else 0)

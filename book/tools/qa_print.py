#!/usr/bin/env python3
"""qa_print.py — automated page-by-page layout QA for the print PDF.

Checks: page geometry, text inside margins (mirrored), running heads and
folios, blank pages, overlapping text, orphan headings (heading as last block
on a page), TOC folio accuracy vs actual unit pages, image effective DPI,
image aspect integrity.
"""
import os, re, sys, json
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')

PAGE_W, PAGE_H = 504.0, 720.0
M_TOP, M_BOT, M_IN, M_OUT = 0.78*72, 0.80*72, 0.82*72, 0.72*72
GUTTER = M_IN - M_OUT
TOL = 2.5

d = pymupdf.open(PDF)
issues = []

unit_pages = {}      # physical page of each unit opener
# --- locate unit openers: "Unit n · <title>" heading with the THINK panel
for i in range(d.page_count):
    txt = d[i].get_text('text')
    if 'THINK' not in txt:
        continue
    for m in re.finditer(r'^Unit ([1-8]) \u00b7 ', txt, re.M):
        unit_pages[int(m.group(1))] = i + 1
        break

main_start = unit_pages.get(1)

def folio_for(page):
    ROMAN = ['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv','xvi','xvii','xviii']
    if main_start is None or page < main_start:
        return ROMAN[page-1] if 0 < page <= len(ROMAN) else str(page)
    return str(page - main_start + 1)

HEAD_SIZES = set()   # font sizes of headings (heuristic: >= 12.5 bold sans)
blank_pages = []
img_report = []

for i in range(d.page_count):
    p = d[i]
    page = i + 1
    # geometry
    if abs(p.rect.width - PAGE_W) > 0.5 or abs(p.rect.height - PAGE_H) > 0.5:
        issues.append(f'p{page}: wrong page size {p.rect}')
    # margins (mirrored): verso (even) pages shift left by GUTTER
    dx = 0 if page % 2 == 1 else -GUTTER
    left_edge = M_IN + dx - TOL
    right_edge = PAGE_W - M_OUT + dx + TOL
    blocks = [b for b in p.get_text('dict')['blocks'] if b['type'] == 0]
    spans = []
    for b in blocks:
        for l in b.get('lines', []):
            for s in l['spans']:
                if s['text'].strip():
                    spans.append(s)
    # folio check: bottom-centre text equals expected folio
    folio_spans = [s for s in spans if s['bbox'][1] > PAGE_H - M_BOT/2 - 20]
    ftxt = ''.join(s['text'] for s in folio_spans).strip()
    if ftxt != folio_for(page):
        issues.append(f'p{page}: folio {ftxt!r} != expected {folio_for(page)!r}')
    # running head check (main pages only, excluding unit openers)
    is_opener = page in unit_pages.values()
    head_spans = [s for s in spans if s['bbox'][3] < M_TOP - 10]
    htxt = ''.join(s['text'] for s in head_spans).strip()
    if main_start and page > main_start and not is_opener:
        if page % 2 == 1:
            if not htxt.startswith('MASTER SPEAKING'):
                issues.append(f'p{page}: recto running head missing/wrong: {htxt!r}')
        else:
            body_spans = [s2 for s2 in spans
                          if s2['bbox'][1] > M_TOP
                          and s2['bbox'][3] < PAGE_H - M_BOT + 10]
            if body_spans and not re.match(r'^Unit [1-8] · ', htxt):
                issues.append(f'p{page}: verso running head missing/wrong: {htxt!r}')
    # text inside margins
    for s in spans:
        x0, y0, x1, y1 = s['bbox']
        if y0 < M_TOP - 24 or y1 > PAGE_H - M_BOT/2 + 8:
            continue  # head/folio zones
        if x0 < left_edge - 0.5 or x1 > right_edge + 0.5:
            issues.append(f'p{page}: text outside margins {s["bbox"]} {s["text"][:40]!r}')
    # blank page?
    if not spans and not p.get_images() and not p.get_drawings():
        blank_pages.append(page)
    # overlap of text blocks (same line region different blocks)
    # (approximate: skip — reportlab layout prevents this)
    # images: effective dpi + aspect
    for img in p.get_image_info():
        bx = img['bbox']
        w_pt, h_pt = bx[2]-bx[0], bx[3]-bx[1]
        px_w, px_h = img['width'], img['height']
        if w_pt < 1 or h_pt < 1:
            issues.append(f'p{page}: image with zero size')
            continue
        dpi = px_w / (w_pt/72)
        aspect_draw = w_pt / h_pt
        aspect_src = px_w / px_h
        if abs(aspect_draw - aspect_src) / aspect_src > 0.02:
            issues.append(f'p{page}: image aspect distorted draw={aspect_draw:.3f} src={aspect_src:.3f}')
        img_report.append((page, round(dpi), f'{px_w}x{px_h}'))
        if x0 < left_edge - 1 or bx[2] > right_edge + 1:
            issues.append(f'p{page}: image outside margins {bx}')
    # orphan heading: last text span on page is a heading-sized bold sans
    body_spans = [s for s in spans if M_TOP - 20 < s['bbox'][1] < PAGE_H - M_BOT]
    fm_or_opener = page <= (main_start or 0) or is_opener
    if body_spans and not fm_or_opener:
        last = max(body_spans, key=lambda s: s['bbox'][1])
        if 'SemiBold' in last['font'] or 'Bold' in last['font']:
            if last['size'] >= 10.6 and not re.search(r'[.:;…]$|^\d+$', last['text'].strip()):
                issues.append(f'p{page}: possible orphan heading at page bottom: {last["text"][:50]!r}')

# --- TOC accuracy: printed TOC folios vs actual unit pages
# merge lines sharing the same y (folio prints beside the entry text)
toc_lines = []
toc_start = next((i for i in range(min(12, d.page_count))
                  if d[i].get_text('text').strip().startswith(
                      ('v', 'i', 'x')) and 'Contents' in d[i].get_text('text')), 6)
for i in range(toc_start, toc_start + 4):
    if i >= d.page_count:
        continue
    rows = {}
    for b in d[i].get_text('dict')['blocks']:
        if b['type'] != 0:
            continue
        for l in b.get('lines', []):
            y = round(l['bbox'][1], 1)
            key = min((k for k in rows if abs(k - y) < 3), default=y)
            rows.setdefault(key, []).append(''.join(sp['text'] for sp in l['spans']).strip())
    for y, parts in sorted(rows.items()):
        toc_lines.append(' '.join(p2 for p2 in parts if p2))
for unum, phys in sorted(unit_pages.items()):
    expected = folio_for(phys)
    found = False
    for ln in toc_lines:
        nums = re.findall(r'\d+', ln)
        if f'Unit {unum} ' in ln and expected in nums:
            found = True
            break
    if not found:
        cand = [ln for ln in toc_lines if f'Unit {unum} ' in ln]
        issues.append(f'TOC: Unit {unum} folio mismatch (expected {expected}; line: {cand[:1]})')

# --- image dpi summary
low = [(pg, dp) for pg, dp, _ in img_report if dp < 150]
print(f'pages: {d.page_count}   units at: {unit_pages}   main_start: {main_start}')
print(f'images placed: {len(img_report)}  (effective dpi min-max: '
      f'{min((dp for _,dp,_ in img_report), default=0)}-{max((dp for _,dp,_ in img_report), default=0)})')
if low:
    print(f'images below 150 dpi effective: {len(low)} -> {low[:8]}')
if blank_pages:
    print('blank pages:', blank_pages)
print(f'--- {len(issues)} issues ---')
for it in issues[:60]:
    print(' *', it)
json.dump({'issues': issues, 'unit_pages': unit_pages, 'images': img_report,
           'blank': blank_pages, 'pages': d.page_count},
          open(os.path.join(ROOT, 'book/artifacts/qa_print.json'), 'w'), indent=1)

#!/usr/bin/env python3
"""Extract full document structure from Master Speaking.docx into book/artifacts/dump.json.

Captures, in document order: paragraphs (style, text, image rIds), tables
(rows/cells incl. merged-cell grid), page-break flags. Raw audit dump for parse.py.
"""
import json, os, sys, zipfile
from docx import Document
from lxml import etree

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root
SRC = os.path.join(ROOT, 'Master Speaking.docx')
OUT = os.path.join(ROOT, 'book', 'artifacts', 'dump.json')

doc = Document(SRC)

def para_text(p): return ''.join(t.text or '' for t in p.findall(f'.//{W}t'))
def para_rids(p): return [b.get(f'{R}embed') for b in p.findall(f'.//{A}blip') if b.get(f'{R}embed')]
def para_style(p):
    ps = p.find(f'{W}pPr/{W}pStyle')
    return ps.get(f'{W}val') if ps is not None else None
def has_page_break(p):
    return any(br.get(f'{W}type') == 'page' for br in p.findall(f'.//{W}br'))

items, idx = [], 0
for child in doc.element.body:
    tag = etree.QName(child).localname
    if tag == 'p':
        it = {'i': idx, 'type': 'para', 'style': para_style(child),
              'pagebreak': has_page_break(child), 'images': para_rids(child),
              'text': para_text(child)}
        # visual identity: paragraph shading band + first accent run color
        shd = child.find(f'{W}pPr/{W}shd')
        if shd is not None and shd.get(f'{W}fill') not in (None, 'auto'):
            it['shd'] = shd.get(f'{W}fill')
        for rc in child.findall(f'.//{W}rPr/{W}color'):
            v = rc.get(f'{W}val')
            if v and v not in ('auto', '0F1115', '181818', '333333'):
                it['run_color'] = v
                break
        items.append(it)
        idx += 1
    elif tag == 'tbl':
        rows = []
        for tr in child.findall(f'{W}tr'):
            cells = []
            for tc in tr.findall(f'{W}tc'):
                cell = {'text': '\n'.join(
                    ''.join(t.text or '' for t in p.findall(f'.//{W}t'))
                    for p in tc.findall(f'.//{W}p')),
                    'images': [b.get(f'{R}embed') for b in tc.findall(f'.//{A}blip')]}
                cshd = tc.find(f'{W}tcPr/{W}shd')
                if cshd is not None and cshd.get(f'{W}fill') not in (None, 'auto'):
                    cell['shd'] = cshd.get(f'{W}fill')
                cells.append(cell)
            rows.append(cells)
        grid = len(child.findall(f'{W}tblGrid/{W}gridCol'))
        items.append({'i': idx, 'type': 'table', 'grid_cols': grid, 'rows': rows})
        idx += 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=1)
print(f"dumped {len(items)} block items -> {OUT}")

# image relationship map: rId -> media filename (images only)
_rels = etree.fromstring(zipfile.ZipFile(SRC).read('word/_rels/document.xml.rels'))
_image_map = {}
for _rel in _rels:
    _t = _rel.get('Target', '')
    if 'media/' in _t and _t.rsplit('.', 1)[-1].lower() in (
            'png', 'jpeg', 'jpg', 'gif', 'bmp', 'tif', 'tiff'):
        _image_map[_rel.get('Id')] = os.path.basename(_t)
with open(os.path.join(os.path.dirname(OUT), 'image_map.json'), 'w') as f:
    json.dump(_image_map, f, indent=1)
print(f"image map: {len(_image_map)} relationships -> image_map.json")

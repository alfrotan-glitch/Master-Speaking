#!/usr/bin/env python3
"""Regression checks for the October editorial/design fixes."""
import json
from pathlib import Path
import zipfile
from lxml import etree
from docx import Document
from docx.oxml.ns import qn
from design import contrast, BAND, BANNER, ACCENT, INK

ROOT = Path(__file__).resolve().parents[2]
book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
edits = json.loads((ROOT / 'book/master/reviewed-edits.json').read_text())
for edit in edits:
    blocks = book['units'][edit['unit'] - 1]['chapters'][edit['chapter'] - 1]['blocks']
    if 'table_column' in edit:
        column = edit['table_column']
        values = [row[column] for block in blocks if block.get('k') == 'table'
                  for row in block['rows'][1:] if len(row) > column]
        assert values.count(edit['correction']) == 1 and edit['original'] not in values, edit
    else:
        if edit.get('action') != 'remove':
            assert sum(b.get('text') == edit['correction'] for b in blocks) == 1, edit
        assert sum(b.get('text') == edit['original'] for b in blocks) == edit.get('expected_matches', 1) - 1, edit
front_edits = json.loads((ROOT / 'book/master/reviewed-front-edits.json').read_text())
for edit in front_edits:
    parent = book['front']
    for key in edit['path'][:-1]:
        parent = parent[key]
    key = edit['path'][-1]
    if edit.get('action') == 'remove':
        assert isinstance(parent, list) and len(parent) == key
    else:
        assert parent[key] == edit['correction']
question = next(b['text'] for b in book['units'][4]['chapters'][1]['blocks']
                if b.get('text', '').startswith('Imagine that scientists'))
raw = json.loads((ROOT / 'book/artifacts/dump.json').read_text())
original = next(b['text'] for b in raw if b['i'] == 1582)
assert question == 'I' + original.strip(), 'AI question must preserve all source words except its missing initial I'
assert question.endswith('Should we give it significant decision-making power?')
for paragraph in json.loads((ROOT / 'book/master/classroom-guide.json').read_text()):
    assert paragraph in book['front']['howto']['paras']
assert min(contrast(ACCENT, 'FFFFFF'), contrast('FFFFFF', BANNER), contrast(INK, BAND)) >= 4.5
word = Document(ROOT / 'Master-Speaking-7x10.docx')
assert sum(p.style.name == 'MS Chapter Title' for p in word.paragraphs) == 32
assert not any(p.style.name == 'MS FM Sub' and p.text.startswith('Chapter') for p in word.paragraphs)
assert word.styles['MS Instruction'].paragraph_format.keep_with_next
assert word.styles['MS Body'].font.size.pt == 11
chapter_color = str(word.styles['MS Chapter Title'].font.color.rgb)
assert contrast(chapter_color, 'FFFFFF') >= 4.5
# Official static typefaces: verify provenance, weight, family, and licenses.
import hashlib
from fontTools.ttLib import TTFont
for font in json.loads((ROOT / 'book/assets/fonts/provenance.json').read_text()):
    path = ROOT / 'book/assets/fonts' / font['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == font['sha256']
    assert (path.parent / font['license']).is_file()
    face = TTFont(path)
    assert 'ExtraLight' not in face['name'].getDebugName(1)
    assert face['OS/2'].usWeightClass in (400, 600, 700)
for table in word.tables:
    grid = [int(c.get(qn('w:w'))) for c in table._tbl.find(qn('w:tblGrid'))]
    for row in table.rows:
        for col, cell in enumerate(row.cells):
            assert abs(cell.width.twips - grid[col]) <= 2, 'Grid and cell widths disagree'
with zipfile.ZipFile(ROOT / 'Master-Speaking.epub') as epub:
    opf = etree.fromstring(epub.read('content.opf'))
    ns = {'o': 'http://www.idpf.org/2007/opf'}
    covers = opf.xpath('//o:item[@properties="cover-image"]', namespaces=ns)
    assert len(covers) == 1
    assert covers[0].get('href') in epub.namelist()
    cover = etree.fromstring(epub.read('cover.xhtml'))
    assert cover.xpath('//*[local-name()="img"]')[0].get('alt')
# Instructional regression: stress must remain distinguishable in all exports.
import re
import pymupdf
flat = 'Emotional intelligence is important for everyone.'
stressed = 'Emotional intelligence is IMPORTANT for EVERYONE.'
blocks = book['units'][2]['chapters'][3]['blocks']
assert sum(b.get('text') == flat for b in blocks) == 1
assert sum(b.get('text') == stressed for b in blocks) == 1
for number, sentence in enumerate([
        'Why is emotional intelligence important in leadership?',
        'Emotional intelligence helps people build stronger relationships.',
        'What would happen if people never controlled their emotions?',
        'We can improve emotional intelligence through daily practice.'], 1):
    assert any(p.text == f'{number}. {sentence}' for p in word.paragraphs), 'Pronunciation practice numbering'
assert any('Wh-questions often end with a falling tone.' in b.get('text', '') for b in blocks)
normalize_space = lambda text: re.sub(r'\s+', ' ', text)
with pymupdf.open(ROOT / 'Master-Speaking-print-7x10.pdf') as pdf:
    pdf_text = normalize_space(' '.join(p.get_text() for p in pdf))
    comparison_pages = [p for p in pdf if 'Flat delivery' in p.get_text()]
    assert len(comparison_pages) == 1
    comparison = normalize_space(comparison_pages[0].get_text())
    assert flat in comparison and stressed in comparison and 'Emphasize Key Words' in comparison, \
        'Teaching comparison split across PDF pages'
with zipfile.ZipFile(ROOT / 'Master-Speaking.epub') as epub:
    epub_text = normalize_space(' '.join(etree.fromstring(epub.read(n)).xpath('string()')
                                         for n in epub.namelist() if n.endswith('.xhtml')))
word_text = normalize_space(' '.join(p.text for p in word.paragraphs))
master_text = normalize_space(etree.parse(str(ROOT / 'book/master/master.xhtml')).xpath('string()'))
groups = etree.parse(str(ROOT / 'book/master/master.xhtml')).xpath(
    '//*[local-name()="div" and @class="stress-contrast"]')
assert len(groups) == 1 and len(groups[0]) == 6
start = next(i for i, p in enumerate(word.paragraphs) if p.text == 'Emphasize Key Words')
assert all(p.paragraph_format.keep_with_next is True for p in word.paragraphs[start:start+5])
for text in [pdf_text, epub_text, word_text, master_text]:
    assert flat in text and stressed in text, 'Stress contrast lost in an export'
    assert 'Flat delivery' in text and 'With key-word stress' in text
print(f'PASS: {len(edits) + len(front_edits)} reviewed edits, complete AI question, classroom guidance, contrast, '
      '32 Word chapter headings, instruction keeps, table grids, EPUB cover/alt text.')

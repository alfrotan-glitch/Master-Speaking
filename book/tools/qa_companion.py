#!/usr/bin/env python3
"""Check companion exports, content coverage, and PDF text boundaries."""
from pathlib import Path
import re
import pymupdf
from docx import Document
from companion import blocks, ROOT


def normalize(text):
    return re.sub(r'\s+', '', text).replace('•', '')


def check():
    source = ROOT / 'book/companion/speaking-class.md'
    expected = list(blocks(source.read_text(encoding='utf-8')))
    doc = Document(ROOT / 'Master-Speaking-Class-Companion.docx')
    word = normalize('\n'.join(p.text for p in doc.paragraphs))
    pdf = pymupdf.open(ROOT / 'Master-Speaking-Class-Companion.pdf')
    pages = []
    for page in pdf:
        lines = page.get_text().splitlines()
        pages.append('\n'.join(line for line in lines
                               if 'Master Speaking | Class Companion | Supplementary material' not in line
                               and line.strip() != str(page.number + 1)))
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    x0, y0, x1, y1 = span['bbox']
                    assert x0 >= 35 and x1 <= page.rect.width - 35, (page.number, span)
                    assert y0 >= 15 and y1 <= page.rect.height - 15, (page.number, span)
    exported = normalize('\n'.join(pages))
    for kind, text in expected:
        assert normalize(text) in word, f'Word missing: {text[:70]}'
        assert normalize(text) in exported, f'PDF missing: {text[:70]}'
    headings = [t for k, t in expected if k == 'heading' and re.match(r'^\d+\.', t)]
    assert len(headings) == 15
    for heading in headings:
        assert any(normalize(page).startswith(normalize(heading)) for page in pages), heading
    assert sum('Outcome:' in text for _, text in expected) == 8
    print(f'PASS: {len(expected)} source blocks present in both exports; 8 unit outcomes; '
          f'15 section starts verified; {len(pdf)} PDF pages within text boundaries.')


if __name__ == '__main__':
    check()

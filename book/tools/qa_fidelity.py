#!/usr/bin/env python3
"""qa_fidelity.py — rendering fidelity: every master text block must be
traceable in ALL THREE final outputs (print PDF text layer, EPUB XHTML,
and the editable Word master).

Closes the last link of the chain:
  docx -> dump -> book.json -> master -> {PDF, EPUB, DOCX}
Pass 1 (qa_content) proved docx->master; this proves master->outputs,
catching dropped flowables, missing EPUB sections or copy bugs (it caught
the missing unit-opener warmup blocks).

Method:
  * master texts collected block-aware; h1/h2 containers are split into
    their kicker/name spans (the PDF renders them as separate lines)
  * PDF target text built from get_text('blocks') sorted by (y, x) with
    running-head/folio zones removed — keeps table cells contiguous
  * probe windows matched loosely; short texts (<5 loose chars) matched
    exactly against the target's leaf-text set; underscore runs matched
    against the normalized (not loose) target text
Writes book/artifacts/qa_fidelity.json.
"""
import json, os, re, sys, unicodedata, zipfile
from lxml import etree
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER = os.path.join(ROOT, 'book', 'master', 'master.xhtml')
PDF = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')
EPUB = os.path.join(ROOT, 'Master-Speaking.epub')

BLOCK = {'li', 'ol', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'h5',
         'table', 'tr', 'td', 'th', 'div', 'figure'}
XH = 'http://www.w3.org/1999/xhtml'


def btext(el):
    parts = []
    if el.text:
        parts.append(el.text)
    for c in el:
        if not isinstance(c.tag, str):
            if c.tail:
                parts.append(c.tail)
            continue
        if etree.QName(c).localname in BLOCK:
            parts.append(' ')
            parts.append(btext(c))
            parts.append(' ')
        else:
            parts.append(btext(c))
        if c.tail:
            parts.append(c.tail)
    return ''.join(parts)


tree = etree.parse(MASTER)
texts = []          # (text, kind) kind in {'body','heading-part'}
for el in tree.getroot().iter():
    if not isinstance(el.tag, str):
        continue
    ln = etree.QName(el).localname
    if ln in ('h1', 'h2'):
        # split into span parts (kicker / name) — rendered as separate lines
        spans = [c for c in el.iter(f'{{{XH}}}span')]
        if spans:
            for sp in spans:
                t = btext(sp).strip()
                if t:
                    texts.append((t, 'heading-part'))
            continue
        t = btext(el).strip()
        if t:
            texts.append((t, 'heading-part'))
    elif ln in ('p', 'li', 'th', 'td', 'h3', 'h4', 'h5'):
        t = btext(el).strip()
        if t:
            texts.append((t, 'body'))


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\xa0', ' ')
    s = re.sub(r'[“”]', '"', s)
    s = re.sub(r'[’‘]', "'", s)
    s = re.sub(r'[–—]', '-', s)
    s = re.sub(r'[✅✔❌✗]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


def loose(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', s)).strip()


# ---- PDF target: block-based, (y,x) ordered, head/folio stripped ---------
d = pymupdf.open(PDF)
page_texts = []
pdf_leaf_set = set()
for pg in d:
    blocks = [b for b in pg.get_text('blocks')
              if b[6] == 0 and 45 < b[1] < 655]
    blocks.sort(key=lambda b: (round(b[1], 1), b[0]))
    page_texts.append(' '.join(b[4].replace('\n', ' ') for b in blocks))
    for b in blocks:
        for line in b[4].split('\n'):
            pdf_leaf_set.add(loose(norm(line)))
pdf_text = norm(' '.join(page_texts))
pdf_loose = loose(pdf_text)
pdf_leaf_set.discard('')

# ---- DOCX target ----------------------------------------------------------
from docx import Document as _Docx
_w = _Docx(os.path.join(ROOT, 'Master-Speaking-7x10.docx'))
docx_texts = [p.text for p in _w.paragraphs if p.text.strip()]
for _t in _w.tables:
    for _r in _t.rows:
        for _c in _r.cells:
            if _c.text.strip():
                docx_texts.append(_c.text)
docx_text = norm(' '.join(docx_texts))
docx_loose = loose(docx_text)
docx_leaf = set()
for _t in docx_texts:
    docx_leaf.update(loose(norm(_l)) for _l in _t.split('\n') if _l.strip())
docx_leaf.discard('')

# ---- EPUB target ----------------------------------------------------------
z = zipfile.ZipFile(EPUB)
epub_parts = []
epub_leaf_set = set()
for n in z.namelist():
    if n.endswith('.xhtml') and 'nav.xhtml' not in n:
        doc = etree.fromstring(z.read(n))
        epub_parts.append(btext(doc))
        for el in doc.iter():
            if isinstance(el.tag, str) and etree.QName(el).localname in (
                    'p', 'li', 'th', 'td', 'h1', 'h2', 'h3', 'h4', 'h5', 'span'):
                if not any(isinstance(c.tag, str) and
                           etree.QName(c).localname in BLOCK for c in el):
                    epub_leaf_set.add(loose(norm(btext(el))))
epub_text = norm(' '.join(epub_parts))
epub_loose = loose(epub_text)
epub_leaf_set.discard('')


def windows(t):
    out = []
    if len(t) < 60:
        out.append(t)
    else:
        out.append(t[:60])
        out.append(t[20:80])
        out.append(t[len(t) // 2:len(t) // 2 + 60])
        out.append(t[-60:])
    return [p.strip() for p in out if p.strip()]


def hit(t, target_loose, target_leaf, target_norm_text):
    n = norm(t)
    l = loose(n)
    if not l:
        return '_' in n and n in target_norm_text      # underscore blanks
    if len(l) < 5:
        return l in target_leaf or l in target_loose
    for w in windows(l):
        if w in target_loose:
            return True
    return False


miss_pdf, miss_epub, miss_docx = [], [], []
n = 0
for t, kind in texts:
    if len(norm(t)) < 4:
        continue
    n += 1
    if not hit(t, pdf_loose, pdf_leaf_set, pdf_text):
        miss_pdf.append(t[:90])
    if not hit(t, epub_loose, epub_leaf_set, epub_text):
        miss_epub.append(t[:90])
    if not hit(t, docx_loose, docx_leaf, docx_text):
        miss_docx.append(t[:90])

report = {'master_blocks': n,
          'pdf': {'covered': n - len(miss_pdf), 'missing': miss_pdf},
          'epub': {'covered': n - len(miss_epub), 'missing': miss_epub},
          'docx': {'covered': n - len(miss_docx), 'missing': miss_docx},
          'ok': not miss_pdf and not miss_epub and not miss_docx}
open(os.path.join(ROOT, 'book/artifacts/qa_fidelity.json'), 'w').write(
    json.dumps(report, indent=1, ensure_ascii=False))
print(f'master blocks checked: {n}')
print(f'  PDF : covered {n - len(miss_pdf)}, missing {len(miss_pdf)}')
for t in miss_pdf[:30]:
    print('   MISS-PDF:', t)
print(f'  EPUB: covered {n - len(miss_epub)}, missing {len(miss_epub)}')
for t in miss_epub[:30]:
    print('   MISS-EPUB:', t)
print(f'  DOCX: covered {n - len(miss_docx)}, missing {len(miss_docx)}')
for t in miss_docx[:30]:
    print('   MISS-DOCX:', t)
print('OK' if report['ok'] else 'ISSUES PRESENT')
sys.exit(0 if report['ok'] else 1)

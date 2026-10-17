"""Cross-format chapter names, opening pages, contents and reading-order checks."""
import json
from pathlib import Path
from zipfile import ZipFile
import pymupdf
from docx import Document
from lxml import etree

ROOT = Path(__file__).resolve().parents[2]
book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
plan = json.loads((ROOT / 'book/master/chapter-titles.json').read_text())
chapters = [(u, c) for u in book['units'] for c in u['chapters']]
issues = []
def check(ok, message):
    if not ok:
        issues.append(message)
def norm(text):
    return ' '.join(text.split())
check(len(chapters) == 32, 'Expected 32 chapters')
# Repeated existing lesson titles are intentional, not grounds to invent names.
for u, c in chapters:
    check(c['title'] == plan[u['number']-1]['titles'][c['number']-1], 'Title plan mismatch')
    check(c.get('focus', '').startswith('Speaking through '), 'Original learning focus missing')
    source = plan[u['number']-1]['sources'][c['number']-1]
    check(c.get('title_source') == source, 'Title provenance mismatch')
    if source == 'original-chapter-heading':
        check(c['title'] == c['focus'], 'Original chapter heading was replaced')
    else:
        check(any(x.get('k') == source and x.get('text') == c['title'] for x in c['blocks']),
              f'Title does not exactly match chapter content: {c["title"]}')

word = Document(ROOT / 'Master-Speaking-7x10.docx')
paras = word.paragraphs
headings = [(i, p) for i, p in enumerate(paras) if p.style.name == 'MS Chapter Title']
check(len(headings) == 32, 'Word chapter count')
for (i, p), (u, c) in zip(headings, chapters):
    label = f"Chapter {c['number']} · {c['title']}"
    check(norm(p.text) == label, f'Word title mismatch: {label}')
    page_break = p.paragraph_format.page_break_before
    if page_break is None:
        page_break = p.style.paragraph_format.page_break_before
    check(page_break is True, f'Word new-page property missing: {label}')
    if c['title'] != c['focus']:
        check(i+1 < len(paras) and paras[i+1].style.name == 'MS Chapter Focus'
              and paras[i+1].text == c['focus'], f'Word focus subtitle missing: {label}')
    else:
        check(i+1 < len(paras) and paras[i+1].style.name != 'MS Chapter Focus',
              f'Redundant repeated subtitle: {label}')
    check(p.style.paragraph_format.keep_with_next is True, f'Word heading not kept with subtitle: {label}')
check(word.styles['MS Chapter Focus'].paragraph_format.keep_with_next is True, 'Word subtitle orphan protection')

with pymupdf.open(ROOT / 'Master-Speaking-print-7x10.pdf') as pdf:
    outline = pdf.get_toc()
    main_start = next(pg for depth, title, pg in outline if title.startswith('Unit 1 ·'))
    starts = [item for item in outline if item[0] == 2 and item[1].startswith('Chapter ')]
    check(len(starts) == 32, 'PDF chapter bookmark count')
    check(len({item[2] for item in starts}) == 32, 'Chapters share an opening page')
    toc_pages = [p for p in pdf if 'contents' in p.get_text().casefold() and p.number < main_start-1]
    for (_, label, pg), (u, c) in zip(starts, chapters):
        expected = f"Chapter {c['number']} · {c['title']}"
        check(norm(label) == expected, f'PDF bookmark mismatch: {expected}')
        page = pdf[pg-1]
        # The title and learning focus must occupy the first body block; no
        # preceding chapter text may appear above them on the opening page.
        blocks = sorted((b for b in page.get_text('blocks') if 35 < b[1] < 650), key=lambda b: b[1])
        opening = norm(' '.join(b[4] for b in blocks[:3]))
        check(expected in opening and c['focus'] in opening, f'PDF opening missing title/focus: {expected}')
        check(bool(blocks) and blocks[0][1] < 100, f'Chapter does not open near page top: {expected}')
        entries = []
        for contents in toc_pages:
            spans = [s for b in contents.get_text('dict')['blocks']
                     for line in b.get('lines', []) for s in line['spans']]
            for title_span in (s for s in spans if norm(s['text']) == expected):
                numbers = [s['text'].split()[-1] for s in spans
                           if abs(s['bbox'][1]-title_span['bbox'][1]) < 1
                           and s['bbox'][0] > title_span['bbox'][2]]
                # Equal source titles can legitimately recur in different units.
                # Select the entry by its printed folio before checking its link.
                if numbers != [str(pg-main_start+1)]:
                    continue
                entries.extend(numbers)
                check(any(link.get('page') == pg-1 and
                          link['from'].intersects(pymupdf.Rect(title_span['bbox']))
                          for link in contents.get_links()), f'Contents link mismatch: {expected}')
        check(entries == [str(pg-main_start+1)], f'Contents folio mismatch: {expected}')
    for i, page in enumerate(pdf):
        expected = str(i-main_start+2) if i >= main_start-1 else None
        if expected:
            check(page.get_label() == expected, f'PDF viewer label mismatch at physical page {i+1}')
    with pymupdf.open(ROOT / 'Master-Speaking.pdf') as reader:
        check(len(reader) == len(pdf)+1, 'Reader cover offset')
        check(reader[0].get_label() == 'Cover', 'Cover viewer label')
        for i, page in enumerate(pdf):
            check(reader[i+1].get_label() == page.get_label(), f'Reader page-label offset at {i+2}')
        check(reader.get_toc()[1:] == [[d,t,p+1] for d,t,p in outline], 'Reader bookmark offset')

ns = {'o':'http://www.idpf.org/2007/opf', 'x':'http://www.w3.org/1999/xhtml'}
with ZipFile(ROOT / 'Master-Speaking.epub') as z:
    opf = etree.fromstring(z.read('content.opf'))
    manifest = {item.get('id'):item.get('href') for item in opf.xpath('//o:manifest/o:item', namespaces=ns)}
    spine = [manifest[item.get('idref')] for item in opf.xpath('//o:spine/o:itemref', namespaces=ns)]
    unit_spine = [f for f in spine if f.startswith('unit')]
    expected_spine = []
    for u in book['units']:
        expected_spine.append(f"unit{u['number']}.xhtml")
        expected_spine.extend(f"unit{u['number']}-ch{c['number']}.xhtml" for c in u['chapters'])
    check(unit_spine == expected_spine, 'EPUB unit/chapter reading order')
    nav = etree.fromstring(z.read('nav.xhtml'))
    for u, c in chapters:
        href = f"unit{u['number']}-ch{c['number']}.xhtml"
        node = etree.fromstring(z.read(href))
        name = node.xpath('string(//x:span[@class="chapter-name"])', namespaces=ns)
        focus = node.xpath('string(//x:p[@class="chapter-focus"])', namespaces=ns)
        check(name == c['title'] and focus == (c['focus'] if c['title'] != c['focus'] else ''),
              f'EPUB heading/focus mismatch: {href}')
        links = nav.xpath('//x:a[@href=$href]', namespaces=ns, href=href)
        check(len(links) == 1 and c['title'] in ''.join(links[0].itertext()), f'EPUB navigation mismatch: {href}')

report = {'chapters':len(chapters), 'issues':issues, 'status':'PASS' if not issues else 'FAIL'}
(ROOT / 'book/artifacts/qa_chapters.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
raise SystemExit(bool(issues))

"""Master-Speaking production renderer: DOCX -> PDF.

Reads the production Word master (Master-Speaking-7x10.docx) and renders it
to print PDF.  The DOCX is the single source: text runs, fonts, colours,
paragraph shading (banners/bands), table cell fills, images, column widths
and page-break structure are all read FROM the .docx file -- never from the
semantic master.  Any PDF fix therefore starts life as a DOCX fix.

Reuses the font/style/page machinery of pdf.py (same metrics, folios,
running heads, recto-forcing convergence loop).
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pdf as P
from pdf import (S, register_fonts, build_styles, folio_for, fallback, esc,
                 BAND, BANNER, ACCENT, BOX_GREEN, BOX_OLIVE, RULE, ZEBRA,
                 INK, SOFT, PAGE_W, PAGE_H, M_IN, M_OUT, M_TOP, M_BOT,
                 GUTTER_SHIFT, TEXT_W, SERIF, SANS, BookDoc, State,
                 on_page_fm, on_page_opener)
from reportlab.lib.colors import HexColor

MS_FIXED = [None]        # pinned first decimal-folio page (fixpoint)


def on_page_main(canv, doc):
    """Mirrors the DOCX running heads: recto = book title (right),
    verso = current unit title (left); folio bottom-centre."""
    page = canv.getPageNumber()
    folio = folio_for(page, MS_FIXED[0] or doc.main_start)
    dx = 0 if page % 2 == 1 else -GUTTER_SHIFT
    canv.saveState()
    canv.setFont(SANS, 8.2)
    canv.setFillColor(SOFT)
    y = PAGE_H - M_TOP + 22
    if page % 2 == 1:
        canv.drawRightString(PAGE_W - M_OUT, y, 'MASTER SPEAKING')
    else:
        canv.drawString(M_IN, y, doc.head_left or '')
    canv.setStrokeColor(RULE)
    canv.setLineWidth(0.6)
    canv.line(PAGE_W / 2 - 100, y - 4.5, PAGE_W / 2 + 100, y - 4.5)
    canv.setFont(SANS, 8.8)
    canv.drawCentredString(PAGE_W / 2, M_BOT / 2 + 4, folio)
    canv.restoreState()
    if dx:
        canv.translate(dx, 0)

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table as DxTable
from docx.text.paragraph import Paragraph as DxPara
from docx.document import Document as DxDocument

from reportlab.lib.pagesizes import inch as IN
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (Paragraph, Spacer, PageBreak, Image, Table,
                                TableStyle, Frame, PageTemplate,
                                NextPageTemplate, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab import rl_config

ROOT = os.path.dirname(os.path.dirname(HERE))       # repo root
SRC = os.path.join(ROOT, 'Master-Speaking-7x10.docx')
OUT = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')

EMU_PT = 72.0 / 914400.0

# docx style name -> ReportLab style key (S[...] built by pdf.build_styles)
STYMAP = {
    'MS Book Title': 'booktitle', 'MS Author': 'author',
    'MS Copyright Line': 'copyright', 'MS FM Head': 'fmhead',
    'MS FM Sub': 'fmsub', 'MS Epigraph': 'epigraph',
    'MS TOC Heading': 'tochead', 'MS Unit Title': 'unittitle',
    'MS Chapter Title': 'chaptitle', 'MS Section': 'sec',
    'MS Subsection': 'sub', 'MS Reading Title': 'readingtitle',
    'MS Body': 'body', 'MS Instruction': 'instr', 'MS Label': 'label',
    'MS Topic': 'topic', 'MS Title Line': 'titleline',
    'MS Media Title': 'mediatitle', 'MS RunIn': 'subsub',
    'MS Question': 'q', 'MS Option': 'opt', 'MS Statement': 'tf',
    'MS Reading': 'reading', 'MS Note': 'note', 'List Bullet': 'li',
    'MS Signature': 'signature', 'MS Sign Date': 'signdate',
}

_img_cache = {}


def para_flows(p, doc, ctx=None):
    """One docx paragraph -> list of flowables (markup + images + breaks)."""
    out = []
    name = p.style.name if p.style is not None else 'MS Body'
    skey = STYMAP.get(name, 'body')
    segs = []            # (text, bold, italic) fragments
    def flush():
        if not segs:
            return
        mk = ''
        for txt, b, i in segs:
            t = fallback(txt, S[skey].fontName.split('-')[0]
                         if False else (SERIF if skey in
                                        ('body', 'q', 'opt', 'tf', 'reading',
                                         'note', 'pair', 'li', 'epigraph',
                                         'titleline', 'copyright')
                                         else SANS))
            if b and i:
                mk += f'<b><i>{t}</i></b>'
            elif b:
                mk += f'<b>{t}</b>'
            elif i:
                mk += f'<i>{t}</i>'
            else:
                mk += t
        if not mk.strip() and mk == '':
            return
        out.append(Paragraph(mk, S[skey]))
        segs.clear()
    for r in p.runs:
        rpr = r._r.find(qn('w:rPr'))
        # skip field machinery (TOC fields render via our own TOC flowable)
        if r._r.findall(qn('w:fldChar')) or r._r.findall(qn('w:instrText')):
            if r._r.findall(qn('w:instrText')):
                instr = ''.join(r._r.itertext())
                if 'TOC' in instr:
                    out.append(('__TOC_FIELD__',))
            continue
        blips = r._r.findall('.//' + qn('a:blip'))
        if blips:
            flush()
            for b in blips:
                rid = b.get(qn('r:embed'))
                if not rid:
                    continue
                part = doc.part.related_parts.get(rid)
                if part is None:
                    continue
                fn = os.path.join(_img_cache_dir, f'{rid}.img')
                if rid not in _img_cache:
                    with open(fn, 'wb') as fh:
                        fh.write(part.blob)
                    _img_cache[rid] = fn
                ext = r._r.find('.//' + qn('wp:extent'))
                w = int(ext.get('cx')) * EMU_PT if ext is not None else 0
                h = int(ext.get('cy')) * EMU_PT if ext is not None else 0
                if w <= 0:
                    from PIL import Image as PILImage
                    with PILImage.open(_img_cache[rid]) as im:
                        w, hh = im.size
                    h = w and hh
                    w = min(w, TEXT_W)
                w = min(w, TEXT_W)
                if h and w:
                    f = Image(_img_cache[rid], width=w, height=h)
                    f.hAlign = 'CENTER'
                    out.append(f)
            continue
        txt = r.text
        if not txt:
            continue
        segs.append((txt, bool(r.bold), bool(r.italic)))
    flush()
    return out


def has_page_break_before(p):
    if p.paragraph_format.page_break_before:
        return True
    ppr = p._p.find(qn('w:pPr'))
    if ppr is not None and ppr.find(qn('w:pageBreakBefore')) is not None:
        return True
    st = p.style
    while st is not None:
        if st.paragraph_format.page_break_before:
            return True
        st = st.base_style
    return False


def cell_fill(cell):
    tcpr = cell._tc.find(qn('w:tcPr'))
    if tcpr is None:
        return None
    shd = tcpr.find(qn('w:shd'))
    if shd is None:
        return None
    v = shd.get(qn('w:fill'))
    return v if v and v not in ('auto', 'FFFFFF') else None


def is_header_row(row):
    trpr = row._tr.find(qn('w:trPr'))
    return trpr is not None and trpr.find(qn('w:tblHeader')) is not None


def table_flow(t, doc):
    grid = [int(g.get(qn('w:w')) or 0) for g in
            t._tbl.find(qn('w:tblGrid')).findall(qn('w:gridCol'))]
    if not grid:
        return []
    ncol = len(grid)
    scale = TEXT_W / (sum(grid) / 20.0) if sum(grid) else 1.0
    widths = [max(g / 20.0 * scale, 0.4 * IN) for g in grid]
    over = sum(widths) - TEXT_W
    if over > 0 and ncol > 1:
        widths[widths.index(max(widths))] -= over

    fills = [cell_fill(c) for row in t.rows for c in row.cells
             if cell_fill(c)]
    tbl_fill = max(set(fills), key=fills.count) if fills else None
    header = t.rows and is_header_row(t.rows[0])

    data = []
    for row in t.rows:
        cells = []
        for cell in row.cells:
            flows = []
            for p in cell.paragraphs:
                fl = para_flows(p, doc)
                fl = [f for f in fl if not isinstance(f, tuple)]
                if not fl:
                    continue
                flows.extend(fl)
            if not flows:
                flows = [Paragraph('', S['tabcell'])]
            cells.append(flows if len(cells) == 0 else flows)
        data.append(cells)

    style = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('GRID', (0, 0), (-1, -1), 0.5, RULE),
    ]
    if tbl_fill in ('B9E9B5', 'BFDDAB'):
        fc = BOX_GREEN if tbl_fill == 'B9E9B5' else BOX_OLIVE
        style += [('BACKGROUND', (0, 0), (-1, -1), fc),
                  ('GRID', (0, 0), (-1, -1), 1.0, colors.white),
                  ('LEFTPADDING', (0, 0), (-1, -1), 9),
                  ('RIGHTPADDING', (0, 0), (-1, -1), 9),
                  ('TOPPADDING', (0, 0), (-1, -1), 6),
                  ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]
    elif header:
        style.append(('BACKGROUND', (0, 0), (-1, 0), BAND))
        for ri in range(1, len(data)):
            if ri % 2 == 0:
                style.append(('BACKGROUND', (0, ri), (-1, ri), ZEBRA))
    else:
        for ri in range(len(data)):
            if ri % 2 == 1:
                style.append(('BACKGROUND', (0, ri), (-1, ri), ZEBRA))

    tab = Table(data, colWidths=widths, hAlign='LEFT')
    tab.setStyle(TableStyle(style))
    return [Spacer(1, 3), tab, Spacer(1, 8)]


_img_cache_dir = tempfile.mkdtemp(prefix='docxpdf-img-')


def iter_body(doc):
    for child in doc.element.body:
        if child.tag == qn('w:p'):
            yield DxPara(child, doc)
        elif child.tag == qn('w:tbl'):
            yield DxTable(child, doc)


def paragraph_closes_section(p):
    ppr = p._p.find(qn('w:pPr'))
    return ppr is not None and ppr.find(qn('w:sectPr')) is not None


def main():
    register_fonts()
    rl_config.canvas_basefontname = SANS
    build_styles()

    dx = Document(SRC)

    # main_start (first decimal-folio page) is PINNED across builds so that
    # folios and TOC numbers are pass-independent (fixpoint on unit-1 page)
    FIXED_MS = None
    extra_breaks = set()
    for attempt in range(8):
        doc = BookDoc(OUT, pagesize=(PAGE_W, PAGE_H),
                      leftMargin=M_IN, rightMargin=M_OUT,
                      topMargin=M_TOP, bottomMargin=M_BOT,
                      title='Master Speaking', author='Abdul Raziq Nazari')
        frame = Frame(M_IN, M_BOT, TEXT_W, PAGE_H - M_TOP - M_BOT, id='main',
                      leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)
        doc.addPageTemplates([
            PageTemplate(id='fm', frames=[frame], onPage=on_page_fm),
            PageTemplate(id='main', frames=[frame], onPage=on_page_main),
            PageTemplate(id='opener', frames=[frame], onPage=on_page_opener),
        ])
        toc = TableOfContents()
        toc.levelStyles = [S['toc0'], S['toc1']]
        toc.tableStyle = TableStyle(
            [('FONTNAME', (0, 0), (-1, -1), SANS),
             ('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('LEFTPADDING', (0, 0), (-1, -1), 0),
             ('RIGHTPADDING', (0, 0), (-1, -1), 0),
             ('TOPPADDING', (0, 0), (-1, -1), 0),
             ('BOTTOMPADDING', (0, 0), (-1, -1), 0)])
        toc.dotsMinLevel = 1
        MS_FIXED[0] = FIXED_MS
        toc.formatter = lambda page: folio_for(page, FIXED_MS or doc.main_start)

        story = []
        cur_unit = 0
        unit_seen = False
        for el in iter_body(dx):
            if isinstance(el, DxPara):
                name = el.style.name if el.style is not None else ''
                # section boundary: end of front matter (roman folios)
                if paragraph_closes_section(el):
                    # section boundary already emitted at the TOC; keep any
                    # real text, never re-emit the page machinery
                    for f in para_flows(el, dx):
                        if not isinstance(f, tuple) and f.getPlainText().strip():
                            story.append(f)
                    continue
                if name == 'MS TOC Heading':
                    continue                       # rendered below
                flows = para_flows(el, dx)
                if any(isinstance(f, tuple) for f in flows):
                    # docx TOC field -> our generated Contents; the body
                    # starts on a fresh page with decimal folios
                    story.append(PageBreak())
                    story.append(Paragraph('Contents', S['tochead']))
                    story.append(toc)
                    story.append(NextPageTemplate('main'))
                    story.append(PageBreak())
                    if FIXED_MS:
                        story.append(State(doc, main_start=FIXED_MS))
                    else:
                        story.append(State(doc, main_start=None))
                    continue
                if name == 'MS Unit Title':
                    cur_unit += 1
                    unit_seen = True
                    story.append(NextPageTemplate('opener'))
                    if has_page_break_before(el) or cur_unit > 1:
                        story.append(PageBreak())
                    if cur_unit in extra_breaks:
                        story.append(PageBreak())
                    txt = ''.join(r.text for r in el.runs)
                    for f in flows:
                        if isinstance(f, Paragraph):
                            f._toc = (0, txt)
                            f._tockey = f'unit-{cur_unit}'
                    story.extend(f for f in flows if not isinstance(f, tuple))
                    story.append(State(doc, head_left=txt, head_right=''))
                    continue
                if name == 'MS Chapter Title':
                    if has_page_break_before(el):
                        story.append(PageBreak())
                    if not unit_seen:
                        unit_seen = unit_seen
                    txt = ''.join(r.text for r in el.runs)
                    for f in flows:
                        if isinstance(f, Paragraph):
                            f._toc = (1, txt)
                            f._tockey = f'unit-{cur_unit}-ch-{txt[:24]}'
                    story.extend(f for f in flows if not isinstance(f, tuple))
                    continue
                if has_page_break_before(el):
                    story.append(PageBreak())
                story.extend(f for f in flows if not isinstance(f, tuple))
                # after the warm-up table, body template resumes
                if name == 'MS Chapter Title':
                    story.append(NextPageTemplate('main'))
            elif isinstance(el, DxTable):
                story.extend(table_flow(el, dx))
                if not unit_seen:
                    continue
                # warm-up box ends the opener page pattern
                fills = [cell_fill(c) for row in el.rows for c in row.cells]
                if fills and fills[0] == 'B9E9B5' and cur_unit:
                    story.append(NextPageTemplate('main'))
        doc.multiBuild(story)
        bad = sorted((pg, int(k.split('-')[1])) for k, pg in
                     doc.unit_pages.items() if pg % 2 == 0)
        u1 = doc.unit_pages.get('unit-1')
        # unit 1 must open the decimal sequence: folio(u1) == 1
        if FIXED_MS != u1:
            FIXED_MS = u1
            continue
        if not bad:
            break
        extra_breaks.add(bad[0][1])
    else:
        raise SystemExit('recto forcing did not converge')
    print(f'PDF written: {OUT} ({os.path.getsize(OUT):,} bytes) | '
          f'unit pages: {sorted(doc.unit_pages.items())}')


if __name__ == '__main__':
    main()

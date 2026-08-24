#!/usr/bin/env python3
"""pdf.py — print typesetter for Master Speaking.

Input : book/master/master.xhtml (editable source of truth)
Output: Master-Speaking-print-7x10.pdf (print-ready, 7 x 10 in)

Design system
-------------
Trim 7x10in. Margins: top 0.78in, bottom 0.80in, inside (gutter) 0.82in,
outside 0.72in — mirrored via canvas offset. Body: Source Serif 4 10.3/15.2,
justified, hyphenated (en_US), widow/orphan controlled. Heads: Source Sans 3.
Single accent colour (deep teal #0E6E5C). Unit openers start on recto; chapters
start on a fresh page. Running heads on main pages; folios bottom-centre;
front matter in roman numerals, main text in arabic from Unit 1. TOC with dot
leaders and real folios (multiBuild + formatter). Fonts fully embedded; DejaVu
Sans used as automatic glyph fallback for IPA/symbols. Tables repeat header
rows. Images aspect-true.
"""
import os, re
from lxml import etree
from reportlab import rl_config
from reportlab.lib.units import inch as IN
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Table, TableStyle, Image,
                                KeepTogether, NextPageTemplate, Flowable)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage
from fontTools.ttLib import TTFont as FTFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER = os.path.join(ROOT, 'book', 'master', 'master.xhtml')
FONTS = os.path.join(ROOT, 'book', 'assets', 'fonts')
IMAGES = os.path.join(ROOT, 'book', 'assets', 'images')
OUT = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')

PAGE_W, PAGE_H = 7 * IN, 10 * IN
M_TOP, M_BOT = 0.78 * IN, 0.80 * IN
M_IN, M_OUT = 0.82 * IN, 0.72 * IN
TEXT_W = PAGE_W - M_IN - M_OUT
GUTTER_SHIFT = M_IN - M_OUT          # mirrored-margin offset applied to verso pages

INK = colors.HexColor('#14181A')
# ---- original manuscript visual identity (audited from Master Speaking.docx)
BAND = colors.HexColor('#7BE1D0')      # mint band behind section headings
BANNER = colors.HexColor('#92D050')    # bright green: FM banners, chapter titles
ACCENT = colors.HexColor('#00B050')    # deep green: kickers, labels, bullets
ACCENT_HEX = '#00B050'
BOX_GREEN = colors.HexColor('#B9E9B5')  # light-green box fill (U1-5 vocab, warm-ups)
BOX_OLIVE = colors.HexColor('#BFDDAB')  # pale-olive box fill (U6-8 vocab)
RULE = colors.HexColor('#A9D8A0')
ZEBRA = colors.HexColor('#F0F8EC')
FILL_MAP = {'B9E9B5': BOX_GREEN, 'BFDDAB': BOX_OLIVE}
SOFT = colors.HexColor('#5A6B66')

SERIF, SANS, FALLBACK = 'SourceSerif', 'SourceSans', 'DejaVuSans'
NS = {'x': 'http://www.w3.org/1999/xhtml'}

# ---------------------------------------------------------------- fonts -----
def register_fonts():
    reg = pdfmetrics.registerFont
    reg(TTFont(SERIF, f'{FONTS}/source-serif-4-latin-400-normal.ttf'))
    reg(TTFont(SERIF + '-I', f'{FONTS}/source-serif-4-latin-400-italic.ttf'))
    reg(TTFont(SERIF + '-B', f'{FONTS}/source-serif-4-latin-700-normal.ttf'))
    reg(TTFont(SANS, f'{FONTS}/source-sans-3-latin-400-normal.ttf'))
    reg(TTFont(SANS + '-I', f'{FONTS}/source-sans-3-latin-400-italic.ttf'))
    reg(TTFont(SANS + '-SB', f'{FONTS}/source-sans-3-latin-600-normal.ttf'))
    reg(TTFont(SANS + '-B', f'{FONTS}/source-sans-3-latin-700-normal.ttf'))
    reg(TTFont(FALLBACK, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    registerFontFamily(SERIF, normal=SERIF, bold=SERIF+'-B', italic=SERIF+'-I',
                       boldItalic=SERIF+'-B')
    registerFontFamily(SANS, normal=SANS, bold=SANS+'-B', italic=SANS+'-I',
                       boldItalic=SANS+'-B')

_cmaps = {}
def cmap_of(name):
    path = {SERIF: 'source-serif-4-latin-400-normal.ttf',
            SANS: 'source-sans-3-latin-400-normal.ttf'}.get(name)
    if path is not None and name not in _cmaps:
        try:
            _cmaps[name] = set(FTFont(os.path.join(FONTS, path)).getBestCmap().keys())
        except Exception:
            _cmaps[name] = set()
    if FALLBACK not in _cmaps:
        _cmaps[FALLBACK] = set(FTFont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
                               .getBestCmap().keys())
    return _cmaps.get(name, _cmaps[FALLBACK])

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

def fallback(text, base=SERIF):
    have = cmap_of(base)
    out, buf, cur = [], [], None
    for ch in text:
        ok = ord(ch) in have
        if cur is None or ok == cur:
            buf.append(ch); cur = ok
        else:
            seg = esc(''.join(buf))
            out.append(seg if cur else f'<font face="{FALLBACK}">{seg}</font>')
            buf = [ch]; cur = ok
    if buf:
        seg = esc(''.join(buf))
        out.append(seg if cur else f'<font face="{FALLBACK}">{seg}</font>')
    return ''.join(out)

def rich_text(el, base=SERIF):
    parts = []
    def walk(node):
        for child in node:
            if not isinstance(child.tag, str):
                continue
            tag = etree.QName(child).localname
            inner = fallback(''.join(child.itertext()), base)
            if tag in ('strong', 'b'):
                parts.append('<strong>' + inner + '</strong>')
            elif tag in ('em', 'i'):
                parts.append('<em>' + inner + '</em>')
            else:
                walk(child)
            if child.tail:
                parts.append(fallback(child.tail, base))
    if el.text:
        parts.append(fallback(el.text, base))
    walk(el)
    return ''.join(parts)

# ---------------------------------------------------------------- styles ----
S = {}
def build_styles():
    P = ParagraphStyle
    S['body'] = P('body', fontName=SERIF, fontSize=10.3, leading=15.2,
                  alignment=TA_JUSTIFY, textColor=INK, spaceAfter=6.5,
                  hyphenationLang='en_US', allowWidows=0, allowOrphans=0,
                  embeddedHyphenation=1)
    S['reading'] = P('reading', parent=S['body'], leading=15.4)
    S['instr'] = P('instr', fontName=SANS+'-I', fontSize=9.6, leading=13.6,
                   textColor=SOFT, alignment=TA_LEFT, spaceBefore=2, spaceAfter=5,
                   hyphenationLang='en_US', allowWidows=0, allowOrphans=0)
    S['label'] = P('label', fontName=SANS+'-SB', fontSize=9.6, leading=13.5,
                   alignment=TA_LEFT, spaceBefore=3, spaceAfter=3, keepWithNext=1)
    S['topic'] = P('topic', fontName=SANS+'-SB', fontSize=10.8, leading=14.5,
                   alignment=TA_LEFT, textColor=INK, backColor=BAND,
                   borderPadding=(2, 5, 3, 5), spaceBefore=7, spaceAfter=5,
                   keepWithNext=1)
    S['titleline'] = P('titleline', fontName=SERIF+'-I', fontSize=10.5, leading=14.5,
                       alignment=TA_LEFT, spaceAfter=4, keepWithNext=0)
    S['mediatitle'] = P('mediatitle', fontName=SANS+'-SB', fontSize=11.5, leading=15,
                        alignment=TA_LEFT, spaceBefore=1, spaceAfter=7, keepWithNext=1)
    S['q'] = P('q', parent=S['body'], leftIndent=22, firstLineIndent=-22,
               alignment=TA_LEFT, spaceAfter=5, leading=14.8)
    S['opt'] = P('opt', parent=S['body'], leftIndent=40, firstLineIndent=-14,
                 alignment=TA_LEFT, spaceAfter=2.5, fontSize=10.1)
    S['tf'] = P('tf', parent=S['body'], leftIndent=26, firstLineIndent=-26,
                alignment=TA_LEFT, spaceAfter=5)
    S['fill'] = P('fill', parent=S['body'], leftIndent=18, firstLineIndent=-18,
                  alignment=TA_LEFT, spaceAfter=5)
    S['pair'] = P('pair', parent=S['body'], leftIndent=16, firstLineIndent=-16,
                  alignment=TA_LEFT, spaceAfter=3.5)
    S['li'] = P('li', parent=S['body'], leftIndent=18, firstLineIndent=-18,
                alignment=TA_LEFT, spaceAfter=3.5)
    S['note'] = P('note', fontName=SERIF+'-I', fontSize=9.8, leading=14,
                  textColor=SOFT, leftIndent=2, rightIndent=4, alignment=TA_LEFT)
    S['sec'] = P('sec', fontName=SANS+'-SB', fontSize=13, leading=16,
                 textColor=INK, backColor=BAND,
                 borderPadding=(2.5, 5, 3.5, 5),
                 spaceBefore=16, spaceAfter=6, keepWithNext=1)
    S['sub'] = P('sub', fontName=SANS+'-SB', fontSize=10.8, leading=14,
                 textColor=ACCENT, spaceBefore=11, spaceAfter=3.5, keepWithNext=1)
    S['subsub'] = P('subsub', fontName=SANS+'-B', fontSize=9.4, leading=12.5,
                    spaceBefore=8, spaceAfter=2.5, keepWithNext=1)
    S['readingtitle'] = P('readingtitle', fontName=SERIF+'-B', fontSize=14.5,
                          leading=18.5, spaceBefore=6, spaceAfter=7, keepWithNext=1)
    S['unitkicker'] = P('unitkicker', fontName=SANS+'-SB', fontSize=12.5, leading=15,
                        textColor=ACCENT, spaceAfter=8)
    S['unittitle'] = P('unittitle', fontName=SERIF+'-B', fontSize=27, leading=31,
                       textColor=INK, backColor=BAND,
                       borderPadding=(3, 6, 5, 6), spaceAfter=8)
    S['chapkicker'] = P('chapkicker', fontName=SANS+'-SB', fontSize=10.5, leading=13,
                        textColor=ACCENT, spaceAfter=5)
    S['chaptitle'] = P('chaptitle', fontName=SERIF+'-B', fontSize=17.5, leading=21.5,
                       textColor=BANNER, spaceAfter=6)
    S['warmhead'] = P('warmhead', fontName=SANS+'-SB', fontSize=11, leading=14,
                      textColor=ACCENT, spaceAfter=4)
    S['fmhead'] = P('fmhead', fontName=SERIF+'-B', fontSize=19, leading=24,
                    textColor=colors.white, backColor=BANNER,
                    borderPadding=(3, 6, 4, 6), spaceAfter=14, alignment=TA_LEFT)
    S['fmsub'] = P('fmsub', fontName=SANS+'-SB', fontSize=11.5, leading=15,
                   textColor=ACCENT, spaceBefore=10, spaceAfter=5, keepWithNext=1)
    S['fmsub2'] = P('fmsub2', fontName=SANS+'-SB', fontSize=10.5, leading=14,
                    spaceBefore=9, spaceAfter=3, keepWithNext=1)
    S['halftitle'] = P('halftitle', fontName=SERIF+'-B', fontSize=22, leading=27,
                       alignment=TA_CENTER)
    S['booktitle'] = P('booktitle', fontName=SERIF+'-B', fontSize=34, leading=40,
                       alignment=TA_CENTER)
    S['author'] = P('author', fontName=SANS+'-SB', fontSize=13, leading=17,
                    textColor=ACCENT, alignment=TA_CENTER)
    S['copyright'] = P('copyright', fontName=SERIF, fontSize=9.3, leading=13.5,
                       alignment=TA_LEFT, spaceAfter=6)
    S['epigraph'] = P('epigraph', fontName=SERIF+'-I', fontSize=12.5, leading=19,
                      alignment=TA_CENTER, leftIndent=40, rightIndent=40)
    S['signature'] = P('signature', fontName=SANS+'-SB', fontSize=10.5, leading=14,
                       spaceBefore=14)
    S['signdate'] = P('signdate', fontName=SANS, fontSize=9.8, leading=13,
                      textColor=SOFT)
    S['toc0'] = P('toc0', fontName=SANS+'-SB', fontSize=11, leading=15, spaceBefore=4)
    S['toc1'] = P('toc1', fontName=SERIF, fontSize=10, leading=13.2, leftIndent=18)
    S['tochead'] = P('tochead', fontName=SERIF+'-B', fontSize=19, leading=24,
                     textColor=colors.white, backColor=BANNER,
                     borderPadding=(3, 6, 4, 6), spaceAfter=16)
    S['tabhead'] = P('tabhead', fontName=SANS+'-SB', fontSize=8.8, leading=11.5,
                     textColor=INK, alignment=TA_LEFT)
    S['tabcell'] = P('tabcell', fontName=SERIF, fontSize=9.2, leading=12.2,
                     textColor=INK, alignment=TA_LEFT)
    for st in S.values():
        st.bulletFontName = SANS

# ------------------------------------------------------------- helpers ------
def text_of(el):
    return ''.join(el.itertext()).strip()

def Q(el, p):
    return el.xpath(p, namespaces=NS)

def para(el, style):
    return Paragraph(rich_text(el), style)

MIN_PRINT_DPI = 150
def image_flow(src, max_w):
    path = os.path.join(IMAGES, os.path.basename(src))
    if src.endswith('.gif') and os.path.exists(path.replace('.gif', '.png')):
        path = path.replace('.gif', '.png')
    if not os.path.exists(path):
        return None
    with PILImage.open(path) as im:
        w, h = im.size
    dpi_cap = w * 72.0 / MIN_PRINT_DPI      # keep >= 150 effective dpi
    draw_w = min(max_w, TEXT_W, dpi_cap)
    f = Image(path, width=draw_w, height=draw_w * h / w)
    f.hAlign = 'CENTER'
    return f

class State(Flowable):
    """Sets doc attributes at draw time (page parity forcing, folio epoch)."""
    def __init__(self, doc, **attrs):
        Flowable.__init__(self)
        self.doc, self.attrs = doc, attrs
        self.width = self.height = 0
    def wrap(self, aw, ah):
        return (0, 0)
    def draw(self):
        for k, v in self.attrs.items():
            setattr(self.doc, k, self.canv.getPageNumber() if v is None else v)

class PageEnv(Flowable):
    """Requests a recto page break if the next page would not be recto."""
    def __init__(self, doc):
        Flowable.__init__(self)
        self.doc = doc
        self.width = self.height = 0
    def wrap(self, aw, ah):
        return (0, 0)
    def draw(self):
        pass

ROMAN = ['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii',
         'xiv','xv','xvi','xvii','xviii']

def folio_for(page, main_start):
    if main_start is None or page < main_start:
        return ROMAN[page-1] if 0 < page <= len(ROMAN) else str(page)
    return str(page - main_start + 1)

# ------------------------------------------------------------ doc template --
class BookDoc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, **kw)
        self.main_start = None
        self.head_left = 'Master Speaking'
        self.head_right = ''
        self.unit_pages = {}

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        if flowable.style.name == 'unittitle':
            key = getattr(flowable, '_tockey', None)
            if key:
                self.unit_pages[key] = self.page
        toc = getattr(flowable, '_toc', None)
        if toc:
            level, text = toc
            key = getattr(flowable, '_tockey', None)
            if key:
                self.canv.bookmarkPage(key)
                olevel = 0 if level == 0 else 1
                if level == 0:
                    try:
                        self.canv.addOutlineEntry(text, key, level=0, closed=False)
                    except Exception:
                        pass
                else:
                    try:
                        self.canv.addOutlineEntry(text, key, level=1, closed=False)
                    except Exception:
                        pass
            self.notify('TOCEntry', (level, text, self.page, key))

def on_page(canv, doc, kind):
    page = canv.getPageNumber()
    folio = folio_for(page, doc.main_start)
    dx = 0 if page % 2 == 1 else -GUTTER_SHIFT     # verso pages shift left
    canv.saveState()
    canv.setFont(SANS, 8.8)
    canv.setFillColor(SOFT)
    canv.drawCentredString(PAGE_W / 2, M_BOT / 2 + 4, folio)
    if kind == 'main':
        head = doc.head_left + ('   ·   ' + doc.head_right if doc.head_right else '')
        canv.setFont(SANS, 8.2)
        y = PAGE_H - M_TOP + 22
        canv.drawCentredString(PAGE_W / 2, y, head)
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.6)
        canv.line(PAGE_W / 2 - 100, y - 4.5, PAGE_W / 2 + 100, y - 4.5)
    canv.restoreState()
    if dx:
        canv.translate(dx, 0)     # mirrored margins for the flowables drawn next

def on_page_v(canv, doc): on_page(canv, doc, 'main')
def on_page_fm(canv, doc): on_page(canv, doc, 'fm')
def on_page_opener(canv, doc): on_page(canv, doc, 'opener')

class RectoBreak(Flowable):
    """Break to the next recto page (for unit openers)."""
    def __init__(self, doc, state_attrs):
        Flowable.__init__(self)
        self.doc = doc
        self.state_attrs = state_attrs
        self.width = self.height = 0
    def wrap(self, aw, ah):
        return (0, 0)
    def draw(self):
        pass

# ---------------------------------------------------------------- tables ----
def table_flow(el):
    header, data = [], []
    thead = Q(el, './x:thead/x:tr')
    if thead:
        header = [text_of(th) for th in Q(thead[0], './x:th')]
    body_rows = Q(el, './x:tbody/x:tr')
    rows_txt = [[text_of(td) for td in Q(r, './x:td')] for r in body_rows]
    all_rows = ([header] if header else []) + rows_txt
    ncol = max((len(r) for r in all_rows), default=0)
    if ncol == 0:
        return None
    cls = (el.get('class') or '').split()
    role = cls[-1] if len(cls) > 1 else 'generic'
    fill = FILL_MAP.get(el.get('data-fill') or '')
    if role in ('questions', 'warmup'):
        # write-in tables: question + answer space, minimal rules
        data = [[Paragraph(fallback(t), S['tabcell']) for t in r] + [Paragraph('', S['tabcell'])]
                for r in rows_txt]
        widths = [TEXT_W * 0.62] + [TEXT_W * 0.38 / (ncol - 1)] * (ncol - 1) if ncol > 1 else [TEXT_W]
        t = Table(data, colWidths=widths, hAlign='LEFT')
        t.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,-1), SANS),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 4.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
            ('LEFTPADDING', (0,0), (-1,-1), 2),
            ('LINEBELOW', (0,0), (-1,-2), 0.5, RULE),
        ]))
        return [Spacer(1, 3), t, Spacer(1, 8)]
    data = []
    if header:
        data.append([Paragraph(fallback(h, SANS), S['tabhead']) for h in header])
    for r in rows_txt:
        row = [Paragraph(fallback(t), S['tabcell']) for t in r]
        while len(row) < ncol:
            row.append(Paragraph('', S['tabcell']))
        data.append(row)
    weights = []
    for ci in range(ncol):
        wsum = 0
        for row in data:
            txt = row[ci].getPlainText() if ci < len(row) else ''
            wsum += min(len(txt), 90)
        weights.append(max(wsum, 10))
    total = sum(weights)
    min_w = 50 if ncol >= 3 else 70
    widths = [max(min_w, TEXT_W * w / total) for w in weights]
    over = sum(widths) - TEXT_W
    if over > 0:
        widths[widths.index(max(widths))] -= over
    # never narrower than the longest unbreakable token (prevents ReportLab
    # splitLongWords mid-word breaks like "underst / and" in vocab columns)
    from reportlab.pdfbase.pdfmetrics import stringWidth
    style_cell = S['tabcell']
    pad = 10 + 2                                    # cell padding + slack
    needs = []
    for ci in range(ncol):
        longest = 0
        for row in data:
            txt = row[ci].getPlainText() if ci < len(row) else ''
            for tok in txt.split():
                longest = max(longest, stringWidth(
                    tok, style_cell.fontName, style_cell.fontSize))
        needs.append(longest + pad)
    for ci in range(ncol):
        if widths[ci] < needs[ci]:
            widths[ci] = needs[ci]
    excess = sum(widths) - TEXT_W
    if excess > 0:
        # reclaim from columns with surplus over their need, proportionally
        surplus = [max(0.0, widths[ci] - needs[ci]) for ci in range(ncol)]
        pool = sum(surplus)
        if pool >= excess - 0.01:
            for ci in range(ncol):
                widths[ci] -= excess * surplus[ci] / pool if pool else 0
        else:
            # extreme case: shrink every column proportionally
            k = TEXT_W / sum(widths)
            widths = [w * k for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    style = [('FONTNAME', (0,0), (-1,-1), SANS),
             ('VALIGN', (0,0), (-1,-1), 'TOP'),
             ('TOPPADDING', (0,0), (-1,-1), 3.5),
             ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
             ('LEFTPADDING', (0,0), (-1,-1), 5),
             ('RIGHTPADDING', (0,0), (-1,-1), 5),
             ('GRID', (0,0), (-1,-1), 0.5, RULE)]
    if fill:
        # original identity: solid pastel box with white separators
        style += [('BACKGROUND', (0,0), (-1,-1), fill),
                  ('GRID', (0,0), (-1,-1), 1.0, colors.white)]
        if header:
            style += [('TOPPADDING', (0,0), (-1,0), 4),
                      ('BOTTOMPADDING', (0,0), (-1,0), 4)]
    elif header:
        style += [('BACKGROUND', (0,0), (-1,0), BAND),
                  ('TOPPADDING', (0,0), (-1,0), 4),
                  ('BOTTOMPADDING', (0,0), (-1,0), 4)]
        for ri in range(1, len(data)):
            if ri % 2 == 0:
                style.append(('BACKGROUND', (0,ri), (-1,ri), ZEBRA))
    else:
        for ri in range(len(data)):
            if ri % 2 == 1:
                style.append(('BACKGROUND', (0,ri), (-1,ri), ZEBRA))
    t.setStyle(TableStyle(style))
    return [Spacer(1, 3), t, Spacer(1, 8)]

# ---------------------------------------------------------------- blocks ----
def bullet_para(text, style, marker, marker_font=SANS+'-SB', color=ACCENT_HEX):
    return Paragraph(f'<bullet><font name="{marker_font}" color="{color}">{marker}</font></bullet>'
                     + fallback(text), style)

def strip_opt_markers(t):
    return re.sub(r'^[A-Da-d][\.\)]\s+', '', t)

def build_list(ul):
    out = []
    cls_ = (ul.get('class') or 'items').split()[0]
    items = [text_of(li) for li in Q(ul, './x:li')]
    if cls_ == 'tf':
        out += [Paragraph(fallback(it), S['tf']) for it in items]
    elif cls_ == 'fill':
        out += [Paragraph(fallback(it), S['fill']) for it in items]
    elif cls_ in ('pairs', 'choices'):
        out += [bullet_para(it, S['pair'], '–', SANS+'-SB', ACCENT_HEX) for it in items]
    else:
        out += [bullet_para(it, S['li'], '•', SANS+'-SB', ACCENT_HEX) for it in items]
    return out

def wrap_block(flows, kind):
    if not flows:
        return []
    style = [('FONTNAME', (0,0), (-1,-1), SANS), ('VALIGN', (0,0), (-1,-1), 'TOP')]
    if kind == 'reading':
        style += [('LINEBEFORE', (0,0), (0,-1), 1.6, ACCENT),
                  ('LEFTPADDING', (0,0), (-1,-1), 12),
                  ('RIGHTPADDING', (0,0), (-1,-1), 4),
                  ('TOPPADDING', (0,0), (-1,0), 2),
                  ('BOTTOMPADDING', (0,-1), (-1,-1), 4)]
    elif kind == 'note':
        style += [('BACKGROUND', (0,0), (-1,-1), ZEBRA),
                  ('LINEBEFORE', (0,0), (0,-1), 1.6, ACCENT),
                  ('LEFTPADDING', (0,0), (-1,-1), 10),
                  ('RIGHTPADDING', (0,0), (-1,-1), 10),
                  ('TOPPADDING', (0,0), (-1,-1), 7),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 7)]
    elif kind == 'warmup':
        style += [('BACKGROUND', (0,0), (-1,-1), BOX_GREEN),
                  ('LINEBEFORE', (0,0), (0,-1), 2, BANNER),
                  ('LEFTPADDING', (0,0), (-1,-1), 12),
                  ('RIGHTPADDING', (0,0), (-1,-1), 10),
                  ('TOPPADDING', (0,0), (-1,-1), 9),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 9)]
    t = Table([[flows]], colWidths=[TEXT_W])
    t.setStyle(TableStyle(style))
    return t

def section_fig(fig_el, max_w=None):
    img = fig_el.find('x:img', NS)
    if img is None:
        return None
    cls = fig_el.get('class') or ''
    if max_w is None:
        max_w = TEXT_W * 0.72 if 'unit-figure' in cls else TEXT_W * 0.86
    return image_flow(img.get('src'), max_w)

def content_flowables(section, story):
    for el in section:
        if not isinstance(el.tag, str):
            continue
        tag = etree.QName(el).localname
        cls_ = (el.get('class') or '').split()
        if tag == 'h3':
            story.append(Paragraph(fallback(text_of(el)), S['sec']))
        elif tag == 'h4':
            st = 'readingtitle' if 'reading-title' in cls_ else 'sub'
            story.append(Paragraph(fallback(text_of(el)), S[st]))
            if st == 'readingtitle':
                fig = Q(section, f'./x:h4/following-sibling::x:figure[1]')
                # figure handled by iteration below
        elif tag == 'h5':
            story.append(Paragraph(fallback(text_of(el)), S['subsub']))
        elif tag == 'p':
            k = cls_[0] if cls_ else 'body'
            stmap = {'instr': 'instr', 'label': 'label', 'topic': 'topic',
                     'titleline': 'titleline', 'media-title': 'mediatitle',
                     'reading': 'reading'}
            st = stmap.get(k, 'body')
            if k == 'titleline':
                story.append(Paragraph('<em>' + fallback(text_of(el)) + '</em>', S[st]))
            else:
                story.append(para(el, S[st]))
        elif tag == 'div' and 'note' in cls_:
            p = Q(el, './x:p')[0]
            story.append(Spacer(1, 4))
            story.append(wrap_block([para(p, S['note'])], 'note'))
            story.append(Spacer(1, 6))
        elif tag == 'div' and 'reading-block' in cls_:
            fig = el.find('x:figure', NS)
            if fig is not None:
                f = section_fig(fig, TEXT_W * 0.7)
                if f:
                    story.append(Spacer(1, 2))
                    story.append(f)
                    story.append(Spacer(1, 8))
            paras = Q(el, './x:p')
            for pi, pr in enumerate(paras):
                st = [('FONTNAME', (0,0), (-1,-1), SANS),
                      ('VALIGN', (0,0), (-1,-1), 'TOP'),
                      ('LINEBEFORE', (0,0), (0,-1), 1.6, ACCENT),
                      ('LEFTPADDING', (0,0), (-1,-1), 12),
                      ('RIGHTPADDING', (0,0), (-1,-1), 2)]
                if pi == 0:
                    st.append(('TOPPADDING', (0,0), (-1,-1), 2))
                else:
                    st.append(('TOPPADDING', (0,0), (-1,-1), 0))
                if pi == len(paras) - 1:
                    st.append(('BOTTOMPADDING', (0,0), (-1,-1), 4))
                else:
                    st.append(('BOTTOMPADDING', (0,0), (-1,-1), 0))
                t = Table([[para(pr, S['reading'])]], colWidths=[TEXT_W])
                t.setStyle(TableStyle(st))
                story.append(t)
            story.append(Spacer(1, 6))
        elif tag == 'div' and 'warmup' in cls_:
            warmup_flow(el, story)
        elif tag == 'ol':
            if 'questions' in cls_:
                n = 0
                for li in Q(el, './x:li'):
                    n += 1
                    opts = Q(li, './x:ol/x:li')
                    qtext = text_of(li)
                    qp = bullet_para(qtext, S['q'], f'{n}.')
                    if opts:
                        lts = 'ABCDEFGHIJ'
                        opt_ps = [bullet_para(strip_opt_markers(text_of(o)), S['opt'],
                                              f'{lts[i]}.', SANS, INK.hexval()[2:] and '#14181A')
                                  for i, o in enumerate(opts)]
                        story.append(KeepTogether([qp] + opt_ps))
                    else:
                        story.append(qp)
            elif 'options' in cls_:
                lts = 'ABCDEFGHIJ'
                for i, li in enumerate(Q(el, './x:li')):
                    story.append(bullet_para(strip_opt_markers(text_of(li)), S['opt'],
                                             f'{lts[i]}.', SANS, '#14181A'))
        elif tag == 'ul':
            story.extend(build_list(el))
        elif tag == 'table':
            tf = table_flow(el)
            if tf:
                story.extend(tf)
        elif tag == 'figure':
            f = section_fig(el)
            if f is not None:
                story.append(f)
                story.append(Spacer(1, 8))
    return story

def warmup_flow(el, story):
    flows = [Paragraph('THINK', S['warmhead'])]
    for sub in el:
        if not isinstance(sub.tag, str):
            continue
        tag = etree.QName(sub).localname
        if tag == 'h2':
            continue
        if tag == 'p':
            flows.append(para(sub, S['instr']))
        elif tag == 'table':
            tf = table_flow(sub)
            if tf:
                flows.extend(tf)
    story.append(Spacer(1, 6))
    story.append(wrap_block(flows, 'warmup'))

# ------------------------------------------------------------------ units ---
def unit_flowables(section, doc, first_unit):
    story = []
    name = text_of(section.find('.//x:span[@class="unit-name"]', NS))
    unum = int(section.get('data-unit'))
    # ensure recto start
    story.append(NextPageTemplate('opener'))
    story.append(PageBreak())
    if first_unit:
        story.append(State(doc, main_start=None))
    story.append(State(doc, head_right=name))
    h1 = section.find('x:h1', NS)
    kicker = text_of(h1.find('x:span[@class="unit-kicker"]', NS))
    k = para_mark(kicker.upper(), S['unitkicker'])
    t = Paragraph(fallback(name), S['unittitle'])
    t._toc = (0, f'Unit {unum}   {name}')
    t._tockey = f'unit-{unum}'
    story.append(k)
    story.append(t)
    rule = Table([['']], colWidths=[64], rowHeights=[2.2])
    rule.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), SANS),
                              ('BACKGROUND', (0,0), (-1,-1), ACCENT)]))
    rule.hAlign = 'LEFT'
    story.append(rule)
    story.append(Spacer(1, 14))
    fig = section.find('x:figure', NS)
    if fig is not None:
        f = section_fig(fig, TEXT_W * 0.8)
        if f:
            story.append(f)
            story.append(Spacer(1, 14))
    for sub in section:
        if not isinstance(sub.tag, str):
            continue
        tag = etree.QName(sub).localname
        cls_ = (sub.get('class') or '').split()
        if tag == 'div' and 'warmup' in cls_:
            warmup_flow(sub, story)
        elif tag == 'section' and 'chapter' in cls_:
            story.append(NextPageTemplate('main'))
            story.append(PageBreak())
            cnum = int(sub.get('data-chapter'))
            ch = sub.find('x:h2', NS)
            ck = text_of(ch.find('x:span[@class="chapter-kicker"]', NS))
            cn = text_of(ch.find('x:span[@class="chapter-name"]', NS))
            story.append(Paragraph(fallback(ck.upper()), S['chapkicker']))
            ct = Paragraph(fallback(cn), S['chaptitle'])
            ct._toc = (1, f'{ck} · {cn}')
            ct._tockey = f'unit-{unum}-chapter-{cnum}'
            story.append(ct)
            story.append(Spacer(1, 4))
            content_flowables(sub, story)
    return story

def para_mark(text, style):
    return Paragraph(fallback(text, SANS), style)

# ------------------------------------------------------------- frontmatter --
def fm_flowables(body, doc, toc):
    story = []
    for section in body:
        part = section.get('data-part')
        cls_ = section.get('class') or ''
        if part == 'half-title':
            story.append(NextPageTemplate('fm'))
            story.append(PageBreak())
            story.append(Spacer(1, PAGE_H * 0.36))
            story.append(para(section.find('x:h1', NS), S['halftitle']))
        elif part == 'title-page':
            story.append(PageBreak())
            story.append(Spacer(1, PAGE_H * 0.30))
            story.append(para(section.find('x:h1', NS), S['booktitle']))
            story.append(Spacer(1, 26))
            story.append(para(section.find('x:p', NS), S['author']))
        elif part == 'copyright':
            story.append(PageBreak())
            story.append(Spacer(1, PAGE_H - M_TOP - M_BOT - 110))
            for p in Q(section, './x:p'):
                story.append(para(p, S['copyright']))
        elif part == 'foreword':
            story.append(PageBreak())
            for el in section:
                tag = etree.QName(el).localname
                kcls = el.get('class') or ''
                if tag == 'h1':
                    h = para(el, S['fmhead'])
                    h._toc = (0, 'Foreword')
                    h._tockey = 'fm-foreword'
                    story.append(h)
                elif kcls == 'lead-in':
                    story.append(para(el, S['mediatitle']))
                elif kcls == 'signature':
                    story.append(para(el, S['signature']))
                elif kcls == 'signature-date':
                    story.append(para(el, S['signdate']))
                elif tag == 'p':
                    story.append(para(el, S['body']))
        elif part == 'how-to-use':
            story.append(PageBreak())
            for el in section:
                tag = etree.QName(el).localname
                kcls = el.get('class') or ''
                if tag == 'h1':
                    h = para(el, S['fmhead'])
                    h._toc = (0, 'How to Use This Book')
                    h._tockey = 'fm-howto'
                    story.append(h)
                elif tag == 'h2':
                    story.append(para(el, S['fmsub']))
                elif kcls == 'media-title':
                    story.append(para(el, S['mediatitle']))
                elif tag == 'div':
                    for sub in el:
                        stag = etree.QName(sub).localname
                        if stag == 'h3':
                            story.append(para(sub, S['fmsub2']))
                        elif stag == 'p':
                            story.append(para(sub, S['instr']))
                        elif stag == 'ul':
                            story.extend(build_list(sub))
                elif tag == 'ul':
                    story.extend(build_list(el))
                elif tag == 'p':
                    story.append(para(el, S['body']))
        elif part == 'epigraph':
            story.append(PageBreak())
            story.append(Spacer(1, PAGE_H * 0.30))
            story.append(para(section.find('x:blockquote/x:p', NS), S['epigraph']))
        elif part == 'contents':
            story.append(PageBreak())
            story.append(Paragraph('Contents', S['tochead']))
            story.append(toc)
    return story

# ------------------------------------------------------------------ build ---
def main():
    register_fonts()
    rl_config.canvas_basefontname = SANS   # avoid unembedded Helvetica resource
    build_styles()
    tree = etree.parse(MASTER)
    body = tree.getroot().find('x:body', NS)

    sections = list(body)
    # find insertion point: after epigraph, before first unit
    idx_epi = next((i for i, s in enumerate(sections)
                    if s.get('data-part') == 'epigraph'), len(sections)-1)
    fm_sections = sections[:idx_epi+1]
    unit_sections = [s for s in sections if s.get('class') == 'unit']

    # --- recto forcing: rebuild from scratch until every unit opener is recto
    extra_breaks = set()          # unit numbers needing a preceding page break
    for attempt in range(8):
        doc = BookDoc(OUT, pagesize=(PAGE_W, PAGE_H),
                      leftMargin=M_IN, rightMargin=M_OUT,
                      topMargin=M_TOP, bottomMargin=M_BOT,
                      title='Master Speaking', author='Abdul Raziq Nazari')
        frame = Frame(M_IN, M_BOT, TEXT_W, PAGE_H - M_TOP - M_BOT, id='main',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        doc.addPageTemplates([
            PageTemplate(id='fm', frames=[frame], onPage=on_page_fm),
            PageTemplate(id='main', frames=[frame], onPage=on_page_v),
            PageTemplate(id='opener', frames=[frame], onPage=on_page_opener),
        ])
        toc = TableOfContents()
        toc.levelStyles = [S['toc0'], S['toc1']]
        from reportlab.lib import colors as _c
        toc.tableStyle = TableStyle([('FONTNAME', (0,0), (-1,-1), SANS),
                                     ('VALIGN', (0,0), (-1,-1), 'TOP'),
                                     ('LEFTPADDING', (0,0), (-1,-1), 0),
                                     ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                     ('TOPPADDING', (0,0), (-1,-1), 0),
                                     ('BOTTOMPADDING', (0,0), (-1,-1), 0)])
        toc.dotsMinLevel = 1
        toc.formatter = lambda page: folio_for(page, doc.main_start)

        story = fm_flowables(fm_sections, doc, toc)
        story.append(PageBreak())
        story.append(Paragraph('Contents', S['tochead']))
        story.append(toc)
        for j, us in enumerate(unit_sections):
            unum = int(us.get('data-unit'))
            if unum in extra_breaks:
                story.append(PageBreak())
            story += unit_flowables(us, doc, first_unit=(j == 0))
        doc.multiBuild(story)
        bad = sorted((pg, int(k.split('-')[1])) for k, pg in doc.unit_pages.items()
                     if pg % 2 == 0)
        if not bad:
            break
        extra_breaks.add(bad[0][1])
    else:
        raise SystemExit('recto forcing did not converge')
    print('PDF written:', OUT, '| unit pages:', sorted(doc.unit_pages.items()))

if __name__ == '__main__':
    main()

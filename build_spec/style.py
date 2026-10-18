# -*- coding: utf-8 -*-
"""TOEFL HOUSE design system for 'Grammar for Special Speaking'.
Restrained palette, clear hierarchy, print-friendly. Design spec: section 13."""
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---- palette (restrained: navy + teal + gold accents, greys) ----
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
TEAL = RGBColor(0x0E, 0x6B, 0x6B)
GOLD = RGBColor(0x8A, 0x62, 0x00)
INK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x55, 0x55, 0x55)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FILL_NAVY = "1F3A5F"
FILL_TEAL = "0E6B6B"
FILL_BOX_TEAL = "EAF4F4"     # speaking / practice boxes
FILL_BOX_GREY = "F3F4F6"     # formula boxes
FILL_BOX_GOLD = "FBF3E2"     # warnings / advanced boxes
FILL_LINE = "D9DDE3"

BODY_FONT = "Calibri"
HEAD_FONT = "Calibri"
CODE_FONT = "Consolas"

PAGE_W = Inches(6.3)  # usable width with 0.9" margins on 8.27" A4


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def cell_margins(cell, top=60, bottom=60, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement('w:tcMar')
    for tag, v in (('top', top), ('start', left), ('bottom', bottom), ('end', right)):
        e = OxmlElement(f'w:{tag}')
        e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa')
        mar.append(e)
    tcPr.append(mar)


def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    e = OxmlElement('w:tblHeader'); e.set(qn('w:val'), 'true')
    trPr.append(e)


def run(p, text, size=11, bold=False, italic=False, color=INK,
        font=BODY_FONT, caps=False):
    r = p.add_run(text)
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    r.font.all_caps = caps
    return r


def para(doc_or_cell, text="", size=11, bold=False, italic=False, color=INK,
         align=None, space_before=2, space_after=2, indent=None, font=BODY_FONT):
    p = doc_or_cell.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if indent:
        p.paragraph_format.left_indent = Inches(indent)
    if align == 'c':
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if text:
        run(p, text, size=size, bold=bold, italic=italic, color=color, font=font)
    return p


def h_banner(doc, text, sub=None, fill=FILL_NAVY):
    """Full-width colored banner (part / lesson headers)."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    shade(c, fill); cell_margins(c, 90, 90, 140, 140)
    p = c.paragraphs[0]
    run(p, text, size=13, bold=True, color=WHITE, font=HEAD_FONT)
    if sub:
        p2 = c.add_paragraph()
        run(p2, sub, size=9.5, color=WHITE, font=HEAD_FONT)
    spacer(doc, 4)
    return t


def section_label(doc, text):
    """One of the 8 standard lesson parts."""
    t = doc.add_table(rows=1, cols=1)
    c = t.rows[0].cells[0]
    shade(c, FILL_TEAL); cell_margins(c, 50, 50, 120, 120)
    p = c.paragraphs[0]
    run(p, text, size=10.5, bold=True, color=WHITE, font=HEAD_FONT, caps=True)
    spacer(doc, 3)
    return t


def box(doc, label, lines, fill=FILL_BOX_GREY, label_color=GOLD, formula=False):
    """Standard content box: formula / warning / speaking etc."""
    t = doc.add_table(rows=1, cols=1)
    try:
        t.style = 'Table Grid'
    except Exception:
        pass
    c = t.rows[0].cells[0]
    shade(c, fill); cell_margins(c)
    first = True
    if label:
        p = c.paragraphs[0]
        run(p, label, size=9.5, bold=True, color=label_color, font=HEAD_FONT, caps=True)
        first = False
    for item in lines:
        if isinstance(item, tuple):
            txt, bold = item[0], item[1]
        else:
            txt, bold = item, False
        if first:
            p = c.paragraphs[0]; first = False
        else:
            p = c.add_paragraph()
        p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
        run(p, txt, size=10.5 if not formula else 11, bold=bold,
            font=CODE_FONT if formula else BODY_FONT,
            color=NAVY if bold else INK)
    spacer(doc, 3)
    return t


def table(doc, headers, rows, widths=None, header_fill=FILL_NAVY,
          zebra=True, font_size=10):
    # defensive: align header count with row width
    width = max([len(headers)] + [len(r) for r in rows]) if rows else len(headers)
    if len(headers) != width:
        print(f"[style.table] header/row mismatch: headers={len(headers)} rows={[len(r) for r in rows][:3]} -> normalising to {width} cols")
        headers = list(headers) + [""] * (width - len(headers))
    t = doc.add_table(rows=1, cols=len(headers))
    try:
        t.style = 'Table Grid'
    except Exception:
        pass
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0]
    set_repeat_header(hdr)
    for i, h in enumerate(headers):
        c = hdr.cells[i]
        shade(c, header_fill); cell_margins(c, 40, 40, 90, 90)
        p = c.paragraphs[0]
        run(p, h, size=font_size, bold=True, color=WHITE, font=HEAD_FONT)
    for ri, r in enumerate(rows):
        r = list(r) + [""] * (width - len(r))
        cells = t.add_row().cells
        for i, val in enumerate(r):
            c = cells[i]
            if zebra and ri % 2 == 1:
                shade(c, "F7F8FA")
            cell_margins(c, 40, 40, 90, 90)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            bold = isinstance(val, tuple)
            txt = val[0] if bold else val
            run(p, txt, size=font_size, bold=bold,
                color=NAVY if bold else INK)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows:
                row.cells[i].width = Inches(w)
    spacer(doc, 4)
    return t

def spacer(doc, pts=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run()
    r.font.size = Pt(pts)
    return p


def page_break(doc):
    from docx.enum.text import WD_BREAK
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run().add_break(WD_BREAK.PAGE)


def setup_doc():
    from docx import Document
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = BODY_FONT
    st.font.size = Pt(11)
    st.font.color.rgb = INK
    st.paragraph_format.space_after = Pt(3)
    st.paragraph_format.space_before = Pt(2)
    st.paragraph_format.line_spacing = 1.08
    for s in doc.sections:
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        # footer
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run(fp, "TOEFL HOUSE  |  Grammar for Special Speaking",
            size=8.5, color=GREY)
    return doc

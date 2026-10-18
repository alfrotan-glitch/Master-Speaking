#!/usr/bin/env python3
"""Build print PDF and reflowable EPUB from the generated, authoritative DOCX.
Run after build_spec/build.py and tools/build_html.py, or use --all to rebuild all outputs.
Builds both the Student Book and the Teacher's Book.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml.ns import qn
from ebooklib import epub
from lxml import etree, html as lxml_html
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, PageBreak, Paragraph, Spacer,
    Table, LongTable, TableStyle, PageTemplate, NextPageTemplate,
)

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Grammar for Special Speaking (TOEFL House)"
TEACHER_TITLE = "Grammar for Special Speaking — Teacher's Book (TOEFL House)"
TITLES = [TITLE, TEACHER_TITLE]
SOURCE_DOCX = ROOT / f"{TITLE}.docx"
TEACHER_DOCX = ROOT / f"{TEACHER_TITLE}.docx"
DIST = ROOT / "dist"
PDF_OUT = DIST / f"{TITLE}.pdf"
EPUB_OUT = DIST / f"{TITLE}.epub"
HTML_IN = DIST / f"{TITLE}.html"
TEACHER_PDF = DIST / f"{TEACHER_TITLE}.pdf"
TEACHER_EPUB = DIST / f"{TEACHER_TITLE}.epub"
TEACHER_HTML = DIST / f"{TEACHER_TITLE}.html"
NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#0E6B6B")
INK = colors.HexColor("#1A1A1A")
GREY = colors.HexColor("#555555")
PALE = colors.HexColor("#F3F4F6")
PALE_TEAL = colors.HexColor("#EAF4F4")
PALE_GOLD = colors.HexColor("#FBF3E2")


def paragraph_html(p):
    """Convert Word runs to safe, searchable ReportLab paragraph markup."""
    out = []
    for r in p.runs:
        text = escape(r.text).replace("\n", "<br/>").replace("\t", "    ")
        if not text:
            continue
        if r.bold:
            text = f"<b>{text}</b>"
        if r.italic:
            text = f"<i>{text}</i>"
        color = getattr(r.font.color, "rgb", None)
        if color:
            text = f'<font color="#{color}">{text}</font>'
        out.append(text)
    if not out and p.text:
        return escape(p.text).replace("\n", "<br/>")
    return "".join(out)


def shade_color(cell, default=None):
    shd = cell._tc.tcPr.find(qn("w:shd"))
    if shd is None:
        return default
    value = shd.get(qn("w:fill"))
    if not value or value in ("auto", "FFFFFF"):
        return default
    try:
        return colors.HexColor("#" + value)
    except Exception:
        return default


class TaggedParagraph(Paragraph):
    """A heading that adds a PDF bookmark and a clickable, numbered TOC entry."""
    def __init__(self, text, style, title, key, level=0):
        super().__init__(text, style)
        self.book_title, self.book_key, self.book_level = title, key, level

    def draw(self):
        super().draw()
        canvas = self.canv
        canvas.bookmarkPage(self.book_key)
        canvas.addOutlineEntry(self.book_title, self.book_key, level=self.book_level, closed=False)
        template = getattr(canvas, "_doctemplate", None)
        if template is not None:
            template.notify("TOCEntry", (self.book_level, self.book_title, canvas.getPageNumber(), self.book_key))


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename, title):
        super().__init__(str(filename), pagesize=A4,
                         leftMargin=18*mm, rightMargin=18*mm,
                         topMargin=17*mm, bottomMargin=17*mm,
                         title=title, author="TOEFL HOUSE")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      id="normal", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="book", frames=frame, onPage=self._footer)])

    @staticmethod
    def _footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D9DDE3"))
        canvas.setLineWidth(0.4)
        canvas.line(doc.leftMargin, 12*mm, A4[0]-doc.rightMargin, 12*mm)
        canvas.setFont("BookSans", 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(doc.leftMargin, 8*mm, "TOEFL HOUSE  |  Grammar for Special Speaking")
        canvas.drawRightString(A4[0]-doc.rightMargin, 8*mm, str(doc.page))
        canvas.restoreState()


def pdf_styles():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    fontdir = Path("/usr/share/fonts/truetype/dejavu")
    regular = fontdir / "DejaVuSans.ttf"
    bold = fontdir / "DejaVuSans-Bold.ttf"
    italic = fontdir / "DejaVuSans-Oblique.ttf"
    bolditalic = fontdir / "DejaVuSans-BoldOblique.ttf"
    mono = fontdir / "DejaVuSansMono.ttf"
    if not regular.exists() or not bold.exists() or not mono.exists():
        raise RuntimeError("DejaVu Sans fonts are required for the PDF build (install fonts-dejavu-core).")
    italic = italic if italic.exists() else regular
    bolditalic = bolditalic if bolditalic.exists() else bold
    for name, file in (("BookSans", regular), ("BookSans-Bold", bold),
                       ("BookSans-Italic", italic), ("BookSans-BoldItalic", bolditalic),
                       ("BookMono", mono)):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(file)))
    pdfmetrics.registerFontFamily("BookSans", normal="BookSans", bold="BookSans-Bold",
                                  italic="BookSans-Italic", boldItalic="BookSans-BoldItalic")
    return {
        "body": ParagraphStyle("BookBody", fontName="BookSans", fontSize=9.1, leading=12.2,
                                textColor=INK, spaceBefore=2, spaceAfter=3, splitLongWords=1),
        "small": ParagraphStyle("BookSmall", fontName="BookSans", fontSize=8, leading=10.2,
                                 textColor=INK, spaceAfter=2),
        "h1": ParagraphStyle("BookH1", fontName="BookSans-Bold", fontSize=13, leading=16,
                             textColor=NAVY, spaceBefore=7, spaceAfter=5, keepWithNext=True),
        "h2": ParagraphStyle("BookH2", fontName="BookSans-Bold", fontSize=10.5, leading=13,
                             textColor=TEAL, spaceBefore=5, spaceAfter=3, keepWithNext=True),
        "h3": ParagraphStyle("BookH3", fontName="BookSans-Bold", fontSize=10, leading=12,
                             textColor=NAVY, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        "toc": ParagraphStyle("TOCHead", fontName="BookSans-Bold", fontSize=19, leading=24,
                              textColor=NAVY, spaceAfter=10),
        "table": ParagraphStyle("BookTable", fontName="BookSans", fontSize=8.1, leading=10.1,
                                 textColor=INK, spaceAfter=0),
        "tablehead": ParagraphStyle("BookTableHead", fontName="BookSans-Bold", fontSize=8.1,
                                     leading=10.1, textColor=colors.white, spaceAfter=0),
        "toc_entry": ParagraphStyle("TOCEntry", fontName="BookSans", fontSize=9.2, leading=13,
                                     leftIndent=8, firstLineIndent=0, textColor=NAVY),
    }


def _is_page_break(paragraph):
    return any(br.get(qn("w:type")) == "page" for br in paragraph._p.iter(qn("w:br")))


def _is_major_heading(p):
    text = p.text.strip()
    if p.style.name.startswith("Heading 1"):
        return text
    if re.match(r"^(LESSON \d+\s+·|REVIEW TEST \d+|FINAL ASSESSMENT|APPENDIX \d+|INTRODUCTION|HOW TO USE THIS BOOK|CONTENTS|DIAGNOSTIC TEST|COURSE OVERVIEW|TEACHING PRINCIPLES|PACING AND FEEDBACK|ASSESSMENT GUIDANCE|COPYRIGHT)", text, re.I):
        return text
    return None


def _table_flowable(table, styles, doc_width):
    rows = []
    for ri, row in enumerate(table.rows):
        cells = []
        for cell in row.cells:
            ps = []
            for p in cell.paragraphs:
                text = paragraph_html(p)
                if not text:
                    continue
                style = styles["table"]
                major = _is_major_heading(p)
                if p.style.name.startswith("Heading 1"):
                    style = styles["h1"]
                elif p.style.name.startswith("Heading 2"):
                    style = styles["h2"]
                elif p.runs and any(r.bold for r in p.runs) and len(p.text) < 110:
                    style = styles["h3"]
                if major:
                    key = "pdf-" + re.sub(r"[^a-z0-9]+", "-", major.lower()).strip("-")
                    if re.match(r"^(LESSON|REVIEW TEST|FINAL ASSESSMENT|APPENDIX)", major, re.I):
                        ps.append(TaggedParagraph(text, style, major, key, 0))
                    else:
                        ps.append(Paragraph(text, style))
                else:
                    ps.append(Paragraph(text, style))
            cells.append(ps or [Paragraph(" ", styles["table"])])
        rows.append(cells)
    if not rows:
        return None
    cols = len(rows[0])
    widths = []
    try:
        widths = [float(table.columns[i].width) / 914400 * 72 for i in range(cols)]
    except Exception:
        widths = []
    if len(widths) != cols or sum(widths) <= 1:
        widths = [doc_width / cols] * cols
    scale = doc_width / sum(widths)
    widths = [w * scale for w in widths]
    if cols == 1:
        data = [[rows[0][0]] ]
        flow = LongTable(data, colWidths=widths, splitByRow=1, splitInRow=1, hAlign="LEFT")
        fill = shade_color(table.rows[0].cells[0], PALE)
        flow.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), fill or colors.white),
            ("BOX", (0, 0), (-1, -1), 0.35, colors.HexColor("#D9DDE3")),
            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        return flow
    data = []
    for ri, row in enumerate(rows):
        data.append([Table(cell, colWidths=[widths[i]-5], hAlign="LEFT") if len(cell) > 1
                     else cell[0] for i, cell in enumerate(row)])
    row_heights = [float(row.height) / 914400 * 72 if row.height else None for row in table.rows]
    flow = LongTable(data, colWidths=widths, rowHeights=row_heights,
                     repeatRows=1 if len(rows) > 1 else 0,
                     splitByRow=1, splitInRow=1, hAlign="LEFT")
    style_cmds = [
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C8CDD4")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ]
    for ri in range(2, len(rows), 2):
        style_cmds.append(("BACKGROUND", (0, ri), (-1, ri), colors.HexColor("#F7F8FA")))
    for i, cell in enumerate(table.rows[0].cells):
        fill = shade_color(cell)
        if fill:
            style_cmds.append(("BACKGROUND", (i, 0), (i, 0), fill))
    flow.setStyle(TableStyle(style_cmds))
    return flow


def _build_pdf_for(source_docx: Path, pdf_out: Path, title: str):
    if not source_docx.exists():
        raise FileNotFoundError(source_docx)
    styles = pdf_styles()
    doc = Document(source_docx)
    story = []
    toc_active = False
    toc_inserted = False
    contents_tables_skipped = False
    doc_width = A4[0] - 36*mm
    body = doc.element.body
    for child in body:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "p":
            from docx.text.paragraph import Paragraph as DocxParagraph
            p = DocxParagraph(child, doc)
            if _is_page_break(p):
                if toc_active:
                    toc_active = False
                story.append(PageBreak())
                continue
            text = paragraph_html(p)
            raw = p.text.strip()
            if toc_active and raw:
                continue
            if not raw:
                story.append(Spacer(1, 2))
                continue
            if p.style.name.startswith("Heading 2"):
                story.append(Paragraph(text, styles["h2"]))
            elif p.style.name.startswith("Heading 1"):
                story.append(Paragraph(text, styles["h1"]))
            else:
                story.append(Paragraph(text, styles["body"]))
        elif tag == "tbl":
            from docx.table import Table as DocxTable
            tbl = DocxTable(child, doc)
            first = next((p for c in tbl.rows[0].cells for p in c.paragraphs if p.text.strip()), None) if tbl.rows else None
            raw = first.text.strip() if first is not None else ""
            if raw.upper() == "CONTENTS":
                story.append(_table_flowable(tbl, styles, doc_width))
                story.append(Spacer(1, 10))
                story.append(Paragraph("Lessons, assessments and reference", styles["toc_head"] if "toc_head" in styles else styles["toc"]))
                from reportlab.platypus.tableofcontents import TableOfContents
                toc = TableOfContents()
                toc.levelStyles = [styles["toc_entry"]]
                toc.dotsMinLevel = 0
                story.append(toc)
                story.append(Spacer(1, 8))
                toc_active = True
                toc_inserted = True
                continue
            if toc_active and not contents_tables_skipped:
                contents_tables_skipped = True
                continue
            if toc_active and contents_tables_skipped:
                continue
            flow = _table_flowable(tbl, styles, doc_width)
            if flow is not None:
                story.append(flow)
                story.append(Spacer(1, 2))
    if not toc_inserted:
        raise RuntimeError(f"Could not locate the source contents banner for the PDF TOC in {source_docx.name}")
    DIST.mkdir(exist_ok=True)
    template = BookDocTemplate(pdf_out, title)
    template.multiBuild(story, maxPasses=5)
    return pdf_out


def build_pdf():
    return _build_pdf_for(SOURCE_DOCX, PDF_OUT, TITLE)


def build_teacher_pdf():
    return _build_pdf_for(TEACHER_DOCX, TEACHER_PDF, TEACHER_TITLE)


def _plain_text(node):
    return " ".join(" ".join(node.itertext()).split())


def _build_epub_for(html_path: Path, epub_path: Path, title: str, uuid: str):
    if not html_path.exists():
        raise FileNotFoundError(html_path)
    parser = lxml_html.HTMLParser(encoding="utf-8", recover=True)
    tree = lxml_html.parse(str(html_path), parser)
    body = tree.find(".//body")
    if body is None:
        raise RuntimeError("HTML source has no body")
    content_root = etree.Element("div")
    entries = []
    seen = set()
    seen_titles = set()
    in_static_contents = False
    for element in list(body):
        text = _plain_text(element)
        if not text:
            continue
        candidates = element.xpath("self::h1|self::h2|self::h3|.//h1|.//h2|.//h3|self::p|.//p")
        heading_node = next((n for n in candidates if _plain_text(n)), None)
        heading_text = _plain_text(heading_node) if heading_node is not None else ""
        if in_static_contents and heading_text.upper() != "DIAGNOSTIC TEST":
            continue
        if heading_text.upper() == "DIAGNOSTIC TEST":
            in_static_contents = False
        match = re.match(r"^(LESSON\s+\d+\s+·\s+.+|REVIEW TEST\s+\d+|FINAL ASSESSMENT(?:\s+—\s+PART\s+2)?|APPENDIX\s+\d+\s+.*|INTRODUCTION|HOW TO USE THIS BOOK|CONTENTS|DIAGNOSTIC TEST|COURSE OVERVIEW|TEACHING PRINCIPLES|PACING AND FEEDBACK|ASSESSMENT GUIDANCE|COPYRIGHT)", heading_text, re.I)
        if match and heading_text.casefold() not in seen_titles:
            seen_titles.add(heading_text.casefold())
            hid = "nav-" + re.sub(r"[^a-z0-9]+", "-", heading_text.lower()).strip("-")
            base, suffix = hid, 2
            while hid in seen:
                hid = f"{base}-{suffix}"; suffix += 1
            seen.add(hid)
            h = etree.Element("h1", id=hid)
            h.text = heading_text
            if heading_node is not None and heading_node.getparent() is not None:
                heading_node.getparent().replace(heading_node, h)
            else:
                element.insert(0, h)
            entries.append((heading_text, hid))
        content_root.append(element)
        if heading_text.upper() == "CONTENTS":
            in_static_contents = True
    css = """
    body { font-family: serif; line-height: 1.5; margin: 5%; color: #1a1a1a; }
    h1,h2,h3 { font-family: sans-serif; color: #1f3a5f; break-before: page; }
    h1 { font-size: 1.45em; } h2 { font-size: 1.15em; }
    table { width: 100%; border-collapse: collapse; margin: 0.8em 0; }
    td,th { border: 1px solid #c8cdd4; padding: 0.35em; vertical-align: top; }
    img { max-width: 100%; height: auto; }
    a { color: #0e6b6b; }
    """
    book = epub.EpubBook()
    book.set_identifier(uuid)
    book.set_title(title)
    book.set_language("en")
    book.add_author("TOEFL HOUSE")
    book.add_metadata("DC", "publisher", "TOEFL HOUSE")
    book.add_metadata("DC", "description", "A practical grammar course for accurate, natural, confident speech.")
    chapter = epub.EpubHtml(title="Complete book", file_name="book.xhtml", lang="en")
    chapter.content = (
        '<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">'
        '<head><title>' + escape(title) + '</title><link rel="stylesheet" type="text/css" href="style/book.css"/></head>'
        '<body>' + etree.tostring(content_root, encoding="unicode", method="html") + '</body></html>'
    )
    style = epub.EpubItem(uid="book-css", file_name="style/book.css", media_type="text/css", content=css.encode("utf-8"))
    book.add_item(style)
    book.add_item(chapter)
    book.toc = tuple(epub.Link(f"book.xhtml#{anchor}", title, f"toc-{i}") for i, (title, anchor) in enumerate(entries, 1))
    book.spine = ["nav", chapter]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    DIST.mkdir(exist_ok=True)
    epub.write_epub(str(epub_path), book, {})
    return epub_path


def build_epub():
    return _build_epub_for(HTML_IN, EPUB_OUT, TITLE, "urn:uuid:3c0c1cc0-4920-4e6a-9302-16eac22f77b6")


def build_teacher_epub():
    return _build_epub_for(TEACHER_HTML, TEACHER_EPUB, TEACHER_TITLE, "urn:uuid:9e1a2c3d-7b1f-4e6a-9302-teacher-book-01")


def verify_epub(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB mimetype must be the first ZIP member")
        if z.read("mimetype") != b"application/epub+zip":
            raise RuntimeError("Incorrect EPUB mimetype")
        required = {"META-INF/container.xml", "EPUB/content.opf", "EPUB/nav.xhtml", "EPUB/book.xhtml", "EPUB/style/book.css"}
        missing = required - set(names)
        if missing:
            raise RuntimeError(f"EPUB package is missing {sorted(missing)}")
        parser = etree.XMLParser(resolve_entities=False, no_network=True)
        for name in names:
            if name.endswith((".xhtml", ".opf", ".ncx", ".xml")):
                etree.fromstring(z.read(name), parser)
        xhtml = z.read("EPUB/book.xhtml").decode("utf-8")
        # Student book vs teacher book: check appropriate tokens
        if "Teacher" in str(path):
            for token in ("LESSON 16", "TEACHER GUIDE", "ASSESSMENT GUIDANCE"):
                if token not in xhtml:
                    raise RuntimeError(f"EPUB content check failed: {token} missing in {path.name}")
        else:
            for token in ("LESSON 16", "FINAL ASSESSMENT", "APPENDIX 5", "REVIEW TEST 3"):
                if token not in xhtml:
                    raise RuntimeError(f"EPUB content check failed: {token}")
            if xhtml.count("LESSON ") < 16:
                raise RuntimeError("EPUB has fewer than 16 lessons")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="rebuild DOCX and HTML before PDF/EPUB")
    args = parser.parse_args()
    if args.all:
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "build_spec" / "build.py")], check=True)
        subprocess.run([sys.executable, str(ROOT / "build_spec" / "build_teacher.py")], check=True)
        DIST.mkdir(exist_ok=True)
        shutil.copy2(SOURCE_DOCX, DIST / SOURCE_DOCX.name)
        shutil.copy2(TEACHER_DOCX, DIST / TEACHER_DOCX.name)
        subprocess.run([sys.executable, str(ROOT / "tools" / "build_html.py")], check=True)
    pdf = build_pdf()
    epub_path = build_epub()
    verify_epub(epub_path)
    print(f"PDF:   {pdf.relative_to(ROOT)} ({pdf.stat().st_size:,} bytes)")
    print(f"EPUB:  {epub_path.relative_to(ROOT)} ({epub_path.stat().st_size:,} bytes; package/XML checks passed)")
    # Teacher book — only if DOCX exists
    if TEACHER_DOCX.exists() and TEACHER_HTML.exists():
        tpdf = build_teacher_pdf()
        tepub = build_teacher_epub()
        verify_epub(tepub)
        print(f"Teacher PDF:  {tpdf.relative_to(ROOT)} ({tpdf.stat().st_size:,} bytes)")
        print(f"Teacher EPUB: {tepub.relative_to(ROOT)} ({tepub.stat().st_size:,} bytes; package/XML checks passed)")
    elif TEACHER_DOCX.exists():
        print(f"NOTE: Teacher HTML not found at {TEACHER_HTML.name} — skipping teacher EPUB (run build_html first)")

if __name__ == "__main__":
    main()

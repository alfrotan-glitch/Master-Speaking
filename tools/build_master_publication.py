#!/usr/bin/env python3
"""Reproducible PROOF exports of the independent Master Speaking.docx.

The original is never overwritten. These outputs require editorial, image-rights,
screen-reader, EPUB navigation, and visual print inspection before final release.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

import pymupdf
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from ebooklib import epub
from lxml import etree
from docx.oxml.ns import qn


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Master Speaking.docx"
PROOF = ROOT / "proof"
TITLE = "Master Speaking (TOEFL House)"
WORKING = PROOF / f"{TITLE}.docx"
PDF = PROOF / f"{TITLE}.pdf"
EPUB = PROOF / f"{TITLE}.epub"
HTML = PROOF / f"{TITLE}.html"
REPORT = ROOT / "docs" / "master-speaking-publication-audit.md"
CSS = ROOT / "build_master" / "book.css"


def run(*args):
    print("COMMAND:", " ".join(map(str, args)), flush=True)
    subprocess.run([str(x) for x in args], cwd=ROOT, check=True, timeout=900)


def words(s):
    return len(re.findall(r"\b[\w'-]+\b", s))



# Curated *content* headings, not the reusable exercise labels that currently
# account for hundreds of meaningless DOCX outline entries.
NAV_TOPICS = [
    "The Power of Communication",
    "Are You a Good Listener?",
    "The Importance of Communication",
    "Dreams Become Reality through Goals",
    "The Power of Emotional Intelligence",
    "Can Money Buy Happiness?",
    "Living with AI: Friend or Foe?",
    "Job Creator or Job Destroyer?",
    "Is Love Enough?",
    "The World Is Getting Smaller",
    "Globalization: Opportunity or Threat?",
    "English: From a Local Language to a Global Lingua Franca",
]


def _norm_nav(text):
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def _match_topic(title):
    phrase = _norm_nav(title)
    for topic in NAV_TOPICS:
        if _norm_nav(topic) == phrase or (
                _norm_nav(topic) in phrase and len(phrase) <= len(_norm_nav(topic)) + 7):
            return topic
    return None


def _curate_pdf_bookmarks():
    with pymupdf.open(PDF) as pdf:
        selected = []
        already = set()
        for level, title, page, *rest in pdf.get_toc():
            topic = _match_topic(title)
            if topic and topic not in already:
                selected.append([1, topic, page])
                already.add(topic)
        if len(selected) < 6:
            raise AssertionError(f"Could not identify enough meaningful PDF topics: {selected}")
        pdf.set_toc(selected)
        newpdf = PDF.with_name(PDF.stem + ".optimized.pdf")
        pdf.save(newpdf, garbage=4, deflate=True)
    newpdf.replace(PDF)
    return selected


def _curate_epub_navigation():
    with zipfile.ZipFile(EPUB) as zin:
        names = zin.namelist()
        nav_name = next((n for n in names if n.endswith("nav.xhtml")), None)
        if not nav_name:
            raise AssertionError("EPUB lacks a navigation XHTML file")
        parser = etree.XMLParser(resolve_entities=False, no_network=True)
        navtree = etree.fromstring(zin.read(nav_name), parser)
        navs = navtree.xpath("//*[local-name()='nav']")
        nav = next((n for n in navs if n.get("{http://www.idpf.org/2007/ops}type") == "toc"), None)
        if nav is None and navs:
            nav = navs[0]
        if nav is None:
            raise AssertionError("EPUB navigation has no toc section")
        candidates = []
        seen = set()
        for anchor in nav.xpath(".//*[local-name()='a']"):
            topic = _match_topic(" ".join(anchor.itertext()))
            href = anchor.get("href")
            if topic and href and topic not in seen:
                candidates.append((topic, href))
                seen.add(topic)
        if len(candidates) < 6:
            raise AssertionError(f"EPUB lacks usable topic anchors: {candidates}")
        lists = nav.xpath(".//*[local-name()='ol']")
        if not lists:
            raise AssertionError("EPUB navigation has no ordered list")
        ol = lists[0]
        for child in list(ol):
            ol.remove(child)
        XHTML = "{http://www.w3.org/1999/xhtml}"
        for topic, href in candidates:
            li = etree.SubElement(ol, XHTML + "li")
            a = etree.SubElement(li, XHTML + "a", href=href)
            a.text = topic
        modified = {nav_name: etree.tostring(navtree, encoding="utf-8", xml_declaration=True)}
        ncx_name = next((n for n in names if n.endswith(".ncx")), None)
        if ncx_name:
            ncxroot = etree.fromstring(zin.read(ncx_name), parser)
            maps = ncxroot.xpath("//*[local-name()='navMap']")
            if maps:
                navmap = maps[0]
                for child in list(navmap):
                    navmap.remove(child)
                NCX = "{http://www.daisy.org/z3986/2005/ncx/}"
                for i, (topic, href) in enumerate(candidates, 1):
                    point = etree.SubElement(navmap, NCX + "navPoint", id=f"nav-{i}", playOrder=str(i))
                    label = etree.SubElement(point, NCX + "navLabel")
                    etree.SubElement(label, NCX + "text").text = topic
                    etree.SubElement(point, NCX + "content", src=href)
                modified[ncx_name] = etree.tostring(ncxroot, encoding="utf-8", xml_declaration=True)
        tmp = EPUB.with_name(EPUB.stem + ".optimized.epub")
        with zipfile.ZipFile(tmp, "w") as zout:
            for info in zin.infolist():
                zout.writestr(info, modified.get(info.filename, zin.read(info.filename)))
    tmp.replace(EPUB)
    return candidates


# Structured hierarchy for the *working proof only*. The original file stays
# unchanged. An exercise prompt must not be marked up as a chapter heading.
SECTION_HEADINGS = {
    "vocabulary preview", "vocabulary check", "critical thinking",
    "speaking through reading", "think pair share", "before listening",
    "listening strategy", "listening comprehension", "homework",
    "speaking toolbox", "vocabulary activation", "guided discussion",
    "speaking challenge", "pronunciation clinic", "presentation toolbox",
    "research task", "organizing your presentation", "group discussion",
    "mini debate", "reading comprehension",
}



def _recover_textbox_alternatives(document):
    """Use already-visible textbox text for drawing accessibility, never guesses.

    The source contains textbox drawings with missing alt metadata. Extract
    text from the actual drawing subtree only; leave genuinely image-only
    drawings unresolved for an editor who can see them.
    """
    changes={"derived_from_text": 0, "unresolved": 0, "already_present": 0}
    for drawing in document.element.body.iter(qn("wp:docPr")):
        if drawing.get("descr") or drawing.get("title"):
            changes["already_present"] += 1
            continue
        parent=drawing.getparent()
        while parent is not None and parent.tag not in (
                qn("wp:anchor"), qn("wp:inline"), qn("w:drawing")):
            parent=parent.getparent()
        if parent is None:
            changes["unresolved"] += 1
            continue
        # w:txbxContent is the existing Word textbox, not a new description.
        texts=[]
        for field in parent.iter():
            if field.tag==qn("w:t") and field.text:
                texts.append(field.text.strip())
        visible=" ".join(text for text in texts if text)
        visible=re.sub(r"\s+"," ",visible).strip()
        if visible:
            label="Text panel: " + visible
            drawing.set("descr", label[:220])
            changes["derived_from_text"]+=1
        else:
            changes["unresolved"]+=1
    return changes


def _normalise_proof_heading_hierarchy(document):
    """Retain the existing visible typography, correct semantic outline levels.

    Styles derived from original headings inherit their appearance, but explicitly
    set outlineLvl=9 so exercise questions never appear in Word's Navigation pane.
    """
    derived = {}
    changes = {"topic_headings": 0, "section_headings": 0,
               "demoted_prompts": 0}
    paras = list(document.paragraphs)
    for tab in document.tables:
        for row in tab.rows:
            for cell in row.cells:
                paras.extend(cell.paragraphs)
    for p in paras:
        if not p.text.strip() or not p.style:
            continue
        original_style = p.style.name
        if not re.match(r"^Heading [123]$", original_style):
            continue
        topic = _match_topic(p.text)
        section = _norm_nav(p.text) in SECTION_HEADINGS
        if topic:
            p.style = document.styles["Heading 1"]
            changes["topic_headings"] += 1
        elif section:
            p.style = document.styles["Heading 2"]
            changes["section_headings"] += 1
        else:
            if original_style not in derived:
                label = "Speaking Exercise Label " + original_style[-1]
                st = document.styles[label] if label in document.styles else document.styles.add_style(label, WD_STYLE_TYPE.PARAGRAPH)
                st.base_style = document.styles[original_style]
                ppr = st.element.get_or_add_pPr()
                outline = ppr.find(qn("w:outlineLvl"))
                if outline is None:
                    outline = OxmlElement("w:outlineLvl")
                    ppr.append(outline)
                outline.set(qn("w:val"), "9")
                derived[original_style] = st
            p.style = derived[original_style]
            changes["demoted_prompts"] += 1
    if changes["topic_headings"] < 10 or changes["demoted_prompts"] < 50:
        raise AssertionError(f"Unexpected heading classification: {changes}")
    return changes


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(SOURCE)
    for command in ("libreoffice", "pandoc"):
        if not shutil.which(command):
            raise RuntimeError(f"Required publisher {command} is not installed")
    PROOF.mkdir(exist_ok=True)

    original = Document(SOURCE)
    source_text = "\n".join(p.text for p in original.paragraphs)
    source_text += "\n" + "\n".join(c.text for t in original.tables for r in t.rows for c in r.cells)
    source_words = words(source_text)
    source_media = 0
    with zipfile.ZipFile(SOURCE) as zin:
        source_media = sum(p.startswith("word/media/") for p in zin.namelist())

    # Update safe, factual metadata; retain the entire original manuscript's
    # paragraphs, embedded images, tables, sections, and typography.
    original.core_properties.title = "Master Speaking"
    original.core_properties.author = "TOEFL HOUSE"
    original.core_properties.subject = "English speaking coursebook"
    original.core_properties.keywords = "speaking, communication, TOEFL HOUSE"
    heading_fixes = _normalise_proof_heading_hierarchy(original)
    alt_recovery = _recover_textbox_alternatives(original)
    original.save(WORKING)

    profile = "file:///tmp/libreoffice-master-speaking-proof"
    run("libreoffice", f"-env:UserInstallation={profile}", "--headless",
        "--convert-to", "pdf:writer_pdf_Export", "--outdir", PROOF, WORKING)
    if not PDF.is_file() or PDF.stat().st_size == 0:
        raise RuntimeError("LibreOffice failed to produce the proof PDF")

    run("pandoc", WORKING, "--from=docx", "--to=epub3", "--standalone",
        "--toc", "--toc-depth=3", "--css", CSS,
        "--metadata=title:Master Speaking", "--metadata=author:TOEFL HOUSE",
        "--metadata=lang:en", "-o", EPUB)
    run("pandoc", WORKING, "--from=docx", "--to=html5", "--standalone",
        "--self-contained", "--metadata=title:Master Speaking",
        "--metadata=lang:en", "-o", HTML)

    curated_pdf = _curate_pdf_bookmarks()
    curated_epub = _curate_epub_navigation()

    with pymupdf.open(PDF) as pdf:
        pdf_pages = pdf.page_count
        pdf_text = "\n".join(page.get_text() for page in pdf)
        a4_pages = sum(abs(p.rect.width - 595.28) < 3 and
                       abs(p.rect.height - 841.89) < 3 for p in pdf)
        pdf_bookmarks = len(pdf.get_toc())
    pdf_words = words(pdf_text)

    # Word's Navigation pane should show true topic/section headings,
    # never hundreds of question and exercise text headings.
    inspect = Document(WORKING)
    named = [(p.style.name, p.text.strip()) for p in inspect.paragraphs
             if p.text.strip() and p.style.name.startswith("Heading ")]
    if sum(k == "Heading 1" for k, _ in named) < 10:
        raise AssertionError("Working DOCX lost topical Heading 1 entries")
    if any(k.startswith("Heading") and
           ("multiple choice" in s.casefold() or s.startswith("_____"))
           for k, s in named):
        raise AssertionError("Exercise text still appears as Word navigation headings")

    with zipfile.ZipFile(EPUB) as archive:
        names = archive.namelist()
        if names[0] != "mimetype" or archive.read("mimetype") != b"application/epub+zip":
            raise AssertionError("EPUB's first ZIP member must be the uncompressed EPUB MIME file")
        parser = etree.XMLParser(resolve_entities=False, no_network=True)
        container = etree.fromstring(archive.read("META-INF/container.xml"), parser)
        opf_name = container.xpath("string(//*[local-name()='rootfile']/@full-path)")
        if opf_name not in names:
            raise AssertionError("EPUB has no package file")
        package = etree.fromstring(archive.read(opf_name), parser)
        for item in package.xpath("//*[local-name()='manifest']/*[local-name()='item']"):
            target = str(Path(opf_name).parent / item.get("href"))
            if target not in names:
                raise AssertionError(f"EPUB manifest resource not found: {target}")
        if not package.xpath("//*[local-name()='spine']/*[local-name()='itemref']"):
            raise AssertionError("EPUB spine is empty")
        xhtml_files = [x for x in names if x.endswith(".xhtml") and "nav." not in x]
        eptext = []
        for name in xhtml_files:
            elem = etree.fromstring(archive.read(name), parser)
            eptext.extend(elem.itertext())
        epub_words = words(" ".join(eptext))

    ebook = epub.read_epub(str(EPUB), options={"ignore_ncx": False})
    epub_images = sum(1 for item in ebook.get_items()
                      if item.media_type.startswith("image/"))
    if source_words < 5000 or pdf_pages < 20 or epub_words < source_words * 0.60:
        raise AssertionError("Publication proof is incomplete: unexpected text or page loss")
    if a4_pages != pdf_pages:
        raise AssertionError(f"Unexpected non-A4 PDF pages: {pdf_pages-a4_pages}")
    if HTML.stat().st_size < 20_000:
        raise AssertionError("Generated HTML unusually small")

    report = {
        "source_words_estimate": source_words,
        "working_proof_heading_hierarchy": heading_fixes,
        "text_box_accessibility_recovery": alt_recovery,
        "pdf_extracted_words": pdf_words,
        "epub_extracted_words": epub_words,
        "pdf_pages": pdf_pages,
        "pdf_a4_pages": a4_pages,
        "pdf_bookmarks": pdf_bookmarks,
        "curated_pdf_topics": [v[1] for v in curated_pdf],
        "curated_epub_topics": [v[0] for v in curated_epub],
        "source_media_files": source_media,
        "epub_embedded_images": epub_images,
        "source_graphic_properties": sum(1 for _ in original.element.body.iter(qn("wp:docPr"))),
        "proof_files": {p.name: p.stat().st_size for p in (WORKING, PDF, EPUB, HTML)},
    }
    # Human-readable heading inventory makes false chapter navigation visible.
    # Headings used for exercise labels should not become top-level ebook chapters.
    from collections import Counter
    heading_inventory = Counter(
        (p.style.name, p.text.strip()) for p in original.paragraphs
        if p.text.strip() and p.style is not None
        and p.style.name in ("Heading 1", "Heading 2")
    )
    outline_report = ROOT / "docs" / "master-speaking-heading-inventory.md"
    lines = [
        "# Master Speaking — heading/navigation audit",
        "",
        "Generated from the independent original Word document; headings may be",
        "exercise labels rather than genuine chapter titles. Do not treat each as",
        "an EPUB chapter or PDF bookmark without editorial review.",
        "",
        "| Word style | Heading text | Repetitions |",
        "|---|---|---:|",
    ]
    for (style_name, heading), count in heading_inventory.items():
        display = heading.replace("|", "/").replace("\n", " ").strip()[:110]
        lines.append(f"| {style_name} | {display} | {count} |")
    outline_report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    report["distinct_heading_1_2_labels"] = len(heading_inventory)
    REPORT.write_text(
        "# Master Speaking — publication proof audit\n\n"
        "> PROOF BUILDS ONLY. This report establishes structural conversion checks, "
        "not an editorial signoff, perfect image parity, accessible EPUB, third-party "
        "image rights, a qualified teaching review, or a print-ready release.\n\n"
        + "\n".join(f"- **{k.replace('_', ' ')}:** {v}" for k, v in report.items()) + "\n\n"
        "The original Master Speaking.docx is preserved unchanged. "
        "Review all pages, graphics, exercise keys, media links, navigation and EPUB "
        "rendition on real devices before approving a release.\n",
        encoding="utf-8")
    print("MASTER_PUBLICATION_REPORT=" + json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

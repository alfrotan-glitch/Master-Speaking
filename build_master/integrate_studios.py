"""Integrate the eight original speaking studios into their manuscript units.

The source file Master Speaking.docx stays untouched. Each studio is inserted
at the end of the corresponding unit, not as disconnected bonus pages.
"""
from __future__ import annotations

import re
from collections import defaultdict
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from speaking_studios import UNITS

NAVY=RGBColor(27,52,76)
TEAL=RGBColor(13,105,110)
INK=RGBColor(38,49,61)


def _style(doc,name,base,size,bold=False,color=INK,space=5):
    if name in doc.styles:
        return doc.styles[name]
    style=doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
    style.base_style=doc.styles[base]
    style.font.name="Aptos"
    style.font.size=Pt(size)
    style.font.bold=bold
    style.font.color.rgb=color
    style.paragraph_format.space_before=Pt(space)
    style.paragraph_format.space_after=Pt(5)
    return style



ORIGINAL_UNIT_HEADINGS=[
    "THE POWER OF COMMUNICATION",
    "THE ART OF GOAL SETTING",
    "EMOTIONAL INTELLIGENCE",
    "MONEY AND HAPPINESS",
    "LIVING WITH AI (ARTIFICIAL INTELLIGENCE)",
    "MARRIAGE",
    "GLOBALIZATION",
    "LINGUA FRANCA",
]


def _refresh_contents(document):
    """Remove hard-coded, now-incorrect page numbers from source's eight-unit TOC.

    A semantic source-of-truth book must not display page numbers from the
    pre-expansion 2026 manuscript after eight new studio sections are inserted.
    """
    paragraphs=document.paragraphs
    if len(paragraphs)<10:
        raise AssertionError("Unexpectedly short source front matter")
    contents_style=_style(document,"Studio Contents Entry","Normal",10,False,NAVY,3)
    for n,title in enumerate(ORIGINAL_UNIT_HEADINGS,1):
        p=paragraphs[n+1]
        if not re.match(rf"(?i)^UNIT\s*{n}\s*:",p.text.strip()):
            raise AssertionError(f"Contents item {n} was not the expected UNIT {n}: {p.text[:70]}")
        p.clear()
        p.style=contents_style
        first=p.add_run(f"UNIT {n}  |  {title}")
        first.bold=True
        first.font.color.rgb=NAVY
        p.add_run("\nReading  ·  Listening  ·  Discussion  ·  Presentation  ·  Speaking Studio")
    return len(ORIGINAL_UNIT_HEADINGS)


def _setup(doc):
    _style(doc,"Studio Section","Heading 2",16,True,NAVY,14).paragraph_format.keep_with_next=True
    _style(doc,"Studio Subsection","Heading 3",11,True,TEAL,10).paragraph_format.keep_with_next=True
    _style(doc,"Studio Body","Normal",10.5,False,INK,3)
    _style(doc,"Studio Dialogue","Normal",10,False,INK,2).paragraph_format.left_indent=Inches(.22)
    _style(doc,"Studio Accent","Normal",10.5,True,TEAL,6)


def _add(doc,text,style="Studio Body"):
    return doc.add_paragraph(text,style=style)


def _box(doc,title,body):
    table=doc.add_table(rows=1,cols=1)
    cell=table.cell(0,0)
    tcpr=cell._tc.get_or_add_tcPr()
    shd=OxmlElement("w:shd")
    shd.set(qn("w:fill"),"EDF4F4")
    tcpr.append(shd)
    p=cell.paragraphs[0]
    r=p.add_run(title.upper())
    r.bold=True
    r.font.size=Pt(9)
    r.font.color.rgb=TEAL
    cell.add_paragraph(body,style="Studio Body")


def _section(doc,title):
    return _add(doc,title,"Studio Subsection")


def _write_studio(doc,u):
    title=_add(doc,"SPEAKING STUDIO  |  "+u["name"],"Studio Section")
    title.paragraph_format.page_break_before=True
    _box(doc,"Your speaking mission",u["mission"]+"  "+u["can_do"])
    _section(doc,"Get started")
    _add(doc,u["warmup"])
    _section(doc,"Words that help you speak")
    for phrase in u["language"]:
        _add(doc,"•  "+phrase)
    _section(doc,"A conversation to solve")
    _add(doc,u["pair"]["title"],"Studio Accent")
    _add(doc,u["pair"]["setup"])
    for role in u["pair"]["roles"]:
        _add(doc,"•  "+role)
    for i,step in enumerate(u["pair"]["steps"],1):
        _add(doc,f"{i}. {step}")
    _box(doc,"What success looks like",u["pair"]["target"])
    _section(doc,"Think further")
    _add(doc,u["challenge"])
    _section(doc,"Your short talk")
    _add(doc,u["presentation"])
    _section(doc,"One possible conversation")
    for line in u["model"]:
        _add(doc,line,"Studio Dialogue")
    _section(doc,"Check and try again")
    _add(doc,u["feedback"])
    _add(doc,"With a new partner, repeat the conversation. Change one response using what you learned.")
    _section(doc,"Take it into real life")
    _add(doc,u["transfer"])


def _clean(s):
    return " ".join(s.split()).strip()


def _anchors(doc):
    """Chapter-1 starts are the real eight unit boundaries.

    The first pages contain a misleading contents section with multi-line UNIT
    entries; do not anchor to those text paragraphs.
    """
    found=defaultdict(list)
    starts=[]
    for idx,p in enumerate(doc.paragraphs):
        t=_clean(p.text)
        if re.match(r"(?i)^chapter\s+1\s*:\s*speaking\s+through\s+reading$",t):
            starts.append((idx,p,t))
    for n,item in enumerate(starts,1):
        found[n].append(item)
    if len(starts)!=8:
        raise AssertionError(f"Expected 8 manuscript Chapter 1 starts, got {len(starts)}: {[x[0] for x in starts]}")
    chosen={n:found[n][0] for n in range(1,9)}
    return chosen,found


def insert_studios(document):
    assert len(UNITS)==8 and [u["unit"] for u in UNITS]==list(range(1,9))
    _setup(document)
    cleaned_contents=_refresh_contents(document)
    chosen,all_candidates=_anchors(document)
    if len(chosen)!=8:
        summary={n:[(i,t) for i,p,t in options] for n,options in all_candidates.items()}
        raise AssertionError(f"Expected 8 distinct body unit headings, found {list(chosen)}. Candidates: {summary}")
    indices=[chosen[n][0] for n in range(1,9)]
    if indices!=sorted(indices):
        raise AssertionError(f"Unit anchors are out of order: {indices}")
    # Capture newly added body nodes and move before the next unit's heading.
    results=[]
    for u in UNITS:
        n=u["unit"]
        # Keep strong references to existing lxml nodes; comparing their
        # transient Python id() values can misclassify the original document.
        before_nodes=list(document.element.body)
        _write_studio(document,u)
        new_nodes=[el for el in document.element.body if el not in before_nodes
                   and el.tag!=qn("w:sectPr")]
        if len(new_nodes)<14:
            raise AssertionError(f"Unit {n} studio content unexpectedly short: {len(new_nodes)} nodes")
        if n<8:
            anchor=chosen[n+1][1]._p
            for element in new_nodes:
                anchor.addprevious(element)
        results.append({"unit":n,"name":u["name"],"blocks":len(new_nodes)})
    if cleaned_contents!=8:
        raise AssertionError("Unit TOC rebuild incomplete")
    return results

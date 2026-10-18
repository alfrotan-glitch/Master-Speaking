# -*- coding: utf-8 -*-
"""The 10-Expert Pass: fix issues the panel found + insert 16 'expert desk' feature
boxes (a rotating panel of 10 master voices) into every unit.

Run: python tools/expert_pass.py
"""
import re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PATH = '/home/user/Master-Speaking/Master Grammar C1-C2 (TOEFL House).docx'

NAVY = RGBColor(0x3D, 0x3B, 0xF5)
INK = RGBColor(0x1A, 0x1A, 0x2E)
AMBER = RGBColor(0xC7, 0x87, 0x00)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


# ---------------- 16 expert tips (10 desks, rotating) ----------------
TIPS = {
    1: ("🎓 EXAMINER'S EYE — TOEFL Speaking",
        "In speaking tests, tense control is the fastest signal of level. Anchor your story "
        "in the past simple, then zoom out with the present perfect: \"I failed twice, but "
        "I've learned more from failure than from success.\""),
    2: ("📚 LITERATURE & RHETORIC DESK",
        "Background → event → flashback is the classic three-part story shape used by "
        "novelists. Listeners remember stories shaped this way — and forget flat lists of "
        "past verbs. Structure is what makes a story sound professional."),
    3: ("🧪 RESEARCH DESK — Corpus Evidence",
        "Corpus studies show native speakers use 'going to' more than 'will' in conversation. "
        "Reserve 'will' for instant decisions and predictions you are willing to defend."),
    4: ("💼 PROFESSIONAL ENGLISH DESK",
        "In professional life, \"I'd suggest…\" opens doors; \"You must…\" closes them. "
        "Power is choosing the right strength — not the strongest one."),
    5: ("🎯 TOP-STUDENT DESK — Study Strategy",
        "Don't memorise rules — memorise one living example per type: \"If you heat ice, it "
        "melts.\" / \"If it rains, we'll cancel.\" / \"If I were you, I'd wait.\" Three "
        "sentences contain the whole system."),
    6: ("🧠 MEMORY LAB — Learning Science",
        "Emotion glues grammar to memory. Learn these structures by saying them about real "
        "feelings, never invented ones — the brain keeps what it feels."),
    7: ("📐 GRAMMAR PROFESSOR — Precision",
        "The most examined point at C1: mustn't ≠ can't. \"He can't be home\" (I'm sure he "
        "isn't) vs \"He mustn't leave\" (I forbid him). One word apart — worlds apart."),
    8: ("✍️ STYLE DESK — Elegant English",
        "Weak: \"X is better than Y.\" Strong: \"X is by far the most reliable predictor of Y.\" "
        "Comparatives with evidence are the mark of a mature arguer."),
    9: ("🌍 USAGE WATCH — Real-World English",
        "Academic English hides the doer on purpose: \"It is widely believed that…\" An "
        "answer built on passive reporting verbs sounds objective — and objectivity sounds "
        "educated."),
    10: ("🎓 EXAMINER'S EYE — TOEFL Speaking",
         "Third conditionals earn marks because they prove you can manage two time levels at "
         "once. One perfect \"Had I known…\" can lift an entire answer a band."),
    11: ("🗣️ SOUND COACH — Pronunciation",
         "When retelling, drop 'that' and flatten your intonation: \"She said she'd already "
         "left.\" The lively voice of direct speech and the flat voice of report are two "
         "different instruments — learn to switch."),
    12: ("🎯 TOP-STUDENT DESK — Study Strategy",
         "Don't learn fifty verbs — learn five chunks a day in real sentences: \"I enjoy "
         "swimming.\" \"I decided to leave.\" Chunks survive exams; lists don't."),
    13: ("📚 LITERATURE & RHETORIC DESK",
         "The aside — the non-defining clause — is how writers add a second voice mid-sentence: "
         "\"Kabul, which has survived centuries of change, remains vibrant.\" Use it to show "
         "composure inside a long answer."),
    14: ("💼 PROFESSIONAL ENGLISH DESK",
         "Fronted participles instantly upgrade formal speech: \"Considering the costs…\", "
         "\"Given the evidence…\", \"Looking at the bigger picture…\". Three phrases — instant "
         "professional polish."),
    15: ("📐 GRAMMAR PROFESSOR — Precision",
         "Inversion is punctuation for the ear: it signals 'this is my central claim'. Use it "
         "once per answer — twice is theatre, never is invisible."),
    16: ("🧪 RESEARCH DESK — Corpus Evidence",
         "Academic corpora show expert writers hedge three to five times per page. A hedged "
         "claim (\"It may be argued…\") reads as confident control — not weakness. That is C2."),
}

# ---------------- fix literal markdown in runs (Copy Editor) ----------------
def fix_literal_md(par):
    n = 0
    for r in par.runs:
        if "**" in r.text or "*" in r.text:
            txt = r.text
            segs = re.split(r'(\*\*.+?\*\*)', txt)
            if len(segs) > 1 or "**" in txt:
                # rebuild as bold segments inside this run position
                parent = r._element.getparent()
                idx = list(parent).index(r._element)
                new_els = []
                for s in segs:
                    if not s:
                        continue
                    nr = par.add_run()
                    if s.startswith("**") and s.endswith("**"):
                        nr.text = s[2:-2]
                        nr.font.bold = True
                    else:
                        nr.text = s
                    nr.font.name = "Calibri"
                    nr.font.size = Pt(11)
                    nr.font.color.rgb = INK
                    new_els.append(nr._element)
                parent.remove(r._element)
                for k, el in enumerate(new_els):
                    parent.insert(idx + k, el)
                n += 1
                continue
            # single stray asterisks (e.g. *learner*) -> italic
            if "*" in r.text:
                segs = re.split(r'(\*[^*]+\*)', r.text)
                if len(segs) > 1:
                    parent = r._element.getparent()
                    idx = list(parent).index(r._element)
                    new_els = []
                    for s in segs:
                        if not s:
                            continue
                        nr = par.add_run()
                        if s.startswith("*") and s.endswith("*") and len(s) > 2:
                            nr.text = s[1:-1]
                            nr.font.italic = True
                        else:
                            nr.text = s
                        nr.font.name = "Calibri"
                        nr.font.size = Pt(11)
                        nr.font.color.rgb = r.font.color.rgb if r.font.color and r.font.color.rgb else INK
                        new_els.append(nr._element)
                    parent.remove(r._element)
                    for k, el in enumerate(new_els):
                        parent.insert(idx + k, el)
                    n += 1
    return n


def insert_tip_box(doc, anchor_par, title, body):
    t = doc.add_table(rows=1, cols=1)
    try:
        t.style = 'Table Grid'
    except Exception:
        pass
    cell = t.rows[0].cells[0]
    shade(cell, "FFF6E0")
    p0 = cell.paragraphs[0]
    r = p0.add_run("💡 " + title)
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = AMBER
    r.font.name = "Segoe UI"
    p1 = cell.add_paragraph()
    r2 = p1.add_run(body)
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = INK
    r2.font.name = "Calibri"
    anchor_par._p.addprevious(t._tbl)
    # spacer paragraph after box
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(2)
    anchor_par._p.addprevious(sp._p)
    return t


def main():
    doc = Document(PATH)
    fixed = 0
    for p in doc.paragraphs:
        fixed += fix_literal_md(p)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    fixed += fix_literal_md(p)
    print("markdown fixes:", fixed)

    # insert expert tips before each unit's Common Mistakes heading
    inserted = 0
    unit = 0
    for p in list(doc.paragraphs):
        m = re.match(r"^🔥 UNIT (\d+)", p.text.strip())
        if m:
            unit = int(m.group(1))
        if "Common Mistakes — Watch Out!" in p.text and unit >= 1:
            if unit in TIPS:
                title, body = TIPS[unit]
                insert_tip_box(doc, p, title, body)
                inserted += 1
                unit = 0 if inserted >= 16 else unit
    print("expert tips inserted:", inserted)
    doc.save(PATH)
    print("SAVED — 10-expert pass complete.")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""De-schedule the book: remove ALL course-planning language (Day/Week/Month/schedule).

A published grammar book speaks in UNITS — not days, weeks or months.
Run: python tools/de_schedule_book.py   (then inspect the leftovers report)
"""
import re
from docx import Document

PATH = '/home/user/Master-Speaking/Master Grammar C1-C2 (TOEFL House).docx'

# ---------------------------------------------------------- run-level replaces
RUN_REPLACES = [
    # scheduling -> book language
    (re.compile(r"\bDAY (\d+)"), r"UNIT \1"),
    (re.compile(r"\bDay (\d+)"), r"Unit \1"),
    (re.compile(r"\bDays (\d+)"), r"Units \1"),
    ("PROGRESS TEST", "REVIEW TEST"),
    ("Progress Test", "Review Test"),
    ("progress test", "review test"),
    # title page
    ("A Complete English Grammar Course in 16 Days",
     "A Complete English Grammar Course in 16 Units"),
    ("16 Days  ·  8 Weeks  ·  2 Months", "16 Units  ·  5 Tests  ·  4 Appendices"),
    ("**Duration**", "**Structure**"),
    ("2 months  |  8 weeks  |  2 days per week  |  16 teaching days",
     "16 units  |  complete C1–C2 grammar syllabus  |  5 tests  |  4 appendices"),
    ("The Advanced Speaking Class — The TOEFL House",
     "Learners of English at C1–C2 level"),
    # part dividers & subbanners
    ("PART ONE  ·  MONTH 1", "PART ONE"),
    ("PART TWO  ·  MONTH 2", "PART TWO"),
    ("PART ONE — MONTH 1  ·  BUILDING THE GRAMMAR CORE  (Units 1–8)",
     "PART ONE  ·  BUILDING THE GRAMMAR CORE  (Units 1–8)"),
    ("PART TWO — MONTH 2  ·  MASTERING STYLE & PRECISION  (Units 9–16)",
     "PART TWO  ·  MASTERING STYLE & PRECISION  (Units 9–16)"),
    ("Building the Grammar Core  —  Units 1–8", "Building the Grammar Core  —  Units 1–8"),
    ("Mastering Style & Precision  —  Units 9–16", "Mastering Style & Precision  —  Units 9–16"),
    # headings & labels
    ("Course Map — Two Months at a Glance", "Course Outline"),
    ("The Structure of Every Day", "The Structure of Every Unit"),
    ("How this book is organised — every day", "How this book is organised — every unit"),
    ("9.  Homework & Self-Check", "9.  Practice & Self-Check"),
    ("9. Homework & Self-Check", "9. Practice & Self-Check"),
    ("Homework & Self-Check", "Practice & Self-Check"),
    # colophon / misc meta
    ("Written and designed for the Advanced Speaking Class — The TOEFL House, Kabul.",
     "The TOEFL House — English Department  ·  Kabul."),
    ("16 days  ·  8 weeks  ·  2 months  ·  Grammar syllabus level: Destination C1 & C2 (original content written for speaking).",
     "A complete C1–C2 grammar course following the Destination C1 & C2 grammar syllabus."),
    ("The last written check of the course — the full grammar system in 30 questions.",
     "The last written check — the full grammar system in 30 questions."),
]

# ---------------------------------------------------------- full-paragraph rewrites
PARA_REWRITES = [
    ("The course is designed for",
     "This book is organised into sixteen units, each one a complete lesson. It begins "
     "with the tense system and future forms, moves through modals and conditionals, and "
     "finishes with the most powerful structures of C1–C2 English: the passive, reported "
     "speech, complex clauses, inversion, emphasis and hedging. By the final unit, you "
     "will command the complete C1–C2 grammar system."),
    ("This book contains",
     "This book contains sixteen units. Each unit is a complete grammar lesson: clear "
     "explanations, natural examples, careful practice and speaking tasks — everything "
     "you need to master one area of C1–C2 grammar. Work through the units in order, "
     "or choose the grammar you need most."),
    ("Best rhythm for this course",
     "Best rhythm: review each unit's card the next day, then again after three and "
     "seven days. Use blank cards for pure self-testing — never re-read, always recall."),
    ("Fifteen minutes a day",
     "Fifteen minutes a day beats three hours at the weekend. That is the whole method."),
    ("This test shows you (and your teacher)",
     "This test shows you which grammar areas are already strong and which need attention. "
     "Work alone. Don't use a dictionary. Time: 25 minutes."),
    ("Your teacher may also use this as the written part",
     ""),  # delete sentence (paragraph handled below)
    ("Eight weeks. Two days per week.",
     "Sixteen units, from the tense system to the finest points of style — a complete "
     "journey through the C1–C2 grammar system."),
    ("Use the grammar the same day.",
     "Use the grammar immediately. Force yourself to use the new structure at least "
     "three times outside the exercise book."),
    ("Record yourself. Every homework",
     "Record yourself. Every recording task is real speaking practice — listen once "
     "before you share it."),
    ("Day A of each week",
     "Some units are heavier on form and accuracy; others on fluency and production — "
     "pace yourself accordingly."),
]

# assessment bullets (rewritten completely)
BULLETS = {
    "Before": "•  **Before you begin:** the Diagnostic Test — find your strong and weak grammar areas (score guide included).",
    "Daily:": "•  **Every unit:** a recording task using the target grammar + the 'Grammar at a Glance' self-check.",
    "Progress Tests:": "•  **Review Tests 1–3:** after every four units — written tests with full answer keys.",
    "Final (": "•  **Final Written Test** (30 questions) + self-assessment against the Can-Do Checklist in Appendix C.",
}

COURSE_MAP_HEADERS = ["Week", "Day"]  # scoped table headers to fix
WEEK_MAP = {"1": "1–2", "2": "3–4", "3": "5–6", "4": "7–8",
            "5": "9–10", "6": "11–12", "7": "13–14", "8": "15–16"}


def replace_in_runs(p):
    n = 0
    for r in p.runs:
        t = r.text
        if not t:
            continue
        for pat, rep in RUN_REPLACES:
            if callable(getattr(pat, "sub", None)):
                t2 = pat.sub(rep, t)
            else:
                t2 = t.replace(pat, rep)
            if t2 != t:
                n += 1
                t = t2
        r.text = t
    return n


def rewrite_para(p, new_text):
    if new_text == "":
        p._p.getparent().remove(p._p)
        return
    # clear all runs, keep paragraph style; write single run
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    r = p.add_run(new_text)
    r.font.name = "Calibri"
    from docx.shared import Pt as _Pt
    r.font.size = _Pt(11)


def main():
    doc = Document(PATH)
    stats = {"runs": 0, "paras": 0, "bullets": 0, "tables": 0}

    for p in doc.paragraphs:
        stats["runs"] += replace_in_runs(p)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    stats["runs"] += replace_in_runs(p)

    # full paragraph rewrites
    for key, new in PARA_REWRITES:
        for p in list(doc.paragraphs):
            if p.text.strip().startswith(key) or (key in p.text and p.text.strip().startswith(key[:20])):
                if key in p.text:
                    rewrite_para(p, new)
                    stats["paras"] += 1
                    break

    # assessment bullets
    for p in list(doc.paragraphs):
        t = p.text.strip()
        for key, new in BULLETS.items():
            if t.startswith("•") and key in t:
                rewrite_para(p, new)
                stats["bullets"] += 1
                break

    # scoped course-outline tables
    for t in doc.tables:
        hdr = [c.text.strip() for c in t.rows[0].cells]
        if "Grammar Area" in hdr and ("Week" in hdr or "Day" in hdr):
            for j, name in enumerate(hdr):
                cell = t.rows[0].cells[j]
                if name == "Week":
                    for r in cell.paragraphs[0].runs: r.text = "Units" if r.text.strip() == "Week" else r.text
                    if not cell.text.strip() or cell.text.strip() == "Week":
                        cell.paragraphs[0].runs[0].text = "Units"
                if name == "Day":
                    for r in cell.paragraphs[0].runs:
                        if r.text.strip() == "Day": r.text = "Unit"
            # first column value pairs
            for i, row in enumerate(t.rows):
                if i == 0: continue
                c = row.cells[0]
                val = c.text.strip()
                if val in WEEK_MAP:
                    runs = c.paragraphs[0].runs
                    if runs:
                        runs[0].text = WEEK_MAP[val]
                        for r in runs[1:]: r.text = ""
                    else:
                        c.paragraphs[0].add_run(WEEK_MAP[val])
                    stats["tables"] += 1

    doc.save(PATH)

    # ---------------- leftovers report ----------------
    doc2 = Document(PATH)
    texts = [p.text for p in doc2.paragraphs]
    for t in doc2.tables:
        for r in t.rows:
            for c in r.cells:
                texts.append(c.text)
    blob = "\n".join(texts)
    print("stats:", stats)
    print("\n=== LEFTOVER SCHEDULING WORDS (context check) ===")
    for w in [r"\bDays?\b", r"\bWEEK\b", r"\bWeek\b", r"\bweek\b", r"\bMonth\b", r"\bmonth\b",
              r"\bMONTH\b", r"\bDAY\b", r"\b90-minute\b", r"\bhomework\b", r"\bHomework\b",
              r"\bteaching days\b", r"\bschedule\b"]:
        hits = []
        for t in texts:
            for m in re.finditer(w, t):
                s = max(0, m.start()-32); hits.append(t[s:m.end()+32].replace("\n", " "))
        if hits:
            print(f"\n{w}: {len(hits)}")
            for h in hits[:6]:
                print("   …" + h + "…")


if __name__ == "__main__":
    main()

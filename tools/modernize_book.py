# -*- coding: utf-8 -*-
"""Modern design + voice transformation for Master Grammar C1-C2.

- Modern palette (vivid indigo, teal, coral, amber) instead of old navy
- Modern fonts: Calibri body + Segoe UI headings + Consolas formulas
- Icon-first headings (emoji) for instant scanability
- A punchy 'hook line' at the top of every day (modern voice, memory-focused)
- Bigger, bolder day banners

Run: python tools/modernize_book.py   (idempotent)
"""
import re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

PATH = '/home/user/Master-Speaking/Master Grammar C1-C2 (TOEFL House).docx'

# ---------- palette ----------
INDIGO = RGBColor(0x3D, 0x3B, 0xF5)
TEAL   = RGBColor(0x00, 0xB3, 0x9F)
CORAL  = RGBColor(0xE8, 0x45, 0x45)
AMBER  = RGBColor(0xE9, 0xA4, 0x00)
INK    = RGBColor(0x1A, 0x1A, 0x2E)
VIOLET = RGBColor(0x7C, 0x3A, 0xED)

# old shading fills -> new fills
FILL_MAP = {
    "1F3364": "3D3BF5",  # navy banners/headers -> indigo
    "0E766E": "00B39F",  # teal -> vivid teal
    "B8860B": "E9A400",  # gold -> amber
    "A31F1F": "E84545",  # dark red -> coral red
    "E8EDF7": "F1F2FF",  # subbanner tint
    "FBF6E9": "FFF6E0",  # warm boxes
    "EAF0FA": "EEF3FF",  # formula cards
    "EEF4EE": "E9FBF6",  # example boxes
    "F8ECEC": "FFEFEF",  # mistake zebra
    "F2F5FA": "F5F6FF",  # table zebra
}
# old run colors -> new colors
COLOR_MAP = {
    "1F3364": (0x3D, 0x3B, 0xF5),
    "0E766E": (0x00, 0xB3, 0x9F),
    "B8860B": (0xE9, 0xA4, 0x00),
    "A31F1F": (0xE8, 0x45, 0x45),
    "1E6B3A": (0x0E, 0x9F, 0x6E),
    "222222": (0x1A, 0x1A, 0x2E),
}

BODY_FONT = "Calibri"
HEAD_FONT = "Segoe UI"
CODE_FONT = "Consolas"

# ---------- hook lines: modern voice, one per day ----------
HOOKS = {
    1:  "🔥 REAL TALK — \"I have seen him yesterday\" is the mistake that screams *learner*. "
        "Today it dies forever. Your story, your journey, your English — in the right tense.",
    2:  "🎬 Stories win interviews, speeches and hearts. Today you learn the tense layering "
        "that makes every story you tell impossible to forget.",
    3:  "🔮 Predict your own future — in English. Will? Going to? After today, never mix them again.",
    4:  "🚦 Must? Should? Had better? One wrong modal changes everything. Today: total control of your voice.",
    5:  "🪄 Welcome to the IF-box — the grammar of dreams, plans and 'what if…'. Mind the sign on the door!",
    6:  "💔 Regret. Love. Annoyance. Emotions need the right grammar — today: the structures of the heart.",
    7:  "🕵️ Detectives of English: guess, accuse, regret — with 100% grammatical precision.",
    8:  "📊 Richer or happier? City or village? Arguments live and die in comparisons. Today you win them all.",
    9:  "🤖 News, science, technology — the global voice speaks in the passive. Sound like a professional today.",
    10: "⏳ Time travel, grammar style: regret the past, rewrite the present — and argue about any 'what if'.",
    11: "🗣️ \"She said she loved me…\" Retell anything — a fight, a study, a speech — like a born storyteller.",
    12: "🧩 -ing or to? The great verb puzzle — today it becomes a picture, and it stays in your memory.",
    13: "🧬 Turn flat sentences into rich ones. Detail is power — today you add it smoothly, like a novelist.",
    14: "⚡ Condense. Contrast. Persuade. The sentence skills that make you sound like a professor.",
    15: "🎤 Spotlight time. Today: the structures that make any audience stop and listen.",
    16: "🕊️ Diplomacy is real power. Speak softly, argue precisely — and finish this course as a true C1–C2 master.",
}

# ---------- emoji prefixes for scanability ----------
PREFIXES = [
    (r"^FORMULA CARD", "⚡ "),
    (r"^MEMORY HOOK", "🧠 "),
    (r"^GRAMMAR AT A GLANCE", "🔑 "),
    (r"^1\.\s+Speak First", "🎤 "),
    (r"^2\.\s+Grammar Focus", "📘 "),
    (r"^3\.\s+How We Really Say It", "🎧 "),
    (r"^4\.\s+Common Mistakes", "❌ "),
    (r"^5\.\s+Practice", "✏️ "),
    (r"^6\.\s+Pronunciation Clinic", "🗣️ "),
    (r"^7\.\s+Speak!", "💬 "),
    (r"^8\.\s+TOEFL-Speaking Task", "🎯 "),
    (r"^9\.\s+Homework", "📝 "),
    (r"^DAY \d+", "🔥 "),
    (r"^PROGRESS TEST", "🧪 "),
    (r"^FINAL WRITTEN TEST", "🏁 "),
    (r"^DIAGNOSTIC TEST", "🧭 "),
    (r"^APPENDIX A", "✅ "),
    (r"^APPENDIX B", "🧰 "),
    (r"^APPENDIX C", "📈 "),
    (r"^APPENDIX D", "🗂️ "),
    (r"^THE MASTER METHOD", "🚀 "),
    (r"^The Five Tools", "🖐️ "),
    (r"^Golden Rules", "⭐ "),
    (r"^Tips for Teachers", "👩‍🏫 "),
    (r"^The Mistake Killer", "🔨 "),
    (r"^My Three Persistent Errors", "🎯 "),
    (r"^My Final Reflection", "🪞 "),
    (r"^Score guide", "📊 "),
    (r"^Final score guide", "🏆 "),
    (r"^PART A", "🅰️ "),
    (r"^PART B", "🅱️ "),
    (r"^PART C", "🅲 "),
]


def recolor_shading(doc):
    n = 0
    for shd in doc.element.body.iter(qn('w:shd')):
        fill = shd.get(qn('w:fill'))
        if fill and fill.upper() in FILL_MAP:
            shd.set(qn('w:fill'), FILL_MAP[fill.upper()])
            n += 1
    return n


def restyle_fonts(doc):
    def fix_runs(runs, head=False, code=False):
        for r in runs:
            name = CODE_FONT if code else (HEAD_FONT if head else BODY_FONT)
            r.font.name = name
            rPr = r._element.get_or_add_rPr()
            rf = rPr.find(qn('w:rFonts'))
            if rf is None:
                rf = rPr.makeelement(qn('w:rFonts'), {})
                rPr.append(rf)
            for attr in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
                rf.set(qn(attr), name)
            col = r.font.color
            if col is not None and col.rgb is not None:
                key = str(col.rgb)
                if key in COLOR_MAP:
                    rr, gg, bb = COLOR_MAP[key]
                    col.rgb = RGBColor(rr, gg, bb)

    for p in doc.paragraphs:
        txt = p.text.strip()
        code = any((r.font.name or "") == "Courier New" for r in p.runs)
        head = bool(re.match(r"^(DAY \d|PART |APPENDIX|DIAGNOSTIC|PROGRESS|FINAL WRITTEN|"
                             r"CONTENTS|FOREWORD|HOW TO USE|THE MASTER METHOD|COURSE MAP|"
                             r"GRAMMAR SYLLABUS|MASTER|GRAMMAR|C1|A Complete|16 Days|"
                             r"By the end|The Structure|Golden Rules|Tips for|The Five Tools|"
                             r"Tool \d|Your Golden|The Mistake|Assessment|My )", txt))
        fix_runs(p.runs, head=head, code=code)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    code = any((r.font.name or "") == "Courier New" for r in p.runs)
                    fix_runs(p.runs, code=code)


def apply_emoji(doc):
    n = 0
    for p in doc.paragraphs:
        txt = p.text.strip()
        if not txt:
            continue
        for pat, emo in PREFIXES:
            if re.match(pat, txt):
                if txt.startswith(emo):
                    break
                # skip if any known emoji already at start
                if re.match(r"^[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\s]", txt):
                    break
                if p.runs:
                    p.runs[0].text = emo + p.runs[0].text
                    n += 1
                break
    return n


def bigger_day_banners(doc):
    for p in doc.paragraphs:
        if re.match(r"^🔥 DAY |^DAY ", p.text.strip()):
            for r in p.runs:
                r.font.size = Pt(17)


def insert_hooks(doc):
    """Insert a modern hook line after each day's 'Grammar Area' subbanner."""
    paras = list(doc.paragraphs)
    n = 0
    for i, p in enumerate(paras):
        m = re.match(r"^🔥 DAY (\d+)|^DAY (\d+)", p.text.strip())
        if not m:
            continue
        d = int(m.group(1) or m.group(2))
        # the next paragraph should be the subbanner ("Grammar Area: ...")
        for j in range(i + 1, min(i + 4, len(paras))):
            if paras[j].text.strip().startswith("Grammar Area:"):
                if any("REAL TALK" in paras[k].text or "Welcome to the IF-box" in paras[k].text
                       or "Detectives of English" in paras[k].text or "Spotlight time" in paras[k].text
                       for k in range(j + 1, min(j + 3, len(paras)))):
                    break  # already inserted
                hp = doc.add_paragraph()
                hp.paragraph_format.space_before = Pt(4)
                hp.paragraph_format.space_after = Pt(10)
                r = hp.add_run(HOOKS[d])
                r.font.size = Pt(11.5)
                r.font.bold = True
                r.font.color.rgb = INDIGO
                r.font.name = HEAD_FONT
                paras[j]._p.addnext(hp._p)
                n += 1
                break
    return n


def main():
    doc = Document(PATH)
    print("shading recolored :", recolor_shading(doc))
    restyle_fonts(doc)
    print("emoji prefixes    :", apply_emoji(doc))
    bigger_day_banners(doc)
    print("hook lines added  :", insert_hooks(doc))
    doc.save(PATH)
    print("SAVED — modern edition ready.")


if __name__ == "__main__":
    main()

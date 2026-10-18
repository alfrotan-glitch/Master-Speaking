# -*- coding: utf-8 -*-
"""Front matter: title, introduction & objectives, how to use (students & teachers),
contents, diagnostic test. Spec sections 2, 9, 10, 11."""
from style import (para, run, box, table, spacer, h_banner, page_break,
                   setup_doc, NAVY, TEAL, GOLD, INK, GREY, WHITE,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY, FILL_NAVY, FILL_TEAL)
from docx.enum.text import WD_ALIGN_PARAGRAPH

PARTS = [
    ("Part One", "Build Strong Sentences", [1, 2]),
    ("Part Two", "Express Ideas Clearly", [3, 4]),
    ("Part Three", "Think Beyond the Present", [5, 6]),
    ("Part Four", "Compare and Persuade", [7, 8]),
    ("Part Five", "Describe and Explain", [9, 10]),
    ("Part Six", "Speak with Greater Precision", [11, 12]),
    ("Part Seven", "Sound More Natural and Advanced", [13, 14]),
    ("Part Eight", "Speak with Confidence", [15, 16]),
]

LESSON_TITLES = {
    1: "Tenses for Real Communication",
    2: "Telling Stories and Describing Experiences",
    3: "Questions, Auxiliary Verbs, and Follow-up Questions",
    4: "Modal Verbs for Real-Life Situations",
    5: "Conditionals for Decisions and Possibilities",
    6: "Wishes, Regrets, and Hypothetical Situations",
    7: "Comparisons Beyond the Basics",
    8: "Linking Ideas and Building Arguments",
    9: "Passive Voice in Natural English",
    10: "Causative Structures",
    11: "Gerunds and Infinitives",
    12: "Relative Clauses and Concise Descriptions",
    13: "Reported Speech and Reporting Verbs",
    14: "Participles and Advanced Sentence Patterns",
    15: "Hedging, Emphasis, and Natural Inversion",
    16: "Grammar in Real Conversation",
}


def title_page(doc):
    spacer(doc, 60)
    para(doc, "TOEFL HOUSE", size=14, bold=True, color=TEAL, align='c', space_after=2)
    para(doc, "GRAMMAR FOR", size=30, bold=True, color=NAVY, align='c', space_before=18, space_after=0)
    para(doc, "SPECIAL SPEAKING", size=30, bold=True, color=NAVY, align='c', space_before=0, space_after=6)
    para(doc, "A practical grammar course for accurate, natural, confident speech",
         size=13, italic=True, color=GREY, align='c', space_before=6, space_after=24)
    box(doc, None, [
        ("Learn the grammar. Use it in conversation. Make it part of your speech.", True),
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    spacer(doc, 40)
    para(doc, "For Intermediate and Advanced learners", size=12, color=INK, align='c')
    para(doc, "16 lessons  ·  3 review tests  ·  final assessment  ·  5 appendices",
         size=11, color=GREY, align='c')
    page_break(doc)


def introduction(doc):
    h_banner(doc, "INTRODUCTION", sub="What this book does and how it works")
    para(doc, "This book has one purpose: to help you use grammar accurately, naturally and "
              "confidently when you speak English.")
    para(doc, "It is not enough to know a rule. The goal is to turn that knowledge into active "
              "speaking skill — to choose the right structure, in the right moment, and say it "
              "without thinking about it.")
    para(doc, "Every lesson follows the same path: you speak first, you learn one clear rule, "
              "you see how similar structures differ, you practise, and then you speak again — "
              "this time with the new grammar in your voice. Each lesson ends with a short review "
              "and a self-check, so you always know what you can already do.")
    para(doc, "The course works for both Intermediate and Advanced learners in the same room. "
              "Everyone studies the same core lesson. The core work builds accuracy; the Advanced "
              "Upgrade boxes build flexibility, precision and naturalness. Advanced work rewards "
              "appropriate, precise use — never complexity for its own sake.")
    para(doc, "", space_after=6)
    para(doc, "By the end of the course, you should be able to:", size=11, bold=True, color=NAVY)
    for b in [
        "construct grammatically accurate sentences while speaking;",
        "choose appropriate tenses and sentence structures for your meaning;",
        "ask questions and respond with greater precision;",
        "explain experiences, opinions and hypothetical situations;",
        "connect ideas into coherent spoken responses;",
        "use a wider range of structures naturally;",
        "recognise and correct your recurring grammatical mistakes;",
        "apply learned structures in unfamiliar speaking situations.",
    ]:
        para(doc, f"•  {b}", indent=0.12)
    para(doc, "Completion of the sixteen lessons is not proof of these outcomes by itself. The "
              "Diagnostic Test and the Final Assessment use comparable tasks so that your progress "
              "can be seen honestly — and so you know exactly what to work on next.",
         size=11, italic=True, color=GREY)
    page_break(doc)


def how_to_use(doc):
    h_banner(doc, "HOW TO USE THIS BOOK", sub="For students and teachers")
    para(doc, "For students", size=12, bold=True, color=NAVY)
    para(doc, "Work through the lessons in order: each one builds on earlier material. Always "
              "begin with the Speaking Hook — say your answers out loud before you read the rule. "
              "The rule then gives you the tool you were already reaching for.")
    para(doc, "Do the exercises out loud whenever possible. Grammar becomes speech through the "
              "mouth, not only through the eyes. Use the Pair Speaking and Real Talk sections as "
              "they are designed: no reading from notes.")
    para(doc, "After every lesson, cover the page and try the retrieval questions. Tick the "
              "self-check honestly. Return to the Formula Book (Appendix 1) whenever you review.")
    para(doc, "", space_after=4)
    para(doc, "Two pathways, one classroom", size=12, bold=True, color=NAVY)
    table(doc, ["Pathway", "Focus", "What to do"], [
        [("Intermediate — Build Accuracy", True),
         "guided construction, error correction, short clear responses",
         "complete all core practice; use the Intermediate box in each Advanced Upgrade"],
        [("Advanced — Build Flexibility", True),
         "choice between structures, subtle meaning, extended arguments",
         "add the Advanced Upgrade work; in speaking tasks, qualify, counter and connect"],
    ], widths=[1.7, 2.2, 2.4])
    para(doc, "Both groups can respond to the same topic at different levels: give a clear opinion "
              "with two reasons (Intermediate), or qualify your position, address a counterargument "
              "and connect ideas with varied structures (Advanced).")
    para(doc, "", space_after=4)
    para(doc, "For teachers", size=12, bold=True, color=NAVY)
    para(doc, "Keep grammar explanation short and give learners substantial time to produce spoken "
              "English. The suggested pacing below is a guide — adjust it to your class length.")
    table(doc, ["Activity", "Minutes (of a 60-minute lesson)"], [
        ["Explanation and examples", "15"],
        ["Controlled practice", "10"],
        ["Pair speaking", "20"],
        ["Independent speaking challenge", "10"],
        ["Feedback and review", "5"],
        [("Total", True), ("60", True)],
    ], widths=[3.6, 2.7])
    para(doc, "Review earlier structures in the review tests and in retrieval practice. Evaluate "
              "speaking with the success criteria and the rubric in the Final Assessment — not with "
              "rigid model answers. Accept alternative answers where an exercise allows them.")
    page_break(doc)


def contents(doc):
    h_banner(doc, "CONTENTS", sub="Sixteen lessons in eight thematic parts")
    rows = []
    for pno, ptitle, lessons in PARTS:
        rows.append([(f"{pno}  —  {ptitle}", True), ""])
        for ln in lessons:
            rows.append([f"    Lesson {ln}", LESSON_TITLES[ln]])
    table(doc, ["", "Lesson"], rows, widths=[1.5, 4.8], zebra=False)
    rows2 = [
        ["Review Test 1  (after Lesson 4)", "Cumulative review — Lessons 1–4"],
        ["Review Test 2  (after Lesson 8)", "Cumulative review — Lessons 1–8"],
        ["Review Test 3  (after Lesson 12)", "Cumulative review — Lessons 1–12"],
        [("Final Assessment", True), "Grammar assessment + independent speaking task"],
        ["Appendix 1", "Grammar Formula Book"],
        ["Appendix 2", "Common Errors and Corrections Guide"],
        ["Appendix 3", "Essential Sentence Patterns for Speaking"],
        ["Appendix 4", "Speaking Self-Assessment and Can-Do Tracker"],
        ["Appendix 5", "Complete Answer Key"],
    ]
    table(doc, ["Tests and reference", ""], rows2, widths=[2.6, 3.7], zebra=True)
    page_break(doc)


def diagnostic(doc, keys_registry):
    h_banner(doc, "DIAGNOSTIC TEST", sub="Find your starting point — 25 questions · no time limit")
    para(doc, "Do this test before Lesson 1. Do not study first: the point is to see what you can "
              "already do. Mark your score out of 25, then keep the paper — you will compare it "
              "with your Final Assessment later.", size=11, italic=True, color=GREY)
    para(doc, "Part A — Tenses and time  (10 questions)", size=11, bold=True, color=NAVY)
    A = [
        "I __________ (see) that film last week.",
        "She __________ (work) here since 2021.",
        "While I __________ (cook), the phone rang.",
        "He told me he __________ already __________ (leave).",
        "Water __________ (boil) at 100°C.",
        "They __________ (build) a new bridge when we visited.",
        "I __________ my keys — I can't get in.  (lose)",
        "Last summer we __________ (go) to Herat.",
        "How many books __________ you __________ (read) this month?",
        "When I arrived, the train __________ already __________ (leave).",
    ]
    for i, q in enumerate(A, 1):
        para(doc, f"{i}.  {q}", indent=0.12)
    para(doc, "Part B — Structures  (10 questions)", size=11, bold=True, color=NAVY)
    B = [
        "If it __________ (rain), we'll stay home.",
        "I wish I __________ (know) the answer.",
        "My phone needs __________.  (repair)",
        "The report __________ (write) by the team last week.",
        "He suggested __________ early.  (leave)",
        "Could you tell me where __________ ?  (the station / be)",
        "The girl __________ helped me was very kind.  (who / whose / which)",
        "I'd rather you __________ (not, smoke) here.",
        "Ali is __________ than his brother.  (intelligent)",
        "Not until midnight __________.  (she / finish)",
    ]
    for i, q in enumerate(B, 11):
        para(doc, f"{i}.  {q}", indent=0.12)
    para(doc, "Part C — Use and communication  (5 questions)", size=11, bold=True, color=NAVY)
    C = [
        "I __________ find my passport anywhere.  (mustn't / can't)",
        "__________ being very tired, he finished the race.  (Despite / Although)",
        "She asked me, \"Where do you live?\"  →  She asked me __________.",
        "It __________ rain later — take an umbrella.  (certainty: 50%)",
        "I __________ my hair cut yesterday.",
    ]
    for i, q in enumerate(C, 21):
        para(doc, f"{i}.  {q}", indent=0.12)
    box(doc, "Diagnostic answer key", [
        "A.  1 saw · 2 has worked · 3 was cooking · 4 had left · 5 boils · 6 were building · "
        "7 have lost / 've lost · 8 went · 9 have … read · 10 had already left",
        "B.  11 rains · 12 knew · 13 repairing (or: to be repaired) · 14 was written · 15 leaving · "
        "16 the station is · 17 who · 18 didn't smoke · 19 more intelligent · 20 did she finish",
        "C.  21 can't · 22 Despite · 23 where I lived · 24 might · 25 had",
    ], fill=FILL_BOX_GREY, label_color=NAVY)
    keys_registry["Diagnostic"] = {
        "A": ["saw", "has worked", "was cooking", "had left", "boils", "were building",
              "have lost", "went", "have read", "had already left"],
        "B": ["rains", "knew", "repairing / to be repaired", "was written", "leaving",
              "the station is", "who", "didn't smoke", "more intelligent", "did she finish"],
        "C": ["can't", "Despite", "where I lived", "might", "had"],
    }
    para(doc, "Score guide: 21–25 — strong base, keep the Advanced Upgrade in sight.  "
              "15–20 — solid core; work carefully through both pathways.  "
              "Below 15 — do the core practice twice and speak every answer aloud; "
              "accuracy first, speed later.", size=10.5, italic=True, color=GREY)
    page_break(doc)

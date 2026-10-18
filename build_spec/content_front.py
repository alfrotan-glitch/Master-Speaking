# -*- coding: utf-8 -*-
"""Front matter: title, publication info, introduction, how to use,
contents, and diagnostic test."""
from style import (para, run, box, table, spacer, h_banner, page_break,
                   setup_doc, NAVY, TEAL, GOLD, INK, GREY, WHITE,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY, FILL_NAVY, FILL_TEAL)
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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
    spacer(doc, 48)
    para(doc, "TOEFL HOUSE", size=14, bold=True, color=TEAL, align='c', space_after=4)
    para(doc, "GRAMMAR FOR", size=28, bold=True, color=NAVY, align='c', space_before=14, space_after=2)
    para(doc, "SPECIAL SPEAKING", size=28, bold=True, color=NAVY, align='c', space_before=0, space_after=8)
    para(doc, "A practical grammar course for accurate, natural, confident speech",
         size=13, italic=True, color=GREY, align='c', space_before=4, space_after=24)
    box(doc, None, [
        ("Learn the grammar. Use it in conversation. Make it part of your speech.", True),
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    spacer(doc, 36)
    para(doc, "A classroom and self-study course for real spoken communication", size=11.5, color=INK, align='c')
    para(doc, "16 lessons  ·  3 review tests  ·  final assessment  ·  5 reference appendices",
         size=10.5, color=GREY, align='c')
    page_break(doc)


def publication_info(doc):
    h_banner(doc, "COPYRIGHT AND PUBLICATION INFORMATION",
             sub="Grammar for Special Speaking — TOEFL HOUSE")
    para(doc, "© TOEFL HOUSE, 2026. All rights reserved.", size=11, bold=True, color=NAVY)
    para(doc, "Grammar for Special Speaking — a practical grammar course for accurate, natural, "
              "confident speech. Author and publisher: TOEFL HOUSE. Publication year: 2026.")
    para(doc, "No part of this publication may be reproduced, stored or transmitted in any form "
              "without prior written permission from the publisher, except for brief quotations "
              "used in teaching, review and private study.")
    para(doc, "", space_after=4)
    table(doc, ["Publication detail", "Information"], [
        ["Title", "Grammar for Special Speaking"],
        ["Author / creator", "TOEFL HOUSE"],
        ["Edition", "First Classroom Edition (2026)"],
        ["Companion volume", "Grammar for Special Speaking — Teacher's Book (TOEFL HOUSE)"],
        ["Language", "English"],
    ], widths=[2.0, 4.3], font_size=10)
    para(doc, "", space_after=4)
    para(doc, "Trademark notice", size=11, bold=True, color=NAVY)
    para(doc, "TOEFL® is a registered trademark of Educational Testing Service (ETS). This book is "
              "an independent educational resource prepared by TOEFL HOUSE; it is not affiliated with, "
              "authorised or endorsed by ETS. Any reference to speaking exams or academic tasks is for "
              "general language-learning purposes.")
    para(doc, "Where to find the answers", size=11, bold=True, color=NAVY, space_before=4)
    para(doc, "The complete answer key for learners appears in Appendix 5 at the back of this book. "
              "Instructors teaching with this course should use the companion Teacher's Book, which "
              "provides complete lesson procedures, answer notes, acceptable alternatives, model "
              "conversations, timing plans and classroom guidance.",
         size=10.5, italic=True, color=GREY)
    page_break(doc)


def introduction(doc):
    h_banner(doc, "INTRODUCTION", sub="Why knowing a rule on paper is different from owning it in speech")
    para(doc, "Most English learners have had the same frustrating experience. You study a grammar rule, "
              "you complete a page of exercises without a single mistake, and you feel ready. Then someone "
              "asks you an unexpected question in a real conversation — and in that split second, the rule "
              "disappears. You hesitate, translate in your head, or fall back on the same safe, simple "
              "sentences you were using two years ago.")
    para(doc, "That gap between what you recognize on paper and what you can say out loud is not a lack "
              "of intelligence or effort. It happens because most grammar books teach grammar as a set of "
              "abstract formulas for your eyes, whereas speaking requires fast, meaningful choices in your "
              "voice.")
    para(doc, "In real life, grammar is not decoration. It is how you signal what you mean. The difference "
              "between 'I lived in Herat for three years' and 'I have lived in Herat for three years' tells "
              "your listener whether you still live there today. The difference between 'You mustn't be late' "
              "and 'He can't be late' separates a strict rule from a logical guess. When you understand what "
              "a structure actually does for your listener, you stop memorizing charts and start making clear, "
              "confident choices.")
    para(doc, "This book is built around one simple habit: speak first, see the principle clearly, hear the "
              "difference, and immediately use the pattern in real conversation. Every small improvement in "
              "how you connect tenses, frame questions, compare ideas, or soften a claim compounds over time. "
              "Fix one recurring habit in each lesson, and within sixteen lessons your spoken English sounds "
              "noticeably clearer, more natural, and more persuasive.")
    para(doc, "By the end of this course, you will be able to:", size=11, bold=True, color=NAVY, space_before=4)
    for b in [
        "choose the right tense to describe habits, ongoing projects, past stories, and life changes;",
        "ask natural questions, soften polite requests, and keep a real conversation moving;",
        "express advice, certainty, possibilities, wishes, and regrets with the exact shade of meaning you intend;",
        "compare options persuadably and connect your ideas into clear, logical arguments;",
        "shift focus smoothly using the passive voice, causative patterns, relative clauses, and participles;",
        "report what others said accurately and control your tone with hedging and natural emphasis;",
        "catch and repair your own slips in the middle of a conversation without losing your flow.",
    ]:
        para(doc, f"•  {b}", indent=0.12)
    page_break(doc)


def how_to_use(doc):
    h_banner(doc, "HOW TO USE THIS BOOK", sub="A practical guide to turning grammar into automatic speech")
    para(doc, "Four habits that make this book work", size=12, bold=True, color=NAVY)
    para(doc, "1. Always speak before you read the rule.  Every lesson begins with The Speaking Hook — a "
              "short situation or question to discuss with a partner right away. Do not worry about perfection "
              "in those first two minutes. Speaking first wakes up your ear; when you read The Simple Rule "
              "a moment later, you will immediately recognize the exact tool you were just reaching for.")
    para(doc, "2. Read the side-by-side contrasts aloud.  In See the Difference, you will see pairs of "
              "sentences that look similar on the page but send very different messages in conversation. "
              "Say both sentences out loud and notice where your voice stresses the words. Your ear remembers "
              "contrasts far better than definitions.")
    para(doc, "3. Stretch your answers to match your voice.  Everyone in your class works through the same "
              "lessons and conversations together. In every speaking activity, start by making your core point "
              "clearly and accurately. Once that feels comfortable, push yourself one step further: add a "
              "concrete example, explain the reason behind your choice, address another point of view, or try "
              "one of the sharper patterns in Part 6 (Say It with Greater Precision).")
    para(doc, "4. Close the book for the final recall check.  At the end of every lesson, cover the page and "
              "answer the retrieval prompts out loud from memory. Calling a pattern up from memory without "
              "looking at the page is what moves grammar from short-term recognition into long-term speech.")
    para(doc, "", space_after=2)
    para(doc, "How each lesson moves from curiosity to confident speech", size=12, bold=True, color=NAVY)
    table(doc, ["Lesson step", "What you do", "Why it matters"], [
        [("Part 1 · The Speaking Hook", True),
         "Discuss a real-life situation or short contrast with a partner.",
         "Activates your own ideas so the grammar answers a real need."],
        [("Part 2 · The Simple Rule", True),
         "Learn how the pattern works through meaning and natural examples.",
         "Gives you a clear mental picture instead of a dry rule to memorize."],
        [("Part 3 · See the Difference", True),
         "Compare easily confused forms side by side in the same situation.",
         "Shows you how a small change in grammar changes what people hear."],
        [("Part 4 · Practice the Pattern", True),
         "Complete, repair, and transform sentences — saying each one aloud.",
         "Builds accuracy before you have to think on your feet."],
        [("Part 5 · Pair Speaking", True),
         "Use the grammar in a guided back-and-forth conversation.",
         "Turns controlled sentences into responsive dialogue."],
        [("Part 6 · Say It with Greater Precision", True),
         "Explore ways to add nuance, detail, and sharper focus to your ideas.",
         "Helps you express more sophisticated thoughts naturally."],
        [("Part 7 · Real Talk Challenge", True),
         "Plan briefly with keywords and speak for 1–2 minutes without notes.",
         "Builds real-world fluency and independence under time pressure."],
        [("Part 8 · Review and Self-Check", True),
         "Test your memory with the page covered and check your progress.",
         "Locks in the core insight and spots any habit that still needs attention."],
    ], widths=[1.95, 2.2, 2.15], font_size=9.5)
    page_break(doc)


def contents(doc):
    h_banner(doc, "CONTENTS", sub="Sixteen lessons in eight thematic parts")
    para(doc, "This is an automatic Word table of contents. It updates to show page numbers when opened "
              "in Word; if it has not refreshed, select it and choose Update Field / Update entire table.",
         size=10.5, italic=True, color=GREY)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = 4
    p.paragraph_format.space_after = 4
    begin_run = p.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    begin_run._r.append(fld_begin)
    instr_run = p.add_run()
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = ' TOC \\o "1-1" \\h \\z \\u '
    instr_run._r.append(instr)
    sep_run = p.add_run()
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    sep_run._r.append(separate)
    result = p.add_run("Update this field to populate the contents and page numbers.")
    result.font.italic = True
    result.font.color.rgb = GREY
    end_run = p.add_run()
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    end_run._r.append(fld_end)
    page_break(doc)


def diagnostic(doc, keys_registry):
    h_banner(doc, "DIAGNOSTIC TEST", sub="Find your starting point — 25 questions · no time limit")
    para(doc, "Complete this test before Lesson 1 without studying first: the purpose is simply to see which "
              "patterns already feel natural and which ones deserve extra attention. Mark your score out of 25 "
              "and keep your notes. This is a broad starting snapshot, not a parallel form of the 30-item "
              "Final Assessment; do not interpret the difference between their raw totals as a learning gain. "
              "For a direct before-and-after comparison, complete the speaking sample in Part D and score it "
              "with the same four-criterion rubric used at the end of the book.", size=10.5, italic=True, color=GREY)
    para(doc, "Part A — Tenses and time  (10 questions)", size=11, bold=True, color=NAVY)
    A = [
        "I __________ (see) that film last week.",
        "She __________ (work) here since 2021.",
        "While I __________ (cook — ongoing background), the phone rang.",
        "They __________ (work) there for ten years before they moved to Kabul.",
        "At sea level, pure water __________ (boil) at 100°C.",
        "They __________ (build) a new bridge when we visited.",
        "I __________ my keys — I can't get in.  (lose)",
        "Last summer we __________ (go) to Herat.",
        "How many books __________ you __________ (read) so far this month?",
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
        "The girl __________ helped me was very kind.  (who / that / whose / which)",
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
        "It __________ rain later — take an umbrella.  (may / might / could)",
        "I __________ my hair cut yesterday.  (had / got)",
    ]
    for i, q in enumerate(C, 21):
        para(doc, f"{i}.  {q}", indent=0.12)
    page_break(doc)
    para(doc, "Part D — Baseline speaking sample (not included in the 25-point written snapshot)",
         size=11, bold=True, color=NAVY)
    box(doc, "Speak for two minutes", [
        "Choose one topic. Prepare for two minutes, then speak for two minutes without reading a script:",
        "•  A decision that changed your life — and what you would do differently today.",
        "•  One change that would improve education or work in your country.",
        "•  A person who influenced you, and the advice they gave you.",
        "After your talk, a partner asks two follow-up questions. Answer them, then ask one relevant "
        "question in return. If you get stuck, repair and continue. Record the topic and, if possible, "
        "save an audio recording. At the end of the course, repeat this task under the same conditions. "
        "The Final Assessment uses the same task and four-criterion rubric so you can compare your baseline "
        "and final scores directly."
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    table(doc, ["Criterion", "4 — Strong", "3 — Good", "2 — Developing", "1 — Beginning"], [
        [("Grammatical accuracy", True), "structures are consistently accurate; occasional slips do not affect meaning", "generally accurate; some errors, meaning always clear", "frequent errors; meaning sometimes unclear", "errors dominate; meaning often unclear"],
        [("Appropriate structure selection", True), "wide range used naturally (tenses, conditionals, linkers, hedging…) for the intended meaning", "good range; choices usually match the meaning", "limited range; some structures forced or inappropriate", "basic structures only; frequent wrong choices"],
        [("Clarity", True), "ideas well organised and easy to follow; effective linking", "clear overall; some linking", "ideas loosely connected; hard to follow at times", "ideas listed without clear connection"],
        [("Successful communication", True), "message fully delivered; natural delivery, relevant follow-up exchange and self-repair", "message delivered; answers and asks relevant follow-ups, with some hesitation", "message partly delivered; responses are limited or pauses are long", "message largely not delivered; little response to questions"],
    ], widths=[1.35, 1.35, 1.25, 1.2, 1.15], font_size=8.5)
    para(doc, "Baseline speaking score: ____ / 16. Keep this page for your end-of-course comparison.",
         size=10.5, italic=True, color=GREY)
    para(doc, "When you finish, check your work in Appendix 5. The answer key is kept at the back of the book so you can complete the diagnostic first.",
         size=10.5, italic=True, color=GREY)
    keys_registry["Diagnostic"] = {
        "A": ["saw", "has worked / has been working", "was cooking", "had worked / had been working; 'worked' is also possible with before", "boils", "were building",
              "have lost", "went", "have read", "had already left"],
        "B": ["rains", "knew", "repairing / to be repaired", "was written", "leaving",
              "the station is", "who / that", "didn't smoke", "more intelligent", "did she finish"],
        "C": ["can't", "Despite", "where I lived / where I live (if still true)", "may / might / could", "had / got"],
    }
    para(doc, "What your snapshot means: 21–25 — strong foundation; pay special attention to nuance, register, "
              "and the precision patterns in Part 6 of each lesson.  15–20 — solid core; study the side-by-side "
              "contrasts in Part 3 carefully and speak every practice item aloud.  Below 15 — take your time with "
              "the core explanations in Part 2, repeat Practice A and B aloud, and build clean, accurate sentences "
              "first.", size=10.5, italic=True, color=GREY)
    page_break(doc)

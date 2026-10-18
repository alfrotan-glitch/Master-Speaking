# -*- coding: utf-8 -*-
"""Front matter for the Grammar for Special Speaking Teacher's Book."""
from style import (para, box, table, spacer, h_banner, page_break,
                   NAVY, TEAL, GOLD, INK, GREY,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY)
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def title_page(doc):
    spacer(doc, 48)
    para(doc, "TOEFL HOUSE", size=14, bold=True, color=TEAL, align='c', space_after=4)
    para(doc, "GRAMMAR FOR", size=28, bold=True, color=NAVY, align='c',
         space_before=14, space_after=2)
    para(doc, "SPECIAL SPEAKING", size=28, bold=True, color=NAVY, align='c',
         space_before=0, space_after=6)
    para(doc, "TEACHER'S BOOK", size=22, bold=True, color=GOLD, align='c',
         space_before=6, space_after=10)
    para(doc, "Lesson procedures, complete answer keys, model speaking responses, "
              "timing plans and mixed-classroom guidance for all sixteen lessons",
         size=12.5, italic=True, color=GREY, align='c', space_before=4, space_after=24)
    box(doc, None, [
        ("Companion to the Student Book: Grammar for Special Speaking", True),
        ("Learn the grammar. Use it in conversation. Make it part of your speech.", False),
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    spacer(doc, 36)
    para(doc, "For instructors of the Special Speaking classroom", size=11.5, color=INK, align='c')
    para(doc, "16 lesson guides  ·  3 review-test guides  ·  assessment keys  ·  classroom feedback guide",
         size=10.5, color=GREY, align='c')
    page_break(doc)


def publication_note(doc):
    h_banner(doc, "COPYRIGHT AND PUBLICATION INFORMATION",
             sub="Teacher's Book — Grammar for Special Speaking")
    para(doc, "© TOEFL HOUSE, 2026. All rights reserved.", size=11, bold=True, color=NAVY)
    para(doc, "This Teacher's Book is the companion volume to the Student Book "
              "Grammar for Special Speaking (author and publisher: TOEFL HOUSE; publication year "
              "2026). Full publication details and copyright notices printed on the Student Book's "
              "copyright page apply equally to this volume.")
    para(doc, "The lesson guides in this volume match the Student Book's sixteen lessons, practice "
              "items, answers, and model responses for classroom delivery. Assessment keys are provided "
              "in the back matter for instructors; they should not be distributed to learners before a "
              "test is completed.")
    para(doc, "TOEFL® is a registered trademark of Educational Testing Service (ETS). This book is "
              "an independent educational resource prepared by TOEFL HOUSE; it is not affiliated with, "
              "authorised or endorsed by ETS.")
    page_break(doc)


def introduction(doc):
    h_banner(doc, "INTRODUCTION", sub="Teaching one unified Special Speaking classroom")
    para(doc, "This Teacher's Book is designed so that you can walk into your Special Speaking "
              "classroom ready to run an engaging, clear, and productive lesson without having to "
              "invent missing explanations, answer keys, follow-up prompts, or timing plans.")
    para(doc, "In a real Special Speaking class, learners sit in the same room with a wide range of "
              "fluency and confidence — from solid intermediate speakers who still hesitate over "
              "tense choices or word order to more advanced speakers who are ready to refine their "
              "register, nuance, and rhetorical control. Rather than splitting the room into separate "
              "tracks or handing out different worksheets, the Student Book teaches the whole class "
              "through one shared learning journey. Every student participates in the same opening "
              "conversation, learns from the same clear explanation and side-by-side contrasts, and "
              "engages in the same pair and real-talk tasks.")
    para(doc, "Differentiation happens naturally through the richness of each student's spoken "
              "response and through how you guide them in the room. Each lesson guide in this book "
              "gives you concrete ways to support developing speakers (so they can participate "
              "accurately and confidently in the shared task) and ways to stretch stronger speakers "
              "(through deeper follow-up questions, added nuance, and the precision patterns in "
              "Part 6) without ever labeling or segregating learners.")
    para(doc, "Across all sixteen guides you will find: clear lesson objectives and observable "
              "success criteria; board and preparation notes; a practical 60-minute timing plan "
              "(plus a 45-minute adaptation); step-by-step guidance for all eight lesson parts; "
              "quick concept-check questions; complete Practice A and B answer keys with explanatory "
              "notes and acceptable alternatives; model pair exchanges and Real Talk responses; "
              "mixed-classroom support and extension strategies; targeted remedies for common "
              "misunderstandings; and fluency-protecting feedback routines.")
    page_break(doc)


def how_to_use(doc):
    h_banner(doc, "HOW TO USE THIS TEACHER'S BOOK", sub="A quick map of each lesson guide")
    para(doc, "What each lesson guide contains", size=12, bold=True, color=NAVY)
    table(doc, ["Section of each guide", "How it helps you in class"], [
        ["Lesson outcomes and observable success criteria",
         "Defines the communicative goal of the hour and what to listen for as evidence of learning"],
        ["Materials and board preparation",
         "Shows the simple board layout or timeline to set up before class begins"],
        ["Suggested timing (60-minute lesson)",
         "Allocates minutes across the eight lesson steps; every guide totals exactly 60 minutes"],
        ["Parts 1–8 (step-by-step teaching procedures)",
         "Follows the exact sequence of the Student Book with practical classroom instructions"],
        ["Check understanding",
         "Gives fast, interactive concept checks to confirm the rule landed before written practice"],
        ["Answer key and explanatory teaching notes",
         "Provides all Practice A/B answers (matching Student Book Appendix 5) plus why common traps occur"],
        ["Model exchange and model response",
         "Supplies natural conversational models for rehearsal and post-task comparison"],
        ["Supporting and stretching one mixed classroom",
         "Shows how to scaffold developing speakers and challenge stronger speakers within the same activity"],
        ["Common misunderstandings, 45-minute plan, and feedback",
         "Offers rapid board repairs, a shorter-session plan, and delayed error-correction guidance"],
    ], widths=[2.6, 3.7], font_size=9.5)
    para(doc, "Three habits of effective delivery", size=12, bold=True, color=NAVY, space_before=6)
    box(doc, "Before and during class", [
        "•  Let students speak first in Part 1 before you explain any grammar on the board — those first two minutes create curiosity for the rule.",
        "•  Keep everyone on the same task: use sentence starters or board prompts when a pair needs support, and ask 'Why?', 'Under what conditions?', or 'How could you say that more precisely?' when a pair finishes early.",
        "•  Protect spoken fluency during Parts 5 and 7: listen and note recurring slips quietly, then run a brisk three-minute board repair after everyone has finished speaking.",
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    page_break(doc)


def contents(doc):
    h_banner(doc, "CONTENTS", sub="Front matter, sixteen lesson guides, and assessment keys")
    para(doc, "This is an automatic Word table of contents. It updates to show page numbers when "
              "opened in Word; if it has not refreshed, select it and choose Update Field / Update "
              "entire table.", size=10.5, italic=True, color=GREY)
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
    end_run = p.add_run()
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    end_run._r.append(fld_end)
    page_break(doc)


def course_overview(doc, lessons, lesson_titles):
    h_banner(doc, "COURSE OVERVIEW", sub="The sixteen-lesson syllabus and assessment structure")
    para(doc, "The course comprises sixteen lessons arranged in eight thematic parts, progressing "
              "from core sentence and tense control to persuasive comparison, focus structures, "
              "and confident rhetorical style.")
    rows = []
    for L in lessons:
        rows.append([str(L["n"]), lesson_titles[L["n"]], f"Part {L['part_no']}", L["goal"]])
    table(doc, ["#", "Lesson", "Part", "Speaking goal"], rows,
          widths=[0.4, 2.1, 0.7, 3.1], font_size=9)
    para(doc, "Assessment architecture", size=12, bold=True, color=NAVY, space_before=6)
    _bullets = [
        "Diagnostic Test (25 written items + matched baseline speaking sample) — before Lesson 1.",
        "Review Test 1 after Lesson 4 (Lessons 1–4); Review Test 2 after Lesson 8 (Lessons 1–8); "
        "Review Test 3 after Lesson 12 (Lessons 1–12). Each review test assesses only taught material.",
        "Final Assessment after Lesson 16: 30 written items sampling all lessons, plus the matched "
        "two-minute speaking task and four-criterion rubric.",
        "Five student reference appendices: Grammar Formula Book, Common Errors Guide, Essential "
        "Sentence Patterns, Can-Do Tracker, and the Complete Answer Key (Appendix 5).",
    ]
    for b in _bullets:
        para(doc, f"•  {b}", indent=0.12)
    page_break(doc)


def teaching_principles(doc):
    h_banner(doc, "TEACHING PRINCIPLES", sub="Eight habits that make grammar stick in conversation")
    principles = [
        ("1. Situation and meaning before terminology.",
         "Begin every lesson with a concrete human situation and let learners talk in Part 1 before "
         "introducing any rule. When a grammatical term is needed, explain what it means in everyday English."),
        ("2. Keep explanation brisk; give the hour to speaking.",
         "Parts 1–3 should take roughly 15 minutes in total. The remaining 45 minutes belong to active "
         "practice, pair conversation, precision building, and the unscripted Real Talk Challenge."),
        ("3. Teach contrasts side by side in the same context.",
         "Students rarely understand a structure in isolation. Show how changing 'I lived' to 'I have lived' "
         "or 'mustn't' to 'can't' changes the real-world message in the listener's mind."),
        ("4. One classroom, open-ended depth.",
         "Never split the room into separate tracks. Give the whole class the same communicative task; "
         "help hesitant speakers land a clear, accurate core answer while prompting confident speakers "
         "to elaborate with reasons, stories, concessions, and the precision patterns in Part 6."),
        ("5. Models are inspiration, not scripts to memorize.",
         "Have learners attempt the speaking task first before uncovering the printed Model Response. "
         "Then ask them to notice one useful phrase or connection in the model and try a second round."),
        ("6. Correct without interrupting communication.",
         "During pair work and Real Talk, listen with the printed criteria and jot down two or three "
         "anonymous sentences on a notepad. Put them on the board after the timer ends so the whole "
         "class can repair them together."),
        ("7. Honour legitimate grammatical alternatives.",
         "English often allows more than one natural form depending on the speaker's focus (for instance, "
         "present perfect simple vs continuous, or 'may / might / could' for possibility). Credit every "
         "accurate option noted in the key."),
        ("8. Close every lesson with active recall.",
         "In the final five minutes, ask students to close their books and produce the target patterns "
         "from memory. Retrieval without looking at the page is what builds real-time fluency."),
    ]
    for title, text in principles:
        box(doc, title, [text], fill=FILL_BOX_GREY, label_color=GOLD)
    page_break(doc)


def pacing_and_feedback(doc):
    h_banner(doc, "PACING AND FEEDBACK", sub="Managing a 60-minute or 45-minute Special Speaking class")
    para(doc, "Every lesson guide in this book is paced for a standard 60-minute class session, "
              "grouped into five clear teaching blocks:")
    table(doc, ["Teaching block", "Minutes", "Lesson parts covered"], [
        ["Opening, explanation, and contrast", "15", "Part 1 (Speaking Hook) + Part 2 (Simple Rule) + Part 3 (See the Difference)"],
        ["Controlled oral and written practice", "10", "Part 4 (Practice the Pattern A & B)"],
        ["Interactive speaking and precision", "20", "Part 5 (Pair Speaking) + Part 6 (Say It with Greater Precision)"],
        ["Independent transfer challenge", "10", "Part 7 (Real Talk Challenge + model comparison)"],
        ["Active recall and feedback", "5", "Part 8 (Review and Self-Check) + board repair"],
        [("Total", True), ("60", True), ("", False)],
    ], widths=[2.3, 0.8, 3.2], font_size=9.5)
    para(doc, "Adapting to different class schedules", size=12, bold=True, color=NAVY, space_before=6)
    for b in [
        "45-minute session: follow the 'Shorter-session adaptation' box in each lesson guide — keep the "
        "15-minute explanation and 10-minute practice intact, run a focused 12-minute Pair Speaking + "
        "precision round, a 5-minute Real Talk sprint, and a 3-minute recall check.",
        "90-minute session: run the full 60-minute plan, then have students switch partners and repeat "
        "the Real Talk Challenge on a second topic, incorporating feedback from the first round.",
    ]:
        para(doc, f"•  {b}", indent=0.12)
    para(doc, "Fluency-protecting feedback routine", size=12, bold=True, color=NAVY, space_before=6)
    box(doc, "While students are speaking — listen and note", [
        "•  Circulate quietly with the lesson's success criteria; never interrupt a speaker mid-thought to fix a grammar slip.",
        "•  Write down two strong sentences you hear and two recurring errors on your notepad (without student names).",
        "•  If a pair stalls, join briefly as a curious listener and ask one natural follow-up question to restart the flow.",
    ], fill=FILL_BOX_TEAL, label_color=TEAL)
    box(doc, "After the speaking round — repair in three minutes", [
        "•  Start by praising one specific communicative success and one strong sentence from the room.",
        "•  Write the two anonymous error sentences on the board and invite pairs to spot and repair the pattern in 30 seconds.",
        "•  Have the whole class say the repaired sentences aloud once so the natural rhythm lands in everyone's ear.",
    ], fill=FILL_BOX_GREY, label_color=GOLD)
    # Note: render_teacher_lesson begins with page_break(doc), so we do not add a duplicate page_break here.


def assessment_guidance(doc, keys_registry, model_final_speech):
    page_break(doc)
    h_banner(doc, "ASSESSMENT GUIDANCE", sub="Keys, acceptable alternatives, and scoring spoken progress")
    para(doc, "How the assessments work together", size=12, bold=True, color=NAVY)
    for b in [
        "Lesson Practice A and B keys: printed inside every lesson guide (and in Student Book Appendix 5).",
        "Diagnostic Test, Review Tests 1–3, and Final Assessment keys: printed below for instructor reference.",
        "Open-ended speaking tasks: evaluate using the lesson's observable criteria and the four-criterion "
        "speaking rubric (Grammatical accuracy · Appropriate structure selection · Clarity · Successful "
        "communication; 1–4 points each, total 16).",
    ]:
        para(doc, f"•  {b}", indent=0.12)
    para(doc, "Fair marking principles", size=12, bold=True, color=NAVY, space_before=6)
    for b in [
        "Credit every grammatical alternative listed in the key (and any other natural form that accurately "
        "fulfils the prompt and context).",
        "For sentence transformations and open prompts, judge whether the target structure and meaning are "
        "accurate rather than requiring identical wording.",
        "Do not compare the 25-item Diagnostic raw score with the 30-item Final Assessment raw score as a "
        "numerical gain claim — the two written tests have different lengths and blueprints. Instead, compare "
        "learners' baseline and final speaking scores across the four rubric criteria under identical task conditions.",
    ]:
        para(doc, f"•  {b}", indent=0.12)
    para(doc, "Model final speaking response (one strong example, not a script)", size=12,
         bold=True, color=NAVY, space_before=6)
    box(doc, "Approximately two minutes, delivered without reading", [model_final_speech],
        fill=FILL_BOX_GOLD, label_color=GOLD)
    para(doc, "Use this sample to calibrate rubric scoring with colleagues: identify how the speaker "
              "combines narrative tenses, conditionals, passives, relative clauses, hedging, and cleft "
              "focus, and remember that any student response that meets the four criteria in the student's "
              "own voice deserves full marks.",
         size=10.5, italic=True, color=GREY)
    para(doc, "Keys — Diagnostic Test and Review Tests", size=12, bold=True, color=NAVY,
         space_before=8)
    for name in ["Diagnostic", "Review Test 1", "Review Test 2", "Review Test 3"]:
        ans = keys_registry.get(name)
        if not ans:
            continue
        para(doc, name, size=11, bold=True, color=TEAL, space_before=4, keep_with_next=True)
        lines = []
        for part in ("A", "B", "C"):
            if ans.get(part):
                lines.append(f"{part}.  " + "  ·  ".join(f"{i + 1}. {a}" for i, a in enumerate(ans[part])))
        box(doc, None, lines, fill=FILL_BOX_GREY, label_color=NAVY)
    para(doc, "Key — Final Assessment (30 items)", size=12, bold=True, color=NAVY, space_before=8, keep_with_next=True)
    ans = keys_registry.get("Final Assessment")
    if ans:
        lines = []
        for part in ("A", "B", "C"):
            if ans.get(part):
                lines.append(f"{part}.  " + "  ·  ".join(f"{i + 1}. {a}" for i, a in enumerate(ans[part])))
        box(doc, None, lines, fill=FILL_BOX_GREY, label_color=NAVY)
    para(doc, "Explanatory notes on key test items", size=12, bold=True, color=NAVY, space_before=6, keep_with_next=True)
    for b in [
        "Review Test 1 A4 ('is studying'): 'these days' frames an ongoing current project; past simple would clash with the time cue.",
        "Review Test 1 B1 ('must') vs B4 ('don't have to / needn't'): B1 expresses a legal requirement, whereas B4 expresses absence of obligation (not 'mustn't', which means forbidden).",
        "Review Test 2 B1: credit both 'Despite the exam being hard, everyone passed' and 'Despite the difficulty, everyone passed' — both avoid attaching 'being hard' to 'everyone'.",
        "Review Test 3 A3 ('to speak'): passive reporting structure from Lesson 9 ('She is said to speak five languages').",
        "Final Assessment A1: credit 'have lived', ''ve lived', and 'have been living' — all three accurately express a situation continuing up to now with 'since 2020'.",
        "Final Assessment C3 & C4: credit any well-formed hedge ('may well', 'probably', 'tends to', 'is likely to') on C3 and any accurate degree modifier + comparative + reason on C4.",
        "Diagnostic Test: credit all listed alternatives ('has worked / has been working', 'who / that', 'may / might / could', 'had / got').",
    ]:
        para(doc, f"•  {b}", indent=0.12)

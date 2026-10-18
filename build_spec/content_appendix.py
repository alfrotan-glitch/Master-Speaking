# -*- coding: utf-8 -*-
"""Appendices 1-5: Formula Book · Common Errors · Sentence Patterns · Can-Do Tracker · Complete Answer Key."""
from style import (para, run, box, table, spacer, h_banner, page_break,
                   NAVY, TEAL, GOLD, INK, GREY,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY)
from content_front import LESSON_TITLES

FORMULA_CARDS = [
    (1, "Tenses for Real Communication",
     ["Present simple = facts & habits  ·  Present continuous = around now",
      "Past simple = finished time  ·  Present perfect = connected to now",
      "going to = plan  ·  will = decision/prediction  ·  present continuous = arrangement"]),
    (2, "Telling Stories",
     ["Past continuous = the scene  ·  past simple = the events  ·  past perfect = the earlier past",
      "when + past simple  ·  while + past continuous  ·  by the time + past perfect before past simple",
      "Shape: background → events (First… Then…) → ending/reflection"]),
    (3, "Questions and Follow-ups",
     ["Wh- + auxiliary + subject + verb  ·  Yes/No: auxiliary + subject + verb",
      "Indirect: question word + subject + verb (no inversion) — 'Do you know where the bank is?'",
      "Follow-ups keep conversations alive: 'Really? What happened next? How about you?'"]),
    (4, "Modal Verbs",
     ["Modal + base verb: can/could = ability · may/could = permission · must/have to = obligation · should = advice · might = possibility",
      "must be = certainly (positive) · might be = possible · can't be = certainly not",
      "mustn't = prohibition ≠ can't (deduction)  ·  Would you mind + -ing?"]),
    (5, "Conditionals",
     ["Zero: If + present, present  ·  First: If + present, will + verb",
      "Second: If + past, would + verb  ·  Third: If + past perfect, would have + participle",
      "Mixed: If + past perfect, would + verb  ·  unless = if not  ·  no 'will' in if-clauses"]),
    (6, "Wishes and Regrets",
     ["wish + past simple = present wish  ·  wish + past perfect = past regret",
      "wish + would = complaint/request  ·  If only…! = strong emotion",
      "would rather + base (me) / + past (someone else)  ·  It's (high) time + past"]),
    (7, "Comparisons",
     ["comparative + than (two)  ·  the superlative (three+)  ·  as + adj + as",
      "the + comparative, the + comparative  ·  comparative + and + comparative",
      "far / much / slightly / by far + comparison  ·  comparisons persuade with reasons"]),
    (8, "Linking and Arguments",
     ["although + clause  ·  despite / in spite of + noun or -ing  ·  however = new sentence",
      "because + clause  ·  because of + noun  ·  therefore / as a result = consequence",
      "Argument skeleton: POINT → REASON → EXAMPLE → SUMMARY"]),
    (9, "Passive Voice",
     ["be + past participle (tense lives in 'be'): is done · was done · will be done · has been done · must be done",
      "Use: result matters · doer unknown/obvious/general · objective tone",
      "It is said that … = He is said to …"]),
    (10, "Causative Structures",
     ["have/get + object + participle = arrange a service (or: something happened to me)",
      "make + person + base (force) · let + base (allow) · have + base (instruct) · get + to (persuade)",
      "'get' keeps 'to' — the other three don't."]),
    (11, "Gerunds and Infinitives",
     ["enjoy/avoid/mind/suggest/keep + -ing  ·  decide/hope/plan/promise/refuse + to",
      "remember/forget/stop/try: -ing = earlier action · to = later action",
      "Preposition + -ing — including 'to' in look forward to / be used to"]),
    (12, "Relative Clauses",
     ["who (people) · which (things) · that (both) · whose · where — object pronouns can drop",
      "Defining = no commas (identifies)  ·  Non-defining = commas (extra detail, no 'that')",
      "Reduced: 'the man (who is) standing there' — only drop who is / which was"]),
    (13, "Reported Speech",
     ["Backshift one tense: present → past → past perfect · will → would · can → could",
      "ask + if/whether or question word + statement order  ·  told/asked + person + to",
      "say (+ that) vs tell (+ person)  ·  time words shift: tomorrow → the next day"]),
    (14, "Participles",
     ["-ing adjective = causes feeling  ·  -ed adjective = feels it (boring lecture / bored class)",
      "Participle clause: 'Having finished, she left.' — subject must match the main clause",
      "Frames: Given… / Considering… / With + noun + -ing"]),
    (15, "Hedging, Emphasis, Inversion",
     ["Hedge: may well / might / tend to / it could be argued that …",
      "Cleft: It was X that … / What I need is …  ·  do-emphasis: 'I do believe…'",
      "Inversion after negative openers: Never have I… / Not only did… / Only then did…"]),
    (16, "Grammar in Real Conversation",
     ["Four jobs: TIME (tenses, reported) · CHOICE (modals, conditionals, wishes) · SHAPE (questions, linkers, relatives, passives) · STYLE (comparison, hedging, emphasis)",
      "Think meaning → choose structure → say it whole",
      "Accuracy first, then range; repair and continue: 'What I mean is…'"]),
]

ERRORS = [
    ("I have seen him yesterday.", "I saw him yesterday.", "finished time needs past simple"),
    ("I am knowing the answer.", "I know the answer.", "state verbs take simple forms"),
    ("She is more taller than me.", "She is taller than me.", "no double comparatives"),
    ("This is better then that.", "This is better than that.", "than (comparison) not then (time)"),
    ("If it will rain, we'll stay.", "If it rains, we'll stay.", "no 'will' in if-clauses"),
    ("If I would have known…", "If I had known…", "third conditional: if + past perfect"),
    ("I wish I have more time.", "I wish I had more time.", "wish + past for unreal present"),
    ("I'd rather you don't smoke.", "I'd rather you didn't smoke.", "would rather + subject + past"),
    ("It's time we will go.", "It's time we went.", "it's time + past (already late)"),
    ("Despite of the cost…", "Despite the cost… / In spite of the cost…", "no 'despite of'"),
    ("Although the cost, we bought it.", "Despite the cost, we bought it.", "although + clause; despite + noun"),
    ("Do you know where is the bank?", "Do you know where the bank is?", "indirect questions use statement order"),
    ("Did she called you?", "Did she call you?", "base verb after did"),
    ("He said me that he was tired.", "He told me that he was tired.", "tell + person; say + that"),
    ("She suggested me to wait.", "She suggested waiting.", "suggest + -ing (or that + clause)"),
    ("I look forward to meet you.", "I look forward to meeting you.", "'to' here is a preposition"),
    ("I enjoy to read.", "I enjoy reading.", "enjoy + -ing"),
    ("He made me to wait.", "He made me wait.", "make + person + base verb"),
    ("I will get my car to repair.", "I will get my car repaired.", "have/get + object + participle"),
    ("The house was builted in 1990.", "The house was built in 1990.", "past participle of build = built"),
    ("My phone was stolen by me.", "I lost my phone.", "active is clearer for your own actions"),
    ("The book what I read…", "The book (that) I read…", "no 'what' as a relative pronoun"),
    ("My mother, that lives…", "My mother, who lives…", "'that' is not used after commas"),
    ("Never I have seen such a mess.", "Never have I seen such a mess.", "inversion after negative openers"),
    ("He mustn't be at home.", "He can't be at home.", "can't = deduction; mustn't = prohibition"),
    ("Would you mind to open the window?", "Would you mind opening the window?", "mind + -ing"),
    ("I am very interesting in history.", "I am very interested in history.", "-ed = feels; -ing = causes"),
    ("Opening the window, the room was cold.", "Opening the window, I felt the cold.", "participle subject must match"),
    ("He denied to break it.", "He denied breaking it.", "deny + -ing"),
    ("Unless you don't hurry…", "Unless you hurry…", "'unless' already means 'if not'"),
]

PATTERNS = [
    ("Experience", "I have (never) …  ·  One experience that changed me was …"),
    ("Story", "First … Then … After that … Suddenly … Finally …"),
    ("Opinion", "I believe that … because …  ·  From my point of view …"),
    ("Reason", "This is mainly because …  ·  The main reason is that …"),
    ("Example", "For instance …  ·  A good example of this is …"),
    ("Contrast", "Although …, …  ·  Despite + noun/-ing …  ·  On the other hand …"),
    ("Concession", "It is true that …; nevertheless …  ·  Admittedly …; even so …"),
    ("Result", "As a result …  ·  This means that …  ·  Consequently …"),
    ("Hedged claim", "It could be argued that …  ·  … may well …  ·  … tend(s) to …"),
    ("Emphasis", "It is … that …  ·  What I mean is …  ·  I do believe …"),
    ("Advice", "If I were you, I'd …  ·  You might want to …  ·  It might be worth …"),
    ("Regret", "I wish I had …  ·  If only I had …  ·  What I should have done was …"),
    ("Preference", "I'd rather … than …  ·  I prefer … to …  ·  If I had to choose, I'd …"),
    ("Prediction", "In the future, … will probably …  ·  … is likely to …"),
    ("Polite request", "Would you mind …-ing?  ·  Could I possibly …?  ·  I was wondering if …"),
    ("Reporting", "He said (that) …  ·  She pointed out that …  ·  They warned me not to …"),
    ("Description", "…, who/which …  ·  The person who …  ·  …, which means that …"),
    ("Comparison", "… is far more … than …  ·  The more …, the more …  ·  … is by far the most …"),
    ("Process", "First, … is done; then … is …  ·  Having been …, …  ·  … is then …"),
    ("Summary", "To sum up …  ·  All in all …  ·  The point I want to make is …"),
    ("Self-repair", "What I mean is …  ·  Let me rephrase that …  ·  Or rather …"),
    ("Ending", "That's why …  ·  This taught me that …  ·  Looking ahead, I plan to …"),
]

CANDO = [
    (1, "I can talk about habits, current situations and past experiences accurately."),
    (2, "I can tell a story with background, clear sequence and a meaningful ending."),
    (3, "I can ask polite questions and keep a conversation going with follow-ups."),
    (4, "I can give advice, express obligation and show degrees of certainty with the right modal."),
    (5, "I can discuss real possibilities, imaginary situations and unreal pasts."),
    (6, "I can express wishes, regrets and preferences naturally."),
    (7, "I can compare options and support my comparisons with reasons."),
    (8, "I can link ideas and build a short argument with a clear skeleton."),
    (9, "I can choose active or passive for the right focus in reports and descriptions."),
    (10, "I can talk about services, arrangements and influence using causatives."),
    (11, "I can use gerund and infinitive patterns accurately, including meaning changes."),
    (12, "I can describe people and places precisely with defining and non-defining clauses."),
    (13, "I can report statements, questions and commands with accurate backshift."),
    (14, "I can compress ideas with participles without losing clarity."),
    (15, "I can control certainty, emphasis and formality in formal speech."),
    (16, "I can use the course grammar together in free, confident conversation."),
]


def render_all(doc, keys_registry):
    # ---- Appendix 1: Formula Book ----
    page_break(doc)
    h_banner(doc, "APPENDIX 1  ·  GRAMMAR FORMULA BOOK",
             sub="Sixteen cards — one per lesson. Review with this book closed first.")
    for n, title, lines in FORMULA_CARDS:
        box(doc, f"Card {n} — {title}", lines, fill=FILL_BOX_GREY, label_color=GOLD, formula=True)

    # ---- Appendix 2: Common Errors ----
    page_break(doc)
    h_banner(doc, "APPENDIX 2  ·  COMMON ERRORS AND CORRECTIONS GUIDE",
             sub="Thirty errors that mark learners — and the fix for each")
    table(doc, ["✗ Error", "✓ Correction", "Why"], ERRORS, widths=[2.1, 2.3, 1.9], font_size=9.5)

    # ---- Appendix 3: Sentence Patterns ----
    page_break(doc)
    h_banner(doc, "APPENDIX 3  ·  ESSENTIAL SENTENCE PATTERNS FOR SPEAKING",
             sub="Build answers from these skeletons until they are automatic")
    table(doc, ["Function", "Patterns"], PATTERNS, widths=[1.4, 4.9], font_size=10)

    # ---- Appendix 4: Can-Do Tracker ----
    page_break(doc)
    h_banner(doc, "APPENDIX 4  ·  SPEAKING SELF-ASSESSMENT AND CAN-DO TRACKER",
             sub="Tick honestly:  ✓ = I can do this in speech  ·  ~ = almost  ·  ✗ = not yet")
    rows = [[f"Lesson {n}", stmt, "", ""] for n, stmt in CANDO]
    table(doc, ["Lesson", "Can-do statement", "Before the course", "After Lesson 16"],
          rows, widths=[0.8, 3.6, 1.0, 1.0], font_size=9.5)
    para(doc, "Speaking self-assessment", size=11, bold=True, color=NAVY)
    para(doc, "Record yourself for two minutes (any topic) and rate yourself with the Final Assessment "
              "rubric. Repeat after one month and compare the recordings — that is your true progress.",
         size=10.5, italic=True, color=GREY)

    # ---- Appendix 5: Complete Answer Key ----
    page_break(doc)
    h_banner(doc, "APPENDIX 5  ·  COMPLETE ANSWER KEY",
             sub="All exercises, review tests and the final assessment")
    para(doc, "Alternative answers are accepted where the exercise allows them. Speaking tasks are "
              "evaluated with the success criteria and rubric — not with rigid model answers.",
         size=10.5, italic=True, color=GREY)
    for name in ["Diagnostic"] + [f"Lesson {i}" for i in range(1, 17)] \
            + ["Review Test 1", "Review Test 2", "Review Test 3", "Final Assessment"]:
        ans = keys_registry.get(name)
        if not ans:
            continue
        para(doc, name, size=11, bold=True, color=NAVY, space_before=6)
        if name == "Diagnostic":
            lines = ["A.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['A'])),
                     "B.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['B'])),
                     "C.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['C']))]
        elif name.startswith("Lesson"):
            lines = []
            if ans.get('A'):
                lines.append("Practice A.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['A'])))
            if ans.get('B'):
                lines.append("Practice B.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['B'])))
        else:
            lines = ["A.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['A'])),
                     "B.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['B'])),
                     "C.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(ans['C']))]
        box(doc, None, lines, fill=FILL_BOX_GREY, label_color=NAVY)

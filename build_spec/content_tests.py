# -*- coding: utf-8 -*-
"""Review Tests 1-3 (cumulative) + Final Assessment (grammar + speaking rubric + error plan)."""
from style import (para, run, box, table, spacer, h_banner, page_break,
                   NAVY, TEAL, GOLD, INK, GREY,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY)


def _qblock(doc, title, items, start=1):
    para(doc, title, size=11, bold=True, color=NAVY)
    for i, q in enumerate(items, start):
        para(doc, f"{i}.  {q}", indent=0.12)


def review_test(doc, num, after, keys_registry):
    page_break(doc)
    h_banner(doc, f"REVIEW TEST {num}",
             sub=f"Cumulative review — Lessons 1–{after}  ·  15 questions  ·  suggested time: 20 minutes")
    if num == 1:
        A = [
            "I __________ (not/see) him since Monday.",
            "While we __________ (wait), the announcement came.",
            "Water __________ (freeze) at 0°C.",
            "She __________ (study) medicine these days.",
            "By the time we arrived, the guests __________ (eat) everything.",
            "Look at the sky — it __________ (rain).",
            "How long __________ you __________ (know) Nadia?",
            "He said he __________ (be) busy that day.",
        ]
        B = [
            "If I __________ (be) you, I would apply for the visa.",
            "__________ you mind __________ (close) the door?",
            "Do you know where the post office __________ ?  (be)",
            "Despite __________ (be) very tired, she finished the work.",
        ]
        C = [
            "Rewrite as a second conditional: 'I don't have time, so I can't help.'",
            "Report: 'Where did you park?' She asked me __________.",
            "Give a deduction: You see a colleague carrying a tennis racket. 'You __________ (be) on your way to a game.'",
        ]
        key = {
            'A': ["haven't seen", "were waiting", "freezes", "is studying", "had eaten",
                  "is going to rain / will rain", "have / known", "was"],
            'B': ["were", "Would / closing", "is", "being"],
            'C': ["If I had time, I would help. / If I had more time, I could help.",
                  "where I had parked", "must be"],
        }
    elif num == 2:
        A = [
            "If I __________ (know) his number, I would call him now.",
            "I wish I __________ (take) that opportunity last year.",
            "This method is __________ (effective) than the old one.",
            "Not until midnight __________ (the team / finish).",
            "The letter __________ (write) by the manager yesterday.",
            "He avoided __________ (answer) the direct question.",
            "The results, __________ were published today, surprised everyone.  (which / that)",
            "She promised __________ (call) back before noon.",
        ]
        B = [
            "Combine with despite: 'The exam was hard. Everyone passed.'",
            "Rewrite with causative: 'A professional painted my flat last week.'",
            "Hedge the claim: 'This plan will solve the problem.'",
            "Report the order: 'Don't be late,' the teacher said.  (The teacher warned…)",
        ]
        C = [
            "Make a cleft sentence (focus the price): 'The price changed my mind.'",
            "Compare with a reason: 'This course is better than that one.'  (use far + reason)",
            "Correct and explain: 'I look forward to hear from you.'",
        ]
        key = {
            'A': ["knew", "had taken", "more effective", "did the team finish", "was written",
                  "answering", "which", "to call"],
            'B': ["Despite being hard, everyone passed the exam. / Despite the difficulty, everyone passed.",
                  "I had my flat painted last week.",
                  "This plan may well solve the problem. / This plan will probably solve the problem. (answers vary)",
                  "The teacher warned us not to be late."],
            'C': ["It was the price that changed my mind.",
                  "answers vary — far + comparative + reason",
                  "I look forward to hearing from you. ('to' here is a preposition)"],
        }
    else:
        A = [
            "The house __________ (build) in the 1960s.",
            "I had my watch __________ (repair) last week.",
            "She is said __________ (speak) five languages.",
            "He avoided __________ (make) the same mistake twice.",
            "This is the café __________ we first met.",
            "__________ (finish) the report, she sent it to the board.",
            "I'd rather you __________ (not/mention) this to anyone.",
            "It's high time we __________ (make) a decision.",
        ]
        B = [
            "Report: 'I never lie.'  (He denied…)  — use deny + -ing.",
            "Rewrite with inversion: 'I have never heard such a strange story.'",
            "Combine with a participle: 'Because she had not been warned, she was surprised.'",
            "Make it formal and passive: 'People believe that the economy is improving.'",
        ]
        C = [
            "Hedge formally: 'This is the only solution.'  (use 'it could be argued')",
            "Report a question in correct order: 'When will the office close?'  (She asked me…)",
            "Use 'the more…the more' about practice and confidence.",
            "Fix: 'Never I have seen such a mess.'",
        ]
        key = {
            'A': ["was built", "repaired", "to speak", "making", "where", "Having finished",
                  "didn't mention", "made"],
            'B': ["He denied making the same mistake… / He denied ever lying. (per item)",
                  "Never have I heard such a strange story.",
                  "Not having been warned, she was surprised.",
                  "It is believed that the economy is improving. / The economy is believed to be improving."],
            'C': ["It could be argued that this is the only solution. (answers vary)",
                  "She asked me when the office would close.",
                  "The more you practise, the more confident you become. (answers vary)",
                  "Never have I seen such a mess."],
        }

    _qblock(doc, "Part A — Complete the sentences.", A)
    _qblock(doc, "Part B — Rewrite, combine or transform.", B)
    _qblock(doc, "Part C — Use and communication.", C)
    box(doc, "Answer key", [
        "A.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['A'])),
        "B.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['B'])),
        "C.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['C'])),
    ], fill=FILL_BOX_GREY, label_color=NAVY)
    keys_registry[f"Review Test {num}"] = key


def final_assessment(doc, keys_registry):
    page_break(doc)
    h_banner(doc, "FINAL ASSESSMENT", sub="Part 1: Grammar knowledge  ·  Part 2: Independent speaking task")
    para(doc, "Part 1 — Grammar knowledge  (30 questions · suggested time: 35 minutes)",
         size=12, bold=True, color=NAVY)
    para(doc, "Section A — Complete the sentences.  (12 questions)", size=11, bold=True, color=TEAL)
    A = [
        "I __________ (live) here since 2020.",
        "When I got home, my family __________ (already / have) dinner.",
        "If it __________ (be) sunny tomorrow, we'll go to the lake.",
        "I wish I __________ (not/say) that yesterday.",
        "The meeting __________ (cancel) yesterday afternoon.",
        "You look exhausted — you __________ (must / work) all night.  (past deduction)",
        "She avoided __________ (make) any promises.",
        "The teacher made us __________ (rewrite) the essay.",
        "This is the most __________ (challenge) course I've ever taken.",
        "__________ (warn) about the storm, the fishermen stayed ashore.",
        "He suggested __________ (leave) before the traffic.",
        "Not only __________ (she / apologise), but she also offered a refund.",
    ]
    for i, q in enumerate(A, 1):
        para(doc, f"{i}.  {q}", indent=0.12)
    para(doc, "Section B — Rewrite or transform.  (10 questions)", size=11, bold=True, color=TEAL)
    B = [
        "Report: 'I'll help you tomorrow,' he said.",
        "Report: 'Where did you buy it?'  (She asked me…)",
        "Polite question: 'When does the shop close?'",
        "Third conditional: 'He didn't revise, so he failed.'",
        "Passive (formal): 'Someone has stolen the documents.'",
        "Cleft (focus the manager): 'The manager approved the plan.'",
        "Causative: 'I paid someone to fix the roof.'",
        "Inversion: 'She had rarely felt so confident.'",
        "Combine with although: 'The task was difficult. They finished it.'",
        "Combine with a participle: 'Because he had studied hard, he passed easily.'",
    ]
    for i, q in enumerate(B, 13):
        para(doc, f"{i}.  {q}", indent=0.12)
    para(doc, "Section C — Use and communication.  (8 questions)", size=11, bold=True, color=TEAL)
    C = [
        "Choose: He (mustn't / can't) be at home — his car is gone.",
        "Complete with a linker: __________ being expensive, the course is worth it.",
        "Hedge the claim: 'This method is the best.'  (may well / probably)",
        "Compare with nuance: 'Option A is better than Option B.'  (use far + give a reason frame)",
        "Correct: 'Despite of the delay, we left on time.'",
        "Complete: The more you practise, the __________ (confident) you become.",
        "Report advice: 'You should apply early,' she said.  (She advised…)",
        "Complete with the right pattern: I look forward to __________ (meet) you.",
    ]
    for i, q in enumerate(C, 23):
        para(doc, f"{i}.  {q}", indent=0.12)
    key = {
        'A': ["have lived / 've lived", "had already had", "is", "hadn't said", "was cancelled",
              "must have been working", "making", "rewrite", "challenging", "Having been warned",
              "leaving", "did she apologise"],
        'B': ["He said he would help me the next day.",
              "She asked me where I had bought it.",
              "Could you tell me when the shop closes?",
              "If he had revised, he wouldn't have failed.",
              "The documents have been stolen.",
              "It was the manager who approved the plan.",
              "I had the roof fixed.",
              "Rarely had she felt so confident.",
              "Although the task was difficult, they finished it.",
              "Having studied hard, he passed easily."],
        'C': ["can't", "Despite", "This method may well be the best. / This method is probably the best. (answers vary)",
              "Option A is far better than Option B because… (answers vary)",
              "Despite the delay, we left on time.",
              "more confident", "She advised me to apply early.", "meeting"],
    }
    box(doc, "Answer key — Final Assessment", [
        "A.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['A'])),
        "B.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['B'])),
        "C.  " + "  ·  ".join(f"{i+1} {a}" for i, a in enumerate(key['C'])),
    ], fill=FILL_BOX_GREY, label_color=NAVY)
    keys_registry["Final Assessment"] = key
    para(doc, "Accept alternative answers where the exercise allows them (e.g. 'may well' / 'probably' / "
              "'is likely to' for hedging). Compare this score with your Diagnostic Test score — "
              "the difference is your progress.", size=10.5, italic=True, color=GREY)

    page_break(doc)
    h_banner(doc, "FINAL ASSESSMENT — PART 2", sub="Independent speaking task and evaluation")
    box(doc, "Speaking task (2 minutes to prepare · 2 minutes to speak)",
        ["Speak on ONE of the following topics:",
         "•  A decision that changed your life — and what you would do differently today.",
         "•  One change that would improve education or work in your country.",
         "•  A person who influenced you, and the advice they gave you.",
         "",
         "You may make brief notes during the preparation time. Speak without reading a script."],
        fill=FILL_BOX_TEAL, label_color=TEAL)
    para(doc, "Evaluation rubric", size=11, bold=True, color=NAVY)
    table(doc, ["Criterion", "4 — Strong", "3 — Good", "2 — Developing", "1 — Beginning"], [
        [("Grammatical accuracy", True),
         "structures are consistently accurate; occasional slips do not affect meaning",
         "generally accurate; some errors, meaning always clear",
         "frequent errors; meaning sometimes unclear",
         "errors dominate; meaning often unclear"],
        [("Appropriate structure selection", True),
         "wide range used naturally (tenses, conditionals, linkers, hedging…) for the intended meaning",
         "good range; choices usually match the meaning",
         "limited range; some structures forced or inappropriate",
         "basic structures only; frequent wrong choices"],
        [("Clarity", True),
         "ideas well organised and easy to follow; effective linking",
         "clear overall; some linking",
         "ideas loosely connected; hard to follow at times",
         "ideas listed without clear connection"],
        [("Successful communication", True),
         "message fully delivered; confident, natural delivery with self-repair",
         "message delivered; some hesitation",
         "message partly delivered; long pauses",
         "message largely not delivered"],
    ], widths=[1.35, 1.35, 1.25, 1.2, 1.15], font_size=9)
    para(doc, "Score: ____ / 16     Compare with the Diagnostic Test and note the progress in each criterion.",
         size=11, bold=True, color=NAVY)
    para(doc, "Personal error analysis and improvement plan", size=11, bold=True, color=NAVY)
    para(doc, "Copy every error you made in the Final Assessment (written and spoken) into the table. "
              "An error that is analysed is halfway to being fixed.", size=10.5, italic=True, color=GREY)
    table(doc, ["My error", "Correct form", "Why it happened (rule I forgot)", "My fix — where I will practise it"], [
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
    ], widths=[1.6, 1.6, 1.6, 1.6], font_size=9.5, zebra=False)
    para(doc, "My next three goals:", size=11, bold=True, color=NAVY)
    for i in range(1, 4):
        para(doc, f"{i}.  ", indent=0.12)
    para(doc, "Remember: improvement is measured by what you can do in speech — not by pages completed. "
              "Record yourself speaking for two minutes on the same topic in a month, and listen to the difference.",
         size=10.5, italic=True, color=GREY)


def render_all(doc, keys_registry):
    review_test(doc, 1, 4, keys_registry)
    review_test(doc, 2, 8, keys_registry)
    review_test(doc, 3, 12, keys_registry)
    final_assessment(doc, keys_registry)

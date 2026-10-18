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
            "While we __________ (wait — ongoing action), the announcement came.",
            "At standard atmospheric pressure, pure water __________ (freeze) at 0°C.",
            "She __________ (study) medicine these days.",
            "By the time we arrived, the guests __________ (eat) everything.",
            "Look at the sky — it __________ (rain).",
            "How long __________ you __________ (know) Nadia?",
            "Before the meeting __________ (start), we had already discussed the plan.",
        ]
        B = [
            "You __________ wear a seat belt; it's the law.  (must / might)",
            "__________ you mind __________ (close) the door?",
            "Do you know where the post office __________ ?  (be)",
            "You __________ bring any food; we will provide everything.  (not / have to)",
        ]
        C = [
            "Give advice: A friend is exhausted but has a long drive.  (use should)",
            "Make it polite: 'Where did you park?'  (Could you tell me…)",
            "Give a deduction: You see a colleague carrying a tennis racket. 'You __________ (be) on your way to a game.'",
        ]
        key = {
            'A': ["haven't seen", "were waiting", "freezes", "is studying", "had eaten",
                  "is going to rain / will rain", "have / known", "started"],
            'B': ["must", "Would / closing", "is", "don't have to / needn't"],
            'C': ["Answers vary; e.g., 'You should rest before driving.' (should + base verb)",
                  "Could you tell me where you parked?",
                  "must be"],
        }
    elif num == 2:
        A = [
            "If I __________ (know) his number, I would call him now.",
            "I wish I __________ (take) that opportunity last year.",
            "This method is __________ (effective) than the old one.",
            "While I __________ (read — ongoing action), the lights went out.",
            "When we arrived, the guests __________ (already / leave).",
            "It's high time we __________ (make) a decision.",
            "This option is by far the __________ (good) for our budget.",
            "Unless you __________ (hurry), you'll miss the bus.",
        ]
        B = [
            "Combine with despite: 'The exam was hard. Everyone passed.'",
            "Rewrite as a second conditional: 'I don't have a car, so I can't drive you.'",
            "Give polite advice to a friend who wants to quit their job without a plan.  (2 modals)",
            "Make it polite: 'Where is the bank?'",
        ]
        C = [
            "Rewrite as a mixed conditional (past → present): 'She didn't save money, so she can't buy the car now.'",
            "Compare with a reason: 'This course is better than that one.'  (use far + reason)",
            "Correct: 'Despite of the cost, we decided to proceed.'",
        ]
        key = {
            'A': ["knew", "had taken", "more effective", "was reading", "had already left",
                  "made", "best", "hurry"],
            'B': ["Despite the exam being hard, everyone passed. / Despite the difficulty, everyone passed.",
                  "If I had a car, I would drive you. / If I had a car, I could drive you.",
                  "answers vary — advice with should/could/might",
                  "Could you tell me where the bank is?"],
            'C': ["If she had saved money, she could buy the car now. / …would be able to buy…",
                  "answers vary — far + comparative + reason",
                  "Despite the cost, we decided to proceed."],
        }
    else:
        A = [
            "The house __________ (build) in the 1960s.",
            "I had my watch __________ (repair) last week.",
            "She is said __________ (speak) five languages.",
            "He avoided __________ (make) the same mistake twice.",
            "This is the café __________ we first met.",
            "She is the teacher __________ class inspired me.  (who / whose)",
            "I'd rather you __________ (not/mention) this to anyone.",
            "He talks as if he __________ (know) everything.",
        ]
        B = [
            "Rewrite with need: 'The room must be cleaned.'",
            "Rewrite as a deduction (past): 'Perhaps he missed the train.'",
            "Reduce: 'Students who are interested in the course should apply.'",
            "Make it formal and passive: 'People believe that the economy is improving.'",
        ]
        C = [
            "Complete: The __________ (much) you practise, the __________ (confident) you become.",
            "Correct the indirect question: 'Do you know where is the bank?'",
            "Complete the causative: I __________ my hair cut yesterday.",
            "Correct: 'I enjoy to read novels.'",
        ]
        key = {
            'A': ["was built", "repaired", "to speak", "making", "where", "whose",
                  "didn't mention", "knew"],
            'B': ["The room needs cleaning. / The room needs to be cleaned.",
                  "He must have missed the train.",
                  "Students interested in the course should apply.",
                  "It is believed that the economy is improving. / The economy is believed to be improving."],
            'C': ["more / more confident",
                  "Do you know where the bank is?",
                  "had",
                  "I enjoy reading novels."],
        }

    _qblock(doc, "Part A — Complete the sentences.", A)
    _qblock(doc, "Part B — Rewrite, combine or transform.", B)
    _qblock(doc, "Part C — Use and communication.", C)
    para(doc, "When you finish, check your work in Appendix 5. The answers are kept separate so you can complete the test without seeing them.",
         size=10.5, italic=True, color=GREY)
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
        "Correct: 'The book what I read was amazing.'",
        "Complete: The more you practise, the __________ (confident) you become.",
        "Report advice: 'You should apply early,' she said.  (She advised…)",
        "Complete with the right pattern: I look forward to __________ (meet) you.",
    ]
    for i, q in enumerate(C, 23):
        para(doc, f"{i}.  {q}", indent=0.12)
    key = {
        'A': ["have lived / 've lived / have been living", "had already had", "is", "hadn't said", "was cancelled",
              "must have been working", "making", "rewrite", "challenging", "Warned / Having been warned",
              "leaving", "did she apologise"],
        'B': ["He said he would help me the next day.",
              "She asked me where I had bought it.",
              "Could you tell me when the shop closes?",
              "If he had revised, he wouldn't have failed.",
              "The documents have been stolen.",
              "It was the manager who/that approved the plan.",
              "I had the roof fixed.",
              "Rarely had she felt so confident.",
              "Although the task was difficult, they finished it.",
              "Having studied hard, he passed easily."],
        'C': ["can't", "Despite", "This method may well be the best. / This method is probably the best. (answers vary)",
              "Option A is far better than Option B because… (answers vary)",
              "The book (that / which) I read was amazing.",
              "more confident", "She advised me to apply early.", "meeting"],
    }
    para(doc, "Stop here until you have completed all 30 items. The answer key is in Appendix 5.",
         size=10.5, italic=True, color=GREY)
    keys_registry["Final Assessment"] = key
    para(doc, "Accept alternative answers where the exercise allows them (e.g. 'may well' / 'probably' / "
              "'is likely to' for hedging). The Diagnostic Test is a broad starting snapshot, not a "
              "parallel form of this 30-item assessment. Do not compare the raw grammar totals as "
              "a measure of gain; compare your four speaking-rubric criterion scores instead.", size=10.5, italic=True, color=GREY)

    page_break(doc)
    h_banner(doc, "FINAL ASSESSMENT — PART 2", sub="Independent speaking task and evaluation")
    box(doc, "Speaking task (2 minutes to prepare · 2 minutes to speak, then follow-up exchange)",
        ["Speak on ONE of the following topics:",
         "•  A decision that changed your life — and what you would do differently today.",
         "•  One change that would improve education or work in your country.",
         "•  A person who influenced you, and the advice they gave you.",
         "After your talk, a partner asks two follow-up questions. Answer them, then ask one relevant "
         "question in return. If you get stuck, repair and continue.",
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
         "message fully delivered; natural delivery, relevant follow-up exchange and self-repair",
         "message delivered; answers and asks relevant follow-ups, with some hesitation",
         "message partly delivered; responses are limited or pauses are long",
         "message largely not delivered; little response to questions"],
    ], widths=[1.35, 1.35, 1.25, 1.2, 1.15], font_size=8.5)
    para(doc, "Score: ____ / 16     Compare each criterion with your recorded Diagnostic speaking score.",
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
        para(doc, f"{i}.  ________________________________________________________________", indent=0.12)
    para(doc, "Remember: improvement is measured by what you can do in speech — not by pages completed. "
              "Record yourself speaking for two minutes on the same topic in a month, and listen to the difference.",
         size=10.5, italic=True, color=GREY)


def render_all(doc, keys_registry):
    review_test(doc, 1, 4, keys_registry)
    review_test(doc, 2, 8, keys_registry)
    review_test(doc, 3, 12, keys_registry)
    final_assessment(doc, keys_registry)

# -*- coding: utf-8 -*-
"""Teacher's Book guides for Lessons 13-16 (Parts Seven and Eight)."""


def _t(hook, rule, diff, pair, adv):
    assert hook + rule + diff == 15 and pair + adv == 20
    return [("The Speaking Hook", hook), ("The Simple Rule", rule),
            ("See the Difference", diff), ("Practice the Pattern", 10),
            ("Pair Speaking", pair), ("The Advanced Upgrade", adv),
            ("Real Talk Challenge", 10), ("Review and Self-Check", 5)]


T13 = {
    'objectives': [
        "Report statements, questions and commands with correct backshift and time reference.",
        "Use reporting verbs beyond say (admit, warn, suggest, remind…) naturally in speech.",
        "Retell a real conversation with at least four varied reported items and a final comment.",
    ],
    'success': [
        "backshift accurate for at least 4 of 5 statements",
        "reported questions use statement order (no do, no inversion)",
        "time words shifted where the reporting is later",
    ],
    'prep': [
        "Board: backshift ladder (present → past → past perfect; will→would; can→could).",
        "Reporting-verb strip: admit/agree/argue/claim/warn/insist/suggest/remind.",
        "Formula Book card 13.",
    ],
    'timing': _t(4, 7, 4, 11, 9),
    'procedure': {
        'hook': [
            "Learners report what someone really said to them this week — no reading, no notes.",
            "Two samples whole-class; mark direct vs reported on the board.",
            "State the aim: half of adult speaking is reporting — accuracy buys respect.",
        ],
        'rule': [
            "Rule 1: one-step backshift — chorally walk the ladder with one sentence per step.",
            "Rule 2: questions/commands — build one Y/N + if and one W(h)-question together on "
            "the board.",
            "Rule 3: reporting verbs as chunks — admit -ing / promised to / warned not to / "
            "suggested -ing.",
            "Rule 4: time shift — two examples only; the 'same-day keep' exception flagged.",
        ],
        'diff': [
            "say vs tell vs ask table: pairs sort three sentences before revealing the pattern line.",
            "Same-tense vs backshift table: ask when present tense stays (still true now).",
            "Command/request/advice row: four force levels, one sentence each.",
        ],
        'practice': [
            "Practice A (6): solo + pairs; A3/A4 test the question/command pattern — force "
            "statement order aloud.",
            "Practice B (6): B1/B2 reported in pairs; B3/B4 corrections stated with the error.",
            "Key after checking; on any suggest-me-to-go error, re-teach Rule 3.",
        ],
        'pair': [
            "Message game: three 'other person' messages per A; B reports to a third listener.",
            "Four different reporting verbs + question + command required before stopping.",
            "Swap roles; whole class hears the clearest retelling chain.",
        ],
        'advanced': [
            "Intermediate base: backshift table drill + four chunk patterns.",
            "Advanced upgrade: 'kept insisting / went on to explain / points out / claimed…' — "
            "one true sentence per frame.",
            "Debate: when does 'He claimed' cast doubt vs just report?",
        ],
        'realtalk': [
            "Planning: choose conversation, list four things said (who + keyword) + four verbs.",
            "90 seconds to a partner; model covered.",
            "Model uncovered; count verbs, check backshift, compare with learners' own retelling "
            "and improve one sentence.",
        ],
        'review': [
            "Covered: report three things from today.",
            "Question/command/promise round — oral only.",
            "Self-check; unticked redo A1–A3 and B3 aloud.",
        ],
    },
    'checking': [
        "'He said me that…' — fix together. (told me)",
        "'She suggested me to go' — fix. (going / that I go)",
        "Time check: 'tomorrow' → 'the next day' — when can you keep 'tomorrow'?",
    ],
    'notes': [
        "A1 'was working' — backshift from 'am working'; accept 'had been working' only if the "
        "learner explains the longer duration — do not mark as wrong automatically.",
        "A4 'not to' — warning/telling not to + base; 'not touch' bare would be wrong here.",
        "A6 'taking' — suggest + -ing; 'to take' is the flagged error (B4).",
        "B2 'would be announced' — will → would; do not accept 'will'.",
        "B5 denies the content, not the act: 'denied breaking the window' (deny + -ing).",
    ],
    'pair_model': "A: My friend said she was worried about the interview. B: My friend said she "
                  "was worried — she admitted she hadn't prepared enough. She said she would call "
                  "me after, and her boss warned her not to arrive late. She asked me if I knew "
                  "what questions would be asked. I suggested going to bed early and promised to "
                  "send her my notes.",
    'assess': [
        "Count backshift, statement order, reporting-verb variety and time shift with the printed "
        "checks; accept a still-true present tense (L6 carryover) where justified.",
        "Accept any real conversation content; the model is not required copying.",
        "Prompt once for a missing question report if learners avoid it.",
    ],
    'inter': [
        "Board ladder stays visible; learners touch the step before speaking.",
        "Chunk desk card: 'admitted -ing · promised to · warned not to · suggested -ing'.",
        "Remediation: re-run say/tell and suggest fixes chorally before Real Talk.",
    ],
    'adv': [
        "Liveliness: 'She kept insisting…' vs 'She insisted…' — register?",
        "Academic stance: 'The report points out that demand has fallen' — learners build one.",
        "Judgement-free: 'He claimed to have seen nothing, yet…' — who is judged?",
    ],
    'errors': [
        "'He said me…' → 'He told me…' — fix: say + that vs tell + person sort.",
        "'She suggested me to go' → 'going' — fix: verb-pattern flash with four verbs.",
        "Keeping question inversion in reported form — fix: statement-order drill with two "
        "questions.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; message game runs two messages per role.",
        "Upgrade becomes homework sentences.",
        "Real Talk: 60 seconds with three reported items + comment.",
    ],
    'review_note': [
        "Exit ticket: report one question, one command, one promise from today.",
        "Reported speech is tested again in the Final Assessment (B1/B2) — flag those items.",
        "Formula card 13.",
    ],
    'feedback': "During pair reporting, tick reporting-verb count and backshift — do not correct "
                "mid-flow; rebuild two errors after the round, choosing the most frequent one first.",
}

T14 = {
    'objectives': [
        "Form participles and participle clauses accurately and keep the subject matching.",
        "Distinguish -ing (cause) from -ed (feeling) adjectives in speech.",
        "Open a formal recommendation with Given/Considering and a Having-clause.",
    ],
    'success': [
        "opening participle clauses match the subject of the main clause",
        "at least two accurate participle clauses per briefing",
        "-ed/-ing adjectives chosen correctly in description",
    ],
    'prep': [
        "Board: -ING = causes feeling · -ED = feels it (boring/bored).",
        "Frame strip: Given… / Considering… / With + noun + -ing / Having + participle.",
        "Formula Book card 14.",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Two-sentence combos: learners combine them any way they like — reveal how many chose "
            "a participle.",
            "Collect the most professional version whole-class; underline the participle.",
            "Name today's aim: compression without confusion.",
        ],
        'rule': [
            "Rule 1: -ing vs -ed adjectives — choral drill of four pairs (boring/bored etc.).",
            "Rule 2: participle clauses — build one Having-example on the board step by step.",
            "Rule 3: absolute/fronted patterns — chorally read the three examples.",
            "Rule 4: compression with the learner-combine sentence: 'Opening the letter…'",
        ],
        'diff': [
            "-ing vs -ed table: pairs state 'what causes? who feels?' for each row.",
            "Participle vs full clause table: same meaning comparison, emphasis on compression.",
            "Subject-rule warning: write the dangling example ('Opening the window, the room was "
            "cold') and repair it together.",
        ],
        'practice': [
            "Practice A (6) solo + pairs; A3/A4 (Having…) need the participle type named aloud.",
            "Practice B (6): B1 spoken compressions in pairs; B3 as whole-class chorus.",
            "Key after checking; re-teach the subject rule if B3 was widely missed.",
        ],
        'pair': [
            "Formal briefing: each partner 60 seconds, two participle clauses, listener reports "
            "in one sentence.",
            "Monitor for Having-clause + Given/Considering + -ed/-ing pair.",
            "Swap; best briefing heard twice for the class.",
        ],
        'advanced': [
            "Intermediate base: -ed/-ing about real life + two correct openings from the week.",
            "Advanced upgrade: 'There being no…', 'Never having…', formal closings — one each.",
            "Discussion: 'Considering all the evidence, we recommend…' — who is considering?",
        ],
        'realtalk': [
            "Planning: evidence → recommendation → closing — mark participle slots as printed.",
            "90 seconds to a partner; model covered.",
            "Model uncovered; count clauses, compare subject matching, improve one learner "
            "sentence together.",
        ],
        'review': [
            "Covered: 'Having…' sentence about today.",
            "One -ing and one -ed adjective about today — round-robin.",
            "Self-check; unticked redo B3 and A2 aloud.",
        ],
    },
    'checking': [
        "'boring vs bored' — things are -ing, people are -ed; quick thumbs.",
        "'Opening the window, the room was cold.' — correct? (no — who opened?) rebuild it.",
        "'Given the costs, the plan is unrealistic' — who is giving? (frame, not verb)",
    ],
    'notes': [
        "A1 'boring' — lecture causes boredom; 'bored' would describe hearers.",
        "A5 'With' — absolute clause; 'Despite' would invert the meaning.",
        "B1 'Having studied hard…' — compresses 'Because…'; 'After' is also correct but less formal.",
        "B2 'The man standing at the door waved' — reduced correctly; 'The man who was standing' "
        "also credited.",
        "B5 'interested' — -ed = feels (about history); 'interesting' would make the person the cause.",
    ],
    'pair_model': "A: Given the short deadline, we finished the work on time. Having worked late "
                  "every evening, we were exhausted but satisfied. B: Was the client interested? "
                  "A: Very — the proposal was fascinating, and the client was clearly impressed. "
                  "With prices falling, they approved the plan quickly. B: So, having delivered "
                  "early, are you now free? A: Considering the feedback, almost — just one report "
                  "to go.",
    'assess': [
        "Assess the two printed checks plus subject matching — no dangling participle counts.",
        "Over-compression is penalised: require clarity alongside brevity.",
        "Model is one register choice; learners may choose a less formal briefing style if "
        "clauses are correct.",
    ],
    'inter': [
        "Subject-link arrow drawn between participle and main-clause subject during pair work.",
        "Frame card: 'Having finished…' · 'Given…' · 'With + noun…'",
        "Remediation: if B3 failed, rebuild one participle opening collaboratively before Real Talk.",
    ],
    'adv': [
        "Formality ladder: after/while/because → Having… / Walking… / Written in… — when formal?",
        "Story upgrade: 'Never having travelled abroad, he found…' — build one true.",
        "Formal closer: 'We recommend delaying the decision.'",
    ],
    'errors': [
        "'Opening the window, the room was cold' (dangling) → '…I felt the cold' — fix: subject "
        "arrow drawn, then learner rebuild.",
        "'I am very interesting in history' → 'interested' — fix: cause-vs-feel sorting.",
        "Over-participle speech ('Having… Having… Given…') — fix: one-two per answer is enough.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; briefing becomes 45 seconds with report-back.",
        "Advanced upgrade moves to a written homework example.",
        "Real Talk: keep both structures but deliver as 60 seconds.",
    ],
    'review_note': [
        "Exit ticket: one 'Having…' sentence + one absolute frame about today.",
        "Participles return in the Final Assessment (C10) — connect the revision.",
        "Formula card 14.",
    ],
    'feedback': "Tick participle openings and subject links during briefings — correct the first "
                "dangling participle the moment it is spoken (board repair), leave the second for "
                "the aftermath.",
}

T15 = {
    'objectives': [
        "Hedge claims appropriately (may well / tend to / it could be argued).",
        "Apply cleft and inversion emphasis accurately and sparingly.",
        "Match certainty language to evidence in a formal talk.",
    ],
    'success': [
        "no inversion-error and no broken cleft in the pair and Real Talk",
        "at least one hedge placed per claim, never three in a row",
        "certainty level defensible by evidence when challenged",
    ],
    'prep': [
        "Board: will/must be (certain) · should/may well (likely) · may/might/could (possible).",
        "Frame cards: It is…that · What I…is · Never have I… · Not only did… Only then did…",
        "Formula Book card 15.",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Board 'The plan will fail' vs 'The plan may well fail' — class votes which sounds "
            "more educated, then defends with 'why?'",
            "Two learners say the same opinion: certain, then hedged — class names the "
            "difference.",
            "Aim: control of strength is control of credibility.",
        ],
        'rule': [
            "Rule 1: hedging — read the three levels, then one example per frame.",
            "Rule 2: clefts — board-build 'It was the price that changed my mind' with focus "
            "marks.",
            "Rule 3: inversion — chorally read the three openers; underline the inverted aux.",
            "Rule 4: register ladder — same request in three registers, spoken by three learners.",
        ],
        'diff': [
            "Certainty table: pairs label will / may well / might with the three claims.",
            "Normal vs inversion table: normal on left, inverted on right — mark when inverted "
            "sounds heavy.",
            "Cleft table: same sentence, three spotlights — ask 'What is in focus?'",
        ],
        'practice': [
            "Practice A (6) solo + pair; A1/A2/A3 test inversion form directly.",
            "Practice B (6): B1–B4 spoken transformations; B5 two-register performance aloud.",
            "Key after checking; drill 'Never have I…' chorally if A1 slipped.",
        ],
        'pair': [
            "Panel: 'What will work look like in ten years?' — one minute per partner + hard "
            "follow-up.",
            "Require hedge + cleft + conclusion in each answer.",
            "Follow-up answered carefully — monitor for hedging under pressure.",
        ],
        'advanced': [
            "Intermediate base: three certainty groups in context + three inversion frames.",
            "Advanced upgrade: 'little did he know', litotes, conditional inversion — one each.",
            "Register check: 'This proposal may well…' vs 'It will…' — evidence matters?",
        ],
        'realtalk': [
            "Planning as printed: claim+evidence → cleft focus → inversion → keywords only.",
            "Two minutes to a partner without notes; model covered.",
            "Model uncovered; count hedge/cleft/inversion, compare, improve one line.",
        ],
        'review': [
            "Covered: one claim at three certainty levels — rapid-fire.",
            "One cleft + one inversion from memory — round-robin.",
            "Self-check; unticked redo B4 and the paired certainty line aloud.",
        ],
    },
    'checking': [
        "'Never I have seen' — fix order. (have I)",
        "Three-level rapid: 'The plan will/may well/might succeed' — evidence for each?",
        "Cleft focus check: 'It was the manager who…' — what was focused? (the actor)",
    ],
    'notes': [
        "A1 'Never' — negative-opener inversion; 'Ever' would not trigger it.",
        "A3 'did I understand' — 'Only after reading it twice' forces inversion.",
        "A4 flexible: both 'suggests' (data as collective) and 'suggest' (data as plural) "
        "credited, as stated in the key.",
        "B3 accepts 'Rarely had I felt so confident' or 'Rarely have I…' where the learner "
        "explains the past/future intention — past tense is the printed answer.",
        "B6 'Not only…but also' — the second clause's but/but also is optional in speech; "
        "credit either.",
    ],
    'pair_model': "A: In ten years, remote work will be normal — it could be argued that offices "
                  "will become meeting places only. B: It is flexibility that workers want most. "
                  "A: Never have I been more confident that change is coming. B: Really — what "
                  "evidence do you have? A: Studies suggest productivity rises 8%, and rarely "
                  "have companies reported wanting to go back fully.",
    'assess': [
        "Use the four feedback criteria as live ticks — hedging not over-hedging is the hardest "
        "to judge, so listen for stacked hedges.",
        "Inversion and cleft must be accurate; one correct example each is enough.",
        "Register must be consistently formal in Real Talk; one casual register slip is the "
        "limit before feedback.",
    ],
    'inter': [
        "Certainty desk card visible during all speaking.",
        "Frame prompts: 'This may well…' · 'It was X who…' · 'Never have I…'",
        "Remediation: if inversion slips, re-drill the three frames chorally before Real Talk.",
    ],
    'adv': [
        "Litotes: 'You are not wrong' vs 'You are right' — when softer?",
        "Formal conditional inversion: 'Were this accepted, we would…' — build one.",
        "Evidence check: challenge a learner's hedge — 'What evidence makes this may-well "
        "rather than might?'",
    ],
    'errors': [
        "'Never I have seen' → 'Never have I…' — fix: negative opener → aux + subject order.",
        "Over-hedging ('It might perhaps possibly…') — fix: one careful hedge is enough; cross "
        "out two.",
        "Over-inverting every sentence — fix: once per talk for impact, marked with a star.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; panel runs one question per pair.",
        "Litotes/conditional-inversion become written homework.",
        "Real Talk: 90 seconds instead of two minutes — still three structures.",
    ],
    'review_note': [
        "Exit ticket: one cleft and one inversion about today.",
        "Hedging/Inversion return in Lessons 16 and the Final Assessment (rubric criterion 2/3).",
        "Formula card 15.",
    ],
    'feedback': "Name one well-judged hedge with its evidence — this teaches hedging better than "
                "generic praise; correct inversion order only in the repair phase.",
}

T16 = {
    'objectives': [
        "Integrate time, choice, shape and style grammar in continuous speech.",
        "Self-repair accurately and keep speaking without freezing.",
        "Prepare for the Final Assessment speaking task conditions.",
    ],
    'success': [
        "at least six different target structures used in the two-minute talk",
        "at least one self-repair performed aloud with a repair phrase",
        "story shape (background → decision → goal) clear to the listener",
    ],
    'prep': [
        "Four-job map printed: TIME · CHOICE · SHAPE · STYLE — visible to every pair.",
        "Repair phrases on desk card: 'What I mean is…' · 'Let me rephrase…' · 'Or rather…'",
        "Timer set to 2 minutes; Final Assessment rubric to hand.",
    ],
    'timing': _t(4, 7, 4, 13, 7),
    'procedure': {
        'hook': [
            "30-second topic to a partner; listeners name every structure they recognise.",
            "Two learners' lists on the board — which four-job bucket is missing?",
            "Aim: today nothing is new — today nothing is hidden either.",
        ],
        'rule': [
            "Four-job map: place every course structure in one bucket together — learners "
            "touch each item on their copy.",
            "Three-step strategy: THINK meaning → CHOOSE structure → SAY it whole — rehearse "
            "with one repair example aloud.",
            "Remind: accuracy before range, every time.",
        ],
        'diff': [
            "Recognition vs use — ask 'Which is harder?' — expect: producing under pressure.",
            "Ask pairs to list one structure per job from their own life in 60 seconds.",
        ],
        'practice': [
            "Practice A (6) fix-and-explain: each error named and corrected aloud — no silent "
            "marking.",
            "Practice B (6): B1 participle spoken; B2–B6 spoken in pairs with brief discussion.",
            "Key after pair checking; use B2 as the reported-speech recap point.",
        ],
        'pair': [
            "Grammar gym: four rounds, one minute per round (storytelling/advice/report/argument).",
            "Partner counts target structures per round and reports one strength.",
            "Best round per pair replayed for the class as the exemplar.",
        ],
        'advanced': [
            "Intermediate base: re-do the hardest earlier exercise aloud; three sentences per job.",
            "Advanced upgrade: stacked 'Had I known…' sentence, style opening, repair phrases — "
            "one each performed.",
            "Discussion: when does a repair show control vs when it hides it?",
        ],
        'realtalk': [
            "Planning exactly as printed: three lines (story / decision / goal) + two 'show-off' "
            "structures chosen deliberately.",
            "Two minutes to a partner without notes; model covered.",
            "Model uncovered; count structures, compare story shape to the printed feedback, "
            "improve one line, then repeat once to a new partner.",
        ],
        'review': [
            "Covered: name the four jobs + one structure per job.",
            "One-minute story with three structures — volunteer.",
            "Self-check; unticked means re-open the Formula Book, not the next book.",
        ],
    },
    'checking': [
        "Four-job map rapid: 'passive?' (shape) — 'wish?' (choice) — 'hedging?' (style)",
        "Repair challenge: give a wrong-sentence starter — learners repair aloud.",
        "Six-structure sprint: count structures heard in 30 seconds.",
    ],
    'notes': [
        "A1–A6 are fix-and-explain — insist on the explanation, not just the correction; these "
        "are course retrospection items.",
        "B2 'She told me not to worry / She reassured me' — both credited; reassured is not a "
        "reporting verb but a semantic equivalent here.",
        "B6 requires indirect (word order) — any polite indirect question on tomorrow's schedule "
        "is open.",
        "B5 accepts any well-formed hedge; B3 accepts any degree-word + reason comparison.",
        "Practice workload here is intentionally integrated — A/B together revise 12 structures.",
    ],
    'pair_model': "A: Last year I almost quit English when I failed the first exam — I was "
                  "working nights and had little time. B: How did you continue? A: A friend told me "
                  "to focus on speaking, not translation. If I had stopped, I would have lost the "
                  "chance — as it was, I passed. B: So what is your argument for the school? A: If "
                  "the school funds evening speaking clubs, students will improve faster — a small "
                  "cost, a clear result. To sum up, start with the learners who need it most.",
    'assess': [
        "Count structures heard against the printed four criteria; repairs are scored as a "
        "positive, not a penalty.",
        "This lesson is also the Final Assessment speaking rehearsal — score with the same rubric "
        "and keep the scores.",
        "Accept any topic that shows range; the model is one path, not the required content.",
    ],
    'inter': [
        "Four-job map always visible; learners point to the job before choosing the structure.",
        "Repair phrase desk card stays out for every round.",
        "Remediation: learners who froze re-do the three-line plan before the next attempt.",
    ],
    'adv': [
        "Stacking: 'Had I known…' as the show-off structure — pairs judge clarity vs complexity.",
        "Style intention: open with inversion, hedge the claim, close with a cleft — deliberate "
        "style, not decoration.",
        "Repair sophistication: 'Or rather…' vs 'What I mean is…' — when more formal?",
    ],
    'errors': [
        "Complexity before accuracy — fix: 'Simple and correct beats fancy and wrong' on the board.",
        "Freezing on an error — fix: repair phrase drill (five errors rebuilt with 'What I mean is').",
        "Stacking too many structures in one sentence until it collapses — fix: one hard structure "
        "per sentence, maximum.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; grammar gym runs two rounds chosen by teacher.",
        "Two remaining gym rounds become the take-home spoken homework (recorded).",
        "Real Talk: still two minutes — do not shorten Lesson 16's culminating talk.",
    ],
    'review_note': [
        "Exit ticket: one story with three structures, spoken — recorded if possible.",
        "Next class is the Final Assessment — use today's rubric scores as the true baseline "
        "companion to the Diagnostic.",
        "Formula cards: entire book. The Can-Do Tracker (Student Book Appendix 4) is today's "
        "takeaway.",
    ],
    'feedback': "Celebrate self-repairs as evidence of control — announce the repair phrase you "
                "heard; correct only the single most repeated structural error for the class, "
                "after every round.",
}

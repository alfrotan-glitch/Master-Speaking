# -*- coding: utf-8 -*-
"""Teacher's Book guides for Lessons 1-8 (Parts One to Four).

Timing helper: every guide totals exactly 60 minutes and matches the Student
Book's five pacing blocks (15 / 10 / 20 / 10 / 5).
"""


def _t(hook, rule, diff, pair, adv):
    assert hook + rule + diff == 15 and pair + adv == 20, \
        f"timing blocks must stay at 15 and 20: {hook}+{rule}+{diff}, {pair}+{adv}"
    return [("The Speaking Hook", hook), ("The Simple Rule", rule),
            ("See the Difference", diff), ("Practice the Pattern", 10),
            ("Pair Speaking", pair), ("The Advanced Upgrade", adv),
            ("Real Talk Challenge", 10), ("Review and Self-Check", 5)]


T1 = {
    'objectives': [
        "Choose accurate forms for habits, current situations, finished past events and future "
        "arrangements in spoken sentences.",
        "Explain in one sentence why a finished-time expression takes the past simple rather than "
        "the present perfect.",
        "Deliver a one-minute account of their English improvement using at least three different "
        "tense families with correct time expressions.",
    ],
    'success': [
        "at least 4 of 5 Practice A items correct before the key is displayed",
        "corrections in Practice B are justified with a time reason, not a guess",
        "in the Real Talk Challenge, time expressions match the chosen tense every time",
    ],
    'prep': [
        "Board with three columns: NOW (present tenses) · FINISHED (past simple) · CONNECTED TO "
        "NOW (present perfect) · NEXT (future choices).",
        "No photocopies required; learners write only keywords during planning.",
        "Optional: phone or recorder for one Real Talk attempt to replay in the next lesson.",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Display the four hook questions. Learners answer all four in pairs — books closed; "
            "the point is to hear which tenses they already reach for.",
            "Take two contrasting samples whole-class ('What has changed since last year?') and "
            "underline the time words learners used.",
            "Tell learners the lesson will give them precise choices for exactly these answers.",
        ],
        'rule': [
            "Teach the three rule groups in order: present tenses, past simple vs present "
            "perfect, future choices. One formula box, two or three examples each — nothing more.",
            "Read each Examples line aloud and have the class repeat one sentence per group.",
            "Contrast 'I saw him yesterday' with 'I have seen him recently' on the board to fix "
            "the finished-time rule with its 'recently' qualification.",
        ],
        'diff': [
            "Cover the right-hand column of the first table and ask pairs to predict the "
            "difference before revealing it.",
            "Drill the state-verb line: learners correct 'I am knowing' chorally, then produce "
            "their own state-verb sentence.",
            "Ask: 'Which time words force the past simple?' — expect: yesterday, last…, in "
            "2020, when…",
        ],
        'practice': [
            "Set Practice A (5 items) — 3 minutes alone, then compare in pairs before taking "
            "whole-class answers.",
            "Set Practice B (4 tasks) — corrections must be given with a one-clause reason.",
            "Display the key only after pair checking; ask 'Why?' for any item where half the "
            "room disagrees.",
        ],
        'pair': [
            "Model one interview round with a confident learner first: ask, listen, ask a "
            "follow-up — then hand over to pairs.",
            "Run the four questions; circulate with the success criteria and tick evidence.",
            "Close with two samples: one learner reports what their partner said (past + "
            "present perfect mix).",
        ],
        'advanced': [
            "Intermediate base: pairs check the time-cue drill aloud; each makes three true "
            "sentences (habit, current project, recent experience).",
            "Advanced upgrade: pairs produce the present-perfect continuous sentence and the "
            "'It's the first time I've…' emphasis frame, then explain when each is better than "
            "the simple forms.",
            "Ask one pair to defend a choice: 'Why present perfect, not past simple?'",
        ],
        'realtalk': [
            "Give the planning time exactly as printed (30 seconds, keywords only) — no full "
            "sentences on paper.",
            "First attempt to a partner (1 minute). Model response stays covered.",
            "Uncover the model; learners underline its tense choices, then retell their own "
            "content with one improved structure.",
        ],
        'review': [
            "Run the retrieval prompts orally — cover the page first, as printed.",
            "Collect the two 'Watch out' corrections as a whole-class chorus.",
            "Learners tick the self-check boxes; anyone with an unticked box returns to the "
            "Simple Rule and a Practice A item before the next lesson.",
        ],
    },
    'checking': [
        "'Last year I…' — which tense? (past simple) · 'Since 2021 she has…' — why not 'worked'?",
        "Fast fingers: show a time phrase card; learners point to the NOW, FINISHED, CONNECTED "
        "or NEXT column.",
        "Ask two learners to give opposite answers with the same verb: 'I work here' vs "
        "'I'm working here this month.'",
    ],
    'notes': [
        "A1 'saw' — 'last week' is a finished time; any present perfect here is an error, not "
        "a variant.",
        "A2 accepts 'has worked / has been working' — since 2022 keeps the situation open, so "
        "both aspects are correct; the continuous adds emphasis on continuation.",
        "A3 'are meeting' — an arrangement with a time word takes the present continuous for "
        "the future; 'will meet' loses the arrangement meaning.",
        "B3 'have you known' — 'How long' asks about a period continuing to now; 'do you know' "
        "asks about present knowledge and is possible only with a different reading, which this "
        "item rules out.",
        "B4 'I'm going to study medicine' — a decided plan; a bare 'I will study' would signal "
        "a decision made while speaking.",
    ],
    'pair_model': "A: What do you usually do at the weekend? B: I usually visit my family, and "
                  "on Sunday I play football. — A: Nice. How long have you been playing? B: "
                  "Since school. What did you do last night? A: I studied for two hours, then I "
                  "watched a film. B: What has changed in your life since last year? A: I speak "
                  "English at work now — I got a new job in March.",
    'assess': [
        "Use the four printed feedback bullets as live criteria; tick what you hear, do not "
        "write during the two minutes.",
        "The model is one strong version — accept any response that names a past event, "
        "explains the learning, and states current work with matching time words.",
        "Score nothing here; note two learners who confused finished and open time for a "
        "three-minute repair at the end.",
    ],
    'inter': [
        "Give a cue card set: yesterday / since 2021 / tomorrow 10 a.m. / these days — learners "
        "match each to a tense before speaking.",
        "Sentence starters: 'I have been… since…' · 'Last year I…' · 'I'm going to…'",
        "Remediation: if A1/A2 were wrong, re-do those two items orally with new time words "
        "before the pair task; delay the Real Talk Challenge until the correction lands.",
    ],
    'adv': [
        "Discussion: 'Which sounds more natural — I've seen her recently or I saw her recently? "
        "When would you choose each?' Expect the time-focus answer.",
        "Upgrade task: combine past simple and present perfect in one sentence about a real "
        "failure and its lesson.",
        "Extension: learners write one 'It's the first time I've…' sentence about an experience "
        "they actually had, then say it with stress on the experience.",
    ],
    'errors': [
        "'I have seen him yesterday.' → 'I saw him yesterday.' — fix: ask 'Is the time finished?' "
        "before choosing a tense; run a 60-second drill with four time phrases.",
        "'She is knowing the answer.' → 'She knows the answer.' — fix: list state verbs on the "
        "board (know, believe, own, seem) and sort five verbs into state/action.",
        "'We will meet tomorrow at ten' for a fixed arrangement — fix: contrast 'I'll help you' "
        "(decision now) with 'we're meeting at ten' (arrangement) using the learners' own "
        "timetables.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 exactly; drop the second pair sample.",
        "Pair Speaking: run questions 1 and 4 only (habit + change), still with follow-ups.",
        "Real Talk Challenge: 45 seconds of speech, 15 seconds planning; move the model "
        "comparison into the self-check at the end.",
    ],
    'review_note': [
        "Use the two retrieval prompts as the exit ticket for the lesson.",
        "Record 'has worked / has been working' as a standing acceptable-alternative reminder "
        "for future marking.",
        "Next lesson's warm-up: one past-simple sentence about yesterday from every learner.",
    ],
    'feedback': "Tick tense/time matches during the pair interview rather than interrupting; "
                "afterwards, put three anonymous sentences on the board — one good, two faulty — "
                "and let the class repair them before you confirm.",
}

T2 = {
    'objectives': [
        "Tell a short story that separates background (past continuous), events (past simple) "
        "and the earlier past (past perfect).",
        "Use at least three sequence markers correctly in a two-minute narrative.",
        "Retell a partner's story in three sentences without losing its order.",
    ],
    'success': [
        "the spoken story contains one accurate background scene and one past perfect clause",
        "the listener can repeat the events in the correct order",
        "at least three sequence words appear (first, then, by the time, suddenly, finally)",
    ],
    'prep': [
        "Board story shape: BACKGROUND → EVENTS → EARLIER → ENDING.",
        "Optional: two short anecdote openings written on slips for weaker pairs.",
        "Timer visible to learners for the ten-second plan in the Real Talk Challenge.",
    ],
    'timing': _t(4, 7, 4, 12, 8),
    'procedure': {
        'hook': [
            "Give every learner 30 seconds to tell a short story to their partner — no planning "
            "time, no notes.",
            "Listeners name the moment that felt most important and why (funny, surprising, "
            "sudden).",
            "Collect two whole-class examples and mark the shape they used on the board.",
        ],
        'rule': [
            "Teach the three levels as one system: background, events, earlier past. Use the "
            "Examples lines as choral reading.",
            "Board drill: 'While I was walking… when I met… because I had forgotten…' — learners "
            "fill each slot with their own content.",
            "Mark 'when + past simple' and 'while + past continuous' as a fixed pair, then read "
            "the 'by the time' remember line.",
        ],
        'diff': [
            "Use the three-column table as a substitution drill: same sentence, three levels — "
            "learners transform 'He took a taxi' across the row.",
            "Ask which level answers 'what was already happening?' — expect past continuous.",
            "Story-shape recap: one learner narrates the printed example scene end to end.",
        ],
        'practice': [
            "Practice A (6 items) solo (4 minutes), then同伴 check — emphasise A5/A6 agreement "
            "of tenses across two clauses.",
            "Practice B (6 tasks): pairs transform first, whole class confirms; B3 and B4 are "
            "spoken, not written.",
            "Display the key; drill aloud any item where the past perfect was omitted.",
        ],
        'pair': [
            "Set the two-minute story with the three required elements displayed as a checklist.",
            "Circulate and note one strength and one missing element per speaker.",
            "Listeners give two follow-up questions before roles swap.",
        ],
        'advanced': [
            "Intermediate base: the three-level drill and the 30-second one-while/one-when/"
            "one-by-the-time story.",
            "Advanced upgrade: repeated-past 'would', earlier background 'had been doing', and a "
            "present reflection ending — each learner produces one of the three.",
            "Discussion: why is 'It taught me a lesson I've never forgotten' a strong ending?",
        ],
        'realtalk': [
            "Ten seconds of silent planning only, as printed — nothing written.",
            "Tell partner 1, then immediately retell to partner 2: 'Tell it again, better.'",
            "Uncover the model; compare the model's shape (background → events → earlier → "
            "reflection) with learners' own.",
        ],
        'review': [
            "Cover and run the two retrieval prompts — the story with one 'while' and one 'by "
            "the time' is the must-pass item.",
            "Self-check boxes, then a show of hands: who missed the past perfect in practice?",
            "Anyone unticked redoes B2 ('By the time we reached the station…') aloud.",
        ],
    },
    'checking': [
        "'While I was walking' vs 'When I walked' — which takes the -ing form? (while)",
        "Show 'By the time we arrived, the film had started.' — learners identify the two past "
        "moments and point to the earlier one.",
        "Quick transform: 'She studied. The lights went out.' → learners say the background "
        "version aloud.",
    ],
    'notes': [
        "A5 'had finished' — 'By 2019' sets a past deadline; the action is earlier than a past "
        "reference point.",
        "A6 tests agreement: 'were playing / was resting' — the second clause may be past "
        "continuous or past simple; both are accepted in the key where listed.",
        "B3 'When I arrived, he had already left.' — the classic order fix; accept the version "
        "with 'already' moved after 'had'.",
        "B5 'while' — 'when' would be wrong here because the phone rang inside an ongoing "
        "bath; actually accept 'when I was having a bath' only if the learner restructures the "
        "clause — explain the difference live.",
        "B6 is open — credit any version with a background + event + wet outcome; do not grade "
        "creativity.",
    ],
    'pair_model': "A: Last winter I was driving to Mazar when the snow started. B: Was the road "
                  "open? A: Yes, but by the time we reached the tunnel, traffic had stopped for "
                  "an hour. We waited, drank tea from a thermos, and finally turned back. B: What "
                  "did you do then? A: We stayed in a guesthouse — it became the best part of the "
                  "trip.",
    'assess': [
        "Checklist listening: background present? order logical? past perfect for the earlier "
        "action? ending explains why it mattered?",
        "Accept any story that meets the four criteria; do not require every target structure "
        "in every story.",
        "If a learner's story lacks the earlier past, prompt once after the retell: 'What had "
        "already happened?' and listen for the repair.",
    ],
    'inter': [
        "Provide the board shape (BACKGROUND → EVENTS → EARLIER → ENDING) as a visible scaffold "
        "during pair work.",
        "Offer sequence starters: First… / Then… / Suddenly… / By the time… / Finally…",
        "Remediation: learners who omitted past perfect re-tell a 30-second version using one "
        "'had + participle' clause before the Real Talk Challenge.",
    ],
    'adv': [
        "Discuss: when does 'would + verb' sound nostalgic rather than merely repeated? (habit "
        "narratives)",
        "Upgrade: produce a 'had been waiting an hour when…' sentence about a real delay.",
        "Peer challenge: listeners award one point per correctly used level (background/events/"
        "earlier) — highest total wins.",
    ],
    'errors': [
        "'When I arrived, he left.' for the earlier action → 'When I arrived, he had left.' — "
        "fix: timeline on the board with two past points; learners place the earlier event.",
        "'While I was walking, I had seen a friend.' → 'I saw' — fix: while marks the scene, "
        "not the earlier past; re-sort four sentences into while/when/by the time.",
        "Sequences without connectors ('…then…then…') — fix: require one connector per event in "
        "the next retell.",
    ],
    'short': [
        "Parts 1–4 fixed at 15 + 10; pair stories limited to 90 seconds with one follow-up.",
        "Advanced upgrade becomes the homework sentence set.",
        "Real Talk Challenge: tell once only; the 'better second telling' moves to the next "
        "lesson's warm-up.",
    ],
    'review_note': [
        "Exit ticket: one sentence containing both 'while' and 'by the time'.",
        "Keep the story-shape board for Lesson 16's integrated story round.",
        "If past perfect is shaky class-wide, reopen Formula Book card 2 at the next session.",
    ],
    'feedback': "After each two-minute story, listeners retell it in three sentences — the "
                "retell itself is feedback on clarity; add your structural note only then, and "
                "always for the class, never for one speaker.",
}

T3 = {
    'objectives': [
        "Form direct and indirect (polite) questions with correct word order.",
        "Sustain a three-minute interview using content-based follow-up questions.",
        "Distinguish subject questions from object questions when speaking.",
    ],
    'success': [
        "no inverted-word-order errors across six spoken questions",
        "at least three follow-ups react to the content of an answer, not just the topic",
        "one indirect question used naturally in the pair task",
    ],
    'prep': [
        "Board: question frame (Aux + subject + verb) and embedded frame (question word + "
        "subject + verb).",
        "Optional: soft-openers strip for weaker learners (Could you tell me… / Do you know…).",
        "Two-column board section for direct vs indirect examples.",
    ],
    'timing': _t(5, 7, 3, 11, 9),
    'procedure': {
        'hook': [
            "Round one: learners find out three things about their partner under the follow-up "
            "rule — one follow-up after every answer.",
            "Stop the class halfway and praise one genuine content follow-up you heard.",
            "Ask: 'Who kept the conversation alive? How?' — expect: questions about details.",
        ],
        'rule': [
            "Teach Rule 1 with the formula boxes; drill 'Do you live here? / Where do you live?' "
            "as a pair.",
            "Flag the subject-question exception with 'Who called you?' — contrast 'Who did you "
            "call?' on the board.",
            "Rule 2 (indirect): build one together: 'Where is the bank?' → 'Could you tell me "
            "where the bank is?' and mark the no-inversion point.",
            "Rule 3: read the follow-up stems aloud; learners repeat all six.",
        ],
        'diff': [
            "Side-by-side table drill: say the direct form, pairs produce the indirect form "
            "before reading the column.",
            "Board race: two teams transform 'What time does it open?' and 'Why are you late?' "
            "— fastest correct word order wins.",
            "Subject vs object: learners sort 'Who broke the window?' vs 'Who did you call?' "
            "into the right pattern.",
        ],
        'practice': [
            "Practice A (6 items) — pairs first, then whole-class keys; insist on full question "
            "forms spoken aloud.",
            "Practice B (6 tasks): B4 follow-ups and B6 are spoken demonstrations, not written "
            "answers.",
            "Key display after pair check; drill any item with missing inversion.",
        ],
        'pair': [
            "Assign A/B roles, run three minutes, swap. Monitor for follow-ups with a tally on "
            "the board.",
            "Replay one strong exchange for the class (heard during monitoring).",
            "Summarise: what did you learn about your partner? One sentence each.",
        ],
        'advanced': [
            "Intermediate base: two orders drilled plus five soft openers shadow-read.",
            "Advanced upgrade: negative questions for surprise, echo questions, and two question "
            "tags — each learner uses one in a real exchange.",
            "Discussion: when does a negative question sound suspicious rather than interested?",
        ],
        'realtalk': [
            "Run exactly as printed: partner gives one starter sentence; conversation must last "
            "two minutes on questions and short reactions.",
            "Coach B to open with a content follow-up within two seconds of the starter.",
            "Compare with the model dialogue: underline its indirect question and reactions, "
            "then note one line from learners' own conversation that was better.",
        ],
        'review': [
            "Cover and perform: one direct + one indirect question about the same thing.",
            "Whole-class chorus of three follow-up stems.",
            "Self-check; unticked boxes return to Rule 2 and B3 for correction.",
        ],
    },
    'checking': [
        "Thumbs: 'Do you know where is the bank?' correct? (no — thumbs down, then rebuild it).",
        "Fast transform: teacher says a direct question; pairs say the indirect version.",
        "'Who called you?' — is there an auxiliary? Why not? (who is the subject)",
    ],
    'notes': [
        "A3 'the library is' — embedded statement order is the whole point; any inversion here "
        "is the target error.",
        "A5 'wrote' vs A6 'did / write' — the pair exists to prove subject vs object questions "
        "differ; walk the pair on the board every time.",
        "B1/B2 accept any correct soft opener with proper embedded order — the opener may vary "
        "(Could you tell me / Do you know / I was wondering).",
        "B4 is open: credit two genuine content follow-ups (about what was said), not two "
        "topic switches.",
        "B6 open: any 'How long…' question with correct indirect or direct order as asked.",
    ],
    'pair_model': "A: Do you know how you usually spend your weekends? B: I usually study in the "
                  "morning and visit family in the evening. How about you? A: I play football on "
                  "Fridays. B: Really — how long have you been playing? A: Since school. B: What "
                  "was the proudest moment you've had this year? A: Passing my driving test. B: "
                  "That's great. What are you going to do to celebrate it?",
    'assess': [
        "Tally board: follow-ups heard per pair — the printed criteria (order, content follow-up, "
        "flow, equal talk) decide success, not accent or speed.",
        "If the conversation stalls twice, the listener may use a printed stem — that is still "
        "success for Intermediate; Advanced should manage without stems.",
        "No numeric score; record who needs the word-order repair drill for the next lesson.",
    ],
    'inter': [
        "Allow the soft-opener strip during the interview; fade it in the second round.",
        "Sentence starters: 'What happened next?' · 'How did that feel?' · 'How about you?'",
        "Remediation: if embedded order slips, re-run B3 orally with three different question "
        "words before the Real Talk Challenge.",
    ],
    'adv': [
        "Discussion: 'Haven't you finished?' — what does the speaker assume? Contrast with "
        "'Have you finished?'",
        "Upgrade: add one question tag to a statement about the partner's answer and check the "
        "auxiliary aloud.",
        "Precision drill: rewrite one blunt question in three polite registers for a professor, "
        "a colleague, a friend.",
    ],
    'errors': [
        "'Do you know where is the bank?' → '…where the bank is?' — fix: draw the embedded frame "
        "and rebuild three questions with question-word cards.",
        "'Did she called you?' → 'Did she call you?' — fix: after do/did, base verb only; "
        "rapid-fire five verbs after 'did'.",
        "Follow-ups that switch topic ('Nice. Do you like pizza?') — fix: require 'What… about "
        "X?' referring to the answer's content; model one recast.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; pair interview runs two topics instead of three.",
        "Advanced upgrade (echo/negative/tags) becomes the optional finishers' task.",
        "Real Talk Challenge: 90 seconds of conversation, keeping the starter-sentence format.",
    ],
    'review_note': [
        "Exit ticket: each learner asks one indirect question to the teacher before leaving.",
        "Collect nothing; the pairs' spoken accuracy is the data.",
        "Carry three follow-up stems into Lesson 4's negotiation warm-up.",
    ],
    'feedback': "Praise the follow-up that showed listening ('You asked about the interview, not "
                "just the topic') — name the behaviour you want; correct word order after the "
                "round, using two anonymous examples.",
}

T4 = {
    'objectives': [
        "Select modals by meaning — ability, advice, obligation, permission, possibility — at "
        "the right strength.",
        "Distinguish deduction (can't be) from prohibition (mustn't) in speech.",
        "Handle a polite role-play request or complaint using soft modal forms.",
    ],
    'success': [
        "modals in the role-play match intended strength in at least 5 of 6 cases",
        "two polite request forms used without prompting",
        "one correct deduction about visible evidence (must be / might be / can't be)",
    ],
    'prep': [
        "Board meanings map: ability · advice · obligation · permission · possibility · certainty.",
        "Role cards optional: delayed order · bad hotel room · missed class.",
        "Note deduction clues on the board (car gone, light on, bag packed) for Rule 2.",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Run the two hook situations as a quick pair warm-up: advice for 'My English is not "
            "improving', then the early-leave request.",
            "Take two responses whole-class and place each on the meanings map.",
            "Tell learners today's job: choosing strength, not just meaning.",
        ],
        'rule': [
            "Rule 1: read the formula line; drill 'no -s, no to' with three wrong forms first "
            "(he cans / he can to swim) so learners hear the error.",
            "Rule 2: build the deduction ladder from visible evidence in the room ('The door is "
            "closed — she must be out').",
            "Rule 3: model two polite requests; pairs shadow both, then create one.",
        ],
        'diff': [
            "Table 1 as a sorting chant: strong advice / external rule / gentle advice — teacher "
            "reads sentences, class holds up 1/2/3 fingers.",
            "Board the can't vs mustn't contrast in big letters with one example each; ask for a "
            "new pair from learners.",
            "Could vs was able to: quick oral check — general ability vs one past achievement.",
        ],
        'practice': [
            "Practice A (6) solo then pairs; A3/A4 (certainty vs prohibition) need spoken "
            "justification.",
            "Practice B (6): pairs perform B1 and B5 aloud as mini-dialogues.",
            "Key after checking; on any confusion between mustn't and can't, stop and rebuild "
            "Rule 2 before continuing.",
        ],
        'pair': [
            "Negotiation task: give a two-minute thinking window for the budget choice; monitor "
            "for polite forms with a tally.",
            "Require an announced decision: 'Our team has decided… because…'",
            "Two pairs perform; class listens for strength choices only.",
        ],
        'advanced': [
            "Intermediate base: job-based sorting of modals and the three deductions drill.",
            "Advanced upgrade: 'must have + participle' past deduction, 'would' preference, and "
            "diplomatic hedged obligation — one true sentence each.",
            "Discussion: why is 'We ought to reconsider' safer than 'We must change this' with a "
            "manager?",
        ],
        'realtalk': [
            "Role cards out; one minute per role as printed; teacher joins a pair if numbers "
            "are odd.",
            "Model response uncovered only after both roles are played once.",
            "Underline the model's strength ladder (wondering → could → must be → should), then "
            "run a second round with one upgraded form per speaker.",
        ],
        'review': [
            "Three deductions about the room, spoken chorally: must be / might be / can't be.",
            "Two very polite requests from different learners.",
            "Self-check; unticked boxes redo A4 and B4 orally.",
        ],
    },
    'checking': [
        "'You mustn't tell anyone' — meaning? (forbidden) vs 'You can't be serious' — meaning? "
        "(deduction)",
        "Show an action: learners fire three advice modals at it (should / could / might).",
        "One wrong form on the board ('He cans swim') — whole-class repair.",
    ],
    'notes': [
        "A4 'mustn't' — prohibition is the only reading for 'touch the wires'; 'can't' would "
        "mean inability or deduction and fails the context.",
        "A5 accepts 'might / could / may' — 50% possibility; 'must' would overstate the "
        "evidence.",
        "B3 accepts 'might have missed / may have missed' — past possibility; 'must have missed' "
        "is wrong (too certain) unless learners justify new evidence.",
        "B4: the fix changes deduction to 'can't be' — learners must state why (lights off = "
        "evidence, not rule).",
        "B5 'No, not at all' — teach the counter-intuitive answer to 'Would you mind…?' explicitly "
        "every time.",
    ],
    'pair_model': "A: We should choose the training course — the team needs it more than the "
                  "weekend trip. B: We mustn't forget the budget, though. A: True, but we could "
                  "cut the trip cost instead. B: Then you could offer to run the training "
                  "yourselves — that saves the trainer's fee. A: Deal, I'll have the materials "
                  "prepared by Friday. B: And the manager might approve the extra day if we show "
                  "him the plan.",
    'assess': [
        "Live tally against the four criteria; the decision must be reached and explained or "
        "the task is incomplete.",
        "Accept any modal set that shows correct strength; politeness is judged by form, not by "
        "volume or accent.",
        "If deduction language is absent, prompt once with a board clue ('His car is here…') "
        "during the feedback phase.",
    ],
    'inter': [
        "Meaning map stays visible during pair work; learners point before they speak.",
        "Frames: 'You should…' · 'Could I possibly…?' · 'She must be…'",
        "Remediation: if mustn't/can't keeps flipping, run the two-column correction drill from "
        "the errors box before Real Talk.",
    ],
    'adv': [
        "Discussion: compare 'You must see this film' (speaker enthusiasm) with 'You have to see "
        "a film' (external rule) — where is the force coming from?",
        "Upgrade: report a past deduction about a friend ('You must have been exhausted').",
        "Precision: rewrite a direct order for a client at three politeness levels.",
    ],
    'errors': [
        "'He mustn't be at home' for deduction → 'He can't be at home' — fix: evidence vs rule "
        "drill with three pictures.",
        "'Would you mind to open…?' → '…opening…' — fix: mind + -ing chorus with five verbs.",
        "'He cans swim' / 'he can to swim' → 'he can swim' — fix: modal + base verb flash "
        "practice.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; negotiation scenario runs one option, not a three-way choice.",
        "Real Talk: first role only in class; second role becomes a written dialogue for "
        "homework.",
        "Upgrade sentences move to the self-check as spoken homework.",
    ],
    'review_note': [
        "Exit ticket: one deduction and one polite request per learner.",
        "Revisit the deduction ladder at the start of Lesson 5 (modal review warm-up).",
        "Collect the negotiation decisions if you need a written accuracy sample.",
    ],
    'feedback': "During the negotiation, only tick politeness and strength on the tally; give "
                "the detailed modal-strength feedback in the three-minute repair afterwards, "
                "using learners' own lines.",
}

T5 = {
    'objectives': [
        "Build accurate zero, first, second, third and mixed conditional sentences in speech.",
        "Select the conditional type that matches real vs unreal time in a decision task.",
        "Give hypothetical advice and past reflection using the correct forms.",
    ],
    'success': [
        "all five types appear correctly in oral drill or story chain",
        "if-clauses about the future use present simple without will",
        "the Real Talk decision includes a first, a second, and a third or mixed conditional",
    ],
    'prep': [
        "Board timeline: NOW-FACT · NOW-UNLIKELY · PAST-NEVER · PAST→NOW.",
        "Colour-coded if-clause / main-clause cards (optional but effective).",
        "Formula Book card 5 for display during practice.",
    ],
    'timing': _t(4, 8, 3, 11, 9),
    'procedure': {
        'hook': [
            "Quick round: pairs answer the three hook conditionals aloud — notice which verb "
            "shapes they already produce.",
            "Collect one answer of each type on the board before teaching anything.",
            "Tell learners the lesson names and tunes what they just attempted.",
        ],
        'rule': [
            "Teach Rules 1–3 as one family: real (zero/first) → unreal now (second) → unreal "
            "past (third) → mixed. Use each Examples line as choral drill.",
            "Rule 4 variations: unless / provided / formal should-inversion — read once, drill "
            "'unless' only.",
            "Stress the will-in-if-clause qualification from the remember line: willingness "
            "will is possible; ordinary future conditions take present simple.",
        ],
        'diff': [
            "Second vs third table: pairs transform the two rows aloud and state the time "
            "difference ('now' vs 'then').",
            "Type 3 vs mixed: ask 'Where is the result?' for each sentence — past or present.",
            "One-minute board race: learners sort five sentences under the four timeline "
            "headings.",
        ],
        'practice': [
            "Practice A (6): individual (4 minutes) + pair check; A3/A4 must be read aloud with "
            "full forms.",
            "Practice B (6): transformations spoken in pairs; B5 and B6 are open — take two "
            "samples.",
            "Key display; for any will-in-if error, pause and re-run Rule 1's remember line.",
        ],
        'pair': [
            "Chain game: start the printed opening; each learner adds one sentence within five "
            "seconds (keeps it unscripted).",
            "Tally types used per pair; demand one third and one mixed before finishing.",
            "Second chain only if the first ran smoothly; otherwise set it as the extension.",
        ],
        'advanced': [
            "Intermediate base: one living example per type, then short-form drills aloud "
            "(If I'd… / we wouldn't have…).",
            "Advanced upgrade: inverted conditionals, 'but for', and 'suppose…' — produce one "
            "each, then judge which register they fit.",
            "Discussion: which of the three sounds most formal, and where would you use it?",
        ],
        'realtalk': [
            "Planning: learners assign conditional jobs exactly as the plan box instructs.",
            "One minute of speech to a partner; partners listen for the three required types "
            "with the feedback ticks.",
            "Model uncovered; pairs compare the model's choices (first/second/third-mixed) with "
            "their own, then re-deliver one improved line.",
        ],
        'review': [
            "Covered page: one example of each of the five types (choral then individual).",
            "Turn a real regret into a third conditional — two volunteers.",
            "Self-check; unticked boxes redo the matching A items.",
        ],
    },
    'checking': [
        "'If it will rain' — acceptable for ordinary future? (no; willingness only) rebuild it.",
        "Call a type ('mixed!') — pairs produce a sentence within five seconds.",
        "'unless' sentence from the class — confirm no double negative.",
    ],
    'notes': [
        "A3 'were / would apologise' — 'If I were you' is the standard advice frame; accept "
        "'was' informally but keep 'were' as the taught model.",
        "A5 'knew / would call' — present unreal; 'would' belongs in the main clause only.",
        "B2 accepts 'If he had studied, he wouldn't have failed' — learners often add 'so' — "
        "explain that if and so do not coexist in one clause pair.",
        "B3 accepts 'could buy' or 'would be able to buy' — both correct for the past→present "
        "mixed type.",
        "B5/B6 are open: accept any coherent second conditional advice or prize answer that "
        "keeps if-clause present simple.",
    ],
    'pair_model': "A: If I had woken up early, I would have caught the first bus. B: If I had "
                  "caught the first bus, I would have arrived before the rain. A: If it had "
                  "rained all morning, the streets would have flooded — and if I had been at "
                  "work, I would be tired now. B: If I were you, I'd check the weather before "
                  "travelling tomorrow.",
    'assess': [
        "The feedback ticks (first/second/third-mixed/logic) are the assessment — count types "
        "heard, do not score grammar mid-speech.",
        "Accept any logically consistent chain; the model is one path through the task.",
        "If mixed conditionals dominate wrongly, note it and re-drill the type-3 form in the "
        "review phase.",
    ],
    'inter': [
        "Timeline board stays visible; learners point to the time before choosing the form.",
        "Frames: 'If I had + past perfect, I would have + participle' on a desk card.",
        "Remediation: learners who miss type 3 re-do A4 and B2 aloud before the Real Talk "
        "Challenge.",
    ],
    'adv': [
        "Discussion: 'Had I known…' vs 'If I had known…' — where does inversion belong?",
        "Upgrade: 'But for your help…' replacing a full if-clause; two true examples.",
        "Register check: which of unless / provided / should you require fits a contract vs a "
        "text?",
    ],
    'errors': [
        "'If it will rain…' → 'If it rains…' — fix: future-in-if drill with five verbs; mention "
        "willingness will only if asked.",
        "'If I would have known' → 'If I had known' — fix: main-clause-only-would sorting "
        "exercise.",
        "'unless you don't hurry' → 'unless you hurry' — fix: unless = if not; learners expand "
        "three unless sentences both ways.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; the chain runs one round of six sentences.",
        "Upgrade task becomes homework (one inverted conditional).",
        "Real Talk: first option only (training/equipment/trip consequences) — the past "
        "reflection moves to the self-check prompt.",
    ],
    'review_note': [
        "Exit ticket: one third conditional about today.",
        "Formula card 5 is the revision sheet for Test 2 — point learners to it now.",
        "Rehearse mixed conditionals again before Review Test 2 (they appear there).",
    ],
    'feedback': "During chains, correct only form collapses that block the listener; otherwise "
                "collect two errors per chain and repair them as a class puzzle afterwards.",
}

T6 = {
    'objectives': [
        "Express present wishes, past regrets and preferences with accurate verb forms.",
        "Use would rather and it's time with correct tense patterns in speech.",
        "Deliver a one-minute regret-and-advice turn using both wish types.",
    ],
    'success': [
        "wish + past vs wish + past perfect chosen correctly in 4 of 5 spoken examples",
        "would rather matches subject and tense in both personal and interpersonal cases",
        "the Real Talk response contains one past regret, one present wish, and advice",
    ],
    'prep': [
        "Board: WISH-NOW (past) · WISH-THEN (past perfect) · WANT-CHANGE (would/could).",
        "Optional: complaint slips (studies, work, health) for pairs who stall.",
        "Formula Book card 6 for display.",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Learners complete the three hook stems honestly and read them to a partner.",
            "Sort three class examples on the board under now/then/ability.",
            "Set the aim: natural regrets without long if-sentences.",
        ],
        'rule': [
            "Rule 1: present wish; drill the 'time steps back one level' idea with 'I wish I "
            "knew' (but I don't).",
            "Rule 2: regret with past perfect; pair it with 'If only…!' for emotion.",
            "Rule 3: would rather and it's time as a two-line formula; chorally drill 'It's high "
            "time we started.'",
            "Rule 4: prefer and as if/as though — one real vs unreal example each.",
        ],
        'diff': [
            "Table 1: pairs transform present wish ↔ past regret and state the time.",
            "could vs would: contrast 'I wish I could come' with 'I wish you would come' — "
            "me/you and ability/willingness.",
            "'It's time' three shapes: read aloud, then learners produce their own for a real "
            "situation (late meeting, unpaid bill).",
        ],
        'practice': [
            "Practice A (6) solo with pair check; A3/A4 (as if / it's high time) need the "
            "pattern named aloud.",
            "Practice B (6): spoken rewrites in pairs; B6 is open — take two samples.",
            "Key display; drill the wish-past-perfect form if A2 was widely missed.",
        ],
        'pair': [
            "Complaint-and-fix: model one complaint-response pair first, then set the two-minute "
            "rounds.",
            "Swap roles on signal; tally wish forms and solution modals.",
            "Two pairs perform the best complaint-fix exchange for the class.",
        ],
        'advanced': [
            "Intermediate base: learners sort their own real regrets into now/then and say each "
            "aloud.",
            "Advanced upgrade: 'If only…!' for emotion, diplomatic wish+would in professional "
            "English, and 'as though nothing had happened' narrative.",
            "Discussion: when does 'I wish you would' cross from request into complaint?",
        ],
        'realtalk': [
            "Planning per the plan box: real regret, present wish, advice — verb forms decided "
            "first.",
            "One minute to a partner; feedback ticks listened for, no interruption.",
            "Model uncovered; learners underline the two wish forms in it, then compare with "
            "their own structure.",
        ],
        'review': [
            "Covered: one present wish + one past regret from each learner (round-robin).",
            "Preference about self vs about partner — two volunteers.",
            "Self-check; unticked boxes redo A1/A2 and B3 aloud.",
        ],
    },
    'checking': [
        "'I wish I have more time' — repair it live. (had)",
        "Call the time ('past regret!') — learners fire a wish sentence instantly.",
        "'I'd rather you don't' — fix it together. (didn't)",
    ],
    'notes': [
        "A4 'made' — it's (high) time + past form, not present; the meaning is 'we are late'.",
        "A6 'were' — traditional subjunctive; accept 'was' informally but keep 'were' as the "
        "careful model, as the lesson states.",
        "B3: the correction changes the verb to 'had' — learners should explain the present "
        "unreal meaning.",
        "B4 'It's time we went' — accept 'It's time we left/go'? No: bare 'go' is not the "
        "pattern taught; keep went/left.",
        "B5 'reading / watching' — parallel patterns; both must match in form.",
    ],
    'pair_model': "A: I wish I had more time for my health — I work late every day. B: We are in the same boat. Have you tried shorter workouts? A: I wish I could explain it to my manager. B: It's high time we told him — would you like me to come with you? A: Thanks, but I'd rather you didn't; I want to handle it myself.",

    'assess': [
        "Assess with the four printed criteria: correct wish forms, natural solutions, genuine "
        "tone, both roles completed.",
        "Accept any complaint topic that uses the target forms; the model is not the only "
        "content.",
        "If present/past wishes keep mixing, run the now/then board sort before the review "
        "phase.",
    ],
    'inter': [
        "Verb-form frame on the desk: 'wish + past = now · wish + had + participle = then'.",
        "Complaint starters: 'I wish I had more time for…' · 'I wish I could…'",
        "Remediation: learners redo B1 and B3 as oral drills before the Real Talk Challenge.",
    ],
    'adv': [
        "Discussion: 'We were hoping the report would be ready' — wish or complaint? Which "
        "structure and why?",
        "Upgrade: narrate one line with 'She greeted me as though we had argued yesterday.'",
        "Register: compare 'I wish you'd be quiet' with 'Would you mind keeping it down?' — "
        "when is each appropriate?",
    ],
    'errors': [
        "'I wish I have more time.' → 'I wish I had more time.' — fix: unreal present takes "
        "past form; five-verb flash repair.",
        "'I'd rather you don't smoke' → 'didn't' — fix: someone else's action takes the past "
        "form; contrast with 'I'd rather stay'.",
        "'It's time we will go.' → 'It's time we went.' — fix: no will inside it's time; two "
        "examples drilled.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; complaint round runs two areas, not four.",
        "Upgrade becomes the self-check homework line.",
        "Real Talk: 45-second version with a written plan only (no second attempt).",
    ],
    'review_note': [
        "Exit ticket: one regret and one preference said aloud.",
        "Flag wish forms for Review Test 2 (items A2/A6 test exactly these).",
        "Formula card 6 as the revision sheet.",
    ],
    'feedback': "Reacts to meaning first ('That sounded like a real regret') — this is a lesson "
                "where tone matters; then fix forms in the repair phase, choosing only the one "
                "error that appeared most often.",
}

T7 = {
    'objectives': [
        "Form comparatives, superlatives and equality patterns accurately in speech.",
        "Add degree words and reasons to make comparisons persuasive.",
        "Build a one-minute persuasion talk containing three accurate comparisons.",
    ],
    'success': [
        "no double comparatives and no then/than confusion across the lesson",
        "every comparison in the pair task is supported by a reason",
        "at least two degree words used (far, much, slightly, by far…)",
    ],
    'prep': [
        "Board: -er/-est vs more/most decision line, plus irregulars good/better/best.",
        "Optional: three real items to compare (two phones, two routes, two courses).",
        "Formula Book card 7 for display.",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Pairs complete the two comparison frames aloud with reasons.",
            "Take two examples; underline the connector 'because'.",
            "State the lesson rule: a comparison without a reason is only an opinion.",
        ],
        'rule': [
            "Rule 1: decision line short/long + irregulars; learners sort five adjectives "
            "aloud.",
            "Rule 2: as…as and the more…the more — drill the printed examples as chunks.",
            "Rule 3: degree words with meaning nuance (far vs slightly) — read the examples, "
            "learners mimic the emphasis.",
        ],
        'diff': [
            "Comparative vs superlative table: pairs explain the difference for each row in "
            "their own words.",
            "Subtle patterns: 'The sooner, the better' vs 'Sooner or later' — ask what each "
            "promises.",
            "Equality vs near-equality: choral drill 'almost as…as'.",
        ],
        'practice': [
            "Practice A (6): solo then pair; A2 superlative needs 'the' and irregular form.",
            "Practice B (6): spoken transformations; B3 and B6 require a spoken reason.",
            "Key display; run the 'more taller' repair chorus if B2 was missed.",
        ],
        'pair': [
            "Recommendation game: 30 seconds prep each, then defend; monitor for degree words "
            "with a tally.",
            "Force the joint decision: pairs must agree and justify the agreement.",
            "Two recommendations played back for class feedback against criteria.",
        ],
        'advanced': [
            "Intermediate base: irregulars and degree-word sentences about real life.",
            "Advanced upgrade: 'by far / the single most…', concessive comparison, and "
            "'compared with' data framing — one of each.",
            "Discussion: which sounds more academic — 'prices have doubled' or 'compared with "
            "2020, participation has doubled'?",
        ],
        'realtalk': [
            "Planning: three comparisons + reasons as printed; keywords only.",
            "One minute to a partner; listeners count comparisons heard.",
            "Model uncovered; learners highlight its degree words, then upgrade one of their "
            "own sentences with 'far' or 'by far'.",
        ],
        'review': [
            "Covered: one 'far' comparison, one 'the more…the more' sentence.",
            "Rank three personal things with superlatives + reasons — round-robin.",
            "Self-check; unticked boxes redo A1/A2 and B2 aloud.",
        ],
    },
    'checking': [
        "'more better' — thumbs down; repair chorally.",
        "Adjective flash (big / expensive / good): instant comparative form from the class.",
        "'better then that' — spot the error in one second (than).",
    ],
    'notes': [
        "A2 'the worst' — superlative with 'of my life' requires 'the'; irregular bad → worst.",
        "A4 'more beautifully' — adverb comparative uses more (beautifully is long); learners "
        "often keep 'beautiful' — clarify adjective vs adverb here.",
        "B1 'twice as expensive as' — the pattern is as + adj + as with the multiple before "
        "the first as.",
        "B3/B6 are open: accept any far/much/a lot + comparative + because-reason, and any "
        "coherent three-city comparison using both forms.",
        "B5 correction is only than (not then) — the meaning is untouched.",
    ],
    'pair_model': "A: Online learning is far more flexible than classroom courses because I can study after work. B: True, but classroom courses are more expensive than online ones and still worth it for discussion. A: It is the feedback that makes the difference — compared with last year, our class has doubled its speaking time. B: The more we practise online, the more confident we become; to sum up, blended learning is best.",

    'assess': [
        "Count comparisons and reasons with the ticks; a comparison without a reason does not "
        "count.",
        "Accept any topic pair; the joint decision must be stated aloud with at least one "
        "degree word.",
        "Note adjective/adverb slips (beautiful vs beautifully) for the repair phase rather "
        "than interrupting.",
    ],
    'inter': [
        "Adjective decision card: short (-er) vs long (more) with five worked examples.",
        "Reason frames: '…because it saves time' · '…especially when…'",
        "Remediation: learners redo A3 and B2 aloud before Real Talk if the pattern slipped.",
    ],
    'adv': [
        "Discussion: when does 'arguably the best' beat 'the best'? (evidence vs assertion)",
        "Upgrade: concessive comparison — 'Although X is cheaper, Y is better value over time.'",
        "Data talk: describe one real figure ('Compared with last year, enrolment has grown by "
        "a third').",
    ],
    'errors': [
        "'more taller' → 'taller' — fix: double-comparative sort with six adjectives.",
        "'better then' → 'better than' — fix: than = comparison, then = time; quick sentence "
        "pair.",
        "Comparing price with quality — fix: like-for-like rule; learners repair one mixed "
        "comparison.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; recommendation game takes one presentation each, decision "
        "included.",
        "Upgrade becomes a written finisher task.",
        "Real Talk: choose ONE prompt topic; still three comparisons with reasons.",
    ],
    'review_note': [
        "Exit ticket: one far/much + comparative about the school or city.",
        "Comparisons feed Lessons 8 and 15 (persuasion and hedging) — revisit in Test 2 "
        "preparation.",
        "Formula card 7 for revision.",
    ],
    'feedback': "During presentations, tick comparisons and reasons separately — the split "
                "shows learners which half they are missing; repair adjective/adverb choices "
                "afterwards with three class-built examples.",
}

T8 = {
    'objectives': [
        "Link ideas with the correct linker family (contrast, cause, result, purpose).",
        "Deliver a short argument with point → reason → example → summary structure.",
        "Use one concession and one counterpoint without breaking grammar rules.",
    ],
    'success': [
        "despite + noun/-ing and although + clause both used correctly at least twice",
        "the spoken argument contains all four skeleton parts",
        "the closing summary opens with a printed summariser",
    ],
    'prep': [
        "Board: four linker families in four columns (contrast / cause / result / addition).",
        "Skeleton strip: POINT → REASON → EXAMPLE → LINK/SUMMARY.",
        "Optional: debate motion written before class ('Homework should be replaced…').",
    ],
    'timing': _t(4, 8, 3, 11, 9),
    'procedure': {
        'hook': [
            "30-second talk on 'Why people learn English', then partner counts the linkers used.",
            "Tally class linkers in the four columns.",
            "Name today's aim: not more linkers — the right linkers, in the right slot.",
        ],
        'rule': [
            "Rule 1: contrast/concession — build although vs despite on the board from one "
            "idea: 'Although it rained' / 'Despite the rain'.",
            "Rule 2: cause/result — clause vs noun pairs; drill because vs because of.",
            "Rule 3: the argument skeleton — say the printed example as a script once, then "
            "learners rebuild it from four keywords.",
            "Rule 4: summarisers — choral drill of four closers.",
        ],
        'diff': [
            "Three-package table (although / despite / however): learners repack one idea "
            "three ways aloud.",
            "because vs because of: instant transformation round.",
            "while/whereas vs although: ask which one concedes — connect to Lesson 7's "
            "comparison language.",
        ],
        'practice': [
            "Practice A (6): solo + pairs; A2 (Despite being…) is the known trap — justify the "
            "choice.",
            "Practice B (6): B4/B6 spoken skeletons; B4 must literally contain point, reason, "
            "example.",
            "Key display; run the 'despite of' repair chorus unconditionally.",
        ],
        'pair': [
            "Mini-debate: positions drawn or assigned; two minutes per side, then swap.",
            "Monitor with the four required linker slots as a checklist.",
            "Require the closing summary and the joint verdict line.",
        ],
        'advanced': [
            "Intermediate base: sort ten linkers into the four families under time pressure.",
            "Advanced upgrade: 'Not only… but also' with inversion, concessive balance "
            "('Admittedly… even so…'), and clause-commenting 'which'.",
            "Discussion: why is 'which changed the whole mood' more elegant than a second "
            "sentence?",
        ],
        'realtalk': [
            "Planning: claim, two reasons, concession, linkers — keywords as printed.",
            "90 seconds to a partner without notes; listeners follow the skeleton on paper.",
            "Model uncovered; mark its four skeleton parts, then compare with the listener's "
            "notes of the learner's own talk.",
        ],
        'review': [
            "Covered: a 20-second argument with exactly three linkers (count them).",
            "Same contrast idea three ways: although / despite / however.",
            "Self-check; unticked boxes redo A1/A2 and B3 aloud.",
        ],
    },
    'checking': [
        "'Despite of' — repair live and keep it on the board as the lesson's anti-example.",
        "Call a family ('result!') — learners shout two linkers from it.",
        "'Although the cost…' — rebuild as despite or although-clause, both acceptable if "
        "grammatical.",
    ],
    'notes': [
        "A2 'Despite' — 'being very tired' is -ing, not a clause; accept the full 'Although "
        "she was very tired' only if the learner restructures.",
        "A5 'As a result' — result of cancellation; 'Although' would invert the logic.",
        "B4 must visibly contain point + reason + example — the key allows variation but not "
        "missing parts.",
        "B6 requires a printed summariser opener (To sum up / All in all / In conclusion) — "
        "any content after it is open.",
        "B3/B5 both accept the two grammatical repairs listed; if a class prefers 'Although "
        "the cost was high', it is equally correct — say so aloud.",
    ],
    'pair_model': "A: I believe homework should be replaced by daily speaking practice. B: Although speaking is important, homework teaches discipline. A: Despite the need for discipline, speaking every day builds fluency faster. B: However, many learners skip daily tasks. A: Therefore we need scheduled speaking slots, not less homework. To sum up, add speaking without removing homework.",

    'assess': [
        "Checklist per side: four linker slots filled, skeleton visible, counterargument "
        "answered, summary spoken.",
        "Argument quality is judged by structure and clarity, not by the position defended.",
        "If despite + clause keeps occurring, stop after the round and rebuild it with the "
        "whole class.",
    ],
    'inter': [
        "Four-column board stays visible; learners point to the column before speaking.",
        "Frames: 'Although…, …' · 'Despite + noun, …' · 'This is because…' · 'To sum up…'",
        "Remediation: pairs re-do B2 and B3 aloud before Real Talk if their debate showed the "
        "error.",
    ],
    'adv': [
        "Discussion: 'It is true that…; nevertheless…' — who are you conceding to? Build one "
        "about the debate motion.",
        "Upgrade: clause-commenting 'which' — two learners describe a manager who apologised.",
        "Precision: compare 'however' vs 'nevertheless' — strength and position in the sentence.",
    ],
    'errors': [
        "'Despite of the cost' → 'Despite the cost / In spite of the cost' — fix: two-slot "
        "board (despite | in spite of) + noun card.",
        "'Although the cost, we bought it' → 'Despite the cost…' or 'Although it was costly…' — "
        "fix: clause-or-noun sorter.",
        "Arguments that list opinions without reasons — fix: skeleton strip visible during "
        "every speaking task from now on.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; debate runs one side only plus a 30-second rebuttal.",
        "Upgrade task moves to the advanced homework sheet.",
        "Real Talk: 60-second talk; summary still required.",
    ],
    'review_note': [
        "Exit ticket: one although sentence and one despite sentence about today.",
        "The argument skeleton returns in Lessons 15–16 and the Final Assessment speaking task.",
        "Formula card 8 for revision before Test 2.",
    ],
    'feedback': "Tick the four linker slots during speeches — visible progress keeps motivation; "
                "repair the contrast family after the debate with two anonymous sentences, one "
                "corrected live.",
}

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
            ("Pair Speaking", pair), ("Say It with Greater Precision", adv),
            ("Real Talk Challenge", 10), ("Review and Self-Check", 5)]


T1 = {
    'objectives': [
        "Choose accurate verb forms for habits, temporary current situations, finished past events, "
        "experiences connected to now, and future plans or arrangements in spoken English.",
        "Explain in plain English why a finished time expression ('yesterday', 'last week', 'in 2020') "
        "requires the past simple rather than the present perfect.",
        "Deliver an unscripted one-minute account of how their English or another practical skill has "
        "improved over time, combining past simple, present perfect, and present simple/continuous.",
    ],
    'success': [
        "at least 4 of 5 Practice A items are completed accurately before the answer key is discussed",
        "corrections in Practice B are justified with a clear time or state-verb reason rather than a guess",
        "in the Real Talk Challenge, time expressions match the speaker's chosen tense consistently",
    ],
    'prep': [
        "Draw four simple columns on the board: NOW & AROUND NOW (present simple / continuous) · "
        "CLOSED PAST (past simple) · CONNECTED TO NOW (present perfect) · NEXT (future choices).",
        "No handouts are needed; learners jot down only three keywords during Real Talk planning.",
        "Optional: encourage learners to use a phone voice-memo app to record their one-minute Real Talk "
        "response so they can hear their own tense choices afterwards.",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Have pairs read the two opening sentence pairs aloud ('I live with my cousin' vs 'I'm living "
            "with my cousin until my flat is ready'; 'I lost my keys yesterday' vs 'I've lost my keys — "
            "can you let me in?'). Ask them to explain what changes in real life between each pair without "
            "using grammar terms.",
            "Give pairs two minutes to answer the two personal hook questions ('What does a normal weekday "
            "look like for you, and what temporary project are you working on this month?' and 'What is one "
            "important thing that has changed in your daily life over the past year?').",
            "Take two brief responses from the room, write the time phrases learners used under the board "
            "columns, and point out that today's lesson makes those tense choices automatic.",
        ],
        'rule': [
            "Walk through the three core rule groups in order: Rule 1 (Present tenses: baseline habits/facts "
            "vs temporary spotlight), Rule 2 (Past simple vs present perfect: closed time vs open bridge to "
            "now), and Rule 3 (Future choices: decided plan vs instant decision vs fixed calendar arrangement).",
            "Have the class read one natural example per rule box aloud so the rhythm of contractions "
            "('I'm working', 'I've sent', 'I'll carry') lands in their ear.",
            "Write 'I saw him yesterday' and 'I've spoken to her recently' on the board to show why finished "
            "time stamps lock the door on the present perfect, while 'recently' allows either tense depending "
            "on the speaker's focus.",
        ],
        'diff': [
            "Ask learners to cover the right-hand column of the 'Present perfect vs past simple' table in "
            "Part 3 and predict with a partner what the listener hears in each pair before uncovering it.",
            "Read the 'State verbs vs action verbs' section together. Contrast 'I think this course is "
            "practical' (opinion = state) with 'I'm thinking about applying for a scholarship' (active mental "
            "process happening now).",
            "Run a 30-second check: call out three time expressions ('last night', 'since 2022', 'these days') "
            "and have the class name the matching tense.",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (5 items) individually, then 1 minute to compare "
            "answers in pairs and read each completed sentence aloud.",
            "Run Practice B (4 items) in pairs: insist that for items 1 and 2, learners state both the "
            "corrected sentence and the one-sentence reason why the original failed.",
            "Confirm answers with the whole class and clarify any item where learners hesitated.",
        ],
        'pair': [
            "Read the 3-turn model exchange ('How it sounds in conversation') aloud with a volunteer so "
            "everyone hears how a natural follow-up question grows out of the partner's answer.",
            "Put learners in pairs to interview each other using the four questions in Part 5, requiring at "
            "least one unscripted follow-up question after every answer.",
            "Close the round by asking two learners to report one interesting change or current project they "
            "learned about their partner.",
        ],
        'advanced': [
            "Guide the whole class through the first block of Part 6 ('Make the core pattern automatic'): "
            "each learner says three true sentences about their own week — one permanent habit, one temporary "
            "project this month, and one experience they have had this year.",
            "Move together to the second block ('Add nuance, detail, and sharper focus'): model the present "
            "perfect continuous ('I've been revising all morning, so my eyes are tired'), a combined past-setback "
            "+ present-growth sentence, and the milestone frame 'It's the first time I've ever…'.",
            "Have pairs build one sentence of their own using either the present perfect continuous or the "
            "past-plus-present-perfect contrast and share the strongest examples with the room.",
        ],
        'realtalk': [
            "Give learners exactly 30 seconds to jot down three keywords only (one past turning point, one "
            "change up to now, and one current habit or focus) — no full written sentences.",
            "Have partners take turns speaking for one full minute while the listener tracks the four items "
            "in the Partner listening checklist. Keep the printed Model response covered during round one.",
            "Have learners uncover the Model response, notice how it links 'Last year I joined…', 'Since then, "
            "my confidence has grown…', and 'These days I listen…', and then deliver a tighter 45-second "
            "second attempt to a new partner.",
        ],
        'review': [
            "Have learners close their books and answer the two active-recall prompts in Part 8 orally with "
            "their partner.",
            "Ask everyone to tick the four 'Can I do this in real speech?' checkboxes honestly; point anyone "
            "with an unticked box to the matching rule in Part 2 and Formula Book Card 1.",
        ],
    },
    'checking': [
        "'Last year I…' — which tense follows, and why can't we use 'have + participle'? (Past simple, "
        "because 'last year' is a finished time period.)",
        "'Nadia has worked here since 2022' — does Nadia still work here today? (Yes — 'since 2022' bridges "
        "past to present.)",
        "Contrast 'I'll help you carry that' with 'We're meeting the director at ten tomorrow' — which one "
        "was arranged before this conversation?",
    ],
    'notes': [
        "A1 'saw' — 'last week' names a finished past time; 'have seen' is never grammatical with a closed "
        "time marker.",
        "A2 accepts both 'has worked' and 'has been working' — 'since 2022' connects the past to now, and "
        "both simple and continuous aspects are natural with 'work' and 'live'.",
        "A3 'are meeting / 're meeting' — a fixed personal arrangement with a specific time word ('tomorrow "
        "morning at ten') naturally takes the present continuous.",
        "B3 'have you known' — 'know' is a state verb (so not 'have you been knowing'), and 'How long' asks "
        "about a duration continuing up to now.",
        "B4 'I'm going to study medicine next year' — 'be going to' expresses a prior personal intention "
        "naturally in conversation.",
    ],
    'pair_model': "A: What are you doing these days that wasn't part of your routine six months ago? "
                  "B: I'm walking to class every morning instead of taking the bus, and I listen to English "
                  "podcasts on the way. A: That's a great habit. How long have you been doing that? B: Since "
                  "March — I've listened to about thirty episodes so far, and my listening has improved a lot.",
    'assess': [
        "Use the four Partner listening checklist items as live criteria while circulating; do not interrupt "
        "speakers mid-minute.",
        "Credit any natural response that names a specific past turning point (past simple), explains progress "
        "up to now (present perfect), and describes current habits or projects (present simple/continuous).",
        "Note two recurring tense/time mismatches anonymously on your notepad for a three-minute whole-class "
        "board repair after the speaking round.",
    ],
    'inter': [
        "Keep the four-column board timeline visible throughout Pair Speaking and Real Talk so hesitant "
        "speakers can glance at the time cues before choosing a verb form.",
        "Offer simple spoken starters on the board: 'Last year I…' · 'Since then, I have…' · 'These days, I'm…'",
        "If a learner struggles with finished vs open time in Practice B1, practice swapping 'last night' and "
        "'so far this week' on the same sentence aloud before starting Part 5.",
    ],
    'adv': [
        "Invite confident speakers to weave past simple, present perfect, and present perfect continuous into "
        "their Part 5 follow-up answers (e.g., explaining both how a change started and how long they have "
        "been working on it).",
        "Ask early finishers in Part 6 to explain the subtle difference between 'I've spoken to her recently' "
        "and 'I spoke to her recently' using a real example from their week.",
        "During the second Real Talk round, challenge confident speakers to include one 'It's the first time "
        "I've…' or 'This is the most… I've ever…' milestone frame naturally.",
    ],
    'errors': [
        "'I have finished my assignment last night.' → 'I finished my assignment last night.' — Fix: ask "
        "'Is last night finished?' Whenever a closed time stamp appears, use the past simple.",
        "'She is knowing three foreign languages.' → 'She knows three foreign languages.' — Fix: remind "
        "learners that mental states ('know', 'believe', 'understand') stay in the simple form.",
        "'We will meet the director tomorrow at ten' for an existing appointment → 'We're meeting the director "
        "tomorrow at ten.' — Fix: reserve 'will' for spontaneous offers/predictions and use present continuous "
        "for calendar arrangements.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; run questions 2 and 4 in Pair Speaking with one follow-up each.",
        "Do the first block of Part 6 orally in class and assign the three nuance sentences in the second "
        "block as short spoken/written homework.",
        "Run one 60-second Real Talk round followed by a brisk two-minute model comparison and exit check.",
    ],
    'review_note': [
        "Use the two closed-book recall prompts in Part 8 as a quick oral exit ticket.",
        "Remind learners that both 'has worked' and 'has been working' are accepted in Appendix 5 for open "
        "durations with 'since' and 'for'.",
        "Open Lesson 2 next session by asking three learners to share one sentence about yesterday (past "
        "simple) and one about their week so far (present perfect).",
    ],
    'feedback': "While pairs speak, jot down two strong tense contrasts you hear and two anonymous sentences "
                "where a finished time word clashed with 'have/has'. Put both on the board after Part 7 and "
                "let pairs repair the slips together in 60 seconds.",
}

T2 = {
    'objectives': [
        "Tell a clear personal story that separates the background scene (past continuous), the main "
        "events (past simple), and an earlier past action (past perfect).",
        "Use time and sequence markers ('while', 'when', 'by the time', 'at first', 'suddenly', 'in the "
        "end') to guide the listener smoothly through a narrative.",
        "Deliver an unscripted two-minute story about a memorable trip, problem, or surprise and retell "
        "it more concisely in a second round.",
    ],
    'success': [
        "each spoken story includes at least one background clause (past continuous) and one earlier-past "
        "clause (past perfect)",
        "the partner can retell the key events in the exact order they happened without confusion",
        "at least three natural sequence markers are used to connect the stages of the story",
    ],
    'prep': [
        "Write the four-part story arc across the board: SCENE (was/were -ing) → MAIN EVENTS (past simple) "
        "→ EARLIER CAUSE (had + participle) → ENDING / TAKEAWAY.",
        "Write the contrast pair 'When the guests arrived, we cooked dinner' vs 'When the guests arrived, "
        "we had cooked dinner' on the board for Part 1.",
        "Have a visible timer ready for the 10-second silent planning window in Part 7.",
    ],
    'timing': _t(4, 7, 4, 12, 8),
    'procedure': {
        'hook': [
            "Have pairs read the two dinner sentences in Part 1 aloud and decide in which house the guests "
            "ate immediately and in which house they had to wait.",
            "Give each learner 60 seconds to tell their partner a brief story about a small problem from "
            "the past month (a late bus, a forgotten item, or a sudden change of plan) while the listener "
            "notices how the background scene was set.",
            "Highlight how the three past tenses act like camera depth — background, foreground action, and "
            "flashback — so the listener never gets lost.",
        ],
        'rule': [
            "Teach Rule 1 (the three past levels) using the board arc: past continuous for the scene in "
            "progress, past simple for the chain of events, and past perfect for what had already happened "
            "before the main moment.",
            "Teach Rule 2 ('when', 'while', and 'by the time'): have the class chorally practise 'While I "
            "was walking down the street, the rain started' and 'By the time we reached the stop, the bus "
            "had already left.'",
            "Teach Rule 3 (story shape and sequence markers), emphasising that a memorable story closes with "
            "why the moment mattered.",
        ],
        'diff': [
            "Walk through the three-column table in Part 3 ('Same situation, three different time signals') "
            "so learners see how changing one verb form changes the timeline of the train and the meeting.",
            "Read the four-stage story arc table together ('Stage 1: Set the scene' to 'Stage 4: Give the "
            "outcome and takeaway') as a blueprint for Parts 5 and 7.",
            "Ask: 'Which tense answers What was already in progress?' (past continuous) and 'Which tense "
            "answers What had already happened earlier?' (past perfect).",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, followed by a 1-minute "
            "pair check focusing on how 'by the time' (A2) and 'by 2019' (A5) trigger the past perfect.",
            "Run Practice B (6 items) in pairs: learners combine and repair items B1–B5 aloud and then build "
            "their two-sentence rain story for B6.",
            "Check answers whole-class and have two volunteers read their B6 mini-stories aloud.",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how a listener asks a curious "
            "mid-story question ('Did you miss your stop?') that prompts a past perfect explanation.",
            "Give each partner two minutes to tell a true story from one of the four prompts in Part 5 while "
            "the listener prepares two follow-up questions and a three-sentence retell.",
            "After both partners have spoken, ask two listeners to share their three-sentence retell with "
            "the class.",
        ],
        'advanced': [
            "Work through the first block of Part 6 ('Make the core pattern automatic') together: have pairs "
            "take one simple event ('I missed the bus') and expand it aloud into a 30-second story using "
            "'while', 'when', and 'by the time'.",
            "Move to the second block ('Add nuance, detail, and sharper focus'): introduce 'would + base verb' "
            "for nostalgic past routines, the past perfect continuous ('had been waiting for an hour when…') "
            "for duration before a past event, and a present perfect takeaway ending ('It taught me a lesson "
            "I've never forgotten').",
            "Have each learner craft one closing takeaway sentence for the story they told in Part 5.",
        ],
        'realtalk': [
            "Give learners 10 seconds of silent mental planning (no writing) to picture the opening scene, "
            "the main turning point, and the earlier past cause of their story.",
            "Round 1: Learners tell their two-minute story to Partner A while Partner A checks the four items "
            "in the Partner listening checklist.",
            "Have learners read the printed Model response, notice its sequence markers and closing reflection, "
            "and then switch to Partner B to tell the same story a second time — smoother, clearer, and more "
            "concise.",
        ],
        'review': [
            "With books closed, have pairs complete the two oral retrieval tasks in Part 8 (explaining the "
            "difference between 'When I arrived, they left' and 'When I arrived, they had left', and telling "
            "a three-sentence mini-story with 'while' and 'by the time').",
            "Have learners tick the self-check boxes and review Formula Book Card 2 if any box remains unticked.",
        ],
    },
    'checking': [
        "'While I was walking' vs 'When I walked' — which connector naturally introduces a longer background "
        "action in progress? ('While' + past continuous.)",
        "Write 'By the time we arrived, the film had started' on the board — which happened first, our arrival "
        "or the start of the film? (The start of the film.)",
        "Can we use 'would' for a past state like 'We would live in a small house'? (No — use 'used to live' "
        "for past states, and 'would' only for repeated past actions.)",
    ],
    'notes': [
        "A5 'had finished' — 'By 2019' establishes a past cut-off point, so an action completed before that "
        "point takes the past perfect.",
        "A6 'were playing / was resting' — two simultaneous background actions in the past naturally take "
        "the past continuous in both clauses.",
        "B3 'When I arrived at the hall, the speaker had already left' — repairs the timeline so the departure "
        "clearly precedes the arrival.",
        "B5 'while' — 'was having a shower' is a longer background action interrupted by the doorbell.",
        "B6 is open-ended — credit any natural two-sentence story that combines 'was/were raining' (scene), "
        "'had forgotten' (earlier past reason), and 'got soaked' (main event).",
    ],
    'pair_model': "A: Last winter I was travelling home on the evening train when the power suddenly went out. "
                  "B: Did you get stuck for long? A: Almost an hour — by the time the backup generator started, "
                  "my phone battery had already died because I hadn't charged it at work. B: How did you let "
                  "your family know? A: A kind passenger lent me his phone, which turned a stressful evening "
                  "into a great conversation.",
    'assess': [
        "Listen against the four Partner listening checklist criteria: opening scene (past continuous), "
        "clear sequence markers, earlier-past flashback (past perfect), and a meaningful closing line.",
        "Accept any authentic personal story; if a speaker forgets to include a past perfect clause, ask one "
        "natural question at the end ('What had already happened before you got there?') to elicit it live.",
        "Compare the first and second tellings in Part 7 — praise smoother pacing and clearer time signalling "
        "in the second round.",
    ],
    'inter': [
        "Leave the four-stage story arc on the board during Parts 5 and 7 so developing speakers can point "
        "to each stage as they move through their story.",
        "Provide five sequence starters on the board: 'It was a… afternoon and I was…' · 'At first…' · "
        "'Suddenly…' · 'By the time…' · 'In the end…'",
        "If a learner strings everything together with 'and then… and then…', have them pause and insert "
        "one 'while' scene and one 'because I had…' reason before the Real Talk round.",
    ],
    'adv': [
        "Encourage confident speakers to open their story with a nostalgic routine ('Whenever we visited "
        "my grandparents, we would…') before shifting into the specific day's events.",
        "Challenge stronger speakers to include one past perfect continuous clause ('We had been driving for "
        "three hours when…') to build tension before the turning point.",
        "Ask listeners in confident pairs to challenge one detail with a follow-up question that requires "
        "a past perfect answer ('Why hadn't you checked the schedule earlier?').",
    ],
    'errors': [
        "'When I arrived at the hall, the speaker already left.' → '…the speaker had already left.' — Fix: "
        "draw two points on a timeline and label the earlier past point 'had + past participle'.",
        "'While I was walking home, I was seeing an old friend.' → '…I saw an old friend.' — Fix: the "
        "shorter interrupting event takes the past simple.",
        "Flat endings ('…and then I went home.') — Fix: ask 'What did that experience teach you?' to prompt "
        "a one-sentence present perfect takeaway.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; limit the Part 5 pair stories to 90 seconds per partner.",
        "Practise the 30-second expansion in Part 6 in class and assign the 'would' / 'had been -ing' "
        "extensions as homework.",
        "Run one telling in Part 7 and use the second telling as the warm-up at the start of Lesson 3.",
    ],
    'review_note': [
        "Exit ticket: each learner says one sentence combining 'while' and 'when' or 'by the time' and 'had' "
        "before leaving.",
        "Save the four-stage story arc — learners will reuse it in Lesson 13 (reporting conversations) and "
        "Lesson 16 (final synthesis).",
        "Point learners to Formula Book Card 2 in Appendix 1 for quick review.",
    ],
    'feedback': "In Part 5, let the listener's three-sentence retell serve as immediate communicative "
                "feedback: if the listener got the order of events right, the storyteller's tenses worked. "
                "Then put two anonymous timeline slips on the board for a quick whole-class repair.",
}

T3 = {
    'objectives': [
        "Form accurate direct questions (with auxiliary inversion) and polite indirect questions "
        "(with embedded statement word order) in real-time conversation.",
        "Distinguish subject questions ('Who called you?') from object questions ('Who did you call?') "
        "without inserting unnecessary 'do/does/did'.",
        "Keep a two-minute conversation flowing naturally using short reactions, content-based follow-up "
        "questions, and echo or tag questions.",
    ],
    'success': [
        "indirect questions in Practice B and Pair Speaking keep the verb after the subject ('Could you "
        "tell me where the station is?')",
        "learners ask at least three follow-up questions that react to the specific content of their "
        "partner's answer rather than changing the subject",
        "subject questions are formed without 'do/did' when 'Who' or 'What' is the subject",
    ],
    'prep': [
        "Write the two contrasting word-order frames on the board: DIRECT = Question word + Auxiliary + "
        "Subject + Verb ('Where does the bus stop?') vs INDIRECT = Polite opener + Question word + Subject "
        "+ Verb ('Could you tell me where the bus stops?').",
        "Write four quick reaction + follow-up stems on the corner of the board: 'Really? How did that "
        "happen?' · 'That sounds intense — what did you do next?' · 'How about you?'",
    ],
    'timing': _t(5, 7, 3, 11, 9),
    'procedure': {
        'hook': [
            "Have pairs read the two exchanges in Part 1 aloud — Exchange 1 (an interrogation that kills "
            "conversation) vs Exchange 2 (a natural conversation with a reaction and follow-up). Ask: 'Why "
            "does Exchange 2 feel so much more human?'",
            "Run the one-minute hook challenge: Partner A makes one simple statement ('I tried to cook a "
            "new dish last night') and Partner B must keep the conversation going for 60 seconds using only "
            "short reactions and follow-up questions.",
            "Point out that great conversationalists rely on three tools: clean question word order, polite "
            "indirect openers, and genuine follow-up questions.",
        ],
        'rule': [
            "Teach Rule 1 (Direct questions): highlight the auxiliary-before-subject pattern ('Where do you "
            "work?', 'Did she call you?'), then contrast subject questions ('Who called you?') with object "
            "questions ('Who did you call?') on the board.",
            "Teach Rule 2 (Indirect questions): show how a polite opener ('Could you tell me…', 'Do you "
            "know…', 'I was wondering if…') already does the job of asking, so the rest of the sentence "
            "returns to normal statement order.",
            "Teach Rule 3 (Follow-up questions): have the class read the three-step rhythm aloud — React "
            "briefly → Ask about a specific detail → Invite the partner back.",
        ],
        'diff': [
            "Use the Direct vs Indirect table in Part 3 as a choral call-and-response: you read the blunt "
            "direct question on the left, and the class answers with the polite indirect question on the right.",
            "Compare the Subject vs Object table ('Who broke the window?' vs 'What did the wind break?') and "
            "ask learners why 'do/did' disappears when the question word is the doer.",
            "Do a 30-second board check: write 'Do you know what time is it?' and let the class repair it aloud.",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, paying special attention "
            "to A3 (embedded word order) and the A5/A6 subject-vs-object pair.",
            "Run Practice B (6 items) in pairs: learners say their polite indirect rewrites (B1–B2), repair "
            "B3, and practise two natural follow-up questions for B4 aloud.",
            "Review the key whole-class and drill any item where 'did + past verb' ('Did she called?') appeared.",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud with a confident student, pointing out how Speaker "
            "A opens with an indirect question ('Could you tell me how you usually spend…?') and follows up "
            "on Speaker B's hiking detail.",
            "Run the three-minute pair interview (3 minutes per partner, then swap): forbid single-sentence "
            "topic jumps and require at least two content follow-ups per topic.",
            "Ask two learners to share the most surprising detail they discovered about their partner.",
        ],
        'advanced': [
            "Guide the class through the first block of Part 6 ('Make the core pattern automatic'): shadow-read "
            "the five polite openers and transform three direct questions into indirect ones without pausing.",
            "Move to the second block ('Add nuance, detail, and sharper focus'): demonstrate negative questions "
            "for surprise ('Didn't we meet at the conference?'), short echo questions ('You're moving to "
            "Herat? Really?'), and conversational question tags ('It's a great course, isn't it?').",
            "Have pairs practice a 30-second exchange that includes one echo question and one question tag.",
        ],
        'realtalk': [
            "Have each learner choose one starter statement from Part 7 (or invent a true one) and spend 20 "
            "seconds thinking of two interesting details they can share when asked.",
            "Run the two-minute unscripted conversation: Partner A says the opening sentence, and Partner B "
            "keeps the conversation alive for two full minutes using reactions, direct/indirect questions, "
            "and follow-ups — then swap roles.",
            "Uncover the printed Model response, compare how both speakers shared the floor, and highlight "
            "one strong follow-up question heard in the room.",
        ],
        'review': [
            "With books closed, have pairs ask the same question in two ways (direct for a friend, indirect "
            "for a professor) and fire three natural follow-up questions at a partner's statement.",
            "Have learners complete the self-check boxes and review Formula Book Card 3 if needed.",
        ],
    },
    'checking': [
        "'Do you know where is the bank?' — why does that sound wrong to an English listener, and how do we "
        "fix it? ('…where the bank is' — no inversion after 'Do you know'.)",
        "'Who phoned you?' vs 'Who did you phone?' — in which question are you the person making the call? "
        "('Who did you phone?')",
        "After 'Did she…', do we say 'called' or 'call'? ('call' — 'did' already carries the past tense.)",
    ],
    'notes': [
        "A3 'the library is' — embedded statement word order after 'Could you tell me where…'.",
        "A5 'wrote' (subject question — 'Who' is the author) vs A6 'did / write' (object question — 'Hamlet' "
        "is the object).",
        "B1 and B2 accept any polite opener ('Could you tell me…', 'Do you know…', 'Would you mind telling me…') "
        "provided the embedded clause uses statement order ('…what time the pharmacy closes', '…if/whether "
        "there is a cash machine near here').",
        "B4 is open — credit any two follow-up questions that react directly to passing a driving test.",
        "B6 accepts any accurate 'How long have you been…' or 'How long does it take…' question.",
    ],
    'pair_model': "A: Could you tell me how you usually spend a free Friday morning? B: I usually go for a "
                  "long walk in the hills outside town. A: Really? Who do you usually go with, and how long "
                  "does the trail take? B: I go with my older brother — it takes about two hours, and we stop "
                  "for tea on the way back. How about you?",
    'assess': [
        "Listen for the four Partner listening checklist targets: accurate direct question auxiliaries, "
        "embedded statement order in indirect questions, genuine content follow-ups, and balanced turn-taking.",
        "If a pair gets stuck, point them silently to the reaction stems on the board so they can keep the "
        "conversation moving without switching into their first language.",
        "Record two examples of inverted indirect questions anonymously for the end-of-lesson board repair.",
    ],
    'inter': [
        "Keep the two word-order frames on the board visible during Pair Speaking so developing speakers can "
        "visually check Subject + Verb order after 'Could you tell me…'.",
        "Give hesitant listeners a simple two-step formula: 'Repeat one key word + ask Why or How' (e.g., "
        "'A new dish? What did you make?').",
        "If a learner keeps saying 'Did she called?', run a 30-second oral drill ('Did you go / Did she see / "
        "Did they finish') before Part 7.",
    ],
    'adv': [
        "Challenge confident speakers to use at least one negative question ('Didn't you…?') and one question "
        "tag ('…isn't it?') naturally during their Part 5 interview.",
        "Ask stronger pairs to compare how they would ask the same sensitive question (e.g., asking for a "
        "deadline extension) to a close colleague, a department head, and an external client.",
        "During Real Talk, encourage confident speakers to use 'I was wondering whether…' for their indirect "
        "question.",
    ],
    'errors': [
        "'Could you tell me where is the station?' → 'Could you tell me where the station is?' — Fix: circle "
        "the subject ('the station') and place the verb ('is') after it.",
        "'Did she called you last night?' → 'Did she call you last night?' — Fix: remind learners that 'did' "
        "already carries the past tense, so the main verb stays in the base form.",
        "'Who did break the cup?' → 'Who broke the cup?' — Fix: when 'Who' is the person doing the action, "
        "no 'did' is used (unless stressing a contradiction).",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; run two interview prompts per partner in Part 5.",
        "Practise the polite openers in Part 6 together and set the question-tag / negative-question items "
        "as a short take-home task.",
        "Run a 90-second Real Talk round per partner and finish with the closed-book recall check.",
    ],
    'review_note': [
        "Exit ticket: each learner asks you or a classmate one polite indirect question before leaving the room.",
        "Carry the three-step follow-up habit (React → Ask a detail → Invite back) into every Pair Speaking "
        "activity for the rest of the course.",
        "Point learners to Formula Book Card 3 in Appendix 1 for review before Review Test 1.",
    ],
    'feedback': "Start your post-task feedback by quoting one follow-up question from the room that showed "
                "genuine listening. Then put two anonymous indirect-question word-order slips on the board "
                "and let pairs fix them together.",
}

T4 = {
    'objectives': [
        "Select modal verbs that match the exact social strength of a situation — advice, obligation, "
        "absence of obligation, prohibition, permission, and polite requests.",
        "Use modals of deduction ('must be', 'might/could be', 'can't be') and past deduction ('must have "
        "been', 'might have missed', 'can't have known') to reason from evidence.",
        "Resolve a delicate workplace or everyday problem in a two-minute role-play using polite requests, "
        "logical deductions, and constructive advice.",
    ],
    'success': [
        "learners clearly separate prohibition ('mustn't') from lack of obligation ('don't have to') and "
        "negative deduction ('can't be')",
        "polite requests with 'Would you mind + verb-ing?' are formed and answered accurately ('No, not at all')",
        "in the Pair Speaking and Real Talk tasks, speakers soften advice and requests rather than issuing "
        "blunt commands",
    ],
    'prep': [
        "Draw two simple scales on the board: (1) OBLIGATION & ADVICE: must / have to → should / ought to → "
        "might want to / could; (2) DEDUCTION FROM EVIDENCE: must be (95% sure Yes) → might/could be (possible) "
        "→ can't be (95% sure No).",
        "Write the classic contrast pair 'You mustn't come tomorrow' vs 'You don't have to come tomorrow' on "
        "the board for Part 1.",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Have pairs read the two situations in Part 1 aloud ('You must solve this problem today' vs "
            "'We might want to look at this problem today'; 'You mustn't come in tomorrow' vs 'You don't have "
            "to come in tomorrow') and discuss who has a relaxing Saturday!",
            "Give pairs 90 seconds to answer the two personal hook prompts (giving advice to a friend with "
            "a sore throat before a presentation, and asking a busy director to leave thirty minutes early).",
            "Show how modals act as the volume control of English — letting speakers sound diplomatic, "
            "confident, or firm without changing the topic.",
        ],
        'rule': [
            "Teach Rule 1 (Obligation, prohibition, and advice): contrast internal/strong obligation ('must') "
            "and external rules ('have to') with the crucial split between 'mustn't' (forbidden) and 'don't "
            "have to' (optional).",
            "Teach Rule 2 (Deduction from evidence): use clues in the classroom ('Her coat is on the chair, "
            "so she must be in the building'; 'The lights are off, so they can't be in a meeting') and show "
            "how past deduction uses 'modal + have + past participle'.",
            "Teach Rule 3 (Polite requests and offers): drill 'Would you mind + verb-ing?' and its natural "
            "green-light answer ('No, not at all / Of course not').",
        ],
        'diff': [
            "Walk through the two contrast tables in Part 3: first, the three-way split between 'mustn't', "
            "'don't have to', and 'can't be'; second, the difference between general past ability ('could') "
            "and a specific hard-won past success ('was able to / managed to').",
            "Have pairs test each other on the board scales: one partner names a situation ('It's a hospital "
            "no-smoking zone'), and the other picks the exact modal.",
        ],
        'practice': [
            "Give learners 4 minutes for Practice A (6 items) individually, then check in pairs — ask learners "
            "to justify A3 ('can't' for logical impossibility) vs A4 ('mustn't' for prohibition).",
            "Run Practice B (6 items) in pairs: have learners perform B1 and B5 aloud as natural mini-exchanges "
            "and explain the deduction repair in B4.",
            "Confirm the key whole-class and chorally practise 'Would you mind closing the window?' — 'No, not "
            "at all.'",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how the two committee members "
            "weigh options using 'should', 'mustn't', 'could', and 'might'.",
            "Give pairs four minutes to negotiate the workplace budget decision in Part 5 (weekend trip vs "
            "communication workshop vs coffee machine) and agree on one final choice.",
            "Have two pairs announce their final decision and reasoning to the room.",
        ],
        'advanced': [
            "Run the first block of Part 6 ('Make the core pattern automatic'): point to three real clues "
            "in or outside the classroom and have pairs make one 'must be', one 'might be', and one 'can't be' "
            "deduction aloud.",
            "Move to the second block ('Add nuance, detail, and sharper focus'): practise past deductions "
            "('They must have got stuck in traffic'), softened professional advice ('You might want to back "
            "up those files', 'It might be worth checking…'), and 'would' for polite distance ('I'd suggest…').",
            "Have each learner rewrite one blunt 'You must…' statement into a diplomatic workplace suggestion.",
        ],
        'realtalk': [
            "Have pairs choose one of the three realistic situations in Part 7 (delayed laptop repair, noisy "
            "hotel room before an exam, or a teammate who missed a deadline) and spend 30 seconds planning "
            "their opening request, deduction, and solution.",
            "Run a two-minute unscripted role-play (1 minute per role, then swap to a second situation) while "
            "listening for the four checklist items.",
            "Uncover the Model response, highlight how it layers 'I was wondering if you could…', 'It must be "
            "a busy week…', and 'Could we either… or should I…?', and have pairs try one upgraded turn.",
        ],
        'review': [
            "With books closed, have learners complete the two oral recall checks in Part 8 (explaining why "
            "'The office is dark, so he mustn't be there' is wrong, and making one polite request plus one "
            "past deduction).",
            "Have learners tick the self-check boxes and remind them that Review Test 1 follows this lesson.",
        ],
    },
    'checking': [
        "'You mustn't pay' vs 'You don't have to pay' — which one means the ticket is free? ('You don't "
        "have to pay.')",
        "'His car isn't in the car park — he (mustn't / can't) be in the office.' Which modal expresses "
        "logical impossibility? ('can't be'.)",
        "If someone asks 'Would you mind opening the window?' and you are happy to open it, do you say 'Yes' "
        "or 'No, not at all'? ('No, not at all' — meaning 'I do not mind'.)",
    ],
    'notes': [
        "A3 'can't' — evidence ('just had a huge lunch') points to logical impossibility now.",
        "A4 'mustn't' — touching live wires is dangerous and strictly forbidden.",
        "A5 accepts 'might', 'may', or 'could' — 'I'm not sure' signals 50% possibility.",
        "B3 accepts 'might have missed / may have missed / could have missed' — past possibility.",
        "B4 'He can't be at home' — repairs 'mustn't be' because dark windows are evidence for a deduction, "
        "not a rule.",
        "B5 'No, not at all. / Of course not. I'll turn it down right away.' — confirms willingness politely.",
    ],
    'pair_model': "A: I think we should choose the communication workshop because the whole team will benefit "
                  "from it all year. B: That's true, though we mustn't ignore how tired everyone has been "
                  "lately — a trip could boost morale. A: What if we book a half-day workshop and use the "
                  "remaining budget for a team lunch on Friday? B: That might be the best compromise — the "
                  "director ought to approve that easily.",
    'assess': [
        "Evaluate role-plays using the four Partner listening checklist criteria: soft request opener, "
        "accurate present/past deduction, constructive advice ('should / ought to / could'), and a clear "
        "agreed action.",
        "Judge politeness by grammatical choice and tone rather than accent or speed.",
        "Note any confusion between 'mustn't' and 'can't be' or between 'could' and 'was able to' for the "
        "closing board repair.",
    ],
    'inter': [
        "Leave the two board scales visible during Pair Speaking and Real Talk so learners can visually "
        "pick one modal from each scale during their conversation.",
        "Offer three ready-to-use role-play frames on the board: 'I was wondering if you could…' · "
        "'There must be…' · 'Perhaps we could…'",
        "If learners say 'Would you mind to help me?', chorally drill 'mind helping / mind waiting / "
        "mind checking' for 20 seconds before Part 7.",
    ],
    'adv': [
        "Encourage confident speakers to include at least one past deduction ('You must have been…' or "
        "'They might have forgotten…') naturally in both Part 5 and Part 7.",
        "Ask stronger pairs to practise diplomatic disagreement in their budget negotiation using 'That's "
        "a fair point, though we might want to consider…' and 'Wouldn't it be safer to…?'",
        "Have early finishers compare the tone of 'You must finish this by Friday', 'You need to finish "
        "this by Friday', and 'We ought to have this ready by Friday'.",
    ],
    'errors': [
        "'He mustn't be at home — the lights are off.' → 'He can't be at home.' — Fix: 'mustn't' is for "
        "rules; 'can't' is for logical deductions.",
        "'Would you mind to open the door?' → 'Would you mind opening the door?' — Fix: 'mind' is always "
        "followed by the -ing form.",
        "'The fire spread quickly, but everyone could escape.' → '…everyone was able to / managed to escape.' "
        "— Fix: for one specific past achievement, use 'was able to' or 'managed to' in affirmative sentences.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; give pairs 3 minutes for the budget decision in Part 5.",
        "Do the classroom deduction drill in Part 6 together and assign the softened workplace rewrites "
        "as homework.",
        "Run one role-play scenario in Part 7 (1 minute per partner) and finish with the Part 8 recall check.",
    ],
    'review_note': [
        "Exit ticket: each learner gives one logical deduction about something in the room and one polite "
        "request.",
        "Remind learners that Review Test 1 (covering Lessons 1–4) can now be completed in class (20 minutes) "
        "or as a timed self-check before Lesson 5.",
        "Point learners to Formula Book Card 4 in Appendix 1 for review.",
    ],
    'feedback': "Praise pairs who resolved their Part 7 complaint calmly using soft modals ('Could we…', "
                "'might want to…'). Then put two anonymous modal slips on the board and let the class repair "
                "them together.",
}

T5 = {
    'objectives': [
        "Build accurate zero, first, second, third, and mixed conditional sentences in natural speech.",
        "Choose the conditional pattern that matches whether a situation is a real future possibility "
        "(first), an imaginary present scenario (second), or an unchangeable past event (third/mixed).",
        "Weigh a complex real-life decision in a one-minute talk using at least three conditional types.",
    ],
    'success': [
        "learners use the present simple (not 'will') inside ordinary future if-clauses ('If it rains "
        "tomorrow, we'll stay inside')",
        "learners keep 'would' and 'would have' in the main result clause rather than inside the if-clause",
        "in the Real Talk Challenge, speakers combine a first conditional, a second conditional, and a "
        "third or mixed conditional coherently",
    ],
    'prep': [
        "Write four clear labels across the board: REAL HABIT/FACT (Zero) · REAL FUTURE PLAN (First) · "
        "IMAGINARY NOW (Second) · UNREAL PAST & PRESENT ECHO (Third / Mixed).",
        "Write the three airport sentences from Part 1 on the board so learners can see the shift from "
        "real plan to imaginary present to past regret.",
    ],
    'timing': _t(4, 8, 3, 11, 9),
    'procedure': {
        'hook': [
            "Have pairs read the three airport sentences in Part 1 aloud ('If we leave at six, we'll catch "
            "the early flight' / 'If we had a car, we wouldn't need a taxi' / 'If we had left at six, we "
            "wouldn't have missed the flight') and identify which speaker still has a chance to catch the plane.",
            "Give pairs 90 seconds to answer the two personal hook questions (a real plan for this weekend "
            "vs an imaginary change to their city or schedule).",
            "Explain that conditionals are not five disconnected rules — they are one system for moving "
            "from real possibilities to hypothetical thinking.",
        ],
        'rule': [
            "Teach Rule 1 (Zero and First conditionals for real situations): highlight that ordinary future "
            "if-clauses take the present simple ('If the train arrives on time, I'll call you'), while noting "
            "that 'will' can appear in an if-clause only when expressing polite willingness or refusal.",
            "Teach Rule 2 (Second conditional for imaginary present/future): show how English steps one tense "
            "back ('If + past simple → would + base verb') to signal distance from present reality, including "
            "the classic advice frame 'If I were you, I'd…'.",
            "Teach Rule 3 (Third and Mixed conditionals): contrast a purely past regret ('If I had known, I "
            "would have told you') with a past cause that shapes right now ('If she had taken that job, she "
            "would live in Herat now').",
            "Teach Rule 4 (Natural connectors beyond 'if'): practise 'unless' (= if not), 'as long as / "
            "provided that', and 'in case'.",
        ],
        'diff': [
            "Compare the two tables in Part 3: first, First vs Second Conditional ('If I have time tomorrow' "
            "vs 'If I had more free time'); second, Third vs Mixed Conditional ('wouldn't have missed the "
            "flight then' vs 'would be in Istanbul right now').",
            "Ask pairs to explain in their own words what changes when 'would have + participle' shifts to "
            "'would + base verb (now)'.",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, then compare in pairs "
            "and read each sentence aloud with natural contractions ('I'd', 'wouldn't have').",
            "Run Practice B (6 items) in pairs: learners transform B1–B4 aloud and share their personal "
            "second-conditional answers for B5 and B6.",
            "Confirm the key whole-class, pausing on B4 ('If I had known…') to reinforce why 'would have' "
            "never belongs inside the if-clause.",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how a chain story builds from "
            "third conditional to mixed conditional to second conditional advice.",
            "Run the four-minute chain game in pairs using the three starter prompts in Part 5: each partner "
            "picks up the result of the previous sentence and turns it into the next 'If…' condition.",
            "Have two pairs perform their most creative four-sentence chain for the class.",
        ],
        'advanced': [
            "Guide the class through the first block of Part 6 ('Make the core pattern automatic'): have pairs "
            "say one true sentence for each of the five conditional types and practise the spoken contractions "
            "('If I'd known…', 'She'd help if she could').",
            "Move to the second block ('Add nuance, detail, and sharper focus'): introduce formal inverted "
            "conditionals ('Should you need…', 'Were we to…', 'Had I known…'), 'But for your help…', and "
            "conversational 'Suppose / What if…?' openers.",
            "Have pairs transform one third conditional from Practice B into a formal 'Had I…' sentence.",
        ],
        'realtalk': [
            "Give learners 30 seconds to plan their one-minute talk on a major life or career decision "
            "(or a past turning point), jotting down keywords for one first conditional, one second "
            "conditional, and one third or mixed conditional.",
            "Partners take turns speaking for one full minute while the listener ticks the four criteria "
            "in the Partner listening checklist.",
            "Uncover the Model response, trace how it moves from 'If I pass the entrance exam…' to 'If the "
            "tuition were lower…' to 'If my mentor hadn't encouraged me…', and have learners refine one "
            "sentence from their talk.",
        ],
        'review': [
            "With books closed, have pairs complete the two oral retrieval tasks in Part 8 (naming all five "
            "conditional types with examples and turning a real past mistake into a third + mixed conditional).",
            "Have learners tick the self-check boxes and point anyone who hesitated to Formula Book Card 5.",
        ],
    },
    'checking': [
        "'If it will rain tomorrow, we'll cancel the picnic' — how do we repair the if-clause for an ordinary "
        "future condition? ('If it rains tomorrow…')",
        "'If I would have known your number, I would have called' — where does 'had' belong? ('If I had known…')",
        "Rewrite 'If you don't hurry, you'll be late' using 'unless'. ('Unless you hurry, you'll be late' — "
        "no 'don't' after 'unless'.)",
    ],
    'notes': [
        "A3 'were / would apologise' — 'If I were you' is standard in careful spoken and written English; "
        "note that 'was' is heard in casual speech, as explained in Rule 2.",
        "A4 'had known / would have visited' — third conditional for an unchangeable past situation.",
        "B2 'If he had studied, he wouldn't have failed' — remind learners to drop 'so' when combining two "
        "clauses with 'if'.",
        "B3 'If I had slept last night, I wouldn't be tired now' — mixed conditional linking a past cause "
        "to a present state.",
        "B5 and B6 are open — credit any well-formed second conditional advice or imaginary scenario.",
    ],
    'pair_model': "A: If I had woken up on time this morning, I would have caught the seven o'clock bus. "
                  "B: And if you had caught that bus, you would have arrived at the café before the rain "
                  "started. A: True — and if I hadn't walked through the rain, my notes wouldn't be wet "
                  "right now! B: If I were you, I'd keep a spare umbrella in your bag from now on.",
    'assess': [
        "Listen for the four checklist items during Part 7: a real future condition (first), a hypothetical "
        "present condition (second), a past/mixed reflection (third/mixed), and natural linking.",
        "Accept any coherent personal decision or turning-point topic.",
        "Collect two anonymous examples of 'if + would' or 'unless + don't' for the end-of-class board repair.",
    ],
    'inter': [
        "Keep the four-column board timeline visible so developing speakers can match the time (Future / "
        "Now / Past / Past→Now) before speaking.",
        "Write the third-conditional rhythm on the board as a two-beat chant: 'If I'd KNOWN — I would've "
        "TOLD you.'",
        "If a learner mixes up second and third conditionals, ask simply: 'Are we imagining right now, or "
        "looking back at yesterday?'",
    ],
    'adv': [
        "Challenge confident speakers to include one formal inverted conditional ('Had I known…' or 'Should "
        "the committee approve…') during Part 6 and Part 7.",
        "Encourage stronger pairs to open their Part 5 chain questions with 'Suppose…' or 'Assuming that…' "
        "and use 'provided that' or 'in case' in their responses.",
        "Ask early finishers to explain the difference between 'I'll take an umbrella if it rains' and "
        "'I'll take an umbrella in case it rains' (preparation beforehand).",
    ],
    'errors': [
        "'If it will rain tomorrow, we'll stay home.' → 'If it rains tomorrow, we'll stay home.' — Fix: "
        "ordinary future conditions take the present simple after 'if'.",
        "'If I would have known, I would have helped.' → 'If I had known, I would have helped.' — Fix: keep "
        "'would have' in the result clause only.",
        "'Unless you don't start now, you won't finish.' → 'Unless you start now, you won't finish.' — Fix: "
        "'unless' already means 'if not'.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; run two chain rounds in Part 5 instead of three.",
        "Practice spoken contractions in Part 6 in class and assign the formal inverted conditionals as "
        "written homework.",
        "Run one 60-second Real Talk turn per partner followed by the closed-book recall check.",
    ],
    'review_note': [
        "Exit ticket: each learner produces one third or mixed conditional about their week before leaving.",
        "Flag Formula Book Card 5 in Appendix 1 as a core revision card for Review Test 2 (after Lesson 8).",
        "Remind learners how Lesson 6 (Wishes and Regrets) will build directly on today's 'one step back in "
        "time' rule.",
    ],
    'feedback': "During the chain game and Real Talk, let speakers finish their thought before addressing "
                "any tense slip. Afterwards, write two anonymous 'if + would' sentences on the board and "
                "have pairs repair them aloud.",
}

T6 = {
    'objectives': [
        "Express present wishes ('I wish I had…'), past regrets ('I wish I had taken…'), and frustrations "
        "with changeable behaviour ('I wish you would…') using accurate verb forms.",
        "Express personal and interpersonal preferences naturally using 'would rather', 'prefer', and "
        "'It's (high) time + past simple'.",
        "Deliver a thoughtful one-minute reflection on a past regret, a present wish, and practical "
        "advice for a younger learner.",
    ],
    'success': [
        "learners accurately distinguish 'wish + past simple' (present wish) from 'wish + past perfect' "
        "(past regret)",
        "learners switch cleanly between 'I'd rather stay' (same subject + base verb) and 'I'd rather you "
        "stayed' (different subject + past simple)",
        "in the Real Talk Challenge, speakers combine one past regret, one present wish, and one piece of "
        "advice naturally",
    ],
    'prep': [
        "Write three clear headers on the board: WISH ABOUT NOW (wish + past simple) · REGRET ABOUT THE "
        "PAST (wish + had + participle) · WANT SOMETHING TO CHANGE (wish + would + base verb).",
        "Write the two contrast pairs from Part 1 on the board ('I wish I spoke Arabic' vs 'I wish I had "
        "learned Arabic at school'; 'I'd rather stay home' vs 'I'd rather you stayed home').",
    ],
    'timing': _t(4, 8, 3, 12, 8),
    'procedure': {
        'hook': [
            "Have pairs read the two sentence pairs in Part 1 aloud and explain which speaker is wishing "
            "about today and which is looking back with regret at school days.",
            "Give pairs 90 seconds to complete the three honest personal stems in Part 1 ('One skill I wish "
            "I had right now…', 'One decision from the past few years I wish I had made differently…', and "
            "'One habit I'd rather change this month…').",
            "Connect today's rule to Lesson 5: just like unreal conditionals, wishes and regrets step one "
            "tense back from reality.",
        ],
        'rule': [
            "Teach Rule 1 (Present wishes: 'wish / if only + past simple' and 'wish + could') and Rule 2 "
            "(Past regrets: 'wish / if only + past perfect' and 'wish + would' for annoying habits or "
            "situations we want someone else to change).",
            "Emphasise the golden rule for 'wish + would': we never say 'I wish I would…' about ourselves.",
            "Teach Rule 3 ('would rather' and 'It's high time'): contrast same-subject 'I'd rather walk' with "
            "different-subject 'I'd rather you didn't mention this', and drill 'It's high time we started.'",
            "Teach Rule 4 ('prefer' and 'as if / as though'): compare literal 'It looks as if it's going to "
            "rain' with unreal 'He talks as if he knew everything.'",
        ],
        'diff': [
            "Walk through the two contrast tables in Part 3: first, Present Wish vs Past Regret vs Complaint "
            "('I wish I knew' / 'I wish I had known' / 'I wish he would reply'); second, the three patterns "
            "with 'It's time' ('It's time to leave' / 'It's time for us to leave' / 'It's high time we left').",
            "Have pairs test each other by calling out a time cue ('right now!' or 'last year!') and having "
            "their partner transform 'I wish I…' accordingly.",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, then check in pairs — "
            "pay special attention to A4 ('It's high time we made…') and A6 ('as if he were/was…').",
            "Run Practice B (6 items) in pairs: learners transform B1–B5 aloud and share their true present "
            "wish and past regret for B6.",
            "Review the key whole-class and chorally drill B3 ('I wish I had more free time') and B4 ('It's "
            "time we went home').",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how Speaker A expresses a real "
            "frustration with 'I wish I had…' and 'I wish I could…', and Speaker B responds empathetically "
            "with 'It's high time…' and 'If I were you…'.",
            "Run the four-minute Pair Speaking activity: Partner A shares a real frustration from one of the "
            "four life areas (schedule, study/work space, technology, or travel/health), and Partner B "
            "responds with empathy and practical suggestions — then swap roles.",
            "Invite two pairs to share their most realistic exchange with the class.",
        ],
        'advanced': [
            "Run the first block of Part 6 ('Make the core pattern automatic'): each learner says two true "
            "sentences about right now ('I wish I had/could…') and two about the past ('I wish I had…').",
            "Move to the second block ('Add nuance, detail, and sharper focus'): practise 'If only…!' for "
            "stronger emotional weight, polite workplace 'I'd rather you didn't…', 'What I should have done "
            "was…', and 'as though nothing had happened'.",
            "Ask pairs to compare when 'I wish you would…' sounds like a fair request and when a softer "
            "request ('Would you mind…?') is wiser.",
        ],
        'realtalk': [
            "Give learners 30 seconds to jot down keywords for their one-minute reflection: (1) a past "
            "regret ('I wish I had…'), (2) a present wish ('I wish I had/could…'), and (3) practical advice "
            "for someone younger ('If I were you…' / 'It's high time…').",
            "Partners speak for one full minute each while the listener checks the four Partner listening "
            "checklist criteria.",
            "Uncover the Model response, notice how it links 'I wish I had started speaking out loud from "
            "the very first week', 'Today, I wish I had more opportunities…', and 'It's high time we stopped "
            "treating mistakes as failures', and have learners polish one sentence of their own.",
        ],
        'review': [
            "With books closed, have pairs complete the two oral recall tasks in Part 8 (one present wish + "
            "one past regret, and two 'would rather' sentences with same vs different subjects).",
            "Have learners tick the self-check boxes and review Formula Book Card 6 if needed.",
        ],
    },
    'checking': [
        "'I wish I have more time today' — why is 'have' wrong here, and what is the fix? ('I wish I had "
        "more time' — present wishes step back to the past simple.)",
        "'I'd rather you don't tell anyone' — how do we fix the verb after 'you'? ('I'd rather you didn't "
        "tell anyone' — different subject takes the past simple.)",
        "Can we say 'I wish I would be taller'? (No — 'would' is only for changeable behaviour by someone "
        "else; say 'I wish I were/was taller'.)",
    ],
    'notes': [
        "A2 'had taken' — 'last year' signals a past regret, requiring 'wish + past perfect'.",
        "A4 'made' — 'It's high time + subject + past simple' expresses that the action is already overdue.",
        "A6 accepts 'were' (traditional subjunctive) or 'was' (informal speech) after 'as if he…'.",
        "B3 'I wish I had more free time' — repairs 'have' to 'had' for an unreal present wish.",
        "B5 'reading / watching' — parallel -ing forms after 'prefer X to Y'.",
    ],
    'pair_model': "A: I really wish I had more quiet time in the mornings — my commute is so noisy that I "
                  "arrive at work already tired. B: I know the feeling! Have you tried taking the earlier "
                  "bus, or would you rather not wake up at six? A: I wish I could, but I have to drop my "
                  "younger brother at school first. B: Then it's high time you got a good pair of "
                  "noise-cancelling headphones — if I were you, I'd listen to calm music on the way.",
    'assess': [
        "Listen for the four checklist items during Part 7: accurate past regret ('wish + had + participle'), "
        "accurate present wish ('wish + past simple / could'), natural advice or urgency ('It's high time…'), "
        "and a reflective, conversational tone.",
        "Respond to the speaker's real meaning first before noting any form slips.",
        "Put two anonymous slips (typically 'wish + present' or 'wish + past simple for yesterday') on the "
        "board for a brisk whole-class repair.",
    ],
    'inter': [
        "Keep the three board headers visible so developing speakers can check whether their wish is about "
        "NOW (past simple) or THEN (past perfect) before speaking.",
        "Offer simple sentence starters: 'Looking back, I wish I had…' · 'Right now, I wish I could…' · "
        "'It's high time we…'",
        "If a learner confuses B1 and B3, have them say 'Today I wish I knew' and 'Yesterday I wish I had "
        "known' back-to-back three times.",
    ],
    'adv': [
        "Invite confident speakers to include 'What I should have done was…' or 'as though nothing had "
        "happened' in their Part 5 and Part 7 turns.",
        "Challenge stronger pairs to reframe a blunt workplace complaint ('I wish you would stop sending "
        "late emails') into a diplomatic preference ('I'd rather we agreed on a cut-off time for emails').",
        "Ask early finishers to contrast 'It's time to leave' (neutral schedule) with 'It's high time we "
        "left' (overdue and urgent).",
    ],
    'errors': [
        "'I wish I have more time.' → 'I wish I had more time.' — Fix: unreal present wishes always step "
        "one tense back to the past simple.",
        "'I wish I went to the seminar yesterday.' → 'I wish I had gone to the seminar yesterday.' — Fix: "
        "past regrets require 'had + past participle'.",
        "'It's time we will go home.' → 'It's time we went home.' — Fix: never use 'will' after 'It's "
        "(high) time + subject'.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; run two life areas in Part 5 instead of four.",
        "Practise the now-vs-then wish drill in Part 6 in class and assign the diplomatic workplace rewrites "
        "as homework.",
        "Run one 60-second Real Talk reflection per partner and close with the Part 8 oral check.",
    ],
    'review_note': [
        "Exit ticket: each learner says one past regret ('I wish I had…') and one preference ('I'd rather…') "
        "before leaving.",
        "Remind learners that wishes and 'It's high time' appear directly in Review Test 2 (items A2 and A6).",
        "Point learners to Formula Book Card 6 in Appendix 1 for revision.",
    ],
    'feedback': "Acknowledge the honesty and thoughtfulness of learners' reflections first; then use two "
                "anonymous board examples to reinforce the 'wish + past simple (now)' vs 'wish + had + "
                "participle (then)' contrast.",
}

T7 = {
    'objectives': [
        "Form accurate comparatives, superlatives, and equality structures ('as…as', 'not nearly as…as', "
        "'twice as…as') across adjectives and adverbs.",
        "Use degree modifiers ('far', 'much', 'a great deal', 'slightly', 'by far') and 'the + comparative, "
        "the + comparative' patterns to make comparisons precise and persuasive.",
        "Deliver a persuasive one-minute recommendation comparing two real options with at least three "
        "modified comparisons and clear reasons.",
    ],
    'success': [
        "zero double comparatives ('more better', 'more taller') and zero 'then/than' confusions in practice "
        "and speaking",
        "every comparison in Pair Speaking and Real Talk is supported by a concrete reason ('because…')",
        "speakers use at least two degree modifiers ('far more…', 'slightly cheaper', 'by far the best…') "
        "and one 'the more…, the more…' pattern",
    ],
    'prep': [
        "Write the degree-modifier scale on the board: BIG DIFFERENCE ('far / much / a great deal / a lot') "
        "· SMALL DIFFERENCE ('slightly / a little / a bit') · SUPERLATIVE SPOTLIGHT ('by far / easily / "
        "one of the most…').",
        "Write the two laptop recommendations from Part 1 on the board so learners can see the contrast "
        "between a flat opinion ('good and cheap') and a persuasive comparison ('far lighter… and the battery "
        "lasts nearly twice as long').",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Have pairs read the two laptop recommendations in Part 1 aloud and identify the exact words "
            "that make Speaker B's recommendation convincing.",
            "Give pairs 90 seconds to compare the two hook topics aloud (studying early in the morning vs "
            "late at night; learning in a classroom vs studying online alone) using a 'because' reason for "
            "each choice.",
            "Establish today's core principle: a bare comparison states an opinion, but a modified comparison "
            "plus a reason persuades a listener.",
        ],
        'rule': [
            "Teach Rule 1 (Comparatives and superlatives: short vs long words and irregular forms 'good/better/"
            "best', 'bad/worse/worst', 'far/further/furthest'), reminding learners never to double up with "
            "'more + -er'.",
            "Teach Rule 2 (Equality, multiples, and double comparatives): drill 'just as effective as', "
            "'twice as fast as', and the cause-and-effect rhythm of 'The more you practise, the more confident "
            "you become.'",
            "Teach Rule 3 (Degree modifiers): show how placing 'far', 'much', 'slightly', or 'by far' before "
            "a comparison tells the listener the exact size of the difference.",
        ],
        'diff': [
            "Walk through the two tables in Part 3: first, Comparative (two choices) vs Superlative (standout "
            "in a group); second, how adding degree modifiers and multiples ('far cheaper', 'almost as fast "
            "as', 'three times as many') sharpens vague statements.",
            "Have pairs take one plain sentence ('Bus travel is cheaper than train travel') and say it aloud "
            "in three different strengths ('slightly cheaper', 'far cheaper', 'not nearly as expensive as').",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, checking that A2 includes "
            "'the worst' and A4 uses the adverb comparative 'more beautifully'.",
            "Run Practice B (6 items) in pairs: learners transform B1, repair B2 and B5, and speak their "
            "full reason-backed comparisons for B3, B4, and B6.",
            "Confirm the key whole-class and spotlight why adverbs ending in '-ly' take 'more' ('speaks more "
            "fluently', not 'more fluent').",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how the two partners weigh "
            "online vs classroom courses and reach a joint blended-learning recommendation.",
            "Give pairs four minutes to debate one of the four decision topics in Part 5 and agree on a "
            "joint recommendation using at least three modified comparisons and one 'The more…, the more…' "
            "sentence.",
            "Have two pairs present their joint recommendation in 30 seconds to the class.",
        ],
        'advanced': [
            "Run the first block of Part 6 ('Make the core pattern automatic'): have pairs practise the "
            "irregular forms ('better/best', 'worse/worst', 'further/furthest') and make three true comparisons "
            "about their week with 'far', 'slightly', and 'just as…as'.",
            "Move to the second block ('Add nuance, detail, and sharper focus'): introduce 'by far the most… / "
            "the single most…', concessive comparisons ('While Option A is slightly cheaper, Option B is far "
            "more reliable'), and data-framing openers ('Compared with five years ago, …').",
            "Have each learner build one concessive comparison ('While…, …') about their city or work.",
        ],
        'realtalk': [
            "Give learners 30 seconds to choose one pair of options in Part 7 and jot down three comparison "
            "keywords plus a concrete reason for each.",
            "Partners take turns speaking for one full minute to persuade their listener while the listener "
            "checks the four items in the Partner listening checklist.",
            "Uncover the Model response, notice how it combines 'While studying alone at home is slightly "
            "more convenient…', 'far more effective because…', 'The more you interact…', and 'by far the "
            "most enjoyable way…', and have learners upgrade one of their own comparisons.",
        ],
        'review': [
            "With books closed, have pairs complete the two oral retrieval tasks in Part 8 (one 'far + "
            "comparative' sentence, one 'not nearly as…as' sentence, one 'The more…, the more…' sentence, "
            "and ranking three cities or skills with superlatives).",
            "Have learners tick the self-check boxes and review Formula Book Card 7 if needed.",
        ],
    },
    'checking': [
        "'She is more taller than her sister' — what is the error, and how do we repair it? ('She is taller' "
        "or 'much taller' — never combine 'more' with '-er'.)",
        "'She speaks English more fluent than before' — why do we need 'more fluently'? (Because it describes "
        "how she speaks — an adverb, not a noun.)",
        "Where does 'twice' or 'three times' sit in an 'as…as' comparison? (Right before the first 'as': "
        "'twice as expensive as'.)",
    ],
    'notes': [
        "A2 'the worst' — superlative of 'bad' with 'of my life'.",
        "A4 'more beautifully' — adverb comparative modifying 'sings'.",
        "B1 'This phone is twice as expensive as that one' — multiplier precedes the first 'as'.",
        "B3 and B6 are open — credit any accurate comparison using 'far/much/a lot + comparative + because…' "
        "and any three-city comparison using both comparative and superlative forms.",
        "B5 repairs 'then' (time) to 'than' (comparison).",
    ],
    'pair_model': "A: For our team, an in-person course is far more effective than a self-paced online "
                  "course because people actually practise speaking together. B: That's true, though online "
                  "modules are much more flexible for colleagues who travel. A: What if we combine them? The "
                  "more people review the grammar online at home, the more time we'll have for live speaking "
                  "in class. B: Agreed — a blended course is by far the smartest option for our budget.",
    'assess': [
        "Listen for the four Partner listening checklist targets: modified comparative ('far/much/slightly'), "
        "superlative or equality pattern ('by far the most…' / 'not nearly as…as'), 'The more…, the more…', "
        "and a clear 'because' reason for every comparison.",
        "Remind listeners that a comparison without a reason does not count toward the target.",
        "Jot down any adjective-vs-adverb slips or 'more + -er' slips for the three-minute board repair.",
    ],
    'inter': [
        "Keep the degree-modifier scale visible on the board so developing speakers can add 'far', 'much', "
        "or 'slightly' naturally before every comparative.",
        "Provide three persuasive sentence frames on the board: 'X is far more… than Y because…' · 'Y is "
        "not nearly as… as X' · 'The more we…, the more…'",
        "If a learner hesitates over short vs long adjectives, have them practise five high-frequency pairs "
        "aloud ('cheaper / more expensive', 'faster / more reliable', 'better / more effective').",
    ],
    'adv': [
        "Encourage confident speakers to open their recommendation with a concessive comparison ('While X "
        "is slightly cheaper in the short term, Y is far better value over time').",
        "Challenge stronger pairs to include one data-framing comparison ('Compared with last year, … has "
        "nearly doubled') during Part 5 or Part 7.",
        "Ask early finishers to discuss when 'arguably the best' sounds more credible than 'the best' in "
        "academic or professional speaking.",
    ],
    'errors': [
        "'This route is more faster.' → 'This route is much faster.' — Fix: use 'much' or 'far' (never 'more') "
        "before an '-er' comparative.",
        "'Online courses are cheaper then classroom courses.' → '…cheaper than classroom courses.' — Fix: "
        "'than' compares; 'then' shows time.",
        "'The climate here is warmer than London.' → 'The climate here is warmer than London's / than that "
        "of London.' — Fix: compare like with like (climate with climate).",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; have pairs debate one topic in Part 5 and state their joint verdict.",
        "Practise the degree modifiers in Part 6 orally and assign the concessive 'While…, …' sentence as "
        "written homework.",
        "Run one 60-second persuasion turn per partner in Part 7 and finish with the Part 8 recall check.",
    ],
    'review_note': [
        "Exit ticket: each learner says one persuasive comparison with 'far' or 'by far' and a 'because' "
        "reason before leaving.",
        "Point out that Lesson 8 (Linking Ideas and Building Arguments) will combine today's comparisons "
        "with contrast and result linkers for full debates.",
        "Point learners to Formula Book Card 7 in Appendix 1 for revision.",
    ],
    'feedback': "Tick modified comparisons and reasons separately while listening; praise one speaker who "
                "used 'While…' or 'The more…, the more…' persuasively, then repair two anonymous slips on "
                "the board.",
}

T8 = {
    'objectives': [
        "Connect ideas accurately using the four core linker families: contrast/concession ('although', "
        "'despite', 'however'), cause ('because', 'because of', 'since'), result ('therefore', 'as a "
        "result'), and purpose ('to', 'in order to', 'so that').",
        "Match each linker to its grammatical partner — a full clause ('although / because + subject + verb') "
        "versus a noun phrase or '-ing' form ('despite / because of + noun/-ing').",
        "Deliver a structured 90-second argument using the four-step skeleton: Point → Reason → Example → "
        "Conclusion.",
    ],
    'success': [
        "learners use 'despite / in spite of + noun/-ing' (never 'despite of') and 'although + subject + "
        "verb' accurately",
        "spoken arguments in Pair Speaking and Real Talk follow the four-step skeleton (Point → Reason → "
        "Example → Conclusion)",
        "each speaker acknowledges the other side once ('Although…' / 'Despite…') before defending their "
        "main position",
    ],
    'prep': [
        "Draw the two grammar-pairing columns on the board: TAKES A FULL CLAUSE (Subject + Verb): 'although / "
        "even though / because / since / so that' vs TAKES A NOUN OR -ING: 'despite / in spite of / because "
        "of / due to'.",
        "Write the four-step argument skeleton across the top of the board: 1. POINT → 2. REASON → 3. "
        "EXAMPLE → 4. CONCLUSION ('To sum up, …').",
    ],
    'timing': _t(4, 8, 3, 11, 9),
    'procedure': {
        'hook': [
            "Have pairs read Speaker A and Speaker B in Part 1 aloud and discuss why Speaker B sounds ready "
            "for a university seminar or management meeting even though both speakers share the exact same facts.",
            "Run the 45-second hook challenge: Partner A speaks on 'Why people learn English' while Partner B "
            "counts how many different linking words go beyond 'and', 'but', and 'so'.",
            "Explain that strong speakers don't just have better ideas — they signpost the relationship "
            "between their ideas so the listener can follow effortlessly.",
        ],
        'rule': [
            "Teach Rule 1 (Contrast and concession): write one idea on the board in three packages — "
            "'Although the traffic was heavy, we arrived on time' (clause), 'Despite the heavy traffic, we "
            "arrived on time' (noun), and 'The traffic was heavy. However, we arrived on time' (new sentence).",
            "Emphasise the two classic traps: never say 'despite of', and never put '-ing' directly after "
            "'although' ('Despite being tired…', not 'Although being tired…').",
            "Teach Rule 2 (Cause, result, and purpose): contrast 'because + clause' with 'because of / due to "
            "+ noun', and 'to / in order to + verb' with 'so that + subject + can/could'.",
            "Teach Rule 3 (The four-step argument skeleton) and Rule 4 (Summarizing linkers: 'To sum up', "
            "'All in all', 'Overall', 'In conclusion').",
        ],
        'diff': [
            "Walk through the two contrast tables in Part 3: first, packaging the same contrast three ways "
            "('Although…' / 'Despite…' / 'However, …'); second, Clause Linkers vs Noun-Phrase Linkers side by side.",
            "Run a 45-second oral transformation drill: you say 'Although the course was expensive, it was "
            "worth it', and the class transforms it with 'Despite…' and then with 'However, …'.",
        ],
        'practice': [
            "Give learners 4 minutes to complete Practice A (6 items) individually, then compare in pairs — "
            "ask learners to explain why A2 requires 'Despite' before 'being exhausted'.",
            "Run Practice B (6 items) in pairs: learners combine B1–B2, repair B3 and B5, and speak their "
            "three-sentence argument (B4) and closing summary (B6) aloud.",
            "Confirm the key whole-class, noting that both 'Despite the high cost…' and 'Although the cost "
            "was high…' are valid repairs for B3.",
        ],
        'pair': [
            "Read the 3-turn model exchange in Part 5 aloud so learners hear how the two debaters use "
            "'I firmly believe…', 'Although…', 'Despite…', 'However, …', 'Therefore, …', and 'To sum up, …'.",
            "Have pairs choose one of the three debate motions in Part 5, take opposite sides, and run a "
            "four-minute mini-debate (90 seconds per speaker plus a 1-minute joint conclusion).",
            "Invite two pairs to share their closing summary sentence with the class.",
        ],
        'advanced': [
            "Run the first block of Part 6 ('Make the core pattern automatic'): give pairs 60 seconds to "
            "repackage 'It was raining hard, but the match continued' in four ways ('Although', 'Despite', "
            "'In spite of being…', and 'However').",
            "Move to the second block ('Add nuance, detail, and sharper focus'): practise concessive "
            "counter-balance frames ('It is true that…; nevertheless, …' / 'Admittedly, …; even so, …'), "
            "clause-commenting ', which…', and 'Not only does this…, but it also…'.",
            "Have each learner build one 'Admittedly, …; even so, …' sentence about their debate topic.",
        ],
        'realtalk': [
            "Give learners 30 seconds to choose one claim in Part 7 and jot down four keywords following "
            "the argument skeleton: (1) Main claim, (2) Concession ('Although / Despite'), (3) Reason + "
            "concrete example, (4) Closing summary.",
            "Partners take turns speaking for 90 seconds without reading while the listener checks the "
            "four items in the Partner listening checklist.",
            "Uncover the Model response, trace its four skeleton stages ('I firmly believe…', 'This is "
            "mainly because…', 'For instance…', 'Although some managers worry…', 'To sum up…'), and have "
            "learners tighten one transition in their own talk.",
        ],
        'review': [
            "With books closed, have pairs complete the two oral recall tasks in Part 8 (a 20-second "
            "mini-argument on the four-step skeleton and expressing one contrast in three grammatical ways).",
            "Have learners tick the self-check boxes and remind them that Review Test 2 (Lessons 1–8) "
            "follows this lesson.",
        ],
    },
    'checking': [
        "'Despite of the rain, we walked' — what word must be removed immediately? ('of' — say 'Despite "
        "the rain' or 'In spite of the rain'.)",
        "'Although the high price, we bought it' — give two different grammatical ways to fix this sentence. "
        "('Despite the high price, we bought it' or 'Although the price was high, we bought it'.)",
        "What are the four steps of the argument skeleton in order? (Point → Reason → Example → Conclusion.)",
    ],
    'notes': [
        "A2 'Despite' — followed by the -ing phrase 'being exhausted after a twelve-hour shift'.",
        "A3 'because of' — followed by the noun phrase 'heavy snow on the mountain pass'.",
        "B3 accepts either 'Despite the high cost, we bought the equipment' (noun phrase) or 'Although the "
        "cost was high, we bought the equipment' (full clause).",
        "B4 must visibly include all three parts (Point + Reason + Example) on learning a second language.",
        "B6 is open — credit any coherent summary of the lesson that opens with 'To sum up,' 'All in all,' "
        "or 'In conclusion,'.",
    ],
    'pair_model': "A: I firmly believe that traditional written homework should be replaced by daily "
                  "recorded speaking practice. B: Although speaking practice is essential, written homework "
                  "helps learners notice spelling and sentence structure. A: Despite that advantage, most "
                  "students already spend hours reading and writing in class; as a result, their spoken "
                  "fluency lags behind. B: However, some learners feel shy recording themselves at home. "
                  "A: Therefore, teachers can start with short one-minute voice notes. To sum up, combining "
                  "short daily recordings with a brief weekly written check gives learners the best balance.",
    'assess': [
        "Evaluate the 90-second talks using the four Partner listening checklist criteria: four-step "
        "argument skeleton, accurate contrast linker ('although' + clause or 'despite' + noun/-ing), "
        "cause/result linker, and a clear closing summary.",
        "Judge the talk by structural clarity and linker accuracy rather than personal agreement with the claim.",
        "Collect two anonymous clause-vs-noun linker slips for the end-of-lesson board repair.",
    ],
    'inter': [
        "Keep both the Clause vs Noun chart and the four-step Argument Skeleton visible on the board "
        "throughout Parts 5 and 7.",
        "Provide four ready-to-use signpost openers on the board: 'I believe that…' · 'This is mainly "
        "because…' · 'For instance, …' · 'To sum up, …'",
        "If a learner says 'Despite of…' or 'Although + noun', pause after their turn and ask them to "
        "point to the Clause vs Noun column on the board to self-correct.",
    ],
    'adv': [
        "Encourage confident speakers to use 'Admittedly, …; even so, …' or 'It is true that…; nevertheless, …' "
        "when handling the counterargument in Part 7.",
        "Challenge stronger pairs to include one 'Not only does this…, but it also…' inversion or one "
        "clause-commenting ', which…' sentence during their mini-debate.",
        "Ask early finishers to compare the register and punctuation of 'however', 'nevertheless', and 'yet'.",
    ],
    'errors': [
        "'Despite of the delay, we arrived on time.' → 'Despite the delay… / In spite of the delay…' — Fix: "
        "'despite' never takes 'of'.",
        "'Although being tired, she finished the report.' → 'Despite being tired… / Although she was tired…' "
        "— Fix: 'although' requires a subject and verb.",
        "Listing disconnected opinions ('First… Also… Another thing…') — Fix: require the four-step skeleton "
        "(Point → Reason → Example → Conclusion) for every opinion turn.",
    ],
    'short': [
        "Keep Parts 1–4 at 15 + 10 minutes; run a 2-minute mini-debate in Part 5.",
        "Do the four-way contrast repackaging in Part 6 in class and assign the 'Not only…' / 'Admittedly…' "
        "sentences as homework.",
        "Run a 60-second Real Talk argument per partner and close with the Part 8 oral recall check.",
    ],
    'review_note': [
        "Exit ticket: each learner states one contrast idea in two ways — once with 'although' and once "
        "with 'despite'.",
        "Remind learners that Review Test 2 (covering Lessons 1–8) follows this lesson; point them to "
        "Formula Book Cards 1–8 in Appendix 1.",
        "Note that the four-step argument skeleton taught today will be used again in Lessons 15 and 16 "
        "and in the Final Assessment speaking task.",
    ],
    'feedback': "Praise speakers who clearly signposted their four argument stages ('This is mainly because…', "
                "'For instance…', 'To sum up…'). Then put two anonymous 'although / despite' slips on the "
                "board and let pairs repair them in 60 seconds.",
}

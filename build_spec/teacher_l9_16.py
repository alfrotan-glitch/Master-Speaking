# -*- coding: utf-8 -*-
"""Teacher's Book guides for Lessons 9-16 (Parts Five to Eight)."""


def _t(hook, rule, diff, pair, adv):
    assert hook + rule + diff == 15 and pair + adv == 20
    return [("The Speaking Hook", hook), ("The Simple Rule", rule),
            ("See the Difference", diff), ("Practice the Pattern", 10),
            ("Pair Speaking", pair), ("The Advanced Upgrade", adv),
            ("Real Talk Challenge", 10), ("Review and Self-Check", 5)]


T9 = {
    'objectives': [
        "Build accurate passive forms across tenses and choose active or passive for the right focus.",
        "Use one reporting structure (It is said / believed that …) in a short news brief.",
        "Explain to a listener when the agent is kept and when it is omitted.",
    ],
    'success': [
        "at least 5 of 6 Practice A passive forms correct without prompting",
        "the newsroom exchange includes two passives and one reporting structure",
        "listeners confirm the tone sounds objective, not personal",
    ],
    'prep': [
        "Board: PASSIVE = be + past participle — tense lives in 'be' (is/are/was/were/will be/has been).",
        "News prompts ready: accident, opening, rule change, sports result.",
        "Formula Book card 9 for display.",
    ],
    'timing': _t(4, 7, 4, 12, 8),
    'procedure': {
        'hook': [
            "Display the two bicycle sentences side-by-side. Elicit: whose story is each one?",
            "Pairs produce one active and one passive version of a real event from their week.",
            "Take two pairs' answers and mark which focuses on the result.",
        ],
        'rule': [
            "Rule 1: passive formation across tenses — chorally read the four lines, then transform "
            "one sentence through every tense.",
            "Rule 2: when to use it — ask 'Who cares about the doer here?' for each Examples line.",
            "Rule 3: reporting verbs — drill the It-is-said pair aloud.",
        ],
        'diff': [
            "Active vs passive table: cover the right column, pairs guess the rule, then reveal.",
            "Get-passive contrast — mark the emotion tag and give one informal get example.",
            "False passives: read two on the board; ask why they are not real passives.",
        ],
        'practice': [
            "Practice A (6) solo + pair check; insist on full forms including auxiliaries.",
            "Practice B (6): B1–B3 spoken transformations in pairs; B4–B6 corrections aloud.",
            "Key after checking; drill any tense error by walking the verb through the four tenses.",
        ],
        'pair': [
            "Newsroom: assign reporter/editor; three events each, passives in report style.",
            "Editor question 'Who did it?' forces the agent decision.",
            "Swap roles in the second round.",
        ],
        'advanced': [
            "Intermediate base: passive in four tenses from objects in the room + reporting pair.",
            "Advanced upgrade: get-promoted example, alleged/assumed, and participle tail in "
            "speech — one of each.",
            "Discussion: where does the passive improve credibility (reports, data)?",
        ],
        'realtalk': [
            "Planning as printed: three events — two about the result, one for comment — tenses fixed.",
            "90 seconds to a partner; covered model until after one attempt.",
            "Uncover the model; compare passive count and final active comment, then re-deliver "
            "one improved sentence.",
        ],
        'review': [
            "Covered: three objects from the room into passives (different tenses).",
            "Formal reporting sentence about a known person — volunteer round.",
            "Self-check; unticked boxes redo Practice A and B4 aloud.",
        ],
    },
    'checking': [
        "Board transform: 'They clean the office every day.' → learners say the passive.",
        "'My phone was broken by me' — natural? (no — use the active)",
        "Reporting pair quick-fire: 'People say that he is the best.' → two passive versions.",
    ],
    'notes': [
        "A5 'has just been introduced' — adverb position before the participle; 'has just introduced' "
        "would be active and wrong.",
        "B3 accepts either 'It is said that he is the best' or 'He is said to be…'.",
        "B5 'I lost my phone' — insist on the natural active; 'I had my phone stolen' is also credited "
        "where noted.",
        "B2 'The board made the decision' — learners must restore the agent as subject; 'It was decided' "
        "would need a different structure.",
        "B6 is open only within the passive requirement — insist on one future passive with when/tomorrow.",
    ],
    'pair_model': "A: A new library was opened near the hospital. B: Who opened it? A: The mayor opened it, "
                  "but it is said that funding came from abroad. B: How about a rule change? A: Smoking has been "
                  "banned on campus — students were informed this morning. B: Was anyone upset? A: A few were, "
                  "but the meeting was held calmly.",
    'assess': [
        "Passives counted live against the four criteria; objective tone means no first-person story.",
        "Accept any news content that holds the structure; the model is one of many.",
        "If reporting structure is missing, prompt once with 'People say…' → 'It is said…'.",
    ],
    'inter': [
        "Tense table stays visible during pair work; learners point before speaking.",
        "Frames: 'was/were done' · 'is/are done' · 'will be done' · 'It is said that…'",
        "Remediation: re-do B4 (builted → built) as a choral correction before Real Talk.",
    ],
    'adv': [
        "Get-passive in speech: 'He got promoted' vs 'He was promoted' — feeling marked?",
        "Reporting nuance: alleged vs claimed — which accuses more strongly?",
        "Formal tail: 'Founded in 1971, the school…' — one own example.",
    ],
    'errors': [
        "'The house was builted' → 'was built' — fix: irregular participle sort.",
        "'My phone was stolen by me' → 'I lost my phone' — fix: active for your own actions.",
        "Keeping the agent when the event matters more — fix: agent-last rule; give the agent only "
        "if asked.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; newsroom runs two items instead of three.",
        "Upgrade moves to homework; reporting pair kept in class.",
        "Real Talk: two events only, still with one reporting structure and final active comment.",
    ],
    'review_note': [
        "Exit ticket: one passive from each of two tenses about today.",
        "Passive feeds Lessons 10, 13–14 and the Final Assessment (A5/B5).",
        "Formula card 9.",
    ],
    'feedback': "Tick passives and reporting structures without interrupting the report-style delivery; "
                "repair the tense of be only after the brief, with two anonymous examples.",
}

T10 = {
    'objectives': [
        "Use have/get something done to arrange services and to describe misfortunes.",
        "Distinguish make, let, have and get + person + verb in speech.",
        "Negotiate a service conversation that includes causative language and a price/time agreement.",
    ],
    'success': [
        "causative service vs accident distinction correct in at least 4 of 5 attempts",
        "make/let/have/get verb patterns used correctly (to only after get)",
        "negotiation ends with a stated time and price",
    ],
    'prep': [
        "Board: HAVE/GET + object + participle = service OR accident.",
        "Service vocabulary ready: haircuts, repairs, tailoring, deliveries, cleaning.",
        "Formula Book card 10.",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Hook conversation: what do people 'have done' in your city? — collect five examples "
            "on the board.",
            "Ask who does it (self vs hired) for each — mark S or H.",
            "Tell learners the lesson names this structure.",
        ],
        'rule': [
            "Rule 1: have/get sth done — chorally read, then contrast service vs story-misfortune "
            "examples.",
            "Rule 2: make/let/have/get + person + verb — sort four sentences by force (force / "
            "allow / instruct / persuade).",
            "Rule 3: service phrases — drill 'I get my…done…every month' as a chunk.",
        ],
        'diff': [
            "Service vs accident table: pairs label each row before seeing the Why column.",
            "Causative-verbs table: read aloud, then learners supply their own 'made me…' sentence.",
            "Make-passive point: 'I was made to wait' — mark the kept to.",
        ],
        'practice': [
            "Practice A (6) solo + pair; A3/A6 (made/lost vs persuade) need the pattern named.",
            "Practice B (6): spoken rewrites; B5 and B6 are open — two samples.",
            "Key display; on any to-after-make error, stop and rebuild Rule 2.",
        ],
        'pair': [
            "Service shop: A = shop, B = customer with three problems; causatives + price/time.",
            "Monitor for make/let/get inclusion with a tick; prompt once if missing.",
            "Swap roles or run a second customer if time allows.",
        ],
        'advanced': [
            "Intermediate base: four causatives from own life + service chunks.",
            "Advanced upgrade: have-person-do delegation, 'had us laughing', 'got round to…' — one "
            "each true.",
            "Discussion: when is have-person-do businesslike but impolite?",
        ],
        'realtalk': [
            "Planning: three moments — arranged service, accident, make/let/get.",
            "One minute to a partner; model covered.",
            "Model uncovered; underline the causatives, compare counts, then improve one line.",
        ],
        'review': [
            "Covered: three things to have done this month — each a full causative sentence.",
            "Made vs let: one person per learner.",
            "Self-check; unticked redo A1/A6 and B2 aloud.",
        ],
    },
    'checking': [
        "'I had my phone stolen on the bus.' — is the stealing a service? (no — misfortune) "
        "but same grammar.",
        "Pattern check: make + to? (no) get + to? (yes)",
        "Board 'get my car to repair' — whole-class repair.",
    ],
    'notes': [
        "A3 'lose' — made + base verb, no to; 'made to lose' here would be passive and wrong.",
        "A6 'to eat' — get needs to; 'eat' alone would be make/have/let.",
        "B1 'I had my car serviced.' — accept 'got' variant.",
        "B2 'I got my friend to drive us.' — the persuasion marker to is the whole point.",
        "B3 correction: 'get my car repaired' (participle, not infinitive). B4: 'made me wait'.",
    ],
    'pair_model': "A: I need to have my suit shortened — can you do it this week? B: We can have "
                  "it ready by Thursday; it will cost 400 afghanis. A: My mother made me wear it "
                  "to the wedding — I had my shoes repaired too. B: Did your boss let you leave "
                  "early? A: He got me to finish the report first, then he let me go.",
    'assess': [
        "Listen for the four printed criteria; time/price agreement is required.",
        "Misfortune 'had sth done' counts as causative only if learners name it as accident, not "
        "service.",
        "Accept any price vocabulary that closes the negotiation.",
    ],
    'inter': [
        "Desk card: HAVE/GET + object + done; make/let/have + base / get + to.",
        "Chunk drill: 'I had my car fixed' · 'I got my friend to help me'.",
        "Remediation: re-drill A5/A6 before Real Talk if pair work confused to.",
    ],
    'adv': [
        "Delegation: 'I'll have the team look into it.' vs 'I'll ask the team to…' — difference?",
        "Story colour: 'He had us all laughing' — when does it fit?",
        "End-up pattern: 'I ended up waiting…' as complement to causatives.",
    ],
    'errors': [
        "'Will get my car to repair' → 'repaired' — fix: have/get + done chorus.",
        "'Made me to wait' → 'wait' — fix: make-pattern sort.",
        "Using have-done for self-done actions — fix: 'I fixed my laptop' vs 'I had it fixed' "
        "contrast on the board.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; negotiation runs two items with price/time.",
        "Second role in the pair becomes homework dialogue.",
        "Upgrade moves to the self-check spoken task.",
    ],
    'review_note': [
        "Exit ticket: one service and one misfortune sentence.",
        "Causatives return in the Final Assessment (A8/B7); link them there.",
        "Formula card 10.",
    ],
    'feedback': "During the shop role-play, tick causative accuracy and negotiation outcome only; "
                "repair a sample of to errors afterwards on the board, one pair at a time.",
}

T11 = {
    'objectives': [
        "Choose gerund or infinitive correctly after the core lesson verbs.",
        "Use one meaning-changing verb (remember/forget/stop/try) with both patterns.",
        "Handle preposition + -ing including look forward to / be used to.",
    ],
    'success': [
        "at most two -ing/to errors across the pair interview",
        "one meaning-changing verb used correctly and explained",
        "no 'to + -ing' errors where to is a preposition",
    ],
    'prep': [
        "Board: -ING verbs (enjoy, mind, avoid…) vs TO verbs (hope, decide, plan…).",
        "Meaning-changers ready: stop (quit vs pause) · remember (before vs after) · try.",
        "Formula Book card 11.",
    ],
    'timing': _t(4, 7, 4, 12, 8),
    'procedure': {
        'hook': [
            "Learners finish the four hook stems; pairs compare.",
            "Ask 'Which felt natural with -ing? With to?' — collect five on each side.",
            "State the aim: -ing after some verbs is not a decoration.",
        ],
        'rule': [
            "Rule 1: -ing verbs as a group; Rule 2: to verbs as a group — two quick sorts.",
            "Rule 3: meaning-changing demo: read both I-remember sentences and ask which action "
            "came first.",
            "Rule 4: preposition + -ing — insist 'look forward to + -ing' chorally three times.",
        ],
        'diff': [
            "Meaning-changing table: cover the right column; pairs predict, then reveal.",
            "Need + -ing vs need + to — write both; ask which is more natural in the region.",
            "Preposition traps: rapid-fire four prompts ('interested in…').",
        ],
        'practice': [
            "Practice A (6) solo + pair; A4 is the preposition trap — emphasise it.",
            "Practice B (6): B1–B3 corrections aloud; B5 meaning choice named.",
            "Key display; if B2 recurs, re-drill look-forward-to with the whole class.",
        ],
        'pair': [
            "Interview: pairs adapt the four printed question frames; use four patterns each.",
            "One follow-up after most answers required — monitor for interview depth.",
            "Swap roles; take two strong exchanges to replay for the class.",
        ],
        'advanced': [
            "Intermediate base: five chunks per pattern + meaning-pair drill.",
            "Advanced upgrade: gerund as subject, 'no point in + -ing / worth + -ing', 'have "
            "difficulty + -ing'.",
            "Discussion: when does 'There is no point…' shut down a debate politely?",
        ],
        'realtalk': [
            "Planning: three -ing activities + two to-plans + one meaning-changer marked.",
            "One minute to a partner; model covered.",
            "Model uncovered; count the patterns in it, compare with own talk, upgrade one line.",
        ],
        'review': [
            "Covered: two sentences per meaning-changer (stop + try).",
            "Five verbs per list from memory — pairs compete.",
            "Self-check; unticked redo A1/A6 and B2 aloud.",
        ],
    },
    'checking': [
        "Five-verb thumbs: enjoy? (ing) decide? (to) mind? (ing) hope? (to) suggest? (ing)",
        "'I stopped to eat' vs 'I stopped eating' — action test: which lunch ended?",
        "'look forward to' — following verb is…? (meeting)",
    ],
    'notes': [
        "A4 'hearing' — 'to' is a preposition here; 'to hear' in this frame is the target error.",
        "A5 'smoking' — 'stopped smoking' = quit; 'stopped to smoke' would be pause-and-smoke.",
        "A6 'to open' — attempt, not experiment; 'try opening' would be method.",
        "B3 'suggested going' — 'suggested me to go' is the error this item exists to remove.",
        "B5 expects the -ing reading for 'I remember calling her'; credit the alternative only if "
        "the learner explains the meaning correctly.",
    ],
    'pair_model': "A: What do you enjoy doing at weekends? B: I enjoy hiking. A: Have you decided "
                  "to change anything this year? B: I have decided to learn English properly. A: What "
                  "do you avoid doing? B: I try to avoid complaining — I stopped doing it last year. "
                  "A: Nice. What are you looking forward to? B: Looking forward to finishing this course!",
    'assess': [
        "Pattern accuracy decides success — meaning-changer and preposition items are must-pass.",
        "Follow-ups must be present; interview that lists answers without questioning is incomplete.",
        "The Real Talk requirement is quantitative: 3× -ing + 2× to + decision sentence.",
    ],
    'inter': [
        "Chunk cards: 'enjoy + ing' · 'decided to + base' · 'look forward to + ing'.",
        "Starter bank: 'I enjoy…' · 'I decided to…' · 'I avoid…'",
        "Remediation: if to-preposition slips, re-do A4 and B2 chorally before Real Talk.",
    ],
    'adv': [
        "Subject gerund debate: 'Finding time is harder than finding motivation' — true?",
        "Worth / no-point frames: three opinions about study habits.",
        "Difficulty frame: 'I had difficulty + -ing' about accent or reading speed.",
    ],
    'errors': [
        "'Enjoy to read' → 'reading' — fix: -ing-verb list drill.",
        "'Look forward to meet' → 'meeting' — fix: preposition-to check; board both uses of to.",
        "Using only to-patterns — fix: require one -ing sentence per answer in the interview.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; interview uses three questions instead of four.",
        "Upgrade patterns become homework examples.",
        "Real Talk: 45 seconds with the same counting requirement.",
    ],
    'review_note': [
        "Exit ticket: preposition + -ing about this lesson.",
        "Test 3 revisits this lesson — flag Appendix 1 card 11.",
        "Gerund/infinitive feeds Lesson 13's verb patterns (suggest/warn) — connect there.",
    ],
    'feedback': "Note the meaning-changing verbs live — one 'stop' correction from a learner's "
                "own story teaches more than ten worksheet items; repair the rest after.",
}

T12 = {
    'objectives': [
        "Build accurate defining and non-defining relative clauses in speech.",
        "Reduce a clause correctly by dropping which-is/who-was where possible.",
        "Choose who/which/that/whose/where and punctuate meaning accordingly.",
    ],
    'success': [
        "relative pronoun choice correct in at least 5 of 6 spoken descriptions",
        "one non-defining clause used with correct meaning and pause",
        "one reduced clause produced naturally in the talk",
    ],
    'prep': [
        "Board: who/people · which/things · that/both · whose/possession · where/place.",
        "Optional: classroom objects to describe without naming.",
        "Formula Book card 12.",
    ],
    'timing': _t(5, 7, 3, 12, 8),
    'procedure': {
        'hook': [
            "Guessing hook: learners describe (who/which/that in every sentence) without naming.",
            "Two strong descriptions played back; class names the pronoun each used.",
            "Goal stated: two ideas in one clean sentence.",
        ],
        'rule': [
            "Rule 1: defining — essential, no commas; object pronoun can drop — drill with one "
            "sentence each on the board.",
            "Rule 2: non-defining — extra detail, commas, never that — contrast the same name "
            "with/without commas.",
            "Rule 3: preposition position — formal vs normal vs speech, all three versions of "
            "one sentence.",
            "Rule 4: reduced — drop only who is/which was; wrong drops shown first as anti-examples.",
        ],
        'diff': [
            "Defining vs non-defining table: pairs state 'how many?' for each row.",
            "that/which/who sorting: speech vs commas rule — three quick examples.",
            "Whose vs of-whom: why is 'whose' natural and 'of whom' clumsy?",
        ],
        'practice': [
            "Practice A (6) solo + pair; A2 comma and A5 gap require justification.",
            "Practice B (6): B1–B5 transformations spoken; B6 performed as a 20-second talk.",
            "Key display; if A5 is missed, re-teach the reduced rule with the printed example.",
        ],
        'pair': [
            "Guessing game: two items each, defining + non-defining, make the partner guess.",
            "Second pass: improve the sentences to be more concise — one edit each.",
            "Class hears the best concise version.",
        ],
        'advanced': [
            "Intermediate base: four pronouns drilled + object pronoun dropped.",
            "Advanced upgrade: which-comment, cleft 'what', reduced in formal register — one "
            "each.",
            "Discussion: 'which surprised everyone' vs 'that surprised everyone' — which is a "
            "comment on the whole sentence?",
        ],
        'realtalk': [
            "Planning: person → defining role → non-defining extra → reduced description.",
            "One minute to a partner without notes; model covered.",
            "Model uncovered; count its four clauses, compare, improve one learner sentence.",
        ],
        'review': [
            "Covered: one defining + one non-defining about the room.",
            "City description: two + reduced — volunteer then pairs.",
            "Self-check; unticked redo A1/A4 and B3 aloud.",
        ],
    },
    'checking': [
        "'My mother, that lives…' — correct? (no: who after commas)",
        "'The book what I read' — which pronoun? (that/which, no what)",
        "Reduced test: can 'who called' become 'man called'? (no — full verb, not droppable)",
    ],
    'notes': [
        "A2 'which' — commas demand which/who, not that.",
        "A5 expects the reduced form or explicit 'which were'; both credited; the gap is the "
        "lesson's test.",
        "A6: the omitted pronoun is subject vs object — B6 in student book clarifies it; both "
        "'that' and 'which' credited for the object case.",
        "B3 accepts only 'who' after commas; 'that' after commas is never correct.",
        "B6 is open but must demonstrably contain both clause types — do not score a single-clause "
        "name.",
    ],
    'pair_model': "A: The woman who is standing by the window is my colleague — the one who taught "
                  "me last year. B: The colleague with whom you worked? A: Yes, the colleague I worked "
                  "with on the project. She, who lives in Bamyan, visits us twice a year. — B: The "
                  "students interested in the course should apply early; the man whose son won the "
                  "prize applied yesterday.",
    'assess': [
        "Criteria in the pair and talk boxes decide — pronoun choice + defining/non-defining "
        "meaning + concision.",
        "Guessing success is the speaking test: if the partner guesses, the description did its "
        "job.",
        "Count the reduced clause in Real Talk explicitly — accept only a droppings of who-is/",
        "which-was, not a raw participle.",
    ],
    'inter': [
        "Pronoun board visible; learners point before speaking.",
        "Starters: 'The person who…' · 'The place where…'",
        "Remediation: if A2/B3 keep failing, drill commas-as-pauses aloud with hand gestures.",
    ],
    'adv': [
        "Comment-which: 'She apologised, which changed the whole mood.' — learners build one.",
        "Cleft focus: 'What I need is time.' — build one about their own study.",
        "Reduced formality: when does 'Anyone arriving late…' sound sharper than 'If you "
        "arrive late…'?",
    ],
    'errors': [
        "'The book what I read' → 'the book I read' — fix: pronoun chart on desk.",
        "'My mother, that…' → 'who' — fix: after a comma, never that.",
        "Dropping a full verb instead of who is — fix: only who is/which was droppable, "
        "shown by two anti-examples.",
    ],
    'short': [
        "Parts 1–4 at 15 + 10; guessing game one item each.",
        "Advanced upgrades become three written sentences for homework.",
        "Real Talk: two clause types required instead of three + reduced.",
    ],
    'review_note': [
        "Exit ticket: 'The person who…which…' about a classmate.",
        "Relative clauses return in the Final Assessment (C5/C8) — flag those items.",
        "Formula card 12.",
    ],
    'feedback': "Tick clause-type accuracy rather than elegance during descriptions; repair the "
                "worst pronoun error on the board afterwards with two correct reformulations.",
}

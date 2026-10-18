# -*- coding: utf-8 -*-
"""Lessons 13-16 — Part Seven: Sound More Natural and Advanced; Part Eight: Speak with Confidence."""
from lesson_template import render_lesson

L13 = {
    'n': 13, 'part_no': 7, 'part_title': 'Sound More Natural and Advanced',
    'title': 'Reported Speech and Reporting Verbs',
    'goal': 'report conversations and summarise information accurately and naturally',
    'intro': "Half of real speaking is reporting what other people said. This lesson makes that effortless.",
    'hook': [
        "Tell your partner: what did a friend or family member say to you this week? "
        "Report the words — don't read them. What exactly did they say?",
    ],
    'rules': [
        {'label': 'Rule 1 — The backshift: one step back in time',
         'formula': ["Direct: 'I am tired.'  →  She said (that) she was tired.",
                     "Present simple → past simple · Present continuous → past continuous",
                     "Past simple → past perfect · will → would · can → could · may → might",
                     "would / could / should / past perfect → stay the same"],
         'text': ["When you report, the verbs usually step back one tense. 'That' is optional and often "
                  "dropped in speech."],
         'examples': ["\"I work here.\" → He said he worked there.",
                      "\"I've finished.\" → She said she had finished.",
                      "\"I'll call you.\" → He said he would call me."],
         'remember': ["If the statement is still true, you may keep the original tense: "
                      "'She said the earth goes round the sun.'"]},
        {'label': 'Rule 2 — Reporting questions and commands',
         'formula': ["Yes/No question:  ask + if / whether + subject + verb  (statement order!)",
                     "Wh- question:  ask + question word + subject + verb",
                     "Command:  tell / ask / order + person + to + base verb",
                     "Negative command:  told me not to + base verb"],
         'text': ["Reported questions use statement word order — no auxiliary 'do', no question mark."],
         'examples': ["\"Where do you live?\" → She asked me where I lived.",
                      "\"Are you ready?\" → He asked if I was ready.",
                      "\"Sit down.\" → She told me to sit down.",
                      "\"Don't worry.\" → He told me not to worry."],
         'remember': ["'say' has no object: 'He said that…' · 'tell' needs a person: 'He told me that…' "
                      "(never 'He said me…')."]},
        {'label': 'Rule 3 — Reporting verbs: beyond say and tell',
         'formula': ["admit · agree · apologise · argue · claim · complain · explain · insist · "
                     "mention · promise · refuse · remind · suggest · warn",
                     "Patterns:  verb + that …  ·  verb + to + verb  ·  verb + person + to + verb  ·  verb + -ing"],
         'text': ["Reporting verbs make summaries compact and precise — exactly what the TOEFL and "
                  "professional English require."],
         'examples': ["He admitted making a mistake.  (verb + -ing)",
                      "She promised to call back.  (verb + to)",
                      "The doctor warned me not to travel.  (verb + person + to)",
                      "He suggested leaving early.  (verb + -ing)"],
         'remember': ["'suggest' takes -ing or 'that': 'She suggested going' / 'She suggested that we go' "
                      "(not 'suggested me to go')."]},
        {'label': 'Rule 4 — Time and place references',
         'formula': ["now → then · today → that day · yesterday → the day before",
                     "tomorrow → the next day / the following day · last week → the week before",
                     "here → there · this → that · ago → before"],
         'text': ["When you report later, shift the time words too — or the story makes no sense."],
         'examples': ["\"I'll do it tomorrow.\" → She said she would do it the next day.",
                      "\"I saw him yesterday.\" → He said he had seen him the day before."],
         'remember': ["If you report on the same day, you can keep the time words: "
                      "'He said he'd do it tomorrow' (said earlier today)."]},
    ],
    'differences': [
        {'title': 'say vs tell (and ask)',
         'rows': [
             ["He said that he was busy.", "He told me that he was busy.", "He asked me if I was busy.", "say + that (no person) · tell + person · ask + person + question"],
         ], 'headers': ['say + that', 'tell + person', 'ask + person', 'The pattern']},
        {'title': 'reporting with the same tense or backshift',
         'rows': [
             ["She said she was tired. (reported later)", "She said she is tired. (still true now)", "Both can be correct: backshift for reporting later; no shift when the fact is still true — or when you report immediately."],
         ], 'headers': ['Reported later (backshift)', 'Still true now (no shift)', 'The rule']},
        {'title': 'command vs request vs advice',
         'rows': [
             ["told me to wait", "asked me to wait", "advised me to wait", "insisted on my waiting", "The verb carries the force: order → request → advice → insistence."],
         ], 'headers': ['order: told me to wait', 'request: asked me to wait', 'advice: advised me to wait', 'insistence: insisted on my waiting', 'The force']},
    ],
    'practice_a': [
        "\"I am working now.\"  →  He said he __________ (work) then.",
        "\"We have finished.\"  →  They said they __________ (finish).",
        "\"Where did you park?\"  →  She asked me where I __________ (park).",
        "\"Don't touch it!\"  →  He warned me __________ touch it.",
        "\"I'll help you.\"  →  She promised __________ (help) me.",
        "\"Let's take a break.\"  →  He suggested __________ (take) a break.",
    ],
    'practice_b': [
        "Report: 'I never lie.'  (He said…)",
        "Report a question: 'When will the results be announced?'  (They asked…)",
        "Correct: 'He said me that he was tired.'",
        "Correct: 'She suggested me to go early.'",
        "Report with a strong verb: 'No, I didn't break the window.'  (He denied…)",
        "Report advice your teacher has given you (2 sentences, 2 different reporting verbs).",
    ],
    'pair': {
        'intro': "The message game. Partner A reads (or says) three short messages from 'other people' "
                 "(notes, emails, quotes). Partner B reports them to a third person (the teacher/another pair) "
                 "using different reporting verbs. Swap.",
        'task': ["Messages to report: a complaint · a promise · a warning · an invitation · a refusal.",
                 "Use at least four different reporting verbs and both question and command reports."],
        'output': "Five faithfully reported messages per reporter, using at least four different "
                  "reporting verbs, with one reported question and one reported command, that the "
                  "listener can repeat accurately.",
        'criteria': ["backshift is accurate",
                     "question word order correct in reports",
                     "at least four reporting verbs used",
                     "time references shifted correctly"],
    },
    'advanced': {
        'base': ["Drill the backshift table out loud with true sentences about your day.",
                 "Learn the verb patterns in chunks: 'admitted -ing' · 'promised to' · 'warned me not to' · 'suggested -ing'."],
        'upgrade': ["Use continuous reporting verbs for liveliness: 'She kept insisting that she was right.' · 'He went on to explain…'",
                    "Use 'point out / observe / note' in academic reporting: 'The report points out that demand has fallen.'",
                    "Report with judgement-free precision: 'He claimed to have seen nothing, yet witnesses disagreed.'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): choose a real conversation and list four things that were "
                "said — keywords only, with who said each one. Pick your four reporting verbs before "
                "you speak: admitted, warned, promised, suggested, agreed, asked…",
        'task': "Retell challenge (ninety seconds): report a real conversation you had this week — a "
                "discussion, an argument, an interview or a negotiation. Report at least four things people "
                "said, using varied reporting verbs. End with your own comment.",
        'model': "On Saturday my sister called to tell me that she had accepted the job offer. She "
                 "admitted that she was nervous, but she promised to ask for a training week. My "
                 "father warned her not to sign without reading the contract, and she agreed to send "
                 "it to him first. She also asked me whether I thought she should negotiate the "
                 "salary; I suggested doing the same research she had done for the interview. In my "
                 "opinion, she should ask — the worst they can say is no.",
        'feedback': ["accurate backshift and time references",
                     "varied reporting verbs (not only 'said')",
                     "questions and commands reported correctly",
                     "clear final comment"],
    },
    'review': {
        'points': ["Backshift: one tense back; time words shift too.",
                   "say (+ that) vs tell (+ person); reported questions use statement order.",
                   "Reporting verbs (admit, promise, warn, suggest…) carry meaning and grammar patterns."],
        'retrieval': ["Report three things someone said to you today.",
                      "Report one question, one command and one promise — all out loud."],
        'watch': ["'He said me…' → 'He told me…'.",
                  "'She suggested me to go' → 'She suggested going' / 'She suggested that I go'."],
        'selfcheck': ["I can report statements, questions and commands accurately.",
                      "I use reporting verbs beyond 'say'."],
        'answers': {
            'A': ["was working", "had finished", "had parked (or: parked)", "not to", "to help", "taking"],
            'B': ["He said (that) he never lied. / He said (that) he never lies.",
                  "They asked when the results would be announced.",
                  "He told me that he was tired.",
                  "She suggested going early. / She suggested that I go early.",
                  "He denied breaking the window.", "answers vary"],
        },
    },
}

L14 = {
    'n': 14, 'part_no': 7, 'part_title': 'Sound More Natural and Advanced',
    'title': 'Participles and Advanced Sentence Patterns',
    'goal': 'combine ideas concisely without losing clarity',
    'intro': "Participles are how English professionals compress ideas — speed without confusion.",
    'hook': [
        "Combine these ideas aloud, any way you like:",
        "•  The team was exhausted. They finished the project on time.",
        "•  She opened the letter. She found the news she had waited for.",
        "Which version sounds most professional?",
    ],
    'rules': [
        {'label': 'Rule 1 — Present and past participles as adjectives',
         'formula': ["-ing (present participle)  →  causes the feeling:  a boring lecture",
                     "-ed (past participle)  →  feels the effect:  bored students"],
         'text': ["The rule: things are -ing; people (and animals) are usually -ed — because they feel it."],
         'examples': ["The film was fascinating.  (the film causes interest)",
                      "I was fascinated.  (I felt it)",
                      "tiring work / tired workers · confusing news / confused readers"],
         'remember': ["Some -ing words describe a person's behaviour instead: 'He is very interesting' "
                      "(he holds my attention) vs 'He is very interested' (he feels interest)."]},
        {'label': 'Rule 2 — Participial clauses: the professional connector',
         'formula': ["Verb-ing …, subject + verb   →  same time / reason",
                     "Having + past participle …, subject + verb   →  earlier action",
                     "Past participle …, subject + verb   →  passive meaning",
                     "Used carefully, these replace 'because/after/while + full clause'"],
         'text': ["Participial clauses open or close a sentence with compressed information. "
                  "Use them in formal speech and writing."],
         'examples': ["Having finished the report, she left the office.  (After she had finished…)",
                      "Written in 1963, the novel is still popular.  (The novel, which was written…)",
                      "Walking to the station, I realised my mistake.  (While I was walking…)"],
         'remember': ["In a reduced opening clause with no stated subject, the understood subject should match the main clause: 'Walking to the station, I got soaked' (I was walking), not 'Walking to the station, the rain started.' An absolute clause names its own subject: 'With prices rising, families are worried.'"]},
        {'label': 'Rule 3 — Absolute and fronted patterns for emphasis',
         'formula': ["Fronted participle:  'Considering the costs…', 'Given the evidence…', 'Looking at the results…'",
                     "With + noun + participle:  'With prices rising, families are worried.'",
                     "Having been + participle:  'Having been warned, we prepared carefully.'"],
         'text': ["These patterns frame a whole clause — they sound composed and formal."],
         'examples': ["Given the circumstances, we agreed to wait.",
                      "With the deadline approaching, the team worked faster.",
                      "All things considered, it was a success."],
         'remember': ["'Given' = when you consider; 'considering' = taking into account; "
                      "'all things considered' = final judgement phrase."]},
        {'label': 'Rule 4 — Concise combination: fewer words, same meaning',
         'formula': ["'She opened the letter and she read it slowly.'  →  'Opening the letter, she read it slowly.'",
                     "Two actions → one main verb + participle (if the subject is the same)."],
         'text': ["Concision is not using difficult words; it is removing whole clauses."],
         'examples': ["Because he had not slept, he made mistakes. → Not having slept, he made mistakes.",
                      "The report, which was published today, contains errors. → The report published today contains errors."],
         'remember': ["Do not over-compress speech. One or two participial clauses per answer is plenty."]},
    ],
    'differences': [
        {'title': '-ing vs -ed adjectives',
         'rows': [
             ["an exciting game", "excited players", "The game causes excitement; the players feel it."],
             ["a tiring day", "tired students", "The day causes tiredness; the students experience it."],
         ], 'headers': ['-ing (causes the feeling)', '-ed (feels it)', 'Example']},
        {'title': 'participle clause vs full clause',
         'rows': [
             ["Having finished, she left.", "After she had finished, she left.", "Same meaning; the participle version is compressed and formal."],
             ["Written in haste, the report had errors.", "The report, which was written in haste, had errors.", "Compression with a passive participle."],
         ], 'headers': ['Participle clause (compressed)', 'Full clause', 'Why']},
        {'title': 'the subject rule',
         'text': ["In a reduced participle clause with no stated subject, the understood subject should normally match the main clause: "
                  "'Opening the door, I felt the cold.' (I opened), not 'Opening the door, the room was cold.' Absolute clauses state their own subject, as in 'Weather permitting, we will leave.'"]},
    ],
    'practice_a': [
        "The lecture was so __________ (bore) that half the class fell asleep.",
        "We were __________ (amaze) by the results.",
        "__________ (finish) his speech, he answered questions.",
        "__________ (warn) about the traffic, we left early.",
        "__________ the prices rising, families are saving more.  (with / despite)",
        "__________ (walk) into the room, she noticed the broken window.",
    ],
    'practice_b': [
        "Combine with a participle: 'Because she had studied hard, she passed easily.'",
        "Combine with a participle: 'The man who was standing at the door waved.'",
        "Correct: 'Opening the window, the cold air came in.'",
        "Rewrite with 'Given': 'When you consider the costs, the plan is unrealistic.'",
        "Correct: 'I am very interesting in history.'",
        "Compress one of your own sentences with 'Having + past participle'.",
    ],
    'pair': {
        'intro': "The formal briefing. Each partner gives a 60-second briefing on a situation "
                 "(a project, a trip, an event). The briefing must use at least two participle clauses.",
        'task': ["Include: one 'Having + past participle', one opening with 'Given/Considering/With', "
                 "and one -ed/-ing adjective pair.",
                 "Partner listens and reports the briefing back in one sentence."],
        'output': "One 60-second briefing per partner containing the three required structures, plus "
                  "a listener's one-sentence report-back that matches the briefing's content.",
        'criteria': ["participle clauses have correct subjects",
                     "forms are accurate (-ing / -ed / having done)",
                     "meaning stays clear after compression",
                     "listener's report matches the content"],
    },
    'advanced': {
        'base': ["Drill -ed/-ing pairs about real life: tired/tiring, confused/confusing, interested/interesting — five sentences.",
                 "Practise the subject rule: make two correct participle openings from your week."],
        'upgrade': ["Use 'There being + noun': 'There being no further questions, the meeting ended.'",
                    "Use 'Not having… / Never having…': 'Never having travelled abroad, he found the airport overwhelming.'",
                    "Use participles in formal closings: 'Considering all the evidence, we recommend…'"],
    },
    'realtalk': {
        'plan': "Planning (45 seconds): choose the policy and write three lines — your evidence, "
                "your recommendation, your closing judgement. Mark where 'Given…' and 'Having…' will "
                "go so the openings come out whole.",
        'task': "Ninety-second formal recommendation: recommend one policy for your workplace or school "
                "(more training, a schedule change, a new rule). Open with 'Considering…' or 'Given…', "
                "use one 'Having…' clause, and close formally.",
        'model': "Given the number of late arrivals, we recommend shifting the morning meeting to "
                 "nine o'clock. Having reviewed the attendance records, I noticed that most delays "
                 "happen before ten, when the traffic is heaviest. The current schedule is "
                 "frustrating for parents, and several tired employees arrive unprepared. "
                 "Considering the cost of the change — none — the benefit is obvious. All things "
                 "considered, a two-week trial would settle the question.",
        'feedback': ["at least two accurate participle clauses",
                     "-ed/-ing adjectives used correctly",
                     "recommendation is clear and logical",
                     "formal, composed tone"],
    },
    'review': {
        'points': ["-ing adjectives cause feelings; -ed adjectives feel them.",
                   "Participle clauses compress because/after/while clauses — subject must match.",
                   "'Given…', 'Considering…', 'With + noun + participle' frame formal speech."],
        'retrieval': ["Open a sentence with 'Having…' about your day.",
                      "Describe today with one -ing and one -ed adjective."],
        'watch': ["'Opening the window, the room was cold.' (subject mismatch).",
                  "'interesting in' → 'interested in'."],
        'selfcheck': ["I can compress two clauses into one formal sentence.",
                      "My participle clauses keep the correct subject."],
        'answers': {
            'A': ["boring", "amazed", "Having finished", "Having been warned / Warned", "With", "Walking"],
            'B': ["Having studied hard, she passed easily.",
                  "The man standing at the door waved.",
                  "Opening the window, I felt the cold air come in. / As I opened the window, the cold air came in.",
                  "Given the costs, the plan is unrealistic.",
                  "I am very interested in history.", "answers vary"],
        },
    },
}

L15 = {
    'n': 15, 'part_no': 8, 'part_title': 'Speak with Confidence',
    'title': 'Hedging, Emphasis, and Natural Inversion',
    'goal': 'control certainty, emphasis and formality like an educated speaker',
    'intro': "The difference between good and excellent English is control: how strong, how sure, how formal.",
    'hook': [
        "Two speakers say: 'The plan will fail.' / 'The plan may well fail.'  Which sounds more educated? Why?",
        "Give the same opinion twice: once very certain, once carefully hedged. How does the effect change?",
    ],
    'rules': [
        {'label': 'Rule 1 — Hedging: the art of careful claims',
         'formula': ["may / might / could + base verb  ·  may well  ·  it is likely that …",
                     "seem to / tend to / appear to  ·  generally / broadly / in most cases",
                     "it could be argued that …  ·  one possible explanation is …"],
         'text': ["Hedging can make a claim sound measured when evidence is limited or a conclusion is uncertain. Academic and professional speakers often hedge; too much hedging, however, can make a message unclear."],
         'examples': ["The results suggest a small improvement.",
                      "This policy may well reduce costs in the long run.",
                      "It could be argued that the data is incomplete."],
         'remember': ["Too many hedges sound vague: 'It might perhaps possibly be…' — one careful hedge per claim is enough."]},
        {'label': 'Rule 2 — Emphasis: clefts and focus',
         'formula': ["It is/was + emphasised part + who/that …   (cleft)",
                     "What I need is …  ·  What surprised me was …  (wh-cleft)",
                     "do/does/did + base verb  (auxiliary emphasis): 'I do believe you.'"],
         'text': ["Cleft sentences split one idea in two to put the spotlight on one part."],
         'examples': ["It was the price that changed my mind.  (not the quality)",
                      "What I love about this city is its energy.",
                      "She did call — I saw the message."],
         'remember': ["In speech, stress the focused word: 'It was JOHN who…'."]},
        {'label': 'Rule 3 — Inversion: formal emphasis',
         'formula': ["Negative opener + auxiliary + subject + verb:",
                     "Never have I seen …  ·  Not only did she …, but she also …",
                     "Rarely / Seldom / Little / Nowhere + auxiliary + subject + verb",
                     "Only + adverbial + auxiliary + subject + verb:  Only then did I understand …",
                     "No sooner … than …  ·  Hardly … when …  ·  Under no circumstances …"],
         'text': ["When a sentence begins with a strong negative or limiting phrase, English reverses the "
                  "order — like raising your voice politely."],
         'examples': ["Never have I been so surprised.",
                      "Not only did he apologise, but he also refunded the money.",
                      "Only after the meeting did I understand the decision."],
         'remember': ["Inversion is punctuation for the ear. Use it once for impact — never in every sentence."]},
        {'label': 'Rule 4 — Choosing the right level of certainty and formality',
         'formula': ["Strong prediction/inference: will (prediction) · must be (strong deduction)",
                     "Expectation/likelihood: should · be likely to · may well",
                     "Possibility: may · might · could (no fixed ranking; context and speaker matter)",
                     "formal markers: passive · inversion · clefts · hedging · full forms"],
         'text': ["Match the strength of your language to your evidence and your audience. "
                  "Over-claiming damages credibility; careful claims build it."],
         'examples': ["Formal: 'Should you require further information, please do not hesitate to contact us.'",
                      "Neutral: 'If you need more information, contact us.'",
                      "Casual: 'Just call me if you need anything.'"],
         'remember': ["A careful hedge signals that you are matching the strength of your claim to the evidence — not that you lack confidence."]},
    ],
    'differences': [
        {'title': 'certainty levels',
         'rows': [
             ["The plan will succeed.  (certain)", "The plan may well succeed.  (likely)", "The plan might succeed.  (possible)", "Same claim, three levels of commitment."],
         ], 'headers': ['Certain: will', 'Likely: may well', 'Possible: might', 'The idea']},
        {'title': 'normal order vs inversion',
         'rows': [
             ["I have never seen such a mess.", "Never have I seen such a mess.", "The inverted version is emphatic and formal — powerful in speeches, heavy in casual chat."],
         ], 'headers': ['Normal order', 'Inversion (emphatic)', 'The effect']},
        {'title': 'cleft focus changes meaning',
         'rows': [
             ["I met the manager yesterday.", "It was the manager who I met yesterday.", "What I did yesterday was meet the manager.", "Each version puts the spotlight in a different place."],
         ], 'headers': ['Basic sentence', 'It-cleft', 'Wh-cleft', 'The idea']},
    ],
    'practice_a': [
        "__________ have I heard such a convincing argument.  (Never / Ever)",
        "Not only __________ (she / pass) the exam, but she also got the highest mark.",
        "Only after reading it twice __________ (I / understand) the letter.",
        "The data __________ (suggest) that costs are falling.  (hedged claim)",
        "It was __________ the deadline that forced us to decide.  (focus on the reason)",
        "This method __________ (tend) to work better with small groups.",
    ],
    'practice_b': [
        "Hedge the claim: 'This policy will reduce costs.'",
        "Make a cleft: 'The price changed my mind.'  (focus the price)",
        "Invert: 'I had rarely felt so confident.'",
        "Correct: 'Never I have seen such a mess.'",
        "Say the same request at two formality levels: you need more time for a report.",
        "Use 'Not only … but also' with inversion about two of your skills.",
    ],
    'pair': {
        'intro': "The panel discussion. Question: 'What will work look like in ten years?' Each partner "
                 "gives a one-minute answer using hedging and at least one emphatic structure "
                 "(cleft or inversion). Then ask each other one hard follow-up question.",
        'task': ["Plan for ten seconds only. In your answer include: one hedge (may well / tend to / it could be argued), "
                 "one cleft (It is… that / What… is), and one conclusion.",
                 "Answer the follow-up question carefully — hedging is welcome when you are unsure."],
        'output': "Two one-minute answers per partner, each containing one well-placed hedge, one "
                  "accurate emphasis structure and a clear conclusion — plus one careful answer to "
                  "the partner's hard follow-up question.",
        'criteria': ["claims are hedged appropriately (not over-hedged)",
                     "emphasis structures used accurately once or twice",
                     "certainty level matches the evidence",
                     "answers stay clear and confident"],
    },
    'advanced': {
        'base': ["Practise three certainty groups in context: strong prediction/inference (will / must be), expectation or likelihood (should / may well), and possibility (may / might / could). Explain what evidence supports each choice.",
                 "Learn three inversion frames by heart: 'Never have I…' · 'Not only did…' · 'Only then did…'."],
        'upgrade': ["Use 'little did he know…' and 'little did I realise…' in storytelling.",
                    "Use litotes (understatement): 'not unlike', 'no small achievement', 'not bad at all'.",
                    "Use formal conditional inversion in writing-style speech: 'Were this proposal accepted…' · 'Had we known…'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): one claim plus its evidence for the hedge; one fact worth "
                "spotlighting for the cleft; one strong statement for the inversion. Write single "
                "keywords, not sentences — you will not read them.",
        'task': "Two-minute formal talk: 'One change that would improve education in my country.' "
                "Include: a hedged claim, one cleft sentence, one inversion, and a clear closing. "
                "Speak with confidence — no notes.",
        'model': "Education in my country will change in one area above all: access. It is "
                 "broadband that will decide who benefits from that change. Rarely have we seen "
                 "technology move so quickly in our cities, yet rural schools are often left without "
                 "a reliable connection. The government could take the first step by funding "
                 "internet in district centres — this may well be the cheapest investment of the "
                 "decade. If the infrastructure were in place, teachers could share materials "
                 "overnight. In closing, I would say one thing: connect the schools first, and the "
                 "rest will follow.",
        'feedback': ["hedging used for claims, not for every word",
                     "at least one cleft and one inversion — accurate",
                     "register is consistently formal",
                     "closing states the position clearly"],
    },
    'review': {
        'points': ["Hedging (may well, tend to, it could be argued) makes claims professional.",
                   "Clefts and do-emphasis spotlight information: 'It was X that…' / 'What I need is…'.",
                   "Inversion follows negative openers: 'Never have I…' — use for impact, sparingly."],
        'retrieval': ["Make one claim at three certainty levels.",
                      "Say one cleft and one inversion from memory."],
        'watch': ["'Never I have seen' → 'Never have I seen'.",
                  "Over-hedging sounds vague; over-inverting sounds theatrical."],
        'selfcheck': ["I can control how strong my claims sound.",
                      "I can emphasise with clefts and inversion — accurately and sparingly."],
        'answers': {
            'A': ["Never", "did she pass", "did I understand", "suggests (or: suggest)", "the deadline", "tends"],
            'B': ["This policy may well reduce costs. / This policy is likely to reduce costs.",
                  "It was the price that changed my mind.",
                  "Rarely had I felt so confident.",
                  "Never have I seen such a mess.", "answers vary", "answers vary"],
        },
    },
}

L16 = {
    'n': 16, 'part_no': 8, 'part_title': 'Speak with Confidence',
    'title': 'Grammar in Real Conversation',
    'goal': 'bring all the course grammar together in free, accurate, confident speech',
    'intro': "This lesson is not new theory — it is the moment everything you have learned becomes your voice.",
    'hook': [
        "Warm-up round with a partner: speak for thirty seconds on any topic. Your partner listens "
        "and names every grammar structure they recognise (tenses, conditionals, passives…). Swap.",
    ],
    'rules': [
        {'label': 'The course grammar: one map',
         'formula': ["TIME:        tenses · storytelling · reported speech",
                     "CHOICE:      modals · conditionals · wishes · gerunds/infinitives",
                     "SHAPE:       questions · linkers · relatives · participles · passive · causative",
                     "STYLE:       comparisons · hedging · emphasis · inversion"],
         'text': ["Every lesson in this course belongs to one of these four jobs. When you speak, "
                  "ask: what job does my next sentence need?"],
         'examples': ["Tell the story (time) → explain the cause (choice) → describe the people (shape) → give your view (style)."],
         'remember': ["Accuracy first, then range. A clear sentence in the right tense beats a fancy one in the wrong tense."]},
        {'label': 'The speaking strategy: three steps to confident speech',
         'formula': ["1. THINK the meaning  →  2. CHOOSE the structure  →  3. SAY it whole",
                     "If stuck: simplify — and keep going. Repair later: 'What I mean is…'"],
         'text': ["Fluency is not speed; it is continuity. Keep the message moving and fix problems as you go."],
         'examples': ["'If I would have known…' — stop, repair: 'If I had known, I would have come.'"],
         'remember': ["Self-repair is a strength in speaking tests — it shows control."]},
    ],
    'differences': [
        {'title': 'recognition vs use',
         'text': ["You already recognise most course structures. The final step is producing them "
                  "under pressure — that is what the challenges below train."]},
    ],
    'practice_a': [
        "Fix and explain: 'I have seen him yesterday.'",
        "Fix and explain: 'If I will have time, I will help.'",
        "Fix and explain: 'Despite of the price, we bought it.'",
        "Fix and explain: 'He suggested me to wait.'",
        "Fix and explain: 'Never I have been so tired.'",
        "Fix and explain: 'I look forward to meet you.'",
    ],
    'practice_b': [
        "Combine (participles): 'Because he had not slept, he made errors.'",
        "Report: 'Don't worry,' she said.  (2 forms)",
        "Compare with nuance: 'This option is better.'  (use a degree word + reason)",
        "Make it passive and formal: 'Someone has changed the schedule.'",
        "Hedge the claim: 'This method is the best.'",
        "Ask a polite indirect question about tomorrow's schedule.",
    ],
    'pair': {
        'intro': "The grammar gym — four rounds. Each round: speak for one minute on the topic, using the "
                 "target structures. Partner counts the structures used and gives feedback.",
        'task': ["Round 1 — Storytelling: a challenge you overcame.  (tenses, participles)",
                 "Round 2 — Advice: a friend must choose between two jobs.  (modals, conditionals)",
                 "Round 3 — Report: what your colleagues or classmates have decided.  (reported speech, passives)",
                 "Round 4 — Argument: one change that would improve your school or workplace.  (linkers, hedging, emphasis)"],
        'output': "Four one-minute rounds per pair: each round delivered without notes, with the "
                  "target structures counted aloud and at least one self-repair noted by the "
                  "listener.",
        'criteria': ["structures match the round's target",
                     "errors are self-corrected during speech",
                     "ideas are clear and well-linked",
                     "confidence and continuity are maintained"],
    },
    'advanced': {
        'base': ["Re-do any lesson exercise that felt hard — out loud, not on paper.",
                 "For each of the four jobs (time / choice / shape / style), write three sentences from your own life."],
        'upgrade': ["Stack structures in one sentence: 'Had I known that the report would be delayed, I would have asked for help.'",
                    "Use style deliberately: open a talk with an inversion, hedge your main claim, close with a cleft.",
                    "Practise repair phrases: 'What I mean is…' · 'Let me rephrase that…' · 'Or rather…'"],
    },
    'realtalk': {
        'plan': "Planning (one minute): three lines only — the story (when and what changed), the "
                "decision (what you chose and why), the goal (what comes next and how you will know "
                "you have reached it). Then deliberately choose two 'show-off' structures.",
        'task': "Final speaking challenge (two minutes): 'How I have changed — and what comes next.' "
                "Tell a story, explain a decision, and state a goal. Use at least six different structures "
                "from the course. This is also your practice for the Final Speaking Assessment.",
        'model': "Two years ago I avoided speaking English in class because I was afraid of mistakes "
                 "— I would translate every sentence in my head first. Joining a speaking club "
                 "changed that: within a month, I had made friends who corrected me kindly. Since "
                 "then I have been practising almost every day, and my teachers have noticed the "
                 "difference. I've decided to take the TOEFL next spring, which is why I'm "
                 "recording myself twice a week. If I keep this up, the score will take care of "
                 "itself. What I need most now is confidence under pressure — and that comes only "
                 "from speaking.",
        'feedback': ["range of structures used accurately",
                     "clear story shape with linking",
                     "at least one hedged or emphatic structure",
                     "confident, continuous delivery with natural self-repair"],
    },
    'review': {
        'points': ["Course grammar does four jobs: time, choice, shape, style.",
                   "Speak in three steps: think meaning → choose structure → say it whole.",
                   "Accuracy first, then range; self-repair shows control."],
        'retrieval': ["Name all four grammar jobs and one structure for each.",
                      "Tell a one-minute story using three different course structures."],
        'watch': ["Choosing complexity over accuracy — simple and correct is always better.",
                  "Freezing on errors — repair and continue instead."],
        'selfcheck': ["I can use structures from at least six lessons in free speech.",
                      "I can self-repair and keep talking."],
        'answers': {
            'A': ["I saw him yesterday. (finished time)",
                  "If I have time, I will help.",
                  "Despite the price, we bought it. / Although it was expensive, we bought it.",
                  "He suggested waiting. / He suggested that I wait.",
                  "Never have I been so tired.",
                  "I look forward to meeting you."],
            'B': ["Not having slept, he made errors.",
                  "She told me not to worry. / She reassured me.",
                  "answers vary — degree word + reason required",
                  "The schedule has been changed.",
                  "This method may well be the best. / This method is probably the best. (answers vary)",
                  "answers vary — indirect word order required"],
        },
    },
}

LESSONS_13_16 = [L13, L14, L15, L16]


def render_all(doc, keys_registry):
    for L in LESSONS_13_16:
        render_lesson(doc, L, keys_registry)

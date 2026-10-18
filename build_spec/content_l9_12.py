# -*- coding: utf-8 -*-
"""Lessons 9-12 — Part Five: Describe and Explain; Part Six: Speak with Greater Precision."""
from lesson_template import render_lesson

L9 = {
    'n': 9, 'part_no': 5, 'part_title': 'Describe and Explain',
    'title': 'Passive Voice in Natural English',
    'goal': 'choose between active and passive for the right focus',
    'intro': "The passive is not a fancy extra — it is how English focuses on what matters.",
    'hook': [
        "Look at these two sentences. Which sounds like news, and which sounds like a story?",
        "•  Someone stole my bicycle yesterday.",
        "•  My bicycle was stolen yesterday.",
        "Tell your partner about something that happened to you — once with the active, once with the passive. Which version focuses on the result?",
    ],
    'rules': [
        {'label': 'Rule 1 — How the passive is built',
         'formula': ["be + past participle  (the tense lives in 'be')",
                     "Present: is/are done  ·  Past: was/were done",
                     "Future: will be done  ·  Perfect: has/have been done",
                     "Modals: can/must/should be done"],
         'text': ["To make a passive, change the object of an active sentence into the subject, "
                  "and put the verb into 'be + participle'."],
         'examples': ["They clean the office every day. → The office is cleaned every day.",
                      "They will announce the results tomorrow. → The results will be announced tomorrow."],
         'remember': ["Add the agent with 'by' only when it matters: 'The novel was written by Atiq Rahimi.'"]},
        {'label': 'Rule 2 — When to use the passive',
         'formula': ["Use the passive when: the result matters more · the doer is unknown, obvious, "
                     "or general ('people', 'they') · you want objective or formal tone"],
         'text': ["News, reports, research and professional communication often use the passive to focus on events or processes. The agent may be left out when it is unknown or unimportant, or included in a by-phrase when it matters."],
         'examples': ["Mistakes were made in the report.  (polite — no blame)",
                      "The vaccine is being tested in several countries.",
                      "The meeting has been postponed until Monday."],
         'remember': ["In everyday stories about yourself, the active is usually better: "
                      "'I broke my phone' (clearer than 'my phone was broken by me')."]},
        {'label': 'Rule 3 — Reporting verbs and passive patterns',
         'formula': ["It is said / believed / thought that …",
                     "He is said to be / to have been …",
                     "have/get something done  (see Lesson 10)"],
         'text': ["These patterns sound objective and educated — very useful in formal speaking."],
         'examples': ["It is widely believed that reading improves writing.",
                      "She is said to speak five languages."],
         'remember': ["'It is said that he left' = 'He is said to have left.' (the leaving is earlier)."]},
    ],
    'differences': [
        {'title': 'active vs passive: what changes?',
         'rows': [
             ["Someone attacked the man.", "The man was attacked.", "The passive can omit the agent — the event or result takes focus. Add a by-phrase if the agent matters."],
             ["The committee approved the plan.", "The plan was approved.", "Formal and objective: the decision matters, not the committee."],
         ], 'headers': ['Active', 'Passive', 'Why']},
        {'title': 'get-passive vs be-passive',
         'text': ["'get' + participle is more informal and often emotional or unexpected: 'He got fired.' "
                  "Compare 'He was dismissed.' (formal). 'Get' is common in speech: 'They got married last year.'"]},
        {'title': 'false passives',
         'text': ["Some verbs look passive but are not: 'The book sold well.' · 'The door opened.' "
                  "These describe how something happened, not an action done to it."]},
    ],
    'practice_a': [
        "The bridge __________ (build) in 2019.",
        "The results __________ (announce) tomorrow.",
        "This room __________ (clean) every morning.",
        "My wallet __________ (steal) on the bus yesterday.",
        "A new policy __________ (just / introduce).",
        "The letters must __________ (send) before noon.",
    ],
    'practice_b': [
        "Rewrite in the passive: 'Someone has stolen my bicycle.'",
        "Rewrite in the active: 'The decision was made by the board.'",
        "Rewrite formally: 'People say that he is the best candidate.'",
        "Correct: 'The house was builted in 1990.'",
        "Correct: 'My phone was stolen by me.'  (make it natural)",
        "Report the news with a passive: 'They will close the road tomorrow.'",
    ],
    'pair': {
        'intro': "The newsroom. Each partner is a reporter. Describe three events from yesterday "
                 "(local, personal or world news) using the passive. The editor (partner) asks: who did it?",
        'task': ["Events: an accident · a new opening · a rule change · a sports result · something at work or school.",
                 "Use at least two passives and one reporting structure (It is said / It is believed)."],
        'output': "Three news items per reporter in report-style speech, with two accurate passives "
                  "and one reporting structure, surviving the editor's 'who did it?' question.",
        'criteria': ["passive forms are accurate across tenses",
                     "the agent is given only when it matters",
                     "tone is objective and report-like",
                     "the editor's questions get clear answers"],
    },
    'advanced': {
        'base': ["Drill passive formation in four tenses: present, past, future, perfect — with objects from your daily life.",
                 "Learn the reporting pair: 'It is said that…' / 'He is said to…' — three real examples."],
        'upgrade': ["Use the passive with 'get' for informal emotional colour: 'He got promoted after only six months.'",
                    "Use 'It is claimed / alleged / assumed that…' in formal discussion.",
                    "Use passive + participle clauses in writing-style speech: 'Founded in 1971, the school now teaches over a thousand students.'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): pick three real events from this week — two that affect "
                "people rather than doers, one you want to comment on. Fix the tense of each passive "
                "(is/are, was/were, will be, has been).",
        'task': "Ninety-second news brief: report three things that happened this week (in your city, "
                "your work or your studies). Use the passive for events and one reporting structure. "
                "Finish with one comment in the active voice.",
        'model': "Three things happened this week. A new footbridge was opened near the school, so "
                 "traffic has been diverted along the main road. It is said that the council will "
                 "publish the survey results on Friday, and two main streets were cleaned every "
                 "night last week. My own view is simple: the council should publish the data openly "
                 "— that is the first thing I would ask for.",
        'feedback': ["at least three accurate passive structures",
                     "objective reporting tone",
                     "agent mentioned only when important",
                     "clear final comment (active voice)"],
    },
    'review': {
        'points': ["Passive = be + past participle; the tense lives in 'be'.",
                   "Use the passive for results, unknown/obvious doers, and objective tone.",
                   "'It is said that…' = 'He is said to…' — both are formal and natural."],
        'retrieval': ["Put three objects from your room into passive sentences (different tenses).",
                      "Say one formal reporting sentence about a person you know."],
        'watch': ["'was builted' → 'was built'.",
                  "Don't use the passive for your own story if the active is clearer: 'I lost my keys' is better than 'my keys were lost by me'."],
        'selfcheck': ["I can form the passive in four tenses.",
                      "I choose active or passive for the right focus."],
        'answers': {
            'A': ["was built", "will be announced", "is cleaned", "was stolen",
                  "has just been introduced", "be sent"],
            'B': ["My bicycle has been stolen.", "The board made the decision.",
                  "It is said that he is the best candidate. / He is said to be the best candidate.",
                  "The house was built in 1990.", "I lost my phone. / I had my phone stolen. (answers vary)",
                  "The road will be closed tomorrow."],
        },
    },
}

L10 = {
    'n': 10, 'part_no': 5, 'part_title': 'Describe and Explain',
    'title': 'Causative Structures',
    'goal': 'talk about services, arrangements, influence and responsibility naturally',
    'intro': "English has a special grammar for 'I arranged it — someone else did it'. This is it.",
    'hook': [
        "Talk with a partner: what do people usually 'have done' in your city?",
        "•  haircuts · repairs · cleaning · deliveries · tailoring",
        "Which do you do yourself, and which do you pay others for? Why?",
    ],
    'rules': [
        {'label': 'Rule 1 — have/get something done',
         'formula': ["have + object + past participle   →  arrange for someone to do it",
                     "get + object + past participle   →  the same meaning, more informal",
                     "Negative/question:  I haven't had it done  ·  Did you get it fixed?"],
         'text': ["Use this when you arrange or pay for a service. The doer is unimportant or obvious "
                  "(a professional, a shop, a technician)."],
         'examples': ["I had my car serviced last week.",
                      "She's getting her house painted this month.",
                      "We need to have the documents translated."],
         'remember': ["This structure often appears in stories about problems: 'I had my phone stolen on the bus.' "
                      "(something happened to my possession — not a service I ordered!)"]},
        {'label': 'Rule 2 — make, let, have, get + person + verb',
         'formula': ["make + person + base verb   →  force (no choice)",
                     "let + person + base verb   →  allow (no 'to')",
                     "have + person + base verb   →  instruct/arrange (informal)",
                     "get + person + to + base verb   →  persuade (with 'to'!)"],
         'text': ["These four verbs control other people's actions — with different levels of force."],
         'examples': ["The teacher made us rewrite the essay.",
                      "My parents let me travel alone when I was sixteen.",
                      "I'll have my assistant call you.",
                      "I finally got my brother to help me."],
         'remember': ["'get' is the only one with 'to': 'get someone to do something'."]},
        {'label': 'Rule 3 — Talking about services and arrangements',
         'formula': ["I need to have my… done  ·  I'm having my… done on Tuesday",
                     "How much do you charge to…?  ·  Could you … for me?",
                     "I get my… done at…  (regular arrangement)"],
         'text': ["These chunks are the real-life service English: shops, clinics, offices, travel."],
         'examples': ["I get my hair cut at the same place every month.",
                      "I'm having my laptop repaired — I hope it's ready by Friday."],
         'remember': ["For one action by one person that you do yourself or that isn't a service, "
                      "use the normal active: 'I fixed my laptop' — not 'I had my laptop fixed' (unless you arranged it)."]},
    ],
    'differences': [
        {'title': 'service vs accident',
         'rows': [
             ["I had my car washed.", "I had my car damaged in the storm.", "Same grammar, different world: one is a service I ordered; the other is something that happened to me."],
         ], 'headers': ['Service I ordered', 'Accident that happened', 'Why']},
        {'title': 'causative verbs compared',
         'rows': [
             ["She made me apologise.", "She let me leave.", "She had me rewrite it.", "She got me to help her.", "force → allow → instruct → persuade. The grammar tells you the relationship."],
         ], 'headers': ['make — force', 'let — allow', 'have — instruct', 'get — persuade', 'The relationship']},
        {'title': 'make vs let in passives',
         'text': ["'make' keeps 'to' when it becomes passive: 'I was made to wait an hour.' "
                  "But 'let' does not: 'They let me go' → 'I was allowed to go' (we usually avoid 'I was let go' except in fixed expressions)."]},
    ],
    'practice_a': [
        "I need to have my suit __________ (alter) before the wedding.",
        "When did you last get your hair __________ (cut)?",
        "The noise made me __________ (lose) my concentration.",
        "They let us __________ (use) the kitchen.",
        "I'm having my eyes __________ (test) on Thursday.",
        "She finally got her son __________ (eat) the vegetables.",
    ],
    'practice_b': [
        "Rewrite with have: 'I paid someone to service my car.'",
        "Rewrite with get (persuasion): 'After much discussion, my friend agreed to drive us.'",
        "Correct: 'I will get my car to repair tomorrow.'",
        "Correct: 'She made me to wait outside.'",
        "Describe something you had done recently (service or accident — say which).",
        "Ask politely at a shop: you need your phone screen replaced (causative question).",
    ],
    'pair': {
        'intro': "The service conversation. Partner A runs a repair shop / salon / clinic; Partner B has "
                 "problems with their possessions (car, hair, laptop, phone). Negotiate what will be done, "
                 "when, and for how much — using causatives throughout.",
        'task': ["Partner B: describe at least three things that need doing (need to have… done).",
                 "Partner A: explain what you will do (I'll have… done), what the customer should do, "
                 "and the price. Use make/let/get at least once."],
        'output': "One completed service negotiation per pair: at least three things that need doing, "
                  "a price and a time agreed, and one make/let/get sentence used accurately.",
        'criteria': ["causative forms are accurate (have/get + object + participle)",
                     "service language sounds natural",
                     "prices and times are agreed",
                     "the conversation includes influence language (make/let/get)"],
    },
    'advanced': {
        'base': ["Drill the four causatives: make / let / have / get — one true sentence each about people you know.",
                 "Practise the service chunks: 'I need to have my… done.' · 'When can you have it ready?'"],
        'upgrade': ["Use 'have someone do' for professional delegation: 'I'll have the team look into it.'",
                    "Use experience-causatives in narrative: 'He had us all laughing for an hour.' · 'The film had me thinking for days.'",
                    "Use 'get round to + -ing' and 'end up + -ing': 'I finally got round to having the flat painted.'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): choose a real or invented bad day. Plan three moments — one "
                "service you arranged (had something done), one accident (had something happen to "
                "me), and one make/let/get moment.",
        'task': "Story challenge (one minute): 'A day when everything went wrong.' Use at least two "
                "causatives (including 'had something done' or 'had something happen to me'), and explain "
                "what you made, let or got someone to do afterwards.",
        'model': "Last Friday started badly. I had my car serviced the evening before, but it still "
                 "wouldn't start, so I let my neighbour try the battery — he is a mechanic. Then the "
                 "courier delivered my laptop to the wrong company, and I had to wait while it was "
                 "forwarded. My manager made me postpone the presentation until the afternoon, and I "
                 "finally got my brother to drive me to work. By the evening the whole day had me "
                 "laughing — what a mess!",
        'feedback': ["causative structures used accurately",
                     "clear distinction between service and accident",
                     "story is easy to follow",
                     "at least one make/let/get structure"],
    },
    'review': {
        'points': ["have/get + object + participle = arrange a service (or: something happened to me).",
                   "make = force; let = allow; have = instruct; get = persuade (get + to + verb).",
                   "The passive of 'make' keeps 'to': 'I was made to wait.'"],
        'retrieval': ["Say three things you would like to have done this month.",
                      "Describe one person who made you do something and one who let you do something."],
        'watch': ["'get my car to repair' → 'get my car repaired'.",
                  "'made me to wait' → 'made me wait'."],
        'selfcheck': ["I can arrange services with have/get causatives.",
                      "I can express force, permission, instruction and persuasion correctly."],
        'answers': {
            'A': ["altered", "cut", "lose", "use", "tested", "to eat"],
            'B': ["I had my car serviced.", "I got my friend to drive us. / After much discussion, I got my friend to drive.",
                  "I will get my car repaired tomorrow.",
                  "She made me wait outside.", "answers vary",
                  "Could you have my phone screen replaced? / How much would it cost to have my screen replaced?"],
        },
    },
}

L11 = {
    'n': 11, 'part_no': 6, 'part_title': 'Speak with Greater Precision',
    'title': 'Gerunds and Infinitives',
    'goal': 'choose the right verb pattern for your meaning',
    'intro': "Some verbs want -ing after them; some want 'to'. Getting this right marks you as advanced.",
    'hook': [
        "Finish the sentences — then compare with your partner:",
        "•  I enjoy…   ·   I hope…   ·   I avoid…   ·   I decided…",
        "Which verbs feel natural with -ing? Which with 'to'? You already know more than you think.",
    ],
    'rules': [
        {'label': 'Rule 1 — Verbs that take the gerund (-ing)',
         'formula': ["enjoy · avoid · consider · finish · keep · mind · miss · practise · suggest · "
                     "give up · feel like · can't help  +  verb-ing"],
         'text': ["These verbs talk about experiences, reactions and activities as things."],
         'examples': ["I enjoy reading before bed.",
                      "He avoided making eye contact.",
                      "Would you mind opening the window?"],
         'remember': ["When a verb follows mind directly, use -ing: 'Do you mind waiting?' Other patterns exist, such as 'Would you mind if I opened the window?'" ]},
        {'label': 'Rule 2 — Verbs that take the infinitive (to + verb)',
         'formula': ["agree · decide · hope · intend · learn · manage · offer · plan · promise · "
                     "refuse · seem · tend · want · would like  +  to + base verb"],
         'text': ["These verbs look forward — to intentions, decisions and attempts."],
         'examples': ["She decided to change careers.",
                      "We plan to visit next spring.",
                      "He seems to know everyone."],
         'remember': ["'would like to…' is polite desire: 'I'd like to ask a question.'"]},
        {'label': 'Rule 3 — Verbs that change meaning',
         'formula': ["remember / forget / regret / stop / try / go on / mean",
                     "+ -ing  →  the earlier action   ·   + to  →  the later action (or purpose)"],
         'text': ["With these verbs, the pattern is not decoration — it changes the meaning."],
         'examples': ["I remember locking the door.  (I did it; I recall that)",
                      "Remember to lock the door.  (don't forget — it comes later)",
                      "He stopped smoking.  (he quit)",
                      "He stopped to smoke.  (he paused his walk for a cigarette)",
                      "I tried restarting the laptop.  (a method)",
                      "I tried to open the window.  (an attempt)"],
         'remember': ["'I mean to do it' = I intend to. 'Missing the bus means walking' = results in."]},
        {'label': 'Rule 4 — Gerund as subject and after prepositions',
         'formula': ["Verb-ing + …  =  the activity as a subject",
                     "Preposition + verb-ing   (about doing · instead of going · before leaving · good at speaking)"],
         'text': ["A gerund can be a subject: 'Swimming keeps me fit.' After any preposition, use -ing."],
         'examples': ["Learning a language takes patience.",
                      "She left without saying goodbye.",
                      "I'm interested in improving my pronunciation."],
         'remember': ["'to' is a preposition in some phrases: look forward to · be used to · object to · "
                      "devote … to · when it comes to. All take -ing: 'I look forward to hearing from you.'"]},
    ],
    'differences': [
        {'title': 'meaning-changing pairs',
         'rows': [
             ["I stopped eating sugar.", "I stopped to eat something.", "quit an activity vs pause an activity for another"],
             ["I remembered to call her.", "I remembered calling her.", "did it because I recalled (to) vs recalled the action (-ing)"],
             ["He tried to move the table.", "He tried moving the table.", "attempt (to) vs experiment/method (-ing)"],
         ], 'headers': ['+ -ing (earlier action)', '+ to (later action)', 'The difference']},
        {'title': 'need + -ing vs need + to',
         'text': ["'The car needs washing.' = 'The car needs to be washed.' The gerund here is passive in meaning. "
                  "Also: 'My hair needs cutting.'"]},
        {'title': 'with prepositions: always -ing',
         'text': ["Common traps: 'interested in learning' (not 'in learn') · 'good at explaining' · "
                  "'instead of complaining' · 'before leaving' · 'after finishing'."]},
    ],
    'practice_a': [
        "Would you mind __________ (help) me with this?",
        "She avoided __________ (answer) the question.",
        "We decided __________ (accept) the offer.",
        "I look forward to __________ (hear) from you.",
        "He stopped __________ (smoke) last year.",
        "She tried __________ (open) the window, but it was stuck.  (an attempt)",
    ],
    'practice_b': [
        "Correct: 'I enjoy to read novels.'",
        "Correct: 'I look forward to meet you.'",
        "Correct: 'She suggested to go early.'",
        "Rewrite with need: 'The room must be cleaned.'",
        "Choose and explain: I remembered (posting / to post) the letter.  (I want to say: I recall doing it)",
        "Make a sentence with 'Instead of…' + -ing about study habits.",
    ],
    'pair': {
        'intro': "The habits interview. Ask each other about routines, plans and preferences — using gerund "
                 "and infinitive patterns in every question and answer.",
        'task': ["Questions to adapt: What do you enjoy doing at weekends? What have you decided to change "
                 "this year? What do you avoid doing? What are you looking forward to?",
                 "Each person must use at least four different gerund/infinitive verbs."],
        'output': "A five-question interview per role: each person answers with at least four "
                  "different gerund/infinitive patterns and asks two follow-up questions.",
        'criteria': ["patterns are accurate (-ing vs to)",
                     "at least one meaning-changing verb used correctly",
                     "conversation flows naturally",
                     "follow-up questions asked"],
    },
    'advanced': {
        'base': ["Learn in chunks, not lists: 'I enjoy swimming' · 'I decided to leave' — five chunks a day.",
                 "Drill the meaning pairs: stop/remember/try — with real examples from your week."],
        'upgrade': ["Use complex subjects: 'Finding time to practise is harder than finding motivation.'",
                    "Use 'there is no point in + -ing' · 'it's worth + -ing' · 'it's a waste of time + -ing'.",
                    "Use 'have difficulty (in) + -ing': 'I had difficulty understanding the accent.'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): list three activities you enjoy or avoid (-ing) and two "
                "plans or decisions (to + verb). Mark one meaning-changing verb — stop, remember or "
                "try — to use in both patterns if you can.",
        'task': "Speak for one minute: 'What learning English has taught me about myself.' Use at least "
                "three gerunds and two infinitives. End with one decision you have made (to + verb).",
        'model': "Learning English has taught me to be patient with myself. I enjoy reading in "
                 "English now, and at first I tried translating every word — that only slowed me "
                 "down, so I stopped doing it and started guessing from context. I keep a short "
                 "vocabulary journal every evening because writing helps me notice patterns. I used "
                 "to avoid speaking because I feared mistakes, so I've decided to join an evening "
                 "class this winter and speak with real people.",
        'feedback': ["gerund and infinitive patterns accurate",
                     "at least one meaning-changing verb used correctly",
                     "sentences are connected, not listed",
                     "the final decision is clear"],
    },
    'review': {
        'points': ["Some verbs take -ing, some take 'to', some take both with meaning changes.",
                   "After any preposition, use -ing — including 'to' in look forward to, be used to.",
                   "Gerunds work as subjects: 'Practising daily helps.'"],
        'retrieval': ["Say two sentences with 'stop' (both meanings) and two with 'try' (both meanings).",
                      "Name five verbs + -ing and five verbs + to from memory."],
        'watch': ["'enjoy to read' → 'enjoy reading'.",
                  "'look forward to meet' → 'look forward to meeting'."],
        'selfcheck': ["I can choose the pattern automatically with common verbs.",
                      "I know the meaning-changing pairs."],
        'answers': {
            'A': ["helping", "answering", "to accept", "hearing", "smoking", "to open"],
            'B': ["I enjoy reading novels.", "I look forward to meeting you.",
                  "She suggested going early.",
                  "The room needs cleaning. / The room needs to be cleaned.",
                  "posting", "answers vary"],
        },
    },
}

L12 = {
    'n': 12, 'part_no': 6, 'part_title': 'Speak with Greater Precision',
    'title': 'Relative Clauses and Concise Descriptions',
    'goal': 'describe people, places and ideas precisely in one sentence',
    'intro': "Relative clauses let you build two ideas into one clean sentence — the mark of fluent speech.",
    'hook': [
        "Describe without naming: choose someone in the class, a famous person or a place — "
        "describe it so your partner can guess. Use 'who', 'which' or 'that' in every sentence.",
    ],
    'rules': [
        {'label': 'Rule 1 — Defining relative clauses (essential information)',
         'formula': ["who (people) · which (things) · that (both) · whose (possession) · where · when",
                     "No commas. Without the clause, the sentence changes meaning.",
                     "Object pronouns can be omitted: 'The book (that) I read…'"],
         'text': ["A defining clause tells us WHICH one. It is part of the meaning, so no commas."],
         'examples': ["The woman who called you is my manager.",
                      "The town where I grew up has changed a lot.",
                      "The man whose car was damaged is waiting outside."],
         'remember': ["In speech, drop the object 'that/who/which' when it is the object: "
                      "'The film we watched…' (not 'The film which we watched it…')."]},
        {'label': 'Rule 2 — Non-defining relative clauses (extra information)',
         'formula': [", who … ,   /   , which … ,   (commas — like a quiet aside)",
                     "Never use 'that' here. Never drop the pronoun."],
         'text': ["A non-defining clause adds information about something already identified. "
                  "It is spoken with a small pause."],
         'examples': ["My brother, who lives in Dubai, is visiting next week.",
                      "The project, which took six months, was finally approved."],
         'remember': ["With commas, the clause can comment on the whole sentence: "
                      "'She apologised publicly, which changed the mood.'"]},
        {'label': 'Rule 3 — Prepositions in relative clauses',
         'formula': ["… the clinic to which I go … (formal)",
                     "… the clinic which I go to … (normal)",
                     "… the clinic I go to … (speech)"],
         'text': ["In formal English the preposition moves before the pronoun; in speech it stays at the end."],
         'examples': ["The colleague with whom I worked has retired.  (formal)",
                      "The colleague I worked with has retired.  (natural)"],
         'remember': ["For people after prepositions, use 'whom' in formal English: 'the person to whom I spoke.'"]},
        {'label': 'Rule 4 — Reduced clauses: the concision tool',
         'formula': ["who is / who was + …  →  (drop 'who is'): 'The man (who is) standing there…'",
                     "which was + participle  →  'The results (which were) published today…'"],
         'text': ["Dropping 'who is/which was' makes descriptions tighter — very useful in speech and reports."],
         'examples': ["Anyone wishing to attend must register.  (= who wishes)",
                      "The documents attached to this email…  (= which are attached)"],
         'remember': ["Only drop 'who is/which was' — never drop a full verb: "
                      "'The man who called' cannot become 'The man called'."]},
    ],
    'differences': [
        {'title': 'defining vs non-defining',
         'rows': [
             ["My sister who lives in London is a doctor.  (I have several sisters)", "My sister, who lives in London, is a doctor.  (I have one sister)", "The commas change how much we learn: identification vs extra detail."],
             ["Students who pass the exam receive a certificate.", "My cousin, who passed the exam, received a certificate.", "No commas when the clause defines which ones."],
         ], 'headers': ['Defining (no commas)', 'Non-defining (commas)', 'Why']},
        {'title': 'that vs which vs who',
         'rows': [
             ["The book that I bought…", "The book which I bought…", "The man who helped me…", "that is common for things and people in speech; which/who after commas; 'that' never after commas."],
         ], 'headers': ['that (speech, things/people)', 'which (things)', 'who (people)', 'The rule']},
        {'title': 'whose vs of whom',
         'text': ["'The student whose essay won the prize…' is natural in speech; "
                  "'the student the essay of whom won…' is possible but clumsy. Prefer 'whose'."]},
    ],
    'practice_a': [
        "The girl __________ helped me was kind.  (who / which / whose)",
        "My phone, __________ I bought last year, has already broken.  (that / which)",
        "This is the café __________ we first met.  (where / which)",
        "The man __________ car was stolen is the manager.  (who / whose)",
        "The results __________ were announced today are surprising.  (reduced clause: leave a gap or use which)",
        "I read the article you recommended.  (insert the omitted pronoun — what is it?)",
    ],
    'practice_b': [
        "Combine: 'The teacher is excellent. She taught me last year.'  (use who)",
        "Combine with commas: 'My friend is a pilot. He travels constantly.'  (extra information)",
        "Correct: 'My mother, that lives in Kandahar, is visiting.'",
        "Correct: 'The book what I read was amazing.'",
        "Reduce: 'Students who are interested in the course should apply.'",
        "Describe your favourite place using one defining and one non-defining clause.",
    ],
    'pair': {
        'intro': "The guessing game. Describe a person, place or object from your life using only relative "
                 "clauses — never name it. Partner guesses, then swaps.",
        'task': ["Each person describes two items, using at least one defining and one non-defining clause.",
                 "After guessing, improve each other's sentences: make them more concise."],
        'output': "Two successful guesses per pair: each description contains one defining and one "
                  "non-defining clause, and both partners leave with one improved, more concise "
                  "sentence.",
        'criteria': ["relative pronouns chosen correctly (who/which/whose/where)",
                     "defining vs non-defining punctuation/meaning respected",
                     "descriptions are concise and clear",
                     "partner can guess the item"],
    },
    'advanced': {
        'base': ["Drill the four pronouns: who / which / whose / where — with people and places from your life.",
                 "Practise dropping object pronouns: 'The film we saw…' · 'The course I chose…'"],
        'upgrade': ["Use 'which' to comment on a whole clause: 'He apologised, which surprised everyone.'",
                    "Use cleft focus with 'what': 'What I need is time.' · 'What surprised me was the result.'",
                    "Use reduced clauses in formal speech: 'Anyone arriving late will be asked to wait.'"],
    },
    'realtalk': {
        'plan': "Planning (30 seconds): choose the person, then note three roles — who they are "
                "(defining), one extra detail with commas (non-defining), and one -ing description "
                "(reduced). Decide which clause identifies and which one comments.",
        'task': "Describe-and-explain talk (one minute): talk about a person who influenced you. Use two "
                "defining clauses, one non-defining clause, and one reduced clause. Do not write anything.",
        'model': "The person who influenced me most is my uncle, who taught physics for thirty years. "
                 "He is the man whose advice I still hear when I sit down to study: start with the "
                 "hardest task. The teacher who encouraged me at school lent me books written by "
                 "Afghan authors, and the colleague sitting beside me at my first job showed me how "
                 "to admit a mistake quickly. Anyone working with him learns the same thing — "
                 "preparation beats talent.",
        'feedback': ["relative clauses are accurate and natural",
                     "at least one non-defining clause with correct meaning",
                     "one concise reduced form",
                     "the person's influence is explained clearly"],
    },
    'review': {
        'points': ["Defining clauses identify (no commas); non-defining clauses add detail (commas).",
                   "Drop object pronouns in speech: 'The book I read…'.",
                   "Reduced clauses ('who is' dropped) make descriptions concise."],
        'retrieval': ["Say one defining and one non-defining clause about people near you.",
                      "Describe your city with two relative clauses and one reduced clause."],
        'watch': ["'the book what I read' → 'the book (that) I read'.",
                  "'My mother, that lives…' → 'My mother, who lives…'"],
        'selfcheck': ["I choose the right pronoun and punctuation automatically.",
                      "I can compress descriptions with reduced clauses."],
        'answers': {
            'A': ["who", "which", "where", "whose", "(that) were / which were — or simply 'announced today' with 'The results announced today…'", "that (or which)"],
            'B': ["The teacher who taught me last year is excellent.",
                  "My friend, who is a pilot, travels constantly.",
                  "My mother, who lives in Kandahar, is visiting.",
                  "The book (that) I read was amazing.",
                  "Students interested in the course should apply.", "answers vary"],
        },
    },
}

LESSONS_9_12 = [L9, L10, L11, L12]


def render_all(doc, keys_registry):
    for L in LESSONS_9_12:
        render_lesson(doc, L, keys_registry)

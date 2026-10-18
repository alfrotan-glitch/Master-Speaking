# -*- coding: utf-8 -*-
"""Lessons 9-12 — Part Five: Describe and Explain; Part Six: Speak with Greater Precision."""
from lesson_template import render_lesson

L9 = {
    'n': 9, 'part_no': 5, 'part_title': 'Describe and Explain',
    'title': 'Passive Voice in Natural English',
    'goal': 'choose between active and passive for the right focus',
    'intro': [
        "Compare these two sentences: 'Someone stole my bicycle outside the library yesterday' and 'My bicycle was "
        "stolen outside the library yesterday.' Both report the exact same crime. Yet the first sentence starts with "
        "an unknown stranger ('Someone'), while the second puts the spotlight immediately on what you actually care "
        "about: your bicycle.",
        "The passive voice is not a complicated academic decoration. It is how English speakers control the camera "
        "angle of a sentence — placing the person, object, or result at the front when the doer is unknown, obvious, "
        "or less important than what happened."
    ],
    'hook': [
        "Read these two pairs of sentences aloud with a partner and decide which version sounds more natural in each context:",
        "•  Context 1 (a news broadcast):   'Workers opened the new city hospital this morning.'   vs.   'The new city hospital was opened this morning.'",
        "•  Context 2 (a personal story):   'My tea was spilled by me on my laptop.'   vs.   'I spilled my tea on my laptop.'",
        "Why does the passive sound right in Context 1, while the active sounds much better in Context 2? Tell your "
        "partner about one recent change in your neighbourhood or workplace and one small accident of your own.",
    ],
    'rules': [
        {'label': 'Rule 1 — Building the passive: the tense lives in "be"',
         'text': [
             "To turn an active sentence into a passive one, move the object to the front so it becomes the new "
             "subject, and use 'be + past participle'.",
             "The main verb stays in its past participle form (done, built, written, repaired) across every tense. "
             "Whenever you change the time or add a modal, you simply change the form of 'be' (is, was, will be, has been, must be)."
         ],
         'formula': [
             "Passive core:  Subject (receiver of action) + form of be + past participle (+ by + agent when needed)",
             "Across tenses:  is/are done (present)  ·  was/were done (past)  ·  is/are being done (continuous)  ·  has/have been done (perfect)  ·  will/must/should be done (modal)"
         ],
         'examples': [
             "The clinic rooms are cleaned every evening after the last patient leaves.  (present simple passive)",
             "The stone bridge was built in 2019.  (past simple passive)",
             "The scholarship results will be announced tomorrow afternoon.  (future passive)",
             "The novel was written by Atiq Rahimi.  (the 'by' phrase is included because the author's identity is the key point)"
         ],
         'remember': [
             "Include 'by + person/agent' only when the identity of the doer adds important information ('The policy was signed by the minister'). "
             "Never add vague agents like 'by someone' or 'by people'."
         ]},
        {'label': 'Rule 2 — When to choose the passive (and when to stay active)',
         'text': [
             "News reports, scientific descriptions, workplace updates, and polite professional announcements often "
             "use the passive to focus on events, processes, or results. The agent may be left out when it is unknown "
             "or unimportant, or included in a by-phrase when it matters.",
             "When you are telling a lively personal story about your own actions, however, stay in the active voice: "
             "'I lost my keys' is natural and direct, whereas 'My keys were lost by me' sounds clumsy and evasive."
         ],
         'formula': [
             "Choose the passive when:  1. the result or receiver matters most   ·   2. the doer is unknown, obvious, or general   ·   3. you want an objective, diplomatic tone (without pointing fingers)"
         ],
         'examples': [
             "My wallet was stolen on the crowded bus yesterday.  (doer is unknown)",
             "Two calculation errors were found in the budget draft.  (diplomatic — focuses on the errors rather than blaming a colleague)",
             "Coffee beans are roasted for twelve minutes before being ground.  (describing a process)"
         ],
         'remember': [
             "In everyday stories about yourself, prefer the active voice: say 'I dropped my phone' (not 'My phone was dropped by me')."
         ]},
        {'label': 'Rule 3 — Objective reporting structures: It is said that … / He is said to …',
         'text': [
             "When journalists, researchers, or professionals report widely held beliefs or unconfirmed claims without "
             "saying 'People say…', they use two passive reporting frames with verbs like say, believe, think, expect, "
             "report, and consider."
         ],
         'formula': [
             "Impersonal frame:  It is said / believed / reported / expected that + clause",
             "Subject-focused frame:  Subject + is/are said / believed / thought + to + base verb (or to have + past participle for an earlier past event)"
         ],
         'examples': [
             "It is widely believed that regular reading strengthens spoken vocabulary.",
             "She is said to speak five languages fluently.  (= People say that she speaks…)",
             "The delegation is reported to have arrived in the capital last night.  ('to have arrived' points to an earlier past action)"
         ],
         'remember': [
             "Notice the two infinitive options: use 'to + base verb' for something true now ('He is thought to live in Herat') "
             "and 'to have + past participle' for an earlier event ('He is thought to have left yesterday')."
         ]},
    ],
    'differences': [
        {'title': 'Active vs passive — shifting the spotlight and the tone',
         'text': [
             "Compare how the focus and social effect change when we move from the active column to the passive column:"
         ],
         'rows': [
             ["Someone damaged the main gate last night.", "The main gate was damaged last night.", "The passive omits the unknown 'Someone' and puts the damaged gate first. Add a by-phrase only if the agent matters."],
             ["You did not lock the supply room.", "The supply room was left unlocked.", "The active accuses one person directly; the passive focuses calmly on the issue that needs fixing."],
             ["The board approved the new timetable.", "The new timetable was approved.", "In an announcement to students, what matters is the new timetable, not the internal committee."],
         ], 'headers': ['Active (focus on the doer)', 'Passive (focus on the event/result)', 'Why a speaker chooses it']},
        {'title': 'The informal "get" passive vs the standard "be" passive',
         'text': [
             "In everyday conversation, speakers often replace 'be' with 'get' for sudden, unexpected, or emotional "
             "events: 'He got promoted last month', 'Our car got stuck in the snow', 'They got married in the spring.'",
             "In formal reports, presentations, and academic English, prefer the standard 'be' passive: "
             "'He was promoted to senior manager last month.'"
         ]},
        {'title': 'Verbs that look passive in meaning but stay active in form',
         'text': [
             "A few everyday verbs describe how an object behaves without needing a passive form: "
             "'Her new book sold out in three days', 'The stain washed out easily', 'The clinic door opened at eight.' "
             "These describe what happened naturally rather than an action performed on the object."
         ]},
    ],
    'practice_a': [
        "The stone bridge across the valley __________ (build) in 2019.",
        "The scholarship winners __________ (announce) tomorrow afternoon at two.",
        "This lecture hall __________ (clean) every morning before classes begin.",
        "My cousin's wallet __________ (steal) on the crowded bus yesterday.",
        "A new attendance policy __________ (just / introduce) by the department.",
        "All application forms must __________ (submit) before midday on Friday.",
    ],
    'practice_b': [
        "Rewrite in the passive so the bicycle comes first: 'Someone has stolen my bicycle.'",
        "Rewrite in the active so the doer comes first: 'The final decision was made by the board.'",
        "Rewrite in two formal ways (using 'It is said…' and 'He is said…'): 'People say that he is the strongest candidate.'",
        "Correct the irregular participle mistake: 'The old courthouse was builted in 1990.'",
        "Make this sentence sound natural in a personal story: 'My phone was lost by me on the way home.'",
        "Report this update as a formal passive announcement: 'Engineers will close the main tunnel tomorrow for maintenance.'",
    ],
    'pair': {
        'intro': "Play 'The Morning Newsroom'. Partner A is a local radio reporter delivering three short news updates "
                 "about recent events in your city, campus, or workplace using natural passives. Partner B is the news "
                 "editor asking follow-up questions ('Do we know who did it?', 'What will happen next?'). Then swap roles.",
        'task': [
            "Choose three news items from: a road or building project · a new rule or policy · a community event · a sports or academic achievement · a weather disruption.",
            "In your report, use at least two passive tenses (such as 'was opened', 'has been postponed', 'will be held') and one formal reporting frame ('It is reported that…' or '…is expected to…')."
        ],
        'model': [
            "A: Good morning. The new pedestrian bridge near the university was opened at eight o'clock today, and traffic along the main road has already been reduced.",
            "B: Do we know when the second phase of the project will be completed?",
            "A: It is expected that the cycle lane will be finished before the end of next month."
        ],
        'output': "Three news items per reporter in report-style speech, with two accurate passives "
                  "and one reporting structure, surviving the editor's 'who did it?' question.",
        'criteria': [
            "forms passives accurately across past, present perfect, and future/modal tenses",
            "mentions the agent with 'by' only when the doer's identity genuinely matters",
            "uses at least one formal reporting passive ('It is said/expected that…' or 'is said to…')",
            "answers the editor's follow-up questions clearly, switching between active and passive as needed"
        ],
    },
    'advanced': {
        'intro': "Choosing smoothly between active and passive lets you link sentences together without jumping "
                 "awkwardly from subject to subject.",
        'base': [
            "Practise shifting one everyday object through four passive tenses aloud: 'The report is checked weekly' · 'was checked yesterday' · 'has already been checked' · 'will be checked tomorrow'.",
            "Pair the two formal reporting patterns until you can switch between them effortlessly: 'It is believed that the method works' ↔ 'The method is believed to work'."
        ],
        'upgrade': [
            "Use the passive to keep the same topic at the front of two connected sentences: 'The solar panels were installed in May, and since then electricity costs have been cut by half.'",
            "Use cautious reporting verbs ('It is claimed / alleged / assumed that…') when discussing unverified news or competing viewpoints.",
            "Open a formal description with a compressed passive participle clause: 'Founded in 1971, the institute now trains over a thousand specialists a year.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to pick three real events from your city, school, or workplace this month — two where "
                "the result or public impact matters most (passive), and one where you want to share your own personal "
                "opinion (active). Note only the three topics and the tense of 'be' for each.",
        'task': "Ninety-second community briefing: Report three developments that have happened (or will happen soon) "
                "in your community, campus, or workplace. Use the passive voice for the events, include one reporting "
                "structure ('It is said / expected that…'), and finish with your own active-voice comment on what "
                "should happen next.",
        'model': "Three important updates have happened around our campus this week. First, a new pedestrian footbridge "
                 "was opened near the east gate on Monday, so morning traffic has been diverted away from the main "
                 "walkway. Second, two study rooms on the third floor have been fitted with new lighting and quiet "
                 "desks. Finally, it is expected that the library hours will be extended during the exam period next "
                 "month. In my view, the administration should publish the new evening timetable as soon as possible so "
                 "students can plan their transport home.",
        'feedback': [
            "uses at least three passive verb forms accurately across different tenses",
            "maintains a clear, objective reporting tone for the announcements",
            "includes agents with 'by' only where the doer matters",
            "shifts naturally into the active voice for the speaker's closing recommendation"
        ],
    },
    'review': {
        'points': [
            "Form the passive with 'be + past participle'; the tense or modal always lives in 'be' (was built, has been built, must be built).",
            "Choose the passive when the result or receiver matters most, when the doer is unknown or obvious, or when you want an objective, diplomatic tone.",
            "Use 'It is said/believed that…' or 'Subject + is said/believed to…' to report general views formally."
        ],
        'retrieval': [
            "Look around the room and describe three objects using passive sentences in three different tenses.",
            "Report one widely held belief about health or education in both patterns: 'It is believed that…' and '…is believed to…'."
        ],
        'watch': [
            "'The house was builted in 1990.' → 'The house was built in 1990.' ('Built' is both the past tense and the past participle.)",
            "'My keys were lost by me.' → 'I lost my keys.' (Use the active voice for your own everyday actions.)"
        ],
        'selfcheck': [
            "I can build passive sentences accurately in present, past, present perfect, and modal forms.",
            "I know when to choose the passive for focus and when to keep my sentences active."
        ],
        'answers': {
            'A': ["was built", "will be announced", "is cleaned", "was stolen",
                  "has just been introduced", "be submitted"],
            'B': ["My bicycle has been stolen.",
                  "The board made the final decision.",
                  "It is said that he is the strongest candidate. / He is said to be the strongest candidate.",
                  "The old courthouse was built in 1990.",
                  "I lost my phone on the way home.",
                  "The main tunnel will be closed tomorrow for maintenance."],
        },
    },
}

L10 = {
    'n': 10, 'part_no': 5, 'part_title': 'Describe and Explain',
    'title': 'Causative Structures',
    'goal': 'talk about services, arrangements, influence and responsibility naturally',
    'intro': [
        "If a friend tells you, 'I cut my hair yesterday,' you picture them standing in front of the bathroom mirror "
        "with a pair of scissors. What they almost certainly meant to say is, 'I had my hair cut yesterday' — meaning "
        "they arranged for a barber or hairdresser to do the work.",
        "Causative structures let you express two everyday realities with precision: arranging for a professional "
        "service ('have/get something done'), and describing how people influence, allow, or persuade one another to "
        "act ('make, let, have, and get')."
    ],
    'hook': [
        "Compare these two sentences with a partner:",
        "•  'I painted my living room last weekend.'   vs.   'I had my living room painted last weekend.'",
        "In which sentence did the speaker hold the paintbrush and get paint on their sleeves? Now talk with your "
        "partner about everyday tasks in your city (car repairs, tailoring, computer problems, home maintenance, "
        "cooking for a celebration): which ones do you do with your own hands, and which ones do you have done by a specialist?",
    ],
    'rules': [
        {'label': 'Rule 1 — Arranging a service: have / get + object + past participle',
         'text': [
             "When you pay, ask, or arrange for a professional or service provider to do a job for you, put 'have' "
             "(or the slightly more conversational 'get') before the object, followed by the past participle: "
             "'I had my watch repaired.'",
             "Word order is crucial here: the object comes between 'have/get' and the participle ('had my watch repaired'), "
             "because putting the participle right after 'had' ('I had repaired my watch') turns the sentence into "
             "the ordinary past perfect, meaning you repaired it yourself!"
         ],
         'formula': [
             "Service causative:  Subject + have / get (in any tense) + object + past participle",
             "Questions & negatives:  Where do you get your car serviced?  ·  I haven't had the documents translated yet."
         ],
         'examples': [
             "I had my suit altered by a tailor before my brother's wedding.",
             "She is getting her laptop keyboard replaced this afternoon.",
             "We need to have the heating system checked before winter sets in."
         ],
         'remember': [
             "This exact same structure is also used when something unpleasant happens to your belongings outside your control: "
             "'He had his passport stolen at the station' (obviously he did not arrange the theft — he was affected by it)."
         ]},
        {'label': 'Rule 2 — Influencing people: make, let, have, and get',
         'text': [
             "When you talk about how one person causes or allows another person to do something, English uses four "
             "key verbs — and each one carries a distinct social relationship.",
             "'Make' expresses compulsion or an unavoidable reaction; 'let' expresses permission; 'have' expresses "
             "routine professional instruction or delegation; and 'get' expresses persuading someone or overcoming difficulty. "
             "Notice the grammar: make, let, and have take the bare infinitive (without 'to'), whereas 'get' requires 'to + verb'."
         ],
         'formula': [
             "Compulsion / reaction:  make + person + base verb (no 'to')   →   The coach made us run two extra laps.",
             "Permission:  let + person + base verb (no 'to')   →   My parents let me borrow the car.",
             "Professional delegation:  have + person + base verb (no 'to')   →   I'll have the receptionist call you.",
             "Persuasion / effort:  get + person + to + base verb (with 'to'!)   →   I finally got my brother to help me move."
         ],
         'examples': [
             "The sudden applause made the speaker smile.",
             "Our instructor let us work in pairs for the revision task.",
             "The clinic director had the technician test the samples twice.",
             "How did you get the landlord to lower the rent?"
         ],
         'remember': [
             "Out of make, let, have, and get, only 'get' takes 'to' in the active voice: 'get someone to do something' "
             "(never 'make someone to do' or 'let someone to do')."
         ]},
        {'label': 'Rule 3 — Real-world service conversations',
         'text': [
             "When you walk into a repair shop, clinic, print shop, or tailor's workshop, combining causative patterns "
             "with polite modal questions gives you natural, idiomatic service English."
         ],
         'formula': [
             "Explaining the job:  I need to have / get my … repaired / checked / altered.",
             "Checking timing & cost:  How soon can I have it done?  ·  How much do you charge to have a screen replaced?"
         ],
         'examples': [
             "I get my eyes tested every two years at the optician's on Main Street.",
             "I'm having the brakes checked tomorrow morning — could you give me a lift to work?"
         ],
         'remember': [
             "When 'make' is turned into the passive voice, the 'to' reappears: 'The teacher made us wait' → 'We were made to wait.' "
             "For 'let', we switch to 'be allowed to' in the passive: 'We were allowed to leave early.'"
         ]},
    ],
    'differences': [
        {'title': 'Doing it yourself vs arranging it vs suffering an accident',
         'text': [
             "Compare what your listener pictures in these three sentences:"
         ],
         'rows': [
             ["I washed my car on Saturday.", "I had my car washed on Saturday.", "I tightened the garden hose and washed it myself vs I took it to the car wash and paid an attendant to wash it."],
             ["I had my watch repaired.", "I had my watch broken during the match.", "Same grammar, opposite experience: the first is a service I arranged; the second is an accident that happened to my watch."],
         ], 'headers': ['Sentence A', 'Sentence B', 'What actually happened']},
        {'title': 'Four shades of interpersonal influence: make vs let vs have vs get',
         'rows': [
             ["She made me rewrite the report.", "She let me rewrite the report.", "She had me rewrite the report.", "She got me to rewrite the report.", "1. Make = she forced me (I had no choice).  2. Let = I wanted to rewrite it and she gave permission.  3. Have = she assigned the task as my manager.  4. Get = she persuaded or convinced me to do it."],
         ], 'headers': ['make + verb (force)', 'let + verb (allow)', 'have + verb (assign)', 'get + to + verb (persuade)', 'How the relationship feels']},
    ],
    'practice_a': [
        "I need to have my winter coat __________ (alter) before the cold weather arrives.",
        "Where do you usually get your hair __________ (cut)?",
        "The loud construction noise outside made me __________ (lose) my concentration.",
        "The librarian let us __________ (use) the quiet conference room for our rehearsal.",
        "I'm having my eyes __________ (test) at the clinic on Thursday afternoon.",
        "After a long talk, she finally got her teenage son __________ (turn) off his computer before midnight.",
    ],
    'practice_b': [
        "Rewrite using have + object + past participle: 'I paid a mechanic to service my car last week.'",
        "Rewrite using get (to show persuasion): 'After a long discussion, my friend agreed to drive us to the airport.'",
        "Correct the mistake: 'I will get my laptop to repair tomorrow.'",
        "Correct the mistake: 'The security guard made us to wait outside in the rain.'",
        "Write one true sentence about something you had done recently (a service you arranged or a mishap that happened to you).",
        "Write a polite question you would ask at a repair shop when your phone screen is cracked (using a causative form).",
    ],
    'pair': {
        'intro': "Role-play 'The Busy Repair & Service Counter'. Partner A runs a multi-service centre (handling "
                 "electronics, tailoring, printing, or car repairs); Partner B is a customer who has had a chaotic "
                 "week and needs three different things sorted out before a big event on Friday.",
        'task': [
            "Customer (Partner B): Explain at least three things you need to have done ('I need to have my…', 'I'm hoping to get my…'), and mention why you are in a hurry using make, let, or get.",
            "Service Manager (Partner A): Explain what can be done on site, what you will have a technician look at, how long it will take, and what it will cost. Negotiate until you agree on a plan, then swap roles."
        ],
        'model': [
            "Customer: Good afternoon — I'm giving a conference presentation on Friday, and I need to get my laptop screen replaced and have thirty handouts bound.",
            "Manager: We can have the handouts bound for you within an hour. As for the laptop, I'll have our senior technician check whether we have that screen in stock. If we do, we can get it fixed by tomorrow evening."
        ],
        'output': "One completed service negotiation per pair: at least three things that need doing, "
                  "a price and a time agreed, and one make/let/get sentence used accurately.",
        'criteria': [
            "uses 'have/get + object + past participle' accurately for all service requests",
            "keeps the object before the past participle ('get my screen replaced')",
            "uses make, let, have, or get (+ person) with the right verb pattern ('to' only after get)",
            "agrees clearly on timing and cost in natural spoken English"
        ],
    },
    'advanced': {
        'intro': "Beyond repair shops and salons, causative patterns are essential in workplace delegation and "
                 "expressive storytelling.",
        'base': [
            "Say four true sentences about people in your life using make, let, have, and get — paying special attention to the bare verb after make/let/have and 'to + verb' after get.",
            "Practise everyday service chunks aloud until the word order is automatic: 'I need to have my passport renewed' · 'When can I get it done?'"
        ],
        'upgrade': [
            "Use 'have + person + base verb' for smooth, professional delegation at work: 'I'll have the finance team send you the updated figures this afternoon.'",
            "Use 'have + person + verb-ing' to describe how a speaker, book, or event affected an audience: 'His story had the whole room laughing within two minutes' · 'That documentary had me thinking for days.'",
            "Combine 'get round to + -ing' with a causative when talking about delayed chores: 'I finally got round to having the kitchen roof repaired.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to plan a one-minute story about a chaotic day (real or lightly invented). Jot down "
                "three keywords: one service you arranged ('had/got something done'), one unexpected mishap ('had "
                "something happen'), and one moment where someone made, let, or got someone else to help.",
        'task': "One-minute story challenge: Tell your partner about 'A day when plans went sideways — and how we "
                "sorted it out.' Include at least two service/mishap causatives and at least two interpersonal "
                "causatives (make, let, have, get) without reading from notes.",
        'model': "Last Thursday started badly from the moment I woke up. I had had my car serviced the evening before, "
                 "yet when I turned the key it still wouldn't start, so I got my neighbour to check the battery before "
                 "he left for work. Then, on the bus into town, I almost had my bag taken in the crowd. When I arrived "
                 "twenty minutes late, my manager made me reschedule my morning client call, but she kindly let me use "
                 "her quiet office to prepare for the afternoon presentation. By five o'clock, I had the garage tow "
                 "the car in and replace the starter motor — and the whole chaotic day had us laughing over dinner.",
        'feedback': [
            "uses 'have/get + object + past participle' accurately with the object in the middle",
            "distinguishes clearly between arranged services and unplanned mishaps",
            "uses make, let, have, and get (+ person) with accurate verb patterns",
            "connects the events into an engaging, easy-to-follow spoken story"
        ],
    },
    'review': {
        'points': [
            "Use 'have/get + object + past participle' when you arrange for someone else to do a job (or when an unpleasant event affects your belongings).",
            "Use 'make + person + base verb' (force), 'let + person + base verb' (permission), 'have + person + base verb' (instruction), and 'get + person + to + base verb' (persuasion).",
            "In the passive voice, 'make' regains 'to': 'We were made to wait for an hour.'"
        ],
        'retrieval': [
            "Name three things you would like to have done or repaired this month using full causative sentences.",
            "Describe one teacher or family member who made you work hard and one who let you make your own choices."
        ],
        'watch': [
            "'I will get my car to repair tomorrow.' → 'I will get my car repaired tomorrow.' (Use the past participle for a service done to an object.)",
            "'She made me to wait outside.' → 'She made me wait outside.' (Never put 'to' after active 'make' or 'let'.)"
        ],
        'selfcheck': [
            "I can talk about services and repairs naturally using 'have/get something done'.",
            "I can use make, let, have, and get accurately when talking about other people's actions."
        ],
        'answers': {
            'A': ["altered", "cut", "lose", "use", "tested", "to turn"],
            'B': ["I had my car serviced last week.",
                  "After a long discussion, I got my friend to drive us to the airport.",
                  "I will get my laptop repaired tomorrow.",
                  "The security guard made us wait outside in the rain.",
                  "answers vary (e.g. 'I had my watch battery replaced on Monday.')",
                  "Could I have my phone screen replaced today? / How much would it cost to get my phone screen replaced?"],
        },
    },
}

L11 = {
    'n': 11, 'part_no': 6, 'part_title': 'Speak with Greater Precision',
    'title': 'Gerunds and Infinitives',
    'goal': 'choose the right verb pattern for your meaning',
    'intro': [
        "Listen to the difference between these two five-word sentences: 'He stopped smoking last year' and 'He "
        "stopped to smoke last year.' In the first sentence, a man gave up a habit for good. In the second, he paused "
        "in the middle of a walk in order to light a cigarette.",
        "When you put two verbs together in English, the second verb takes either the gerund (-ing) or the infinitive "
        "(to + base verb). Once you understand the logic behind these two patterns — and the small group of verbs "
        "where choosing '-ing' or 'to' changes the entire meaning — your sentences sound effortless and precise."
    ],
    'hook': [
        "Read these four sentence starters aloud and finish each one instinctively with the first true idea that comes to mind:",
        "•  On a quiet evening, I really enjoy…",
        "•  Before the end of this year, I hope…",
        "•  When I have an important deadline, I try to avoid…",
        "•  Next month, I've decided…",
        "Compare your sentences with a partner. Notice that your ear probably chose '-ing' after 'enjoy' and 'avoid', "
        "and 'to + verb' after 'hope' and 'decided' without even stopping to think!",
    ],
    'rules': [
        {'label': 'Rule 1 — Verbs followed by the gerund (-ing): ongoing experiences and real activities',
         'text': [
             "Why do verbs like enjoy, avoid, mind, finish, keep, practise, suggest, and miss take the -ing form? "
             "Because these verbs usually look at an activity as a real, ongoing experience or a familiar action "
             "that already exists.",
             "When you say 'I enjoy swimming' or 'He avoided answering the question', treat the verb + -ing as a "
             "single rhythmic chunk."
         ],
         'formula': [
             "Verb + verb-ing:  enjoy · avoid · consider · delay · finish · keep · mind · miss · practise · risk · suggest · give up · feel like · can't help + verb-ing"
         ],
         'examples': [
             "I enjoy reading for half an hour before going to sleep.",
             "The speaker avoided giving a direct answer to the journalist's question.",
             "She suggested meeting fifteen minutes earlier to check the slides.",
             "Would you mind opening the window slightly?"
         ],
         'remember': [
             "When a verb follows mind directly, use -ing: 'Do you mind waiting?' Other patterns exist, such as 'Would you mind if I opened the window?'",
             "With 'suggest' and 'recommend', never insert 'me to': say 'She suggested going early' or 'She suggested that we go early' (never 'She suggested me to go')."
         ]},
        {'label': 'Rule 2 — Verbs followed by the infinitive (to + base verb): looking forward',
         'text': [
             "Now look at verbs that take 'to + base verb': decide, hope, plan, promise, agree, offer, refuse, manage, "
             "want, expect, and would like. Notice what almost all of them have in common: they point forward like "
             "an arrow toward a future intention, goal, or decision that has not happened yet.",
             "When you decide *to leave*, promise *to call*, or hope *to pass*, the decision or hope comes first, "
             "and the action points ahead into the future."
         ],
         'formula': [
             "Verb + to + base verb:  agree ·choose · decide · expect · hope · intend · learn · manage · offer · plan · promise · refuse · seem · tend · want · would like + to + verb"
         ],
         'examples': [
             "After working at the bank for three years, she decided to study law.",
             "Despite the flat tyre, we managed to reach the examination hall on time.",
             "He promised to send the revised contract before five o'clock.",
             "I'd like to ask one follow-up question about your proposal."
         ],
         'remember': [
             "To make an infinitive negative, place 'not' immediately before 'to': 'We decided not to travel during the storm' "
             "and 'She promised not to be late.'"
         ]},
        {'label': 'Rule 3 — Verbs where -ing vs to changes the meaning',
         'text': [
             "With a handful of common verbs — remember, forget, regret, stop, try, and mean — both patterns are "
             "grammatical, but they tell two different stories.",
             "Use the timeline test: '-ing' looks back at an earlier action (or an ongoing activity/experiment), "
             "while 'to + verb' looks forward to a subsequent duty, purpose, or difficult attempt."
         ],
         'formula': [
             "remember / forget / regret + verb-ing  →  looking back at an action that already happened",
             "remember / forget / regret + to + verb  →  looking forward to a duty or action that comes next",
             "stop + verb-ing  →  quit the activity   ·   stop + to + verb  →  pause what you are doing in order to do something else",
             "try + verb-ing  →  test an easy method/experiment   ·   try + to + verb  →  make an effort at something difficult"
         ],
         'examples': [
             "I clearly remember locking the front door this morning.  (I locked it first; I recall the memory now)",
             "Please remember to lock the front door when you leave.  (remember first, then lock the door)",
             "He stopped buying bottled water and bought a reusable flask.  (he quit the habit)",
             "On the drive to Herat, we stopped to buy fresh fruit by the roadside.  (we paused our drive in order to buy fruit)",
             "If the room is too warm, try opening the balcony door.  (test it as a simple experiment)   vs.   I tried to open the window, but the latch was painted shut.  (I made an effort, but failed)"
         ],
         'remember': [
             "Also compare 'mean + to + verb' (intend: 'I didn't mean to interrupt you') with 'mean + verb-ing' "
             "(involve as a necessary result: 'Taking the early flight means waking up at four in the morning')."
         ]},
        {'label': 'Rule 4 — Gerunds as sentence subjects and after prepositions',
         'text': [
             "Whenever you want to use an action as the subject of a sentence ('Swimming is good exercise') or place "
             "a verb immediately after a preposition (in, at, of, for, about, without, instead of, before, after), "
             "English always chooses the -ing form.",
             "Watch out for phrases where 'to' is actually a preposition pointing to a noun, such as 'look forward to', "
             "'be used to', and 'object to' — because 'to' is a preposition there, any verb that follows must end in -ing!"
         ],
         'formula': [
             "Subject gerund:  Verb-ing + singular verb …   →   Learning a language takes daily patience.",
             "Preposition + verb-ing:  interested in · good at · instead of · without · before/after + verb-ing",
             "Phrases where 'to' is a preposition:  look forward to · be/get used to · object to + verb-ing"
         ],
         'examples': [
             "Practising aloud for ten minutes a day builds more fluency than silent reading.",
             "She solved the problem without asking anyone for help.",
             "I really look forward to meeting your colleagues next week.",
             "It took me a month to get used to waking up at five."
         ],
         'remember': [
             "Test whether 'to' is a preposition by putting a noun after it: since we say 'I look forward to the holiday' (a noun), "
             "we must also say 'I look forward to seeing you' (a gerund, which acts like a noun)."
         ]},
    ],
    'differences': [
        {'title': 'Meaning-changing pairs side by side',
         'text': [
             "Say each pair aloud and picture the exact sequence of actions in your mind:"
         ],
         'rows': [
             ["I stopped checking my phone during study hours.", "I stopped to check my phone on the way to the library.", "Left (-ing): I gave up the habit of checking my phone.  Right (to): I paused my walk in order to look at my phone."],
             ["I remembered calling my uncle on his birthday.", "I remembered to call my uncle on his birthday.", "Left (-ing): I have the memory of the phone call we had.  Right (to): I didn't forget my duty — I remembered first and then dialled his number."],
             ["Have you tried restarting the router?", "I tried to fix the router, but it's still offline.", "Left (-ing): try it as a simple method to see if it helps.  Right (to): I made a difficult attempt."],
         ], 'headers': ['Verb + -ing', 'Verb + to + base verb', 'How the story changes']},
        {'title': 'Passive meaning with "need + -ing" vs "need + to be + participle"',
         'text': [
             "When a person has an obligation, we use 'need + to + verb': 'I need to charge my phone.'",
             "When an object requires a service, everyday spoken English often uses 'need + verb-ing' with a passive meaning: "
             "'My phone battery needs charging' (= needs to be charged) · 'These windows need cleaning' (= need to be cleaned)."
         ]},
    ],
    'practice_a': [
        "Would you mind __________ (help) me carry these boxes up to the second floor?",
        "During the interview, she carefully avoided __________ (criticise) her former employer.",
        "After comparing both universities, we decided __________ (accept) the offer in Kabul.",
        "I really look forward to __________ (hear) your thoughts on the new proposal.",
        "My uncle stopped __________ (smoke) five years ago, and his health improved rapidly.",
        "She tried __________ (open) the jammed locker door, but the key wouldn't turn.  (a difficult attempt)",
    ],
    'practice_b': [
        "Correct the mistake: 'I really enjoy to read historical biographies in the evening.'",
        "Correct the mistake: 'We look forward to meet your team on Monday.'",
        "Correct the mistake: 'My colleague suggested me to leave early before the snow started.'",
        "Rewrite in two natural ways using need: 'Someone must clean this classroom before tomorrow.'  (The classroom needs…)",
        "Choose the right form and explain why: 'I clearly remember (posting / to post) the package on Tuesday — I still have the receipt in my pocket.'",
        "Write one true sentence about your own study habits starting with 'Instead of + verb-ing…'.",
    ],
    'pair': {
        'intro': "Conduct a lively habits-and-decisions conversation with your partner. Adapt the questions below, "
                 "listen closely to every answer, and ask at least two follow-up questions before swapping roles.",
        'task': [
            "Ask your partner: (1) What is one activity you genuinely enjoy doing when you have a free afternoon? (2) What is one habit you have stopped doing — or are trying to avoid doing — this year? (3) What is one important goal you have decided or promised yourself to achieve over the next twelve months? (4) What is something you are really looking forward to doing soon?",
            "In your answers, use at least four different gerund/infinitive patterns and include at least one meaning-changing verb (remember, stop, or try)."
        ],
        'model': [
            "A: What is one habit you've stopped doing this year?",
            "B: I've stopped estudiar with my phone on the desk. At first I tried turning it face down, but I still kept checking it — so now I leave it in another room.",
            "A: Did it take long to get used to working without it?"
        ],
        'output': "A five-question interview per role: each person answers with at least four "
                  "different gerund/infinitive patterns and asks two follow-up questions.",
        'criteria': [
            "uses -ing and to-infinitive patterns accurately after common verbs",
            "uses '-ing' accurately after prepositions (including 'look forward to' and 'get used to')",
            "uses at least one meaning-changing verb (stop, remember, try) in the right pattern",
            "asks natural follow-up questions that keep the dialogue flowing"
        ],
    },
    'advanced': {
        'intro': "Fluent speakers use gerund phrases to open sentences cleanly and use idiomatic expressions of "
                 "worth, difficulty, and purpose to evaluate choices.",
        'base': [
            "Practise verb patterns as complete spoken chunks rather than isolated rules: 'I enjoy reading…', 'She suggested meeting…', 'We decided to wait…', 'I look forward to seeing…'.",
            "Say two contrasting sentences aloud for 'stop', 'remember', and 'try' using real moments from your own week."
        ],
        'upgrade': [
            "Open formal or reflective sentences with a multi-word gerund subject: 'Finding twenty quiet minutes every morning is easier than finding two free hours at the weekend.'",
            "Use evaluative -ing frames in discussions: 'It's well worth visiting…' · 'There's no point in worrying about…' · 'It's a waste of time arguing over…'",
            "Use 'have difficulty / trouble + verb-ing' (without a preposition): 'At first I had difficulty understanding rapid announcements at the airport.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to note five keywords: two habits you enjoy or keep doing (-ing), one unhelpful "
                "habit you stopped or avoid doing (-ing), one method you tried when learning a skill (try + -ing / to), "
                "and one firm decision you have made for the months ahead (decide / plan + to).",
        'task': "One-minute personal reflection: 'What learning a difficult skill has taught me about myself.' "
                "Use at least three gerund patterns (including one after a preposition or as a subject) and at least "
                "two infinitive patterns, ending with a clear decision you have made for the future.",
        'model': "Learning English as an adult has taught me to be much more patient with myself. When I first started, "
                 "I tried translating every single word in my head before speaking, which only made me hesitate. "
                 "Eventually I stopped doing that and practised listening for whole phrases instead. Nowadays I really "
                 "enjoy reading short articles aloud in the morning, and I keep a small notebook for expressions worth "
                 "remembering. I used to avoid speaking in front of larger groups, but this term I've decided to join "
                 "our department's weekly discussion circle, and I look forward to testing my voice there.",
        'feedback': [
            "uses both gerund (-ing) and infinitive (to + verb) patterns accurately",
            "uses at least one meaning-changing verb (tried, stopped, remembered) with the intended meaning",
            "includes at least one preposition + -ing or gerund subject naturally",
            "closes with a clear forward-looking decision using 'to + base verb'"
        ],
    },
    'review': {
        'points': [
            "Verbs of ongoing experience and avoidance (enjoy, avoid, mind, suggest, keep, finish) take '-ing'; verbs of future intention and decision (decide, hope, plan, promise, manage) take 'to + verb'.",
            "With remember, forget, stop, and try, '-ing' points to an earlier or ongoing action/experiment, while 'to + verb' points to a subsequent purpose or attempt.",
            "After every preposition — including 'to' in 'look forward to' and 'be/get used to' — always use '-ing'."
        ],
        'retrieval': [
            "Say two contrasting sentences with 'stop' (quit vs pause for a purpose) and two with 'try' (experiment vs difficult effort).",
            "Finish these three phrases aloud with actions: 'I suggested…', 'I managed…', 'I look forward to…'."
        ],
        'watch': [
            "'I enjoy to read novels.' → 'I enjoy reading novels.' ('Enjoy' always takes -ing.)",
            "'I look forward to meet you.' → 'I look forward to meeting you.' ('To' is a preposition here, so it takes -ing.)"
        ],
        'selfcheck': [
            "I can choose between -ing and to + verb automatically after common everyday verbs.",
            "I can hear and use the meaning difference after stop, remember, forget, and try."
        ],
        'answers': {
            'A': ["helping", "criticising", "to accept", "hearing", "smoking", "to open"],
            'B': ["I really enjoy reading historical biographies in the evening.",
                  "We look forward to meeting your team on Monday.",
                  "My colleague suggested leaving early before the snow started. / …suggested that we leave early…",
                  "The classroom needs cleaning before tomorrow. / The classroom needs to be cleaned before tomorrow.",
                  "posting (because I posted it first and I recall the memory of doing it now)",
                  "answers vary (e.g. 'Instead of cramming the night before an exam, I review my notes for fifteen minutes every evening.')"],
        },
    },
}

L12 = {
    'n': 12, 'part_no': 6, 'part_title': 'Speak with Greater Precision',
    'title': 'Relative Clauses and Concise Descriptions',
    'goal': 'describe people, places and ideas precisely in one sentence',
    'intro': [
        "Listen to someone speaking in short, choppy fragments: 'I met a doctor yesterday. She studied in Delhi. "
        "She now runs a clinic. The clinic serves three mountain villages.' Every fact is clear, but the rhythm "
        "sounds robotic. Now listen to how a fluent speaker weaves those four fragments into one smooth sentence: "
        "'Yesterday I met a doctor who studied in Delhi and now runs a clinic serving three mountain villages.'",
        "Relative clauses (who, which, that, whose, where) and reduced clauses are the master tools for packing "
        "rich detail into clean, effortless spoken sentences."
    ],
    'hook': [
        "Play a quick 60-second guessing game with your partner:",
        "•  Think of one person in the room, one well-known place in your country, and one everyday object in your bag.",
        "•  Without saying the name, describe each one in a single sentence starting with 'It's someone who…', 'It's a place where…', or 'It's something that…' so your partner can guess it immediately.",
    ],
    'rules': [
        {'label': 'Rule 1 — Defining relative clauses: identifying exactly which one',
         'text': [
             "A defining relative clause gives essential information that tells your listener *which* person, thing, "
             "or place you mean. If you remove a defining clause from 'The woman who interviewed me was very kind', "
             "you are left with 'The woman was very kind' — and your listener has no idea which woman you are talking about.",
             "Use 'who' (or 'that') for people, 'which' or 'that' for things, 'whose' for possession, 'where' for "
             "places, and 'when' for times. When the relative pronoun is the object of the clause ('The book [that] "
             "I read'), natural spoken English usually drops it altogether: 'The book I read was fascinating.'"
         ],
         'formula': [
             "Defining pronouns (no commas):  who / that (people)  ·  which / that (things)  ·  whose (possession)  ·  where (place)  ·  when (time)",
             "Omitting the object pronoun in speech:  The colleague (who/that) I called  ·  The course (that/which) we chose"
         ],
         'examples': [
             "The engineer who designed this solar pump lives in our district.  ('who' is the subject — cannot be dropped)",
             "The article I sent you yesterday explains the new policy clearly.  (object pronoun 'that/which' dropped naturally)",
             "That's the café where we held our first study group.",
             "We interviewed a candidate whose research focuses on water conservation."
         ],
         'remember': [
             "Never repeat the object pronoun at the end of a relative clause: say 'The film we watched was great' "
             "(never 'The film which we watched it was great').",
             "Never use 'what' after a noun as a relative pronoun: say 'The book that I read' (never 'The book what I read')."
         ]},
        {'label': 'Rule 2 — Non-defining relative clauses: adding extra detail with a pause',
         'text': [
             "Sometimes your listener already knows exactly who or what you mean (for example, 'My older brother', "
             "'Kabul University', or 'Our new project'), and you simply want to drop in an extra piece of interesting "
             "information along the way.",
             "In writing, we set this extra clause inside commas; in speech, we frame it with brief natural pauses. "
             "Two strict rules apply here: you can never use 'that' after a comma, and you can never omit the pronoun."
         ],
         'formula': [
             "Non-defining (with commas / spoken pauses):  Noun, who / which / whose / where …, main clause",
             "Commenting on a whole idea:  Full clause, which + singular verb …"
         ],
         'examples': [
             "My older brother, who works as a civil engineer in Herat, is visiting us this weekend.",
             "Our central library, which was renovated last year, stays open until nine in the evening.",
             "The flight was delayed by four hours, which meant we missed the opening session."
         ],
         'remember': [
             "After a comma (or spoken pause) in a non-defining clause, always use 'who' for people and 'which' for things — never 'that'."
         ]},
        {'label': 'Rule 3 — Prepositions in relative clauses: formal speech vs everyday conversation',
         'text': [
             "In formal presentations and writing, a preposition can move in front of 'whom' (for people) or 'which' "
             "(for things): 'the committee to which we reported'. In everyday natural conversation, put the preposition "
             "at the end of the clause and drop the pronoun: 'the committee we reported to'."
         ],
         'formula': [
             "Formal register:  preposition + whom / which   →   the professor with whom I worked  ·  the topic about which she spoke",
             "Natural spoken register:  (who/that/which) … + preposition   →   the professor I worked with  ·  the topic she spoke about"
         ],
         'examples': [
             "The organisation for which he works provides rural medical clinics.  (formal)",
             "The organisation he works for provides rural medical clinics.  (natural conversation)"
         ],
         'remember': [
             "Notice when a place needs 'where' versus 'which': 'the clinic where I work' (= at which I work — no preposition needed) "
             "versus 'the clinic which was opened last year' ('the clinic' is the subject of 'was opened', so use 'which/that', not 'where')."
         ]},
        {'label': 'Rule 4 — Reduced relative clauses: making descriptions crisp and concise',
         'text': [
             "When a relative clause contains 'who/which/that + be' followed by an -ing verb, a past participle, or "
             "an adjective phrase, you can make your sentence cleaner by dropping 'who/which/that + be' altogether."
         ],
         'formula': [
             "Active reduction (-ing):  the woman (who is) talking to the director   →   the woman talking to the director",
             "Passive reduction (past participle):  the results (which were) published today   →   the results published today"
         ],
         'examples': [
             "Anyone wishing to join the debate club should sign up by Thursday.  (= Anyone who wishes…)",
             "The figures shown on the second slide come from this year's survey.  (= The figures which are shown…)",
             "Students interested in the scholarship can collect a form from the office.  (= Students who are interested…)"
         ],
         'remember': [
             "Only reduce a subject relative clause by turning a continuous/active verb into -ing or keeping a passive participle/adjective: "
             "never drop 'who' in front of a single past-simple active verb ('The man who called yesterday' cannot become 'The man called yesterday')."
         ]},
    ],
    'differences': [
        {'title': 'Defining vs non-defining — how a pause changes the number of sisters!',
         'text': [
             "Read these two sentences aloud — pausing at the commas in the right-hand column — and notice what "
             "changes about the speaker's family:"
         ],
         'rows': [
             ["My sister who lives in London is a paediatrician.", "My sister, who lives in London, is a paediatrician.", "Left (no pause/commas): I have more than one sister, and I am specifying which sister I mean (the one in London, not the one in Kabul).  Right (with pauses/commas): I have only one sister, and by the way, she happens to live in London."],
             ["The laptops which were left in the lab were locked away.", "The laptops, which were left in the lab, were locked away.", "Left: only the laptops left in the lab were locked away.  Right: all the laptops were left in the lab, and all of them were locked away."],
         ], 'headers': ['Defining (identifies which one)', 'Non-defining (adds extra detail)', 'What your listener understands']},
        {'title': 'Choosing between who, which, that, whose, and where',
         'rows': [
             ["The mentor who / that guided me…", "The mentor, who guided me for years,…", "'That' works alongside 'who/which' in defining clauses, but is never used after a comma in non-defining clauses."],
             ["The village where I grew up…", "The village that / which I visited…", "Use 'where' when an action happens *in/at* the place; use 'that/which' when the place is the direct object or subject of the verb."],
         ], 'headers': ['Pattern A', 'Pattern B', 'The key distinction']},
    ],
    'practice_a': [
        "The pharmacist __________ helped us find the right medicine was remarkably patient.  (who / which / whose)",
        "My first laptop, __________ I bought six years ago, still runs smoothly.  (that / which)",
        "This is the quiet courtyard __________ we used to revise before our university exams.  (where / which)",
        "The passenger __________ suitcase was misplaced at the airport filed a report at the desk.  (who / whose)",
        "The survey results __________ were published this morning surprised the whole department.  (use which/that, or reduce the clause by omitting both words)",
        "I really enjoyed the documentary you recommended last week.  (which relative pronoun was omitted after 'documentary'?)",
    ],
    'practice_b': [
        "Combine into one smooth sentence using who: 'The instructor is outstanding. She taught us academic speaking last term.'",
        "Combine using commas (non-defining extra detail): 'My uncle is an experienced airline pilot. He has flown to over forty countries.'",
        "Correct the mistake: 'My mother, that lives in Kandahar, is visiting us next Friday.'",
        "Correct the mistake: 'The article what I read on the train was eye-opening.'",
        "Make this sentence more concise by reducing the relative clause: 'Students who are interested in the summer internship should apply online.'",
        "Describe a place you love in one or two sentences using one defining clause and one non-defining clause.",
    ],
    'pair': {
        'intro': "Play 'Precision Portraits' with your partner. Take turns describing two people, two places, or two "
                 "important objects from your own life without naming them first — packing your clues into relative "
                 "and reduced clauses.",
        'task': [
            "For each description, include at least one defining clause (identifying who/what/where it is), one non-defining clause (adding an extra story or comment), and one reduced clause (-ing or past participle).",
            "Once your partner guesses or hears your portrait, work together to tighten one long two-sentence description into a single crisp sentence."
        ],
        'model': [
            "A: I'm thinking of a small bookshop standing opposite our old high school, where I used to spend every Thursday afternoon. The owner, whose family has run the shop for forty years, always kept a shelf of second-hand English novels for students.",
            "B: That sounds wonderful — did he recommend books to you, or did he let you browse on your own?"
        ],
        'output': "Two successful guesses per pair: each description contains one defining and one "
                  "non-defining clause, and both partners leave with one improved, more concise "
                  "sentence.",
        'criteria': [
            "chooses who, which, that, whose, and where accurately",
            "distinguishes between defining meaning and non-defining extra detail",
            "omits object pronouns or reduces clauses naturally to keep speech concise",
            "delivers clear, vivid descriptions that the partner can picture immediately"
        ],
    },
    'advanced': {
        'intro': "When you combine clause-commenting 'which', wh-clefts, and reduced clauses, your spoken descriptions "
                 "gain the crisp authority of a skilled presenter.",
        'base': [
            "Practise describing people and places around you with who, which, whose, and where — and deliberately drop the pronoun whenever it is the object ('the café we visited', 'the friend I called').",
            "Test every 'where' vs 'which' choice by checking whether the place means 'in/at which' ('the town where I lived') or acts as the direct object/subject ('the town that we visited')."
        ],
        'upgrade': [
            "Use ', which…' at the end of a spoken clause to evaluate the impact of a whole situation: 'They moved the meeting to eight in the morning, which gave everyone the afternoon free to finish their reports.'",
            "Use 'What…' nominal relative clauses to spotlight what matters most: 'What impressed me most was how calmly she answered the tough questions.'",
            "Use reduced passive and active clauses for crisp professional summaries: 'Applications received after Friday will be held for the next intake' · 'Anyone needing transport should notify the office.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to choose one person who has had a lasting influence on your life. Jot down three "
                "keywords only: who they are (defining clause), one memorable background detail about them (non-defining "
                "clause with 'who' or 'whose'), and one specific piece of advice or habit they passed on to you "
                "(reduced clause).",
        'task': "One-minute tribute talk: Describe a person who influenced you — a teacher, family member, colleague, "
                "or friend. Use at least two defining relative clauses, one non-defining relative clause (including "
                "'whose' or ', which'), and one concise reduced clause. Speak naturally without notes.",
        'model': "The person who influenced my study habits most is my uncle, who taught secondary-school physics "
                 "for over thirty years. He is the person whose advice I still hear whenever I sit down to tackle a "
                 "difficult project: always start with the part that scares you most. The students taught by him at "
                 "our local school respected him because he never lost his patience, which made even shy learners "
                 "brave enough to ask questions. Anyone working alongside him quickly learns the same quiet lesson "
                 "— steady preparation beats last-minute talent every time.",
        'feedback': [
            "uses defining relative clauses (and dropped object pronouns) naturally to identify people and things",
            "includes at least one non-defining clause ('…, who…', '…, whose…', or '…, which…') accurately",
            "includes at least one concise reduced clause (-ing or past participle)",
            "paints a vivid, memorable portrait of the person and their influence"
        ],
    },
    'review': {
        'points': [
            "Defining relative clauses identify essential meaning (no commas; object pronouns like 'that/who/which' are often dropped in speech).",
            "Non-defining relative clauses add extra information with commas/pauses — always use 'who/which/whose/where', never 'that'.",
            "Reduce 'who/which/that + be' before -ing verbs, past participles, and adjectives to make descriptions tighter ('the data published today')."
        ],
        'retrieval': [
            "Describe two people you know: one using 'whose' and one using a non-defining clause with ', who…'.",
            "Take the sentence 'The students who are waiting outside have registered' and say the reduced version aloud."
        ],
        'watch': [
            "'The book what I read was great.' → 'The book (that) I read was great.' (Never use 'what' after a noun as a relative pronoun.)",
            "'My mother, that lives in Kandahar, called.' → 'My mother, who lives in Kandahar, called.' (Never use 'that' after a comma.)"
        ],
        'selfcheck': [
            "I can combine choppy sentences smoothly using who, which, that, whose, and where.",
            "I can drop object pronouns and reduce relative clauses naturally when speaking."
        ],
        'answers': {
            'A': ["who", "which", "where", "whose", "which / that (or omit 'which/that were' to form the reduced clause 'The survey results published this morning…')", "that / which"],
            'B': ["The instructor who taught us academic speaking last term is outstanding.",
                  "My uncle, who is an experienced airline pilot, has flown to over forty countries. / My uncle, who has flown to over forty countries, is an experienced airline pilot.",
                  "My mother, who lives in Kandahar, is visiting us next Friday.",
                  "The article (that / which) I read on the train was eye-opening.",
                  "Students interested in the summer internship should apply online.",
                  "answers vary"],
        },
    },
}

LESSONS_9_12 = [L9, L10, L11, L12]


def render_all(doc, keys_registry):
    for L in LESSONS_9_12:
        render_lesson(doc, L, keys_registry)

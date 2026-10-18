# -*- coding: utf-8 -*-
"""Lessons 13-16 — Part Seven: Sound More Natural and Advanced; Part Eight: Speak with Confidence."""
from lesson_template import render_lesson

L13 = {
    'n': 13, 'part_no': 7, 'part_title': 'Sound More Natural and Advanced',
    'title': 'Reported Speech and Reporting Verbs',
    'goal': 'report conversations and summarise information accurately and naturally',
    'intro': [
        "Listen to how an inexperienced speaker recounts a meeting: 'The manager said, \"We have a problem.\" Then Sara said, "
        "\"Let's delay the launch.\" Then the manager said, \"No, we can't.\"' Now listen to how an experienced "
        "speaker summarizes the exact same exchange in one breath: 'When the manager explained that we had a problem, "
        "Sara suggested delaying the launch, but he insisted on keeping the original date.'",
        "Nearly half of everyday conversation consists of telling one person what another person said, asked, "
        "promised, or advised. When you master reported speech and expressive reporting verbs, you stop reciting "
        "transcripts and start summarizing ideas with clarity and style."
    ],
    'hook': [
        "Think about two real messages or conversations from your week:",
        "•  A piece of advice or a reminder a family member, teacher, or colleague gave you recently.",
        "•  A question someone asked you this week — and how you answered it.",
        "Tell your partner about both moments without quoting the speaker's exact words ('She told me that…', "
        "'He asked me whether…', 'They reminded me to…'). Which parts felt easy to report, and where did you pause to think?",
    ],
    'rules': [
        {'label': 'Rule 1 — Stepping back in time: tense backshift and when to keep the present',
         'text': [
             "When you report what someone said in the past, the original moment of speaking is now behind you. "
             "To reflect that distance, English normally shifts the verb one step back in time: present simple becomes "
             "past simple, present continuous becomes past continuous, past simple and present perfect become past "
             "perfect, 'will' becomes 'would', and 'can' becomes 'could'.",
             "However, backshift is not a blind mechanical rule. If what the speaker said is a permanent truth, or a "
             "situation that is still clearly true right now, you can either shift the tense or keep the present tense."
         ],
         'formula': [
             "Standard backshift:  am/is/are → was/were  ·  work → worked  ·  worked / have worked → had worked  ·  will → would  ·  can → could",
             "Forms that stay unchanged:  would, could, should, might, and past perfect (had done) stay as they are"
         ],
         'examples': [
             "Direct: \"I'm working on the budget.\"   →   Reported: He said (that) he was working on the budget.",
             "Direct: \"We've already booked the hall.\"   →   Reported: They told us (that) they had already booked the hall.",
             "Direct: \"I'll call you this evening.\"   →   Reported: She said she would call me that evening.",
             "Direct: \"My sister lives in Bamyan.\"   →   Reported: He said his sister lives / lived in Bamyan.  (still true today)"
         ],
         'remember': [
             "Watch the difference between 'say' and 'tell': 'say' never takes a personal object directly ('He said that he was ready' or 'He said to me…'), "
             "while 'tell' must have a person right after it ('He told me that he was ready' — never 'He said me…')."
         ]},
        {'label': 'Rule 2 — Reporting questions, requests, and commands',
         'text': [
             "When you report a question ('She asked me where I lived'), it is no longer a direct question — it is a "
             "statement about a question. That means you drop the question mark, drop the auxiliary 'do/does/did', "
             "and return the words to normal statement order (subject + verb)!",
             "For Yes/No questions, link with 'if' or 'whether'. For requests and commands, use 'asked / told / "
             "warned + person + (not) to + base verb'."
         ],
         'formula': [
             "Reported Wh- question:  asked (+ person) + Wh- word + subject + verb (no inversion!)",
             "Reported Yes/No question:  asked (+ person) + if / whether + subject + verb",
             "Reported command / request:  told / asked / advised / warned + person + (not) to + base verb"
         ],
         'examples': [
             "Direct: \"Where did you park the car?\"   →   She asked me where I had parked (or: parked) the car.",
             "Direct: \"Are the results ready?\"   →   He asked whether the results were ready.",
             "Direct: \"Please check the figures twice.\"   →   The director asked us to check the figures twice.",
             "Direct: \"Don't touch the wet paint!\"   →   He warned the children not to touch the wet paint."
         ],
         'remember': [
             "Place 'not' before 'to' in negative commands: 'She told me not to worry' (not 'She told me to not worry' or 'not worry')."
         ]},
        {'label': 'Rule 3 — Summarising with expressive reporting verbs',
         'text': [
             "If you report every sentence with 'He said… and then she said…', your story quickly sounds repetitive. "
             "Reporting verbs like admit, suggest, promise, deny, remind, warn, apologise, and insist capture the "
             "speaker's exact attitude in a single word — provided you pair each verb with its natural grammar pattern."
         ],
         'formula': [
             "Verb + to + base verb:  agree · offer · promise · refuse · threaten + to do",
             "Verb + person + (not) to + base verb:  advise · encourage · invite · remind · persuade · tell · warn + someone to do",
             "Verb + verb-ing (or that-clause):  admit · deny · recommend · suggest + doing   ·   apologise for / insist on + doing"
         ],
         'examples': [
             "He admitted making a calculation mistake in the first table.  (admit + -ing)",
             "She promised to send the feedback before Friday morning.  (promise + to + verb)",
             "The doctor advised my father to walk for thirty minutes every day.  (advise + person + to + verb)",
             "Tariq suggested taking the early train to avoid the crowd.  (suggest + -ing)"
         ],
         'remember': [
             "Never say 'She suggested me to go' or 'He explained me the rule' — say 'She suggested going / that we go' "
             "and 'He explained the rule to me.'"
         ]},
        {'label': 'Rule 4 — Shifting time and place words naturally',
         'text': [
             "When you report a conversation days or weeks later in a different place, adjust the time and place words "
             "so they match your listener's viewpoint (now → then, today → that day, yesterday → the day before, "
             "tomorrow → the next day, here → there)."
         ],
         'formula': [
             "today → that day   ·   yesterday → the day before / the previous day   ·   tomorrow → the next day / the following day",
             "now → then / at that moment   ·   last week → the week before   ·   here → there   ·   this → that"
         ],
         'examples': [
             "Direct (on Monday): \"I'll finish the report tomorrow.\"   →   Reported (on Friday): She said she would finish the report the next day.",
             "Direct (on Monday): \"I'll finish the report tomorrow.\"   →   Reported (later on Monday): She said she'll / she'd finish the report tomorrow."
         ],
         'remember': [
             "Use common sense with time words: if you are reporting a conversation on the very same day, keep 'today' and 'tomorrow' as they are!"
         ]},
    ],
    'differences': [
        {'title': 'say vs tell vs ask — choosing the right core verb',
         'rows': [
             ["He said (that) the meeting was over.", "He told me (that) the meeting was over.", "He asked me if the meeting was over.", "'Say' focuses on the words (no personal object); 'tell' focuses on informing a person ('told me'); 'ask' reports a question or request."],
         ], 'headers': ['say (+ that)', 'tell + person (+ that)', 'ask (+ person) + if / Wh- / to', 'How to keep them straight']},
        {'title': 'Reporting later (backshift) vs reporting a still-true fact',
         'rows': [
             ["She said she was feeling exhausted.", "She said she speaks three languages.", "In the first, her tiredness belonged to that past moment, so we shift to 'was'. In the second, her ability to speak three languages is still true today, so 'speaks' (or 'spoke') is completely natural."],
         ], 'headers': ['Past situation (backshifted)', 'Permanent / still-true fact', 'Why both work']},
        {'title': 'How reporting verbs compress whole sentences into one precise word',
         'text': [
             "Compare how a specific reporting verb captures the tone without needing a long quote:",
             "•  \"No, I definitely didn't leave the freezer door open!\"   →   He denied leaving the freezer door open.",
             "•  \"Don't forget to bring your passport tomorrow morning.\"   →   She reminded me to bring my passport the next morning.",
             "•  \"Why don't we test the microphone before the guests arrive?\"   →   He suggested testing the microphone before the guests arrived."
         ]},
    ],
    'practice_a': [
        "\"I am working on the presentation right now.\"   →   He said he __________ (work) on the presentation then.",
        "\"We have already submitted the application.\"   →   They told us they __________ (already / submit) the application.",
        "\"Where did you park the van?\"   →   She asked me where I __________ (park) the van.",
        "\"Don't touch the hot Kettle!\"   →   He warned the child __________ touch the hot kettle.",
        "\"I'll definitely help you revise on Saturday.\"   →   She promised __________ (help) me revise on Saturday.",
        "\"Let's take a ten-minute break before part two.\"   →   He suggested __________ (take) a ten-minute break.",
    ],
    'practice_b': [
        "Report this statement: 'I never drink coffee after six in the evening.'  (He said…)",
        "Report this question: 'When will the scholarship results be announced?'  (They asked…)",
        "Correct the mistake: 'He said me that the train had been cancelled.'",
        "Correct the mistake: 'My colleague suggested me to apply for the fellowship.'",
        "Report this sentence using the verb deny: '\"No, I did not share the password with anyone.\"'  (He denied…)",
        "Report two helpful pieces of advice a teacher or family member has given you, using two different reporting verbs (such as advised, encouraged, reminded, or warned).",
    ],
    'pair': {
        'intro': "Play 'The Diplomatic Messenger'. Partner A speaks five short direct messages from everyday life "
                 "(a complaint, a promise, a question, a warning, and a suggestion). Partner B listens carefully and "
                 "reports each message aloud using a precise reporting verb — without repeating 'said' every time. "
                 "Then swap roles.",
        'task': [
            "Partner A: create or adapt five one-sentence messages (for example: 'Why didn't the courier call me?', 'I'll send the slides by noon', 'Don't drive over the mountain pass at night', 'Why don't we meet at the library?', 'I'm sorry I missed your call').",
            "Partner B: report all five messages back to Partner A (or to a neighbouring pair) using at least four different reporting verbs, accurate backshift, and statement word order in questions."
        ],
        'model': [
            "A (Direct): 'I'm really sorry I missed your presentation yesterday — I'll watch the recording tonight.'",
            "B (Reported): 'She apologised for missing my presentation the day before and promised to watch the recording that night.'"
        ],
        'output': "Five faithfully reported messages per reporter, using at least four different "
                  "reporting verbs, with one reported question and one reported command, that the "
                  "listener can repeat accurately.",
        'criteria': [
            "uses tense backshift and time-reference shifts accurately",
            "uses statement word order (no 'do/did' inversion) in all reported questions",
            "uses at least four varied reporting verbs with their right patterns (promised to, suggested -ing, warned not to…)",
            "summarizes the meaning smoothly and naturally"
        ],
    },
    'advanced': {
        'intro': "In academic discussions, journalism, and workplace negotiations, reporting verbs also signal how "
                 "much weight or skepticism you attach to someone else's words.",
        'base': [
            "Practise the four core reporting-verb families as spoken chunks: 'promised / offered / agreed to do' · 'advised / reminded / warned me to do' · 'suggested / admitted / denied doing' · 'explained / pointed out that…'.",
            "Take three questions someone asked you today and report them aloud using 'asked me if…' and 'asked me where/when/why…'."
        ],
        'upgrade': [
            "Use continuous or narrative frames to make spoken storytelling vivid: 'She kept insisting that she knew the shortcut' · 'He went on to explain how the system worked.'",
            "Use analytical reporting verbs in presentations and essays: 'The study points out / demonstrates / confirms that…' · 'Critics argue / question whether…'",
            "Distinguish neutral reporting from cautious skepticism: compare 'The minister stated that costs had fallen' (neutral) with 'The minister claimed to have reduced costs, although the audit disagreed' (cautious)."
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to recall a real conversation you had recently — a family discussion, a job interview, "
                "a team meeting, or a lively debate with a friend. Jot down four keywords for what was said and pick "
                "four different reporting verbs before you speak (for example: asked, suggested, warned, promised, "
                "admitted, agreed).",
        'task': "Ninety-second conversation recap: Retell a memorable conversation you had recently. Report at least "
                "four things that were said (including at least one question and one piece of advice or suggestion) "
                "using varied reporting verbs, and finish with your own reflection on how the conversation turned out.",
        'model': "Last Saturday my younger sister called to tell me that she had been offered a position at a graphic "
                 "design studio. She admitted that she felt nervous about the tight deadlines, but she promised to "
                 "give it her best effort for the first six months. Our father warned her not to sign the contract "
                 "without checking the evening hours first, and she agreed to ask the director for a written schedule. "
                 "She also asked me whether I thought she should negotiate the starting salary; I suggested showing "
                 "them her portfolio from university before naming a figure. In the end, they offered her a better rate "
                 "than she had expected.",
        'feedback': [
            "accurate backshift and time expressions throughout the retelling",
            "uses at least four varied reporting verbs with their natural grammar patterns",
            "reports questions with statement word order and advice/warnings with '(not) to + verb'",
            "ends with a clear personal comment on the outcome of the conversation"
        ],
    },
    'review': {
        'points': [
            "When reporting past speech, verbs normally step back one tense, and time/place words shift to match the listener's viewpoint.",
            "Reported questions return to normal statement word order (subject + verb) with 'if/whether' or a Wh- word — never invert with 'do/did'.",
            "Match each reporting verb to its grammar pattern: 'promised to do', 'warned me not to do', 'suggested doing', 'explained that…'."
        ],
        'retrieval': [
            "Report three things different people have said or asked you over the past two days.",
            "Say one sentence with 'warned', one with 'suggested', and one with 'asked whether' from memory."
        ],
        'watch': [
            "'He said me that he was busy.' → 'He told me that he was busy' or 'He said that he was busy.'",
            "'She suggested me to take a taxi.' → 'She suggested taking a taxi' or 'She suggested that we take a taxi.'"
        ],
        'selfcheck': [
            "I can report statements, questions, and requests accurately without word-order slips.",
            "I can summarize conversations naturally using a variety of reporting verbs beyond 'say' and 'tell'."
        ],
        'answers': {
            'A': ["was working", "had already submitted", "had parked (or: parked)", "not to", "to help", "taking"],
            'B': ["He said (that) he never drank coffee after six in the evening. / He said (that) he never drinks coffee after six in the evening.",
                  "They asked when the scholarship results would be announced.",
                  "He told me that the train had been cancelled. / He said that the train had been cancelled.",
                  "My colleague suggested applying for the fellowship. / My colleague suggested that I apply for the fellowship.",
                  "He denied sharing the password with anyone.",
                  "answers vary (e.g. 'My teacher advised me to read aloud every morning, and my mother reminded me not to skip breakfast before an exam.')"],
        },
    },
}

L14 = {
    'n': 14, 'part_no': 7, 'part_title': 'Sound More Natural and Advanced',
    'title': 'Participles and Advanced Sentence Patterns',
    'goal': 'combine ideas concisely without losing clarity',
    'intro': [
        "Read this sentence carefully and picture what it literally says: 'Walking down the mountain road, the "
        "snowstorm started.' Grammatically, that sentence claims that the snowstorm had two legs and was walking down "
        "the mountain road! What the speaker meant, of course, was: 'Walking down the mountain road, we were caught "
        "in a snowstorm.'",
        "Participles (-ing and past participles) allow you to compress two bulky clauses into one sleek, authoritative "
        "sentence — as long as you keep the subject clear and choose the right participle for the job."
    ],
    'hook': [
        "Try combining each pair of sentences below into one smooth sentence aloud with your partner:",
        "•  Pair 1:  'She finished the presentation. Then she opened the floor to questions.'",
        "•  Pair 2:  'The lecture lasted three hours without a break. The students felt exhausted.'",
        "Now compare: why do we call the lecture 'exhausting' (-ing) but the students 'exhausted' (-ed)? Discuss "
        "one experience you found 'exciting' or 'challenging' recently and how you felt during it.",
    ],
    'rules': [
        {'label': 'Rule 1 — Participle adjectives: -ing (the cause) vs -ed (the feeling)',
         'text': [
             "Many everyday adjectives are built from verbs: boring / bored, confusing / confused, fascinating / "
             "fascinated, exhausting / exhausted. Confusing the two endings can lead to unintentional comedy: saying "
             "'I am boring in class' tells your classmates that *you* put *them* to sleep!",
             "Hold on to one simple principle: the '-ing' adjective describes the source that *causes* the feeling, "
             "while the '-ed' adjective describes how a person *feels* inside as a result."
         ],
         'formula': [
             "Present participle adjective (-ing)  →  the source / cause of the experience:  a confusing instruction · an inspiring talk",
             "Past participle adjective (-ed)  →  the person experiencing the feeling:  confused applicants · inspired listeners"
         ],
         'examples': [
             "The documentary about deep-sea exploration was fascinating, and the audience was fascinated.",
             "Working a twelve-hour shift at the hospital is exhausting, so the nurses are exhausted by evening.",
             "The new bus timetable is confusing — even regular commuters look confused."
         ],
         'remember': [
             "A person can be described with '-ing' only when they are the cause of the feeling in others: "
             "'Our history professor is very interesting' (she fascinates her students) versus 'Our history professor is very interested in ancient coins' (she feels curiosity)."
         ]},
        {'label': 'Rule 2 — Participle clauses: compressing time, reason, and passive background',
         'text': [
             "Instead of starting every sentence with a heavy clause ('Because she wanted to save time…', 'After he "
             "had reviewed the data…', 'The report, which was written in haste…'), you can compress the first clause "
             "into a participle phrase — provided both halves of the sentence share the exact same subject.",
             "Use 'Verb-ing…' for an action happening at the same time or as the reason; use 'Having + past participle…' "
             "when the first action was clearly completed before the second; and use a 'Past participle…' when the "
             "opening idea is passive."
         ],
         'formula': [
             "Simultaneous action or reason (active):  Verb-ing …, subject + main verb   →   Walking into the hall, she spotted her friend.",
             "Earlier completed action (active):  Having + past participle …, subject + main verb   →   Having finished the exam, he breathed a sigh of relief.",
             "Passive condition or reason:  Past participle (or Having been + participle) …, subject + main verb   →   Built in 1920, the bridge still carries heavy traffic."
         ],
         'examples': [
             "Realising that the train was about to leave, we ran to the platform.  (= Because we realised…)",
             "Having lived in Kandahar for ten years, he knew every street in the old city.  (= Because he had lived…)",
             "Warned about the approaching storm, the mountain guides postponed the climb.  (= Because they had been warned…)"
         ],
         'remember': [
             "In a reduced opening clause with no stated subject, the understood subject should match the main clause: "
             "'Walking to the station, I got soaked' (I was walking), not 'Walking to the station, the rain started.' "
             "An absolute clause names its own subject: 'With prices rising, families are worried.'"
         ]},
        {'label': 'Rule 3 — Framing a whole situation: Given, Considering, and With + noun + participle',
         'text': [
             "What if you want to set the stage with an outside factor that has its own subject (such as rising prices "
             "or an approaching deadline), or frame a professional judgment? English uses two clean patterns that "
             "never dangle:",
             "1. Prepositional participle frames ('Given the tight budget…', 'Considering the weather…', 'All things considered…') "
             "which are established discourse markers that do not need to match the main subject.",
             "2. Absolute clauses with 'With + noun + participle' ('With the exams approaching, the library is packed'), "
             "which explicitly state their own noun subject right after 'With'."
         ],
         'formula': [
             "Evaluative frames:  Given + noun phrase, …  ·  Considering + noun phrase / that-clause, …  ·  All things considered, …",
             "With-absolute clause:  With + noun + verb-ing / past participle, main clause"
         ],
         'examples': [
             "Given the limited rehearsal time, the students delivered an impressive performance.",
             "With winter approaching rapidly, the municipality repaired the heating pipes.",
             "Considering how little funding the project received, the results were remarkable.",
             "All things considered, moving the workshop to Saturday was the right call."
         ],
         'remember': [
             "'Given' and 'Considering' are exceptionally useful at the start of formal speaking responses because they "
             "let you weigh the context before stating your conclusion."
         ]},
        {'label': 'Rule 4 — Keeping compression natural in spoken English',
         'text': [
             "Concision is not about sounding like a legal contract; it is about removing clutter so your key verbs "
             "stand out. In spoken English, using one or two well-placed participle openings in a two-minute talk "
             "makes you sound composed and articulate — using ten in a row makes you sound unnatural."
         ],
         'formula': [
             "Two clauses with the same subject  →  Participle opening + main clause",
             "Negative participle opening:  Not knowing / Not having received …, subject + main verb"
         ],
         'examples': [
             "Not wanting to wake the children, we spoke in whispers.",
             "Not having received the agenda in advance, several members asked for extra time to read it."
         ],
         'remember': [
             "To make any participle clause negative, place 'Not' (or 'Never') right at the front: 'Not knowing the route, I asked a taxi driver.'"
         ]},
    ],
    'differences': [
        {'title': '-ing (the source) vs -ed (the experiencer)',
         'rows': [
             ["an inspiring speech", "an inspired audience", "The speech generates the inspiration (-ing); the audience feels it inside (-ed)."],
             ["frustrating delays", "frustrated passengers", "The delays cause the frustration (-ing); the passengers experience it (-ed)."],
         ], 'headers': ['-ing adjective (causes the feeling)', '-ed adjective (feels the effect)', 'How to choose instantly']},
        {'title': 'Full adverbial clause vs compressed participle clause',
         'rows': [
             ["After she had reviewed the patients' charts, she began her rounds.", "Having reviewed the patients' charts, she began her rounds.", "Both sentences mean the exact same thing; 'Having reviewed…' removes three unstressed words and sharpens the rhythm."],
             ["Because the manual was written in clear English, it was easy to follow.", "Written in clear English, the manual was easy to follow.", "The passive participle 'Written…' attaches directly to 'the manual'."],
         ], 'headers': ['Full clause (everyday conversation)', 'Participle clause (crisp / formal)', 'What changes']},
        {'title': 'The subject-matching check — catching dangling participles',
         'text': [
             "In a reduced participle clause with no stated subject, the understood subject should normally match "
             "the main clause: 'Opening the door, I felt the cold air' (I opened the door, and I felt the air) — not "
             "'Opening the door, the room was cold' (which makes it sound as if the room opened the door!). "
             "Absolute clauses state their own subject, as in 'Weather permitting, we will leave at dawn' or "
             "'With the rain pouring down, we stayed indoors.'"
         ]},
    ],
    'practice_a': [
        "The three-hour lecture was so __________ (bore) that several people in the back row nodded off.",
        "We were genuinely __________ (amaze) by how quickly the volunteers rebuilt the footbridge.",
        "__________ (finish) her keynote speech, Dr Sadat invited questions from the audience.  (earlier completed action)",
        "__________ (warn) about the icy mountain pass, the drivers fitted snow chains before dawn.  (passive participle)",
        "__________ fuel prices rising this winter, many commuters are sharing rides to work.  (With / Despite)",
        "__________ (walk) into the laboratory, she immediately noticed the unlocked cabinet.",
    ],
    'practice_b': [
        "Compress into one sentence using Having + past participle: 'Because she had practised her talk five times, she spoke without hesitation.'",
        "Compress by reducing the relative clause: 'The technician who was standing by the generator switched off the power.'",
        "Repair the dangling participle so the subject matches: 'Opening the window, the fresh morning breeze cooled the room.'",
        "Rewrite more concisely starting with Given: 'When you take the tight deadline into account, the team's report is very thorough.'",
        "Correct the adjective mistake: 'I have always been very interesting in architectural history.'",
        "Write one sentence of your own starting with 'Having + past participle…' about something you did earlier today.",
    ],
    'pair': {
        'intro': "Play 'The Sixty-Second Executive Briefing'. Take turns giving a calm, concise 60-second briefing "
                 "to your partner on a recent project, trip, or community event — using participle structures to "
                 "pack background and reasons cleanly.",
        'task': [
            "In your 60-second briefing, include: (1) one 'Having + past participle' clause for an earlier step, (2) one framing opener with 'Given…', 'Considering…', or 'With + noun + -ing', and (3) one pair of -ing and -ed adjectives.",
            "While you listen to your partner, check that every participle opening matches the subject that follows it, then summarize their briefing back in one sentence."
        ],
        'model': [
            "A: Given the short notice we received last Monday, our student book fair went remarkably well. Having collected over three hundred donated books during the week, we set up four stalls in the courtyard. The morning setup was exhausting, but everyone felt energised when the first visitors arrived.",
            "B: So having gathered the books in just a few days, you managed to run a busy fair despite the exhausting start!"
        ],
        'output': "One 60-second briefing per partner containing the three required structures, plus "
                  "a listener's one-sentence report-back that matches the briefing's content.",
        'criteria': [
            "every reduced participle clause matches the subject of the main clause",
            "uses 'Having + past participle' and passive/active participles accurately",
            "distinguishes clearly between -ing (cause) and -ed (feeling) adjectives",
            "maintains natural spoken clarity without overloading a single sentence"
        ],
    },
    'advanced': {
        'intro': "Used thoughtfully, participle and absolute phrases give formal talks, policy recommendations, "
                 "and academic summaries a composed, effortless flow.",
        'base': [
            "Test every -ing/-ed adjective pair on real situations from your week: tiring / tired, encouraging / encouraged, overwhelming / overwhelmed, satisfying / satisfied.",
            "Whenever you start a sentence with an -ing or -ed phrase, make sure the very next word after the comma is the person or thing doing (or receiving) that action."
        ],
        'upgrade': [
            "Use negative participle openings for concise reasons: 'Never having spoken in front of a camera before, he practised with a timer first' · 'Not wanting to delay the team, she sent the summary ahead.'",
            "Use formal absolute expressions when closing a meeting or summarizing a situation: 'Weather permitting, fieldwork will begin on Monday' · 'There being no further objections, the schedule was approved.'",
            "Close formal recommendations with 'Considering all the evidence,…' or 'All things considered,…' to signal a balanced final judgment."
        ],
    },
    'realtalk': {
        'plan': "Take 45 seconds to choose one practical improvement for your school, university, or workplace "
                "(such as shifting morning hours, creating a quiet study zone, or introducing a mentorship system). "
                "Jot down three keywords only: the problem evidence ('Given…' or 'Having reviewed…'), your specific "
                "recommendation, and your closing judgment ('All things considered…').",
        'task': "Ninety-second policy recommendation: Present one practical change to improve your school or workplace. "
                "Open with 'Given…' or 'Considering…', include at least one 'Having + past participle' clause and one "
                "-ing/-ed adjective contrast, and close with 'All things considered…'. Speak without reading.",
        'model': "Given the number of late arrivals during the winter months, I would recommend shifting our first "
                 "morning seminar from eight o'clock to eight-thirty. Having reviewed the attendance logs from last "
                 "January, our committee noticed that almost all delays occurred before eight-fifteen, when icy roads "
                 "make the morning commute frustrating for drivers and passengers alike. Many tired students walk in "
                 "ten minutes late, missing the opening explanation of the lecture. With classes starting just thirty "
                 "minutes later, everyone could travel more safely and arrive focused. All things considered, a "
                 "one-month winter trial costs nothing and would benefit the entire department.",
        'feedback': [
            "includes at least two accurate participle or framing structures ('Given…', 'Having reviewed…', 'With…')",
            "keeps the subject of every reduced participle clause aligned with the main clause",
            "uses -ing and -ed adjectives accurately ('frustrating commute', 'tired students')",
            "delivers a clear, composed, and persuasive recommendation"
        ],
    },
    'review': {
        'points': [
            "Use '-ing' adjectives for the source that causes a feeling ('a tiring journey') and '-ed' adjectives for the person who feels it ('tired travellers').",
            "Participle clauses ('Walking…', 'Having finished…', 'Written in…') compress two clauses into one — make sure their understood subject matches the main-clause subject.",
            "Use 'Given…', 'Considering…', and 'With + noun + participle' to frame evidence and background formally."
        ],
        'retrieval': [
            "Say one sentence about your morning starting with 'Having + past participle…'.",
            "Describe a recent class, book, or journey using one '-ing' adjective and one '-ed' adjective."
        ],
        'watch': [
            "'Opening the window, the room felt cold.' → 'Opening the window, I felt the cold air.' (The room did not open the window!)",
            "'I am very interesting in history.' → 'I am very interested in history.' (People feel '-ed' about a subject.)"
        ],
        'selfcheck': [
            "I can compress two connected clauses into a clean participle sentence without losing the subject.",
            "I can use 'Given…', 'Considering…', and -ing/-ed adjectives naturally in formal speech."
        ],
        'answers': {
            'A': ["boring", "amazed", "Having finished", "Warned / Having been warned", "With", "Walking"],
            'B': ["Having practised her talk five times, she spoke without hesitation.",
                  "The technician standing by the generator switched off the power.",
                  "Opening the window, I felt the fresh morning breeze cool the room. / When I opened the window, the fresh morning breeze cooled the room.",
                  "Given the tight deadline, the team's report is very thorough.",
                  "I have always been very interested in architectural history.",
                  "answers vary (e.g. 'Having had a cup of green tea, I sat down to read Lesson 14.')"],
        },
    },
}

L15 = {
    'n': 15, 'part_no': 8, 'part_title': 'Speak with Confidence',
    'title': 'Hedging, Emphasis, and Natural Inversion',
    'goal': 'control certainty, emphasis and formality like an educated speaker',
    'intro': [
        "Imagine two economists on a panel discussion. The first says, 'This tax policy will destroy small businesses.' "
        "The second says, 'The evidence suggests that this policy may well place extra pressure on small businesses — "
        "and it is the rural shopkeepers who will feel that pressure first.' Who sounds more credible?",
        "Experienced speakers know two secrets of authority: they soften unproved claims so no one can accuse them "
        "of exaggerating (*hedging*), and they save their strongest grammatical spotlights (*cleft sentences* and "
        "*inversion*) for the one key sentence they want the audience to remember."
    ],
    'hook': [
        "Read these two pairs of sentences aloud with a partner, paying attention to tone and voice stress:",
        "•  Pair 1 (Certainty):   'Working from home makes people lazier.'   vs.   'Working from home can sometimes make it harder to separate rest from work.'",
        "•  Pair 2 (Spotlight):   'The practical examples helped me most.'   vs.   'What helped me most were the practical examples.'",
        "With your partner, take one controversial opinion about education or work and say it twice: first as a "
        "blunt 100% generalisation, and second as a careful, measured claim that an expert would respect.",
    ],
    'rules': [
        {'label': 'Rule 1 — Hedging: matching the strength of your claim to the evidence',
         'text': [
             "In real life, very few social or economic statements are true 100% of the time for 100% of people. "
             "When you say 'Social media ruins concentration,' a listener only has to think of one exception to "
             "reject your argument.",
             "Hedging is the art of calibrating your claim with modal expressions ('may well', 'could'), tendency "
             "verbs ('tend to', 'seem to', 'appear to'), frequency qualifiers ('in many cases', 'broadly speaking'), "
             "or impersonal frames ('the data suggests that…', 'it could be argued that…'). Hedging can make a claim "
             "sound measured when evidence is limited or a conclusion is uncertain. Academic and professional speakers "
             "often hedge; too much hedging, however, can make a message unclear."
         ],
         'formula': [
             "Modal hedges:  may / might / could + base verb   ·   may well (= quite likely)   ·   is likely to + verb",
             "Tendency verbs:  tend(s) to + base verb   ·   seem(s) / appear(s) to + base verb",
             "Evidence & argument frames:  The evidence suggests that …   ·   It could be argued that …   ·   In most cases, …"
         ],
         'examples': [
             "Students who study in short daily sessions tend to retain vocabulary longer.",
             "Upgrading the regional roads may well reduce transport costs by twenty percent.",
             "The preliminary figures suggest that enrolment has risen this autumn.",
             "It could be argued that practical apprenticeships are just as valuable as university degrees."
         ],
         'remember': [
             "Use one well-chosen hedge per claim, not three piled on top of each other: 'This policy may well reduce costs' "
             "sounds thoughtful; 'Perhaps this policy might possibly seem to reduce costs' sounds unsure."
         ]},
        {'label': 'Rule 2 — Spotlight emphasis: cleft sentences and emphatic "do"',
         'text': [
             "In writing, you can underline or bold a word to make it stand out. In speaking, English gives you "
             "a structural spotlight called a *cleft sentence*, which splits a single sentence into two halves so "
             "the listener's ear lands squarely on the key point.",
             "Use an 'It-cleft' ('It was the cost that delayed us') to contrast one specific person, thing, or time "
             "with others; use a 'Wh-cleft' ('What we need now is clear communication') to build anticipation before "
             "delivering your main point; or add 'do / does / did' before a base verb for warm personal emphasis."
         ],
         'formula': [
             "It-cleft:  It is / was + focused item + that / who + rest of clause   →   It was Mariam who solved the problem.",
             "Wh-cleft:  What + clause + is / was + focused item (or base/to-verb)   →   What matters most is consistency.",
             "Auxiliary emphasis:  Subject + do / does / did + base verb   →   I do appreciate your patience."
         ],
         'examples': [
             "It wasn't the grammar rules that held me back — it was my fear of speaking aloud.",
             "What surprised the researchers most was how rapidly the village adopted solar power.",
             "We didn't win the tournament, but we did learn how to play as a real team."
         ],
         'remember': [
             "When you speak an It-cleft or auxiliary emphasis sentence, match the grammar with vocal stress on the "
             "spotlighted word: 'It was the DEADLINE that forced our hand' · 'She DID call you yesterday.'"
         ]},
        {'label': 'Rule 3 — Negative and limiting inversion: formal rhetorical power',
         'text': [
             "When you place a strong negative or limiting expression ('Never', 'Rarely', 'Seldom', 'Not only', "
             "'Only after…', 'Under no circumstances') at the very beginning of a sentence for dramatic or formal "
             "emphasis, English flips the subject and auxiliary verb into question word order.",
             "Because inversion is a high-impact rhetorical device, treat it like a trumpet note in a speech: using "
             "it once at a key moment commands attention; using it in every paragraph sounds theatrical."
         ],
         'formula': [
             "Negative adverbial + auxiliary + subject + verb:  Never have I seen …  ·  Rarely does a team achieve …  ·  Seldom had we faced …",
             "Correlative addition:  Not only + did/has/is + subject + verb …, (but) … also …",
             "Limiting 'Only' phrase:  Only then / Only after + phrase/clause + did + subject + base verb"
         ],
         'examples': [
             "Never have I heard a more practical explanation of the issue.",
             "Not only did the clinic treat patients free of charge, but it also trained local nurses.",
             "Rarely do we get a second chance to make a first impression.",
             "Only after reading the contract a second time did I notice the hidden fee."
         ],
         'remember': [
             "With 'Only after…', 'Only when…', and 'Not until…', wait until the main clause to invert the verb: "
             "'Only when the plane landed did I relax' (do not invert 'the plane landed')."
         ]},
        {'label': 'Rule 4 — Calibrating certainty and register to your audience',
         'text': [
             "Notice how English organises probability and formality by meaning and context rather than on a rigid "
             "mathematical ladder. When your evidence is solid, state it firmly ('will', 'must be'); when it is "
             "probable, signal expectation ('should', 'is likely to', 'may well'); when it is one open possibility "
             "among others, keep the door open ('may', 'might', 'could')."
         ],
         'formula': [
             "Strong prediction / inference:  will · must be   ·   Expectation / high likelihood:  should · be likely to · may well   ·   Open possibility:  may · might · could",
             "Adjusting register:  Formal (inversion, clefts, passives, full forms)  ↔  Everyday conversation (contractions, direct active verbs)"
         ],
         'examples': [
             "Formal presentation: 'Not only does this approach reduce waste, but it may well lower operating costs.'",
             "Everyday workplace chat: 'This approach cuts waste, and it'll probably save us money too.'"
         ],
         'remember': [
             "A thoughtful hedge signals intellectual honesty — showing your listener that you are matching the strength "
             "of your claim to the strength of your evidence."
         ]},
    ],
    'differences': [
        {'title': 'Three levels of commitment to the same prediction',
         'rows': [
             ["The new rail link will transform regional trade.", "The new rail link may well transform regional trade.", "The new rail link could transform regional trade.", "1. 'Will' = firm conviction.  2. 'May well' = strong likelihood based on current signs.  3. 'Could' = one realistic possibility if conditions go well."],
         ], 'headers': ['Firm prediction (will)', 'Strong likelihood (may well)', 'Open possibility (could / might)', 'What your audience hears']},
        {'title': 'Standard word order vs formal negative inversion',
         'rows': [
             ["I have never witnessed such determination.", "Never have I witnessed such determination.", "Same factual meaning, different impact: placing 'Never' first and inverting 'have I' elevates the sentence for a speech or key conclusion."],
             [" I understood the problem only after I visited the site.", "Only after I visited the site did I understand the problem.", "The 'Only after…' opening builds suspense and lands the insight ('did I understand') with sharp focus."],
         ], 'headers': ['Everyday word order', 'Inverted emphasis (formal)', 'When to use it']},
        {'title': 'Moving the spotlight with cleft sentences',
         'rows': [
             ["The training budget needs urgent attention.", "It is the training budget that needs urgent attention.", "What needs urgent attention is the training budget.", "1. Neutral statement.  2. It-cleft (contrasts the training budget with other budgets).  3. Wh-cleft (builds anticipation before naming the budget at the end)."],
         ], 'headers': ['Direct statement', 'It-cleft (initial spotlight)', 'Wh-cleft (end spotlight)', 'How the focus shifts']},
    ],
    'practice_a': [
        "__________ have I heard such a clear and fair summary of the debate.  (Never / Ever)",
        "Not only __________ (she / pass) the fellowship exam, but she also achieved the highest score in the province.",
        "Only after reading the instructions twice __________ (I / understand) how the device worked.",
        "The survey data __________ (suggest) that evening classes are popular with working parents.  (hedged claim)",
        "It was __________ that convinced the committee to approve the project.  (spotlight 'the detailed budget')",
        "Learners who practise out loud __________ (tend) to build fluency faster than those who only read silently.",
    ],
    'practice_b': [
        "Hedge this sweeping claim so it sounds measured and credible: 'Online learning will replace classrooms everywhere.'",
        "Rewrite as an It-cleft focusing on 'the practical examples': 'The practical examples made the lesson easy to follow.'",
        "Rewrite using formal negative inversion starting with Rarely: 'We had rarely seen such rapid progress in a single term.'",
        "Correct the word-order mistake: 'Never I have seen such a busy market.'",
        "Make the same request ('I need two more days to finish the report') at two register levels: (1) to a close teammate, and (2) in a formal meeting with a senior director.",
        "Write one sentence about two strengths of a person you admire starting with 'Not only + auxiliary + subject…'.",
    ],
    'pair': {
        'intro': "Hold a two-person 'Future of Work and Study Panel'. Take turns answering the panel question below "
                 "for one minute each, using careful hedging for predictions and at least one emphatic structure "
                 "(a cleft sentence or negative inversion) for your central thesis. Then ask your partner one "
                 "challenging follow-up question.",
        'task': [
            "Panel question: 'How will artificial intelligence and online tools change the way people learn and work over the next ten years?'",
            "In your one-minute view, include: (1) at least two hedged claims ('may well', 'tend to', 'the evidence suggests'), (2) one Wh-cleft or It-cleft ('What will matter most is…' / 'It is… that…'), and (3) one emphatic 'do/did' or inversion."
        ],
        'model': [
            "A: While software tools will handle routine translation, it is human judgment and empathy that will become even more valuable. Digital platforms may well make self-study faster, yet rarely do people master persuasive communication without live human feedback.",
            "B: That's a thoughtful point — do you think rural schools will benefit equally from those tools, or could the gap widen at first?"
        ],
        'output': "Two one-minute answers per partner, each containing one well-placed hedge, one "
                  "accurate emphasis structure and a clear conclusion — plus one careful answer to "
                  "the partner's hard follow-up question.",
        'criteria': [
            "hedges predictions thoughtfully without stacking too many hedges together",
            "uses at least one cleft sentence or negative inversion accurately",
            "matches the strength of claims to realistic evidence",
            "handles the partner's challenging follow-up question with composure"
        ],
    },
    'advanced': {
        'intro': "Knowing when to soften a claim and when to spotlight a conclusion is what separates mechanical "
                 "correctness from genuine rhetorical authority.",
        'base': [
            "Practise expressing the same observation at three levels of certainty in context: firm inference ('will / must be'), reasonable expectation ('should / may well / is likely to'), and open possibility ('may / might / could') — and state what evidence supports each level.",
            "Say three core inversion frames aloud until the auxiliary-before-subject rhythm feels natural: 'Never have I…' · 'Not only did…' · 'Only then did I…'."
        ],
        'upgrade': [
            "Use 'Little did I know / realise…' to add suspense at a turning point in a spoken story: 'Little did we realise how much that five-minute conversation would change our plans.'",
            "Use deliberate understatement (litotes) for composed, diplomatic evaluation: 'Reaching agreement across four departments was no small achievement' · 'The initial results are not unpromising.'",
            "Combine a formal inverted conditional with a hedged result in policy talks: 'Were the municipality to expand the bus network, peak-hour congestion might well fall by a third.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to prepare a two-minute formal talk on improving education or professional training "
                "in your country. Jot down three single keywords only: one realistic benefit to hedge ('may well' / "
                "'tends to'), one core priority to spotlight with a cleft ('It is… that…' or 'What we need most is…'), "
                "and one strong observation to frame with an inversion ('Rarely…' or 'Not only…').",
        'task': "Two-minute keynote talk: 'One practical change that would strengthen education in my country.' "
                "Include at least one hedged claim, one cleft sentence, and one negative inversion, and finish with "
                "a clear, memorable call to action. Speak without reading from notes.",
        'model': "If we want to strengthen education across our country over the next decade, we must look first at "
                 "practical access. It is reliable internet connectivity in district schools that will determine who "
                 "benefits from modern learning tools. Rarely have we seen technology advance as rapidly in our major "
                 "cities as it has in recent years, yet students in smaller towns often study without updated textbooks "
                 "or digital libraries. Providing solar-powered digital libraries in district centres may well be the "
                 "most cost-effective educational investment of the decade. Studies suggest that when teachers can "
                 "share resources easily, classroom engagement rises within a single term. What our students need "
                 "most is not a more complicated syllabus, but equal access to the tools that already exist.",
        'feedback': [
            "uses hedging naturally to make predictions and claims sound credible",
            "uses at least one cleft sentence ('It is… that…' / 'What… is…') to spotlight the central priority",
            "uses one negative or limiting inversion accurately for rhetorical impact",
            "delivers a composed, persuasive two-minute talk with a strong closing line"
        ],
    },
    'review': {
        'points': [
            "Hedging ('may well', 'tend to', 'the evidence suggests', 'it could be argued') calibrates your claims to your evidence and builds credibility.",
            "Cleft sentences ('It was X that…', 'What matters most is…') and auxiliary 'do/did' act as vocal spotlights for key information.",
            "Negative or limiting openers ('Never', 'Rarely', 'Not only', 'Only after…') trigger auxiliary + subject inversion — use them sparingly for high impact."
        ],
        'retrieval': [
            "Take one prediction about your field of work or study and say it at three levels of certainty: 'will', 'may well', and 'might'.",
            "Say one 'What… is…' cleft sentence and one 'Not only did…' sentence from memory."
        ],
        'watch': [
            "'Never I have seen such a crowd.' → 'Never have I seen such a crowd.' (Invert the auxiliary before the subject after a negative opener.)",
            "Avoid stacking hedges ('It might possibly perhaps tend to…') or inverting every sentence — clarity and balance always come first."
        ],
        'selfcheck': [
            "I can soften sweeping claims using natural hedging expressions when the evidence is not absolute.",
            "I can spotlight my most important point using a cleft sentence or a well-placed inversion."
        ],
        'answers': {
            'A': ["Never", "did she pass", "did I understand", "suggests (or: suggest)", "the detailed budget", "tend"],
            'B': ["Online learning may well replace some traditional lectures, or tends to complement classroom study. (answers vary)",
                  "It was the practical examples that made the lesson easy to follow.",
                  "Rarely had we seen such rapid progress in a single term.",
                  "Never have I seen such a busy market.",
                  "answers vary (e.g. Teammate: 'Could I have two more days on the report?' / Director: 'I was wondering if it might be possible to extend the deadline by two days so we can verify the final figures.')",
                  "answers vary (e.g. 'Not only does my mentor listen patiently, but she also gives practical advice.')"],
        },
    },
}

L16 = {
    'n': 16, 'part_no': 8, 'part_title': 'Speak with Confidence',
    'title': 'Grammar in Real Conversation',
    'goal': 'bring all the course grammar together in free, accurate, confident speech',
    'intro': [
        "When a skilled musician walks onto the stage, they are no longer thinking about individual finger exercises "
        "— they are listening to the music and shaping the phrase. Speaking a language works the same way. Over the "
        "past fifteen lessons, you have built every core grammatical tool you need for real-world English.",
        "This final lesson is not about learning a brand-new rule. It is about seeing how all sixteen lessons fit "
        "together on one simple mental map, and mastering the habit that keeps confident speakers moving smoothly "
        "even when they slip: natural self-repair."
    ],
    'hook': [
        "Play a 60-second warm-up round with your partner:",
        "•  Partner A speaks for 45 seconds without stopping on 'One decision that taught me something important.'",
        "•  Partner B listens not only to the story, but also to the grammar tools Partner A uses naturally (tenses, conditionals, linkers, relative clauses, modals, or passives), and names at least three of them at the end. Then swap roles!",
    ],
    'rules': [
        {'label': 'Rule 1 — The whole course on one mental map: four jobs of spoken grammar',
         'text': [
             "Whenever you open your mouth to answer a complex question — in a university seminar, a job interview, "
             "a workplace meeting, or the TOEFL speaking test — you do not need to search through sixteen separate "
             "chapters in your head. Every grammar pattern in this book performs one of just four practical jobs:",
             "1. TIME (Lessons 1, 2, 13): placing events in the present, past, future, or reported speech.",
             "2. CHOICE & POSSIBILITY (Lessons 4, 5, 6, 11): expressing modals, conditionals, wishes, and verb patterns (-ing / to).",
             "3. SENTENCE SHAPE & FOCUS (Lessons 3, 8, 9, 10, 12, 14): asking questions, linking arguments, shifting focus with passives/causatives, and combining ideas with relative or participle clauses.",
             "4. TONE & PRECISION (Lessons 7, 15): comparing persuasively, hedging claims, and spotlighting key ideas with clefts or inversion."
         ],
         'formula': [
             "TIME:  tenses (L1) · narrative layers (L2) · reported speech (L13)",
             "CHOICE:  modals (L4) · conditionals (L5) · wishes & regrets (L6) · gerunds & infinitives (L11)",
             "SHAPE:  questions & follow-ups (L3) · linkers (L8) · passive (L9) · causative (L10) · relatives (L12) · participles (L14)",
             "STYLE:  comparisons (L7) · hedging, clefts & inversion (L15)"
         ],
         'examples': [
             "Story + reflection in four moves:  'Two years ago I was working at a small clinic (TIME — L2) when my mentor encouraged me to apply for a fellowship (TIME/CHOICE — L13/L11). Although the exam was far more demanding than I expected (SHAPE/STYLE — L8/L7), passing it changed my career — and if I hadn't taken that chance, I wouldn't be teaching here today (CHOICE — L5).'"
         ],
         'remember': [
             "Accuracy always comes before complexity: a clear, accurate sentence that fits your meaning beats a "
             "complicated structure forced into the wrong place."
         ]},
        {'label': 'Rule 2 — The three-step speaking habit and the art of self-repair',
         'text': [
             "Many learners think fluency means speaking fast without ever making a mistake. In reality, even native "
             "speakers and experienced professionals start sentences that head down a blind alley. The difference is "
             "that confident speakers do not freeze, apologize, or switch back to their first language — they use a "
             "smooth self-repair phrase ('What I mean is…', 'Or rather…', 'Let me put that another way…') and keep "
             "the message moving.",
             "In speaking assessments and professional life alike, catching and repairing a slip calmly is a sign of "
             "high linguistic control."
         ],
         'formula': [
             "The 3-step habit:  1. PICTURE the meaning  →  2. PICK the right tool (Time / Choice / Shape / Style)  →  3. SPEAK the chunk whole",
             "Natural self-repair phrases:  What I mean is …  ·  Or rather, …  ·  Let me rephrase that — …  ·  To put it more precisely, …"
         ],
         'examples': [
             "Repairing a tense slip mid-sentence: 'I have seen him yesterday — or rather, I saw him yesterday afternoon outside the library.'",
             "Repairing a conditional slip: 'If I would have known — sorry, if I had known about the traffic, I would have taken the train.'",
             "Sharpening an idea: 'The new schedule is better — or to put it more precisely, it gives working students far more flexibility.'"
         ],
         'remember': [
             "Never stop dead in silence when you notice a grammar slip. Either repair it in one smooth breath with "
             "'or rather…' or keep moving forward so your listener never loses the thread of your message."
         ]},
    ],
    'differences': [
        {'title': 'Freezing on a mistake vs repairing like a confident speaker',
         'text': [
             "Compare how two speakers handle the exact same mid-sentence grammar slip during a speaking task:"
         ],
         'rows': [
             ["'Despite of the rain… uh… no, wait… although rain… sorry, I forgot the word…'", "'Despite the heavy rain — or rather, although it was raining heavily — the outdoor concert went ahead.'", "Speaker A panics over a preposition and loses the listener. Speaker B pivots smoothly with 'or rather', repairs the structure in stride, and finishes the thought with authority."],
         ], 'headers': ['Freezing (loses fluency)', 'Natural self-repair (shows control)', 'Why the repair works']},
        {'title': 'Knowing a rule on paper vs owning it under real-time pressure',
         'text': [
             "You already recognize all sixteen grammar areas when you read them quietly. The four-round speaking "
             "workout below trains your brain to summon those same patterns on your feet while your attention is "
             "focused on communicating a real idea."
         ]},
    ],
    'practice_a': [
        "Repair the mistake and name the rule: 'I have finished my university degree in 2022.'",
        "Repair the mistake and name the rule: 'If the flight will be delayed tomorrow, we will call the hotel.'",
        "Repair the mistake in two ways (despite / although): 'Despite of the cold wind, we walked to the summit.'",
        "Repair the mistake and name the verb pattern: 'My supervisor suggested me to attend the workshop.'",
        "Repair the word order: 'Never I have felt so proud of our team.'",
        "Repair the verb form after 'to': 'We really look forward to host your delegation next month.'",
    ],
    'practice_b': [
        "Compress using a participle opening: 'Because he had not slept the night before, he made several small calculation errors.'",
        "Report this sentence in two ways (using 'told' and 'reassured'): '\"Don't worry about the deadline,\" she said to me.'",
        "Strengthen this flat comparison using 'far', a comparative, and a 'because' reason: 'Practising out loud is better than silent reading.'",
        "Rewrite as a formal passive announcement: 'The committee has changed tomorrow's examination schedule.'",
        "Hedge this sweeping claim so it sounds measured: 'This new teaching method is the best for every learner.'",
        "Turn this direct question into a polite indirect question: 'What time does tomorrow's rehearsal start?'",
    ],
    'pair': {
        'intro': "Run the 'Four-Round Conversation Circuit' with your partner. In each round, speak for one full "
                 "minute on the prompt while deliberately weaving in the target grammar family. Your partner listens, "
                 "asks one follow-up question, and notes which structures they heard.",
        'task': [
            "Round 1 — Story & Time (Lessons 1, 2, 14): Tell the story of a challenge or problem you overcame, using narrative tenses and one participle opening.",
            "Round 2 — Choice & Advice (Lessons 4, 5, 6): Advise a friend who is torn between two career paths or cities, using modals, conditionals, and 'If I were you / I'd rather'.",
            "Round 3 — Report & Focus (Lessons 9, 10, 12, 13): Summarize a recent change or conversation at school, work, or in your city, using passives, reporting verbs, and relative clauses.",
            "Round 4 — Persuade & Spotlight (Lessons 7, 8, 15): Argue for one practical improvement in your community, using comparisons, concession linkers, hedging, and a cleft sentence."
        ],
        'model': [
            "A (Round 4): Although expanding our public library hours would require extra staffing, it is by far the most helpful step we could take for students. What many learners lack at home is a quiet desk with reliable lighting...",
            "B: If the library stayed open until nine, how do you think students would manage transport home in winter?"
        ],
        'output': "Four one-minute rounds per pair: each round delivered without notes, with the "
                  "target structures counted aloud and at least one self-repair noted by the "
                  "listener.",
        'criteria': [
            "summons structures from the target grammar family naturally in each round",
            "uses self-repair phrases smoothly if a slip occurs rather than stopping",
            "connects ideas with clear signposts and reasons",
            "responds to the partner's follow-up question with confidence and accuracy"
        ],
    },
    'advanced': {
        'intro': "At your highest level of spoken control, different grammar families work together inside a single "
                 "breath — combining a conditional with reported speech, or opening an argument with an inversion and "
                 "closing it with a cleft.",
        'base': [
            "Go back to any earlier lesson where an exercise made you hesitate and speak those corrected sentences aloud three times without looking at the page.",
            "Create four personal anchor sentences — one each for Time, Choice, Shape, and Style — about your own life goals this year."
        ],
        'upgrade': [
            "Combine two course structures smoothly inside one sentence: 'Had I known that the application deadline had been brought forward, I would have had my transcripts translated a week earlier.'",
            "Pace your rhetorical style deliberately across a two-minute talk: open with a concrete story, hedge your central prediction, and land your conclusion with a crisp cleft sentence.",
            "Keep three natural self-repair and refinement phrases on the tip of your tongue: 'What I mean is…', 'Let me rephrase that…', and 'Or to put it more precisely…'."
        ],
    },
    'realtalk': {
        'plan': "Take one minute to plan your culminating two-minute talk on 'How my communication has changed — and "
                "where I am heading next.' Write down only three brief keyword lines: (1) Past story (where you started "
                "and what turning point changed your approach), (2) Present habits & choices (what you do differently "
                "now and why), and (3) Future goal (what you plan to achieve next and what it will take). Choose two "
                "precision structures (such as a mixed conditional, a non-defining relative clause, or a cleft) to weave in.",
        'task': "Two-minute culminating challenge: Speak for two minutes on 'How I have grown as a speaker — and what "
                "comes next.' Tell a concrete story from your past, explain a decision that helped you improve, and "
                "state your next goal, using structures from at least six different lessons in this course. Then "
                "exchange two follow-up questions with your partner — just as you will in the Final Speaking Assessment.",
        'model': "Two years ago, I used to avoid speaking English in group meetings because I was afraid of making "
                 "mistakes — while others were sharing their ideas, I would translate every sentence in my head until "
                 "the moment had passed. Joining a weekly speaking circle, which a colleague recommended to me, was "
                 "the turning point that changed that habit. Within a month, I had met partners who corrected me "
                 "encouragingly, and I realised that communication is about clarity, not perfection. Since then, I've "
                 "been practising aloud almost every day, and my supervisor has noticed the difference. Next spring "
                 "I'm going to take the TOEFL exam so that I can apply for a graduate programme. If I keep building "
                 "one small habit at a time, the score will take care of itself. What matters most to me now is "
                 "staying calm under pressure — and that comes only from using my voice every day.",
        'feedback': [
            "uses a wide range of course structures (at least six lessons represented) accurately and naturally",
            "moves smoothly from past narrative to present reflection to future goal",
            "includes at least one precision or emphasis structure (relative clause, conditional, hedge, or cleft)",
            "maintains confident, continuous delivery and handles follow-up questions or self-repair smoothly"
        ],
    },
    'review': {
        'points': [
            "All sixteen lessons serve four practical communication jobs: Time, Choice, Sentence Shape, and Style.",
            "Follow the three-step speaking habit: picture the meaning → pick the structure → speak the phrase whole.",
            "When you notice a slip in real conversation, use a natural repair phrase ('What I mean is…', 'Or rather…') and keep your message moving."
        ],
        'retrieval': [
            "Name the four communication jobs of grammar and give one example sentence of your own for each job.",
            "Speak for 60 seconds about a goal for next year, deliberately including one conditional, one relative clause, and one cleft sentence."
        ],
        'watch': [
            "Never sacrifice clarity just to show off a complicated structure — natural accuracy always comes first.",
            "Never freeze in silence after a small slip — repair calmly with 'or rather…' and continue."
        ],
        'selfcheck': [
            "I can combine grammar patterns from across the course naturally in a two-minute unscripted talk.",
            "I can answer unexpected follow-up questions and self-repair smoothly without losing confidence."
        ],
        'answers': {
            'A': ["I finished my university degree in 2022. ('in 2022' is a finished past time → past simple)",
                  "If the flight is delayed tomorrow, we will call the hotel. (ordinary future condition → present simple after 'if')",
                  "Despite the cold wind, we walked to the summit. / Although the wind was cold, we walked to the summit.",
                  "My supervisor suggested attending the workshop. / …suggested that I attend the workshop. ('suggest' takes -ing or a that-clause, never 'me to')",
                  "Never have I felt so proud of our team. (negative opener triggers auxiliary + subject inversion)",
                  "We really look forward to hosting your delegation next month. ('to' in 'look forward to' is a preposition → verb-ing)"],
            'B': ["Not having slept the night before, he made several small calculation errors.",
                  "She told me not to worry about the deadline. / She reassured me that I didn't need to worry about the deadline.",
                  "answers vary (e.g. 'Practising out loud is far more effective than silent reading because it trains your mouth and ear to work together in real time.')",
                  "Tomorrow's examination schedule has been changed (by the committee).",
                  "This new teaching method may well be one of the most effective for many learners. / This new teaching method tends to work very well for most learners. (answers vary)",
                  "Could you tell me what time tomorrow's rehearsal starts? / Do you know what time tomorrow's rehearsal starts?"],
        },
    },
}

LESSONS_13_16 = [L13, L14, L15, L16]


def render_all(doc, keys_registry):
    for L in LESSONS_13_16:
        render_lesson(doc, L, keys_registry)

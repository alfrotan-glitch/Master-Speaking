# -*- coding: utf-8 -*-
"""Lessons 1-4 — Part One: Build Strong Sentences; Part Two: Express Ideas Clearly."""
from lesson_template import render_lesson

L1 = {
    'n': 1, 'part_no': 1, 'part_title': 'Build Strong Sentences',
    'title': 'Tenses for Real Communication',
    'goal': 'talk about habits, experiences and changes accurately',
    'intro': [
        "Imagine two candidates in a job interview. The first says, 'I worked at a city clinic for three years.' "
        "The second says, 'I have worked at a city clinic for three years.' Only one small word changed, yet the "
        "interviewer hears two completely different life stories: the first person no longer works there, while "
        "the second still walks through those clinic doors every morning.",
        "Tenses are not a chart of endings to memorise for a test. They are the camera lens you choose every time "
        "you open your mouth — telling your listener whether something is a permanent routine, a temporary project, "
        "a closed chapter in the past, or a change that still shapes your life today."
    ],
    'hook': [
        "Read these two pairs of sentences aloud with a partner:",
        "•  'I live with my cousin.'   vs.   'I'm living with my cousin until my flat is ready.'",
        "•  'I lost my keys yesterday.'   vs.   'I've lost my keys — can you let me in?'",
        "Without using grammar terms, explain to your partner what changes in the real-world situation between "
        "the left sentence and the right sentence. Then take one minute each to answer:",
        "•  What does a normal weekday look like for you, and what is one temporary project you are working on this month?",
        "•  What is one important thing that has changed in your daily life over the past year?",
    ],
    'rules': [
        {'label': 'Rule 1 — Present tenses: habits, facts and what is happening now',
         'text': [
             "When you talk about the present, English asks a simple question: are you describing your normal "
             "baseline, or are you shining a spotlight on something temporary happening around now?",
             "Use the present simple for your baseline — habits, routines, permanent facts, fixed timetables, "
             "and mental states. Use the present continuous when an action is in progress right now, when a project "
             "is temporary around this period of your life, or when a situation is gradually changing."
         ],
         'formula': [
             "Present simple:  Subject + base verb (+ s/es for he/she/it)  →  habits · facts · fixed timetables · states",
             "Present continuous:  Subject + am/is/are + verb-ing  →  happening now · current projects · temporary situations · changing trends"
         ],
         'examples': [
             "I work in a medical clinic, and our morning shift starts at eight.  (permanent routine and fixed timetable)",
             "I'm working on my pronunciation this month by recording myself for five minutes a day.  (temporary current project)",
             "More professionals are learning English online every year.  (an ongoing trend)",
             "I know the answer, and I believe your plan will work.  (mental states stay in the present simple)"
         ],
         'remember': [
             "Add -s or -es with he, she, and it in the present simple: he works, she studies, it matters.",
             "Stative verbs describe a state rather than an active process (know, believe, understand, own, belong, seem, prefer). "
             "They normally stay in the simple form: say 'I understand the problem' (not 'I am understanding')."
         ]},
        {'label': 'Rule 2 — Past simple vs present perfect: closed time vs connected to now',
         'text': [
             "Many speakers hesitate between 'I did' and 'I have done' because both refer to something that happened "
             "before now. The real difference is not how long ago the event happened — it is whether the time period "
             "is closed or still connected to the present.",
             "Use the past simple when you name or think of a finished time period (yesterday, last summer, in 2020, "
             "when I was a student). That chapter is closed. Use the present perfect when the time period is still open "
             "(today, this week, so far this year), when a past event has a clear result right now, or when a situation "
             "began in the past and continues up to today (often with since or for). 'Recently' can take either tense, "
             "depending on the time focus and variety of English."
         ],
         'formula': [
             "Past simple:  Subject + past verb (verb-ed / irregular)  →  a finished, closed time in the past",
             "Present perfect:  Subject + have/has + past participle  →  open time period · life experience · present result · continuing to now"
         ],
         'examples': [
             "I visited Bamyan last summer with my classmates.  (finished time: 'last summer' is over)",
             "I have visited Bamyan twice in my life.  (life experience up to now — no finished time is named)",
             "Nadia has lived in this neighbourhood since 2021.  (she moved here in 2021 and still lives here today)",
             "I've sent the application, so we can relax now.  (past action with a direct present result)"
         ],
         'remember': [
             "Once you attach a finished time stamp (yesterday, two days ago, in 2019), close the door with the past simple: "
             "'I saw him yesterday' (never 'I have seen him yesterday').",
             "With 'recently', either tense can be natural: 'I've spoken to her recently' (focusing on the recent link to now) "
             "or 'I spoke to her recently' (thinking of that specific recent occasion)."
         ]},
        {'label': 'Rule 3 — Talking about changes and the future',
         'text': [
             "English does not have just one future tense because we do not think about every future event in the same way. "
             "Whenever you talk about tomorrow or next year, you are showing your listener how prepared that future is.",
             "Choose 'be going to + base verb' when you have already made a decision or plan before speaking, or when "
             "you can see clear present evidence of what is about to happen. Choose 'will + base verb' when you make an "
             "instant decision while speaking, make a promise, or state a general prediction. Choose the present continuous "
             "(with a future time expression) when you have a fixed arrangement with another person or organisation."
         ],
         'formula': [
             "am/is/are going to + base verb  →  prior plans and intentions · predictions from visible evidence",
             "will + base verb  →  decisions made while speaking · promises and offers · general predictions",
             "Present continuous + future time word  →  fixed personal arrangements already on the calendar"
         ],
         'examples': [
             "I'm going to take the TOEFL exam next spring — I've already bought the study guide.  (decided plan)",
             "Those bags look heavy — I'll carry one for you.  (instant offer made at the moment of speaking)",
             "We're meeting the new instructor on Thursday at ten.  (fixed arrangement with a specific time)"
         ],
         'remember': [
             "In future time and condition clauses starting with if, when, as soon as, before, or after, use the present simple: "
             "'When the results arrive, I'll call you' and 'If it rains tomorrow, we'll stay indoors.'"
         ]},
    ],
    'differences': [
        {'title': 'Present perfect vs past simple — the choice is about TIME',
         'text': [
             "Look at how the same verb changes meaning when you shift from the past simple to the present perfect. "
             "In each pair below, ask yourself: is the speaker looking back at a finished moment, or looking at how "
             "the past touches right now?"
         ],
         'rows': [
             ["I lost my keys yesterday.", "I've lost my keys.", "The left sentence reports when it happened (perhaps I found them later). The right sentence is about right now: I am standing outside the door and cannot get in."],
             ["She worked at the hospital for five years.", "She has worked at the hospital for five years.", "Past simple means her five-year period is finished — she works somewhere else now. Present perfect means she started five years ago and still works there."],
             ["Did you eat breakfast this morning?", "Have you eaten breakfast this morning?", "We ask 'Did you eat?' when the morning is over. We ask 'Have you eaten?' while it is still morning and there is still time to make you some toast."],
         ], 'headers': ['Past simple (closed past time)', 'Present perfect (connected to now)', 'What your listener hears']},
        {'title': 'State verbs vs action verbs — when a verb changes its job',
         'text': [
             "Most state verbs (know, believe, understand, belong, own, seem, prefer) describe a steady condition, "
             "so they stay in the simple form: 'I understand the rule' — never 'I am understanding the rule.'",
             "However, a few everyday verbs have two meanings: a state meaning (simple) and an active meaning (continuous). "
             "Compare: 'I think this course is practical' (my opinion — state) versus 'I'm thinking about applying for a scholarship' "
             "(an active mental process happening right now). Likewise, 'She has a small car' (ownership) versus "
             "'She's having lunch with her supervisor' (an action in progress)."
         ]},
    ],
    'practice_a': [
        "I __________ (see) that documentary last week, and we talked about it for hours.",
        "Nadia __________ (work) at the children's hospital since 2022.",
        "We __________ (meet) the new course director tomorrow morning at ten.  (fixed arrangement)",
        "Look out of the window — it __________ (snow)!",
        "My older brother __________ (believe) that consistent daily practice beats last-minute cramming.",
    ],
    'practice_b': [
        "Correct the mistake and explain why: 'I have finished my assignment last night.'",
        "Correct the mistake and explain why: 'She is knowing three foreign languages.'",
        "Choose the natural form: How long (do you know / have you known) your closest friend, Sara?",
        "Rewrite using going to so it sounds like a decided plan: 'My intention is to study medicine next year.'",
    ],
    'pair': {
        'intro': "Interview your partner using the four questions below. Do not treat this as a checklist — "
                 "listen closely to the details in every answer and ask at least one natural follow-up question "
                 "before moving to the next prompt.",
        'task': [
            "What does a typical weekend look like for you when you have no urgent deadlines?",
            "What is something new or different you are doing these days that was not part of your routine six months ago?",
            "What was the best part of your last weekend, and who were you with?",
            "What has changed most in your work, studies, or daily habits since last year?"
        ],
        'model': [
            "A: What are you doing these days that wasn't part of your routine six months ago?",
            "B: I'm walking to class every morning instead of taking the bus. It takes forty minutes, so I listen to English podcasts on the way.",
            "A: That's a great habit. How long have you been doing that, and have you noticed a difference in your listening?"
        ],
        'output': "Both partners answer all four questions, exchange at least four follow-up questions in "
                  "total, and can report one interesting answer about the other person to the class.",
        'criteria': [
            "uses present simple for regular habits and routines",
            "uses present continuous for current projects and temporary changes",
            "uses past simple for finished past moments and present perfect for changes continuing to now",
            "asks natural follow-up questions that react to what the partner actually said"
        ],
    },
    'advanced': {
        'intro': "Once your tense choices are accurate, you can express richer shades of time by showing "
                 "continuous effort, contrasting past setbacks with present growth, or highlighting a milestone.",
        'base': [
            "Link every time expression directly to its natural tense: finished markers (yesterday, two weeks ago, in 2020) "
            "close the action in the past simple; open bridges (since 2021, for three months, so far this week) connect to now with the present perfect.",
            "Say three true sentences about your own week aloud: one permanent habit, one temporary project you are doing this month, and one experience you have had this year."
        ],
        'upgrade': [
            "Use the present perfect continuous (have/has been + verb-ing) when you want to emphasise the ongoing effort or visible effect of an activity: 'I've been revising all morning, so my eyes are tired.'",
            "Combine past simple and present perfect in a single sentence to show growth from a past event: 'I failed the driving test twice last year, but I've learned from both mistakes and I feel ready now.'",
            "Use milestone frames such as 'It's the first time I've ever…' or 'This is the most challenging project I've worked on' to highlight a standout experience."
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to jot down three keywords only (do not write full sentences): one past turning point "
                "(past simple), one change that has happened up to now (present perfect), and one habit or focus you "
                "are working on these days (present simple / continuous).",
        'task': "Speak for one full minute: How has your English — or another practical skill you value — improved over time? "
                "Name one specific past moment that helped you, explain what has changed since then, and describe what you "
                "are actively working on right now.",
        'model': "I've been studying English seriously for about two years. Last year I joined a weekly speaking club, "
                 "and that was the moment things really changed for me — I learned to respond in English right away instead "
                 "of translating every word in my head. Since then, my confidence has grown a lot, and I've spoken in front "
                 "of visitors twice at work. These days I listen to a short news podcast every morning while I walk, and "
                 "I'm focusing on making my pronunciation clearer.",
        'feedback': [
            "past simple used for the specific turning-point event",
            "present perfect used for progress and changes up to now",
            "present continuous used for what the speaker is focusing on these days",
            "time expressions match the chosen tenses naturally (last year, since then, these days)"
        ],
    },
    'review': {
        'points': [
            "Present simple describes your permanent baseline (habits, facts, states); present continuous spotlights what is in progress or temporary around now.",
            "Past simple closes the door on a finished time (yesterday, in 2020); present perfect connects the past to the present moment.",
            "For the future, use 'going to' for decided plans, 'will' for spontaneous decisions and predictions, and the present continuous for fixed arrangements."
        ],
        'retrieval': [
            "Describe your last weekend in four connected past-simple sentences, then add one sentence in the present perfect about how your week has gone so far.",
            "Explain three things that have changed in your town, work, or studies since 2020."
        ],
        'watch': [
            "'I have seen him yesterday.' → 'I saw him yesterday.' (A finished time stamp requires the past simple.)",
            "'I am knowing the answer.' → 'I know the answer.' (State verbs stay in the simple form.)"
        ],
        'selfcheck': [
            "I can talk about a routine, a current project, and a past experience in one smooth answer.",
            "I can hear the difference between a finished past event and a situation that continues up to now."
        ],
        'answers': {
            'A': ["saw", "has worked / has been working", "are meeting", "is snowing", "believes"],
            'B': ["I finished my assignment last night. ('last night' is a finished time)",
                  "She knows three foreign languages. ('know' is a state verb)",
                  "have you known",
                  "I'm going to study medicine next year."],
        },
    },
}

L2 = {
    'n': 2, 'part_no': 1, 'part_title': 'Build Strong Sentences',
    'title': 'Telling Stories and Describing Experiences',
    'goal': 'tell a story with background, sequence and clear focus',
    'intro': [
        "Have you ever listened to someone tell a story that sounded like a flat shopping list? 'I woke up late. "
        "I ran outside. It rained. I missed the bus. My phone died.' Every sentence is grammatically correct, yet "
        "the story feels lifeless because every action is painted on the exact same flat surface.",
        "Skilled storytellers use grammar like a film director uses cameras. One tense paints the atmosphere in the "
        "background, another drives the main events forward step by step, and a third flashes back to something that "
        "had already happened before the scene began."
    ],
    'hook': [
        "Compare these two openings to the same story:",
        "•  Version A:  'I walked home from work. The lights went out. I realized my keys were on my office desk.'",
        "•  Version B:  'I was walking home from work when the street lights suddenly went out — and that was the moment I realized I had left my keys on my office desk.'",
        "Read both versions aloud with a partner. Why does Version B pull the listener in? Then take 30 seconds each "
        "to tell a brief true story about a small surprise, delay, or lucky moment from your own life.",
    ],
    'rules': [
        {'label': 'Rule 1 — Past continuous: painting the background scene',
         'text': [
             "Before an audience cares about what happened, they need to see where you were and what was going on around "
             "you. That is the job of the past continuous (was/were + verb-ing).",
             "Think of the past continuous as a wide-angle background shot that is already rolling when a sudden, "
             "shorter action (in the past simple) steps into the frame: 'I was waiting at the pharmacy when my old "
             "teacher walked in.' The waiting was already in progress; the entrance interrupted or punctuated it."
         ],
         'formula': [
             "Past continuous:  Subject + was/were + verb-ing  →  ongoing background scene · action in progress at a past moment",
             "Scene + interruption:  While + past continuous, past simple   /   Past continuous + when + past simple"
         ],
         'examples': [
             "I was walking across the campus when I ran into an old classmate.",
             "A cold wind was blowing and shopkeepers were closing their shutters as we reached the market.",
             "While I was preparing the slides, the projector suddenly stopped working."
         ],
         'remember': [
             "Use 'while' before the ongoing background action (past continuous) and 'when' before the shorter interrupting event (past simple): "
             "'While I was cooking dinner, the lights went out' / 'I was cooking dinner when the lights went out.'"
         ]},
        {'label': 'Rule 2 — Past perfect: stepping one level further back',
         'text': [
             "Stories do not always unfold in strict 1–2–3 calendar order. Often you start your story at an exciting "
             "moment — arriving at the airport gate, opening an exam paper, meeting someone — and then you need to "
             "point back to something that happened earlier.",
             "If you keep using the past simple, your listener thinks the events happened one after another ('When I "
             "arrived, he left' means my arrival caused him to walk out). When you switch to the past perfect (had + past "
             "participle), you signal a flashback: 'When I arrived, he had already left' (the room was already empty when I got there)."
         ],
         'formula': [
             "Past perfect:  Subject + had + past participle  →  an action completed before another past moment"
         ],
         'examples': [
             "By the time we reached the cinema, the film had already started.",
             "She looked relieved because she had finally submitted her thesis.",
             "I recognized the street immediately because I had visited the neighbourhood years earlier."
         ],
         'remember': [
             "Do not overuse the past perfect for every sentence in a story. Use it only when you jump backwards from "
             "your main past storyline to an earlier event: 'By the time the taxi arrived (main past), we had packed everything (earlier past).'"
         ]},
        {'label': 'Rule 3 — Signposting the sequence and landing the ending',
         'text': [
             "In written English, paragraphs show the reader how a story is organized. In spoken English, your listener "
             "cannot see paragraphs — your sequence phrases are their only map.",
             "Clear time signposts (At first, A few minutes later, Suddenly, By the time, In the end) guide the listener "
             "from the opening scene to the turning point, and a final reflection shows why the experience mattered."
         ],
         'formula': [
             "Opening & sequence:  At first …  ·  A moment later …  ·  After that …  ·  All of a sudden …  ·  Finally …",
             "Tight time links:  Earlier that morning …  ·  By the time …  ·  As soon as …"
         ],
         'examples': [
             "At first, everyone at the table stayed quiet. Then, all of a sudden, my grandfather started laughing.",
             "As soon as I opened the envelope, I knew the hard work had paid off.",
             "Looking back, that mistake taught me to check the schedule twice."
         ],
         'remember': [
             "'As soon as' shows that the second action happened immediately after the first, with no gap in between."
         ]},
    ],
    'differences': [
        {'title': 'Three camera angles in the past: event vs scene vs earlier flashback',
         'text': [
             "Notice how changing the tense in the second clause completely changes the timeline of the meal in these three sentences:"
         ],
         'rows': [
             ["When my sister arrived, I cooked dinner.", "When my sister arrived, I was cooking dinner.", "When my sister arrived, I had cooked dinner.", "1. Past simple: she arrived first, and then I started cooking.  2. Past continuous: I was in the middle of cooking when she walked in.  3. Past perfect: the food was already cooked and waiting on the table before she arrived."],
             ["He took a taxi when the rain started.", "He was taking a taxi when the rain started.", "He had taken a taxi before the rain started.", "Each tense places his ride at a different point relative to the rain: after it started, during it, or before it."],
         ], 'headers': ['Past simple (next event)', 'Past continuous (in progress)', 'Past perfect (already finished)', 'How the timeline changes']},
        {'title': 'The three-part architecture of a memorable spoken story',
         'text': [
             "When you tell an anecdote in conversation or in a speaking exam, give it a clear three-part shape: "
             "1. Set the scene (past continuous: where you were, what was happening). "
             "2. Tell the key events in order, flashing back only when needed (past simple + past perfect). "
             "3. Land the ending with what changed or what you learned (past simple or present perfect): "
             "'It was pouring with rain… I slipped on the steps because I had rushed out in smooth shoes… I've checked the weather before leaving the house ever since.'"
         ]},
    ],
    'practice_a': [
        "While I __________ (study) for the final exam, the electricity suddenly went off.",
        "We __________ (already / eat) dinner by the time our cousins arrived.",
        "First, I __________ (call) the clinic, and then I __________ (take) a taxi across town.",
        "She __________ (walk) along the riverbank when she __________ (see) smoke rising from the warehouse.",
        "By 2019, he __________ (finish) his engineering degree and started his first job.",
        "The children __________ (play) in the courtyard while their mother __________ (rest) indoors.",
    ],
    'practice_b': [
        "Combine into one sentence using while: 'I read the contract. The office printer jammed.'",
        "Combine using by the time and the past perfect: 'We reached the station. The train left.'",
        "Correct the timeline mistake: 'When I arrived at the hall, the speaker already left.'",
        "Use sequence signposts (At first, Suddenly, In the end) to tell a three-sentence story about nearly missing a bus or flight.",
        "Choose the natural connector: The doorbell rang (while / when) I was drying my hair.",
        "Rewrite this flat list as a vivid two-sentence story scene using past continuous and past perfect: 'It rained hard. I forgot my umbrella at work. I got soaked.'",
    ],
    'pair': {
        'intro': "Take turns telling a two-minute true story from your own life. While you listen to your partner, "
                 "picture the scene and prepare two genuine follow-up questions about details that make you curious.",
        'task': [
            "Choose one prompt: a journey you still remember clearly · a day when plans went wrong in an unexpected way · an important decision you had to make quickly.",
            "Include all three story layers: a clear opening scene (past continuous), at least one earlier detail that had happened before the main moment (past perfect), and a closing line that explains why the moment mattered."
        ],
        'model': [
            "A: It was a cold Tuesday morning in January, and I was waiting for a shared taxi outside the university. I had stayed up until two in the morning finishing my project, so I was half asleep...",
            "B: Oh no — did you make it to the presentation on time, or had the professor already started when you walked in?"
        ],
        'output': "Each partner tells a two-minute story that the other can retell in three sentences, "
                  "and asks two genuine follow-up questions about it.",
        'criteria': [
            "opens with a clear background scene using the past continuous",
            "guides the listener with natural sequence signposts",
            "uses the past perfect accurately to mark an earlier action",
            "ends with a clear reflection on why the experience mattered"
        ],
    },
    'advanced': {
        'intro': "Once your three basic narrative tenses work smoothly together, you can add texture to your "
                 "storytelling by showing repeated past routines, highlighting how long an earlier activity had "
                 "been going on, and connecting a past story to who you are today.",
        'base': [
            "Before you start speaking, picture the three layers of your story: what was happening in the background (was/were + -ing), what happened next (past simple), and what had already happened earlier (had + past participle).",
            "Practise telling a compact 30-second anecdote aloud that includes one 'while', one 'when', and one 'by the time'."
        ],
        'upgrade': [
            "Use 'would + base verb' (or 'used to') to paint nostalgia or repeated past habits at the start of a story: 'On summer evenings in my hometown, we would sit in the orchard and listen to my uncle's stories.'",
            "Use the past perfect continuous (had been + verb-ing) to show how long an activity had been in progress before the turning point: 'We had been waiting in the rain for forty minutes when the bus finally appeared.'",
            "Close your story by bridging back to the present with the present perfect: 'That afternoon taught me a lesson I've never forgotten.'"
        ],
    },
    'realtalk': {
        'plan': "Take ten seconds of silent mental planning (write nothing down): picture your opening background "
                "scene, the two main events in order, one earlier detail that explains why it happened (had + participle), "
                "and your closing reflection.",
        'task': "Tell a two-minute story about a memorable day in your life — a small crisis, an unexpected kindness, "
                "or a lucky break. After your partner gives feedback, switch partners and tell the same story a second "
                "time, making the sequence and ending even sharper.",
        'model': "It was a Friday afternoon in May. I was walking home from the bookshop when I suddenly realised I had "
                 "left my phone on the counter — I had only been walking for ten minutes, so I turned back at once. "
                 "At first I checked my coat pockets twice; then I hurried back down the street. By the time I reached "
                 "the shop, the owner had already answered a call from my cousin: he had won two tickets to the championship "
                 "final and needed my answer straight away. I called him back from the shop counter, and we went to the "
                 "stadium that evening. I've checked my pockets before leaving every shop ever since.",
        'feedback': [
            "clear three-part story shape (background scene → main events → closing reflection)",
            "natural sequence signposts (at first, then, by the time, in the end)",
            "past continuous and past perfect used accurately to separate time layers",
            "the listener can easily retell the main events in the right order"
        ],
    },
    'review': {
        'points': [
            "Past continuous paints the background scene in progress; past simple moves the main events forward; past perfect flashes back to an earlier past action.",
            "Sequence signposts (at first, suddenly, by the time, as soon as) keep your listener oriented.",
            "Strong spoken stories end by showing what changed or what the speaker learned."
        ],
        'retrieval': [
            "Tell a 30-second true or invented story aloud that uses both 'while' and 'by the time'.",
            "Name the three layers of a well-structured story and give one example sentence for each."
        ],
        'watch': [
            "'When I arrived, he left.' (means he left after I arrived) → 'When I arrived, he had already left.' (means he was gone before I arrived).",
            "'While I was walking, I had seen an old friend.' → 'While I was walking, I saw an old friend.' (Use past simple, not past perfect, for the main interrupting event.)"
        ],
        'selfcheck': [
            "My spoken stories have a clear background scene, logical sequence, and meaningful ending.",
            "I can use the past perfect naturally to show which of two past actions happened first."
        ],
        'answers': {
            'A': ["was studying", "had already eaten", "called / took", "was walking / saw",
                  "had finished", "were playing / was resting"],
            'B': ["While I was reading the contract, the office printer jammed.",
                  "By the time we reached the station, the train had left.",
                  "When I arrived at the hall, the speaker had already left.",
                  "answers vary",
                  "while",
                  "It was raining hard, and because I had forgotten my umbrella at work, I got soaked. (answers vary)"],
        },
    },
}

L3 = {
    'n': 3, 'part_no': 2, 'part_title': 'Express Ideas Clearly',
    'title': 'Questions, Auxiliary Verbs, and Follow-up Questions',
    'goal': 'ask clear questions and keep a conversation alive',
    'intro': [
        "Why do some English conversations feel effortless while others feel like a stiff border-control interview? "
        "Usually it comes down to how people ask questions. When a speaker drops auxiliary verbs, uses direct "
        "interrogation word order with strangers, or jumps from one unrelated topic to the next, the conversation "
        "stalls.",
        "When you master three habits — clean question word order, polite indirect openings, and follow-up questions "
        "that build on what the other person just said — you can keep any conversation alive and make the other "
        "person feel genuinely heard."
    ],
    'hook': [
        "Compare these two short exchanges:",
        "•  Exchange 1:   A: 'Where you work?'   B: 'At a bank.'   A: 'What is your favourite food?'",
        "•  Exchange 2:   A: 'What kind of work do you do?'   B: 'I work at a bank.'   A: 'Really? What part of banking do you focus on?'",
        "With a partner, find out three things about each other: their favourite way to unwind after a busy week, "
        "something they are trying to learn this year, and one place they hope to visit. Rule for this warm-up: "
        "after every answer, you must ask ONE follow-up question about what your partner just said before changing the subject.",
    ],
    'rules': [
        {'label': 'Rule 1 — Forming direct questions: auxiliaries and the subject-question exception',
         'text': [
             "Most direct English questions put an auxiliary verb (do, does, did, am, is, are, have, has, will, can, "
             "should) in front of the subject: 'Where do you live?' or 'Have you finished the report?' Once 'do', "
             "'does', or 'did' carries the tense, the main verb returns to its base form: 'Did she call?' (never 'Did she called?').",
             "There is one crucial exception that trips up even experienced speakers: when the question word itself "
             "(Who, What, Which) is the subject of the verb, there is no inversion and no 'do/did'. Compare: 'Who called you?' "
             "(Someone called you — 'Who' is the subject) versus 'Who did you call?' (You called someone — 'you' is the subject)."
         ],
         'formula': [
             "Yes/No question:  Auxiliary + subject + main verb …?   →   Do you agree?  ·  Have they arrived?",
             "Wh- object question:  Wh- word + auxiliary + subject + main verb …?   →   Where did she go?",
             "Subject question (Who/What = subject):  Wh- subject + verb …?   →   Who wrote this?  ·  What happened?"
         ],
         'examples': [
             "Where do you usually study in the evenings?",
             "Did the coordinator send the new timetable yesterday?  (base verb 'send' after 'did')",
             "What happened at the end of the meeting?  ('What' is the subject — no 'did')",
             "Who organised the workshop, and who did you invite to speak?  (subject question vs object question)"
         ],
         'remember': [
             "After do, does, or did, always use the base verb: 'Where did you buy that?' (not 'Where did you bought that?').",
             "Test whether Who or What is the subject by answering the question in your head: 'Who broke the cup?' → 'Ali broke it' (subject = no 'did')."
         ]},
        {'label': 'Rule 2 — Polite indirect questions: softening the approach',
         'text': [
             "Walking up to a professor, a client, or a stranger and asking 'Where is the office?' or 'How much does "
             "this cost?' is grammatically correct, but it can sound abrupt. To sound polite and composed, English speakers "
             "wrap the question inside a soft opening phrase such as 'Could you tell me…?' or 'Do you know…?'",
             "Here is the golden rule of indirect questions: the opening phrase already does the work of asking the "
             "question, so the second half switches back to normal statement word order (subject + verb) and drops "
             "'do/does/did'."
         ],
         'formula': [
             "Direct question:  Wh- word + auxiliary + subject + verb?   →   Where is the bank?  /  When did he leave?",
             "Indirect question:  Polite opener + Wh- word (or if/whether) + subject + verb   →   Could you tell me where the bank is?  /  Do you know when he left?"
         ],
         'examples': [
             "Could you tell me where the registration desk is?",
             "Do you happen to know what time the library closes on Fridays?",
             "I'd like to know when the interview results will be announced.",
             "I was wondering if you could look over my draft this afternoon."
         ],
         'remember': [
             "Never invert twice! Say 'Do you know where the bank is?' (not 'Do you know where is the bank?').",
             "For Yes/No indirect questions, connect with 'if' or 'whether': 'Do you know if the bus has left?'"
         ]},
        {'label': 'Rule 3 — Follow-up questions: the engine of real conversation',
         'text': [
             "Good conversationalists do not memorize a list of twenty questions. Instead, they ask one clear opening "
             "question, listen for an interesting word or feeling in the answer, and ask a follow-up question about "
             "that exact detail.",
             "Content follow-ups show your partner that you are actually listening to their story, not just waiting "
             "for your turn to talk."
         ],
         'formula': [
             "Quick reactions + follow-ups:  Really? What happened next?  ·  How did you decide to do that?",
             "Digging deeper:  You mentioned it was challenging — which part was hardest?  ·  What would you do differently next time?"
         ],
         'examples': [
             "A: I switched from engineering to teaching last year.   B: That's a big step — what made you decide to change?",
             "A: I took the speaking test twice before I got the score I needed.   B: What did you change between the first attempt and the second?"
         ],
         'remember': [
             "Build your follow-up from the content of your partner's sentence rather than switching topics: "
             "echo one key idea they mentioned and ask 'Why?', 'How?', or 'What was that like?'"
         ]},
    ],
    'differences': [
        {'title': 'Direct vs polite indirect questions in the same situation',
         'text': [
             "Notice two changes when you move from the direct column to the polite column: the tone becomes much "
             "more respectful, and the verb moves back after the subject."
         ],
         'rows': [
             ["Where did you buy that dictionary?", "Could you tell me where you bought that dictionary?", "After 'Could you tell me where', we drop 'did' and put the past tense back on the verb ('you bought')."],
             ["What time does the clinic open?", "Do you know what time the clinic opens?", "After 'Do you know what time', we drop 'does' and use statement order ('the clinic opens')."],
             ["Why was the flight delayed?", "Would you mind telling me why the flight was delayed?", "The auxiliary 'was' moves after 'the flight' so the embedded clause reads like a statement."],
         ], 'headers': ['Direct (quick / casual)', 'Indirect (polite / professional)', 'What changes in the grammar']},
        {'title': 'Subject questions vs object questions — why "Who" works two ways',
         'text': [
             "Compare two questions about the same phone call: suppose Mariam called Tariq.",
             "•  If we ask 'Who called Tariq?', the answer is Mariam (the subject). Because 'Who' stands in the subject's shoes, the verb follows directly: 'Who called Tariq?'",
             "•  If we ask 'Who did Mariam call?', the answer is Tariq (the object), and Mariam is the subject. Because 'Mariam' is the subject, we need the auxiliary 'did' before her name: 'Who did Mariam call?'"
         ]},
    ],
    'practice_a': [
        "__________ you ever __________ (try) traditional Kabuli palaw cooked over wood fire?",
        "What __________ (happen) at the end of the department meeting yesterday?",
        "Do you know where __________ ?  (the main library / be)",
        "Could you tell me how much this course __________ ?  (cost)",
        "Who __________ (write) this summary on the board?",
        "Who __________ you __________ (speak) to at the admissions office yesterday?",
    ],
    'practice_b': [
        "Make this question polite for a stranger: 'Where did you park your car?'",
        "Make this question polite for an administrator: 'When will the exam results be ready?'",
        "Correct the word-order mistake: 'Do you know where is the nearest pharmacy?'",
        "Write two natural content follow-up questions for a partner who says: 'I'm planning to change careers next year.'",
        "Correct the verb mistake: 'Did she called you after the interview?'",
        "Write one question starting with 'How long…' to ask a classmate about a skill or hobby they have.",
    ],
    'pair': {
        'intro': "Run a three-minute conversational interview with your partner. Partner A starts by asking about "
                 "one of the topics below, but every conversation must stay on that single topic for at least three "
                 "follow-up exchanges before moving on. Then swap roles.",
        'task': [
            "Choose three topics from: learning English · a moment you felt proud of your work · a difficult decision you had to make · a plan for the next two years.",
            "Each partner must use at least one polite indirect question ('Could you tell me…', 'I was wondering…') and at least three content-based follow-up questions."
        ],
        'model': [
            "A: I was wondering what your biggest goal is for the next year.",
            "B: I'm hoping to apply for a master's programme abroad.",
            "A: Really? Do you know which university you want to apply to, or are you still comparing options?"
        ],
        'output': "A three-minute exchange per pair in each role: three answers, at least three "
                  "content-based follow-ups, one indirect question — then a one-sentence summary of "
                  "what you learned about your partner.",
        'criteria': [
            "question word order is accurate in both direct and indirect questions",
            "follow-up questions build directly on details the partner just shared",
            "the conversation flows naturally without abrupt topic jumps",
            "both partners speak and ask questions in balanced measure"
        ],
    },
    'advanced': {
        'intro': "In real conversation, questions do more than request missing facts — they also express surprise, "
                 "check shared understanding, and invite agreement.",
        'base': [
            "Contrast direct and embedded order aloud until your ear catches inversion errors automatically: 'Where did you go?' versus 'Do you know where you went?'",
            "Keep five polite openers ready for formal and professional situations: 'Could you tell me…', 'Do you happen to know…', 'Would you mind telling me…', 'I was wondering if…', 'Do you have any idea…'"
        ],
        'upgrade': [
            "Use negative questions to express surprise or polite expectation: 'Haven't we met before?' or 'Didn't you receive the schedule I sent?'",
            "Use short echo questions when a detail surprises you and you want the speaker to elaborate: 'You waited how many hours at the airport?'",
            "Use natural question tags with falling intonation to invite agreement and keep the listener engaged: 'It's been a busy week, hasn't it?' · 'You've worked with Dr Rahimi before, haven't you?'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to prepare: write down one single-sentence story opener of your own (for example, "
                "'I almost missed an important flight last year' or 'I tried cooking for twenty guests last month'), "
                "plus two polite indirect question frames you can use during the conversation.",
        'task': "Two-minute conversation challenge: Partner A says only their one-sentence opener. Partner B must "
                "keep the conversation going for two full minutes by asking natural follow-up questions, reacting "
                "genuinely, and using at least one indirect question — while Partner A answers naturally and asks "
                "questions back.",
        'model': "A: I almost missed my flight last week.\n"
                 "B: Really? What happened?\n"
                 "A: The main road to the airport was closed, so I reached the check-in desk twenty minutes before boarding. "
                 "Do you travel often, or do you prefer staying close to home?\n"
                 "B: I fly for work a few times a year. Could you tell me how you managed to get through security in time?\n"
                 "A: One of the staff saw my boarding pass and took me to the front of the queue. Have you ever missed a connection?\n"
                 "B: Not a flight, but I missed the last bus from Herat once. How did you feel when you finally sat down on the plane?",
        'feedback': [
            "asks genuine follow-up questions that react to content rather than switching topics",
            "uses at least one polite indirect question with statement word order",
            "maintains accurate auxiliary and subject-question grammar throughout",
            "keeps the two-minute exchange lively and balanced from start to finish"
        ],
    },
    'review': {
        'points': [
            "Most direct English questions put an auxiliary before the subject — except when Who or What is the subject of the verb ('Who called you?').",
            "Polite indirect questions ('Could you tell me…', 'Do you know…') switch to statement word order and drop 'do/does/did'.",
            "Follow-up questions that react to specific details turn a dry Q&A into a real conversation."
        ],
        'retrieval': [
            "Take one question about your city or school and say it twice: first as a direct question, then as a polite indirect question.",
            "Say one subject question ('Who…') and one object question ('Who did…') using the same verb."
        ],
        'watch': [
            "'Do you know where is the bank?' → 'Do you know where the bank is?' (Use statement word order inside an indirect question.)",
            "'Did she called you?' → 'Did she call you?' ('Did' already carries the past tense.)"
        ],
        'selfcheck': [
            "I can ask polite indirect questions without accidentally inverting the verb.",
            "I can keep a conversation moving for two minutes using natural follow-up questions."
        ],
        'answers': {
            'A': ["Have / tried", "happened", "the main library is", "costs", "wrote", "did / speak"],
            'B': ["Could you tell me where you parked your car?",
                  "Do you know when the exam results will be ready? / Could you tell me when the exam results will be ready?",
                  "Do you know where the nearest pharmacy is?",
                  "answers vary (e.g. 'What field are you thinking of moving into?' / 'What made you decide to make a change?')",
                  "Did she call you after the interview?",
                  "answers vary (e.g. 'How long have you been studying English?')"],
        },
    },
}

L4 = {
    'n': 4, 'part_no': 2, 'part_title': 'Express Ideas Clearly',
    'title': 'Modal Verbs for Real-Life Situations',
    'goal': 'express ability, advice, obligation, permission, possibility and certainty at the right strength',
    'intro': [
        "Suppose a colleague shows you a draft of an important email that has several confusing sentences. If you say, "
        "'You must rewrite this,' you sound like a strict commander. If you say, 'You might want to make the second "
        "paragraph a little clearer,' you sound like a helpful teammate.",
        "Modal verbs (can, could, should, must, might, would) are the volume controls of English. They let you adjust "
        "the exact social strength of your advice, requests, obligations, and logical guesses so your listener hears "
        "both your message and your respect."
    ],
    'hook': [
        "Imagine two real-life moments with a partner:",
        "•  Situation 1: A close friend tells you, 'I study English for two hours every night, but I still freeze when I have to speak.' Give them two pieces of helpful advice.",
        "•  Situation 2: You need to leave today's class or work meeting fifteen minutes early for a medical appointment. How would you ask the instructor or manager?",
        "Compare the exact words you both chose. Which words made your advice sound encouraging rather than bossy, "
        "and which words made your request sound polite?",
    ],
    'rules': [
        {'label': 'Rule 1 — Choosing modals by meaning and social strength',
         'text': [
             "Structurally, core modal verbs are the simplest verbs in English: they are followed directly by the base "
             "verb for every person, with no '-s' in the third person and no 'to' ('She can swim', 'He should wait').",
             "The real skill is choosing the right modal for the relationship. 'Must' and 'have to' express necessity "
             "or strong obligation; 'should' and 'ought to' offer advice; 'can', 'could', and 'may' handle ability, "
             "possibility, and permission."
         ],
         'formula': [
             "Modal + base verb  (never add -s or 'to': he can speak · she should wait · you mustn't touch)",
             "Obligation: must / have to   ·   Advice: should / ought to   ·   Possibility: may / might / could   ·   Ability & permission: can / could / may"
         ],
         'examples': [
             "All applicants have to submit their transcripts by Friday.  (external institutional rule)",
             "You really must try the fresh bread from that bakery!  (speaker's personal enthusiasm / strong recommendation)",
             "You should take a short break before you drive home.  (supportive advice)",
             "We could meet on Wednesday, or we might wait until the report is ready.  (open possibilities)"
         ],
         'remember': [
             "'Have to' usually points to an external rule or situation ('I have to wear an ID badge at work'), whereas 'must' "
             "often expresses the speaker's own authority or personal conviction ('I must remember to call my mother tonight').",
             "In the negative, their meanings split completely: 'don't have to' means it is not necessary ('You don't have to bring food'), "
             "while 'mustn't' means it is forbidden ('You mustn't park in front of the ambulance bay')."
         ]},
        {'label': 'Rule 2 — Degrees of certainty: reading the evidence',
         'text': [
             "We also use modal verbs when we look at clues in front of us and make a logical guess (a deduction). "
             "Suppose you knock on a colleague's office door and nobody answers.",
             "If her coat is on the chair and her computer screen is on, you say, 'She must be in the building' (you are "
             "almost certain it is true). If you have no idea where she is, you say, 'She might / may / could be in a "
             "meeting' (it is one possibility). If you just saw her drive out of the car park, you say, 'She can't be in "
             "her office' (you are almost certain it is impossible)."
         ],
         'formula': [
             "Present deduction:  must be (almost certainly true)  ·  may / might / could be (possible)  ·  can't be (almost certainly not true)",
             "Past deduction:  must have + past participle  ·  may / might / could have + participle  ·  can't / couldn't have + participle"
         ],
         'examples': [
             "He has been travelling for fourteen hours — he must be exhausted.",
             "Take a warm jacket; the temperature might drop after sunset.",
             "That can't be Bilal at the door — he's in Kandahar all week.",
             "She isn't answering her phone; she must have left it in her bag."
         ],
         'remember': [
             "For negative logical deductions, always use 'can't be' (never 'mustn't be'): "
             "say 'He can't be at home — all the lights are off' (deduction from evidence), whereas 'He mustn't leave the room' is a prohibition."
         ]},
        {'label': 'Rule 3 — Diplomatic and polite framing in real life',
         'text': [
             "When you ask a favour, make a complaint, or suggest a change at work, stepping back from 'can/will' to "
             "softer forms ('could', 'would', 'might') gives the other person room to say yes comfortably."
         ],
         'formula': [
             "Polite requests:  Could I possibly …?  ·  Would you mind + verb-ing …?  ·  I was wondering if I could …",
             "Diplomatic suggestions:  It might be worth + verb-ing …  ·  We could always …  ·  You might want to …"
         ],
         'examples': [
             "Would you mind moving your bag slightly so I can sit down?",
             "Could I possibly have an extra day to check the figures?",
             "I was wondering if we could reschedule our meeting for Thursday afternoon."
         ],
         'remember': [
             "Because 'Would you mind…?' literally means 'Would it bother you…?', a polite 'yes, go ahead' answer uses a negative word: "
             "'No, not at all' or 'Of course not — go right ahead.'"
         ]},
    ],
    'differences': [
        {'title': 'must vs have to vs should — choosing the right weight',
         'text': [
             "Hear how the social pressure changes across these three ways of talking about seeing a doctor:"
         ],
         'rows': [
             ["You must see a doctor today.", "You have to see a doctor to get a medical certificate.", "You should see a doctor if that cough continues.", "'Must' carries urgent personal insistence from the speaker; 'have to' states an external requirement; 'should' gives sensible, non-pushy advice."],
             ["You mustn't work on Saturday.", "You don't have to work on Saturday.", "You shouldn't work every Saturday.", "'Mustn't' forbids it; 'don't have to' says it is optional; 'shouldn't' advises against it for your well-being."],
         ], 'headers': ['must / mustn\'t', 'have to / don\'t have to', 'should / shouldn\'t', 'What the listener hears']},
        {'title': "can't (logical deduction) vs mustn't (prohibition)",
         'text': [
             "This is one of the most important contrasts in spoken English:",
             "•  Deduction ('can't'): 'The restaurant can't be open yet — the chairs are still on the tables.' (I am judging from the evidence that it is impossible.)",
             "•  Prohibition ('mustn't'): 'You mustn't use your phone in the examination hall.' (It is against the rules.)"
         ],
         'headers': ["can't = logically impossible", "mustn't = forbidden by rule", "Why the difference matters"],
         'rows': [
             ["He can't be home yet — his car is gone.", "He mustn't leave yet — the guests are arriving.", "Using 'mustn't' for a guess makes you sound as if you are giving an order rather than drawing a conclusion."],
         ]},
        {'title': 'could vs was able to for past achievements',
         'text': [
             "Use 'could' for general past ability ('I could swim when I was six'), and also with verbs of perception ('I could hear the music from outside'). "
             "When you talk about managing to succeed in one specific, difficult past situation, use 'was/were able to' (or 'managed to'): "
             "'The road was blocked, but after an hour we were able to find another route' (not 'we could find another route'). "
             "In the negative, both forms work everywhere: 'We couldn't / weren't able to find it.'"
         ]},
    ],
    'practice_a': [
        "You look exhausted after that double shift. You __________ get some rest tonight.  (supportive advice)",
        "My grandmother __________ speak four languages fluently when she was a young teacher.  (general past ability)",
        "Dr Karimi __________ be in the clinic today — his car is parked right outside the entrance.  (strong positive deduction)",
        "Visitors __________ touch the laboratory equipment — it is high-voltage and dangerous!  (prohibition)",
        "Take an umbrella just in case; it __________ rain later this afternoon.  (possibility)",
        "__________ you mind __________ (open) the window for a few minutes?",
    ],
    'practice_b': [
        "Rewrite this blunt command as a polite request: 'Open the window.'",
        "Rewrite using a modal of deduction: 'I am almost certain she is at home right now.'",
        "Rewrite using a past modal of possibility: 'Perhaps he missed the early train.'",
        "Correct the modal mistake: 'He mustn't be at home — all his lights are off.'  (intended meaning: I'm sure he isn't)",
        "Write a natural, polite reply agreeing to this request: 'Would you mind waiting five minutes?'",
        "Give gentle, diplomatic advice to a classmate who has a bad headache (write two sentences using different modals).",
    ],
    'pair': {
        'intro': "Work with your partner as two colleagues on an organising committee. Your department has a small "
                 "budget and one free weekend, and you must agree on ONE shared option from the three choices below.",
        'task': [
            "Options: (1) a two-day communication workshop, (2) upgrading the student study lounge, or (3) a one-day team excursion outside the city.",
            "Negotiate naturally using modals at different strengths: make suggestions (should / could), point out rules or budget limits (have to / mustn't), make logical guesses about how people will react (must be / might), and use polite requests (Would you mind… / Could we…)."
        ],
        'model': [
            "A: I think we should invest in the study lounge — the current chairs must be ten years old, and students use that room every day.",
            "B: That's true, though a communication workshop could help everyone before the exam period. Would you mind if we priced the chairs first to see if we might afford a half-day workshop too?"
        ],
        'output': "One agreed decision per pair, justified with at least three different modals, plus "
                  "two polite request forms used naturally during the negotiation.",
        'criteria': [
            "chooses modal strength that fits the situation (gentle advice vs firm rule)",
            "uses polite request or suggestion frames at least twice (Would you mind… / Could we…)",
            "uses deduction modals accurately based on evidence (must be / might be / can't be)",
            "reaches a clear joint decision and explains the reasoning"
        ],
    },
    'advanced': {
        'intro': "To sound truly natural in professional and academic speaking, notice how modals extend into the past "
                 "and how subtle phrases soften suggestions when speaking to senior colleagues or clients.",
        'base': [
            "Sort modals by the job they do in context rather than on a single mechanical scale: must be = strong logical deduction from evidence; should be = reasonable expectation ('The bus should be here soon'); may / might / could be = open possibilities.",
            "Look around the classroom or out of the window and make three spoken deductions right now: one with 'must be', one with 'might be', and one with 'can't be'."
        ],
        'upgrade': [
            "Use past deduction forms (must have / might have / can't have + past participle) to interpret past events: 'You must have been relieved when you saw your name on the list.'",
            "Use 'would' to soften preferences and recommendations: 'I'd suggest waiting until Monday' · 'Would you prefer morning or afternoon?'",
            "Use diplomatic obligation frames when proposing changes to a team: 'We really ought to consider…' · 'It might be worth reviewing the schedule before we commit.'"
        ],
    },
    'realtalk': {
        'plan': "Take one minute to choose your role and prepare three keywords: your main problem or goal, two polite "
                "modal frames you will use ('I was wondering if…', 'Could we possibly…'), and one deduction you can make "
                "about the situation ('There must have been…', 'You must be…'). Swap roles after one minute.",
        'task': "Role-play a real-world problem call: one partner is a client or student dealing with a problem (a "
                "delayed book order, a double-booked room, or a missed registration deadline); the other is the "
                "professional resolving it. Explain the issue politely, make deductions, propose options, and agree on "
                "a solution. Then switch roles.",
        'model': "Client: Good morning — I was wondering if I could speak to someone about my textbook order. It was due "
                 "on Tuesday, and it still hasn't arrived.\n"
                 "Professional: I'm very sorry about that. You must be frustrated, especially with classes starting this week. "
                 "Let me check the tracking number… Ah, it looks as if the parcel was sent to the wrong district depot.\n"
                 "Client: In that case, could I possibly have it delivered tomorrow? I have to teach until four, so it might "
                 "need to arrive in the evening.\n"
                 "Professional: That should be possible. We could book an evening courier slot for you, or I could have the "
                 "main bookshop hold a fresh copy for you to collect today. Which would you prefer?",
        'feedback': [
            "modals match the intended social strength (polite request, gentle advice, firm obligation)",
            "maintains a composed, polite tone even while explaining a problem",
            "includes at least one natural deduction (must be / must have been / can't be)",
            "arrives at a practical solution that both speakers accept"
        ],
    },
    'review': {
        'points': [
            "Core modals are followed directly by the base verb (no -s, no 'to') and let you adjust the strength of advice, obligation, and possibility.",
            "Use 'must be', 'might be', and 'can't be' for logical deductions from evidence; never confuse 'can't be' (impossible) with 'mustn't' (forbidden).",
            "Softening frames ('Could I possibly…', 'Would you mind + -ing…', 'I was wondering if…') keep requests and negotiations polite."
        ],
        'retrieval': [
            "Make three logical deductions about people or things around you using 'must be', 'might be', and 'can't be'.",
            "Ask a partner for a small favour in two different ways using polite modal openings."
        ],
        'watch': [
            "'He mustn't be at home.' → 'He can't be at home.' (Use 'can't' when you mean 'I am sure it isn't true'.)",
            "'Would you mind to open the window?' → 'Would you mind opening the window?' ('Mind' takes the -ing form.)"
        ],
        'selfcheck': [
            "I can adjust how strong or polite my advice and requests sound in conversation.",
            "I can make present and past deductions accurately using must, might, and can't."
        ],
        'answers': {
            'A': ["should", "could", "must", "mustn't", "might / may / could", "Would / opening"],
            'B': ["Could you open the window, please? / Would you mind opening the window?",
                  "She must be at home.",
                  "He might have missed the early train. / He may / could have missed the early train.",
                  "He can't be at home — all his lights are off.",
                  "No, not at all. / Of course not — take your time.",
                  "answers vary (e.g. 'You should drink some water and rest your eyes. You might also want to step outside for some fresh air.')"],
        },
    },
}

LESSONS_1_4 = [L1, L2, L3, L4]


def render_all(doc, keys_registry):
    for L in LESSONS_1_4:
        render_lesson(doc, L, keys_registry)

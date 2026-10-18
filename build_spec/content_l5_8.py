# -*- coding: utf-8 -*-
"""Lessons 5-8 — Part Three: Think Beyond the Present; Part Four: Compare and Persuade."""
from lesson_template import render_lesson

L5 = {
    'n': 5, 'part_no': 3, 'part_title': 'Think Beyond the Present',
    'title': 'Conditionals for Decisions and Possibilities',
    'goal': 'talk about consequences, alternatives and hypothetical situations accurately',
    'intro': [
        "Listen to two managers discussing a project delay. The first says, 'If we get the parts tomorrow, we'll "
        "finish on Friday.' The second says, 'If we got the parts tomorrow, we'd finish on Friday.' Both sentences "
        "talk about tomorrow, yet the first manager expects the parts to arrive, while the second manager doubts "
        "they will show up at all.",
        "Conditionals are how English speakers weigh decisions, test possibilities, and learn from past mistakes. "
        "By shifting the verb tense in the 'if' clause, you tell your listener immediately whether you are dealing "
        "with a real plan, a hypothetical daydream, or a past event that cannot be undone."
    ],
    'hook': [
        "Read these three sentences aloud with a partner and notice how your view of the situation changes:",
        "•  'If I have free time this evening, I'll call my brother.'",
        "•  'If I had more free time these days, I'd learn photography.'",
        "•  'If I had known about the traffic this morning, I would have left home half an hour earlier.'",
        "Which sentence talks about a real possibility today? Which one imagines a different present? Which one "
        "looks back at a past moment that is already over? Now tell your partner one real plan for this week (using "
        "the first pattern) and one change you would make if you had an extra free day every week.",
    ],
    'rules': [
        {'label': 'Rule 1 — Zero and first conditionals: real facts and real future possibilities',
         'text': [
             "When you talk about the real world — things that always happen or things that can genuinely happen "
             "tomorrow — keep the 'if' clause in the present tense.",
             "Use the zero conditional (If + present, present) for scientific truths, rules of nature, and automatic "
             "habits. Use the first conditional (If + present, will + base verb) when a future condition is genuinely "
             "open and you are predicting or promising the result."
         ],
         'formula': [
             "Zero conditional (always true):  If / When + present simple, present simple",
             "First conditional (real future possibility):  If + present simple, will (or can / may / should) + base verb"
         ],
         'examples': [
             "If you heat ice above 0°C, it melts.  (general law of nature)",
             "If I drink coffee after dinner, I don't sleep well.  (personal habit that always holds true)",
             "If the weather stays clear tomorrow, we'll hike up to the ridge.  (real future possibility)",
             "If you finish the draft by four, I can check it before I leave.  (real condition with a modal result)"
         ],
         'remember': [
             "In an ordinary future condition, use the present simple in the if-clause: say 'If it rains tomorrow, we'll stay home' "
             "(do not use 'will' just because the event is in the future). Will can occur in if-clauses with a special meaning such as polite willingness ('If you will wait a moment, I'll fetch the director'), but ordinary future conditions take the present simple."
         ]},
        {'label': 'Rule 2 — Second conditional: imagining a different present or unlikely future',
         'text': [
             "What if you want to talk about a situation that is not true right now, or a future scenario that you "
             "consider unlikely? English steps one tense back into the past simple in the 'if' clause, and uses "
             "'would' (or 'could / might') in the result clause.",
             "The past tense here does not point to yesterday — it signals distance from reality. When you say "
             "'If I had her phone number, I would call her right now,' your listener immediately knows two things: "
             "you do not have the number now, and therefore you cannot call."
         ],
         'formula': [
             "Second conditional:  If + past simple, would / could / might + base verb  →  unreal present · unlikely future · hypothetical advice"
         ],
         'examples': [
             "If I had an extra hour every morning, I would read in English before work.  (reality: I don't have that hour now)",
             "If I were you, I'd accept the fellowship offer immediately.  (hypothetical advice)",
             "If public transport were faster, fewer commuters would drive into the city centre."
         ],
         'remember': [
             "In advice and careful English, 'If I were you…' (and 'If he/she/it were…') is the conventional standard form. "
             "'Was' also occurs in informal conversation ('If I was you…'), but 'If I were…' works well in every setting."
         ]},
        {'label': 'Rule 3 — Third and mixed conditionals: looking back at the past',
         'text': [
             "The third conditional is our time machine for hindsight. Because the past is already finished, we step "
             "one level further back to the past perfect (If + had + past participle) and use 'would have + past participle' "
             "for the imagined past result.",
             "Sometimes, however, a past choice still shapes your life right now. When a past event has a present "
             "result (or a permanent present trait caused a past action), we mix the two halves into a mixed conditional."
         ],
         'formula': [
             "Third conditional (both halves in the past):  If + past perfect, would / could / might have + past participle",
             "Mixed (past cause → present result):  If + past perfect, would + base verb (now)",
             "Mixed (present trait → past result):  If + past simple (always), would have + past participle (then)"
         ],
         'examples': [
             "If we had left ten minutes earlier, we wouldn't have missed the train.  (third: we left late, and we missed it)",
             "If I had accepted that job in Herat, I would live there now.  (mixed: past decision → present life)",
             "If she weren't so organized, the conference wouldn't have run so smoothly last week.  (mixed: permanent trait → past result)"
         ],
         'remember': [
             "In natural spoken English, both 'had' and 'would' contract to 'd: 'If I'd known you were waiting, I'd have called.' "
             "Never put 'would have' inside the if-clause (say 'If I had known', not 'If I would have known')."
         ]},
        {'label': 'Rule 4 — Beyond "if": unless, as long as, and provided that',
         'text': [
             "You do not have to begin every condition with 'if'. When you want to set a clear boundary or exception, "
             "'unless' means 'except if / if not', while 'as long as' and 'provided (that)' mean 'on the condition that'."
         ],
         'formula': [
             "unless + affirmative verb  =  if … not   ·   as long as / provided (that)  =  only if"
         ],
         'examples': [
             "You won't notice progress unless you practise speaking out loud.  (= if you don't practise)",
             "I'm happy to lend you my notes as long as you return them by Thursday.",
             "Provided that everyone arrives on time, the meeting will finish by eleven."
         ],
         'remember': [
             "Because 'unless' already means 'if not', do not add a second negative inside the unless-clause: "
             "say 'Unless you hurry, we'll be late' (not 'Unless you don't hurry')."
         ]},
    ],
    'differences': [
        {'title': 'First vs second vs third conditional — one situation across three worlds',
         'text': [
             "Compare how a speaker uses three different conditionals depending on whether the opportunity is still "
             "open, unlikely, or already gone:"
         ],
         'rows': [
             ["If I have time this afternoon, I'll help you.", "If I had time this afternoon, I would help you.", "1st conditional = real possibility (my schedule might allow it).  2nd conditional = unreal present (my afternoon is already full, so I am politely apologizing that I cannot)."],
             ["If I knew her email, I would write to her.", "If I had known her email yesterday, I would have written to her.", "2nd conditional = present gap (I don't know it now).  3rd conditional = past hindsight (yesterday's chance has already passed)."],
         ], 'headers': ['Option A', 'Option B', 'What changes in the speaker\'s mind']},
        {'title': 'Third conditional vs mixed conditional — where does the result live?',
         'text': [
             "When you start a sentence with 'If I had slept earlier last night…', pause for a split second and ask: "
             "is the result also in the past, or is it happening right now?"
         ],
         'rows': [
             ["If I had slept earlier last night, I would have caught the eight o'clock bus.", "If I had slept earlier last night, I wouldn't feel so tired right now.", "Left (3rd): catching the bus was this morning (past).  Right (mixed): feeling tired is right now (present)."],
         ], 'headers': ['Third conditional (past result)', 'Mixed conditional (present result)', 'How to choose']},
    ],
    'practice_a': [
        "If you __________ (heat) pure water at sea level to 100°C, it __________ (boil).",
        "If it __________ (rain) heavily tomorrow morning, we __________ (cancel) the outdoor training session.",
        "If I __________ (be) in your position, I __________ (apologise) to the client in person.",
        "If she __________ (leave) home fifteen minutes earlier, she __________ (not/miss) the train yesterday.",
        "If I __________ (know) his new phone number, I __________ (call) him right now.",
        "We __________ (go) for a walk along the river as long as the weather __________ (stay) dry.",
    ],
    'practice_b': [
        "Rewrite using unless: 'If you don't register before Friday, you can't attend the seminar.'",
        "Rewrite as a third conditional: 'He didn't check the timetable, so he missed the ferry.'",
        "Rewrite as a mixed conditional (past cause → present result): 'She didn't save enough money last year, so she can't buy the car now.'",
        "Correct the mistake: 'If I will have free time tonight, I will review the vocabulary.'",
        "Use a second conditional ('If I were you…') to advise a friend who wants to quit their job tomorrow without another offer.",
        "Answer in your own words with a full second conditional sentence: What would you do if you were given a one-year scholarship to study anywhere?",
    ],
    'pair': {
        'intro': "Play a cause-and-effect chain game with your partner. You will build two short stories together, "
                 "sentence by sentence, where the result of one speaker's conditional becomes the 'if' clause of the "
                 "next speaker's sentence.",
        'task': [
            "Chain 1 (looking back and connecting to now): Start with 'If I had woken up an hour earlier this morning…' Build at least six connected sentences together, including both third and mixed conditionals.",
            "Chain 2 (imagining a change tomorrow): Start with 'If the internet stopped working across the whole city for a week…' Build six connected sentences exploring what people would do."
        ],
        'model': [
            "A: If I had woken up an hour earlier this morning, I would have caught the early bus.",
            "B: And if you had caught the early bus, you wouldn't have run into the morning traffic jam — so you would feel much more relaxed right now!"
        ],
        'output': "One shared story of at least six linked conditional sentences per pair, including "
                  "one third and one mixed conditional, that both partners can retell in summary.",
        'criteria': [
            "conditional verb forms match the intended time (real future, unreal present, unreal past)",
            "includes at least one third conditional and one mixed conditional accurately",
            "each sentence builds logically on the partner's previous idea",
            "both partners contribute equally without reading from notes"
        ],
    },
    'advanced': {
        'intro': "In formal presentations, debates, and storytelling, English speakers often vary their conditional "
                 "openings so they do not repeat the word 'if' in every sentence.",
        'base': [
            "Keep one clear anchor sentence in mind for each conditional pattern: 'If you heat ice, it melts' (zero) · 'If it rains, we'll cancel' (first) · 'If I were you, I'd wait' (second) · 'If I'd known, I'd have come' (third).",
            "Practise saying the natural spoken contractions aloud ('If I'd known…', 'We'd have waited…', 'She wouldn't have minded') so three-part verbs roll off your tongue smoothly."
        ],
        'upgrade': [
            "Use inverted conditionals in formal talks by dropping 'if' and placing Should, Were, or Had at the start: 'Should you require any further details, please let us know' · 'Had we known about the shortage, we would have ordered earlier.'",
            "Use 'but for + noun phrase' as a compact alternative to a negative conditional clause: 'But for your timely advice, we would have signed the wrong contract.'",
            "Use 'suppose' or 'supposing (that)' when inviting a listener to explore a scenario with you: 'Suppose our budget were cut by twenty percent — which project would we protect first?'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to assign each conditional a clear job for your talk: a first conditional for the "
                "realistic outcome of your choice, a second conditional for an option you are rejecting, and a third "
                "or mixed conditional for a lesson learned from last year. Jot down only three or four keywords.",
        'task': "One-minute decision talk: Imagine your school or workplace has received a special grant. You must "
                "choose ONE of three investments: (1) staff training, (2) new computer equipment, or (3) a student "
                "resource library. Explain what will happen if you choose your top option, why the second option is "
                "less effective, and what you would have done differently with last year's budget.",
        'model': "If we invest this grant in staff training, our whole team will improve their teaching skills, and "
                 "students will feel the benefit within a month. Buying new computers would look impressive at first, "
                 "but if I were leading the committee, I would put people ahead of hardware every time. In fact, if "
                 "we had set aside a small training fund last year, we wouldn't be facing such a steep learning curve "
                 "with the new curriculum right now. Provided that we schedule the workshops before the new term starts, "
                 "training is by far the smartest choice.",
        'feedback': [
            "uses a first conditional for realistic future consequences",
            "uses a second conditional to weigh a hypothetical alternative or give advice",
            "uses a third or mixed conditional to reflect on a past decision",
            "connects the options into a persuasive, logical recommendation"
        ],
    },
    'review': {
        'points': [
            "Zero conditional states general truths; first conditional predicts real future possibilities (using the present simple after 'if').",
            "Second conditional ('If + past, would + verb') imagines an unreal present or unlikely future; 'If I were you…' is the classic advice frame.",
            "Third conditional ('If + had + participle, would have + participle') looks back at an unchangeable past; mixed conditionals connect a past cause to a present result."
        ],
        'retrieval': [
            "Say one sentence of your own for each conditional type: zero, first, second, third, and mixed.",
            "Take one real mistake or delay from your past month and turn it into a third conditional sentence."
        ],
        'watch': [
            "'If it will rain tomorrow, we'll stay in.' → 'If it rains tomorrow, we'll stay in.' (Use present simple for ordinary future conditions.)",
            "'Unless you don't hurry, you'll miss the bus.' → 'Unless you hurry, you'll miss the bus.' ('Unless' already means 'if not'.)"
        ],
        'selfcheck': [
            "I can distinguish smoothly between an unreal present (second conditional) and an unreal past (third conditional).",
            "I can link a past decision to a present result using a mixed conditional."
        ],
        'answers': {
            'A': ["heat / boils", "rains / will cancel (or: 'll cancel)", "were / would apologise",
                  "had left / wouldn't have missed", "knew / would call", "will go / stays"],
            'B': ["Unless you register before Friday, you can't attend the seminar.",
                  "If he had checked the timetable, he wouldn't have missed the ferry.",
                  "If she had saved enough money last year, she could buy the car now. / …would be able to buy the car now.",
                  "If I have free time tonight, I will review the vocabulary.",
                  "answers vary (e.g. 'If I were you, I wouldn't resign until I had a signed offer in hand.')",
                  "answers vary"],
        },
    },
}

L6 = {
    'n': 6, 'part_no': 3, 'part_title': 'Think Beyond the Present',
    'title': 'Wishes, Regrets, and Hypothetical Situations',
    'goal': 'express preferences, dissatisfaction, regrets and imagined alternatives naturally',
    'intro': [
        "When you hope something will happen tomorrow, you stay in the real world: 'I hope the bus comes soon.' "
        "When you wish something were different right now, you already know reality is the opposite: 'I wish I had "
        "an umbrella with me' (said while standing in the rain with no umbrella).",
        "Because wishes, regrets, and polite preferences often describe a world that does not match reality, English "
        "uses the same clever device you saw in conditionals: stepping one tense back in time to signal that you "
        "are imagining an alternative."
    ],
    'hook': [
        "Compare these three sentences spoken by a student on the morning of an exam:",
        "•  'I wish I knew the answer to question four.'   (during the exam)",
        "•  'I wish I had studied chapter seven last night.'   (looking back at yesterday evening)",
        "•  'I wish the person behind me would stop tapping their pen.'   (reacting to an annoying noise)",
        "With a partner, discuss how the speaker feels in each sentence and what time each sentence points to. "
        "Then share one skill you wish you had right now and one small decision from the past year you would handle differently.",
    ],
    'rules': [
        {'label': 'Rule 1 — Wishing for a different present: wish + past simple, could, or would',
         'text': [
             "When you want your current reality to be different right now, follow 'wish' (or the more emphatic "
             "'If only') with the past simple: 'I wish I spoke Arabic fluently' means 'I do not speak it fluently right now.'",
             "When the wish is about your own ability, use 'could' ('I wish I could stay longer'). When you want "
             "someone else — or an outside situation — to change their behaviour, use 'would' ('I wish you would "
             "listen before interrupting')."
         ],
         'formula': [
             "Present state wish:  wish / if only + past simple   →   I wish I knew her address.  (reality: I don't know it)",
             "Present ability wish:  wish / if only + could + base verb   →   I wish I could join you.",
             "Desired change in behaviour/situation:  wish / if only + somebody/something + would + base verb"
         ],
         'examples': [
             "I wish our flat were closer to the university.  (were is the traditional subjunctive and common in careful English; was is also widespread informally: I wish our flat was closer.)",
             "I wish I could remember where I put that folder.",
             "I wish the neighbours wouldn't play loud music after midnight."
         ],
         'remember': [
             "Use 'wish + would' when you want someone else's behaviour or an outside situation to change (it often carries a note of impatience or complaint). "
             "We do not say 'I wish I would…' about ourselves — for our own ability, use 'I wish I could…'."
         ]},
        {'label': 'Rule 2 — Wishing for a different past: regrets with wish + past perfect',
         'text': [
             "When a moment is already in the past and you regret what happened (or didn't happen), step one level "
             "further back to the past perfect: 'wish + had + past participle'.",
             "'If only…!' uses the exact same grammar as 'I wish…', but adds stronger personal emotion."
         ],
         'formula': [
             "Past regret:  wish / if only + had (not) + past participle   →   I wish I had started earlier."
         ],
         'examples': [
             "I wish I had asked more questions during the training week.",
             "She wishes she hadn't spoken so sharply during the argument.",
             "If only we had checked the road conditions before setting off!"
         ],
         'remember': [
             "Never use 'wish + past simple' for a finished past event: for yesterday's mistake, say 'I wish I hadn't said that yesterday' "
             "(not 'I wish I didn't say that yesterday')."
         ]},
        {'label': 'Rule 3 — Expressing preferences and overdue actions: would rather and it\'s time',
         'text': [
             "'Would rather' changes its grammar depending on who is doing the action. When you talk about your own "
             "preference, use the base verb: 'I'd rather walk than wait for the bus.' When you want someone else to "
             "do something, introduce a new subject and step back to the past simple: 'I'd rather you didn't mention "
             "this to anyone yet.'",
             "Similarly, 'It's time' (or 'It's high time') followed by a subject and a past simple verb means an "
             "action is already overdue — it should have happened before now: 'It's ten o'clock — it's time we headed home.'"
         ],
         'formula': [
             "Same subject (my own action):  would rather (not) + base verb (than …)   →   I'd rather stay in tonight.",
             "Different subject (someone else's action):  would rather + person + past simple   →   I'd rather you called me tomorrow.",
             "Overdue action:  It is (high / about) time + subject + past simple   →   It's high time we made a decision."
         ],
         'examples': [
             "I'd rather cook a simple meal at home than wait an hour at a crowded restaurant.",
             "I'd rather you didn't park in front of the gate — the delivery lorry needs to get through.",
             "It's high time the city council repaired this bridge."
         ],
         'remember': [
             "Do not confuse 'would rather' (preference) with 'had better + base verb' (strong urgent warning: 'You'd better leave now or you'll miss your flight')."
         ]},
        {'label': 'Rule 4 — Comparing preferences and describing impressions: prefer and as if / as though',
         'text': [
             "With 'prefer', watch how you connect the two options: 'prefer A to B' (with nouns or -ing forms) versus "
             "'would prefer to do A rather than do B'.",
             "With 'as if' and 'as though', use the past simple or past perfect when the comparison is unreal or exaggerated: "
             "'He gives orders as if he owned the company' (he does not own it)."
         ],
         'formula': [
             "General preference:  prefer + noun/-ing + to + noun/-ing   ·   Specific choice:  would prefer + to + verb + rather than + base verb",
             "Unreal impression:  act / look / talk + as if / as though + past simple (present unreal) or past perfect (past unreal)"
         ],
         'examples': [
             "I generally prefer reading printed books to reading on a screen.",
             "Today I'd prefer to walk rather than take a taxi.",
             "She walked back into the meeting room calmly, as though nothing had happened."
         ],
         'remember': [
             "If what follows 'as if' is a real, likely fact based on evidence, keep the normal present tense: "
             "'Look at those dark clouds — it looks as if it is going to pour.'"
         ]},
    ],
    'differences': [
        {'title': 'Present wish vs past regret — stepping back in time',
         'text': [
             "Notice how the verb form after 'wish' tells the listener immediately whether the situation can still "
             "be changed today or belongs to the past:"
         ],
         'rows': [
             ["I wish I had a quieter room to study in.", "I wish I had chosen a quieter room when we moved in.", "Left (past simple): my room is noisy right now.  Right (past perfect): I am looking back with regret at the past choice I made."],
             ["I wish I knew how to fix this engine.", "I wish I had learned how to fix engines at college.", "Left: I am stuck in front of the engine right now.  Right: I regret missing the opportunity years ago."],
         ], 'headers': ['wish + past simple (present reality)', 'wish + past perfect (past regret)', 'What the listener understands']},
        {'title': 'wish + could vs wish + would — ability vs willingness',
         'rows': [
             ["I wish I could come to your graduation.", "I wish you would come to my graduation.", "'Could' points to inability (I have an exam that day, so I am unable to attend). 'Would' appeals to the other person's willingness (you are free, and I want you to decide to come)."],
         ], 'headers': ['wish + could (personal ability)', 'wish + would (other person\'s choice)', 'Why the choice matters']},
        {'title': "Three ways to use 'It's time' — from neutral to urgent",
         'text': [
             "Compare the tone of these three sentences:",
             "1. 'It's time to leave.' (neutral statement — the scheduled moment has arrived).",
             "2. 'It's time we left.' (gently insistent — we are already a little late).",
             "3. 'It's high time he took responsibility for his work.' (emphatic criticism — this is long overdue)."
         ]},
    ],
    'practice_a': [
        "I wish I __________ (know) her email address so I could send her the invitation right now.",
        "I really wish I __________ (not/say) that careless remark during yesterday's meeting.",
        "He gives everyone instructions as if he __________ (own) the entire department.",
        "It's high time we __________ (make) a firm decision about the autumn budget.",
        "I'd rather you __________ (not/tell) anyone about the job offer until the contract is signed.",
        "If only I __________ (be) a little more patient when traffic slows down!",
    ],
    'practice_b': [
        "Rewrite as a past regret using wish: 'I didn't study harder at school, and now I regret it.'",
        "Rewrite politely using would rather: 'Please don't smoke near the doorway.'",
        "Correct the tense mistake: 'I wish I have more free time this semester.'",
        "Correct the tense mistake: 'It's already midnight — it's time we will go home.'",
        "Choose the natural forms: I generally prefer (reading / to read) historical novels to (watch / watching) television.",
        "Write one vivid sentence with 'as if' or 'as though' describing a friend who arrived late and out of breath.",
    ],
    'pair': {
        'intro': "Play 'The Constructive Adviser' with your partner. Partner A shares three honest frustrations or "
                 "regrets from everyday life using 'I wish…', 'If only…', or 'I'd rather…'. Partner B listens, asks "
                 "one clarifying question, and offers a practical step forward using 'It's time…', 'You could…', or "
                 "'If I were you…'. Swap roles after two minutes.",
        'task': [
            "Choose three areas from: study habits · work-life balance · health and sleep · learning English · technology use.",
            "Include at least one present wish (wish + past simple/could/would), one past regret (wish + past perfect), and one response with 'It's time we/you…' or 'I'd rather…'."
        ],
        'model': [
            "A: I wish I didn't spend so much time checking my phone late at night — I always wake up tired.",
            "B: I know that feeling. It's about time we both left our phones in another room after ten o'clock. If you bought a simple alarm clock, you wouldn't need your phone beside your bed at all."
        ],
        'output': "Three complaint–solution exchanges per role: each complaint uses a correct wish "
                  "form, each solution a natural modal or 'it's time', and partners swap roles "
                  "smoothly.",
        'criteria': [
            "distinguishes accurately between present wishes (wish + past) and past regrets (wish + past perfect)",
            "uses 'It's time + past simple', 'would rather', and advice modals naturally",
            "reacts thoughtfully to the partner's situation rather than reading a list",
            "both partners complete all three exchanges in each role"
        ],
    },
    'advanced': {
        'intro': "Notice how skilled speakers use these same hypothetical patterns to soften workplace requests, "
                 "add emotional colour to stories, and express diplomatic dissatisfaction.",
        'base': [
            "Separate your own real-life wishes into two clear mental buckets: what you wish were different today ('I wish I knew / had / could…') versus what you wish had happened differently in the past ('I wish I had known / done…').",
            "Say three true sentences aloud right now: one with 'I wish I knew…', one with 'I wish I had known…', and one with 'I'd rather you…'."
        ],
        'upgrade': [
            "Use 'If only…!' when you want to convey stronger personal feeling or dramatic emphasis in a story: 'If only we had backed up the files before the power cut!'",
            "Use past-continuous framing ('We were hoping…', 'I was wondering…') to express diplomatic wishes in professional settings: 'We were hoping the figures would be ready before Friday.'",
            "Use 'as though' with the past perfect to describe revealing body language in a narrative: 'He greeted everyone cheerfully, as though the argument the night before had never happened.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to note three keywords: one genuine past regret that taught you something useful "
                "(wish + past perfect), one present habit or skill you still wish to change (wish + past simple / could), "
                "and one practical piece of advice for someone younger.",
        'task': "Speak for one full minute: 'A mistake or regret that taught me an important lesson.' Describe what "
                "you wish you had done differently in the past, what you still wish you could do better today, and "
                "what advice you would give a younger student facing the same choice.",
        'model': "I wish I had taken spoken English seriously during my first two years at university — I wasted "
                 "countless classes staying silent because I was afraid of making small grammar slips. Even today, "
                 "I sometimes wish I could express complex technical ideas as effortlessly as my mentor does. But "
                 "that regret taught me something valuable: fluency only grows when you use the language out loud. "
                 "It's high time we stopped treating mistakes as failures. If I were advising a first-year student "
                 "today, I'd tell them to record themselves speaking for two minutes every week — within a month, "
                 "you can hear the difference.",
        'feedback': [
            "uses 'wish + past perfect' (or 'If only + past perfect') accurately for the past regret",
            "uses 'wish + past simple' or 'wish + could' for the present situation",
            "turns the regret into constructive advice using a conditional, modal, or 'It's time…'",
            "speaks naturally and reflectively without reading from notes"
        ],
    },
    'review': {
        'points': [
            "Use 'wish + past simple / could' for present situations you want to be different; use 'wish + past perfect' for regrets about a finished past.",
            "Use 'wish + person/thing + would' when you want someone else's behaviour or an external situation to change.",
            "When 'would rather' or 'It's (high) time' is followed by a subject, step back to the past simple ('I'd rather you waited' · 'It's time we left')."
        ],
        'retrieval': [
            "Say one honest present wish and one honest past regret from your own life.",
            "State one preference about your own evening ('I'd rather…') and one polite preference about someone else's action ('I'd rather you…')."
        ],
        'watch': [
            "'I wish I have more time.' → 'I wish I had more time.' (Present wishes step back to the past form.)",
            "'I'd rather you don't mention this.' → 'I'd rather you didn't mention this.' (Use past simple after a new subject.)"
        ],
        'selfcheck': [
            "I can express both present wishes and past regrets without mixing up their verb tenses.",
            "I can use 'would rather', 'It's high time', and 'as if' naturally in conversation."
        ],
        'answers': {
            'A': ["knew", "hadn't said", "owned", "made", "didn't tell", "were (or: was in informal speech)"],
            'B': ["I wish I had studied harder at school.",
                  "I'd rather you didn't smoke near the doorway.",
                  "I wish I had more free time this semester.",
                  "It's already midnight — it's time we went home.",
                  "reading / watching",
                  "answers vary (e.g. 'He burst through the door out of breath, as if he had run all the way from the station.')"],
        },
    },
}

L7 = {
    'n': 7, 'part_no': 4, 'part_title': 'Compare and Persuade',
    'title': 'Comparisons Beyond the Basics',
    'goal': 'compare clearly and support comparisons with reasons',
    'intro': [
        "When someone says, 'Option A is better than Option B,' they have stated an opinion, but they have not yet "
        "persuaded anyone. Compare that with: 'Option A is far more reliable than Option B because it costs half as "
        "much to maintain, and the longer we use it, the more money we save.'",
        "Every real-world recommendation — choosing a university course, hiring a candidate, defending a budget — is "
        "built on comparison. When you combine accurate comparative forms with precise degree words and clear reasons, "
        "your opinions turn into persuasive arguments."
    ],
    'hook': [
        "Read these two pairs of claims aloud with a partner:",
        "•  'Train travel is better than flying.'   vs.   'On short routes, train travel is far more relaxing than flying because you avoid airport security queues.'",
        "•  'Vocabulary is important.'   vs.   'The more actively you use new vocabulary in speech, the faster it becomes permanent.'",
        "Now take one minute each to compare two ways of learning (studying alone vs studying in a group, or learning "
        "online vs in a classroom). Give at least one specific reason for your choice.",
    ],
    'rules': [
        {'label': 'Rule 1 — Comparatives and superlatives: comparing choices vs identifying an extreme',
         'text': [
             "Comparatives compare two people, things, or sets ('shorter than', 'more practical than'), while "
             "superlatives single out an extreme within a group ('the shortest', 'the most practical'). Use a comparative "
             "to compare two people, things or sets. Use a superlative to identify an extreme within a group, which "
             "often contains three or more. The exact number is a guide, not a grammatical rule: context and meaning decide.",
             "Short one-syllable adjectives (and many two-syllable adjectives ending in -y, like easy → easier) take "
             "'-er' and 'the -est'. Longer adjectives of two or more syllables take 'more' and 'the most' (or 'less' and 'the least')."
         ],
         'formula': [
             "Short adjectives:  adj-er + than  ·  the + adj-est   (fast → faster → the fastest  ·  busy → busier → the busiest)",
             "Longer adjectives & adverbs:  more/less + adj/adv + than  ·  the most/least + adj/adv",
             "Irregular forms:  good/well → better → the best  ·  bad/badly → worse → the worst  ·  far → further/farther → the furthest/farthest"
         ],
         'examples': [
             "Taking the ring road is quicker than driving through the old bazaar.",
             "She explained the financial plan more clearly than the previous consultant.",
             "That was the most challenging — and the most rewarding — project of my career."
         ],
         'remember': [
             "Never stack 'more' and '-er' together: say 'much taller' or 'far better' (never 'more taller' or 'more better').",
             "Spell and pronounce the comparison link as 'than' (not 'then', which refers to time)."
         ]},
        {'label': 'Rule 2 — Equality, multiples, and linked change: as … as and the more …, the more …',
         'text': [
             "Not every comparison says one thing is bigger or better than another. Sometimes you want to show that "
             "two options are equal ('as effective as'), that one falls short ('not as expensive as'), or that one is "
             "a specific multiple of the other ('twice as fast as').",
             "When two changes move together in cause and effect, English uses the double-comparative frame 'The + "
             "comparative …, the + comparative …': 'The more you speak out loud, the more natural the grammar feels.'"
         ],
         'formula': [
             "Equality & gap:  (not) as + adjective/adverb + as   ·   twice / three times / half + as + adj/adv + as",
             "Linked change:  The + comparative …, the + comparative …",
             "Continuous trend:  comparative + and + comparative   (faster and faster · more and more competitive)"
         ],
         'examples': [
             "This compact dictionary is just as comprehensive as the heavy two-volume edition.",
             "Practising aloud for twenty minutes is twice as effective as rereading notes silently for an hour.",
             "The earlier we leave tomorrow morning, the less traffic we will face on the highway.",
             "Solar panels are becoming more and more affordable every year."
         ],
         'remember': [
             "Inside 'as … as', keep the adjective or adverb in its base form: 'twice as expensive as' (not 'twice more expensive than').",
             "In 'the more …, the more …', both halves must use a comparative form: 'The harder you prepare, the calmer you feel.'"
         ]},
        {'label': 'Rule 3 — Calibrating your comparison: degree words that persuade',
         'text': [
             "Saying 'Course A is better than Course B' leaves your listener wondering: is it 2% better or 200% better? "
             "Adding a precise modifier in front of your comparative or superlative ('far more practical', 'slightly "
             "more expensive', 'by far the best') shows that you have weighed the evidence carefully."
         ],
         'formula': [
             "Large difference:  far / much / a great deal / значительно → significantly + comparative",
             "Small difference:  slightly / a little / marginally + comparative   ·   almost / nearly as … as",
             "Emphatic superlative:  by far + the + superlative   ·   easily + the + superlative"
         ],
         'examples': [
             "The evening train is slightly slower than the express bus, but it is far more comfortable.",
             "This year's results were not nearly as predictable as last year's.",
             "Deliberate speaking practice is by far the most effective way to build fluency."
         ],
         'remember': [
             "Always compare like with like: compare one city's climate with another city's climate ('The winter here is milder than in Bamyan' "
             "or 'than Bamyan's winter'), and back up every major comparison with 'because…'."
         ].copy()},
    ],
    'differences': [
        {'title': 'Comparative vs superlative — weighing two options vs crowning a standout',
         'rows': [
             ["This textbook is clearer than the one we used last term.", "This is the clearest textbook in the department library.", "Comparatives weigh options against each other; superlatives identify an extreme within a whole group or category."],
             ["The northern route isfar safer than the mountain pass in winter.", "The northern route is by far the safest option in winter.", "'Far' intensifies a comparative ('far safer'); 'by far' intensifies a superlative ('by far the safest')."],
         ], 'headers': ['Comparative (weighing choices)', 'Superlative (extreme in a group)', 'How the meaning shifts']},
        {'title': 'Small modifiers that flip the meaning of "as … as"',
         'rows': [
             ["The second exam was just as difficult as the first.", "The second exam was not nearly as difficult as the first.", "'Just as' means 100% equal in difficulty; 'not nearly as' means the second exam was much easier."],
             ["The sooner we start, the better.", "Sooner or later, we will have to start.", "'The sooner, the better' links speed to a better result; 'sooner or later' simply means 'eventually'."],
         ], 'headers': ['Expression A', 'Expression B', 'What your listener hears']},
        {'title': 'Turning a flat opinion into a persuasive comparison',
         'text': [
             "Whenever you compare two ideas in a speaking test or meeting, use this three-step formula: "
             "1. Degree modifier + comparative ('Studying in short daily sessions is far more effective than weekend cramming…') "
             "2. Concrete reason ('…because your brain consolidates memory between sessions…') "
             "3. Linked outcome ('…and the more consistently you review, the less you forget under exam pressure.')"
         ]},
    ],
    'practice_a': [
        "Taking the side street is __________ (short) than waiting at the main roundabout.",
        "Waiting six hours at a freezing bus station was __________ (bad) travel experience of my life.",
        "The __________ (much) you read in English, the __________ (fast) your vocabulary grows.",
        "She presented the team's findings __________ (confidently) than anyone expected.",
        "Repairing the old generator is not __________ expensive __________ buying a brand-new one.",
        "He is by far the __________ (talented) debater in our graduating class.",
    ],
    'practice_b': [
        "Rewrite using twice as … as: 'The new battery lasts two times longer than the old one.'",
        "Correct the mistake: 'My younger brother is more taller than me now.'",
        "Strengthen this comparison with 'far' and add a 'because' reason: 'Practising with a partner is better than studying alone.'",
        "Build a 'The more …, the more …' sentence of your own about building confidence in speaking.",
        "Correct the spelling/usage mistake: 'This dictionary is much clearer then my old one.'",
        "Compare three cities or towns you know: use a comparative to contrast two of them, and a superlative to name which one you would most like to live in and why.",
    ],
    'pair': {
        'intro': "Play 'The Persuasive Recommender'. Each partner has 30 seconds to recommend one choice in the same "
                 "category (for example, the best time of day to study, the best way to travel across the country, or "
                 "the most useful skill for a young graduate). Then debate your choices politely and agree on one "
                 "joint recommendation.",
        'task': [
            "In your recommendation, include at least: one comparative with a degree word (far, much, slightly), one superlative (or 'by far the…'), and one 'as … as' or 'the more …, the more …' sentence.",
            "Every comparison must be supported by a concrete reason ('because…'). Finish by agreeing on one winner together."
        ],
        'model': [
            "A: Studying early in the morning is far more productive than studying late at night because your mind is fresh and the house is quiet.",
            "B: Morning study is quieter, that's true, but for me evening study is just as effective as long as I turn off my phone. Still, I agree that the earlier you finish your hardest task, the better the rest of your day feels."
        ],
        'output': "Two 30-second recommendations, each containing at least three accurate comparisons "
                  "with reasons, followed by one agreed joint choice stated aloud.",
        'criteria': [
            "comparative and superlative forms are accurate (no double comparatives)",
            "every comparison is backed up by a clear reason",
            "uses at least two degree modifiers (far, much, slightly, by far, not nearly)",
            "reaches and states a polite joint recommendation at the end"
        ],
    },
    'advanced': {
        'intro': "In academic discussions and professional presentations, speakers rarely make one-sided comparisons; "
                 "instead, they acknowledge what the other option does well before showing why their choice is stronger.",
        'base': [
            "Master the irregular trios aloud until they are automatic: good / better / the best · bad / worse / the worst · far / further / the furthest.",
            "Practise pairing degree modifiers with real items in front of you: 'slightly heavier than', 'far more durable than', 'not nearly as complicated as'."
        ],
        'upgrade': [
            "Use emphatic superlative frames for confident evaluation: 'by far the most practical solution' · 'the single most important factor' · 'the least likely outcome'.",
            "Use concessive comparisons to sound fair and persuasive: 'While Option A is slightly cheaper upfront, Option B is far better value in the long run.'",
            "Use 'Compared with…' or 'In contrast to…' at the start of a sentence to frame evidence cleanly: 'Compared with five years ago, access to online courses has grown dramatically.'"
        ],
    },
    'realtalk': {
        'plan': "Take 30 seconds to pick one topic below and jot down three comparison keywords: one 'far / much + "
                "comparative', one 'by far + superlative', and one 'the more …, the more …' or 'twice as … as' pattern, "
                "plus one brief reason for each.",
        'task': "One-minute persuasion talk: Argue for your view on ONE of these questions — (1) What is the best age "
                "to start learning a second language? (2) What is the most effective way to prepare for a high-stakes "
                "speaking test? or (3) What is the smartest investment of one free hour every day?",
        'model': "In my view, early childhood is the easiest age to pick up natural pronunciation, because young children "
                 "imitate sounds far more effortlessly than adults and are much less afraid of making mistakes. However, "
                 "when it comes to using one hour a day as an adult learner, deliberate speaking practice is by far the "
                 "most valuable investment you can make. Speaking aloud with a partner is twice as effective as silent "
                 "review because you get immediate feedback when a sentence is unclear. Compared with memorizing word "
                 "lists alone, real conversation builds habits that last — and the more regularly you speak, the more "
                 "natural your grammar becomes.",
        'feedback': [
            "accurate comparative, superlative, and equality forms throughout",
            "every comparison is supported by a clear reason or example",
            "uses degree words naturally to calibrate strength (far, much, twice as, by far)",
            "closes with a memorable conclusion that answers the prompt directly"
        ],
    },
    'review': {
        'points': [
            "Comparatives compare two choices; superlatives identify an extreme within a group; 'as … as' expresses equality or multiples ('twice as fast as').",
            "'The + comparative …, the + comparative …' links two changing processes together.",
            "Degree modifiers ('far', 'much', 'slightly', 'by far') and 'because' reasons turn flat opinions into persuasive arguments."
        ],
        'retrieval': [
            "Make one comparison using 'far more … than' and one sentence using 'The more …, the more …'.",
            "Name three skills or subjects you have studied, rank them using superlatives, and give one reason for your top choice."
        ],
        'watch': [
            "'She is more taller than me.' → 'She is taller than me.' (Never use 'more' with an -er comparative.)",
            "'This route is faster then the highway.' → 'This route is faster than the highway.' ('Than' compares; 'then' marks time.)"
        ],
        'selfcheck': [
            "I can use comparatives, superlatives, and 'as … as' patterns accurately with degree modifiers.",
            "I can support my spoken comparisons with clear reasons and 'the more …, the more …' sentences."
        ],
        'answers': {
            'A': ["shorter", "the worst", "more / faster", "more confidently", "as / as", "most talented"],
            'B': ["The new battery lasts twice as long as the old one.",
                  "My younger brother is taller than me now.",
                  "Practising with a partner is far better than studying alone because you have to respond in real time. (answers vary)",
                  "answers vary (e.g. 'The more often you speak in class, the more confident you feel.')",
                  "This dictionary is much clearer than my old one.",
                  "answers vary"],
        },
    },
}

L8 = {
    'n': 8, 'part_no': 4, 'part_title': 'Compare and Persuade',
    'title': 'Linking Ideas and Building Arguments',
    'goal': 'organise opinions into coherent, well-linked spoken arguments',
    'intro': [
        "Have you ever listened to a speaker who had intelligent ideas, yet after thirty seconds you lost track of "
        "what they were trying to prove? Usually the problem is not their vocabulary — it is that their sentences "
        "arrive with no turn-signals.",
        "Linking words (although, despite, because of, therefore, for instance, to sum up) are the turn-signals of "
        "spoken English. They warn your listener in advance whether your next thought is a reason, a concrete example, "
        "a concession to the other side, or your final conclusion."
    ],
    'hook': [
        "Listen to the difference between these two ways of expressing the same view:",
        "•  Speaker A: 'Online courses are popular. Some students drop out. They miss classroom discussion. Online courses save travel time. I think blended learning is best.'",
        "•  Speaker B: 'Although online courses save valuable travel time, many students drop out because they miss live classroom discussion. Therefore, I believe a blended approach works best.'",
        "Read both versions aloud with a partner. Then speak for 30 seconds each on 'Why people in our city learn "
        "English' while your partner counts how many different linking expressions you use naturally.",
    ],
    'rules': [
        {'label': 'Rule 1 — Contrast and concession: although vs despite vs however',
         'text': [
             "When you want to show an unexpected contrast between two facts, English gives you three tools — and "
             "each tool requires a different grammatical package after it.",
             "Use 'although' or 'even though' before a full clause (subject + verb). Use 'despite' or 'in spite of' "
             "before a noun phrase or an -ing verb form (never a bare subject + verb). Use 'however', 'nevertheless', "
             "or 'on the other hand' to open a brand-new sentence (or clause after a semicolon), followed by a comma."
         ],
         'formula': [
             "Clause linker:  Although / Even though + subject + verb, main clause",
             "Noun / -ing linker:  Despite / In spite of + noun phrase or verb-ing, main clause",
             "Sentence connector:  First sentence. However, / Nevertheless, / On the other hand, second sentence."
         ],
         'examples': [
             "Although the snow was heavy, the morning bus arrived on schedule.  (subject 'the snow' + verb 'was')",
             "Despite the heavy snow, the morning bus arrived on schedule.  (noun phrase 'the heavy snow')",
             "Despite waking up with a migraine, she delivered her presentation clearly.  (-ing form)",
             "The proposal involves some initial risk. Nevertheless, the committee voted to approve it."
         ],
         'remember': [
             "Never mix 'despite' and 'in spite of' into 'despite of' — say either 'despite the delay' or 'in spite of the delay'.",
             "If you want to put a subject + verb after 'despite', insert 'the fact that': 'Despite the fact that it was snowing, we went out.'"
         ]},
        {'label': 'Rule 2 — Cause, result, and purpose: matching the grammar to the linker',
         'text': [
             "Just like contrast linkers, cause linkers divide into a clause family and a noun family. Use 'because', "
             "'since', or 'as' before a full clause (subject + verb); use 'because of', 'due to', or 'owing to' "
             "before a noun phrase.",
             "To introduce a logical consequence, use 'therefore', 'as a result', or 'consequently'. To express the "
             "purpose of an action, use 'in order to / to + base verb' or 'so that + subject + modal verb'."
         ],
         'formula': [
             "Cause (+ clause):  because / since / as + subject + verb   ·   Cause (+ noun):  because of / due to + noun phrase",
             "Result:  therefore / as a result / consequently   ·   Purpose:  in order to + verb  ·  so that + subject + can/could/will/would"
         ],
         'examples': [
             "We postponed the match because the pitch was flooded.  (+ full clause)",
             "We postponed the match because of / due to the flooded pitch.  (+ noun phrase)",
             "Public libraries extended their evening hours; as a result, student attendance doubled.",
             "I recorded the lecture so that my classmate could listen to it while recovering at home."
         ],
         'remember': [
             "Keep 'because' and 'therefore' in separate jobs: 'because' introduces the reason, while 'therefore' introduces the result. "
             "Do not use both to join the same two clauses."
         ]},
        {'label': 'Rule 3 — Building an argument you can deliver out loud',
         'text': [
             "When you are asked for your opinion in a meeting, interview, or speaking exam, do not just state what "
             "you think and stop. Give your listener a clear four-step architecture: state your Point, explain your "
             "Reason, make it concrete with an Example, and close with a short Link or Summary.",
             "Three well-connected sentences with a real example are far more persuasive than ten disconnected claims."
         ],
         'formula': [
             "1. POINT:  I firmly believe that … / In my view, …   →   2. REASON:  This is mainly because …",
             "3. EXAMPLE:  For instance, … / To give a concrete example, …   →   4. ADDITION:  Moreover, … / What is more, …"
         ],
         'examples': [
             "In my view, every university course should include short weekly presentations. This is mainly because "
             "graduates need to explain their ideas clearly at work. For instance, in my cousin's engineering firm, "
             "junior staff present project updates every Monday. Moreover, regular practice removes the fear of speaking in public."
         ],
         'remember': [
             "Acknowledge the other side briefly before stating your main point ('Although exams test individual memory, "
             "presentations prepare students for real teamwork') — a speaker who addresses counterarguments sounds fair and authoritative."
         ]},
        {'label': 'Rule 4 — Ordering points and landing a memorable summary',
         'text': [
             "When your listener cannot see your notes, verbal signposts ('First of all…', 'Another key factor is…', "
             "'To sum up…') act like headings for the ear and make your conclusion stick."
         ],
         'formula': [
             "Sequencing points:  First of all, …  ·  Secondly, …  ·  Another key point is that …",
             "Closing summary:  To sum up, …  ·  All in all, …  ·  In short, …"
         ],
         'examples': [
             "To sum up, the long-term benefits of staff training clearly outweigh the initial cost.",
             "All in all, I would recommend starting with a two-week pilot programme."
         ],
         'remember': [
             "Listeners remember the last sentence you say best — always finish an opinion talk with a crisp summary line."
         ]},
    ],
    'differences': [
        {'title': 'One contrast, three grammatical packages: although vs despite vs however',
         'text': [
             "See how the exact same idea changes its grammatical shape depending on which linker you choose:"
         ],
         'rows': [
             ["Although the traffic was heavy, we arrived on time.", "Despite the heavy traffic, we arrived on time.", "The traffic was heavy; however, we arrived on time.", "'Although' takes a subject + verb ('the traffic was'); 'Despite' takes a noun phrase ('the heavy traffic'); 'However' opens the second independent clause."],
         ], 'headers': ['although + clause', 'despite + noun / -ing', 'however + new clause', 'How the grammar works']},
        {'title': 'because (+ clause) vs because of (+ noun)',
         'rows': [
             ["Because she worked tirelessly, the clinic succeeded.", "Because of her tireless work, the clinic succeeded.", "Adding 'of' turns 'because' into a prepositional phrase, so it must be followed by a noun phrase ('her tireless work') rather than a verb."],
         ], 'headers': ['because + subject + verb', 'because of + noun phrase', 'What changes']},
        {'title': 'Direct contrast (while / whereas) vs concession (although)',
         'text': [
             "Use 'while' or 'whereas' when you are simply placing two different facts side by side on a scale: "
             "'My brother enjoys bustling city life, whereas I prefer quiet mountain towns.'",
             "Use 'although' or 'even though' when the first fact makes the second fact surprising: "
             "'Although I usually prefer quiet mountain towns, I really enjoyed my year working in the capital.'"
         ]},
    ],
    'practice_a': [
        "__________ the heavy morning traffic, everyone arrived at the examination centre on time.  (Despite / Although)",
        "__________ feeling exhausted after the night shift, she stayed to brief the morning nurse.  (Despite / Although)",
        "He failed his first driving test; __________, he practised every afternoon and passed the next month.  (however / despite)",
        "We left home at six in the morning __________ we could cross the pass before midday.  (so that / because of)",
        "The main highway was closed by snow. __________, all flights out of the valley were fully booked.  (As a result / Although)",
        "I prefer working in a quiet library, __________ my study partner learns best by discussing ideas aloud.  (whereas / despite)",
    ],
    'practice_b': [
        "Combine into one sentence using although: 'The assignment was challenging. Every group finished on time.'",
        "Combine into one sentence using despite + -ing (or a noun phrase): 'She was not selected the first time. She applied again the following year.'",
        "Correct the mistake: 'Despite of the high cost, the hospital purchased the new scanner.'",
        "Build a three-sentence spoken argument (Point → Reason → Example) supporting the statement: 'Reading widely improves spoken English.'",
        "Correct the mistake in two different ways: 'Although the rain, the football match continued.'",
        "State two brief advantages of technology in education, then close with a summary sentence starting with 'To sum up,' or 'All in all,'.",
    ],
    'pair': {
        'intro': "Hold a polite two-minute mini-debate with your partner on the motion below. First, Partner A "
                 "argues in favour and Partner B argues against; after two minutes, switch sides and argue the "
                 "opposite position so you practise seeing both sides of an issue.",
        'task': [
            "Debate motion: 'Written homework in language classes should be replaced by daily recorded speaking practice.'",
            "In each turn, follow the argument skeleton (Point → Reason → Example), acknowledge one point from your partner's side using 'Although…' or 'Despite…', and close with a clear summary sentence."
        ],
        'model': [
            "A: I believe daily speaking recordings are far more useful than traditional worksheets. This is because learners need active retrieval under real-time pressure. For instance, when I started recording a two-minute voice note every evening, I noticed my hesitation dropping within two weeks.",
            "B: Although voice recordings build fluency, written homework is still essential because it gives learners time to notice spelling and complex sentence structure..."
        ],
        'output': "One two-minute mini-debate per role: a clear point with reason and example, one "
                  "answer to the other side, and a closing summary — followed by a one-sentence "
                  "verdict you both accept.",
        'criteria': [
            "uses contrast and concession linkers accurately (especially despite + noun/-ing vs although + clause)",
            "follows a clear Point → Reason → Example structure",
            "acknowledges and responds to the partner's counterargument",
            "lands a clear closing summary before agreeing on a balanced verdict"
        ],
    },
    'advanced': {
        'intro': "Strong speakers do not use more linking words — they use the exact right linker to show how two "
                 "ideas relate, and they use concessive balance to win over skeptical listeners.",
        'base': [
            "Group your linkers by their job in conversation: contrast (although, despite, however, whereas) · cause (because, since, due to) · result (therefore, as a result) · example and summary (for instance, to sum up).",
            "Practise expressing the same real-life contrast in both grammatical shapes aloud: 'Although the course was demanding…' and 'Despite the demanding course…'."
        ],
        'upgrade': [
            "Use 'Not only … but also …' (with inversion when placed at the start of a formal sentence) to build momentum: 'Not only did the programme reduce costs, but it also improved staff morale.'",
            "Use two-step concessive frames to sound fair and measured in debates: 'It is certainly true that…; nevertheless, …' or 'Admittedly, the initial cost is high; even so, the long-term savings are substantial.'",
            "Use ', which…' at the end of a clause to comment on the whole consequence of an event: 'The director answered every question openly, which immediately put the staff at ease.'"
        ],
    },
    'realtalk': {
        'plan': "Take 45 seconds to write down four keywords only: your main claim, two reasons (with one real "
                "personal example in mind), and one concession to another viewpoint. Choose your four linkers "
                "before you start speaking (for example: because · for instance · although / despite · to sum up).",
        'task': "Ninety-second opinion talk: 'What makes a truly effective teacher or mentor?' State your main "
                "claim, support it with two reasons and a concrete example from your own experience, acknowledge "
                "one competing view, and finish with a memorable summary — without looking at notes.",
        'model': "I believe what makes a truly effective teacher is clear, honest feedback combined with patience. "
                 "This is because learners improve fastest when they know exactly what to adjust without feeling "
                 "discouraged. For instance, my first English instructor corrected our pronunciation habits every "
                 "day with a warm smile, and as a result our whole class gained confidence within a month. Although "
                 "entertaining games can make a classroom lively, I would trade entertainment for clear guidance "
                 "any day. To sum up, a great teacher shows you the next step clearly and makes you believe you can take it.",
        'feedback': [
            "clear Point → Reason → Example → Summary architecture throughout the talk",
            "accurate use of contrast/concession linkers (although + clause or despite + noun/-ing)",
            "natural cause and result connections (because, as a result, therefore)",
            "a crisp closing summary that leaves a clear final impression"
        ],
    },
    'review': {
        'points': [
            "Use 'although / even though' before a full clause (subject + verb); use 'despite / in spite of' before a noun phrase or -ing form; use 'however' to open a new sentence.",
            "Use 'because' before a clause and 'because of / due to' before a noun phrase; use 'therefore / as a result' for consequences.",
            "Build spoken arguments on a four-part skeleton: Point → Reason → Example → Summary."
        ],
        'retrieval': [
            "Deliver a 20-second argument on any everyday topic using 'because', 'for instance', and 'to sum up'.",
            "Express the same contrast idea in three ways aloud: once with 'although', once with 'despite', and once with 'however'."
        ],
        'watch': [
            "'Despite of the delay, we arrived.' → 'Despite the delay…' or 'In spite of the delay…' (Never say 'despite of'.)",
            "'Although the high price, we bought it.' → 'Despite the high price, we bought it' or 'Although the price was high, we bought it.'"
        ],
        'selfcheck': [
            "I can switch smoothly between clause linkers (although, because) and noun/-ing linkers (despite, because of).",
            "I can organize an unscripted 90-second opinion into a clear Point → Reason → Example → Summary structure."
        ],
        'answers': {
            'A': ["Despite", "Despite (followed by -ing; 'Although' needs a subject + verb: 'Although she felt exhausted')",
                  "however", "so that", "As a result", "whereas"],
            'B': ["Although the assignment was challenging, every group finished on time.",
                  "Despite not being selected the first time, she applied again the following year. / Despite the initial rejection, she applied again.",
                  "Despite the high cost, the hospital purchased the new scanner.",
                  "answers vary — must include a clear point, a reason, and an example",
                  "Despite the rain, the football match continued. / Although it was raining, the football match continued.",
                  "answers vary — must close with To sum up / All in all / In conclusion"],
        },
    },
}

LESSONS_5_8 = [L5, L6, L7, L8]


def render_all(doc, keys_registry):
    for L in LESSONS_5_8:
        render_lesson(doc, L, keys_registry)

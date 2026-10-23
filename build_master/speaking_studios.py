"""Original, reusable eight-unit speaking studios and aligned teacher guidance.

This is authored instructional content, not course-planning metadata for
students. All learners use the same tasks; teachers provide support as needed.
"""
UNITS = [
    {
        "unit": 1,
        "theme": "Communication",
        "name": "Make the Other Person Feel Heard",
        "mission": "Understand a partner's concern before suggesting a solution.",
        "can_do": "I can ask open questions, paraphrase a concern, clarify a misunderstanding and disagree respectfully.",
        "language": [
            "If I understand you correctly, the main concern is ...",
            "When you say ..., do you mean ...?",
            "Would you tell me a little more about ...?",
            "I see why that matters. Could we also consider ...?",
            "I may have missed something. Could you explain that last part?"
        ],
        "warmup": "Think of a time someone listened well to you, or invent a situation. What did the listener actually do? Compare behaviors rather than personalities.",
        "pair": {
            "title": "Plan a community event together",
            "setup": "Your class has one hour to organize a free event. A wants a lively speaking competition; B worries that quieter people will not participate. Neither person can approve a plan alone.",
            "roles": [
                "Partner A: Explain the value of a public speaking event, then ask about B's concerns before offering another idea.",
                "Partner B: Explain why a competition may exclude some participants. Give one practical alternative and ask A to summarize your point."
            ],
            "steps": [
                "Speak for 45 seconds each while the listener does not interrupt.",
                "Each person paraphrases the other's main concern and asks one open question.",
                "Negotiate a plan that keeps one strength from each proposal.",
                "Switch roles and try again with clearer follow-up questions."
            ],
            "target": "Agree on one plan and explain how it includes different participants."
        },
        "challenge": "Is understanding more important than agreeing? State a position, give a counterexample, and respond to one follow-up question.",
        "presentation": "Deliver a one-minute recommendation: 'Three habits that make difficult conversations better.' Begin with a real or fictional example; end with an action listeners can try today.",
        "model": [
            "A: I'd love a speaking contest. It could bring a lot of energy to the event.",
            "B: I understand the idea, but some learners might not feel comfortable performing.",
            "A: So your worry is that we might discourage people who need more practice. Is that right?",
            "B: Exactly. Could we include small-group speaking games as well?",
            "A: That makes sense. Let's begin in small groups and invite volunteers to share at the end."
        ],
        "feedback": "Notice whether you asked a real follow-up question, summarized your partner fairly and changed your response after hearing new information.",
        "transfer": "In your next discussion, ask one question before offering your own opinion. Afterwards, write down how the reply changed what you said.",
        "teacher": {
            "aim": "Observe listening as an interaction skill, not just a silent behavior.",
            "preteach": "Contrast 'Why didn't you...?' with 'What made that difficult?'; model a neutral paraphrase before corrective advice.",
            "pitfall": "Learners often respond with solutions before accurately restating the concern.",
            "correction": "Pause a pair and model 'What I'm hearing is ... Did I understand?' Invite the partner to confirm or repair the summary.",
            "support": "Offer one question stem and a sentence frame; remove the frame on the second round.",
            "stretch": "Require an accurate paraphrase of a position the learner disagrees with before rebuttal.",
            "evidence": "Listen for an open question, one paraphrase, one clarification and a negotiated final proposal."
        }
    },
    {
        "unit": 2,
        "theme": "Goals and habits",
        "name": "Turn a Goal into a Workable Plan",
        "mission": "Negotiate an ambitious goal while making the next step realistic.",
        "can_do": "I can describe a goal, specify an action, name an obstacle and suggest a fallback plan.",
        "language": [
            "My longer-term aim is ..., so this week I will ...",
            "A possible obstacle is ...; if that happens, I'll ...",
            "What would you change if your schedule became busier?",
            "That sounds ambitious. How could you make it manageable?",
            "Rather than measuring only the final result, we could track ..."
        ],
        "warmup": "Imagine you are mentoring a learner who wants to speak more confidently in English. What is the difference between a wish, a measurable action and a habit?",
        "pair": {
            "title": "Coach a learner with a busy schedule",
            "setup": "A wants to give a three-minute English presentation in six weeks but can practise only fifteen minutes on most days. B is a supportive classmate.",
            "roles": [
                "Partner A: Describe what you want and what could prevent you from practising. Ask for specific suggestions.",
                "Partner B: Ask about resources and time. Help A select two repeatable actions and one backup option."
            ],
            "steps": [
                "Ask three questions before giving advice.",
                "Agree on an action, a frequency and simple evidence of progress.",
                "Add an 'if ... then ...' fallback for a difficult day.",
                "Reverse roles with a different, fictional goal."
            ],
            "target": "Explain a plan that works even when the original schedule fails."
        },
        "challenge": "Could setting an ambitious target sometimes reduce motivation? Present the strongest argument for each side, then explain your own qualified view.",
        "presentation": "Give a 75-second 'plan under pressure' update to a team. Mention one goal, two actions, one risk and a reasonable revision.",
        "model": [
            "A: I want to speak without hesitation, but I usually stop practising after a few days.",
            "B: What part is hardest: finding time, choosing a topic or speaking in front of someone?",
            "A: Mostly finding time.",
            "B: Could you record a one-minute answer after dinner on four days? Then on Friday, listen and improve one sentence.",
            "A: Yes. If I miss dinner practice, I'll do the recording before I go to bed."
        ],
        "feedback": "Check that your plan contains an action someone can observe; 'be better' is a goal, not a practical next step.",
        "transfer": "Record an initial one-minute response today. Repeat the same prompt after several lessons and compare clarity, not only speed.",
        "teacher": {
            "aim": "Move from vague aspirations to feasible actions and respectful coaching.",
            "preteach": "Contrast 'I will practise more' with 'I will record a one-minute response on four evenings'.",
            "pitfall": "Advice becomes a lecture, or plans depend on ideal conditions.",
            "correction": "Ask the listener to replace every general suggestion with one action, a trigger and a fallback.",
            "support": "Give an 'If X happens, I'll do Y instead' frame; allow fictional goals.",
            "stretch": "Challenge the assumption that faster or more frequent practice always means better progress.",
            "evidence": "Listen for clarification questions, observable actions, a realistic obstacle and a contingency."
        }
    },
    {
        "unit": 3,
        "theme": "Emotional intelligence",
        "name": "Respond without Making the Conflict Worse",
        "mission": "Handle frustration in a project discussion with empathy and clear boundaries.",
        "can_do": "I can name the problem without blame, acknowledge a feeling, make a request and check agreement.",
        "language": [
            "I felt frustrated when ... because ...",
            "I can see this has been stressful.",
            "Could we focus on what needs to happen next?",
            "Would you be able to ... by ...?",
            "I agree with part of that, although I see ... differently."
        ],
        "warmup": "Read two responses to a late group member: 'You're always irresponsible' and 'We missed the deadline; what happened?' Which opens a better conversation? Explain why.",
        "pair": {
            "title": "Repair a group-project misunderstanding",
            "setup": "A and B are preparing a presentation. A thinks B did too little work. B believes the responsibilities were not clear. The deadline is tomorrow.",
            "roles": [
                "Partner A: Explain the effect of the delay without attacking B's character. Ask for a plan.",
                "Partner B: Acknowledge the impact, clarify what happened and offer a realistic commitment."
            ],
            "steps": [
                "State the observable situation before interpreting motives.",
                "Acknowledge one concern and ask one question.",
                "Negotiate who will prepare each remaining part and by when.",
                "Repeat the dialogue, making the second version calmer and more specific."
            ],
            "target": "Leave with a shared plan rather than a winner or loser."
        },
        "challenge": "Should students always speak openly about their feelings? Distinguish respectful honesty from oversharing, privacy and pressure to disclose.",
        "presentation": "Present a fictional workplace conflict in 60 seconds: what happened, two interpretations, a constructive response and the likely outcome.",
        "model": [
            "A: We still don't have the slides, and I'm worried about tomorrow's presentation.",
            "B: I understand. I thought I was responsible for the research, not the slide design.",
            "A: That explains the confusion. Could we divide the remaining work now?",
            "B: Yes. I can finish the sources tonight if you design the final slides.",
            "A: Let's check everything together in the morning."
        ],
        "feedback": "Prefer descriptions of actions to personal labels; check whether the final agreement is concrete.",
        "transfer": "Rewrite a blaming sentence as a calm observation plus a specific request. You may invent the situation.",
        "teacher": {
            "aim": "Build constructive disagreement; never treat a classroom role-play as counseling.",
            "preteach": "Model an 'I' statement that describes impact without claiming to know another person's intentions.",
            "pitfall": "Overusing 'you always' or demanding personal emotional disclosure.",
            "correction": "Invite fictional cases; reformulate 'You never help' as 'We missed one deadline'.",
            "support": "Allow a written first attempt, then rehearse the same response orally.",
            "stretch": "Require a charitable alternative interpretation and a boundary-setting request.",
            "evidence": "Record use of observed facts, acknowledgment, clear request and agreed next step."
        }
    },
    {
        "unit": 4,
        "theme": "Money and happiness",
        "name": "Decide What Matters When the Budget Is Tight",
        "mission": "Explain spending priorities and evaluate different definitions of value.",
        "can_do": "I can compare options, justify a budget decision, question assumptions and compromise.",
        "language": [
            "My first priority would be ... because ...",
            "We should distinguish an immediate need from a longer-term benefit.",
            "That may help, but it depends on ...",
            "We could reserve some money for ...",
            "Which option would benefit the most people?"
        ],
        "warmup": "A learning center receives an unexpected donation. Is a comfortable room, a library or a community event the best first use? There is no single correct answer.",
        "pair": {
            "title": "Allocate a small community grant",
            "setup": "A student group has a fictional budget of 30,000 afghanis. Options: repair a classroom fan (12,000), buy graded readers (10,000), hold an open speaking event (8,000), or reserve funds for future needs. You may adjust the figures as a hypothetical example.",
            "roles": [
                "Partner A: Protect essential improvements and explain the consequences of postponing repairs.",
                "Partner B: Make the case for materials and activities that encourage more students to participate."
            ],
            "steps": [
                "Define two decision criteria before choosing.",
                "Compare at least three uses of the money.",
                "Create an affordable combination or explain why one choice must wait.",
                "Present your decision and answer one challenging question."
            ],
            "target": "Agree on a budget whose total does not exceed 30,000 afghanis."
        },
        "challenge": "Does more money necessarily create more well-being? Distinguish financial security, personal experience and how money is used; avoid claiming there is one universal income threshold.",
        "presentation": "Deliver a 90-second funding recommendation with one figure, one trade-off, and a conclusion that respects different circumstances.",
        "model": [
            "A: I think we should repair the fan first. The room gets very hot, and learners cannot concentrate.",
            "B: I agree that's urgent, but books would help every class for years.",
            "A: We have 30,000 afghanis. What if we spend 12,000 on the repair and 10,000 on readers?",
            "B: Then we still have 8,000. We could run a simple speaking event or keep the money for emergencies.",
            "A: Let's reserve it until we know what the next priority is."
        ],
        "feedback": "Check your arithmetic, distinguish facts from preferences, and explain why someone might reasonably disagree.",
        "transfer": "Ask two classmates what 'good value' means to them. Report the two views without naming their personal finances.",
        "teacher": {
            "aim": "Teach qualified claims, budget reasoning and collaborative problem solving.",
            "preteach": "Demonstrate: 'This might improve participation' is safer than 'This will make everyone happy'.",
            "pitfall": "Learners treat money-versus-happiness as a universal moral lesson or ignore budget constraints.",
            "correction": "Ask pairs to distinguish a prediction from an observed fact and to total allocations aloud.",
            "support": "Give a simple four-row budget table; use fictitious finances only.",
            "stretch": "Introduce a hidden maintenance cost or an accessibility concern and invite a revised allocation.",
            "evidence": "Check totals, criteria, explicit trade-off, respectful counterargument and feasible conclusion."
        }
    },
    {
        "unit": 5,
        "theme": "Artificial intelligence",
        "name": "Use an AI Tool without Handing Over Your Judgment",
        "mission": "Decide when an AI-assisted answer is useful, uncertain or inappropriate.",
        "can_do": "I can explain a technology's benefit, identify a risk, request verification and defend a practical policy.",
        "language": [
            "The tool may help us with ..., but we still need to check ...",
            "What evidence supports that statement?",
            "We should not enter private information because ...",
            "A safer alternative would be ...",
            "I would allow this use only if ..."
        ],
        "warmup": "A student finds a polished AI-generated paragraph containing a quotation that cannot be verified. What should the student do before presenting it?",
        "pair": {
            "title": "Design a fair classroom AI agreement",
            "setup": "Your school is deciding how learners may use generative AI to prepare presentations. Some students want help with outlines; others worry about copying, made-up information and privacy.",
            "roles": [
                "Partner A: Propose two useful, limited uses of AI and explain how they support learning.",
                "Partner B: Explain two risks and propose checks that students can actually follow."
            ],
            "steps": [
                "Agree on a clear learning goal for the policy.",
                "Choose three permitted or restricted behaviors.",
                "Include one fact-checking rule and one privacy rule.",
                "Present the policy; the other pair tests it with a difficult scenario."
            ],
            "target": "Produce a short, understandable agreement that students can follow without specialist knowledge."
        },
        "challenge": "Does a fluent answer deserve trust? Explain the difference between convincing language, evidence and the reliability of an underlying source.",
        "presentation": "Give a 90-second school policy briefing: two opportunities, two risks and one simple rule. A partner must ask: 'How would we know it works?'",
        "model": [
            "A: AI could help students organize ideas before giving a talk.",
            "B: That sounds useful, but what if it invents a source?",
            "A: We should require students to check every quoted claim against the original source.",
            "B: And they shouldn't enter someone else's private information.",
            "A: Agreed. We can use it to prepare, but we remain responsible for what we say."
        ],
        "feedback": "Do not confuse fluency with factual accuracy. State how someone could test each proposed safeguard.",
        "transfer": "Find one claim in a tool-generated response and verify it with a reliable primary source before you repeat it.",
        "teacher": {
            "aim": "Develop careful, balanced reasoning instead of advertising or fearing technology.",
            "preteach": "Contrast 'the tool said' with 'the cited source supports'. Demonstrate a verification question without sharing personal data.",
            "pitfall": "Overconfident or entirely speculative claims about AI's present and future abilities.",
            "correction": "Ask for one specific use case, one failure mode and one testable safeguard.",
            "support": "Provide a policy table: allowed / not allowed / check needed.",
            "stretch": "Challenge whether a seemingly fair policy could disadvantage students with limited internet access.",
            "evidence": "Listen for qualified claims, fact-checking, a privacy rule and respectful consideration of access."
        }
    },
    {
        "unit": 6,
        "theme": "Relationships",
        "name": "Make Agreements that Protect Trust",
        "mission": "Set expectations and handle a small conflict without assuming bad intentions.",
        "can_do": "I can raise an issue calmly, explain a boundary, negotiate responsibilities and repair an agreement.",
        "language": [
            "When ..., the impact on me/the group is ...",
            "I want to understand how you saw it.",
            "Could we agree on ... for next time?",
            "I can do ..., but I can't promise ...",
            "Let's check whether this arrangement is working."
        ],
        "warmup": "Imagine two roommates disagree about shared chores. Which matters more for trust: an expensive apology or keeping a small promise? Explain.",
        "pair": {
            "title": "Negotiate shared responsibilities",
            "setup": "Two fictional roommates or club members share a workspace. One has done most of the cleaning. The other has a demanding schedule. Neither wants the arrangement to become unfair.",
            "roles": [
                "Partner A: Describe the workload and suggest one fair boundary without blaming the other person.",
                "Partner B: Explain a realistic constraint, propose a fair share and say what you can reliably do."
            ],
            "steps": [
                "Name the concrete problem, not the other person's character.",
                "Ask about a constraint you may not know.",
                "Write two specific responsibilities and a time to review them.",
                "Practise what you would say if one promise was missed."
            ],
            "target": "Reach an agreement that both people could realistically keep."
        },
        "challenge": "Is compromise always fair? Consider cases where one person repeatedly gives up something important. Discuss how a respectful boundary differs from selfishness.",
        "presentation": "Describe a fictional trust-building agreement: the problem, the request, a compromise and a method for checking progress.",
        "model": [
            "A: I've cleaned the shared room on the last three weekends, and I'd like us to share the work.",
            "B: I'm sorry. I have classes on Saturdays, so I can't come then.",
            "A: Could you take care of it on Sunday instead?",
            "B: Yes, and I can also buy the cleaning supplies this week.",
            "A: That works. Let's review the plan next weekend."
        ],
        "feedback": "Check for a specific request, a realistic promise and respect for different circumstances.",
        "transfer": "Write two sentences: one boundary you could express politely and one way to check agreement. Use a fictional example if you prefer.",
        "teacher": {
            "aim": "Build respectful negotiation without requiring students to disclose real relationship experiences.",
            "preteach": "Contrast a boundary ('I can't stay late') with an accusation ('You don't care').",
            "pitfall": "Assuming compromise requires one person to give in or treating a private personal story as required class material.",
            "correction": "Use the shared-room scenario and ask for two actions that both speakers can control.",
            "support": "Offer a three-turn scaffold: situation, request, agreement.",
            "stretch": "Add a missed commitment and require a non-defensive repair.",
            "evidence": "Look for calm observation, boundaries, reciprocal responsibility and an explicit review point."
        }
    },
    {
        "unit": 7,
        "theme": "Globalization",
        "name": "Explain a Global Choice with Local Consequences",
        "mission": "Weigh the opportunities and risks of an interconnected supply chain.",
        "can_do": "I can describe a connection between local and global events, compare trade-offs and propose a balanced response.",
        "language": [
            "One possible benefit is ..., whereas a risk is ...",
            "For people in our community, this could mean ...",
            "In the short term ..., but over time ...",
            "What would happen if that connection failed?",
            "We could reduce the risk by ..."
        ],
        "warmup": "A classroom uses an imported device that is useful but difficult to repair locally. Discuss what the connection makes possible and what could go wrong.",
        "pair": {
            "title": "Keep a learning center supplied",
            "setup": "A learning center buys essential materials through a distant supplier. Delivery is cheaper but less predictable than buying locally. You must recommend a purchasing policy for the next term.",
            "roles": [
                "Partner A: Argue for a broad choice of affordable international materials.",
                "Partner B: Argue for reliability, local services and a backup plan."
            ],
            "steps": [
                "Define three criteria: cost, reliability and access.",
                "Give a grounded reason for each option.",
                "Propose a mixed approach or explain a justified preference.",
                "Respond to a challenge about what happens if deliveries stop."
            ],
            "target": "Explain who benefits, who bears risks and how the plan can be made more resilient."
        },
        "challenge": "Can globalization increase opportunity and inequality at the same time? Support both parts of your answer without assuming all countries or communities are affected alike.",
        "presentation": "Give a 90-second briefing: a global connection, a local consequence, a possible risk and one practical policy response.",
        "model": [
            "A: Buying overseas could give students more choice at a lower price.",
            "B: Yes, but we may face long delays if a shipment is interrupted.",
            "A: Could we buy the most urgent supplies locally and order specialist materials internationally?",
            "B: That would cost a little more now, but it gives us a backup.",
            "A: Let's recommend that mixed approach and explain the trade-off."
        ],
        "feedback": "Avoid sweeping statements such as 'globalization helps everyone'. Distinguish possible effects from established local facts.",
        "transfer": "Choose an everyday object and describe one cross-border connection and one consequence if it were interrupted.",
        "teacher": {
            "aim": "Move from slogans to concrete causal explanations and respectful trade-off analysis.",
            "preteach": "Model a 'because / therefore / however' chain using a familiar imported school resource.",
            "pitfall": "Presenting global interdependence as uniformly good or bad.",
            "correction": "Ask: 'For whom? In which circumstance? Over what time period?'",
            "support": "Give a simple two-column benefit/risk chart.",
            "stretch": "Introduce an unforeseen supply interruption and ask groups to revise their decision transparently.",
            "evidence": "Listen for a concrete example, at least two competing criteria and a contingency."
        }
    },
    {
        "unit": 8,
        "theme": "English and opportunity",
        "name": "Make Your English Work for Your Message",
        "mission": "Defend an inclusive communication policy and deliver a final evidence-based talk.",
        "can_do": "I can explain a fair policy, respond to disagreement, speak clearly and repair misunderstanding without pretending to have a native accent.",
        "language": [
            "The purpose of the requirement should be ...",
            "Clear communication is not the same as a particular accent.",
            "A fairer option might be ...",
            "I recognize that concern; however ...",
            "Let me rephrase my point more clearly."
        ],
        "warmup": "Imagine a talented applicant with excellent subject knowledge who communicates in understandable English but has a strong local accent. What should an interview assess?",
        "pair": {
            "title": "Design a fair admissions interview",
            "setup": "A scholarship committee wants evidence that applicants can study and communicate effectively. It also wants to avoid unnecessary barriers for people whose education was interrupted or expensive.",
            "roles": [
                "Partner A: Defend a practical minimum level of communication needed for successful study.",
                "Partner B: Propose a fair way to assess communication without demanding an imitation of one accent."
            ],
            "steps": [
                "Agree on the real purpose of the interview.",
                "Develop two observable communication criteria and one opportunity to clarify an answer.",
                "Present a policy and give one example of a fair adjustment.",
                "Switch roles; each person must explain the strongest point made by the other."
            ],
            "target": "Recommend an understandable assessment policy rather than a rule based on identity or prestige."
        },
        "challenge": "Should intelligibility matter more than accent similarity? Identify a limitation to your answer and respond to an alternative perspective.",
        "presentation": "Capstone: deliver a 90-second argument on a question from any unit. Open with your position, give a specific example, acknowledge another view and end with a practical implication. Then answer two unscripted follow-up questions.",
        "model": [
            "A: We need to know whether applicants can take part in classes, but a native-like accent doesn't prove that.",
            "B: I agree about accents. How could an interviewer assess understanding fairly?",
            "A: Give everyone the same task and let them ask for clarification if they need it.",
            "B: That would test real interaction, although the task still needs clear scoring criteria.",
            "A: Exactly. Let's assess whether the message is understandable and the person can respond."
        ],
        "feedback": "Review how well you delivered a message, connected ideas, listened and repaired misunderstanding—not whether you sounded like someone from another country.",
        "transfer": "Save your final talk and the feedback you received. Set one precise goal for your next real-life English conversation.",
        "teacher": {
            "aim": "Conduct an evidence-based final performance while respecting accent and linguistic identity.",
            "preteach": "Model a clarification repair ('What I mean is ...') and distinguish it from apologizing for an accent.",
            "pitfall": "Rewarding memorized complexity or accent imitation instead of intelligible, responsive communication.",
            "correction": "Score the same four rubric criteria for all learners and note observable evidence, not vague impressions.",
            "support": "Allow a small outline card and two minutes to organize thoughts; never require disclosure of personal educational barriers.",
            "stretch": "Ask an unscripted objection, then assess qualified response and self-repair.",
            "evidence": "Record a 90-second argument and two responses; compare criterion-specific evidence with earlier performances."
        }
    }
]

COMMON_RUBRIC = [
    ("Message and reasoning", [
        "4: Clear, relevant position supported by specific reasoning and a considered alternative.",
        "3: Clear main point with a relevant reason and example.",
        "2: Main point sometimes unclear or weakly supported.",
        "1: Message difficult to identify despite support."
    ]),
    ("Listening and interaction", [
        "4: Responds directly, checks understanding, and advances the exchange naturally.",
        "3: Responds to partner and asks or answers relevant follow-up questions.",
        "2: Some response, but frequently misses questions or changes subject.",
        "1: Minimal interaction even with clear prompts."
    ]),
    ("Language choices", [
        "4: Language is sufficiently accurate, varied and appropriate to meaning; errors rarely affect understanding.",
        "3: Meaning usually clear despite some errors; vocabulary mostly fits the situation.",
        "2: Repeated errors or restricted choices sometimes obscure meaning.",
        "1: Language limitations frequently prevent intended meaning."
    ]),
    ("Delivery and repair", [
        "4: Understandable pacing and pronunciation; independently clarifies or repairs misunderstandings.",
        "3: Generally understandable with some hesitation; repairs when prompted.",
        "2: Frequent long pauses or unclear stretches; repair requires substantial help.",
        "1: Limited understandable output; repair rarely succeeds even with support."
    ])
]

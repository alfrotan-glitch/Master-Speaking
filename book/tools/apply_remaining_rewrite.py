#!/usr/bin/env python3
"""Prepare guarded source edits for the remaining-unit editorial pass.

One-shot authoring utility, not part of the release pipeline. Refuses to run
if this pass has already been applied. Changes do not fabricate media or keys.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]


def load(path):
    return json.loads((ROOT / path).read_text())


def save(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def main():
    marker = ROOT / 'book/master/remaining-rewrite-plan.json'
    if marker.exists():
        raise SystemExit('Remaining rewrite already prepared; do not apply it twice.')
    book = load('book/artifacts/book.json')
    edits = load('book/master/reviewed-edits.json')
    front = load('book/master/reviewed-front-edits.json')
    changes = []
    # These are applied after the chapter edit register. Do not edit their
    # output through an earlier reconstruction stage.
    protected = set()
    for repair in load('book/master/structural-repairs.json'):
        protected.add(repair.get('anchor', ''))
        protected.add(repair.get('text', ''))
        protected.add(repair.get('expected_tail', ''))
        protected.update(b.get('text', '') for b in repair.get('blocks', []))
    protected.update(['Sources Used', 'Reflect and Try Again'])

    def change(u, c, old, new, reason, column=None):
        if old == new:
            return
        candidates = [e for e in edits if (e['unit'], e['chapter']) == (u, c)
                      and e.get('correction') == old and e.get('table_column') == column]
        if candidates:
            if len(candidates) != 1:
                raise ValueError(('Ambiguous previous edit', old))
            candidates[0]['correction'] = new
            candidates[0]['reason'] += ' Whole-book rewrite: ' + reason
        else:
            if column is None and old in protected:
                return
            block_values = [b.get('text') for b in book['units'][u-1]['chapters'][c-1]['blocks']]
            count = block_values.count(old) if column is None else 1
            if count != 1:
                # Repeated identical directions require individually authored
                # occurrence guards, not a blind text substitution.
                return
            row = {'unit': u, 'chapter': c, 'original': old, 'correction': new,
                   'reason': 'Whole-book rewrite: ' + reason}
            if column is not None:
                row['table_column'] = column
            edits.append(row)
        changes.append({'unit': u, 'chapter': c, 'original': old, 'correction': new,
                        'reason': reason, 'column': column})

    readings = load('book/master/remaining-reading-rewrites.json')
    for unit in book['units'][1:]:
        old = [b['text'] for b in unit['chapters'][0]['blocks'] if b['k'] == 'reading']
        new = readings[str(unit['number'])]
        if len(old) != len(new):
            raise ValueError('Reading paragraph count changed')
        for a, b in zip(old, new):
            change(unit['number'], 1, a, b,
                   'Recompose the full paragraph for a clearer argument, concrete explanation, qualified claims and alignment with the lesson questions.')

    directions = {
        'Discuss.': 'Discuss the questions with a partner. Give a reason or an example for each answer.',
        'Discuss:': 'Discuss the question. Explain your view and ask about a different perspective.',
        'Discuss the questions with your partner.': 'Discuss the questions with a partner. Take turns giving a reason and asking a follow-up question.',
        'Discuss the following questions with your partner.': 'Take turns discussing the questions. Give a reason for your view, then ask your partner to explain theirs.',
        'Discuss the following questions.': 'Discuss the questions. Support your answers with reasons or examples, and make room for a different view.',
        'Discuss the following questions in groups.': 'Discuss the questions in a small group. Take turns and build on a point made by someone else.',
        'Work in groups. Discuss the following questions.': 'Discuss the questions in a small group. Explain your view and respond to someone else’s reason.',
        'Work in groups of 3–4 students. Discuss the following questions.': 'Discuss the questions in groups of three or four. Give everyone a turn and ask for clarification when a point is unclear.',
        'Discuss the questions in pairs or small groups.': 'Discuss the questions in pairs or small groups. Give a reason, listen to another view, and explain any point you reconsider.',
        'Choose the best answer.': 'Choose the answer best supported by the recording, not the one you personally agree with.',
        'Answer in complete sentences.': 'Answer in complete sentences. Use the reading for text-based questions; give reasons for questions asking your opinion.',
        'Answer the questions in complete sentences.': 'Answer in complete sentences. Distinguish what the speaker says from your own interpretation.',
        'Student A: Summarize the reading in one minute.': 'Student A: Give a one-minute summary in your own words. Include the main idea and a supporting example.',
        'Student B: Listen carefully and ask two follow-up questions.': 'Student B: Listen for the main point, then ask two follow-up questions. Switch roles and use one response to improve your summary.',
        'Student A summarizes the article in one minute.': 'Student A: Give a one-minute summary in your own words. Include the main idea and a supporting example.',
        'Student B listens and asks two follow-up questions.': 'Student B: Ask two follow-up questions about the summary. Switch roles, then revise one unclear explanation.',
        'Study the expressions below. Try using them to explain and develop your ideas.': 'Read the expressions and examples. Choose language that fits your meaning, then try it in a short explanation of your own.',
        'Study the following expressions before listening.': 'Read the expressions and examples before listening. Predict which might connect with the topic; check your prediction afterwards.',
        'Focus on key ideas, examples, reasons. Do not try to write every word.': 'Note the main ideas, reasons, and examples. Use short phrases rather than trying to copy every word.',
        'Work in pairs. Choose 10 expressions and create a short conversation using all ten.': 'With a partner, choose ten toolbox expressions and plan a short conversation using all ten. Give each speaker a reason to respond, not just a list of phrases.',
        'Work in groups of 3–4 students. Use at least eight expressions from the Speaking Toolbox.': 'Discuss in groups of three or four. Use at least eight toolbox expressions across the discussion, making sure they fit the point you are making.',
        'Learn these expressions before preparing your presentation.': 'Choose expressions for introducing, developing, and concluding your presentation. Practise them with ideas from your own topic.',
        'Use one of the presentation expressions.': 'Use a presentation expression to introduce your point, then complete it with your own idea.',
        'Write three main points.': 'Write three main points. Add a supporting detail or example to each.',
        'Speak clearly.': 'Aim for a clear message and a comfortable pace; pause when the audience needs time to follow.',
        'Give one personal example.': 'Give one personal or fictional example, and make clear which kind it is.',
        'Give one real-life example.': 'Give one identifiable real-life example. Explain how it supports your point.',
        'Give one real-life example to support your opinion.': 'Support your opinion with one real-life example and explain the connection.',
        'Present at least two research findings.': 'Present at least two findings from identifiable sources. Explain what they support and any limits you notice.',
        'Conduct research before your presentation.': 'Investigate your question before presenting. Keep notes linking each claim to its source.',
        'Use at least three reliable sources, such as books, academic articles, TED or TED-Ed talks, university websites, interviews with successful people': 'Use at least three sources. Check the author’s relevant knowledge, the evidence, the date, and the purpose; a familiar website or a successful person is not automatically reliable.',
        'Prepare a 4–5 minute presentation using the outline below.': 'Prepare a four- to five-minute presentation using the outline. Select evidence that answers your question and practise keeping within the time.',
        'Each student should speak for one minute.': 'Give each speaker one minute to present a reason and an example, then invite a response from the other side.',
        'Prepare a 2-minute oral summary of today’s reading.': 'Prepare a two-minute summary in your own words. Explain the main idea, include a supporting example, and avoid reading a full script.',
        'Read the following sentences aloud. Pause naturally where it makes sense.': 'Read aloud, using the marked pauses as a starting point. Try another grouping and notice how it changes the emphasis.',
        'Read the following sentences aloud with appropriate intonation.': 'Choose an intention for each sentence, then read it aloud. Try a different tone and explain how the meaning changes.',
        'Use a falling tone when:': 'A falling tone can suit these purposes; the meaning and situation still matter:',
        'Read the sentences aloud.': 'Read the sentences aloud. Make the stressed syllables easy to hear without rushing the rest.',
        'Learn these words before reading.': 'Read the meanings and examples. Use two of the words or phrases in examples of your own before starting the reading.',
        'Use at least six expressions from Vocabulary Preview.': 'Use at least six words or phrases from Vocabulary Preview. Choose them for their meaning, not simply to reach the number.',
        'Use at least six expressions from Vocabulary Preview to explain your understanding of the quote.': 'Use at least six words or phrases from Vocabulary Preview to explain the quotation. Distinguish its message from your own judgment.',
        'Choose one position and defend it with at least three arguments.': 'Choose a position and support it with at least three arguments. Explain the assumptions behind any prediction.',
        'Choose one of the following topics.': 'Choose one topic below and narrow it to a question you can investigate in the time available.',
        'Prepare three strong arguments.': 'Prepare three arguments, each with a reason and supporting example or evidence.',
        'Use at least five expressions from today’s vocabulary.': 'Use at least five toolbox expressions accurately as you develop and respond to arguments.',
        'Present three main arguments.': 'Present three main arguments and explain the reason supporting each.',
        'Give at least one real-world example.': 'Give at least one identifiable real-world example; explain what it shows and what it does not establish.',
        'Rank the six ingredients from 1 (most important) to 6 (least important).': 'Rank the six ingredients from 1 to 6 for a fictional relationship. Explain your priorities rather than treating one ranking as the correct answer.',
        'After discussing with your group, would you change your ranking?': 'Review your ranking after the discussion. Explain why you would change it or keep it.',
        'Give a 1-minute response and support your opinion with at least two reasons and one example.': 'Give a one-minute response with at least two reasons and an example. Make your position clear before adding details.',
        'After a voiceless sound such as /k/, /p/, /s/, /ʃ/, /tʃ/, and /f/.': 'After voiceless sounds other than /t/, including /k/, /p/, /s/, /ʃ/, /tʃ/, and /f/.',
        'After a voiced sound such as /b/, /g/, /v/, /z/, /m/, /n/, /l/, and vowels.': 'After voiced sounds other than /d/, including /b/, /g/, /v/, /z/, /m/, /n/, /l/, and vowels.',
        'Read these pairs:': 'Read each pair and notice which sound is voiced. Keep the vowel separate from the consonant contrast.',
        'First slowly, then naturally.': 'Start slowly, then use a comfortable speaking pace without losing the sound contrast.',
        'Choose one and explain your choice.': 'Choose a response and explain your reasoning. Consider one possible objection before deciding.',
        'Prepare 3 arguments supporting the statement.': 'Prepare three arguments supporting the statement, with a reason or example for each.',
        'Prepare 3 arguments against it.': 'Prepare three arguments against the statement, with a reason or example for each.'
    }
    for unit in book['units']:
        for chapter in unit['chapters']:
            u, c = unit['number'], chapter['number']
            if (u, c) == (1, 1):
                continue
            for block in chapter['blocks']:
                old = block.get('text', '')
                if block['k'] == 'instr' and old in directions:
                    change(u, c, old, directions[old], 'Make the action, evidence or interaction explicit while retaining the original task purpose and required quantities.')
                if c == 4 and block['k'] == 'p':
                    template = {
                        'According to research,...': 'According to [author or organization],...',
                        'Studies have shown that...': 'In [study title], [author] reports that...',
                        'Experts believe that...': '[Named source] argues that...',
                        'Don’t pronounce every word separately. Connect words that naturally belong together.': 'Try linking the marked phrases while keeping the words clear. Separate words when that helps you make a contrast.'
                    }
                    if old in template:
                        change(u, c, old, template[old], 'Teach source-specific attribution or meaning-led pronunciation instead of vague authority or an absolute delivery rule.')

    # Align changed readings and remove leading/overgeneralized premises.
    targeted = [
        (2, 1, 'Successful people review their progress regularly.', 'Reviewing progress can help people decide how to adjust their plans.'),
        (4, 1, 'According to the passage, which type of spending often brings greater happiness?', 'Which kind of spending does the passage discuss as a possible source of shared memories?'),
        (4, 1, '_____ Research suggests that earning more money always increases happiness.', '_____ The passage claims that earning more money always increases happiness.'),
        (6, 1, '_____ Daniel Goleman identified five components of emotional intelligence.', ''),
        (8, 1, 'Why has the internet increased the importance of English?', 'How has technology helped people use English across borders?'),
        (3, 3, 'Student B acts as an Emotional Intelligence Coach. Give advice using at least six expressions from the Speaking Toolbox. Explain how the person can manage their emotions, communicate effectively, and solve the problem.', 'Student B is a supportive conversation partner, not a counsellor. Use at least six toolbox expressions to ask questions, acknowledge feelings, and suggest a possible next step. Do not diagnose the person or assume one response will solve the problem.'),
        (4, 3, 'Do you think wealthy people are under more pressure than ordinary people? Explain.', 'How might financial pressures differ for people with high and low incomes? Give an example without assuming everyone in either group has the same experience.'),
        (6, 1, 'What are your criteria for marriage?', 'What qualities matter in a respectful relationship? Use a fictional marriage, friendship, or team.'),
        (8, 3, 'Can English completely bridge a language gap, or are cultural differences still a problem?', 'How can English help bridge a language gap, and what cultural understanding might still be needed?')
    ]
    for u, c, old, new in targeted:
        if new and any(b.get('text') == old for b in book['units'][u-1]['chapters'][c-1]['blocks']):
            change(u, c, old, new, 'Keep questions answerable from the rewritten passage or remove an unnecessary social assumption.')
    table_edits = [
        (3, 1, 2, 'Recent studies have challenged the assumption that money guarantees happiness.', 'Her experience challenged the assumption that more money would solve every problem.'),
        (3, 1, 2, 'Hard work is often a more reliable predictor of success than natural talent.', 'One exam score is not a reliable predictor of success in every field.'),
        (3, 3, 1, 'become upset when receiving feedback', 'treat criticism of your work as an attack on you personally'),
        (3, 3, 2, 'Successful people don’t take criticism personally; they learn from it.', 'She tried not to take criticism personally and asked for a specific example.'),
        (4, 3, 2, 'People who live within their means usually experience less financial stress.', 'Planning purchases helps me live within my means.'),
        (5, 3, 1, 'make a task be done automatically by technology', 'use technology to carry out a task automatically'),
        (6, 1, 1, 'beliefs about what is unlikely or impossible', 'expectations that are unlikely to be met in the circumstances')
    ]
    for u, c, col, old, new in table_edits:
        change(u, c, old, new, 'Improve the definition or use a concrete example without an unsupported research or success claim.', col)

    # Front-guide paths are applied after the existing authored guidance.
    front_changes = [
        (['howto','paras',1], 'Use this book to practise explaining, questioning, discussing, and presenting ideas in English.'),
        (['howto','paras',2], 'Each unit gives you several ways to explore a topic. You are not expected to produce a perfect answer. Prepare your ideas, speak in your own words, and use feedback to make the next attempt clearer.'),
        (['howto','chapters',0,'desc'], 'Explore the unit’s topic through a reading, vocabulary, questions, and speaking activities.'),
        (['howto','chapters',0,'you_will',3], 'use personal or fictional examples'),
        (['howto','chapters',1,'desc'], 'Use the assigned talk or video to practise listening for a main message, supporting details, and the speaker’s position.'),
        (['howto','chapters',3,'desc'], 'Develop a focused research question and present an answer supported by identifiable sources.'),
        (['howto','closing'], 'At the end of a unit, return to its main question. Explain your position, support it with reasons or evidence, and notice one thing you can now communicate more clearly.')
    ]
    for path, new in front_changes:
        current = book['front']
        for key in path:
            current = current[key]
        prior = [e for e in front if e['path'] == path]
        if prior:
            if len(prior) != 1:
                raise ValueError('Ambiguous front edit')
            prior[0]['correction'] = new
            prior[0]['reason'] += ' Whole-book rewrite: make the guide concrete and avoid unsupported progression or outcome promises.'
        else:
            front.append({'path':path,'original':current,'correction':new,
                          'reason':'Whole-book rewrite: clarify the learner’s action and purpose without promising a certified level or requiring personal disclosure.'})
    save('book/master/reviewed-edits.json', edits)
    save('book/master/reviewed-front-edits.json', front)
    save('book/master/remaining-rewrite-plan.json', {'scope':'Substantive editorial revision across all remaining units; not an independent every-word proof.', 'changes': changes})
    print('Prepared', len(changes), 'remaining-unit changes, plus', len(front_changes), 'guide revisions.')


if __name__ == '__main__':
    main()

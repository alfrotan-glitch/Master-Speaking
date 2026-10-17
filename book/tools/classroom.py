#!/usr/bin/env python3
"""Build separate student/teacher packs from authored classroom sources.

Original videos remain unverified. Never map the new listening keys to them.
Run: python book/tools/classroom.py && python book/tools/qa_classroom.py
"""
import json
import csv
from pathlib import Path
from companion import build, ROOT

SOURCE = ROOT / 'book/classroom'
LABELS = ['Chapter 1 · Reading into speaking', 'Chapter 2 · Listening and clarification',
          'Chapter 3 · Discussion', 'Chapter 4 · Presentation and questions']
STUDENT_STEM = 'Master-Speaking-Student-Practice-Pack'
TEACHER_STEM = 'Master-Speaking-Teacher-Implementation-Pack'


def compose():
    modules = json.loads((SOURCE / 'modules.json').read_text())
    key = json.loads((SOURCE / 'unit1-reading-key.json').read_text())
    student = ['# Master Speaking', '## Student Practice Pack',
               'New supplementary practice • October 2026',
               'Use this pack with the book and Class Companion. It adds chapter success checklists, short speaking models, and questions for eight new teacher-read listening alternatives. These alternatives do not use the book’s original video questions.',
               'The models and listening stories are newly authored fictional teaching examples. A model shows one possible way to communicate; it is not a script to memorize or the only acceptable opinion. These short responses do not meet every full-length presentation requirement in the book.',
               'Start by trying a task in your own words. Study the model, notice one useful move, then try again with a different example. Use keywords rather than copying whole sentences.',
               'For each checklist, mark N = not yet, S = with support, or I = independently. Add a specific example of what you said or understood. These are local practice goals, not certified proficiency descriptors. Personal disclosure and recording are optional.']
    for index, module in enumerate(modules):
        student.append(f"## {2 * index + 1}. Unit {module['unit']} • {module['title']}")
        student.append('Chapter success checklists — mark N / S / I after the matching lesson.')
        for label, goals in zip(LABELS, module['goals']):
            student.append('### ' + label)
            student.extend('- ___ ' + goal for goal in goals)
            student.append('Evidence from my attempt: _______________________________________')
        student.append('### Short model exchange — notice the moves, not just the words.')
        student.extend(module['dialogue'])
        student.append('Notice: ' + module['notice'])
        student.append('### Short model response — an example to analyze, not a full timed assignment.')
        student.append(module['response'])
        student.append('### Language support')
        student.extend('- ' + phrase for phrase in module['frames'])
        student.append('Your turn: ' + module['transfer'])
        student.append('First attempt → feedback → second attempt: change one thing, then explain whether it helped your listener.')
        student.append(f"## {2 * index + 2}. Unit {module['unit']} • New listening worksheet")
        student.append(module['listening']['title'])
        student.append('Input: a new fictional teacher-read story, not the original book video. Listen before you see the script. Use this worksheet only with the matching story in the Teacher Implementation Pack.')
        student.append('First listening — gist: What is the main problem or decision? Give a one-sentence answer.')
        student.append('My gist note: ___________________________________________________')
        student.append('Second listening — details: read the questions, listen again, and answer in short phrases.')
        for number, question in enumerate(module['listening']['questions'], 1):
            student.append(f"{number}. {question['prompt']}")
            student.append('Answer: ________________________________________________________')
            student.append('_______________________________________________________________')
        student.append('Partner check: Which answer are you least certain about? Say what you need to hear again.')
        student.append('After checking: tell the story’s main problem and response in your own words. You may now use the script if the teacher provides it.')
        student.append('Input/support record: teacher read / other: __________  Replays: ___  Transcript before listening? yes / no')
        student.append('One thing I understood: __________  One next listening goal: __________')
    student.extend(['## 17. Practice record and feedback',
                    'Name or learner code: __________  Unit/date: __________',
                    'Task: __________  Preparation time: ___  Speaking time: ___',
                    'My first attempt: What was my main point? _________________________',
                    'A question I asked or answered: ___________________________________',
                    'Feedback I can use: ______________________________________________',
                    'Change in my second attempt: _____________________________________',
                    'Evidence that it helped, or why I am still unsure: __________________',
                    'My next small goal and review date: _______________________________',
                    'For the Unit 1 pilot: Which instruction was unclear? Which activity helped you speak? What support did you need? You may give private feedback to the teacher. No real personal story or recording is required.'])
    teacher = [(SOURCE / 'teacher-notes.md').read_text().strip()]
    section = None
    for item in key:
        if item['section'] != section:
            section = item['section']
            teacher.append('### ' + section)
        teacher.extend([f"### Question: {item['stem']}", f"Answer / acceptable content: {item['answer']}",
                        f"Reason: {item['why']}", f"Text evidence: “{item['evidence']}”"])
    for index, module in enumerate(modules):
        listening = module['listening']
        teacher.append(f"## {7 + index}. Unit {module['unit']} • Original teacher-read alternative")
        teacher.extend([module['title'] + ' — ' + listening['title'],
                        'Fictional teaching script, newly authored for this pack. It is not the original video transcript and does not answer the original book’s listening exercise.',
                        f"Delivery: read the following {len(listening['script'].split())}-word script twice using Section 1. Do not give students the script or key before the first listening unless an access arrangement requires it.",
                        '### Read-aloud script', listening['script'],
                        'Gist — suggested answer: ' + listening['gist'],
                        '### Detail key — one point each; accept accurate paraphrases.'])
        for number, question in enumerate(listening['questions'], 1):
            teacher.extend([f"{number}. {question['prompt']}",
                            'Answer: ' + question['answer'],
                            'Evidence: “' + question['evidence'] + '”'])
        teacher.append('Transfer: use the matching Your turn activity in the Student Practice Pack. Assess the new exchange, not whether a learner reproduces the script’s wording or opinion.')
    teacher.extend(['## 15. Pilot observation and revision record',
                    'A plan is supplied; a live pilot and its findings are not. Complete this record after teaching rather than claiming improvement in advance.',
                    'Class/date: __________  Unit/lesson: __________  Number of learners: ___',
                    'Selected input: verified original recording / new teacher-read alternative / other: __________',
                    'Actual timings and unfinished work: ________________________________',
                    'Observed learner strength, with an example: ________________________',
                    'Observed difficulty, with an example: ______________________________',
                    'Learners needing different support (private codes only): ______________',
                    'Did all learners get speaking turns? How did I check? _________________',
                    'Did anyone need a neutral topic or access adaptation? _________________',
                    'What the students’ feedback suggests: ______________________________',
                    'One revision to try, and when: _____________________________________',
                    'If comparing attempts, record the prompt, preparation time, speaking time, support, and evidence. Improvement on a repeated task does not by itself prove general proficiency growth or a causal effect of this book.',
                    'Remaining development: source verification and keys for the original listening lessons; reading keys for Units 2–8; independent human review; and actual classroom trial evidence. The new alternatives and Unit 1 key are not a claim that those tasks are complete.'])
    student_path, teacher_path = SOURCE / 'student-practice.md', SOURCE / 'teacher-implementation.md'
    student_path.write_text('\n\n'.join(student) + '\n')
    teacher_path.write_text('\n\n'.join(teacher) + '\n')
    register = ROOT / 'book/publishing/listening-alternatives.csv'
    register.parent.mkdir(parents=True, exist_ok=True)
    with register.open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['unit', 'alternative_id', 'title', 'script_source', 'detail_questions',
                         'delivery', 'recorded_audio_supplied', 'original_video_status', 'live_pilot_conducted'])
        for module in modules:
            writer.writerow([module['unit'], f"U{module['unit']}-ALT", module['listening']['title'],
                             f"book/classroom/modules.json — unit {module['unit']}, listening.script",
                             5, 'TEACHER_READ', 'NO', 'UNVERIFIED', 'NO'])
    return student_path, teacher_path


def main():
    student, teacher = compose()
    for source, stem, label in [(student, STUDENT_STEM, 'Student Practice'),
                                (teacher, TEACHER_STEM, 'Teacher Implementation')]:
        build(source=source, pdf_path=ROOT / (stem + '.pdf'), docx_path=ROOT / (stem + '.docx'),
              title_text='Master Speaking — ' + label + ' Pack',
              footer_label='Master Speaking | ' + label + ' | New supplementary material',
              compact=(stem == STUDENT_STEM))


if __name__ == '__main__':
    main()

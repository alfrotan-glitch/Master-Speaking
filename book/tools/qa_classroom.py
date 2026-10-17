#!/usr/bin/env python3
"""Validate authored classroom content, source-linked Unit 1 key, and exports.

These checks establish internal consistency, not pedagogical validity or a
claim that a live teacher/student pilot has occurred.
"""
import json
from pathlib import Path
import re
import pymupdf
from docx import Document
from companion import blocks, ROOT
from classroom import SOURCE, STUDENT_STEM, TEACHER_STEM


def norm(text):
    return re.sub(r'\s+', '', text).replace('•', '')


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for value in obj.values():
            yield from strings(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from strings(value)


def export_check(source, stem):
    expected = list(blocks(source.read_text()))
    word = norm('\n'.join(p.text for p in Document(ROOT / (stem + '.docx')).paragraphs))
    pages = []
    with pymupdf.open(ROOT / (stem + '.pdf')) as pdf:
        for page in pdf:
            pages.append('\n'.join(line for line in page.get_text().splitlines()
                                   if not line.startswith('Master Speaking |') and line.strip() != str(page.number + 1)))
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    for span in line['spans']:
                        x0, y0, x1, y1 = span['bbox']
                        assert x0 >= 35 and x1 <= page.rect.width - 35, (stem, page.number, span)
                        assert y0 >= 15 and y1 <= page.rect.height - 15, (stem, page.number, span)
        count = len(pdf)
        outline = [title for _, title, _ in pdf.get_toc()]
        for kind, title in expected:
            if kind == 'heading':
                assert title in outline, f'Missing PDF bookmark: {title}'
    text = norm('\n'.join(pages))
    for kind, paragraph in expected:
        assert norm(paragraph) in word, f'Word missing: {paragraph[:60]}'
        assert norm(paragraph) in text, f'PDF missing: {paragraph[:60]}'
        if kind == 'heading' and re.match(r'^\d+\.', paragraph):
            assert any(norm(page).startswith(norm(paragraph)) for page in pages), paragraph
    return {'pages': count, 'source_blocks': len(expected), 'ok': True}


def main():
    modules = json.loads((SOURCE / 'modules.json').read_text())
    key = json.loads((SOURCE / 'unit1-reading-key.json').read_text())
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    assert [m['unit'] for m in modules] == list(range(1, 9))
    student = (SOURCE / 'student-practice.md').read_text()
    scripts = []
    for module, unit in zip(modules, book['units']):
        assert module['title'] == unit['title']
        assert len(module['goals']) == 4 and all(len(goals) == 2 for goals in module['goals'])
        assert all(goal.startswith('I can ') for goals in module['goals'] for goal in goals)
        assert len(module['dialogue']) == 6 and len(module['frames']) == 3
        script = module['listening']['script']
        assert 100 <= len(script.split()) <= 180
        assert script not in scripts and norm(script) not in norm(student), 'Teacher script exposed in student pack'
        scripts.append(script)
        questions = module['listening']['questions']
        assert len(questions) == 5 and len(set(q['prompt'] for q in questions)) == 5
        for question in questions:
            assert question['answer'].strip() and norm(question['evidence']) in norm(script), question
    assert 'Answer / acceptable content:' not in student and 'Text evidence:' not in student
    chapter = book['units'][0]['chapters'][0]['blocks']
    passage = norm(' '.join(strings(chapter)))
    assert len(key) == 15
    vocabulary_start = next(i for i, b in enumerate(chapter) if b.get('text') == 'Vocabulary Check')
    vocabulary_end = next(i for i, b in enumerate(chapter) if b.get('text') == 'Before You Read')
    source_fills = [b['text'] for b in chapter[vocabulary_start:vocabulary_end] if b['k'] == 'fill']
    assert [k['stem'] for k in key if k['section'] == 'Vocabulary Check'] == source_fills
    reading_start = next(i for i, b in enumerate(chapter) if b.get('text') == 'Reading Comprehension')
    reading_end = next(i for i, b in enumerate(chapter) if b.get('text') == 'Answer the Questions')
    stems = [chapter[i]['text'] for i in range(reading_start, reading_end)
             if chapter[i]['k'] in ('p', 'q') and chapter[i+1]['k'] == 'opt']
    assert [k['stem'] for k in key if 'Choose the Best Answer' in k['section']] == stems
    table = next(b for b in chapter if b.get('role') == 'questions')
    assert [k['stem'] for k in key if k['section'].startswith('Answer the Questions')] == [r[0] for r in table['rows']]
    for item in key:
        assert norm(item['stem']) in passage, f"Unknown key question: {item['stem']}"
        assert norm(item['evidence']) in passage, f"Unsupported evidence: {item['evidence']}"
        if 'Choose the Best Answer' in item['section']:
            index = next(i for i, block in enumerate(chapter) if block.get('text') == item['stem'])
            letter = item['answer'][0]
            option = next(block['text'] for block in chapter[index + 1:index + 5]
                          if block['k'] == 'opt' and block['text'].startswith(letter + '.'))
            loose = lambda value: re.sub(r'[^a-z0-9]', '', value.lower())
            assert loose(option[2:]) == loose(item['answer'].split('—', 1)[1]), item
    # Pilot lesson timings are contiguous and genuinely total 75 minutes.
    notes = (SOURCE / 'teacher-notes.md').read_text()
    for number in range(2, 6):
        section = notes.split(f'## {number}. ', 1)[1].split('\n## ', 1)[0]
        intervals = [(int(a), int(b)) for a, b in re.findall(r'^- (\d+)–(\d+):', section, re.M)]
        assert intervals[0][0] == 0 and intervals[-1][1] == 75
        assert all(a < b for a, b in intervals)
        assert all(intervals[i][1] == intervals[i+1][0] for i in range(len(intervals)-1))
    exports = {}
    for path, stem in [(SOURCE / 'student-practice.md', STUDENT_STEM),
                        (SOURCE / 'teacher-implementation.md', TEACHER_STEM)]:
        exports[stem] = export_check(path, stem)
    report = {'ok': True, 'units': 8, 'chapter_checklists': 32, 'can_do_statements': 64,
              'speaking_dialogues': 8, 'short_responses': 8, 'new_listening_scripts': 8,
              'new_listening_detail_questions': 40, 'unit1_reading_key_items': 15,
              'pilot_lessons_minutes': [75, 75, 75, 75], 'exports': exports,
              'original_video_inputs_verified': False, 'live_pilot_conducted': False}
    (ROOT / 'book/artifacts/qa_classroom.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

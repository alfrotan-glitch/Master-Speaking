"""Apply the author-approved self-contained edition after the historical edits.

Old source materials remain in the repository for audit, never in this edition.
Every replaced chapter is guarded by its pre-replacement content fingerprint.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import re
ROOT=Path(__file__).resolve().parents[2]


def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def text_values(block):
    if block.get('text'):
        yield block['text']
    for row in block.get('rows',[]):
        yield from (cell for cell in row if cell)


def listening_blocks(chapter, module):
    old=chapter['blocks']; n=module['unit']; story=module['listening']
    vocab=deepcopy(next(x for x in old if x['k']=='table' and x['role']=='vocab'))
    start=next(i for i,x in enumerate(old) if x.get('text')=='Group Discussion' and x['k']=='sec')
    finish=next((i for i in range(start,len(old)) if old[i].get('text')=='Homework' and old[i]['k']=='sec'),len(old))
    discussion=deepcopy(old[start:finish])
    # Retained extension questions explore the unit topic, not unsupported
    # assertions from an absent video. The source-complete AI scenario stays.
    for block in discussion:
        if block.get('k')=='instr' and re.search(r'video|talk|speaker',block.get('text',''),re.I):
            block['text']='Discuss the questions using reasons and examples. Distinguish details in the story from your own views about the wider topic.'
    b=lambda kind,text,**kw:dict(k=kind,text=text,**kw)
    result=[b('mediatitle',chapter['title']),b('sec','Before Listening'),
        b('instr','Work with a teacher or partner. Keep the script at the end of this chapter covered until after the second listening.'),
        b('sub',story['title']),b('q','From the story title, what situation do you expect?'),
        b('q','What information would you listen for to understand the problem and the response?'),
        b('sec','Topic Language'),
        b('instr','Use this language when discussing the story and the wider topic. You are not expected to hear every expression in the story.'),vocab,
        b('sec','Listening Strategy'),b('sub','First Listening',img=f'edition-unit-{n}-listening.png'),
        b('instr','Listen to the whole story without reading the script. What is the main problem or decision? Give a one-sentence answer.'),
        b('sub','Second Listening'),b('instr','Read the detail questions, listen again, and take short notes in a notebook under the two headings below. Ask to hear a part again if you need it.'),
        {'k':'table','role':'notes','rows':[['Main Point','Details I Heard'],['','']]},
        b('sec','Listening Comprehension'),b('instr','Answer in short phrases. Use details you heard, not guesses about what usually happens.')]
    result.extend(b('q',question['prompt']) for question in story['questions'])
    result.extend([b('sub','Compare and Clarify'),b('instr','Compare answers with a partner. Explain which detail supports an answer. Check the script only after the listening task, then correct any misunderstanding.')])
    result.extend(discussion[:1])
    result.append(b('instr','Use the story as a starting point for the wider questions below. Distinguish what the narrator describes from your own opinions and predictions.'))
    result.extend(discussion[1:])
    result.extend([b('sec','Try It Again'),b('instr','Retell the main problem and response in your own words. Ask a partner one follow-up question, then make your retelling clearer.'),
        b('sec','Listening Script'),b('sub',story['title']),
        b('label','Fictional story • read aloud by a teacher or partner'),b('p',story['script']),
        b('instr','For independent reading practice, read the story once, cover it, and answer from memory. This is reading recall; it does not replace listening to another person.')])
    return result


def apply(book,log):
    plan=json.loads((ROOT/'book/master/self-contained-edition.json').read_text())
    modules=json.loads((ROOT/'book/classroom/modules.json').read_text())
    if book['front']['epigraph'] != plan['expected_old_epigraph']:
        raise ValueError('Epigraph source changed; review the replacement')
    log('Self-contained edition · opening reflection',book['front']['epigraph'],plan['epigraph'],
        'Author approved replacing the externally attributed quotation with newly authored learner-facing text.','new authored text; not external clearance')
    book['front']['epigraph']=plan['epigraph']
    guide=book['front']['howto']['chapters'][1]
    log('Self-contained edition · listening guidance',guide['desc'],plan['new_chapter2_description'],
        'Replace the unsupplied video dependency with included original read-aloud stories.')
    for value in guide['you_will']:
        log('Self-contained edition · listening outcomes',value,'See current listening outcomes','Align outcomes to original listening stories and independent reading fallback.')
    guide['desc']=plan['new_chapter2_description'];guide['you_will']=plan['new_chapter2_goals']
    for unit,row,module in zip(book['units'],plan['units'],modules):
        n=unit['number'];chapter=unit['chapters'][1]
        if digest(chapter['blocks']) != row['expected_old_chapter_sha256']:
            raise ValueError(f'U{n}: guarded original-listening replacement source changed')
        old=deepcopy(chapter['blocks']);chapter['blocks']=listening_blocks(chapter,module)
        chapter['listening_source']=row['script_id']
        for block in old:
            for value in text_values(block):
                log(f'U{n} Ch2 · self-contained listening replacement',value,
                    f'Authored listening lesson {row["script_id"]}; retained topic language/discussion where applicable',
                    'Author-approved replacement of a source-dependent lesson; original words retained in source audit, not silently omitted.',
                    'guarded authored replacement')
        unit['image']=f'edition-unit-{n}-opener.png'
        for c in unit['chapters']:
            if c['number']==2:continue
            for block in c['blocks']:
                if block.get('img'):
                    log(f'U{n} Ch{c["number"]} · original course graphic',block['img'],f'edition-unit-{n}-reading.png','Replace unverified manuscript imagery with original code-drawn course diagrams.')
                    block['img']=f'edition-unit-{n}-reading.png'
    for edit in plan['text_replacements']:
        blocks=book['units'][edit['unit']-1]['chapters'][edit['chapter']-1]['blocks']
        matches=[b for b in blocks if b.get('text')==edit['original']]
        if len(matches)!=1:
            raise ValueError(f'Self-contained text replacement drift: {edit["original"]}')
        matches[0]['text']=edit['correction']
        if edit.get('kind'):matches[0]['k']=edit['kind']
        log(f'U{edit["unit"]} Ch{edit["chapter"]} · self-contained wording',edit['original'],edit['correction'],
            'Align the current lesson to supplied stories and replace unsupported external quotation framing with original discussion prompts.')
    book['edition']={'id':plan['edition_id'],'self_contained_listening':True,'original_interior_graphics':24,'recorded_audio_supplied':False}

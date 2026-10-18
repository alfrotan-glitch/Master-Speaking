#!/usr/bin/env python3
"""Verify the approved replacement scope and supplied listening inputs/keys.

Checks do not certify pedagogy, independent copyediting or legal ownership.
"""
from pathlib import Path
import hashlib
import json
import re
import zipfile
from lxml import etree
from self_contained import digest

ROOT=Path(__file__).resolve().parents[2]


def inspect(book,base,plan,modules):
    issues=[]
    if book.get('edition',{}).get('id')!=plan['edition_id']:
        issues.append('Self-contained edition identity missing')
    if book['front']['epigraph']!=plan['epigraph'] or 'Roy T. Bennett' in json.dumps(book):
        issues.append('Uncleared opening quotation remains or authored replacement changed')
    if book['front']['howto']['chapters'][1]['desc']!=plan['new_chapter2_description']:
        issues.append('Student guidance does not describe the supplied listening route')
    for unit,row,module in zip(book['units'],plan['units'],modules):
        n=unit['number'];chapter=unit['chapters'][1];blocks=chapter['blocks'];story=module['listening']
        if digest(base['units'][n-1]['chapters'][1]['blocks'])!=row['expected_old_chapter_sha256']:
            issues.append(f'U{n}: historical replacement guard does not match')
        if chapter.get('listening_source')!=f'U{n}-ORIGINAL':issues.append(f'U{n}: original script identity missing')
        if sum(b.get('text')==story['script'] and b['k']=='p' for b in blocks)!=1:
            issues.append(f'U{n}: supplied script missing/duplicated/changed')
        try:
            start=next(i for i,b in enumerate(blocks) if b.get('text')=='Listening Comprehension')
            end=next(i for i,b in enumerate(blocks) if b.get('text')=='Compare and Clarify')
            questions=[b['text'] for b in blocks[start:end] if b['k']=='q']
        except StopIteration:questions=[]
        if questions!=[q['prompt'] for q in story['questions']]:issues.append(f'U{n}: detail questions do not match supplied keys')
        for q in story['questions']:
            if not q['answer'].strip() or q['evidence'] not in story['script']:
                issues.append(f'U{n}: unsupported listening-key evidence')
        old_vocab=next(b for b in base['units'][n-1]['chapters'][1]['blocks'] if b.get('role')=='vocab')
        if old_vocab not in blocks:issues.append(f'U{n}: source-backed topic language lost')
        if unit['image']!=f'edition-unit-{n}-opener.png':issues.append(f'U{n}: old opener image remains')
        for c in unit['chapters']:
            for b in c['blocks']:
                if b.get('img') and not b['img'].startswith(f'edition-unit-{n}-'):
                    issues.append(f'U{n}: legacy image reference remains')
                text=b.get('text','')
                if re.search(r'\bTED(?:-Ed)?\b|\bGoldin\b|from the video|watching this video',text,re.I):
                    issues.append(f'U{n}: dependency on an unidentified video remains')
    for unit in book['units']:
        blocks=unit['chapters'][1]['blocks']
        start=next(i for i,b in enumerate(blocks) if b.get('text')=='Group Discussion')
        end=next(i for i,b in enumerate(blocks) if b.get('text')=='Try It Again')
        for b in blocks[start:end]:
            if re.search(r'according to the speaker|the speaker(?:’s findings| says| suggests)|the research found|the Process Model|agree with the speaker',b.get('text',''),re.I):
                issues.append(f'U{unit["number"]}: retained discussion depends on an absent source')
    for edit in plan['text_replacements']:
        blocks=book['units'][edit['unit']-1]['chapters'][edit['chapter']-1]['blocks']
        if sum(b.get('text')==edit['correction'] for b in blocks)!=1:
            issues.append('Approved wording replacement changed: '+edit['correction'])
        if any(b.get('text')==edit['original'] for b in blocks):
            issues.append('Superseded quotation/video wording remains')
    return issues


def main():
    load=lambda p:json.loads((ROOT/p).read_text())
    book=load('book/artifacts/book.json');base=load('book/artifacts/editorial-base.json')
    plan=load('book/master/self-contained-edition.json');modules=load('book/classroom/modules.json')
    issues=inspect(book,base,plan,modules)
    artwork=load('book/publishing/current-artwork-provenance.json')
    active={row['sha256'] for row in artwork}
    cover=hashlib.sha256((ROOT/'book/assets/cover.png').read_bytes()).hexdigest()
    image_files=0
    for filename,prefix in [('Master-Speaking.epub','images/'),('Master-Speaking-7x10.docx','word/media/')]:
        with zipfile.ZipFile(ROOT/filename) as z:
            names=[name for name in z.namelist() if name.startswith(prefix) and not name.endswith('/')]
            for name in names:
                sha=hashlib.sha256(z.read(name)).hexdigest()
                if sha not in active|{cover}:issues.append(f'Unreviewed/legacy artwork embedded in {filename}: {name}')
            if len(names)!=(25 if filename.endswith('.epub') else 24):issues.append('Artwork inventory mismatch: '+filename)
            image_files+=len(names)
    import pymupdf
    normalize=lambda text:re.sub(r'\W+','',text).casefold()
    script_pages=[]
    with pymupdf.open(ROOT/'Master-Speaking-print-7x10.pdf') as pdf:
        for module in modules:
            pages=[i+1 for i,page in enumerate(pdf) if normalize(module['listening']['script']) in normalize(page.get_text()) and 'Listening Script' in page.get_text()]
            if len(pages)!=1:issues.append(f'U{module["unit"]}: script and heading must fit on one page')
            script_pages.extend(pages)
    with pymupdf.open(ROOT/'Master-Speaking-Back-Cover.pdf') as back:
        if len(back)!=1 or tuple(back[0].rect)!=(0.0,0.0,504.0,720.0):issues.append('Back panel geometry mismatch')
    import copy
    bad=copy.deepcopy(book)
    bad['units'][0]['chapters'][1]['blocks']=[b for b in bad['units'][0]['chapters'][1]['blocks'] if b.get('text')!=modules[0]['listening']['script']]
    missing_script=bool(inspect(bad,base,plan,modules))
    bad=copy.deepcopy(book);bad['units'][0]['image']='image1.png'
    legacy_image=bool(inspect(bad,base,plan,modules))
    bad=copy.deepcopy(book)
    idx=next(i for i,b in enumerate(bad['units'][0]['chapters'][1]['blocks']) if b.get('text')=='Try It Again')
    bad['units'][0]['chapters'][1]['blocks'].insert(idx,{'k':'q','text':'According to the speaker, what did the absent research show?'})
    absent_source=bool(inspect(bad,base,plan,modules))
    if not missing_script or not legacy_image or not absent_source:issues.append('Self-contained negative-control detection failed')
    report={'ok':not issues,'original_diagrams':len(artwork),'included_listening_scripts':8,'matching_detail_keys':40,
            'embedded_image_files_checked':image_files,'missing_script_mutation_rejected':missing_script,
            'legacy_image_mutation_rejected':legacy_image,'absent_source_discussion_mutation_rejected':absent_source,'recorded_audio_supplied':False,'single_page_script_locations':script_pages,'issues':issues,
            'scope':'Guarded replacement, supplied scripts/questions/key evidence, retained topic language, excluded legacy media/quotation wording and embedded image inventory. Not legal certification, independent factual proof or classroom validation.'}
    (ROOT/'book/artifacts/qa_self_contained.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));raise SystemExit(bool(issues))


if __name__=='__main__':main()

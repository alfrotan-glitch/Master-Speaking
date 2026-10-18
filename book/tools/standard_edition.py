#!/usr/bin/env python3
"""Build the original-manuscript course edition in an isolated workspace.

Never calls parse.build(): its later stages replace original course material.
The accepted self-contained edition and its release evidence are not modified.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, shutil, subprocess, sys
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'book/standard'
WORK = DEST / 'work'

def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def run(name):
    subprocess.run([sys.executable, str(WORK/'book/tools'/name)], check=True)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def setup():
    for directory in ['tools','assets','master']:
        shutil.copytree(ROOT/'book'/directory, WORK/'book'/directory, dirs_exist_ok=True)
    for directory in ['artifacts','publishing','qa']:
        (WORK/'book'/directory).mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT/'Master Speaking.docx',WORK/'Master Speaking.docx')
    run('extract.py')
    # These layout overrides are tied to the OTHER edition's added scripts.
    shutil.copy2(DEST/'layout-overrides.json',WORK/'book/master/layout-overrides.json')

def construct():
    sys.path.insert(0,str(WORK/'book/tools'))
    spec=importlib.util.spec_from_file_location('original_parser',WORK/'book/tools/parse.py')
    p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
    # Guarded, minimal copyedits only; no replacement passages/scripts.
    edits=json.loads((DEST/'copyedits.json').read_text())
    p.TEXT_FIXES={}
    for edit in edits:
        assert p.items_by_idx[edit['source_block']]['text']==edit['original'],edit
        p.TEXT_FIXES[edit['source_block']]=edit['correction']
    p.REMOVE_ITEMS={}
    p.DROP_HEADINGS=set()
    front=p.parse_front(); units=p.parse_units()
    units[4]['title']='Living with AI (Artificial Intelligence)'
    p.resmarten.fixed=[];p.resmarten(front);p.resmarten(units)
    structural=json.loads((DEST/'structural-edits.json').read_text())
    for edit in structural:
        blocks=units[edit['unit']-1]['chapters'][edit['chapter']-1]['blocks']
        matches=[b for b in blocks if b.get('text')==edit['text'] and b['k']==edit['from']]
        assert len(matches)==1,edit
        matches[0]['k']=edit['to']
        p.log(f"U{edit['unit']} Ch{edit['chapter']} heading role",edit['text'],edit['text'],
              'Formatting only: existing topic/clinic label restored as a heading, not a numbered question.')
    for entry in p.CHANGES:
        if entry['area']=='U6 Ch2 Before Listening':
            entry['confidence']='Internal title consistency only; recording not verified'
            entry['reason']='Repeated title aligned with the original Unit 6 lesson title; not an identification of the external recording.'
    plan=json.loads((ROOT/'book/master/chapter-titles.json').read_text())
    for unit,titles in zip(units,plan):
        for chapter,title,source in zip(unit['chapters'],titles['titles'],titles['sources']):
            chapter['focus']=chapter['title'];chapter['title']=title;chapter['title_source']=source
    book={'meta':{'title':'Master Speaking','author':'Abdul Raziq Nazari','year':'2026',
                  'foreword_date':'September, 2026','source':'Master Speaking.docx'},
          'front':front,'units':units}
    save(WORK/'book/artifacts/book.json',book)
    save(DEST/'book.json',book)
    save(DEST/'copyedit-log.json',p.CHANGES)
    return p,book

def canonical(text):
    return ''.join(c.casefold() for c in text if c.isalnum())

def strings(obj):
    if isinstance(obj,str):yield obj
    elif isinstance(obj,list):
        for x in obj:yield from strings(x)
    elif isinstance(obj,dict):
        for k,v in obj.items():
            if k not in ('img','image','title_source','source','k','role','fill'):yield from strings(v)

def audit(p,book):
    text=canonical(' '.join(strings(book)))
    missing=[];ledger=[]
    for item in p.items:
        values=[item['text']] if item['type']=='para' else [c['text'] for r in item['rows'] for c in r]
        for n,value in enumerate(values):
            key=canonical(value)
            if not key:continue
            # Layout-generated numbering is not carried into list item text.
            without_number=canonical(re.sub(r'^\s*(?:\(?\d+[.)]|[a-dA-D][.)])\s*','',value))
            scoped=text
            unit=p.unit_of(item['i'])
            chapter=p.chap_of(item['i'])
            if unit:
                target=book['units'][unit-1]
                boundaries=[i for i in p.CHAPTER_MARKS if p.unit_of(i)==unit]
                if chapter and item['i']>=min(boundaries):
                    target=target['chapters'][chapter[0]-1]
                scoped=canonical(' '.join(strings(target)))
            retained=key in scoped or (without_number and without_number in scoped)
            row={'source_block':item['i'],'cell':n if item['type']=='table' else None,
                 'original':value,'retained_normalized':bool(retained)}
            ledger.append(row)
            if not retained:missing.append(row)
    unresolved=[]
    for row in ledger:
        i=row['source_block'];original=row['original']
        if row['retained_normalized']:
            row['disposition']='Retained in its original unit/chapter (normalization and list-label handling only).'
            continue
        if i<=9:
            reason='Original contents replaced with generated contents and current page references.'
        elif i==67 or original.startswith('CHAPTER '):
            reason='Front-matter heading supplied by the renderer; chapter strand expanded consistently with source chapter headings.'
        elif i in p.CHAPTER_MARKS:
            reason='Original learning strand retained as chapter subtitle; exact existing principal lesson title promoted to chapter heading.'
        elif i in p.UNIT_OPENERS:
            reason='Duplicated unit opener collapsed to one unit number and one title.'
        elif original.startswith('Before You ReadDiscuss.'):
            u=p.unit_of(i);target=canonical(' '.join(strings(book['units'][u-1]['chapters'][0])))
            assert all(canonical(q) in canonical(original) and canonical(q) in target for q in p.BYR_QUESTIONS[u])
            if u in p.BYR_STRAY_FILLIN:assert canonical(p.BYR_STRAY_FILLIN[u]) in target
            reason='Repeated Before You Read text collapsed; each distinct original question retained. Merged vocabulary item retained where present.'
        elif 'Chooses 10 expressions' in original:
            assert canonical(original.replace('Chooses 10','Choose 10')) in canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][2])))
            reason='Imperative grammar: Chooses 10 corrected to Choose 10; exercise unchanged.'
        elif original.startswith('Activity '):
            tail=re.sub(r'^Activity \d+:\s*','',original)
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert canonical(tail) in target
            reason='Activity heading and instruction separated; duplicated activity numbers regularized; wording retained.'
        elif i in p.TEXT_FIXES:
            edit=next(e for e in json.loads((DEST/'copyedits.json').read_text()) if e['source_block']==i)
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert canonical(edit['correction']) in target
            reason=edit['reason']
        elif i==1925:
            reason='Repeated Unit 4 video title corrected to match the Unit 6 original lesson heading. Internal consistency repair only; recording identity remains unverified.'
        else:
            unresolved.append(row);continue
        row['disposition']=reason
    if unresolved:
        save(DEST/'unresolved-source-differences.json',unresolved)
        raise ValueError(f'{len(unresolved)} unexplained source differences')
    save(DEST/'source-ledger.json',ledger)
    save(DEST/'source-differences.json',[row for row in ledger if not row['retained_normalized']])
    reading_evidence=[]
    for unit in book['units']:
        previous=-1;indices=[]
        for block in unit['chapters'][0]['blocks']:
            if block['k']!='reading':continue
            candidates=[x for x in p.items if x['type']=='para' and p.unit_of(x['i'])==unit['number']
                        and p.chap_of(x['i']) and p.chap_of(x['i'])[0]==1 and canonical(x['text'])==canonical(block['text'])]
            assert len(candidates)==1,(unit['number'],block['text'][:70])
            source=candidates[0];assert source['i']>previous;previous=source['i'];indices.append(previous)
        assert indices
        reading_evidence.append({'unit':unit['number'],'original_paragraphs_in_order':indices,
                                 'paragraphs':len(indices),'replacement_reading':False})
    model_images=[u['image'] for u in book['units']]+[b['img'] for u in book['units'] for c in u['chapters'] for b in c['blocks'] if b.get('img')]
    assert len(model_images)==24 and set(model_images)==set(p.image_map.values())
    assert not any(b.get('role')=='listening-script' for u in book['units'] for c in u['chapters'] for b in c['blocks'])
    save(DEST/'source-audit-summary.json',{'source_sha256':digest(ROOT/'Master Speaking.docx'),
         'method':'Normalized presence checked within original unit/chapter, with explicit dispositions for structural/copyedit differences. Reading paragraphs additionally checked in original order. This is not a character-for-character facsimile or independent editorial review.',
         'nonempty_source_paragraphs_and_cells':len(ledger),
         'differences_with_explicit_dispositions':sum(not x['retained_normalized'] for x in ledger),
         'unexplained_differences':0,'original_illustrations':24,'reading_passages':reading_evidence})
    print('Source passages/cells:',len(ledger),'requiring reconciliation:',len(missing))


def artwork():
    """Keep every source illustration; never substitute a content-bearing image."""
    from zipfile import ZipFile
    from PIL import Image
    descriptions=json.loads((DEST/'image-descriptions.json').read_text())
    records=[];provenance=[]
    with ZipFile(ROOT/'Master Speaking.docx') as archive:
        mapping=json.loads((WORK/'book/artifacts/image_map.json').read_text())
        assert len(set(mapping.values()))==24
        for filename in sorted(set(mapping.values())):
            path=WORK/'book/assets/images'/filename
            path.write_bytes(archive.read('word/media/'+filename))
            entry={'file':filename,'path':str(path.relative_to(WORK)),
                   'sha256':digest(path),'alt':descriptions[filename]}
            if filename.endswith('.gif'):
                twin=path.with_suffix('.png')
                with Image.open(path) as image:image.convert('RGB').save(twin)
                entry['aliases']={twin.name:digest(twin)}
            records.append(entry)
            with Image.open(path) as image:dimensions=list(image.size)
            provenance.append({'file':filename,'sha256':digest(path),'pixels':dimensions,
                               'origin':'Exact embedded image from the original manuscript',
                               'permission_status':'Unverified; supplied artwork is not a permission grant'})
    records.append({'file':'cover.png','path':'book/assets/cover.png',
                    'sha256':digest(WORK/'book/assets/cover.png'),
                    'alt':'Master Speaking by Abdul Raziq Nazari. Original-manuscript course edition. The TOEFL House. Green cover with intersecting conversation paths.'})
    save(WORK/'book/master/image-descriptions.json',{'images':records})
    save(DEST/'artwork-provenance.json',provenance)


def production():
    # Adapt ONLY the staging copy of the approved cover generator.
    path=WORK/'book/tools/cover.py'
    source=path.read_text().replace('An English speaking course in eight thematic units',
                                   'Original-manuscript course edition')
    source=source.replace('to an original story, recover details and clarify meaning.',
                          'to the course videos, recover details and clarify meaning.')
    source=source.replace('Fictional listening scripts are included for a teacher or partner to read aloud. No external video or subscription is required.',
                          'The original video-based listening lessons are retained. The course instructor must arrange the required video resources before teaching these lessons.')
    path.write_text(source)
    epub_path=WORK/'book/tools/epub.py'
    epub_source=epub_path.read_text().replace(
        'Master Speaking / Abdul Raziq Nazari / 2026',
        'Master Speaking / Abdul Raziq Nazari / 2026 / Original-manuscript course edition')
    epub_source=epub_source.replace(
        'Listening exercises use included fictional scripts read aloud by a teacher or partner; no recorded audio is supplied.',
        'Listening exercises require the original external course videos, which are not embedded. No verified transcripts or recorded audio are supplied. The low-resolution goal-setting mind map does not have a complete text transcription.')
    epub_path.write_text(epub_source)
    run('cover.py');artwork()
    for tool in ['master.py','wordmaster.py','docxpdf.py','epub.py']:run(tool)
    import pymupdf
    with pymupdf.open(WORK/'Master-Speaking-print-7x10.pdf') as interior:
        with pymupdf.open(WORK/'Master-Speaking-Front-Cover.pdf') as reader:
            reader.insert_pdf(interior)
            reader.set_toc([[1,'Cover',1]]+[[level,title,page+1] for level,title,page in interior.get_toc()])
            reader.set_page_labels([{'startpage':0,'prefix':'Cover','style':''}]+
                                  [dict(rule,startpage=rule['startpage']+1) for rule in interior.get_page_labels()])
            reader.set_metadata({'title':'Master Speaking — Original-Manuscript Course Edition',
                                 'author':'Abdul Raziq Nazari','subject':'Original course text and video-based lessons'})
            reader.save(WORK/'Master-Speaking.pdf',garbage=4,deflate=True)
    results={}
    for tool in ['qa_word','qa_fidelity','qa_print','qa_proof','qa_epub','qa_epubcheck','qa_chapters','qa_visual']:
        result=subprocess.run([sys.executable,str(WORK/'book/tools'/f'{tool}.py')],capture_output=True,text=True)
        results[tool]={'exit_code':result.returncode,'output':result.stdout+result.stderr}
        print(tool,result.returncode,result.stdout[-350:],flush=True)
        artifact=WORK/'book/artifacts'/f'{tool}.json'
        if artifact.exists():shutil.copy2(artifact,DEST/artifact.name)
    shutil.copy2(WORK/'book/artifacts/epubcheck-official.json',DEST/'epubcheck-official.json')
    save(DEST/'production-checks.json',results)
    names={'Master-Speaking.pdf':'Master-Speaking-Standard.pdf',
           'Master-Speaking-print-7x10.pdf':'Master-Speaking-Standard-print-7x10.pdf',
           'Master-Speaking-7x10.docx':'Master-Speaking-Standard-7x10.docx',
           'Master-Speaking.epub':'Master-Speaking-Standard.epub',
           'Master-Speaking-Front-Cover.pdf':'Master-Speaking-Standard-Front-Cover.pdf',
           'Master-Speaking-Back-Cover.pdf':'Master-Speaking-Standard-Back-Cover.pdf'}
    for original,destination in names.items():shutil.copy2(WORK/original,ROOT/destination)
    shutil.copy2(WORK/'book/master/master.xhtml',DEST/'master.xhtml')
    save(DEST/'build-manifest.json',{'semantic_sha256':digest(DEST/'book.json'),'master_sha256':digest(DEST/'master.xhtml'),'source':'Master Speaking.docx','source_sha256':digest(ROOT/'Master Speaking.docx'),
         'outputs':{destination:digest(ROOT/destination) for destination in names.values()},
         'scope':'Original manuscript; original videos, readings, exercises and illustrations. Separate from the accepted self-contained edition.',
         'checks_passed':sum(r['exit_code']==0 for r in results.values()),'checks_run':len(results)})
    if any(r['exit_code'] for r in results.values()):
        raise SystemExit('Production checks need review; see book/standard/production-checks.json. No blanket release approval.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source-only',action='store_true');args=parser.parse_args()
    protected=[ROOT/n for n in ['Master Speaking.docx','Master-Speaking.pdf','Master-Speaking-print-7x10.pdf',
                               'Master-Speaking-7x10.docx','Master-Speaking.epub','book/artifacts/book.json','book/master/master.xhtml']]
    before={str(p):digest(p) for p in protected}
    try:
        setup();p,book=construct();audit(p,book)
        if not args.source_only:production()
    finally:
        after={str(p):digest(p) for p in protected}
        assert before==after,'Protected edition or source changed'
        save(DEST/'protected-inputs.json',{'unchanged':True,'sha256':{str(Path(p).relative_to(ROOT)):h for p,h in after.items()}})

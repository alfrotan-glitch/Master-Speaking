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
    # Exact-match, source-indexed corrections; table-cell edits and removals
    # are separately guarded so the original DOCX and other edition stay intact.
    edits=json.loads((DEST/'copyedits.json').read_text())
    p.TEXT_FIXES={}
    p.REMOVE_ITEMS={}
    table_edits=[]
    for edit in edits:
        item=p.items_by_idx[edit['source_block']]
        if 'cell' in edit:
            assert item['type']=='table',edit
            cells=[cell for row in item['rows'] for cell in row]
            assert cells[edit['cell']]['text']==edit['original'],edit
            table_edits.append(edit)
            continue
        assert item['type']=='para' and item['text']==edit['original'],edit
        if edit.get('action')=='remove':
            p.REMOVE_ITEMS[edit['source_block']]=(f"Standard follow-up source block {edit['source_block']}",
                                                  edit['original'],edit['reason'])
        else:
            p.TEXT_FIXES[edit['source_block']]=edit['correction']
    p.DROP_HEADINGS=set()
    # Override this hand-split before parsing so the guarded correction is
    # not overwritten by the shared parser's stale join-mark examples.
    p.JAM_FIXES[1676]=['turn it off','pick it up','work in','depend on']
    front=p.parse_front(); units=p.parse_units()
    # Front matter is parsed separately from the chapter body; apply its
    # guarded edits explicitly rather than mutating the source dump.
    def replace_front(block, path, original, correction, reason):
        parent=front
        for key in path[:-1]:parent=parent[key]
        key=path[-1]
        current=parent[key]
        expected=p.clean(original)
        if isinstance(current,list):
            if all(isinstance(entry,str) for entry in current):
                matches=[i for i,entry in enumerate(current) if entry==expected]
                assert len(matches)==1,(block,expected)
                current[matches[0]]=p.clean(correction)
            else:
                matches=[entry for entry in current if isinstance(entry,dict) and entry.get('text')==expected]
                assert len(matches)==1,(block,expected)
                matches[0]['text']=p.clean(correction)
        else:
            assert current==expected,(block,current,expected)
            parent[key]=p.clean(correction)
        p.log(f'Front matter source block {block}',original,correction,reason,'high (reviewed)')
    replace_front(18,('foreword',),
        'You will also be asked to step outside your comfort zone.',
        next(e['correction'] for e in edits if e['source_block']==18),
        next(e['reason'] for e in edits if e['source_block']==18))
    replace_front(70,('howto','paras'),
        'Welcome to the TOEFL House-Master speaking course designed to help you do more than simply learn English.',
        next(e['correction'] for e in edits if e['source_block']==70),
        next(e['reason'] for e in edits if e['source_block']==70))
    epigraph_edit=next(e for e in edits if e['source_block']==121)
    if epigraph_edit.get('action')=='remove':
        assert front['epigraph']==p.clean(epigraph_edit['original']),(121,front['epigraph'])
        front['epigraph']=''
        p.log('Front matter source block 121',epigraph_edit['original'],
              '(attributed epigraph removed from publication export)',epigraph_edit['reason'],'high (rights pending)')
    else:
        replace_front(121,('epigraph',),epigraph_edit['original'],
                      epigraph_edit['correction'],epigraph_edit['reason'])
    # The last outcome sentence was collected once as a list item and again
    # as the How-to closing. Keep the intended closing occurrence only.
    closing=front['howto']['closing']
    chapter4=front['howto']['chapters'][3]['you_will']
    if chapter4.count(closing)==1:
        chapter4.remove(closing)
        p.log('Front matter duplicate outcome sentence',closing,closing,
              'Remove the accidental duplicate from the Chapter 4 bullet list; retain the same source sentence once as the How-to closing.')
    else:
        raise ValueError('Expected one duplicated How-to outcome sentence in Chapter 4 list')
    # Apply cell-level copyedits only to the Standard model after parsing.
    for edit in table_edits:
        matches=[b for u in units for c in u['chapters'] for b in c['blocks']
                 if b.get('k')=='table' and b.get('src')==edit['source_block']]
        assert len(matches)==1,edit
        table=matches[0]
        flat=[(ri,ci) for ri,row in enumerate(table['rows']) for ci,_ in enumerate(row)]
        ri,ci=flat[edit['cell']]
        assert table['rows'][ri][ci]==p.clean(edit['original']),edit
        table['rows'][ri][ci]=edit['correction']
        p.log(f"U4 Ch4 pronunciation/table source block {edit['source_block']} cell {edit['cell']}",
              edit['original'],edit['correction'],edit['reason'],'high (verified)')
    # Vocabulary sentences merged into duplicated Before You Read paragraphs
    # belong to the preceding Vocabulary Check, not after the discussion.
    for unit_number in (3,7):
        chapter=units[unit_number-1]['chapters'][0]
        filltext=p.BYR_STRAY_FILLIN[unit_number]
        matches=[i for i,b in enumerate(chapter['blocks']) if b.get('k')=='fill' and b.get('text')==filltext]
        before=[i for i,b in enumerate(chapter['blocks']) if b.get('k')=='sec' and b.get('text')=='Before You Read']
        vocab=[i for i,b in enumerate(chapter['blocks']) if b.get('k')=='sec' and b.get('text')=='Vocabulary Check']
        assert len(matches)==len(before)==len(vocab)==1 and vocab[0]<before[0],unit_number
        fill=chapter['blocks'].pop(matches[0])
        before_index=next(i for i,b in enumerate(chapter['blocks']) if b.get('k')=='sec' and b.get('text')=='Before You Read')
        chapter['blocks'].insert(before_index,fill)
        p.log(f'U{unit_number} Ch1 vocabulary-check placement',filltext,filltext,
              'Move the merged fill-in sentence back into the Vocabulary Check before Before You Read; sentence text unchanged.')
    # The one-line connected-speech source was jammed together and looked like
    # spelling-to-pronunciation notation; the pre-parse override keeps phrases
    # as neutral practice prompts rather than fabricated phonetic spellings.
    units[4]['title']='Living with AI (Artificial Intelligence)'
    p.resmarten.fixed=[];p.resmarten(front);p.resmarten(units)
    structural=json.loads((DEST/'structural-edits.json').read_text())
    for edit in structural:
        blocks=units[edit['unit']-1]['chapters'][edit['chapter']-1]['blocks']
        matches=[b for b in blocks if b.get('text')==edit['text'] and b['k'] in (edit['from'],edit['to'])]
        assert len(matches)==1,edit
        already_classified=matches[0]['k']==edit['to']
        matches[0]['k']=edit['to']
        reason=edit.get('reason','Formatting only: an existing topic/clinic label is restored as a heading, not a numbered question.')
        if already_classified and edit['from']!=edit['to']:
            reason+=' The corrected text is already recognized with this role by the source parser.'
        p.log(f"U{edit['unit']} Ch{edit['chapter']} structural role",edit['text'],edit['text'],reason)
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
          'front':front,'units':units,
          'research_references':json.loads((DEST/'research-references.json').read_text())}
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
            source_cell=n if item['type']=='table' else None
            reviewed=next((e for e in json.loads((DEST/'copyedits.json').read_text())
                           if e['source_block']==item['i'] and e.get('cell')==source_cell),None)
            if reviewed and (reviewed.get('action')=='remove' or reviewed['correction']!=value):
                retained=False
            row={'source_block':item['i'],'cell':source_cell,
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
            if u in p.BYR_STRAY_FILLIN:
                assert canonical(p.BYR_STRAY_FILLIN[u]) in target
                reason='Repeated Before You Read text collapsed; each distinct original question retained. The merged vocabulary fill-in is restored to the preceding Vocabulary Check.'
            else:
                reason='Repeated Before You Read text collapsed; each distinct original question retained.'
        elif 'Chooses 10 expressions' in original:
            assert canonical(original.replace('Chooses 10','Choose 10')) in canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][2])))
            reason='Imperative grammar: Chooses 10 corrected to Choose 10; exercise unchanged.'
        elif original.startswith('Activity '):
            tail=re.sub(r'^Activity \d+:\s*','',original)
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert canonical(tail) in target
            reason='Activity heading and instruction separated; duplicated activity numbers regularized; wording retained.'
        elif (edit:=next((e for e in json.loads((DEST/'copyedits.json').read_text())
                          if e['source_block']==i and 'cell' in e and e['cell']==row['cell']),None)) is not None:
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert canonical(edit['correction']) in target,(i,row['cell'],edit['correction'])
            reason=edit['reason']
        elif i in p.REMOVE_ITEMS:
            edit=next(e for e in json.loads((DEST/'copyedits.json').read_text())
                      if e['source_block']==i and e.get('action')=='remove')
            reason=edit['reason']
        elif i==1676:
            edit=next(e for e in json.loads((DEST/'copyedits.json').read_text())
                      if e['source_block']==i and 'cell' not in e)
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert all(canonical(phrase) in target for phrase in p.JAM_FIXES[i]),(i,p.JAM_FIXES[i])
            reason=edit['reason']+' Phrases are retained as separate practice targets; the joined source is not copied as a pronunciation transcription.'
        elif i in p.TEXT_FIXES and i<166:
            edit=next(e for e in json.loads((DEST/'copyedits.json').read_text())
                      if e['source_block']==i and 'cell' not in e)
            target=canonical(' '.join(strings(book['front'])))
            assert canonical(edit['correction']) in target,(i,edit['correction'])
            reason=edit['reason']
        elif i in p.TEXT_FIXES:
            edit=next(e for e in json.loads((DEST/'copyedits.json').read_text())
                      if e['source_block']==i and 'cell' not in e)
            target=canonical(' '.join(strings(book['units'][p.unit_of(i)-1]['chapters'][p.chap_of(i)[0]-1])))
            assert canonical(edit['correction']) in target,(i,edit['correction'])
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
    copyedits=json.loads((DEST/'copyedits.json').read_text())
    edit_by_source={e['source_block']:e for e in copyedits if 'cell' not in e and e.get('action')!='remove'}
    for unit in book['units']:
        previous=-1;indices=[]
        for block in unit['chapters'][0]['blocks']:
            if block['k']!='reading':continue
            candidates=[x for x in p.items if x['type']=='para' and p.unit_of(x['i'])==unit['number']
                        and p.chap_of(x['i']) and p.chap_of(x['i'])[0]==1 and canonical(x['text'])==canonical(block['text'])]
            if not candidates:
                corrected=[source_id for source_id,edit in edit_by_source.items()
                           if canonical(edit['correction'])==canonical(block['text'])
                           and p.unit_of(source_id)==unit['number'] and p.chap_of(source_id)
                           and p.chap_of(source_id)[0]==1]
                candidates=[x for x in p.items if x['type']=='para' and x['i'] in corrected]
            assert len(candidates)==1,(unit['number'],block['text'][:70])
            source=candidates[0];assert source['i']>previous;previous=source['i'];indices.append(previous)
        assert indices
        reading_evidence.append({'unit':unit['number'],'original_paragraphs_in_order':indices,
                                 'paragraphs':len(indices),'replacement_reading':False})
    model_images=[u['image'] for u in book['units']]+[b['img'] for u in book['units'] for c in u['chapters'] for b in c['blocks'] if b.get('img')]
    assert len(model_images)==24 and set(model_images)==set(p.image_map.values())
    assert not any(b.get('role')=='listening-script' for u in book['units'] for c in u['chapters'] for b in c['blocks'])
    save(DEST/'source-audit-summary.json',{'source_sha256':digest(ROOT/'Master Speaking.docx'),
         'method':'Normalized text presence checked within original unit/chapter, with explicit dispositions for structural/copyedit differences. Reading paragraphs additionally checked in original order. Original embedded illustrations were excluded from exports and replaced with newly drawn geometric artwork because permissions were undocumented. This is not a character-for-character facsimile or independent editorial/legal clearance.',
         'nonempty_source_paragraphs_and_cells':len(ledger),
         'differences_with_explicit_dispositions':sum(not x['retained_normalized'] for x in ledger),
         'unexplained_differences':0,'source_illustrations_excluded':24,
         'original_replacement_illustrations':24,'reading_passages':reading_evidence})
    print('Source passages/cells:',len(ledger),'requiring reconciliation:',len(missing))


def artwork():
    """Exclude unlicensed source art; draw original geometric replacements in staging only."""
    from zipfile import ZipFile
    from io import BytesIO
    from PIL import Image
    from standard_artwork import generate
    import hashlib
    records=[];provenance=[];descriptions={};unmapped_media=[]
    with ZipFile(ROOT/'Master Speaking.docx') as archive:
        mapping=json.loads((WORK/'book/artifacts/image_map.json').read_text())
        mapped_files=set(mapping.values())
        assert len(mapped_files)==24
        for member in archive.namelist():
            if member.startswith('word/media/') and Path(member).name not in mapped_files:
                data=archive.read(member)
                unmapped_media.append({'source_file':Path(member).name,
                    'source_sha256':hashlib.sha256(data).hexdigest(),
                    'source_bytes':len(data),
                    'source_permission_status':'Unverified; additional Office image-layer payload linked through an extension in the protected source DOCX; excluded from Standard exports.',
                    'exported':False})
        for filename in sorted(mapped_files):
            source=archive.read('word/media/'+filename)
            source_sha=hashlib.sha256(source).hexdigest()
            with Image.open(BytesIO(source)) as image:source_pixels=list(image.size)
            path=WORK/'book/assets/images'/filename
            alt=generate(filename,path,tuple(source_pixels))
            descriptions[filename]=alt
            entry={'file':filename,'path':str(path.relative_to(WORK)),
                   'sha256':digest(path),'alt':alt,
                   'origin':'Original geometric illustration generated by book/tools/standard_artwork.py using generic shapes, course-owned labels, and bundled Source Sans 3 fonts under the SIL Open Font License; no source image, video still, logo, or speaker likeness imported.'}
            if filename.endswith('.gif'):
                twin=path.with_suffix('.png')
                with Image.open(path) as image:image.convert('RGB').save(twin)
                entry['aliases']={twin.name:digest(twin)}
            records.append(entry)
            with Image.open(path) as image:replacement_pixels=list(image.size)
            provenance.append({'source_file':filename,'source_sha256':source_sha,
                               'source_pixels':source_pixels,
                               'source_permission_status':'Unverified; exact source artwork is retained only inside the protected original DOCX and is not exported.',
                               'replacement_file':filename,'replacement_sha256':digest(path),
                               'replacement_pixels':replacement_pixels,
                               'export_aliases':({twin.name:digest(twin)} if filename.endswith('.gif') else {}),
                               'replacement_origin':'Original geometric illustration drawn by book/tools/standard_artwork.py with generic shapes, course-owned labels, and bundled Source Sans 3 fonts under the SIL Open Font License (book/assets/fonts/source-sans-LICENSE.md); no external images, video stills, logos, or speaker likenesses imported.',
                               'release_note':'Publisher/legal review of the replacement set remains required.'})
    save(DEST/'image-descriptions.json',descriptions)
    records.append({'file':'cover.png','path':'book/assets/cover.png',
                    'sha256':digest(WORK/'book/assets/cover.png'),
                    'alt':'Master Speaking by Abdul Raziq Nazari. Review proof, not approved for publication. Green cover with original geometric conversation paths.'})
    save(WORK/'book/master/image-descriptions.json',{'images':records})
    save(DEST/'artwork-provenance.json',provenance)
    save(DEST/'unmapped-source-media.json',unmapped_media)
    audit=json.loads((DEST/'source-audit-summary.json').read_text())
    audit['additional_unmapped_source_media_excluded']=unmapped_media
    save(DEST/'source-audit-summary.json',audit)


def production():
    # Adapt only staging copies. Keep the unprefixed self-contained edition untouched.
    path=WORK/'book/tools/cover.py'
    source=path.read_text()
    source=source.replace('An English speaking course in eight thematic units',
                          'Original-manuscript review edition')
    source=source.replace('to an original story, recover details and clarify meaning.',
                          'to the course videos, recover details and clarify meaning.')
    source=source.replace('Fictional listening scripts are included for a teacher or partner to read aloud. No external video or subscription is required.',
                          'The original video-based listening lessons are retained. The course instructor must arrange the required video resources before teaching these lessons.')
    assert source.count('THE TOEFL HOUSE')==2
    source=source.replace('THE TOEFL HOUSE','REVIEW PROOF - NOT APPROVED FOR PUBLICATION')
    path.write_text(source)

    # Replace unverified copyright and publisher claims with a transparent
    # proof notice; the original source and its rights remain unchanged.
    master_path=WORK/'book/tools/master.py'
    master_source=master_path.read_text()
    epigraph_marker="epi = book['front']['epigraph']\nparts.append("
    assert master_source.count(epigraph_marker)==1
    master_source=master_source.replace(epigraph_marker,
        "epi = book['front']['epigraph']\nif epi:\n    parts.append(",1)
    start=master_source.index('# copyright\n')
    end=master_source.index('# foreword\n',start)
    copyright_block = (
        "# copyright\n"
        "parts.append('<section class=\"fm\" data-part=\"copyright\" id=\"copyright\">\\n'\n"
        "             '<p class=\"copyright-line\">Review proof; not approved for publication.</p>\\n'\n"
        "             '<p class=\"copyright-line\">Author and publisher attributions have not been independently verified.</p>\\n'\n"
        "             '<p class=\"copyright-line\">Supplied source illustrations and the attributed epigraph are omitted from this export. Manuscript rights, attribution, and external-media permissions remain unverified; replacement illustrations need publisher/legal review.</p>\\n'\n"
        "             '</section>')\n\n"
    )
    master_source=master_source[:start]+copyright_block+master_source[end:]
    marker="doc = f" + chr(39)*3
    assert master_source.count(marker)==1
    references_code = (
        "# Standard-edition research references are end matter, not source manuscript text.\n"
        "research_references = book.get('research_references', [])\n"
        "if research_references:\n"
        "    reference_lines = [\n"
        "        '<section class=\"fm\" data-part=\"references\" id=\"research-references\">',\n"
        "        '<h1 class=\"fm-head\">Selected Research References</h1>',\n"
        "        '<p>These references support the qualified research claims cited in the readings. They do not constitute publication, rights, or course-owner clearance.</p>'\n"
        "    ]\n"
        "    for ref in research_references:\n"
        "        url = ref.get('url') or ''\n"
        "        link = (f' <a href=\"{html.escape(url, quote=True)}\">{esc(url)}</a>' if url else '')\n"
        "        reference_lines.append(f'<p class=\"reference\">{esc(ref[\"citation\"])}{link}</p>')\n"
        "    reference_lines.append('</section>')\n"
        "    parts.append('\\n'.join(reference_lines))\n\n"
    )
    master_source=master_source.replace(marker,references_code+marker,1)
    master_path.write_text(master_source)

    # The shared Word renderer treats unknown front-matter sections as
    # non-printing metadata. Append this one as back matter, after Unit 8.
    wordmaster_path=WORK/'book/tools/wordmaster.py'
    wordmaster_source=wordmaster_path.read_text()
    keep_marker="            first=next(i for i,p in enumerate(paragraphs) if p.text==override['keep_from'])"
    assert wordmaster_source.count(keep_marker)==1
    pagebreak_logic=(
        "            if 'page_break_before_text' in override:\n"
        "                target=next(p for p in paragraphs if p.text==override['page_break_before_text'])\n"
        "                target.paragraph_format.page_break_before=True\n"
        "                continue\n"
    )
    wordmaster_source=wordmaster_source.replace(keep_marker,pagebreak_logic+keep_marker,1)
    wordmaster_source=wordmaster_source.replace(
        "cp.title = 'Master Speaking'",
        "cp.title = 'Master Speaking — Original-Manuscript Review Proof'")
    wordmaster_source=wordmaster_source.replace(
        "cp.subject = 'English speaking course'",
        "cp.subject = 'Review proof; not approved for publication'" )
    word_marker='doc.save(OUT)'
    assert wordmaster_source.count(word_marker)==1
    word_refs=(
        "reference_part = body.find('x:section[@data-part=\"references\"]', NS)\n"
        "if reference_part is not None:\n"
        "    heading = add_par('Selected Research References', 'MS FM Head')\n"
        "    heading.paragraph_format.page_break_before = True\n"
        "    for reference in reference_part.findall('x:p', NS):\n"
        "        add_par(text_of(reference), 'MS Body')\n\n"
    )
    wordmaster_source=wordmaster_source.replace(word_marker,word_refs+word_marker,1)
    wordmaster_path.write_text(wordmaster_source)

    epub_path=WORK/'book/tools/epub.py'
    epub_source=epub_path.read_text().replace(
        'Master Speaking / Abdul Raziq Nazari / 2026',
        'Master Speaking / Abdul Raziq Nazari / 2026 / Original-manuscript course edition')
    epub_source=epub_source.replace(
        'Listening exercises use included fictional scripts read aloud by a teacher or partner; no recorded audio is supplied.',
        'Listening exercises require the original external course videos, which are not embedded. The Standard-edition media register lists independently located candidates; intended-source confirmation and permissions remain unverified.')
    epub_source=epub_source.replace(
        "dc('description', 'An English speaking course: eight units on communication, goals, emotional intelligence, money, AI, marriage, globalization, and English as a lingua franca.')",
        "dc('description', 'Original-manuscript review proof; not approved for publication. Original video-based listening lessons require external resources; intended-source confirmation, availability, exercise alignment, and permissions remain unverified.')")
    assert 'Original-manuscript review proof; not approved for publication.' in epub_source
    assert 'Listening exercises require the original external course videos' in epub_source

    # Permit outbound links only on citation anchors; no external resources
    # are loaded by the EPUB, so media remains unembedded and unverified.
    qa_epub_path=WORK/'book/tools/qa_epub.py'
    qa_epub_source=qa_epub_path.read_text()
    qa_start=qa_epub_source.index('    if REMOTE.search(raw_txt):')
    qa_end=qa_epub_source.index('# css url() resolution',qa_start)
    qa_epub_block=(
        "    # Bibliography anchors may point outward; loaded resources may not.\n"
        "    remote_ref = re.compile(r'^(?:https?:)?//', re.I)\n"
        "    base = os.path.dirname(zp)\n"
        "    for el in doc.iter():\n"
        "        src = el.get('src')\n"
        "        href_ref = el.get('href')\n"
        "        if src and remote_ref.match(src):\n"
        "            err(f'{zp}: remote src resource')\n"
        "            continue\n"
        "        if href_ref and remote_ref.match(href_ref):\n"
        "            if el.tag == f'{{{XH}}}a':\n"
        "                continue\n"
        "            err(f'{zp}: remote href resource')\n"
        "            continue\n"
        "        ref = src if el.tag == f'{{{XH}}}img' else href_ref\n"
        "        if ref and not ref.startswith('#'):\n"
        "            tgt = ref.split('#')[0]\n"
        "            target = os.path.normpath(os.path.join(base, tgt)).replace('\\\\\\\\', '/')\n"
        "            if target not in names:\n"
        "                err(f'{zp}: reference {ref!r} unresolved in zip')\n"
        "\n"
    )
    qa_epub_source=qa_epub_source[:qa_start]+qa_epub_block+qa_epub_source[qa_end:]
    qa_epub_path.write_text(qa_epub_source)

    qa_word_path=WORK/'book/tools/qa_word.py'
    qa_word_source=qa_word_path.read_text()
    old_fm='    \'MS FM Head\': 2,                      # Foreword + How to Use'
    assert qa_word_source.count(old_fm)==1
    qa_word_source=qa_word_source.replace(old_fm,
        "    'MS FM Head': mcount('h1', 'fm-head'), # Semantic front/back matter headings")
    qa_word_path.write_text(qa_word_source)

    nav_marker='    # ---- nav doc ---------------------------------------------------------'
    assert epub_source.count(nav_marker)==1
    epub_refs = (
        "    # ---- back matter: research references -------------------------------\n"
        "    for sec in q(body, './x:section[@data-part=\"references\"]'):\n"
        "        children = copy_children(sec)\n"
        "        for child in children:\n"
        "            fix_img_paths(child)\n"
        "        add_xhtml('research-references.xhtml', 'Selected Research References', children,\n"
        "                  'Selected Research References', 1)\n\n"
    )
    epub_source=epub_source.replace(nav_marker,epub_refs+nav_marker,1)
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
         'scope':'Original manuscript text, readings, exercises, and external video dependencies. Supplied image assets and the attributed epigraph are excluded from exports; 24 original geometric replacements are included. Separate from the accepted self-contained edition.',
         'publication_status':'Review proof; not approved for publication.',
         'rights_status':'Manuscript rights, final author/publisher attribution, remaining quotations, external media, and replacement-artwork approval remain outstanding; supplied source images and the attributed epigraph are excluded from exports.',
         'checks_passed':sum(r['exit_code']==0 for r in results.values()),'checks_run':len(results)})
    freshness=subprocess.run([sys.executable,str(ROOT/'book/tools'/'qa_standard.py')],capture_output=True,text=True)
    print('qa_standard',freshness.returncode,freshness.stdout[-700:],flush=True)
    if freshness.returncode:
        raise SystemExit('Standard edition freshness/identity check failed; see book/standard/qa_standard.json.')
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

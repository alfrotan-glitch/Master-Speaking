#!/usr/bin/env python3
"""Cover all vocabulary completion stems without treating reflections as blanks."""
from pathlib import Path
import copy
import json
import re
ROOT=Path(__file__).resolve().parents[2]


def inspect(book,keys):
    issues=[];expected=[]
    for unit in book['units']:
        blocks=unit['chapters'][0]['blocks']
        start=next((i for i,b in enumerate(blocks) if b.get('text')=='Vocabulary Check'),None)
        if start is None:continue
        end=next(i for i,b in enumerate(blocks) if b.get('text')=='Before You Read')
        vocab={r[0].casefold() for b in blocks if b.get('role')=='vocab' for r in b['rows'][1:]}
        fills=[b['text'] for b in blocks[start:end] if b['k']=='fill']
        for i,stem in enumerate(fills,1):
            identity=(unit['number'],i,stem);expected.append(identity)
            matches=[k for k in keys if (k['unit'],k['item'],k['stem'])==identity]
            if len(matches)!=1:
                issues.append(f'Vocabulary key missing/duplicate/stale: U{unit["number"]} item {i}');continue
            key=matches[0]
            if key['source_expression'].casefold() not in vocab:issues.append('Unknown source expression: '+key['source_expression'])
            if not key['answer'].strip() or re.sub(r'_{2,}',lambda _:key['answer'],stem)!=key['completed_sentence']:
                issues.append('Invalid completed-sentence example: '+stem)
    if len(keys)!=len(expected) or len(set((k['unit'],k['item']) for k in keys))!=len(expected):
        issues.append('Vocabulary key inventory mismatch')
    return issues


def main():
    book=json.loads((ROOT/'book/artifacts/book.json').read_text())
    keys=json.loads((ROOT/'book/classroom/vocabulary-keys.json').read_text())
    issues=inspect(book,keys)
    bad=copy.deepcopy(keys);bad[0]['stem']='Changed question'
    bad_detected=bool(inspect(book,bad))
    missing_detected=bool(inspect(book,keys[:-1]))
    if not bad_detected or not missing_detected:issues.append('Vocabulary key negative control failed')
    import pymupdf
    normalize=lambda value:re.sub(r'[\W_]+','',value).casefold()
    with pymupdf.open(ROOT/'Master-Speaking-Teacher-Implementation-Pack.pdf') as pdf:
        pages=[normalize(page.get_text()) for page in pdf]
    for key in keys:
        parts=[key['stem'],'Suggested answer: '+key['answer'],'Completed sentence: '+key['completed_sentence']]
        if key['alternatives']:parts.append('Other acceptable completions: '+'; '.join(key['alternatives'])+'.')
        if not any(all(normalize(part) in page for part in parts) for page in pages):
            issues.append(f'U{key["unit"]} item {key["item"]}: complete vocabulary key must fit on one teacher-pack page')
    report={'ok':not issues,'items':len(keys),'units':7,'complete_key_items_kept_on_one_page':not issues,'stale_stem_mutation_rejected':bad_detected,
            'missing_key_mutation_rejected':missing_detected,'issues':issues,
            'scope':'All 36 vocabulary-completion stems, source-expression identities and completed-sentence examples. Suggested answers may admit suitable alternatives. Not automatic semantic proof, open personal reflections or independent specialist approval.'}
    (ROOT/'book/artifacts/qa_vocabulary_keys.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));raise SystemExit(bool(issues))


if __name__=='__main__':main()

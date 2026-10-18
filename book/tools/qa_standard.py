#!/usr/bin/env python3
"""Freshness and edition-identity checks, independent of the replacement edition."""
from pathlib import Path
import hashlib,json,zipfile,uuid
from lxml import etree
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'book/standard'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(n):return json.loads((D/n).read_text())
m=load('build-manifest.json');issues=[]
def check(ok,message):
    if not ok:issues.append(message)
check(sha(ROOT/m['source'])==m['source_sha256'],'Original manuscript hash mismatch')
for name,digest in m['outputs'].items():check(sha(ROOT/name)==digest,f'Output hash mismatch: {name}')
check(sha(D/'book.json')==m['semantic_sha256'],'Semantic book changed since build')
check(sha(D/'master.xhtml')==m['master_sha256'],'Master changed since build')
for name,digest in load('protected-inputs.json')['sha256'].items():
    check(sha(ROOT/name)==digest,f'Accepted edition/source changed: {name}')
check(all(x['exit_code']==0 for x in load('production-checks.json').values()),'A production check failed')
check(load('epubcheck-official.json')['sha256']==sha(ROOT/'Master-Speaking-Standard.epub'),'EPUBCheck report is stale')
check(load('epubcheck-official.json')['valid'],'Official EPUBCheck failed')
check(load('source-audit-summary.json')['unexplained_differences']==0,'Unexplained source differences')
check(all(x.get('disposition') for x in load('source-ledger.json')),'Source ledger has unexplained entries')
b=load('book.json');plan=json.loads((ROOT/'book/master/chapter-titles.json').read_text())
check([u['number'] for u in b['units']]==list(range(1,9)),'Unit order changed')
check(sum(len(u['chapters']) for u in b['units'])==32,'Chapter count mismatch')
for u,p in zip(b['units'],plan):check([c['title'] for c in u['chapters']]==p['titles'],'Source-backed chapter titles changed')
with zipfile.ZipFile(ROOT/'Master-Speaking-Standard.epub') as z:
    opf=etree.fromstring(z.read('content.opf'))
    ns={'o':'http://www.idpf.org/2007/opf','d':'http://purl.org/dc/elements/1.1/'}
    summary=opf.xpath('string(//o:meta[@property="schema:accessibilitySummary"])',namespaces=ns)
    check('original external course videos' in summary and 'fictional scripts' not in summary,'EPUB has the wrong edition accessibility summary')
    identifier=opf.xpath('string(//d:identifier)',namespaces=ns)
    expected='urn:uuid:'+str(uuid.uuid5(uuid.NAMESPACE_URL,'Master Speaking / Abdul Raziq Nazari / 2026 / Original-manuscript course edition'))
    check(identifier==expected,'EPUB edition identifier mismatch')
result={'status':'PASS' if not issues else 'FAIL','issues':issues,'outputs_checked':len(m['outputs']),
        'edition':'Original-manuscript course edition; not the self-contained edition',
        'scope':'Freshness, identity and source/accepted-edition protection; not editorial or legal clearance'}
(D/'qa_standard.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
raise SystemExit(bool(issues))

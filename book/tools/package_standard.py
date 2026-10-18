#!/usr/bin/env python3
"""Package only the manuscript edition, never the other edition's teacher keys."""
from pathlib import Path
import hashlib,json,subprocess,sys
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(ROOT/'book/tools/qa_standard.py')],check=True)
manifest=json.loads((ROOT/'book/standard/build-manifest.json').read_text())
proof=json.loads((ROOT/'book/standard/qa/reviewed.json').read_text())
if proof['pdf_sha256']!=manifest['outputs']['Master-Speaking-Standard-print-7x10.pdf']:
    raise SystemExit('Visual-review record does not match current interior; inspect it before packaging.')
files=list(manifest['outputs'])+['STANDARD-EDITION-READ-ME.md','STANDARD-EDITION-REVIEW.md']
output=ROOT/'Master-Speaking-Standard-Edition.zip'
with ZipFile(output,'w',compression=ZIP_DEFLATED,compresslevel=9) as z:
    for name in files:z.write(ROOT/name,name)
    z.write(ROOT/'book/standard/build-manifest.json','build-manifest.json')
with ZipFile(output) as z:
    assert z.testzip() is None
    for name,digest in manifest['outputs'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest
print(f'Verified {len(manifest["outputs"])} edition files and 3 handoff records; {output.name} ({output.stat().st_size:,} bytes)')

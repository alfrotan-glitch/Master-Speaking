#!/usr/bin/env python3
"""Build the download bundle only from exports matching the current QA summary."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]


def main():
    progress = json.loads((ROOT / 'book/artifacts/rewrite-progress.json').read_text())
    checks = json.loads((ROOT / 'book/artifacts/qa_october_run.json').read_text())
    if not checks or any(row['exit_code'] for row in checks.values()):
        raise SystemExit('Bundle refused: release checks are missing or failing.')
    if progress['release_checks'] != {key: row['exit_code'] for key, row in checks.items()}:
        raise SystemExit('Bundle refused: revision status does not match the release checks.')
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    if progress['semantic_content_sha256'] != digest(ROOT / 'book/artifacts/book.json'):
        raise SystemExit('Bundle refused: revision summary does not match the semantic source.')
    files = ['Master-Speaking.pdf', 'Master-Speaking-print-7x10.pdf',
             'Master-Speaking-7x10.docx', 'Master-Speaking.epub', 'Master-Speaking-Front-Cover.pdf']
    for pack in ['Student-Practice-Pack', 'Teacher-Implementation-Pack', 'Class-Companion']:
        files.extend(f'Master-Speaking-{pack}.{ext}' for ext in ['pdf', 'docx'])
    for name in files:
        if digest(ROOT / name) != progress['sha256'].get(name):
            raise SystemExit(f'Bundle refused: changed or unchecked export: {name}')
    readme = f'''Master Speaking — revised editions

Start with Master-Speaking.pdf ({progress['reader_pages']} pages including cover).
The separate print interior has {progress['interior_pages']} pages, 7 x 10 inches.
The front-cover file is a concept, not a complete printer-specific cover wrap.
Main editable book: Master-Speaking-7x10.docx. Reflowable ebook: Master-Speaking.epub.
The three supporting books each include PDF and editable Word editions.
Keep teacher scripts and answers separate from learners during listening.
The Reading-Edition PDF alias is identical to Master-Speaking.pdf and is not duplicated here.

All {len(checks)} release checks pass. This does not certify commercial clearance,
independent every-word/every-page proof, accessibility conformance or printer approval.
Original recordings and third-party permissions still require verification.
Teacher-read alternatives are newly authored, not original recording transcripts.

SHA-256 checksums
'''
    readme += ''.join(f'{progress["sha256"][name]}  {name}\n' for name in files)
    out = ROOT / 'Master-Speaking-All-Books.zip'
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in files:
            z.write(ROOT / name, name)
        z.writestr('READ-ME.txt', readme)
    with zipfile.ZipFile(out) as z:
        if z.testzip() is not None:
            raise SystemExit('Bundle integrity check failed.')
    print(f'Bundle verified: {out.name}; {len(files)} editions + guide; {out.stat().st_size/1024**2:.1f} MiB')


if __name__ == '__main__':
    main()

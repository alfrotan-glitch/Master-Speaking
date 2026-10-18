#!/usr/bin/env python3
"""Check recorded first-section review coverage; not a whole-book proof claim."""
from pathlib import Path
import hashlib
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[2]


def review_fields(book):
    fields = []
    for i, paragraph in enumerate(book['front']['foreword']):
        fields.append((['front', 'foreword', i, 'text'], paragraph['text']))
    base = ['units', 0, 'chapters', 0]
    chapter = book['units'][0]['chapters'][0]
    for key in ['title', 'focus']:
        fields.append((base+[key], chapter[key]))
    for i, block in enumerate(chapter['blocks']):
        path = base+['blocks', i]
        if block.get('text'):
            fields.append((path+['text'], block['text']))
        for ri, row in enumerate(block.get('rows', [])):
            for ci, cell in enumerate(row):
                if cell:
                    fields.append((path+['rows', ri, ci], cell))
    return fields


def main():
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    review = json.loads((ROOT / 'book/master/rewrite-review.json').read_text())
    actual = {json.dumps(p): t for p, t in review_fields(book)}
    recorded = {json.dumps(r['path']): r for r in review['fields']}
    issues = []
    if set(actual) != set(recorded) or len(recorded) != len(review['fields']):
        issues.append('Missing, extra or duplicate reviewed fields')
    for path, text in actual.items():
        record = recorded.get(path, {})
        if record.get('sha256') != hashlib.sha256(text.encode()).hexdigest():
            issues.append('Reviewed text changed: '+path)
        if record.get('decision') not in ['revised', 'retained after review']:
            issues.append('Review decision absent: '+path)
    if review['chapters_without_field_level_fingerprints'] != 31 or review['all_chapters_field_fingerprinted']:
        issues.append('Detailed first-section fingerprints must not imply all-chapter field-level proof')
    with pymupdf.open(ROOT / 'Master-Speaking-print-7x10.pdf') as pdf:
        chapter_page = next(p for _, title, p in pdf.get_toc()
                            if title == 'Chapter 1 · The Power of Communication')
        end = next(p for _, title, p in pdf.get_toc()
                   if title == 'Chapter 2 · Are You a Good Listener?')
        pages = [pdf[i].get_text() for i in range(chapter_page-1, end-1)]
        text = re.sub(r'\s+', ' ', ' '.join(pages))
        if not re.search(r'3\. Can someone become successful', text):
            issues.append('Critical-thinking numbering restarts instead of continuing to 3')
        for page in pages:
            if 'Answer the Questions' in page and 'Why do many students avoid speaking English?' not in page:
                issues.append('Question-table heading stranded without its first content row')
    report = {'ok': not issues, 'reviewed_fields': len(actual), 'chapters_field_fingerprinted': 1,
              'chapters_without_field_level_fingerprints': 31, 'issues': issues,
              'scope': 'Detailed fingerprints: foreword and Unit 1 Chapter 1 only. See qa_whole_revision for the separate all-chapter revision pass; neither is independent human proof.'}
    (ROOT / 'book/artifacts/qa_rewrite_review.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

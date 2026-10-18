#!/usr/bin/env python3
"""Every question-plus-options block must fit on a single production PDF page."""
import json
from pathlib import Path
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
normalize = lambda text: re.sub(r'\W+', '', text).casefold()


def main():
    book = json.loads((ROOT / 'book/artifacts/book.json').read_text())
    chapters = [c for u in book['units'] for c in u['chapters']]
    issues = []
    checked = 0
    with pymupdf.open(ROOT / 'Master-Speaking-print-7x10.pdf') as pdf:
        starts = [p for _, title, p in pdf.get_toc() if title.startswith('Chapter ')]
        if len(starts) != len(chapters):
            issues.append('Chapter boundaries missing')
        for ci, (chapter, start) in enumerate(zip(chapters, starts)):
            end = starts[ci+1]-1 if ci+1 < len(starts) else len(pdf)
            pages = [(i+1, normalize(pdf[i].get_text())) for i in range(start-1, end)]
            blocks = chapter['blocks']
            for bi, block in enumerate(blocks[:-1]):
                if block['k'] != 'q' or blocks[bi+1]['k'] != 'opt':
                    continue
                options = []
                for following in blocks[bi+1:]:
                    if following['k'] != 'opt':
                        break
                    options.append(following['text'])
                checked += 1
                if not any(all(normalize(t) in text for t in [block['text']]+options)
                           for _, text in pages):
                    issues.append(f'Chapter sequence {ci+1}: item split or missing: {block["text"][:100]}')
    report = {'ok': not issues, 'items_checked': checked, 'issues': issues,
              'scope': 'Every structured MCQ stem and all its options on one PDF page; not answer correctness or native Word pagination.'}
    (ROOT / 'book/artifacts/qa_mcq_layout.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

# Grammar for Special Speaking — TOEFL HOUSE

> **Learn the grammar. Use it in conversation. Make it part of your speech.**

A practical, independent grammar course for Intermediate and Advanced English learners. The maintained lesson and assessment data in `build_spec/` generate the editable DOCX, print PDF, and reflowable EPUB.

## Final book files

- [PDF — print and digital reading](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.pdf)
- [EPUB — reflowable ebook](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.epub)
- [DOCX — editable Word manuscript](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.docx)
- [HTML — browser/print fallback with in-page navigation](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.html)

The root-level `Grammar for Special Speaking (TOEFL House).docx` remains the generated working manuscript. The copy in `dist/` is the distribution file.

## Rebuild from a clean checkout

Requirements: Python 3.10 or newer, pip, and the system DejaVu Sans fonts (the `fonts-dejavu-core` package on Debian/Ubuntu). Install the font dependency with `sudo apt install fonts-dejavu-core`; the PDF embeds these Unicode-capable fonts. No Word installation is required to build the files.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r build_spec/requirements.txt
.venv/bin/python tools/build_publication.py --all
```

`--all` rebuilds the root DOCX from `build_spec/`, copies it into `dist/`, creates the HTML edition, then generates the PDF and EPUB. Direct build commands are also available:

```bash
.venv/bin/python build_spec/build.py
.venv/bin/python tools/build_html.py
.venv/bin/python tools/build_publication.py
```

## Quality checks

```bash
.venv/bin/python build_spec/qa.py
.venv/bin/python tools/validate_publication.py
```

The source QA checks syllabus titles, all 16 lesson frameworks, pathways, practice/answer-key counts, assessment order and scope, the final-assessment matrix, known grammar regressions, DOCX headings, and A4 layout. The publication validator checks editable DOCX structure, searchable A4 PDF text and bookmarks, EPUB XML/package/navigation/local links, and required-section consistency across formats.

The DOCX has a native, updateable Word contents field and live page-number fields; compatible Word processors are asked to refresh fields on open. If the contents has not refreshed, select it and choose **Update Field / Update entire table**. The EPUB was checked with the project's XML/package/link validator and EbookLib's parser. **EPUBCheck was not available in this environment**, so no EPUBCheck result is claimed. The PDF was structurally checked and rendered for visual inspection at the beginning, contents, diagnostic/baseline, a lesson, a review test, the final assessment/rubric, and the answer-key/end pages. DOCX structure was checked, but rendered DOCX pages still need inspection in Word or LibreOffice.

## Book structure

- Front matter, use guidance, baseline diagnostic and matched speaking sample
- **16 lessons** in eight thematic Parts, each retaining the functional eight-part lesson framework
- Intermediate accuracy pathway and Advanced flexibility pathway
- Three cumulative review tests (Lessons 1–4, 1–8, and 1–12)
- Final assessment: 30 written items, an item-level coverage matrix, and a matched speaking interaction/rubric
- Five appendices, including the complete answer key

See [the assessment coverage matrix](docs/final-assessment-coverage.md) and [editorial audit and issue log](docs/editorial-audit.md).

## Editorial and external-validation status

The source was revised and checked with automated regression gates and a documented editorial audit. This is **not** a claim of independent expert approval, classroom testing, EPUBCheck certification, proven learning gains, or final print approval. Qualified teacher review and a real learner pilot remain pending; blank instruments are provided at [`docs/teacher-review-checklist.md`](docs/teacher-review-checklist.md) and [`docs/pilot-feedback-form.md`](docs/pilot-feedback-form.md).

# Grammar for Special Speaking — TOEFL HOUSE

> **Learn the grammar. Use it in conversation. Make it part of your speech.**

A practical, independent grammar course for Intermediate and Advanced English learners. The maintained lesson and assessment data in `build_spec/` generate the editable DOCX, print PDF, and reflowable EPUB for the Student Book and its companion Teacher's Book.

## Final book files

**Student Book — Grammar for Special Speaking**

- [PDF — print and digital reading](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.pdf)
- [EPUB — reflowable ebook](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.epub)
- [DOCX — editable Word manuscript](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.docx)
- [HTML — browser/print fallback with in-page navigation](dist/Grammar%20for%20Special%20Speaking%20%28TOEFL%20House%29.html)

**Teacher's Book — Grammar for Special Speaking — Teacher's Book**

- [PDF — print and digital reading](dist/Grammar%20for%20Special%20Speaking%20%E2%80%94%20Teacher%27s%20Book%20%28TOEFL%20House%29.pdf)
- [EPUB — reflowable ebook](dist/Grammar%20for%20Special%20Speaking%20%E2%80%94%20Teacher%27s%20Book%20%28TOEFL%20House%29.epub)
- [DOCX — editable Word manuscript](dist/Grammar%20for%20Special%20Speaking%20%E2%80%94%20Teacher%27s%20Book%20%28TOEFL%20House%29.docx)
- [HTML — browser/print fallback with in-page navigation](dist/Grammar%20for%20Special%20Speaking%20%E2%80%94%20Teacher%27s%20Book%20%28TOEFL%20House%29.html)

The root-level `.docx` files remain the generated working manuscripts. The copies in `dist/` are the distribution files.

## Rebuild from a clean checkout

Requirements: Python 3.10 or newer, pip, and the system DejaVu Sans fonts (the `fonts-dejavu-core` package on Debian/Ubuntu). Install the font dependency with `sudo apt install fonts-dejavu-core`; the PDF embeds these Unicode-capable fonts. No Word installation is required to build the files.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r build_spec/requirements.txt
.venv/bin/python tools/build_publication.py --all
```

`--all` rebuilds both DOCX manuscripts from `build_spec/`, copies them into `dist/`, creates both HTML editions, then generates the PDFs and EPUBs. Direct build commands are also available:

```bash
.venv/bin/python build_spec/build.py              # Student Book DOCX
.venv/bin/python build_spec/build_teacher.py       # Teacher's Book DOCX
.venv/bin/python tools/build_html.py              # Both HTML editions
.venv/bin/python tools/build_publication.py       # Both PDF + EPUB editions
```

## Quality checks

```bash
.venv/bin/python build_spec/qa.py
.venv/bin/python tools/validate_publication.py
```

The source QA checks syllabus titles, all 16 lesson frameworks, pathways, practice/answer-key counts, assessment order and scope, the final-assessment matrix, known grammar regressions, DOCX headings, A4 layout, Lesson 1's approved revision (three core rule groups, 5+4 practice), Pair Speaking vs Real Talk separation, and heading-to-content flow. The publication validator checks editable DOCX structure, searchable A4 PDF text and bookmarks, EPUB XML/package/navigation/local links, and required-section consistency across formats.

The DOCX files have native, updateable Word contents fields and live page-number fields; compatible Word processors are asked to refresh fields on open. If the contents has not refreshed, select it and choose **Update Field / Update entire table**. The EPUBs were checked with the project's XML/package/link validator and EbookLib's parser. **EPUBCheck was not available in this environment**, so no EPUBCheck result is claimed. Both PDFs were structurally checked and rendered for visual inspection at the beginning, contents, diagnostic/baseline, a lesson, a review test, the final assessment/rubric, and the answer-key/end pages. DOCX structures were checked, but rendered DOCX pages still need inspection in Word or LibreOffice. No Word/LibreOffice was available in this environment, so rendered-page inspection was performed via the PDF and HTML renderings.

## Book structure

- Student Book front matter including a copyright/publication page, introduction, use guidance, copyright disclaimer, contents, and baseline diagnostic with matched speaking sample
- **16 lessons** in eight thematic Parts, each retaining the functional eight-part lesson framework (Speaking Hook · Simple Rule · See the Difference · Practice the Pattern · Pair Speaking · Advanced Upgrade · Real Talk Challenge · Review / Self-Check), with expected speaking output, planning guidance, model responses and return-to-rule links
- Intermediate accuracy pathway and Advanced flexibility pathway in every lesson
- Three cumulative review tests (Lessons 1–4, 1–8, and 1–12)
- Final assessment: 30 written items, an item-level coverage matrix, and a matched speaking interaction/rubric
- Five appendices, including the complete answer key
- Teacher's Book: front matter, course overview, teaching principles, pacing/feedback guidance, 16 lesson guides with objectives, materials, timing (every lesson totals 60 minutes and matches the Student Book's pacing guidance), step-by-step procedures for all eight functions, answer keys with explanatory notes, model exchanges, assessment guidance for open-ended tasks, differentiation, common-error notes, shorter-session (45-minute) adaptations, and review/consolidation guidance — plus an assessment-guidance section covering the diagnostic, three review-test and final-assessment keys, acceptable alternatives, and a model final speaking response

See [the assessment coverage matrix](docs/final-assessment-coverage.md) and [editorial audit and issue log](docs/editorial-audit.md).

## Editorial and external-validation status

The Student Book and Teacher's Book were produced from shared, reproducible sources and checked with automated regression gates, structural publication validation, and a documented editorial audit. This is **not** a claim of independent expert approval, classroom testing, EPUBCheck certification, proven learning gains, or final print approval. Qualified teacher review and a real learner pilot remain pending; blank instruments are provided at [`docs/teacher-review-checklist.md`](docs/teacher-review-checklist.md) and [`docs/pilot-feedback-form.md`](docs/pilot-feedback-form.md).

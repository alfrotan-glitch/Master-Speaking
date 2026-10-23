# TOEFL HOUSE — Speaking Book Library

> **Speak with purpose. Practise with evidence. Build confidence through real communication.**

This repository houses **two separate but complementary English-speaking coursebooks**. The original **Master Speaking** develops communication, listening, reading-to-speak, discussion, pronunciation, and presentation skills. **Grammar for Special Speaking** is a separate 16-lesson grammar-in-conversation course with Student and Teacher editions. Each has its own production and quality checks.

## Master Speaking — original coursebook

The 24,000-word original `Master Speaking.docx` is preserved without content changes. Reproducible **proof** editions now exist for review; they are not represented as independently approved, fully edited print releases.

- [A4 PDF — 123-page print proof](proof/Master%20Speaking%20%28TOEFL%20House%29.pdf)
- [EPUB3 — ebook proof with curated topic navigation](proof/Master%20Speaking%20%28TOEFL%20House%29.epub)
- [DOCX — editable working proof](proof/Master%20Speaking%20%28TOEFL%20House%29.docx)
- [HTML — standalone browser proof](proof/Master%20Speaking%20%28TOEFL%20House%29.html)

The PDF and EPUB contain 12 topic-oriented navigation entries, rather than hundreds of exercise-question bookmarks. See the [Master Speaking publication audit](docs/master-speaking-publication-audit.md), [heading inventory](docs/master-speaking-heading-inventory.md), and [production instructions](build_master/README.md).

## Grammar for Special Speaking — Student and Teacher Books

> **Learn the grammar. Use it in conversation. Make it part of your speech.**

A dedicated grammar-speaking resource for one shared classroom, using core practice and optional stretch challenges without dividing students into labelled proficiency groups. The maintained lesson and assessment data in `build_spec/` generate editable DOCX, A4 PDF, HTML and reflowable EPUB for both volumes.

## Generated book editions

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

The source QA checks syllabus titles, all 16 lesson frameworks, pathways, practice/answer-key counts, assessment order and scope, the final-assessment matrix, known grammar regressions, DOCX headings, A4 layout, Lesson 1's approved revision (three core rule groups, 5+4 practice), Pair Speaking vs Real Talk separation, and heading-to-content flow. The publication validator checks **both the Student Book and Teacher's Book** independently for DOCX structure, searchable A4 PDF text and bookmarks, EPUB XML/package/navigation/local links, and required-section consistency across formats.

The DOCX files have native, updateable Word contents fields and live page-number fields; compatible Word processors are asked to refresh fields on open. If the contents has not refreshed, select it and choose **Update Field / Update entire table**. The EPUBs were checked with the project's XML/package/link validator and EbookLib's parser. **EPUBCheck was not available in this environment**, so no EPUBCheck result is claimed. Both PDFs were structurally checked and rendered for visual inspection at the beginning, contents, diagnostic/baseline, a lesson, a review test, the final assessment/rubric, and the answer-key/end pages. DOCX structures were checked, but rendered DOCX pages still need inspection in Word or LibreOffice. No Word/LibreOffice was available in this environment, so rendered-page inspection was performed via the PDF and HTML renderings.

## Book structure

- Student Book front matter including a copyright/publication page, introduction, use guidance, copyright disclaimer, contents, and baseline diagnostic with matched speaking sample
- **16 lessons** in eight thematic Parts, each retaining the functional eight-part lesson framework (Speaking Hook · Simple Rule · See the Difference · Practice the Pattern · Pair Speaking · Advanced Upgrade · Real Talk Challenge · Review / Self-Check), with expected speaking output, planning guidance, model responses and return-to-rule links
- One shared classroom sequence in each lesson: build the pattern, then stretch the answer when ready; no learner-level labels in the Student Book
- Three cumulative review tests (Lessons 1–4, 1–8, and 1–12)
- Final assessment: 30 written items, an item-level coverage matrix, and a matched speaking interaction/rubric
- Five appendices, including the complete answer key
- Teacher's Book: front matter, course overview, teaching principles, pacing/feedback guidance, 16 lesson guides with objectives, materials, timing (every lesson totals 60 minutes and matches the Student Book's pacing guidance), step-by-step procedures for all eight functions, answer keys with explanatory notes, model exchanges, assessment guidance for open-ended tasks, differentiation, common-error notes, shorter-session (45-minute) adaptations, and review/consolidation guidance — plus an assessment-guidance section covering the diagnostic, three review-test and final-assessment keys, acceptable alternatives, and a model final speaking response

See [the assessment coverage matrix](docs/final-assessment-coverage.md) and [editorial audit and issue log](docs/editorial-audit.md).

## Editorial and external-validation status

The Student Book and Teacher's Book were produced from shared, reproducible sources and checked with automated regression gates, structural publication validation, and a documented editorial audit. This is **not** a claim of independent expert approval, classroom testing, EPUBCheck certification, proven learning gains, or final print approval. Qualified teacher review and a real learner pilot remain pending; blank instruments are provided at [`docs/teacher-review-checklist.md`](docs/teacher-review-checklist.md) and [`docs/pilot-feedback-form.md`](docs/pilot-feedback-form.md).

## Source-of-truth and release safeguards

The editable `build_spec/` content is the source of truth for **Grammar for Special Speaking** (Student and Teacher editions); changing a source file alone does **not** update previously exported books. The editorial branch includes an automated rebuild that regenerates the distribution formats, runs source QA, and validates the generated DOCX/PDF/EPUB files before committing new exports. A pull request must not be described as publication-ready until the generated files and validation have actually passed.

The separate `Master Speaking.docx` source has its **own** read-only manuscript audit and proof-publication pipeline in `tools/audit_master_speaking.py` and `tools/build_master_publication.py`. Grammar-book QA does not validate this original speaking manuscript, and successful conversion does not replace line-by-line language editing, image rights clearance, accessibility review, media verification or a physical print proof. See [scope and release gates](docs/repository-scope-and-release-gates.md).

## Evidence-led quality assessment (20 lenses)

A source-aware, reproducible [20-dimension audit](docs/quality-audit-20-dimensions.md) checks both book projects and distinguishes verified structural invariants from issues needing independent educational, editorial, accessibility, rights and print review. The [review protocol](docs/quality-protocol-20-dimensions.md) intentionally **does not assign perfect scores without evidence**.

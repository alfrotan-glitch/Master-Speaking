# Grammar for Special Speaking — TOEFL HOUSE

> **Learn the grammar. Use it in conversation. Make it part of your speech.**

A practical, independent grammar course for the Special Speaking classroom and self-study learners. The maintained lesson and assessment data in `build_spec/` generate the editable DOCX, print PDF, reflowable EPUB, and browser HTML for both the **Student Book** and the companion **Teacher's Book**.

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

The source QA (`build_spec/qa.py`) checks syllabus titles, all 16 lesson frameworks, narrative lesson openings, prose-first rule explanations, practice/answer-key counts, assessment order and scope, the final-assessment matrix, known grammar regressions, absence of proficiency-track labels or placeholder text, DOCX headings (H1/H2/H3), A4 layout, Lesson 1's approved structure (three core rule groups, 5+4 practice), Pair Speaking model exchanges vs Real Talk Challenge separation, and Teacher's Book alignment. The publication validator (`tools/validate_publication.py`) checks editable DOCX structure, searchable A4 PDF text, bookmarks, page flow (zero orphaned headings or sparse/blank pages), EPUB XML/package/navigation/local links, and required-section consistency across formats.

The DOCX files have native, updateable Word contents fields and live page-number fields; compatible Word processors are asked to refresh fields on open. If the contents has not refreshed, select it and choose **Update Field / Update entire table**. The EPUBs were checked with the project's XML/package/link validator and EbookLib's parser. **EPUBCheck was not available in this environment**, so no EPUBCheck result is claimed. Both PDFs were structurally checked and rendered to PNG for visual inspection across title pages, front matter, lessons, review tests, final assessments, appendices, and Teacher's Book guides.

## Book structure

- **Student Book front matter**: title page, copyright/publication page, student-facing introduction, unified eight-part lesson guide, contents, and baseline diagnostic test with a matched two-minute speaking task
- **16 lessons** in eight thematic Parts, teaching the whole class together through one shared learning journey and eight clear lesson steps:
  1. *Part 1 · The Speaking Hook*
  2. *Part 2 · The Simple Rule* (plain-English explanation + consolidated pattern, natural examples, and *Keep in mind* callout)
  3. *Part 3 · See the Difference* (side-by-side contrasts showing what the listener hears)
  4. *Part 4 · Practice the Pattern* (controlled completion and sentence transformation/repair)
  5. *Part 5 · Pair Speaking* (interactive task, 3-turn model exchange, conversation goal, and listener checklist)
  6. *Part 6 · Say It with Greater Precision* (whole-class progression from automatic core accuracy to added nuance, detail, and rhetorical focus)
  7. *Part 7 · Real Talk Challenge* (unscripted transfer speaking task with keyword planning, model response, and listening checklist)
  8. *Part 8 · Review and Self-Check* (numbered quick answers, active recall, and *Can I do this in real speech?* checklist)
- **Three cumulative review tests** (after Lessons 4, 8, and 12) strictly scoped to taught lessons
- **Final assessment**: 30 written items mapped across all 16 lessons, plus a matched speaking task, 4-criterion evaluation rubric, and personal error analysis plan
- **Five reference appendices**: Grammar Formula Book, Common Errors Guide, Essential Sentence Patterns, Speaking Self-Assessment & Can-Do Tracker, and Complete Answer Key
- **Teacher's Book**: front matter, course overview, eight teaching principles, 60-minute and 45-minute pacing and feedback routines, 16 lesson guides (objectives, observable criteria, preparation, 60-minute timing table, step-by-step procedures for Parts 1–8, concept checks, full Practice A & B keys with explanatory notes, sample partner exchanges, Real Talk models and assessment guidance, mixed-classroom scaffolding and stretch strategies, common misunderstandings, and feedback routines), plus full assessment keys and a model final speaking response

See [the assessment coverage matrix](docs/final-assessment-coverage.md) and [the editorial audit](docs/editorial-audit.md).

## Editorial and external-validation status

The Student Book and Teacher's Book were produced from shared, reproducible sources and checked with automated regression gates, structural publication validation, and a documented editorial audit. This is **not** a claim of independent expert approval, classroom testing, EPUBCheck certification, proven learning gains, or final print approval. Qualified teacher review and a real learner pilot remain pending; blank instruments are provided at [`docs/teacher-review-checklist.md`](docs/teacher-review-checklist.md) and [`docs/pilot-feedback-form.md`](docs/pilot-feedback-form.md).

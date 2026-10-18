# Master Speaking

English speaking course book by Abdul Raziq Nazari, with print, Word, and EPUB editions.

## Revised book — October 2026

**Start with [the clean book PDF](Master-Speaking.pdf)**: cover plus the reader-facing book, with navigation bookmarks. Discussion notes, production reports, and teaching packs are not included. The older `Master-Speaking-Reading-Edition.pdf` link remains an identical compatibility copy.

- [Editable Word book](Master-Speaking-7x10.docx)
- [Reflowable ebook with cover](Master-Speaking.epub)
- [Print interior, 7×10](Master-Speaking-print-7x10.pdf)
- [Front-cover concept](Master-Speaking-Front-Cover.pdf) — front only, not a printer cover wrap
- [Editorial and publication review](PUBLICATION-READINESS.md)
- [Final language and typography review](FINAL-EDITORIAL-REVIEW.md)
- [Whole-book critical audit and remediation](WHOLE-BOOK-AUDIT.md)
- [Modern redesign and visual review](DESIGN-REVIEW.md)
- [Current QA results](QA-REPORT.md) and [text change log](CHANGELOG.md)

This revision restores a previously truncated AI question, applies reviewed learner-facing copyedits, adds practical learning/research guidance without production commentary, improves default text contrast, and repairs chapter/table/title-page rendering. **It is an editorial proof, not a commercially cleared release.** Exact listening inputs, image permissions, factual substantiation, and final printer/device proofs remain open.

### Rebuild the revised book

```sh
bash book/tools/bootstrap.sh
python book/tools/release.py
```

The release command rebuilds the semantic book, cover, Word, PDF, EPUB, and reading edition, then runs 14 regression, lesson-structure, and production checks, including official EPUBCheck 5.3.0. `--skip-build` rechecks existing exports. The original manuscript is retained. Reviewed edits and added guidance live in `book/master/*.json`; do not edit generated exports expecting those edits to survive a rebuild. Use this release workflow rather than the historical `reports.py`, whose report templates predate the revision.

## Classroom implementation packs

The recommendations from the student/teacher review are now supported by two separate printable and editable packs:

- **[Student Practice Pack (PDF)](Master-Speaking-Student-Practice-Pack.pdf)** / [Word](Master-Speaking-Student-Practice-Pack.docx): chapter checklists for all eight units, eight model exchanges, eight short model responses, listening worksheets, and a practice record.
- **[Teacher Implementation Pack (PDF)](Master-Speaking-Teacher-Implementation-Pack.pdf)** / [Word](Master-Speaking-Teacher-Implementation-Pack.docx): eight newly authored teacher-read listening stories with their own questions and keys, the Unit 1 reading key, and four 75-minute pilot lessons.

**Start:** teach Unit 1 using the Teacher Pack’s pilot plan; give students the matching Student Pack pages. Keep teacher scripts and answers separate during listening. The pilot is intentionally slower than the companion’s two-meeting-per-unit course plan.

The teacher-read stories are fictional **alternatives**, not the original video transcripts, and no recorded audio is supplied. Use their own worksheets, not the book’s video questions. The original recordings remain unverified. The source-linked original-book reading key currently covers **Unit 1, Chapter 1 only**, not all eight units. No live pilot results are claimed.

```sh
python book/tools/classroom.py
python book/tools/qa_classroom.py
```

Authored sources: `book/classroom/modules.json`, `unit1-reading-key.json`, and `teacher-notes.md`. The two Markdown pack files are generated; edit the authored sources before rebuilding. See [CLASSROOM-QA-REPORT.md](CLASSROOM-QA-REPORT.md) and `book/publishing/listening-alternatives.csv` for scope and checks.

## Special Speaking Class companion

New supplementary materials for teachers and students, separate from the original manuscript:

- **[Printable class companion (PDF)](Master-Speaking-Class-Companion.pdf)** — A4, 17 pages, numbered sections start on fresh sheets.
- **[Editable class companion (Word)](Master-Speaking-Class-Companion.docx)** — adapt prompts, timings, and student sheets.
- [Editable source (Markdown)](book/companion/speaking-class.md).

Includes a 16-meeting course plan (75 minutes each), eight unit-aligned task sequences, role plays, useful language, intelligibility practice, mixed-level support, offline alternatives, student planning and feedback sheets, a final showcase, and a five-dimension classroom rubric. Intended approximately for B1–B2 learners; use the entry task to adapt to the actual class. It is not a standardized proficiency test.

Start with Sections 1–3, teach the matching unit in Sections 4–11, and copy the reusable sheets in Section 13. Section 14 contains assessment descriptors. Sensitive topics have neutral fictional alternatives; recording and internet access are optional.

### Rebuild and verify the companion

```sh
bash book/tools/bootstrap.sh
python book/tools/companion.py
python book/tools/qa_companion.py
```

Requires Python and the dependencies installed by the existing bootstrap. These commands only build the companion, not the original book. Edit the Markdown source rather than editing generated exports if you intend to rebuild. The exporter supports title/section headings, paragraphs, and bullet lists. Word may substitute fonts if Source Sans 3 is not installed; the PDF embeds its typefaces.

See [COMPANION-QA-REPORT.md](COMPANION-QA-REPORT.md) for verification and limitations.

## Manuscript and production files

- `Master Speaking.docx` — original manuscript.
- `Master-Speaking-7x10.docx` — formatted Word edition.
- `Master-Speaking-print-7x10.pdf` — print edition.
- `Master-Speaking.epub` — ebook edition.

Existing production scripts are under `book/tools/`; editorial and production reports remain in the repository root. The companion remains separate from the book. Current edition limitations are tracked in `UNRESOLVED-ISSUES.md` and `PUBLICATION-READINESS.md`; earlier production report snapshots are marked historical.

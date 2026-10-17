# Final Language, Typography & Design Review

17 October 2026 • Master Speaking

## Result

The current book is a **revised editorial proof**, with a 160-page print interior and a 161-page reading edition including the front cover. Ten automated regression/production checks pass. The separate 17-page classroom companion also passes its export checks. The original author-supplied manuscript has not been modified.

This is not a certification that the book is error-free, entirely human-written, or commercially cleared. The editing and production work is AI-assisted. Natural prose is an editorial goal, not proof of who wrote a passage; no AI-detector score or authorship guarantee is offered.

## Language and authorial voice

The title **Master Speaking** is retained. It describes the course without inventing a test qualification or an endorsement. The author-provided examples and thematic structure remain; the text has not been wholesale rewritten into a uniform promotional voice.

The reviewed-edit register now contains **42 exact-match changes** across chapter prose, vocabulary cells, and front matter, in addition to the earlier reconstruction repairs and the complete AI-question restoration. Every such change is guarded against source drift and logged.

Specific follow-up improvements:

- Removed the stray one-minute prediction direction in the relationships unit; it belonged to a different activity type.
- Changed remaining teacher-facing instructions into direct directions to the learner.
- Replaced “carefully selected” promotional filler with a practical instruction to use the expressions in discussion. Repeated lesson structure remains intentional, not a reason to vary instructions arbitrarily.
- Repaired the opening welcome line, parallel verb-led learning outcomes, a duplicated closing sentence, and missing final punctuation.
- Removed the misleading contrast implying IQ cannot change; retained practical advice for working on emotional skills.
- Qualified the claim that AI is faster and more accurate than people; performance is now explicitly task-dependent.
- Standardized ordinary vocabulary headwords to lowercase while retaining proper names, acronyms, and sentence capitalization.
- Renamed the Unit 8 quote-based vocabulary activity “Vocabulary in Discussion,” matching what students actually do.

These edits improve clarity and restraint. They do not establish that every research claim in the remaining readings has been independently verified. Exact listening inputs and research references remain publication tasks.

## Typography and design

| Element | Current treatment | Verification / limit |
|---|---|---|
| Main title | Master Speaking; coordinated cover/title-page typography | No invented qualification or bestseller claim |
| Main reading and question text | Source Serif 4, 11 pt; print leading approximately 15.6 pt | Larger than the preceding print proof; native Word output still needs comparison |
| Instructions | Source Sans 3, 10 pt, distinct from readings | Directions kept with following content where supported |
| Table text | 9.2 pt, left aligned, content-aware widths | Long headwords receive reserved width; not a large-print edition |
| Headings | Teal accents, consistent chapter hierarchy, pale section bands | Single chapter heading in Word/PDF; no duplicate fused label |
| Typefaces | Official static Adobe Source Sans 3 / Source Serif 4 files | Pinned source revisions, SHA-256 hashes, and OFL texts in `book/assets/fonts/` |
| Fallback glyphs | Existing DejaVu font path in PDF renderer | Distribution copyright/license notice retained alongside font records |
| Color | Dark teal on white, white on dark teal, dark ink on pale mint | Contrast ratios 6.86:1, 7.87:1, and 15.44:1 respectively; not whole-book accessibility certification |
| Student guide | Compact, parallel chapter overviews with visible bullets | Each short chapter overview kept together |
| Contents | One-page print contents; all eight units and 32 chapters | Page references checked against current pagination |
| Recto starts | Units begin on recto; deliberate blank versos may remain | Front blank no longer carries an inherited unit header |
| EPUB | Reflowable text with reader-font fallbacks and descriptive cover alt text | Font size and appearance depend on reading-system preferences; official EPUBCheck/device tests pending |
| Print cover | Original front-only typographic concept | Not a full printer-specified bleed/spine/back wrap |

The previous font subsets had inconsistent family metadata, including “ExtraLight” names for regular-weight files. They were replaced rather than cosmetically relabelled. The new files are sourced from pinned official Adobe repository revisions, with licenses and provenance retained.

## Verification evidence

- All ten gates in `QA-REPORT.md` pass: revision, source content, editorial mechanics, Word structure, cross-format fidelity, print, page proof, preflight, EPUB structure, and layout metrics.
- All **3,399 semantic text blocks** are traced into PDF, Word, and EPUB. The change from the preceding block count reflects removal of the stray prediction and duplicated guide sentence, not silent loss.
- All 160 pages were rendered in eight thumbnail overviews for a broad layout scan. Thirteen selected full-size page renders cover the title, guide, contents, first reading chapter in every unit, and final page. The current PDF checksum and image coverage are recorded in `book/qa/edition-review/index.json`.
- The overview scan checks broad layout balance, missing content regions, and obvious placement anomalies. It is not a line-by-line reading of every page. Selected full-size pages were inspected during the revision.
- Content/editorial/print QA scripts now return a failing process status when they find issues. Page-proof checks use the detected main-text start, not the previous hard-coded page 11. Word heading checks distinguish the four front-guide headings from instructional section headings.
- `git diff --check` passes for textual changes. Publication exports are declared binary in `.gitattributes`.

## What still needs an independent sign-off

Before calling the book commercially ready, obtain exact recordings and check their exercises, substantiate remaining research claims, clear existing image/quotation rights, confirm publishing metadata, run native Word and ebook/device tests, and approve a physical printer proof. A qualified human English-language editor should also review the complete final manuscript and confirm the intended voice, audience, and exercise answerability.

See `PUBLICATION-READINESS.md`, `UNRESOLVED-ISSUES.md`, and the publishing registers for those concrete tasks. The aim is a dependable teaching book, not an unsupported promise that “everything is perfect.”

## Subsequent reader-facing cleanup

The book’s discussion/revision commentary has been removed at the author’s request. Reader guidance remains as ordinary book prose; production history and unresolved requirements stay in external reports. Two further exact-match edits remove a teacher-facing aside and revise an indirect instruction. Current counts and checks supersede the snapshot above: see QA-REPORT.md and `book/artifacts/qa_publication.json`. The clean reader file is `Master-Speaking.pdf`.

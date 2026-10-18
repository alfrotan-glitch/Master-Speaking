# Master Speaking — Editorial & Publication Review

October 17, 2026 • Revised classroom edition in development

## Edition status

**Improved editorial/design proof, not yet cleared for commercial publication.** The new reading PDF is suitable for reviewing the revised book. Automated production checks pass, but they do not substitute for rights clearance, media verification, factual review, classroom trials, or a physical printer proof.

Author and existing publisher attribution remain Abdul Raziq Nazari / The TOEFL House. No ISBN, accreditation, endorsement, or proficiency certification has been invented. The original `Master Speaking.docx` is unchanged.

## What changed in this revision

### Editing and teaching

- Restored the **entire Unit 5 AI decision-making question** from manuscript item 1582. The previous reconstruction accidentally stopped after “climate change,” removing “disease, and poverty” and the actual decision-making question. Only the missing initial I is repaired in the restored source text.
- Applied 130 exact-match reviewed edits across chapter text, vocabulary cells, and front matter. These clarify learner-facing instructions, fix “their choice” to “your choice,” remove a reference to nonexistent bold words, and align Unit 6’s pronunciation heading with its actual regular past-tense lesson.
- Retained three plain learner-guidance paragraphs: a speaking/repetition routine, privacy and sensitive-topic choices, and research-source attribution. Production and media-verification notes remain only in separate reports.
- Kept the author’s readings, eight themes, and 32-chapter sequence. No third-party transcript, exercise answer, research finding, or missing vocabulary item was fabricated.
- Retained the separate 17-page Class Companion with lesson plans, assessment, role plays, and student practice tools. Its approximate B1–B2 planning range is not a certified level for the main book; the manuscript itself includes more demanding material. Diagnose the actual class before choosing pace and support.

### Design and production

- Created an original front-cover concept using vector typography and paired speech shapes. Teal, warm ivory, and mint connect the cover to the interior without introducing stock imagery.
- Replaced bright-green text/banner defaults with a shared dark-teal palette. Default text contrast ratios: accent/white 6.86:1, white/banner 7.87:1, ink/pale band 15.44:1. This is not a claim of whole-book accessibility compliance.
- Fixed a duplicated chapter heading in the Word/PDF rendering path: one navigable heading now appears per chapter, not an extra fused “Chapter1Speaking…” line beneath it.
- Fixed table grid/cell width disagreement. Column widths now reserve space for complete words and distribute remaining space by content. Table text is smaller, left-aligned, and header rows repeat when PDF tables continue across pages.
- Connected instructions to the following content to reduce stranded directions at page bottoms.
- Fixed title-page placement by respecting Word’s display-style inset and spacing in the custom PDF renderer.
- Added a cover image to the EPUB manifest and spine, with descriptive alt text and a navigation entry.
- Built a bookmarked **reading edition** combining the front cover with the interior. The separate 7×10 interior remains available for production review.

## Files and intended uses

| File | Use |
|---|---|
| `Master-Speaking-Reading-Edition.pdf` | Main review/read-through copy: front cover plus revised interior, with bookmarks |
| `Master-Speaking-print-7x10.pdf` | Revised interior only; 7×10 trim, no bleed; printer review required |
| `Master-Speaking-7x10.docx` | Editable formatted Word edition; refresh TOC in Word before native export |
| `Master-Speaking.epub` | Reflowable ebook with new cover; passes official EPUBCheck 5.3.0; device/accessibility tests pending |
| `Master-Speaking-Front-Cover.pdf` | Front-cover concept only, not a complete print cover wrap |
| `Master-Speaking-Class-Companion.pdf` / `.docx` | Separate teacher/student support pack |
| `book/publishing/media-register.csv` | Eight listening lessons awaiting exact source identification and alignment checks |
| `book/publishing/asset-rights-register.csv` | Existing image inventory and rights evidence still needed |

## Classroom implementation follow-up

Two separate 18-page packs now support the student/teacher recommendations. The Student Practice Pack supplies checklists and speaking models for all eight units, with matching alternative-listening worksheets. The Teacher Implementation Pack supplies eight original fictional teacher-read scripts and keys, the 15-item Unit 1 reading key, and four 75-minute pilot plans. These are new supplementary materials, not recovered original videos, a complete eight-unit book key, recorded audio, or evidence of an actual pilot. See `CLASSROOM-QA-REPORT.md` for verified scope and `README.md` for use/build instructions.

## Required before commercial release

1. **Confirm listening inputs.** For every Chapter 2, obtain the intended recording, exact title, creator, stable link, access conditions, and permission basis. Check each comprehension question against the actual recording. Unit 2’s displayed topic and pre-listening title differ; do not guess the intended video. Broad “TED-Ed lesson” references are not proof of source identity or licensing. Do not invent scripts or answer keys.
2. **Review rights and attribution.** Existing manuscript images have not been cleared by this revision. Complete the asset register with source, creator, license, and evidence; replace or remove unlicensed material with author approval. Confirm quotation attribution and retain the bundled font licenses and provenance records. Owning the manuscript file is not evidence of permission for every embedded asset.
3. **Complete subject/factual review.** Check claims about psychology, relationships, money, globalization, and technology against identified sources. Existing readings contain generalized research claims; this pass did not substantiate them. Add precise references or qualify unsupported assertions with author approval. Recheck technology-related passages close to publication.
4. **Supply missing source content or approve its treatment.** The source does not supply a Video Scripts section. Obtain exact recordings and any needed transcript permissions before adding scripts. The earlier allegation about missing Unit 5 Chapter 3 vocabulary-activation items was not substantiated: the current/source task uses the ten supplied expressions; no replacement items are needed for that task.
5. **Proof every final page.** Run a full human review after content approval: question numbering, table continuation, answer space, language accuracy, cross-references, and images. Automated checks are necessary but cannot establish readability or exercise validity. Selected page inspection has been performed, not a signed full proof.
6. **Test access and devices.** Keep the official EPUBCheck gate passing; test common ebook readers, text resizing, dark mode, keyboard navigation, and screen-reader order. Audit whether generic existing image descriptions sufficiently convey instructional meaning. PDF accessibility tagging has not been established.
7. **Prepare the actual print cover.** Confirm binding, final page count, stock/caliper, spine width, bleed, color requirements, and barcode placement with the chosen printer. Produce a full front/spine/back wrap only after these are fixed. The front-cover concept has no bleed and is not that wrap.
8. **Check print assets and native Word.** Two existing image placements are approximately 122 and 143 dpi; obtain originals if the printer requires higher resolution. Install the intended fonts, refresh Word fields, export natively, and compare with the custom-rendered proof. Approve a physical bound proof.
9. **Finalize publishing metadata.** Confirm imprint authority, edition statement, publication date, distribution territories, price, ISBN ownership if applicable, and any required trademark/disclaimer language. The existing copyright page attribution is carried from the earlier project; it has not been independently verified here.
10. **Pilot the course.** Use representative learners to test difficulty, timings, cultural suitability, sensitive-topic alternatives, and assessment consistency. Collect consent-based feedback before describing the book as classroom-validated.

## Reproducible workflow

```sh
bash book/tools/bootstrap.sh
python book/tools/release.py
python book/tools/companion.py
python book/tools/qa_companion.py
```

`release.py` stops if a build stage fails, records each QA process’s exit status, writes fresh checksums and QA results, and returns failure if a QA gate fails. To check existing outputs without rebuilding, use `python book/tools/release.py --skip-build`.

Editorial source chain: original DOCX → existing extracted dump → `parse.py` plus the guarded editorial, structural-repair, learner-review, and exact-title JSON registers → semantic XHTML → formatted DOCX → custom-rendered print PDF. EPUB is generated from semantic XHTML. `cover.py` generates the front concept and ebook image. Editing generated Word/XHTML files without updating the source chain will be overwritten by a rebuild. See `CHANGELOG.md` for all logged text changes and `QA-REPORT.md` for current results.

## Final natural-language and typography sweep

The follow-up pass preserves the supplied authorial voice rather than rewriting every paragraph into a uniform style. It removes teacher-facing leftovers, repairs parallel learning outcomes, softens an unqualified AI-performance claim, removes the misleading “unlike IQ” comparison, and uses lowercase for ordinary vocabulary headwords. Repeated teaching routines remain deliberately consistent. The book title remains **Master Speaking**; it is clear, accurate to the course, and does not imply test certification.

The main reading and question text is now 11 pt, with approximately 15.6 pt leading in the print renderer. Instructions are 10 pt; table text remains 9.2 pt to preserve usable column widths. Official Source Serif 4 and Source Sans 3 static font files replace the earlier inconsistently named subsets. Their revision IDs, hashes, and licenses are retained in `book/assets/fonts/`. The remaining commercial-release rights questions concern existing third-party manuscript content and attribution, not a missing license record for these newly sourced Adobe fonts.

The student-guide chapter summaries stay together, the contents fits on one page, and a blank front-matter verso no longer inherits a stale unit header. The QA tools now derive the main-text start from current pagination, and content/editorial/print tools return a failure exit status when issues are detected. This fixes verification weaknesses rather than changing tolerances to hide defects.

See `FINAL-EDITORIAL-REVIEW.md` for the final scope and limitations.

## Reader-facing publication cleanup

At the author’s request, the book itself no longer includes discussion/revision notices, media-verification status, or references to the separately developed teaching packs. Three ordinary learning-guidance paragraphs remain, without a production-history preface. The media/source limitations are still recorded here and in UNRESOLVED-ISSUES.md; removing their discussion from the reading text does not resolve them.

The main reader file is now `Master-Speaking.pdf`, with the title metadata **Master Speaking**. The former reading-edition filename is an identical compatibility copy. Word’s visible TOC cache now contains the actual eight unit and 32 chapter labels instead of an “Update Field” instruction; native Word may refresh the field to supply its own pagination. No tracked review markup or default generator comment is retained in the formatted Word book.

`qa_publication.py` checks the semantic book, Word, EPUB, PDF text, and PDF metadata for 19 known production/chat phrases. It passes with no findings. This additional content-boundary check is included in the release workflow, forming one of the current fourteen checks. It is not commercial-release certification.

## Chapter titles and pagination follow-up

All 32 chapter headings now follow the exact existing manuscript/lesson wording, with source selectors recorded in `book/master/chapter-titles.json`. Twenty-three headings use an existing principal reading, listening, discussion, or research title; nine retain the original learning-strand chapter heading because no single principal content title is supplied. Existing repeated titles are preserved rather than replaced with invented alternatives. Learning-strand subtitles appear only when they differ from the heading. Chapter numbering still runs 1–4 within each unit to preserve classroom references. Contents entries, Word headings, PDF bookmarks, and EPUB navigation use the same titles. The copied marriage-topic heading in Unit 8’s English discussion has been corrected to “English and Academic Opportunity.”

Every chapter opens on a fresh page in the generated PDF; Word stores an explicit page-break-before property on each chapter heading, with the title and learning-focus subtitle kept together. Native Word pagination still requires a Word proof. Unit openers continue to start on right-hand pages. The interior title page has no visible folio; the front matter uses lowercase Roman numerals and main text uses continuous Arabic numbering. PDF viewer page labels match these sequences, including the separate cover offset. EPUB reading order now places each unit opener before its four chapters, with chapter-level page-break styling for paginated readers; reflowable ebooks do not have fixed print page counts.

A dedicated chapter QA check verifies all 32 names, Word page-break/subtitle properties, actual PDF chapter starts, all chapter contents folios and links, bookmark destinations, reader-edition offsets, and EPUB spine/navigation order. The full release now runs 14 QA checks, including official EPUBCheck 5.3.0. Reports and production notes remain outside the reader-facing book.

## Strict-audit remediation

The Unit 3 pronunciation contrast now distinguishes flat delivery from key-word stress using explicit capitalized targets and matching instructions. The rising-intonation examples now have a tentative/curious context and acknowledge the common falling pattern of wh-questions. Case-sensitive regression checks verify that the contrast survives in semantic XHTML, Word, PDF, and EPUB. Broader specialist review remains open.

The export-fidelity gate now requires complete normalized blocks, with a complete-block whitespace fallback for PDF wrapping and minimum occurrence counts in all three formats. Regression probes reject prefix-only and missing-middle text. Normalization still cannot certify punctuation, every pronunciation symbol, typography, semantic order, or educational validity; these are separate proof responsibilities.

Official EPUBCheck 5.3.0 identified RSC-011: the contents landmark targeted a document outside the spine. The contents is now a visible, styled nonlinear spine resource, accessible on demand without interrupting the chapter sequence. Official validation passes with zero errors and zero warnings. The validator, export SHA-256, and full engine results are recorded in `book/artifacts/epubcheck-official.json`; the release gate fails if the validator is unavailable. This is EPUB format validation, not accessibility or device certification.

`UNRESOLVED-ISSUES.md` is the current release-condition register. `STRICT-AUDIT.md` retains the original audited fingerprints and findings, with a dated remediation update; it is not a claim that the new export has no problems.

The stress comparison is kept together as one short teaching unit in Word/PDF, with break-inside protection in EPUB. Its four subsequent read-aloud practice sentences now form a single 1–4 sequence instead of two lists restarting at 1. Regression checks cover both the same-page comparison and the four-item sequence.

## Exact-title correction requested by the author

The earlier 32 editorial aliases have been removed from the publication. Chapter openings, contents entries, Word headings, PDF bookmarks, and EPUB navigation now use exact existing lesson titles or the original chapter heading—not newly coined names. The original content headings remain in place beside their actual reading/listening/research material. Examples: “The Power of Communication,” “Are You a Good Listener?,” “Living with AI: Friend or Foe?,” and “The Science of a Lasting Relationship.”

Source fidelity takes precedence over artificial title uniqueness. A chapter containing multiple debate/research choices is not renamed after just one optional task. Where no single principal title exists, its original chapter heading is retained, with no redundant repeated subtitle. Build-time guards and chapter QA reject titles without the recorded source match. Distinct chapter identifiers and unit context keep repeated author-supplied titles unambiguous.

## Whole-book critical audit and lesson review

The current pass adds 80 guarded text/table corrections beyond the previous 50-edit baseline (130 chapter/front-matter edits in total), 24 guarded structural repairs, and eight authored learner-review/transfer routines. It fixes misplaced vocabulary items, task-type errors, incomplete or duplicate instructions, a copied research topic, incomplete conclusions, and pronunciation problems. All original chapter-title wording remains source-backed; no editorial aliases were reintroduced.

Five of the ten Unit 4 word-stress models were incorrect. All ten primary-stress positions were cross-checked against the CMU Pronouncing Dictionary at pinned revision `74790861f652b15e4ac49015a90074ad62a27690`. The five incorrect models and both table columns were corrected. The ten selected source entries, scope and source hash are in `book/publishing/pronunciation-reference.json`; the license is `book/assets/cmudict-LICENSE.txt`. This is not verification of every IPA transcription or every accent in the course.

`qa_lessons.py` checks all 32 chapters, 88 multiple-choice groups for task grouping/option labels, seven vocabulary exercises containing 36 source items, all eight reading title/passage openings, the ten stress models, exact exported stress capitals and selected IPA examples, and eight unit-specific review tasks. It does not verify all answers, research claims, recordings, accessibility, or classroom effectiveness. The full release has 14 gates. Current pagination and export fingerprints are in `QA-REPORT.md`; do not reuse earlier 160/161-page counts.

See `WHOLE-BOOK-AUDIT.md` for the unit-by-unit findings and remaining release conditions. Authoritative evidence—not another positive checklist—is still required to close original recording alignment, rights, independent factual/pedagogical review, native Word proof, accessibility/device testing, and physical print approval.

# Master Speaking — Original-manuscript course edition

## What this edition is

This is a separate, source-faithful production edition of **Master Speaking.docx**, not a revision of the accepted self-contained edition. The original manuscript and the previously accepted PDF, Word, EPUB and semantic masters remain unchanged. The original course text takes priority over replacement stories or rewritten readings.

The book uses the approved edition's green visual identity, Source Serif/Source Sans typography, 7 × 10 inch page design, styled tables, running heads, linked contents and navigation. Every chapter opens on its own page. Unit openers begin on recto pages.

### Files

| File | Purpose |
|---|---|
| `Master-Speaking-Standard.pdf` | 162-page reader PDF, including front cover |
| `Master-Speaking-Standard-print-7x10.pdf` | 161-page interior, without cover |
| `Master-Speaking-Standard-7x10.docx` | Editable Word edition |
| `Master-Speaking-Standard.epub` | Reflowable EPUB with its own edition identifier |
| `Master-Speaking-Standard-Front-Cover.pdf` | Separate front panel |
| `Master-Speaking-Standard-Back-Cover.pdf` | Separate back panel with video-dependent course description |
| `Master-Speaking-Standard-Edition.zip` | These six files plus this review and the reading guide |

The cover panels are **not** a printer-imposed wrap. Spine width, bleed, stock, binding and printer approval are still required.

## Manuscript preservation

- All eight original reading passages are retained: **75 reading paragraphs**, checked against the source in their original order. The missing final full stop in Unit 1 is repaired; readings have not been shortened or replaced.
- All eight original video-based listening lessons and their exercises are retained. No fictional replacement listening scripts are inserted.
- The original lesson sequence, discussions, research tasks, vocabulary tables and pronunciation material are retained, subject to the recorded copyediting and structural repairs below.
- The 32 chapter titles use the same exact, source-backed title plan as the approved design. Original learning strands remain as subtitles; legitimate repeated titles remain.
- All 24 source illustrations are retained. Their staged source files match the manuscript's embedded image bytes. The GIF has a derived PNG for formats that require it; its original is retained in the source assets. No stock-image replacement or new diagram silently substitutes for content-bearing artwork.
- The full Unit 5 opener title, including “Artificial Intelligence,” is retained.

The source ledger covers **3,203 nonempty original paragraphs/table cells**. Normalized presence is checked within the original unit/chapter, with **83 explicitly explained differences**, chiefly regenerated contents, heading presentation, duplicate-text cleanup and copyedits. There are **zero unexplained differences**. This is a scoped normalized-content audit, not a claim that every character is unchanged or that an independent editor has approved every sentence.

### Recorded changes, not wholesale rewriting

`book/standard/copyedits.json` contains seven exact-match, source-indexed edits: a final full stop; a missing article; the missing initial letters in “Education” and “Imagine”; the inappropriate true/false direction before eight open questions; “your choice” in a direct instruction; and initial capitalization in a schwa instruction.

The reconstruction log also records six “Chooses 10” → “Choose 10” imperative repairs, splitting jammed options/items, repairing activity numbering, restoring a missing Student A label, numbering the two existing Unit 6 speaking challenges, and formatting existing topic/clinic labels as headings rather than numbered questions. Repeated Before You Read blocks are collapsed without removing distinct questions; merged vocabulary items are retained. Whitespace, apostrophes and list presentation are normalized.

The repeated Unit 4 title inside Unit 6's before-listening section is aligned with the original Unit 6 lesson title. This is an **internal consistency repair**, not verification of the recording's identity.

A localized 3 pt question-spacing override in Unit 7 Chapter 1 prevents its final homework direction from occupying an otherwise empty page. No font size, line spacing or course text is reduced.

## Checks completed

The separate original-manuscript build passed eight production checks: Word structure, cross-format text coverage, print geometry, automated page proof, EPUB structure, official EPUBCheck, chapter/contents/navigation checks, and spread metrics. The independent edition-identity/freshness check also passes.

- **3,422 master text blocks** found in each of PDF, Word and EPUB; zero missing blocks.
- **161 interior pages**, zero reported automated print/proof issues and zero spread-metric flags.
- **32/32 chapter openings** checked against the title plan, contents and navigation.
- Official **EPUBCheck 5.3.0: zero errors and zero warnings**.
- All six delivered file hashes, the semantic master, source manuscript and protected prior-edition hashes are recorded.

### Visual review scope

All interior pages were examined as overview contact sheets during production; selected full-size pages were inspected, including the eight listening openings, the Unit 7 homework repair and the Unit 8 schwa page. Both cover panels and a contact sheet of the 24 original illustrations were inspected. Corrected full-size pages were rechecked during iteration. Candidate generation alone is not counted as inspection; the exact scope and hashes are in `book/standard/qa/reviewed.json`.

This is **not** a complete independent, every-word/full-size proof of all pages. Native Microsoft Word pagination, physical print proofs, learner/teacher pilot approval, assistive-technology testing and EPUB-device testing remain outstanding. The PDF is not a tagged-accessibility publication. EPUB descriptions and navigation do not constitute accessibility conformance certification; the supplied goal-setting mind map lacks a complete text transcription.

## Items requiring course-owner/publisher decisions

1. **Recordings:** the source document contains no external hyperlink relationships identifying the videos. Confirm exact titles, speakers, URLs, versions, availability, captions/transcripts, classroom-use conditions and exercise-to-recording alignment before teaching the listening lessons. None has been externally verified in this work.
2. **Title/thumbnail alignment:** Unit 2's original prediction section/thumbnail says “Why You Should Stop Setting Goals (Yes, Really)” while the lesson heading is “The Art of Goal Setting.” Unit 3's thumbnail says “Are You Emotionally Mature?” while its lesson title is “The Power of Emotional Intelligence.” Unit 5's thumbnail says “Things Are Going to Get Weird.” These source differences are retained, not invented away. Generic “TED-Ed lesson” directions also require checking against the actual recordings, since several source stills show TED-style stages rather than TED-Ed animation.
3. **Artwork/quotation permissions:** preserving a supplied image or quotation does not establish permission to publish it. Clear all source photographs, video stills, marks, the goal-setting mind map and the attributed epigraph; do not infer endorsement. Full artwork provenance is recorded separately.
4. **Image quality:** the original Unit 2 opener and reading illustration place at approximately **122 dpi and 143 dpi**, below the 150 dpi advisory threshold. The SMART mind map is especially small-text artwork. Obtain lawful higher-resolution originals and a complete text equivalent; upsampling cannot recover missing detail.
5. **Original factual/pedagogical claims:** retained passages include unsourced research assertions, the Unit 3 contrast “Unlike IQ” about development, and general claims about goals, money and happiness. These require a factual/reference review rather than an unsupported certification. The Unit 6 clinic's “Skill: Linking Sounds” label precedes material on -ed endings; confirm the intended label. Mixed-dialect IPA and all pronunciation instruction need specialist review. These are not represented as fully validated.
6. **Teacher materials:** the earlier edition's fictional-listening scripts, related answers and teacher-book page references are not validated keys for this standard edition. No new video answer keys are fabricated. The standard-edition ZIP intentionally does not include those other-edition supplements.

**Status:** manuscript-based production/review edition. Not cleared for unrestricted commercial printing or sale. A controlled teacher-led pilot should use only prepared and lawfully available materials; unresolved video lessons must be prepared or deferred, not improvised from unverified answer keys.

## Reproduce and inspect

```sh
bash book/tools/bootstrap.sh
python book/tools/standard_edition.py
python book/tools/qa_standard.py
python book/tools/review_standard.py
```

The build uses ignored `book/standard/work/` staging and never invokes the replacement edition's full parser build. It reconstructs from a fresh extraction of the original Word manuscript, applies guarded copyedits, generates separate exports and validates protected files. `review_standard.py` produces candidates only; re-inspection is needed after a changed build. A new export hash invalidates earlier visual-review evidence until reviewed again.

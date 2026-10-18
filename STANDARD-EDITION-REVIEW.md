# Master Speaking — Original-manuscript Standard review proof

> **Status: review proof; not approved for publication or public release.** A passing build is not author, publisher, legal, accessibility, printer, or course-owner approval.

This separate edition reconstructs the original `Master Speaking.docx` with guarded copyedits and limited structural/layout repairs. It preserves the 32 source-backed chapter titles, original readings, video-based listening lessons, and exercises. It is not the accepted self-contained edition.

## Scope decisions

The requester chose print PDF + EPUB, stated they hold or represent manuscript rights, directed that uncleared third-party material be removed or replaced, and said course-owner confirmations can be supplied. These are authorization and workflow decisions, not independent proof of ownership, third-party clearance, video intent, or publication metadata. The source DOCX and unprefixed accepted-edition files remain unchanged.

The Standard export excludes the attributed epigraph pending primary-source verification/permission. It replaces all **24 canonical source illustrations** with original geometric artwork generated in `book/tools/standard_artwork.py` from generic shapes and course-owned labels. Text uses the bundled Source Sans 3 fonts under the SIL Open Font License (`book/assets/fonts/source-sans-LICENSE.md`); no supplied image, video still, logo, or speaker likeness is used by that renderer. A further WDP image-layer object in the source package is separately inventoried and excluded. Original source media remains only in the protected source DOCX; an old QA contact sheet containing that source imagery was removed. The 35-row `book/standard/publication-clearance.csv` records progress and open evidence requirements; it is not a clearance certificate.

The eight listening lessons remain external and unembedded. The replacement resource cards are generic and make course-owner confirmation explicit. Independently located official video candidates and evidence are in `book/standard/video-dependencies.json`; candidate matching is not owner confirmation or permission.

## Current files

- `Master-Speaking-Standard.pdf` — 163 pages including the front cover.
- `Master-Speaking-Standard-print-7x10.pdf` — 162-page 7 × 10 inch print interior, without a cover.
- `Master-Speaking-Standard.epub` — reflowable EPUB, 47 spine items.
- `Master-Speaking-Standard-7x10.docx` — editable Word proof.
- `Master-Speaking-Standard-Front-Cover.pdf` and `Master-Speaking-Standard-Back-Cover.pdf` — separate cover panels, not an imposed wrap.

The reader PDF and panels identify the review-only status. Printer trim, bleed, spine, stock, binding, imposition, and physical proof remain outstanding.

## Editorial and source audit

The Standard model has **105 exact-source-block copyedits** (including eight removals), **13 structural edits**, and two layout overrides. These are recorded in `book/standard/copyedits.json`, `structural-edits.json`, and `layout-overrides.json`. They address confirmed copy errors, repeated material, directions, a Unit 1 listening stem, sensitive participation language, selected research claims, and limited pagination issues; they are not a wholesale rewrite. Chapter titles were preserved. The Unit 5 connected-speech prompts are not represented as phonetic spellings; the Unit 6 *-ed* explanation/stress examples were corrected, while remaining dialect-specific IPA still requires specialist review.

The source ledger covers **3,203 nonempty source paragraphs/table cells**. It records **184 normalized differences** with explicit dispositions and zero unexplained differences. All **75 original reading paragraphs** remain in source order. This method is not a character-for-character facsimile or independent every-word proof. Eight selected references support a limited set of qualified claims; they do not validate every factual assertion or establish publication rights.

## Build, package, and visual checks

Latest build evidence in `book/standard/production-checks.json`:

- **3,422 master text blocks** checked in PDF, DOCX, and EPUB; zero missing in each.
- 162 print-interior pages; unit starts at physical pages 9, 25, 43, 61, 81, 101, 121, and 141.
- 24 image placements; effective print resolution 327–444 dpi; no automated print issues.
- Eight production checks pass: Word structure; cross-format coverage; print geometry; automated page proof; EPUB structure; official EPUBCheck 5.3.0 (zero errors and warnings); 32 chapter/title/navigation checks; and 77 spread metrics with zero flags.
- `book/tools/qa_standard.py` passes the separate freshness, identity, protected-input, source-image exclusion, and epigraph-removal checks.
- Six overview contact sheets cover all 162 physical interior pages. All 24 replacement illustrations were visually checked in a contact sheet, and selected full-size pages plus both cover panels and the rights notice were inspected. The SMART labels are readable. Generic listening cards do not identify a recording and state that owner confirmation is required.

The inspection record is `book/standard/qa/reviewed.json`; generated files listed in `candidates.json` are candidates, not proof that someone inspected them. The scope does not amount to an every-word/full-size proof, native Word pagination proof, EPUB device test, tagged-PDF/accessibility certification, assistive-technology test, physical printer proof, or independent legal/editorial sign-off. A selected reference appendix and passing EPUBCheck are not accessibility or legal certification.

## Open release conditions

1. **Videos:** Obtain owner confirmation of exact recording/version, playback, exercise alignment, availability, permissions, and caption/transcript plan for each unit. Unit 1's exercise content matches a TED-Ed candidate but its old still appears to show a different School of Life video. Unit 3's exercise content matches a TED-Ed candidate, but its old still identity remains unresolved. Units 2 and 4–8 have transcript-content candidates only. None is confirmed by the course owner. Do not use the prior-edition media register as evidence for this Standard edition.
2. **Rights and attribution:** The requester says they hold or represent manuscript rights, but no supporting authority record or final rights statement has been supplied. Independently confirm author/publisher/imprint metadata and clear remaining text/quotation/mark/media uses, video licenses, transcripts/captions, references, and replacement-artwork use. Excluding the original images and epigraph does not clear the rest of the manuscript.
3. **Metadata and printer:** Obtain final author/publisher/copyright line and required market metadata (for example ISBN/price/legal deposit if applicable), printer specifications, and a physical proof. The covers are separate 7 × 10 panels only.
4. **Access:** PDF files are not tagged-accessible PDFs and have no certification. EPUB structure/image descriptions and EPUBCheck do not establish conformance. Test on actual devices and with assistive technology; review reading order and replacement-image descriptions.
5. **Pronunciation/teaching:** Commission specialist review of remaining IPA and model accent. Keep personal/relationship prompts optional and allow general or fictional answers. No learner level, dialect, first language, classroom pilot, suitability, or learning-effect claim has been established.

Do not publish, distribute, or describe this candidate as release-ready until the appropriate owners/reviewers complete and document these conditions.

## Reproduction

```sh
bash book/tools/bootstrap.sh
python3 book/tools/standard_edition.py --source-only
python3 book/tools/standard_edition.py
python3 book/tools/qa_standard.py
python3 book/tools/review_standard.py
```

The Standard builder stages the original manuscript and shared renderers under ignored `book/standard/work/`, then makes only the prefixed Standard files. It does not rebuild the accepted self-contained edition. `review_standard.py` renders current proof candidates; after actual inspection, update `book/standard/qa/reviewed.json` and rerun the freshness check as appropriate.

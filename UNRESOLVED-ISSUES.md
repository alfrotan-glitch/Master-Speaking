# Current release-condition register — Master Speaking

Updated 17 October 2026 after strict-audit remediation. This register supersedes conflicting historical statements in earlier reports. **Commercial release remains on hold.** Production validation is not rights clearance, factual approval, or classroom validation.

## Open conditions

| ID | Priority / scope | Evidence and closure condition | Responsible review |
|---|---|---|---|
| R01 | Blocking — original listening lessons | All eight entries in `book/publishing/media-register.csv` remain UNVERIFIED. Identify exact recordings, creators, stable links, access and permission basis; verify every vocabulary/comprehension item against the recording. Unit 2's two media labels need reconciliation against the actual source, not a guessed rename. | Author and media editor |
| R02 | Blocking — existing image rights | 24 existing manuscript assets are UNVERIFIED in the asset-rights register. Supply provenance/permission evidence and attribution, or approve replacements/removals. Missing evidence is not proof of infringement. Official font licenses do not clear images. | Author/publisher and rights reviewer |
| R03 | High — claims and language/pedagogy | Verify research assertions in readings, quotations, pronunciation models, instructional answerability and language accuracy. Add source-specific references or approve carefully qualified wording. The repaired Unit 3 rule is not a whole-book specialist sign-off. | Subject, language and pronunciation reviewers |
| R04 | High — native Word pagination | Word has explicit chapter breaks and correct cached contents labels, but the cached TOC lacks page numbers. Install intended fonts, refresh fields in native Word, save/export and compare final folios, page starts and tables. Do not populate native Word with unverified PDF page numbers. | Word production editor |
| R05 | High — accessibility/device testing | Reader PDF lacks structural tagging. EPUB passes official EPUBCheck but device, resizing, dark-mode, keyboard, screen-reader and instructional alt-text testing remain outstanding. Supply appropriate tagged PDF and accessible-reader proof before making compliance claims. | Accessibility specialist and production editor |
| R06 | High — print approval | Interior image placements at 122.4 and 142.9 effective dpi require better originals, viable smaller placements, or printer approval. Front cover is a concept, not a wrap. Confirm stock, binding, bleed, spine, color and barcode requirements; approve a physical proof. | Publisher/printer |
| R07 | High — final proof and classroom pilot | No signed complete page/exercise proof or representative learner pilot. Test level, timings, cultural suitability, sensitive-topic alternatives, answerability and assessment consistency. Separate support packs/pilot plans are not completed trials. | Lead editor and pilot teachers |
| R08 | Publishing metadata | Confirm imprint authority, publication/edition details, distribution territories, quotation attribution and ISBN ownership if applicable. None is certified by retaining manuscript attribution. | Author/publisher |

## Resolved or corrected in the current revision

- All 32 chapter headings use exact existing content titles or original chapter headings, with no invented aliases or redundant identical subtitles, and have separate PDF opening pages; unit openers remain recto. Chapter contents folios/links, bookmarks, reader offsets and EPUB unit-before-chapter order are checked.
- The complete Unit 5 AI decision-making prompt is restored from source. Unit 6's pronunciation heading matches regular past-tense endings. Unit 8's copied marriage heading now matches its English/academic-opportunity questions.
- Unit 3's formerly identical pronunciation examples now visibly contrast flat delivery with capitalized stress targets. The broad rising-question rule now gives context and acknowledges common falling wh-question intonation. All-format, case-sensitive regression checks protect the contrast.
- Export fidelity now requires full normalized blocks and minimum occurrence counts; deliberate prefix-only and missing-middle regression cases fail. This is not universal semantic or typographic verification.
- Official EPUBCheck 5.3.0 found and helped repair RSC-011 in the contents landmark. Validation now passes with zero errors and warnings; it is a mandatory release gate, not a skipped optional test.
- Reader-facing publication files contain ordinary learner material, not discussion/revision commentary. Verification limitations remain in separate reports.
- Current guide: three learner-guidance paragraphs. Current exact-match chapter/front-matter edit count is reported by `qa_revision.py`; do not reuse older fixed counts.

## Closed allegation / scope clarification

- **Missing Unit 5 vocabulary-activation items:** not substantiated for Chapter 3. Its toolbox has ten expressions and its source-backed task asks learners to use all ten in a conversation. No replacement questions should be invented for that task. Reopen only with an exact different location and evidence.
- **Video Scripts section:** not supplied by the original source. This is a dependency if transcripts are to be published, not proof that a promised section was dropped from this edition. Obtain recording identity and any required transcript permission before adding scripts. Do not fabricate source transcripts.
- **Supplementary listening:** separate student/teacher packs contain eight original teacher-read alternatives and their own keys. These do not authenticate the original videos or supply an eight-unit main-book answer key.

## Current evidence

`QA-REPORT.md` and `book/artifacts/qa_october_run.json` record current release checks; `book/artifacts/epubcheck-official.json` records the validator version and export fingerprint. `STRICT-AUDIT.md` preserves the original audit snapshot and a remediation update. Rebuild and rerun gates after any further edit. A passing suite does not close R01–R08.

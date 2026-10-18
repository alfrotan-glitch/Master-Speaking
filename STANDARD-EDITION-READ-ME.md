# Master Speaking — Original-manuscript Standard edition

## Current status

**Review proof; not approved for publication or public release.** This is a separate production of the original `Master Speaking.docx`, not a revision of the previously accepted self-contained edition. The original source manuscript and the unprefixed editions/supporting books remain unchanged; protected-input hashes are recorded in `book/standard/protected-inputs.json`.

The requester says they hold or represent the manuscript rights and authorized preparation, chose print PDF + EPUB, directed that uncleared third-party material be removed or replaced, and says course-owner confirmations can be supplied. Those statements authorize this preparation work; they are not independent evidence of manuscript ownership, third-party permissions, video intent, or final metadata. No unit-by-unit course-owner confirmations have yet been supplied. The intake register is `book/standard/publication-clearance.csv`.

The source attributes the work to Abdul Raziq Nazari and refers to The TOEFL House; those attributions have not been independently verified. The review cover and copyright page explicitly mark the proof status.

## Outputs

| File | Contents |
|---|---|
| `Master-Speaking-Standard.pdf` | 163-page reader PDF including its front cover |
| `Master-Speaking-Standard-print-7x10.pdf` | 162-page 7 × 10 inch print interior, no cover |
| `Master-Speaking-Standard.epub` | Reflowable EPUB with research references in its spine and navigation |
| `Master-Speaking-Standard-7x10.docx` | Editable Word proof; pagination can reflow |
| `Master-Speaking-Standard-Front-Cover.pdf` | Separate review-proof front panel |
| `Master-Speaking-Standard-Back-Cover.pdf` | Separate back panel describing video dependencies and proof status |

The cover panels are not a printer-imposed wrap. Spine, bleed, binding, stock, printer requirements, and physical proof remain outstanding.

## Preparation completed

- **105 guarded copyedits**, including eight removals, and **13 structural edits** are recorded in `book/standard/copyedits.json` and `structural-edits.json`. Chapter titles were preserved. The source ledger covers 3,203 nonempty original paragraphs/table cells; 184 normalized differences have explicit dispositions and none is unexplained. The 75 original reading paragraphs remain in source order. This scoped audit is not a character-for-character facsimile or a full independent proof.
- The **24 canonical embedded illustrations** were replaced in the Standard exports by original geometric artwork generated from generic shapes and course-owned labels by `book/tools/standard_artwork.py`, using the repository's Source Sans 3 fonts under the SIL Open Font License (`book/assets/fonts/source-sans-LICENSE.md`). The original image bytes are not in the Word or EPUB packages. A further WDP image-layer object in the source package is separately recorded and excluded. The protected original DOCX itself was not altered. Hashes, alt text, and provenance are in `book/standard/artwork-provenance.json`, `image-descriptions.json`, and `unmapped-source-media.json`.
- The replacement listening cards identify only an external activity and state that recording details require course-owner confirmation; they do not identify a speaker, publisher, or video. Their alt descriptions are in the image register.
- The attributed epigraph was removed from Standard exports pending primary-source verification and permission. Its presence in the unchanged original DOCX is not a license or attribution confirmation.
- Eight selected references support a limited set of qualified research claims. The appendix does not validate every factual statement or clear publication rights.
- Sensitive participation wording now allows general, imagined, or pass responses. No learner level, CEFR band, dialect, first language, or local context was inferred.

## Build and inspection evidence

The latest Standard-only build reports **3,422 master text blocks** in PDF, Word, and EPUB, with zero missing in each format. The print interior is 162 pages; units begin at physical pages 9, 25, 43, 61, 81, 101, 121, and 141. Automated print QA places 24 images at effective 327–444 dpi. All eight production checks pass: Word structure, cross-format text coverage, print geometry, automated page proof, EPUB structure, official EPUBCheck 5.3.0 (zero errors/warnings), chapter/navigation checks (32 chapters), and spread metrics (zero flags). The separate `qa_standard.py` check also passes for freshness, edition identity, protected inputs, source-image exclusion, and epigraph removal.

The latest 162-page print interior was viewed in six overview contact sheets. The 24 generated replacements were inspected as one contact sheet; the SMART graphic is readable, and the generic listening cards are visibly marked as unconfirmed resources. Selected pages, both cover panels, and the rights notice were rechecked at full size. This is not a complete every-word/full-size proof, a native-Word pagination proof, an assistive-technology test, an EPUB-device test, or a printer proof. The current visual record is `book/standard/qa/reviewed.json`; candidate-generation records alone are not proof of inspection.

Automated checks establish build integrity, not editorial correctness, rights clearance, accessibility conformance, teaching efficacy, or printer approval.

## Decisions and evidence still required before release

1. **Course-owner video sign-off.** `book/standard/video-dependencies.json` lists independently located candidates based on official pages/transcripts and exercise content; it does not establish the owner's intended recording. Confirm each unit's exact title, speaker, publisher, URL/video ID, version, playback, question alignment, captions/transcript plan, availability, and lawful use. Unit 1's exercise content matches a TED-Ed lesson while the old supplied still appears to depict a different School of Life video. Unit 3's exercise content matches a TED-Ed candidate, but the old still's identity remains unresolved. Do not rely on `book/publishing/current-media-register.csv` from the other edition.
2. **Rights, attribution, and legal review.** Confirm authority for manuscript publication and final author/publisher/imprint/copyright metadata. Obtain appropriate review for remaining manuscript quotations, external recordings/transcripts/marks, references, and the newly generated artwork. The supplied images and attributed epigraph were excluded, but this does not clear other content. No endorsement or license is implied.
3. **Final publication metadata.** Supply approved title/author/publisher/imprint/copyright lines and any ISBN, price, legal-deposit, distributor, or market-specific metadata. The source name and publisher reference are not independent verification.
4. **Printer approval.** Provide trim/bleed/spine/binding/stock specifications, impose a printer-specific cover, and approve a physical proof. The current panels are separate concepts.
5. **Accessibility and device checks.** EPUBCheck passes, but this EPUB has not been certified for accessibility. The PDFs are not tagged-accessible PDFs and have no certification. Test assistive technology and target EPUB devices and review reading order, image descriptions, contrast, and the Word source.
6. **Pronunciation review.** A specialist should review remaining dialect-specific/mixed IPA, stress examples, and classroom model accent. Directions allow accent variation; no single dialect has been established.
7. **Use and pilot review.** Personal/relationship prompts should remain optional; learners may answer generally or use fictional examples. No controlled teacher/learner pilot, suitability claim, or learning-effect claim is made.

**Do not describe the current edition as publish-ready.** The release register is an intake/evidence tracker, not a clearance record.

## Rebuild and inspect

```sh
bash book/tools/bootstrap.sh
python3 book/tools/standard_edition.py --source-only
python3 book/tools/standard_edition.py
python3 book/tools/qa_standard.py
python3 book/tools/review_standard.py
```

`standard_edition.py` extracts the protected original into ignored `book/standard/work/`, applies guarded Standard-only edits, replaces source illustrations in the staging copy, creates the six prefixed outputs, and runs production checks. It does not call the accepted edition's replacement-content build. `qa_standard.py` checks hashes, identity, source-image exclusion, and the removed epigraph. `review_standard.py` generates candidates only; inspect the new candidates and update the visual review record after each output-hash change.

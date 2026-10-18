# Master Speaking

An English speaking course by Abdul Raziq Nazari, The TOEFL House.

## Current self-contained edition

The author approved replacing the source-dependent listening lessons, existing imagery and uncleared quotation prompts with authored course material. **All 8 units and 32 exact chapter titles are preserved.**

- **24 original course graphics using eight topic-specific motifs**, with no stock images, screenshots or third-party logos in the current editions.
- **8 original fictional listening stories** included at the end of the matching listening chapters, with the same scripts and keys in the teacher pack. A teacher or partner reads them aloud; no external video or subscription is required. No recorded audio is supplied.
- Teacher keys cover **36 vocabulary completions, 74 closed-reading items and 40 listening-detail questions, plus suggested reasoning for 16 interpretation tasks**. Appropriate alternatives are accepted; these are not independently certified assessment instruments.
- **24 release checks pass**, including source fidelity, original-script/question alignment, exclusion of legacy media, vocabulary-key coverage, accessibility structure, print preflight and official EPUBCheck.
- Main book: **166-page 7×10 interior / 167-page reading PDF including front cover**. Supporting packs: student 18 pages, teacher 41 pages, companion 17 pages.

**Ready for teacher-led use with the supplied scripts. Prepared as a publication candidate, not commercially cleared or “fully verified.”** Independent complete review, publisher metadata approval, device/accessibility testing and printer-specific cover-wrap/physical approval remain distinct tasks. See [publication status](PUBLICATION-READINESS.md) and the [current conditions](UNRESOLVED-ISSUES.md).

See [what changed in the improvement pass](IMPROVEMENT-REVIEW.md) for the protected content and actual review scope.

## Original-manuscript Standard review proof

The separate files named `Master-Speaking-Standard...` reconstruct the original video-based manuscript and remain **review proofs, not approved for publication or public release**. Their 24 supplied illustrations have been replaced with original geometric artwork, and the attributed epigraph is omitted; course-owner video confirmations, final metadata, rights review, accessibility/device checks, and printer approval remain outstanding. They are not the accepted self-contained edition or a source of verified keys for its video lessons. See the [Standard review-proof guide](STANDARD-EDITION-READ-ME.md), [implementation/review record](STANDARD-EDITION-REVIEW.md), and [35-item evidence register](book/standard/publication-clearance.csv).

## Books and cover panels

- **[Main reading PDF](Master-Speaking.pdf)** — clean learner-facing book with cover, linked contents and bookmarks.
- [Editable main book](Master-Speaking-7x10.docx) · [EPUB](Master-Speaking.epub) · [7×10 print interior](Master-Speaking-print-7x10.pdf).
- [Front cover](Master-Speaking-Front-Cover.pdf) · [matching back cover](Master-Speaking-Back-Cover.pdf) — separate 7×10 panels, not an imposed printer-specific wrap.
- [Student Practice Pack PDF](Master-Speaking-Student-Practice-Pack.pdf) · [Word](Master-Speaking-Student-Practice-Pack.docx).
- [Teacher Implementation Pack PDF](Master-Speaking-Teacher-Implementation-Pack.pdf) · [Word](Master-Speaking-Teacher-Implementation-Pack.docx).
- [Class Companion PDF](Master-Speaking-Class-Companion.pdf) · [Word](Master-Speaking-Class-Companion.docx).

`Master-Speaking-Reading-Edition.pdf` is an identical compatibility copy of the main reading PDF.

## Start teaching

Use the Teacher Pack’s four 75-minute Unit 1 lessons and the matching student pages. For listening, keep the script at the end of Chapter 2 covered until after the second listening. Read the matching teacher script aloud twice and use the five matching detail questions. Do not substitute a historical video or unrelated audio and reuse these keys.

For independent reading practice, a learner can read a script, cover it and answer from memory. That is reading recall, not evidence of listening performance. Provide transcripts earlier when an access arrangement requires them and record the support actually used.

The companion offers a different 16-meeting course plan; its timings are not interchangeable with the slower diagnostic Unit 1 plan. Preview topics, permit fictional/neutral alternatives, give feedback and repeat a short task. No live pilot or improvement results are claimed. See [pilot safeguards](PILOT-USE-POLICY.md).

## Rebuild, check and package

```sh
bash book/tools/bootstrap.sh
python book/tools/release.py
python book/tools/package_books.py
```

The release command draws the original course graphics, reconstructs the guarded editorial base, applies the authorized self-contained replacements, rebuilds all books and runs 24 gates. `--skip-build` checks existing exports. Packaging verifies the recorded export hashes before creating `Master-Speaking-All-Books.zip`; the duplicate download ZIP is intentionally excluded from Git.

Authored sources include `book/master/self-contained-edition.json`, `book/classroom/modules.json`, `vocabulary-keys.json`, `reading-closed-keys.json`, `unit1-reading-key.json`, `teacher-notes.md` and `book/companion/speaking-class.md`. Edit sources, not generated editions. The historical `Master Speaking.docx` remains unchanged; old manuscript media is retained only for audit and is excluded from current Word/EPUB exports.

## Evidence and limitations

- [Current QA results and hashes](QA-REPORT.md)
- [Revision and visual-proof scope](REWRITE-PROGRESS.md)
- [Word/EPUB accessibility work](ACCESSIBILITY-REVIEW.md)
- [Editorial change log](CHANGELOG.md)
- Current artwork provenance: `book/publishing/current-artwork-provenance.json`
- Current read-aloud input register: `book/publishing/current-media-register.csv`

Earlier design, audit and ten-lens reports are historical records. They are not independent human endorsements or the current release-condition register. Passing tests does not establish universal factual accuracy, legal ownership, learning efficacy, accessibility certification or printer approval. Production discussion stays outside the learner-facing book.

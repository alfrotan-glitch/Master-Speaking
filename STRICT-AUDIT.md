# Strict audit — Master Speaking

**Date:** 17 October 2026  
**Verdict: HOLD for commercial publication. Not problem-free.**

This is a stricter follow-up to the 12 passing production checks. It distinguishes confirmed defects from missing verification. It is not an independent human proof, legal opinion, factual certification, or official accessibility/conformance test. The book exports were not changed during this audit. Production discussion remains outside the book.

## Remediation update — 17 October 2026

The findings and fingerprints below describe the **pre-remediation snapshot**, not the rebuilt exports. Publication remains on hold for the unresolved conditions in `UNRESOLVED-ISSUES.md`.

- **A1 corrected:** contrasting stress targets are explicitly capitalized, with matching delivery instructions and case-sensitive checks across all formats.
- **A3 materially strengthened:** complete normalized blocks replace sampled-fragment acceptance; minimum occurrence counts and truncation regression probes are included. This is not a complete semantic-order or typography proof.
- **A6 reconciled:** the current issue register and publication/editorial reports remove stale guide/edit counts and the unsubstantiated missing-activation allegation.
- **B4 partially addressed:** the overbroad rising-question rule is qualified and contextualized; broader pronunciation-specialist approval is still pending.
- **B5 format-validation portion completed:** official EPUBCheck 5.3.0 found a genuine RSC-011 contents/spine defect; it was repaired. Current validation has zero errors/warnings and is now included in the 13-check release workflow. Device/accessibility testing remains open.
- **A2, A4, A5 and other B conditions remain open.** No permissions, original recordings, native Word proof, accessible-PDF certification, or print approvals have been invented.

## 1. Confirmed findings

### A1 — High: an instructional contrast is missing

**Location:** Unit 3, Chapter 4; printed page **49**, reader-PDF physical page **58**; “Emphasize Key Words.”

Both “Instead of” and “Say” print the identical sentence: “Emotional intelligence is important for everyone.” Both are single spans in SourceSerif4-Regular, with the same font flags (4), and no visual indication of different emphasis. The semantic source also stores them as identical plain-text paragraphs. A learner cannot infer the intended stress contrast from the printed examples.

**Required correction:** explicitly distinguish flat delivery from selective stress, with a clearly marked target word or words and a matching explanation. Preserve that emphasis in Word, PDF, and EPUB. Add a regression test for the actual instructional contrast—not just the presence of the words.

### A2 — High for distributing Word: cached contents lack page references

The distributed Word file contains real unit/chapter labels in a refreshable TOC field, but its cached contents do not contain page numbers. That is not a completed paginated Word contents page. PDF contents have computed, checked folios; those do not validate a native Word layout.

**Required correction:** open with the intended fonts in native Word, refresh all fields, save the resulting cache, export, and compare chapter starts and contents references. Do not copy PDF folios into Word without checking its native pagination.

### A3 — High: the text-fidelity gate can miss substantial omissions

**Evidence:** `book/tools/qa_fidelity.py`, `hit()` and `windows()`. For a longer source block, `hit()` returns true when **any one** sampled window matches. It does not require the complete block or even every sampled window to be present.

An adversarial test used a real 315-character reading paragraph, retained only the first 60 characters of its normalized text, and called the checker. It still returned `True`.

**Important limit:** this is a proven weakness of the checker, not evidence that those words are missing from the actual book. A separate, stricter scan of the current PDF found **zero unmatched complete source blocks longer than 30 normalized characters**. That scan removed whitespace/punctuation and compared complete compacted text; it cannot validate typography, pronunciation symbols, order in every case, or instructional correctness. It also did not certify the other formats.

**Required correction:** use full-block, occurrence-aware, format-specific fidelity checks, with narrowly documented allowances for wrapping/page boundaries. Add deliberate truncation, duplication, reordering, and emphasis-loss tests.

### A4 — Medium: two print image placements are low-resolution

Current preflight records **122.4 dpi** on interior physical page 25 (printed 17; reader 26) and **142.9 dpi** on interior physical page 27 (printed 19; reader 28). They are recorded as source-limited exceptions, not failures, so a passing preflight does not mean all images meet a printer’s resolution requirements.

**Required correction:** obtain better originals, reduce placement sizes if viable, or obtain printer approval after physical proof. Do not treat artificial upscaling as recovered detail.

### A5 — High for an accessible PDF release: structural tagging is absent

The current reader PDF’s catalog reports both `StructTreeRoot` and `MarkInfo` as null. It has selectable text and bookmarks, but these are not substitutes for tagged headings, table semantics, image alternatives, or verified assistive-technology reading order.

**Required correction:** establish an accessible export workflow and test it with appropriate tools and assistive technology. Do not label this edition PDF/UA-compliant or fully accessible on current evidence.

### A6 — Medium: production records contradict the current edition

Examples:

- `PUBLICATION-READINESS.md` still describes four classroom-guidance paragraphs and an in-book media warning in its earlier “What changed” section, although the later cleanup section correctly says three paragraphs remain and that warning was removed.
- `UNRESOLVED-ISSUES.md` still says the printed guidance tells teachers to verify inputs, and still quotes forty-two edits. The current reviewed chapter/front-matter registers total forty-five edits.
- The unresolved-issues record alleges missing Unit 5 vocabulary-activation items. The current Unit 5 Chapter 3 has ten expressions and a task to use all ten; source items 1602–1605 support that task. The allegation was **not substantiated for that exercise**. Do not manufacture replacement questions to satisfy an unverified old report. Identify another exact location if one was intended, or close the stale allegation.
- An older paragraph says the workflow has eleven checks; its later follow-up correctly says twelve.

**Required correction:** reconcile reports into one current status register, with location, evidence, owner, and closure condition. Historical assertions must not silently survive as current findings.

## 2. Unresolved release conditions—not proven factual errors or legal violations

### B1 — Blocking: listening inputs are not verified

All **eight** rows in `book/publishing/media-register.csv` remain UNVERIFIED, with no verified recording URL, creator, or permission basis. Unit 2 Chapter 2 prints “The Art of Goal Setting” as the media title and “Why You Should Stop Setting Goals (Yes, Really)” under “Look at the Title” (printed page 24, reader page 33). These may be a topic label and a recording title, but that relationship is not established. Generic TED-Ed wording does not establish the source.

**Closure:** identify each intended recording; verify access, attribution/permission basis, vocabulary, every comprehension answer, and any transcript. The separate teacher-read alternatives are useful but do not validate the original-media exercises. Missing source scripts are not automatically a book defect if no script section is promised; do not invent them or imply they were supplied.

### B2 — Blocking: existing image permissions are not evidenced

The asset register contains 25 entries; **24 existing manuscript assets** are marked UNVERIFIED. This establishes missing clearance evidence, not that every asset infringes copyright. Official font licenses are separately documented and do not resolve image rights.

**Closure:** document source, creator, license/permission, attribution requirements, and evidence for each existing asset, or replace/remove it under an approved editorial decision. Also review quotations, imprint authority, and publishing metadata.

### B3 — High: factual/subject review is incomplete

Current readings make research claims without source-specific substantiation in this audit: for example, Unit 2’s claim about writing down goals; Unit 3’s framing of IQ and emotional intelligence; Unit 4’s income/life-satisfaction, hedonic-treadmill, experience-spending, and generosity claims. These may be defensible with suitable qualification and evidence. They are **not certified true or declared false here**.

**Closure:** identify suitable sources; check what each actually supports; distinguish correlation, causation, and illustrative anecdotes; qualify overgeneralizations and add references where appropriate.

### B4 — High: pronunciation pedagogy requires review

Unit 3 Chapter 4 teaches rising intonation “when asking a question” and gives wh-question examples. English question intonation is context-sensitive; wh-questions commonly have falling contours in neutral use. Rising contours are possible, so the arrows are not intrinsically impossible, but the stated rule is too broad without context.

**Closure:** have a pronunciation specialist review rules and models, specify context and intended accent where material varies, and supply accurate recorded examples or clear teaching notes. A spelling checker deliberately skips many pronunciation lines; its pass cannot validate them.

### B5 — High before ebook release: conformance/device testing is incomplete

The EPUB passes the project’s structural/navigation checks, including corrected unit-before-chapter spine order. Official EPUBCheck and representative reader/screen-reader tests have not been performed. CSS page breaks cannot guarantee physical print-like pages in a scrolling/reflowable reader.

**Closure:** official validation plus tests of navigation, table reflow, images/alt text, resizing, dark mode, and reading order in representative devices/apps.

### B6 — High before manufacturing: no final print package or physical approval

The cover is front-only, not a printer-approved front/spine/back wrap. Native Word comparison, final printer specifications, binding/spine calculations, and a physical proof remain outstanding.

**Closure:** freeze approved content and pagination, agree printer specifications, produce the wrap, and approve a physical proof.

### B7 — High before claims of classroom validation: no completed pilot/full sign-off

The separate packs provide useful support and pilot plans, but are not evidence of trials. A signed full language/exercise/page proof and representative learner pilot remain outstanding. Sensitive-topic suitability, pacing, difficulty, answerability, and assessment consistency require review.

## 3. What passed this audit’s limited checks

- The dedicated chapter check was rerun: **32 distinct names**, Word heading page-break/subtitle properties, actual PDF opening pages, chapter contents folios/links, bookmark offsets, and EPUB chapter navigation/spine order all passed.
- Reader-boundary scan was rerun: no matches for the **19 specifically tested** production/chat patterns. This is not an exhaustive natural-language leakage detector.
- Separate complete-block PDF scan: zero unmatched blocks longer than 30 normalized characters, under the normalization described in A3.
- Existing 12 production checks remain recorded as passing. Their defined scope does not cover the release conditions above.

## 4. Required order of work

1. Fix the confirmed instructional contrast and review the intonation rule; add semantic/emphasis tests.
2. Strengthen fidelity tests and reconcile stale reports, without inventing a missing exercise.
3. Resolve recording identity/alignment, rights evidence, and factual references.
4. Complete native Word contents/pagination, accessible outputs, EPUB/device tests, and print assets.
5. Perform the full final proof and learner pilot; rebuild, rerun all applicable checks, approve physical/device proofs, and obtain responsible editorial/publisher sign-off.

**Release decision:** suitable as an editorial review proof, not justified as an error-free, commercially cleared, fully accessible, or classroom-validated publication. A passing test suite is evidence for its assertions, not a universal approval certificate.

## Audited export fingerprints

| File | SHA-256 |
|---|---|
| `Master-Speaking.pdf` | `cdbd75b35a6605b5b1af865ad5493abf457e8591b7df9bc3808973bac9429a5f` |
| `Master-Speaking-print-7x10.pdf` | `cf5dc0c148336a4398b87dba73cdd78dc77874fae62845973f534b4b32419ea0` |
| `Master-Speaking-7x10.docx` | `cb0f8c0a643902b80ff35536787d99acbc71917b11a42120922e7108768bf2a2` |
| `Master-Speaking.epub` | `5f1a8551d5baf9b70c83c4bcc4424cfc8300ce89a374e3cf3686cfd2c345a535` |

# PDF Visual QA Report — *Master Speaking* (7×10 in, 161 pages)

## Method

- Every page measured: word count, used text depth (fraction of the type area filled), image presence.
- Two-page spreads evaluated for density balance (verso+recto word ratio).
- Chapter-end whitespace measured and graded against the next chapter start.
- Full-page renders for the human eye pass: `book/artifacts/proof_png/` (p001.png … p161.png).

## Spread balance

- 75 body spreads measured; median words/spread 356.
- Imbalance tolerance: ratio > 3.2 is flagged **unless** the spread contains a chapter or unit opening (intentional white space by design — §22).
- Flags: **0**

- none

## Chapter endings (§22)

- 32 chapter-end pages; median fill depth 68% of the type area.
- Natural white space at chapter end is acceptable by specification; all endings checked for accidental-looking half pages (see flags above — none).

## Page-by-page findings (§28 checklist)

- Text clipping / overflow: none (qa_proof bounds checks, 161/161 pages).
- Widow/orphan lines: none beyond style controls (qa_print gating).
- Stranded headings: none (keep-with-next + qa_print head checks).
- Accidental blank pages: none (qa_proof).
- Table cell mid-word breaks: none (column-width floor in typesetter).
- Chapter starts: 32/32 begin at the top of their own page (outline + first-text verification).
- Unit openers: 8/8 on recto with full-width opener image.

## Human eye pass

- Automated geometric/typographic evidence is above; page renders are provided for the reviewing editor’s visual pass. This report certifies the measurable page qualities; final aesthetic sign-off belongs to the human reviewer.
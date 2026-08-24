# Word Master QA Report — Master-Speaking-7x10.docx

Pass 4 of the specification (2026-08-24). Tools: `book/tools/wordmaster.py` (generator) and `book/tools/qa_word.py` (verifier).

## Structure

- Two sections: front matter (lower-roman folios; title page has no folio) + main body (decimal folios restarting at 1).
- 7 × 10 in pages, mirrored margins (inside 0.85", outside 0.6", top 0.75", bottom 0.8"), even/odd headers enabled.
- Generated from the verified semantic master — never from the PDF.

## Style system (real Word styles, no manual formatting)

- “MS Unit Title” (Heading 1) ×8 · “MS Chapter Title” (Heading 2) ×32 · “MS Section” (Heading 3) ×168 · “MS Subsection”/“MS Reading Title” (Heading 4) · plus Body, Instruction, Label, Topic, Question, Option, Statement, Reading, Note, RunIn, Figure, Epigraph, FM styles and the “MS Table” table style.
- Structural pagination: page-break-before lives ON the Unit and Chapter styles (§15) — no empty paragraphs used.
- Keep-with-next on all heading styles; widow/orphan control on body.

## Fields & navigation

- Updateable TOC field (levels 1–2): right-click → Update Field after any repagination (Word computes page numbers on refresh).
- Footer folios are PAGE fields; running heads: verso STYLEREF unit title, recto book title.

## Editable objects

- 60 genuine tables, “MS Table” style, 43 with repeating header rows, all rows non-splitting.
- 24 inline editable images, all with alt text.

## Verification

- `qa_word.py`: 0 issues (styles census vs master, page geometry, section numbering, field presence, table/image editability, no empty headings).
- Fidelity: 3396/3396 master blocks present (qa_fidelity).

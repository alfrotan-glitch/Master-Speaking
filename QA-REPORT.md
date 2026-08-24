# QA Report — *Master Speaking*

Build date: 2026-08-24 · Standard: zero-error (§38) · All 9 QA passes of the specification PASS

## The 9 QA passes (§34), mapped to tools and evidence

| # | Pass | Tool(s) | Result | Key facts |
|---|------|---------|--------|-----------|
| 1 | Structural | `qa_content.py` | **PASS** | 8 units / 32 chapters / correct order & hierarchy; 3181 source texts: 3161 covered, 20 classified logged transforms, 0 missing |
| 2 | Editorial | `qa_editorial.py` | **PASS** | 0 unknown words, 0 duplicated words, 0 double spaces, 0 straight quotes/apostrophes, 0 spacing-punctuation errors; 167 pronunciation lines exempt from spellcheck by design |
| 3 | Typographic | `qa_print.py` + `qa_preflight.py` fonts | **PASS** | 8 embedded TrueType subsets (Source Serif 4 / Source Sans 3 / DejaVu Sans), no base-14 fallbacks, curly quotes/dashes unified |
| 4 | Word | `qa_word.py` | **PASS** | 7×10 + mirrored margins, 2 sections (roman/decimal), Heading 1–4 style system, structural page-break-before on Unit/Chapter styles, TOC + PAGE + STYLEREF fields, 60 editable tables (43 repeating header rows), 24 editable images with alt text |
| 5 | PDF layout (page-by-page) | `qa_proof.py` | **PASS** | all 161 pages: folios, parity type areas, no line collisions, opener titles; 32/32 chapters verified to begin at the top of their own page; 2 intentional blank versos before recto unit openers (print convention) |
| 6 | Cross-reference | `qa_print.py` TOC check + `qa_epub.py` nav | **PASS** | print TOC folios verified against real positions; EPUB nav exposes every spine document |
| 7 | Print preflight | `qa_preflight.py` | **PASS** | PDF PDF 1.4, uniform 504×720 pt, 8 fonts embedded, 24 images at 150.0–659.3 dpi, no annotations |
| 8 | EPUB | `qa_epub.py` | **PASS** | 75 files, 45-item spine, OCF zip rules, manifest/spine closure, all references resolve, warm-ups in unit openers; epubcheck not runnable here (no Java) — structural validation as compensating control |
| 9 | Final visual | `qa_visual.py` + page renders | **PASS** | 75 spreads measured, 0 imbalance flags, median chapter-end fill 68%; all 161 page renders in `book/artifacts/proof_png/` for the human eye pass |

## Content fidelity (§35) — master to all three outputs


`qa_fidelity.py`: **3396/3396** master text blocks traced into the print PDF text layer, the EPUB content documents, AND the editable Word master — 100% substantive coverage, no silent loss (this check caught and drove the fix of the EPUB warm-up omission and 7 missing DOCX figures).

## Deterministic rebuild

The complete chain — .docx → extract → parse → book.json → master.xhtml → {PDF, EPUB, DOCX} — was rebuilt from scratch in a factory-reset sandbox (all packages reinstalled) and reproduced the identical book: content, page count, and every QA gate.

## Locked content decisions verified in the build

- Forward → Foreword (heading renamed).
- Second identical “Before You Read” block removed in all 8 units (logged).
- Unit 8 stray heading “The Future of Marriage” removed; questions kept.
- Unit 1 preserved as-is (no invented sections).
- No invented Homework for Units 5 & 8.
- Unit 6 keeps both Speaking Challenges, labelled 1 and 2.
- Empty headings, web-style contamination, dead hdphoto1.wdp and duplicated unit-title artifacts removed (logged).
- Foreword sign-off “September, 2026” carried as in source.

## Reproduce

```
python3 book/tools/extract.py     # docx -> dump.json + image_map.json
python3 book/tools/parse.py       # -> book.json + changelog.json
python3 book/tools/master.py      # -> master.xhtml (source of truth)
python3 book/tools/pdf.py         # -> Master-Speaking-print-7x10.pdf
python3 book/tools/epub.py        # -> Master-Speaking.epub
python3 book/tools/wordmaster.py  # -> Master-Speaking-7x10.docx
python3 book/tools/qa_content.py && python3 book/tools/qa_editorial.py
python3 book/tools/qa_print.py && python3 book/tools/qa_proof.py
python3 book/tools/qa_preflight.py && python3 book/tools/qa_epub.py
python3 book/tools/qa_word.py && python3 book/tools/qa_fidelity.py
python3 book/tools/qa_visual.py && python3 book/tools/reports.py
```

Artifacts: `book/artifacts/qa_*.json` (machine-readable results).
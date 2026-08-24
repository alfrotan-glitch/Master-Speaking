# QA Report — *Master Speaking*

Build date: 2026-08-24 · Standard: zero-error · All 8 named passes PASS

## The 8 named QA passes

| # | Pass | Tool | Result | Key facts |
|---|------|------|--------|-----------|
| 1 | Content integrity (source → master → outputs) | `qa_content.py` + `qa_fidelity.py` | **PASS** | 3181 source texts: 3161 covered, 20 classified logged transforms, 0 missing; and 3396/3396 master blocks traced into BOTH the PDF text layer and the EPUB |
| 2 | Editorial / proofreading | `qa_editorial.py` | **PASS** | 0 unknown words, 0 duplicated words, 0 double spaces, 0 straight quotes/apostrophes, 0 spacing-punct errors; 167 pronunciation lines exempted from spellcheck by design |
| 3 | Layout & pagination | `qa_print.py` | **PASS** | 161 pages; unit openers on recto [11, 29, 45, 63, 81, 101, 121, 141]; 0 issues |
| 4 | Page-by-page proof | `qa_proof.py` | **PASS** | all 161 pages: folios correct, text/images inside the parity-correct type area, no line collisions, no blank pages, unit opener titles verified; visual renders in `book/artifacts/proof_png/` |
| 5 | Print preflight | `qa_preflight.py` | **PASS** | PDF 1.4, uniform 504×720 pt, 8 fonts all embedded TrueType subsets, 24 images at 150.0–659.3 effective dpi, no annotations, not encrypted |
| 6 | EPUB structural validation | `qa_epub.py` | **PASS** | 75 files, 45-item spine, OCF zip rules, manifest/spine closure, all references resolve, nav + landmarks + NCX complete; epubcheck not executable in build environment (no Java) — see EPUB-REPORT.md |
| 7 | Navigation & TOC | `qa_print.py` (TOC-folio check) | **PASS** | contents folios verified against actual unit/chapter positions (same-y line merging) |
| 8 | Deterministic rebuild | full chain from .docx, clean environment | **PASS** | docx → extract → parse → master → PDF/EPUB rebuilt from scratch in a fresh sandbox (packages reinstalled); identical content, 161 pp, all QA gates reproduce |

## Locked content decisions verified in the build

- Forward → Foreword (heading renamed).
- Second identical “Before You Read” block removed in all 8 units (logged).
- Unit 8 stray heading “The Future of Marriage” removed; its questions kept, no invented replacement heading.
- Unit 1 preserved as-is (no invented Research Task / Group Discussion / Homework).
- No invented Homework for Units 5 & 8.
- Unit 6 keeps both Speaking Challenges, labelled 1 and 2.
- Empty headings, web-style contamination, dead hdphoto1.wdp reference and duplicated unit-title artifacts removed (logged).
- Foreword sign-off “September, 2026” carried as in source.

## Reproduce

```
python3 book/tools/parse.py      # docx → book.json (changelog built here)
python3 book/tools/master.py     # book.json → master.xhtml
python3 book/tools/pdf.py        # master → Master-Speaking-print-7x10.pdf
python3 book/tools/epub.py       # master → Master-Speaking.epub
python3 book/tools/qa_content.py && python3 book/tools/qa_editorial.py
python3 book/tools/qa_print.py && python3 book/tools/qa_proof.py
python3 book/tools/qa_preflight.py && python3 book/tools/qa_epub.py
```

Artifacts: `book/artifacts/qa_*.json` (machine-readable results of each pass).
# Unresolved Issues — *Master Speaking*

As of build 2026-08-24. None of these block the deliverables; each is a conscious carry-over or environment limitation, recorded here rather than silently “fixed”.

## Content carries (source defects preserved or dropped, never invented)

1. **U5 vocabulary-activation items missing in source** (dump items 1604–1605): the source document itself lacks these list items; no content was invented to fill the gap.
2. **U8 item 2593 dropped** (mismatched True/False instruction that belonged to a different exercise) — logged in the change log.
3. **Unit 8 “The Future of Marriage” heading** removed (wrong heading in source); its questions retained under the preceding section, with no invented replacement heading (locked decision).
4. **Foreword sign-off “September, 2026”** carried exactly as written in source (comma included).

5. **Video Scripts section — absent from the original manuscript.** A complete audit of `Master Speaking.docx` (all 166,777 body characters reconciled to dump paragraphs and tables; footnotes and endnotes empty; all 50 textbox stories inventoried = front epigraph + 8 unit-opener panels) found **no Video Scripts section anywhere in the source**. Under the locked no-invention rule the fidelity count is therefore **0 = 0 = 0 = 0** across ORIGINAL / DOCX / PDF / EPUB. If scripts exist elsewhere, supply them and the section will be rebuilt to the original visual identity.

## Scope notes

5. **Cover files**: the source document contains no cover art (all 25 media files are interior content images). A designed cover would be new artwork — outside the locked no-invention scope — so none is included. The title page (PDF p. 3 / EPUB title.xhtml) serves as the opening display page.
6. **No bleed**: interior text-and-figure book on white ground; all content sits inside margins. Print-ready as a borderless 7×10 PDF or with standard grip (locked decision).

## Deliberate typographic conventions

11. **Four blank verso pages (physical 28, 106, 128, 150)** immediately before recto unit openers — the standard print convention when sections are locked to recto starts; intentional and verified by QA.

## Word master notes

6. **DOCX TOC field** computes page numbers on refresh: open the file, right-click the TOC, choose “Update Field” (no rendering engine exists in this sandbox to pre-bake field results).
7. **Fonts**: the DOCX references Source Serif 4 / Source Sans 3 by name; without them installed, Word falls back gracefully and the style system (sizes, spacing, colours) is unaffected. The print PDF embeds the fonts and is authoritative for final appearance.

## Environment limitations

10. **DOCX→PDF conversion**: no LibreOffice/MS Word exists in the build sandbox and the system package mirror is unreachable (PyPI only). The print PDF is therefore produced by `book/tools/docxpdf.py`, a dedicated renderer that reads **Master-Speaking-7x10.docx itself** (its styles, shading fills, table cell fills, images, column widths and page-break structure) — never the semantic master — so every PDF fix still starts as a DOCX fix. For a Word/LibreOffice-native render, open the DOCX in Word and export; the DOCX is the production master either way.

8. **epubcheck / Java unavailable** in the build sandbox; EPUB validated structurally instead (see EPUB-QA-REPORT / EPUB-REPORT.md).
9. **Google Fonts offline**: text faces are the locally installed Source Serif 4 / Source Sans 3 / DejaVu Sans files, all embedded and subset in the PDF.

## Verification aids

- Page renders for the human visual pass: `book/artifacts/proof_png/`
- Machine-readable QA artifacts: `book/artifacts/qa_*.json`
- Change log: `CHANGELOG.md` (machine copy `book/artifacts/changelog.json`)
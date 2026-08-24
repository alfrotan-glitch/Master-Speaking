# Unresolved Issues — *Master Speaking*

As of build 2026-08-24. None of these block the deliverables; each is a conscious carry-over or environment limitation, recorded here rather than silently “fixed”.

## Content carries (source defects preserved or dropped, never invented)

1. **U5 vocabulary-activation items missing in source** (dump items 1604–1605): the source document itself lacks these list items; no content was invented to fill the gap.
2. **U8 item 2593 dropped** (mismatched True/False instruction that belonged to a different exercise) — logged in the change log.
3. **Unit 8 “The Future of Marriage” heading** removed (wrong heading in source); its questions retained under the preceding section, with no invented replacement heading (locked decision).
4. **Foreword sign-off “September, 2026”** carried exactly as written in source (comma included).

## Scope notes

5. **Cover files**: the source document contains no cover art (all 25 media files are interior content images). A designed cover would be new artwork — outside the locked no-invention scope — so none is included. The title page (PDF p. 3 / EPUB title.xhtml) serves as the opening display page.
6. **No bleed**: interior text-and-figure book on white ground; all content sits inside margins. Print-ready as a borderless 7×10 PDF or with standard grip (locked decision).

## Environment limitations

7. **epubcheck / Java unavailable** in the build sandbox; EPUB validated structurally instead (see EPUB-REPORT.md).
8. **Google Fonts offline**: text faces are the locally installed Source Serif 4 / Source Sans 3 / DejaVu Sans files, all embedded and subset in the PDF.

## Verification aids

- Page renders for a human visual pass: `book/artifacts/proof_png/`
- Machine-readable QA artifacts: `book/artifacts/qa_*.json`
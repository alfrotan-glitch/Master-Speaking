# Current Word/EPUB accessibility work

18 October 2026 · Self-contained edition

## Implemented

- All 24 interior graphics are original teaching diagrams. Their alternative text includes the full title, explanatory subtitle and card text, rather than generic “illustration” labels. The original front cover also has a description.
- Descriptions in `book/master/image-descriptions.json` are bound to source-image hashes. Word checks match each description to the actual embedded drawing bytes. EPUB checks require the same descriptions and reviewed bytes, exactly once per expected image, including the cover.
- Old manuscript photographs, video screenshots and logos are excluded from the current Word/EPUB packages, including unused embedded files. Original diagrams are drawn by `edition_graphics.py` from the edition plan; font provenance/licenses are recorded separately.
- Each standalone EPUB chapter starts at h1 with no skipped levels. The combined semantic master and Word retain the unit/chapter/section hierarchy. Class-based EPUB styling preserves the design when heading levels change.
- English `lang` and `xml:lang`, labeled contents/landmark navigation, valid target documents/fragments, and table-column header scope are checked.
- Discovery metadata describes implemented features and the supplied read-aloud route. No recorded audio is supplied. The accessibility summary explicitly states that accessibility conformance has not been evaluated.

## Evidence

**24 release gates pass.** Official EPUBCheck 5.3.0 reports zero errors and warnings. The accessibility gate rejects seven isolated mutations: generic alt text, a missing target document, missing language, chapter h2 regression, missing header scope, missing target fragment and swapped image bytes. Separate self-contained checks reject a missing script and reintroduced legacy image.

Graphics are visually reviewed; all PDF pages receive automated geometry/content checks and overview review, with selected readable-page proof recorded separately. The earlier 235-page pixel-identity comparison is historical: this edition deliberately changes artwork, lesson content and pagination.

## Not yet established

Screen-reader, keyboard, resizing, dark-mode and representative device testing remain outstanding. The custom PDF remains structurally untagged; Word headings do not automatically make the PDF accessible. No WCAG, EPUB accessibility or PDF/UA certification is claimed. Independent review of descriptions and retained text is still appropriate. See [UNRESOLVED-ISSUES.md](UNRESOLVED-ISSUES.md).

Machine evidence: `qa_accessibility.json`, `qa_self_contained.json`, `epubcheck-official.json` and [QA-REPORT.md](QA-REPORT.md).

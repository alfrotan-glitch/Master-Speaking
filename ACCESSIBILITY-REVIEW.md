# Word and EPUB accessibility improvements

18 October 2026 · Master Speaking · AI-assisted production review

## Implemented and checked

- Visually inspected the 24 interior illustrations and the front cover. Replaced generic image alternatives with descriptions of visible content. The goal-setting mind map, relationship diagram and cover also received individual image inspection. In particular, the relationship diagram reads **Compassion**, not Communication; the alternative text preserves that distinction.
- The descriptions live in `book/master/image-descriptions.json`, with image SHA-256 fingerprints. Missing descriptions, changed assets or duplicate filename mappings stop reconstruction until the descriptions are reviewed. The single-frame GIF and its PNG replacement have identical decoded pixels.
- The same interior descriptions now reach both Word and EPUB through the semantic master. Word checks bind each description to the actual embedded image bytes, not merely to a drawing count. EPUB checks also compare image bytes with the reviewed originals. Every interior image appears once in each format; EPUB additionally includes the described cover.
- Each of the **32 standalone EPUB chapters now begins with an h1**, and the outline avoids skipped levels. The combined semantic master and Word hierarchy remain unit/chapter/section based. Class-based EPUB styling preserves the chapter-title design when the heading tag changes.
- Added matching English `lang` and `xml:lang` attributes, labels for the contents and landmarks navigation regions, and accessibility metadata describing implemented alternative text, headings and linked contents. The accessibility summary explains that listening needs external recordings and that accessibility conformance has not been evaluated. No certification or conformance claim has been added.
- The new check verifies table-column header scope and resolves contents/landmark links, including fragment identifiers.

## Results

**22 release gates pass**, including `qa_accessibility.py`. Official EPUBCheck 5.3.0 reports **zero errors and warnings**.

Seven isolated negative controls are rejected without changing the publication files:

1. Generic image description substituted for a reviewed description.
2. Link to a missing document.
3. Missing language attribute.
4. Standalone chapter title changed back to h2.
5. Missing column-header scope.
6. Link to a missing fragment.
7. Different image bytes substituted under an existing filename.

The print and three support PDFs retain the same page counts. SHA-256 comparisons of rendered RGB pixels confirm that **all 235 interior/support pages are visually unchanged** from the preceding edition. The prior selected readable-page review therefore remains applicable; this is not a new complete manual proof. See `book/qa/accessibility/render-identity.json` and the linked final-proof index.

## Still open

This is a defined structural and content-description improvement, **not an accessibility certification**. Screen-reader, keyboard, resizing, dark-mode and representative EPUB-device testing remain outstanding. The reader PDF remains untagged; Word structure does not automatically make the custom PDF export accessible. Alternative-text descriptions are AI-assisted and still benefit from independent specialist review. Existing image rights, original recording identification/permissions, full independent copyediting and printer approval remain separate open conditions.

Current machine results: `book/artifacts/qa_accessibility.json`, `book/artifacts/epubcheck-official.json`, and `QA-REPORT.md`. The original manuscript and exact chapter titles remain unchanged; production commentary stays outside the reader-facing main text.

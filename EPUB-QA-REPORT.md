# EPUB Report — *Master Speaking* (reflowable EPUB 3)

Build date: 2026-08-24 · `Master-Speaking.epub` (5,778,094 bytes)

## Structure

- mimetype first entry, STORED (OCF rule); META-INF/container.xml → content.opf
- 75 files: 45 spine items — title page, copyright, foreword, How to Use, epigraph, 8 unit openers + 32 chapters (unit openers carry their THINK warm-up questions)
- one XHTML per front-matter piece / unit opener / chapter; shared `style.css` in em/% units; 24 images (the .gif ships as its .png twin)
- `nav.xhtml` with `epub:type="toc"` (hidden) + landmarks; `toc.ncx` for EPUB2 reading systems; OPF 3.0 with `dcterms:modified`
- identifier: `urn:uuid:c5e64b7d-b933-5c1b-902f-22c646b66a32` (UUIDv5 of “Master Speaking / Abdul Raziq Nazari / 2026”)

## Validation

`qa_epub.py` (structural, PASS): 0 issues — zip rules, XML well-formedness of every doc, manifest/spine closure, image/CSS reference resolution, remote-resource ban, nav completeness vs spine, NCX navPoints vs spine.

> epubcheck could not be executed in the build environment (no Java runtime available; package installs blocked). Structural validation above is the compensating control; recommend a final epubcheck run in any Java-capable environment before distribution (expected result: clean, or trivial warnings only).

## Reflow features

- em/% typography, no fixed page geometry; images `max-width:100%`
- MCQ options as list items (jammed source options were split during parsing; verified absent)
- pronunciation lines (/IPA/, stress respellings) preserved verbatim
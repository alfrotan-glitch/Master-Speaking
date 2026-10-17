# Speaking Class Companion — QA

Date: 2026-10-17

## Scope

New, clearly labelled supplementary teaching material. Creating the companion did not change the original book files. A subsequent October editorial revision updated the book exports and semantic master separately; see PUBLICATION-READINESS.md. The original manuscript remains unchanged. No video transcripts, missing manuscript exercises, or source-based answer keys have been invented.

## Checks performed

- Rebuilt PDF and Word from `book/companion/speaking-class.md` using `book/tools/companion.py`.
- `python book/tools/qa_companion.py`: PASS. All 183 source blocks found in both exported formats after whitespace normalization; eight unit outcomes present; all 15 numbered sections start on fresh PDF sheets; all PDF text spans fit the checked page boundaries.
- PDF: 17 A4 pages, embedded local Source Sans 3 fonts, page numbers and supplementary-material footer.
- Visually inspected a rendered sample during layout development: legible typography, teal section headings, comfortable margins. Full final-edition visual inspection and native Microsoft Word rendering have not been performed.
- Eight unit titles checked against `book/artifacts/book.json`.
- Lesson A timing: 7 + 10 + 8 + 8 + 12 + 7 + 15 + 8 = 75 minutes.
- Lesson B timing: 8 + 10 + 18 + 8 + 15 + 10 + 6 = 75 minutes.
- Rubric: five dimensions, four descriptors each, 5–20 complete score range, missing evidence handled as N/O. Interaction requires an exchange, not only a monologue.

## Teaching safeguards and limitations

Includes fictional scenarios, neutral alternatives for sensitive topics, no compulsory personal disclosure, consent-based recording, no-device practice, and support/extension options. Classroom assessment is explicitly not CEFR certification or a standardized TOEFL measure. Scenarios and imaginary budget figures are labelled as invented teaching data. Activities have not yet been trialled with a live class; teachers should adapt pacing, language difficulty, and access arrangements after the entry task.

No new audio, video, or external research sources were added. The companion can be used offline but does not substitute invented material for the book’s original listening inputs. Word appearance can vary with fonts and the local Word version. Automated checks verify content presence and boundaries, not pedagogical effectiveness or every aspect of pagination.

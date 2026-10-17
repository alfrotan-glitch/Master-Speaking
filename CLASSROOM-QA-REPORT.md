# Classroom Implementation Packs — QA & Scope

17 October 2026

## Deliverables

- `Master-Speaking-Student-Practice-Pack.pdf` / `.docx`: **18 pages** in the PDF; 489 authored/generated source blocks.
- `Master-Speaking-Teacher-Implementation-Pack.pdf` / `.docx`: **18 pages** in the PDF; 339 source blocks.
- Authored sources: `book/classroom/modules.json`, `unit1-reading-key.json`, and `teacher-notes.md`.
- Rebuild: `python book/tools/classroom.py`; verify: `python book/tools/qa_classroom.py`.

The existing main book remains separate. The shared supplementary exporter now supports secondary headings, PDF navigation bookmarks, and an optional compact handout layout. The earlier Class Companion still exports to 17 pages and passes its existing 183-block check.

## Recommendation coverage

| Recommendation | Delivered | Still outstanding |
|---|---|---|
| Dependable listening input | Eight original fictional teacher-read alternatives, matching student worksheets, five detail questions each, gist prompts, and evidence-linked teacher keys | Exact original video identification, permissions, question alignment, and any recorded audio |
| Teacher answer support | Fifteen source-linked Unit 1, Chapter 1 items: five vocabulary, five MCQ, five suggested open reading answers; directions for open speaking tasks | Original-book reading keys for Units 2–8 and verified original-video keys |
| Models and success criteria | Eight six-turn exchanges, eight short responses, 32 chapter checklists with 64 observable can-do statements, language frames, and transfer tasks | Independent review and classroom evidence of difficulty and usefulness |
| Pilot and revision | Four complete 75-minute Unit 1 lesson plans, observation prompts, student feedback, and revision record | Actual teaching, learner feedback, and measured observations; no trial results are claimed |

The Unit 1 pilot is intentionally four meetings, not the companion’s shorter two-meeting unit route. Teachers should use observed timings to select a course schedule rather than implying both routes cover identical work in identical time.

## Automated checks performed

`book/tools/qa_classroom.py` passes:

- All eight unit titles and sequence match the current semantic book.
- Each unit has four chapter checklists with two can-do statements each, a six-turn exchange, a short response, and three language frames.
- All eight scripts are unique, 100–180 words, and excluded from the student pack.
- Each alternative has exactly five distinct detail questions with nonempty answers. Every quoted evidence phrase occurs in the matching script.
- The Unit 1 reading key covers the current chapter’s complete five-item vocabulary exercise, five MCQ stems, and five open reading questions. Stems and evidence match the semantic source; MCQ letters and answer text match actual options. Open answers remain suggested content rather than fixed wording.
- Every pilot schedule begins at minute 0, ends at 75, and has contiguous non-overlapping activity intervals.
- All source blocks occur in both PDF and Word exports. All numbered sections start on fresh PDF sheets. PDF text spans fit the checked page boundaries, and every major section has a PDF navigation bookmark.
- Teacher scripts and key labels are not exposed in the student export.

Machine results: `book/artifacts/qa_classroom.json`. The script checks internal consistency and export integrity, not learning effectiveness or whether every acceptable answer has been anticipated.

## Editorial and visual checks

- Scripts are explicitly labelled new fictional alternatives, not recovered transcripts or research evidence.
- Speaking models are short demonstrations, not promises to satisfy the book’s full timed assignments. The Unit 1 dialogue is explicitly a starter rather than the original ten-expression activation task.
- The Unit 1 key allows both “express” and “communicate” where the sentence permits them. Accurate paraphrases are accepted for open questions.
- Neutral examples, privacy choices, consent-based recording, transcript access arrangements, and alternatives to compulsory eye contact are included.
- Selected student checklist/model pages, a listening worksheet, and teacher script/key pages were rendered and inspected. The first student layout spilled only a few language frames onto a mostly empty page; spacing was revised without reducing text size, producing one unit model/checklist sheet plus one listening sheet per unit.
- A complete independent human proof and a live classroom trial remain outstanding. Font appearance and pagination in native Word may vary by environment.

## Correct use of the new listening route

Read the new script, distribute its matching student worksheet, then use its own key. Do **not** use these answers to mark the original book’s video exercises, and do not record those original exercises as completed. `book/publishing/media-register.csv` remains UNVERIFIED; `listening-alternatives.csv` separately records the new teacher-read route and explicitly states that no recorded audio or live pilot results are supplied.

The original author-supplied manuscript and main book exports were not revised to incorporate these supplementary materials in this step. New material is clearly separated for teacher control and student printing.

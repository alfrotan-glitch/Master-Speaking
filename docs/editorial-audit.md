# Editorial Audit & Full Publication Rewrite — *Grammar for Special Speaking* (TOEFL HOUSE)

## 1. Executive Summary

This audit records the complete editorial, instructional, and typographic rebuild of **TOEFL HOUSE — *Grammar for Special Speaking*** (both the **Student Book** and the **Teacher's Book**).

### Core Editorial & Pedagogical Transformation
1. **One Unified Classroom (No Track Splitting)**:
   - Removed all student-facing proficiency-track divisions (`Intermediate — build accuracy` / `Advanced — build flexibility`) and level labels (`Intermediate`, `Advanced`, `Beginner`) from the Student Book.
   - Replaced the student-facing heading `Part 6 · The Advanced Upgrade` across all 16 lessons, front matter, and Teacher's Book guides with **`Part 6 · Say It with Greater Precision`**, framed as a whole-class progression from automatic core control (`Make the core pattern automatic`) to richer nuance, detail, and rhetorical focus (`Add nuance, detail, and sharper focus`).
   - Removed teacher-only guidance and internal pipeline/QA notes from the Student Book front matter so the Student Book speaks directly to learners from cover to cover.
2. **Narrative, Prose-First Lesson Architecture (Lessons 1–16)**:
   - Added a two-paragraph **real-life situational opening** (`intro`) to every lesson that shows why the grammar choice matters in authentic spoken moments before any rule is stated.
   - Rewrote **`Part 1 · The Speaking Hook`** across all 16 lessons to pair concrete side-by-side spoken contrasts with immediate personal speaking questions.
   - Rewrote **`Part 2 · The Simple Rule`** across all 55 rule blocks in Lessons 1–16 so that every rule begins with clear, plain-English prose explaining *how the pattern works and why speakers choose it*, followed by a single consolidated callout box (`Pattern:` · `Natural examples:` · `Keep in mind:`) instead of three fragmented boxes per rule.
   - Expanded **`Part 3 · See the Difference`** with explanatory prose intros and a third column (*What your listener hears* / *How the story changes*) in contrast tables.
   - Added a realistic 3-turn **partner model exchange** (`How it sounds in conversation:`) to **`Part 5 · Pair Speaking`** in all 16 lessons alongside `Your conversation goal:` and `What makes this conversation work:`.
   - Rewrote **`Part 7 · Real Talk Challenge`** and **`Part 8 · Review and Self-Check`** with natural spoken model responses, numbered `Quick answers (Practice A & B)`, and active-recall reflection checks.
3. **Teacher's Book Rebuild**:
   - Rewrote `build_spec/teacher_front.py` and `build_spec/teacher_render.py` to support a unified mixed Special Speaking classroom (`Supporting developing speakers within the shared task` and `Stretching confident speakers toward deeper precision`).
   - Aligned all 16 lesson guides (`teacher_l1_8.py`, `teacher_l9_16.py`, `teacher_l13_16.py`) with `Part 6 · Say It with Greater Precision`, fixed the stray CJK characters (`同伴` → `pair`) in Lesson 2, fixed the broken string in Lesson 12 (`T12['assess']`), and expanded shorthand notes into clear classroom guidance.
4. **Visual Hierarchy, Page Flow & Cross-Format Fixes (`tools/build_publication.py`, `style.py`)**:
   - Fixed PDF title page rendering so title-page typography honors centered alignment, display font sizes (28pt / 22pt / 14pt), and vertical spacers.
   - Fixed PDF multi-column table width calculation to read `table.rows[0].cells[i].width` from DOCX so custom column proportions render accurately.
   - Eliminated clipped 1-row callout boxes at page bottoms (`splitInRow=0` on short/medium callout boxes) and prevented orphaned section banners (`Part X · ...`) and rule subheadings (`Rule X — ...`) by binding headings to their following content block with `KeepTogether` and `Heading 3` (`keep_with_next=True`).
   - Removed the duplicate page break before Lesson 1 in the Teacher's Book and stripped trailing spacers before page breaks, eliminating blank and sparse pages across both volumes (Student Book PDF: 100 A4 pages; Teacher's Book PDF: 58 A4 pages; zero orphaned headings or sparse pages).

---

## 2. Preserved Syllabus, Scope & Linguistic Safeguards

All approved syllabus and linguistic accuracy requirements are preserved and verified by `build_spec/qa.py` and `tools/validate_publication.py`:
- **16 Lessons in 8 Parts**:
  1. *Tenses for Real Communication* (3 core rule groups; 5 Practice A + 4 Practice B items; present perfect continuous in Part 6)
  2. *Telling Stories and Describing Experiences* (6 + 6 practice items)
  3. *Questions, Auxiliary Verbs, and Follow-up Questions* (6 + 6 practice items; qualified direct-question auxiliary rule)
  4. *Modal Verbs for Real-Life Situations* (6 + 6 practice items; `mustn't` vs `can't be` deduction contrast)
  5. *Conditionals for Decisions and Possibilities* (6 + 6 practice items; qualified `will` in `if`-clauses for willingness/refusal)
  6. *Wishes, Regrets, and Hypothetical Situations* (6 + 6 practice items)
  7. *Comparisons Beyond the Basics* (6 + 6 practice items; natural comparative vs superlative framing)
  8. *Linking Ideas and Building Arguments* (6 + 6 practice items; no ungrammatical `Although being...`)
  9. *Passive Voice in Natural English* (6 + 6 practice items; active vs passive with `by`-agent note)
  10. *Causative Structures* (6 + 6 practice items)
  11. *Gerunds and Infinitives* (6 + 6 practice items; `mind + -ing` note)
  12. *Relative Clauses and Concise Descriptions* (6 + 6 practice items)
  13. *Reported Speech and Reporting Verbs* (6 + 6 practice items)
  14. *Participles and Advanced Sentence Patterns* (6 + 6 practice items; reduced vs absolute participle clause distinction)
  15. *Hedging, Emphasis, and Natural Inversion* (6 + 6 practice items; hedging nuance note)
  16. *Grammar in Real Conversation* (6 + 6 practice items; four-job integration and live self-repair)
- **Assessments & Reference Appendices**:
  - Diagnostic Test (25 written items + baseline speaking task)
  - Review Tests 1, 2, and 3 (strictly scoped after Lessons 4, 8, and 12 with zero untaught grammar leakage)
  - Final Assessment (30 written items mapped across all 16 lessons in `docs/final-assessment-coverage.md` + Part 2 speaking task, 4-criterion rubric, and personal error analysis plan)
  - Appendices 1–5 (Grammar Formula Book, Common Errors Guide, Essential Sentence Patterns, Can-Do Tracker, and Complete Answer Key with legitimate grammatical alternatives)

---

## 3. Verification Summary

- `.venv/bin/python build_spec/qa.py` — **ALL QA GATES PASS** (71/71 checks across Student Book and Teacher's Book).
- `.venv/bin/python tools/validate_publication.py` — **ALL CHECKS PASS** across Student Book and Teacher's Book DOCX, PDF, EPUB, and HTML deliverables.
- Note on EPUBCheck: Java / `epubcheck` is not installed in the build container; `tools/validate_publication.py` verifies ZIP structure, `mimetype` placement, XML well-formedness, OPF manifest/spine, NCX/Nav documents, internal fragment links, and EbookLib parse integrity, and explicitly reports that `epubcheck` is not installed.

# Editorial audit and prioritized revision log

**Edition reviewed:** source regenerated from `build_spec/` on 2026-10-19 (Student Book + Teacher's Book). Lesson/section references are used because Word pagination changes by rendering engine; PDF page references below refer to the current generated PDFs (Student Book 76 pages, Teacher's Book 60 pages). This is an internal editorial pass, not independent expert approval or classroom evidence.

## What changed in this pass (2026-10-19)

- **Student Book — Lesson 1 approved revision:** present-simple and present-continuous merged into one present-tenses group (three core rule groups total); controlled practice corrected to five A items and four B tasks; Pair Speaking now carries explicit expected speaking output; Real Talk Challenge separated as a planning-and-transfer task with its own planning instructions and model response; present-perfect continuous and emphasis patterns kept optional in the Advanced Upgrade; Review links back to the Simple Rule and Appendix card when a self-check item is unticked.
- **Student Book — all 16 lessons:** every Pair Speaking now states the expected speaking output; every Real Talk Challenge now has separate planning guidance and a model response (clearly labelled as one example, not the only answer); Review now gives a return-to-rule reference. Speaking-section headings are prevented from stranding at page bottoms via keep-with-next layout. Automated QA gates were added for the Lesson 1 revision, expected output, Real Talk separation, and heading flow.
- **Student Book — front matter:** added a formal copyright and publication-information page (© TOEFL HOUSE, 2026; placeholders for ISBN/edition/place identified explicitly; disclaimer and statement of limits) and a Teacher's Book cross-reference.
- **Teacher's Book (new):** 16 companion lesson guides generated from the same lesson sources as the Student Book, guaranteeing identical objectives, practice items, answers and model responses. Each guide contains: outcomes and measurable success criteria, materials/preparation, 60-minute timing that matches the Student Book's pacing blocks (every lesson totals exactly 60), step-by-step procedures for all eight functions, checking-understanding prompts, complete Practice A/B answers with explanatory notes, acceptable alternatives, model exchanges and model responses, assessment guidance for open-ended tasks, Intermediate scaffolding, Advanced extension, common errors with correction strategies, shorter-session (45-minute) adaptations, and review/consolidation guidance with feedback-without-interrupting-fluency instructions. Back matter adds a model final speaking response and keys for the Diagnostic, three Review Tests and Final Assessment.
- **Publication:** both books now build from a single reproducible pipeline to DOCX, PDF, EPUB and HTML; both PDFs are searchable A4 with embedded fonts, page numbers and bookmarks; both EPUBs pass package/XML/link checks; both HTMLs are semantic and navigable.

## Prioritized issue list

1. **Major — Review Test 1 exceeded its taught scope.** It assessed the second conditional (Lesson 5) and *despite* (Lesson 8) before those lessons. Removed both leaks and replaced them with Lesson 4 modal targets. Automated scope regression now checks for them.
2. **Major — Review Test 2 contained a dangling modifier in its model answer.** “Despite being hard, everyone passed the exam” grammatically attaches *being hard* to *everyone*. Changed to “Despite the exam being hard, everyone passed” / “Despite the difficulty, everyone passed.”
3. **Major — the diagnostic and final raw scores were presented as directly comparable.** The tests have different lengths and item blueprints. Reframed the grammar diagnostic as a starting snapshot and prohibited raw-total gain claims. Added a matched baseline/final speaking interaction using the same prompts, timing, and rubric; see `docs/final-assessment-coverage.md`.
4. **Moderate — test answers were printed immediately below the test items.** Removed the visible keys from the diagnostic, review tests, and final assessment; the complete keys remain in Appendix 5 so learners can finish first.
5. **Moderate — answer keys hid valid alternatives.** Added acceptable choices for present-perfect aspect, relative pronouns, modal probability, causative *get*, present-tense reported facts, and participial openings; also made the diagnostic prompts more specific where a tense choice needed a cue.
6. **Moderate — several simplified rules sounded absolute.** Qualified “recently” with present perfect/past simple; ordinary future *if*-clauses versus willingness *will*; comparative/superlative meaning; modal certainty groupings; passive agent omission; the subject of reduced participle clauses; and *wish I were/was*. These revisions preserve an accessible core rule while identifying real variation.
7. **Moderate — production/navigation was incomplete.** Added Word heading styles, dynamic PDF contents/bookmarks/page numbers, a reflowable EPUB build and package checks, writable space in the final error-analysis table, and explicit reproducible build/validation documentation.
8. **Pending external work — qualified teacher review, a learner pilot, EPUBCheck, and a rendered Word/print proof.** Instruments are in `docs/teacher-review-checklist.md` and `docs/pilot-feedback-form.md`. No reviewer results, learner results, or learning gains are claimed.
9. **Medium — no Teacher's Book existed.** Added the companion Teacher's Book volume with identical lesson sources, full answer keys with notes, model speaking responses, timing, differentiation and assessment guidance. Both books share one build pipeline.

## Ten-angle findings and corrections

### 1. Grammar accuracy and linguistic authority

- **Major finding — Lessons 1, 5, 6, 7, 9, 11, 14 and 15, Simple Rule / Remember / Review.** Several useful teaching shortcuts could be read as absolute statements: all uses of *recently* taking present perfect; *will* never occurring in an if-clause; comparatives being only for two and superlatives only for three or more; a fixed certainty ranking; “mind always” taking -ing; and every participle clause sharing the main-clause subject. Lesson 9 also described the passive as hiding the agent without noting the agent can be stated.
- **Why it mattered:** learners could reject grammatical alternatives or carry oversimplified rules into real conversation.
- **Correction:** added conditions and contextual examples in Lesson 1; scoped the conditional rule in Lesson 5 and Appendix 1; refined Lesson 6’s *were/was* and *wish + would* notes; reframed Lesson 7 around comparison of choices versus extremes in a group; clarified the passive’s agent in Lesson 9; limited the *mind + -ing* statement to direct verb complements in Lesson 11; distinguished reduced participial clauses from absolute clauses in Lesson 14; replaced Lesson 15’s linear certainty “scale” with meaning-based groups. Lesson 8’s clause pattern remains “Although it was difficult…” versus “Despite the difficulty…”.
- **Verification:** source regression checks, answer-key alignment, final build, and searchable PDF text checks passed. Review Test 2’s corrected concession answer is specifically regression-checked.
- **Severity:** Major for the conditional and test-key defects; Moderate for qualification of usage explanations.
- **Remaining risk:** these edits are an editorial review, not a signed-off review by a qualified grammarian; regional usage judgments still need external review.

### 2. Intermediate and Advanced learner suitability

- **Moderate finding — all Lessons 1–16, Part 6 “The Advanced Upgrade.”** The source has separate `base` and `upgrade` tasks for every lesson, but no CEFR claim should be inferred from the labels alone, and an exercise count by itself does not establish appropriate challenge.
- **Why it mattered:** a mixed class needs supported accuracy work and an actual increase in flexibility, not just more prompts.
- **Correction:** preserved the shared core and distinct Intermediate accuracy / Advanced flexibility tasks. The audited Lesson 1 sequence moves from time-cue practice to using present-perfect continuous and combining past simple with present perfect; Lesson 8 moves from sorting linker families to concessive balance and clause-commenting *which*; Lesson 16’s Advanced tasks stack structures and include repair phrases.
- **Verification:** source-data gates confirm both pathways are present for all 16 lessons, and the lesson/answer counts align. Teacher checklist asks reviewers to judge level suitability directly.
- **Severity:** Moderate.
- **Remaining risk:** suitability for the actual TOEFL HOUSE cohort and the balance between different Intermediate/Advanced learners require a teacher review and pilot.

### 3. Speaking development and communicative value

- **Moderate finding — Lessons 2, 3, 8, 10, 13, 16, Pair Speaking and Real Talk.** The existing tasks already ask learners to tell stories, interview, debate, negotiate services, report conversations, and repair speech. The final assessment, however, was only a prepared monologue and did not directly sample the Lesson 16 follow-up/repair objective.
- **Why it mattered:** grammar for speaking must be observable in responsive use, not just written transformations.
- **Correction:** kept the existing pair/group tasks and added two partner follow-up questions, a return question, and a repair instruction to both baseline and final speaking samples. The same four-criterion rubric is printed with both.
- **Verification:** source QA checks for both exchanges and the shared criterion; the PDF rubric and prompt were rendered and visually inspected (current PDF pp. 6 and 59).
- **Severity:** Moderate.
- **Remaining risk:** no learner recordings or classroom observations exist, so task duration, participation balance, and rubric reliability remain untested.

### 4. Syllabus architecture and progression

- **Moderate finding — front matter, contents, Lessons 1–16, and tests.** The manuscript’s 16 lesson topics and eight thematic Parts match the approved sequence. The original diagnostic/final comparison language did not reflect different test lengths and blueprints.
- **Why it mattered:** learners and teachers need a dependable progression and an honest way to interpret assessment.
- **Correction:** retained all 16 syllabus titles and thematic Parts; retained tests after Lessons 4, 8, and 12; changed assessment interpretation and added the final item-level coverage map. No eight-week labels were introduced.
- **Verification:** QA checks title/order, test placement and scope, 16 lesson components, and matrix coverage; the PDF contents page (current p. 4) has page references.
- **Severity:** Moderate for assessment interpretation; no syllabus replacement was needed.
- **Remaining risk:** actual pacing still depends on class length and learner needs; pilot feedback should inform timing.

### 5. Exercise quality, keys, and assessment validity

- **Major finding — Review Test 1, Review Test 2, Diagnostic Test, and Final Assessment.** Test 1 previously tested a second conditional and Lesson 8 *despite* before either topic was taught. Test 2’s model answer had a dangling modifier. The diagnostic key omitted legitimate alternatives, diagnostic/final raw totals were described as a gain measure despite different lengths (25 vs 30 items), and answer keys appeared directly after assessment items.
- **Why it mattered:** premature targets and unreliable keys mis-score learners; mismatched raw totals cannot support a defensible gain claim.
- **Correction:** removed the two Test 1 leaks; corrected the Test 2 answer; moved diagnostic/review/final keys to Appendix 5; expanded legitimate alternatives; revised baseline/final score guidance; added matched speaking conditions and a written item-level coverage matrix for all lessons.
- **Verification:** QA verifies all test positions and forbidden later-lesson grammar, checks controlled-practice/key item counts, checks the 16-row coverage matrix, and asserts the raw-total caveat and matched speaking instructions. The current final assessment is PDF pp. 58–59.
- **Severity:** Major.
- **Remaining risk:** the matrix is a blueprint, not empirical evidence of reliability, difficulty, inter-rater agreement, or learning gains. Qualified teacher review remains pending.

### 6. Textbook writing and editorial quality

- **Moderate finding — Introduction, Lessons 1, 5–7, 9, 11, 14–15, and Appendix 1.** Some explanations used overly categorical language; the Introduction also described each lesson as teaching “one clear rule,” although many lessons teach several related patterns.
- **Why it mattered:** a confident, simple tone should not turn tendencies or context-dependent forms into false rules.
- **Correction:** the Introduction now says “clear grammar patterns”; the usage qualifications above were added. **Editorial house style:** British English spelling is the default in explanatory prose (*practise* as a verb, *practice* as a noun, *organise*, *behaviour*, *apologised*, *cancelled*). Natural US variants are acceptable and may appear where relevant; examples preserve punctuation needed to illustrate the target construction. Headings use sentence-style wording except branded/title banners; exercises use numbered prompts and answer keys preserve alternatives.
- **Verification:** generated source and outputs were text-extracted and checked; known absolute-claim regressions are in automated QA. No spelling-tool result is treated as a grammar verdict.
- **Severity:** Moderate.
- **Remaining risk:** detailed line editing by a second human editor is still advisable before commercial publication.

### 7. Lesson design and teacher usability

- **Moderate finding — all Lessons 1–16, all eight functional parts.** The shared framework was present; the project needed stronger evidence that each component had actual prompts, criteria, both pathways, an independent challenge, and a self-check rather than a heading only.
- **Why it mattered:** a teacher should be able to run pair work and observe target-language use from the page.
- **Correction:** retained the framework and its variation by topic; added an explicit matched final speaking exchange and enlarged the final written error-analysis rows for handwritten use.
- **Verification:** automated source gates inspect all eight non-empty lesson functions and practice/answer-key counts; teacher checklist covers classroom pacing, naturalness, and key reliability. PDF p. 59 was inspected at page scale.
- **Severity:** Moderate.
- **Remaining risk:** classroom feasibility, interaction timing, and handwriting space need real teacher/pilot confirmation.

### 8. Visual design, accessibility, and print quality

- **Moderate finding — whole book, contents, final rubric, tests, and appendices.** The original DOCX used a restrained palette and A4 geometry but did not supply generated PDF page navigation or page-numbered contents; Word’s semantic navigation needed verification.
- **Why it mattered:** a usable book needs page references, a navigable structure, readable tables, and clear monochrome-safe distinctions.
- **Correction:** preserved the navy/teal/gold/grey print-friendly system; added Word Heading 1/2 styles, a native updateable Word contents field, A4 output, PDF page numbers/bookmarks and live contents, repeatable table headers, and writable blank rows. Meaning is signalled by labels and structure as well as fill colour.
- **Verification:** Student Book PDF rendered and visually sampled at the title, contents (p. 6), copyright page (p. 2), diagnostic test, matched baseline speaking task/rubric, Lesson 1 (Rule 1 now shows the merged present-tenses group), Review Test 1, final written assessment, final speaking rubric/writing table, answer key, and end. PDF structure confirms 76 A4 pages and 26 bookmarks; Teacher's Book PDF confirms 60 A4 pages and 16 bookmarks. Both DOCX files have semantic headings, A4 dimensions and an updateable TOC field.
- **Severity:** Moderate.
- **Remaining risk:** the Word document itself was not rendered in LibreOffice/Word because neither was installed; manual grayscale and physical print proofing remain pending.

### 9. Ebook engineering and cross-format consistency

- **Major finding — distribution pipeline.** The repository initially contained a DOCX and HTML, but no PDF or EPUB.
- **Why it mattered:** HTML renamed as EPUB would not meet ebook-reader navigation or package requirements.
- **Correction:** created a searchable PDF with embedded DejaVu fonts, A4 page numbers, live page-numbered contents, and bookmarks; created a reflowable EPUB package with metadata, navigation, XHTML and CSS; copied the editable DOCX to `dist/` with semantic headings. Final names are linked in the README.
- **Verification:** Python structural validator opens all files, checks required section markers across editions, checks PDF dimensions/text/bookmarks, parses EPUB XML and manifest/spine/nav, resolves internal links, and opens the EPUB with EbookLib for both books. Visual inspection sampled both PDFs as listed above.
- **Severity:** Major at baseline; production now exists.
- **Remaining risk:** EPUBCheck and an actual dedicated reader were unavailable. The package checks are **not** an EPUBCheck certification. Word/LibreOffice visual rendering is also pending.

### 10. Maintainability and reproducibility

- **Moderate finding — `build_spec/`, `tools/`, `README.md`, `dist/`.** Prior to this revision, the documented workflow did not regenerate all three formats from a clean environment and final QA did not verify the new ebook/print packages.
- **Why it mattered:** the outputs must be reproducible after further content changes.
- **Correction:** kept the lesson source data and existing Python DOCX architecture; added production dependencies and `tools/build_publication.py`, `tools/validate_publication.py`, source QA gates, a clear requirements file, and build/validation commands. `dist/` is intentionally not ignored; `.venv/`, `.qa/`, and temporary `build/` are ignored.
- **Verification:** clean virtual environment installation succeeded; the full build and both QA commands passed in this environment. Commands are recorded in the README and final report.
- **Severity:** Moderate.
- **Remaining risk:** PDF generation requires installed DejaVu Sans system fonts; EPUBCheck, Word/LibreOffice page rendering, external teacher review, and learner pilot are not included in the Python dependency set.

## Editorial and validation policy

- British English is the default editorial spelling; accepted US variants are not grammar errors.
- A model answer is an example, not an exclusive key, unless the exercise explicitly constrains the target structure. Legitimate alternatives remain accepted.
- Automated checks establish structure, presence, package integrity, and regressions—not expert approval, classroom effectiveness, or learner gains.
- Teacher review and learner pilot are **pending**. Record results only when actual participants complete the supplied forms.

# Grammar for Special Speaking — TOEFL HOUSE

**Authoritative manuscript:** `Grammar for Special Speaking (TOEFL House).docx` (editable master)  
**Distribution edition:** `dist/Grammar for Special Speaking (TOEFL House).html` (print/digital-friendly)  
**Build system:** `build_spec/` — regenerates both the manuscript and its QA gates.

> **Learn the grammar. Use it in conversation. Make it part of your speech.**

## Reproduce the deliverables (tested commands)

```bash
python3 -m venv .venv
.venv/bin/pip install -r build_spec/requirements.txt
.venv/bin/python build_spec/build.py      # rebuilds the .docx manuscript
.venv/bin/python build_spec/qa.py         # 42 automated QA gates (exit 0 = pass)
.venv/bin/pip install mammoth             # for the HTML distribution edition
.venv/bin/python tools/build_html.py      # rebuilds dist/*.html
```

Verified on Python 3.11 with the requirements above. A clean checkout plus these
commands rebuilds the manuscript from `build_spec/` sources (content-identical; the
.docx container itself embeds build timestamps).

## Book structure

- **Front matter** — title, introduction & objectives, how to use (students & teachers,
  two learning pathways, suggested lesson pacing), contents, diagnostic test (25 items)
- **16 lessons** in 8 thematic parts — each with the standard framework:
  1. The Speaking Hook · 2. The Simple Rule · 3. See the Difference · 4. Practice the Pattern
  5. Pair Speaking · 6. The Advanced Upgrade · 7. Real Talk Challenge · 8. Review and Self-Check
- **Two pathways in one classroom** — Intermediate (Build Accuracy) + Advanced (Build Flexibility)
- **3 cumulative review tests** (after Lessons 4, 8, 12) + **Final Assessment**
  (30-item grammar test + independent speaking task, rubric, error analysis & improvement plan)
- **5 appendices** — Formula Book · Common Errors & Corrections Guide · Essential Sentence
  Patterns · Speaking Self-Assessment & Can-Do Tracker · Complete Answer Key

## Automated QA (`build_spec/qa.py`)

Gates include: 16 lessons × 8-part framework; lesson titles match the specification exactly;
document order and review-test placement; review-test scope (no untaught grammar leaks);
final-assessment coverage of all 16 lessons; answer-key completeness; banned-language checks
(no scheduling words, no Master Speaking references, no unearned claims); design restraint.

Answer keys are generated from the same source data as the exercises, so keys cannot drift.

## Rendering and inspection status (honest)

| Format | Status |
|---|---|
| `.docx` master | Structurally inspected: A4, margins, footer page numbers, font consistency (Calibri/Consolas), table widths within text area, page breaks |
| `.html` edition | Generated with Mammoth; content integrity verified (16 lessons, tests, appendices present); **not** visually pixel-rendered |
| `.pdf` | **Not produced** — no Word/LibreOffice/pandoc in this environment. Export from the .docx in Word (File → Save as PDF) for final print QA |

## External validation still required

Per the specification (§12), the following require people outside this repository and have
**not** been completed:

- Review by qualified English teachers → use `docs/teacher-review-checklist.md`
- Piloting with actual learners → use `docs/pilot-feedback-form.md`
- Visual print QA of the Word/PDF output on paper

## Repository contents

- `Grammar for Special Speaking (TOEFL House).docx` — the book (single authoritative manuscript)
- `dist/` — HTML distribution edition
- `build_spec/` — build system + automated QA
- `docs/` — teacher review checklist and pilot feedback form (blank instruments)
- `archive/` — superseded earlier edition (reference only)
- `Master Speaking.docx` — separate product; the grammar book is fully independent of it
- `tools/` — one-off utilities from earlier development stages

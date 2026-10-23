# Manuscript scope and publication-release gates

## Two different deliverables live in this repository

1. `Master Speaking.docx` is a distinct, approximately 6 MB legacy/original manuscript at the repository root. It is **not** rebuilt, proofread or validated by the `build_spec/` pipeline. Its editorial status must be established from a complete document inspection; no claim of completeness or quality is implied by the grammar book's checks.
2. `Grammar for Special Speaking` has a maintained, structured 16-lesson Student Book and companion Teacher's Book. `build_spec/` is the authoritative source; `dist/` holds the published output formats. These editions have 16 grammar-oriented speaking lessons, diagnostic, three cumulative reviews, final assessment and appendices.

Do **not** confuse these products or silently replace one with the other. The student-facing grammar edition serves a single shared classroom without proficiency labels inside activities. Differentiation stays in the teacher guidance.

## Release acceptance criteria

- **Source/content:** review every lesson for grammatical accuracy, natural spoken English, answer-key alternatives, communicative purpose, balanced teacher/learner speaking time and the distinction between rehearsal and spontaneous speaking.
- **Assessments:** no out-of-scope review questions, no answer leakage, complete coverage, stable instructions, genuinely observable criteria and baseline/final caveats.
- **Build:** regenerate both editions from source. All files in `dist/` must match that source; the root working DOCX files must match their distributed copies.
- **Formats:** run `python build_spec/qa.py` and `python tools/validate_publication.py` against the newly generated DOCX/PDF/EPUB files. Perform EPUBCheck separately when available. Do not represent custom ZIP validation as EPUBCheck.
- **Visual/accessibility proof:** inspect actual PDF and DOCX rendered pages, table breaks, TOC links, fonts, contrast and EPUB navigation; take a physical A4 print proof before commercial printing.
- **Human evidence:** record qualified teacher feedback, trial the activities with actual learners, correct observed problems and record a release decision. A passing automated test is not proof of learning effectiveness.
- **Legacy Master Speaking:** perform its own full-text, copyrighted-material, image-rights, structure, language, layout, assessment and format audit **before** calling that independent document complete.

## Reproducible workflow

After modifying `build_spec/`, run:

```bash
python -m pip install -r build_spec/requirements.txt
python tools/build_publication.py --all
python build_spec/qa.py
python tools/validate_publication.py
```

The editorial branch workflow also builds and checks the editions in a clean Linux runner, and commits the regenerated book files to the editorial branch if its validations pass. The published files must not be claimed updated until that commit exists.

## Remaining limits

No independent classroom trial, signed expert review, ISBN assignment, professional Word print proof, verified EPUBCheck result, or complete audit of `Master Speaking.docx` is established by this repository-level improvement alone. These are release gates, not defects to conceal.

# Master-Speaking

Course books by **The TOEFL House** (Kabul).

## Books in this repository

### 1. Master Grammar C1-C2 (TOEFL House).docx
**The complete English grammar book (C1–C2)** — a standalone, original grammar course
written from zero for the special Speaking class, following the **Destination C1 & C2
grammar syllabus**.

**Course design: 2 months · 8 weeks · 2 days per week = 16 teaching days**

| Month | Weeks | Days | Focus |
|-------|-------|------|-------|
| Month 1 | 1–4 | Days 1–8 | Building the Grammar Core |
| Month 2 | 5–8 | Days 9–16 | Mastering Style & Precision |

| Week | Grammar Area | Days |
|------|--------------|------|
| 1 | Tenses & Time | 1–2 |
| 2 | Future & Modals | 3–4 |
| 3 | Conditionals & Emotion | 5–6 |
| 4 | Deduction & Comparison | 7–8 |
| 5 | Passive & Hypotheticals | 9–10 |
| 6 | Reported Speech & Verb Patterns | 11–12 |
| 7 | Clauses & Connectors | 13–14 |
| 8 | Style & Precision | 15–16 |

Every teaching day contains 10 sections: Speak First → Grammar Focus → How We Really
Say It → Common Mistakes → Practice → Pronunciation Clinic → Speak! → TOEFL-Speaking
Task → Homework & Self-Check → **Grammar at a Glance** (golden recap + one golden
sentence pattern).

**THE MASTER METHOD — the unique learning system of the book** (Grammar is Math,
Story, Music, Habit & Garden):
1. **Formula Cards** — every structure as a math formula (code-style, one per day; all 16 collected in "The Formula Book", Appendix D)
2. **Memory Hooks** — one unforgettable mnemonic image/story per day (The Open Door, The Magic IF-BOX, The Three Clocks, The Rooftop…)
3. **The Say-It Engine** — every example in 3 passes: Clear → Contracted → Fast
4. **The 15-Minute Daily Loop** — Learn (5) → Lock (5) → Live (5)
5. **The Review Calendar** — spaced repetition on days +1, +3, +7, +16
Plus the **Mistake Killer Protocol** and 16 **Golden Patterns** (one sentence frame per day that contains the whole book).

**Built-in assessment system:**
- **Diagnostic Test** before Day 1 (30 items + score guide)
- **Progress Tests 1–3** after Days 4, 8 and 12 (15 items each)
- **Final Written Test** after Day 16 (30 items covering the whole C1–C2 system)
- Full answer keys for every exercise and every test in the appendices,
  plus a Grammar Toolkit (connectors, hedges, reporting verbs) and a Can-Do Checklist

| Day | Grammar Focus |
|-----|---------------|
| 1 | Present Perfect & Past Simple |
| 2 | Past Tense Contrast |
| 3 | The Future in Spoken English |
| 4 | Modals — Advice, Obligation & Necessity |
| 5 | Zero, First & Second Conditionals |
| 6 | Wish, If Only, It's Time, Would Rather & As If |
| 7 | Modals of Deduction, Regret & Criticism |
| 8 | Comparison & Contrast |
| 9 | The Passive Voice & the Causative |
| 10 | Third & Mixed Conditionals + Hypothetical Alternatives |
| 11 | Reported Speech & Reporting Verbs |
| 12 | Gerunds & Infinitives |
| 13 | Relative Clauses |
| 14 | Participle Clauses & Complex Connectors |
| 15 | Emphasis, Focus & Inversion |
| 16 | Hedging, Diplomacy & Precision (+ Articles & Quantifiers Clinic) |

### 2. Master Speaking.docx
The Speaking skills course book (8 thematic units with Reading, Listening, Discussion
and Research & Presentation chapters).

## Building the grammar book

The `.docx` is generated from the Python sources in `build/`:

```bash
python3 -m venv .venv-docx
.venv-docx/bin/pip install python-docx
.venv-docx/bin/python build/build_book.py
```

---

© 2026 The TOEFL House — English Department. Classroom use only.

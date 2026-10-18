# -*- coding: utf-8 -*-
"""Automated QA gates for 'Grammar for Special Speaking' (Student Book and Teacher's Book).
Run AFTER build.py and build_teacher.py:  python build_spec/qa.py
Exit code 0 = all gates pass. Non-zero = genuine defects (do not weaken checks)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.oxml.ns import qn
import content_l1_4, content_l5_8, content_l9_12, content_l13_16
import teacher_l1_8, teacher_l9_16, teacher_l13_16

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(ROOT, 'Grammar for Special Speaking (TOEFL House).docx')
TEACHER_DOCX = os.path.join(ROOT, "Grammar for Special Speaking — Teacher's Book (TOEFL House).docx")

SPEC_TITLES = {
    1: "Tenses for Real Communication", 2: "Telling Stories and Describing Experiences",
    3: "Questions, Auxiliary Verbs, and Follow-up Questions", 4: "Modal Verbs for Real-Life Situations",
    5: "Conditionals for Decisions and Possibilities", 6: "Wishes, Regrets, and Hypothetical Situations",
    7: "Comparisons Beyond the Basics", 8: "Linking Ideas and Building Arguments",
    9: "Passive Voice in Natural English", 10: "Causative Structures",
    11: "Gerunds and Infinitives", 12: "Relative Clauses and Concise Descriptions",
    13: "Reported Speech and Reporting Verbs", 14: "Participles and Advanced Sentence Patterns",
    15: "Hedging, Emphasis, and Natural Inversion", 16: "Grammar in Real Conversation",
}
PARTS_LABELS = ["The Speaking Hook", "The Simple Rule", "See the Difference",
                "Practice the Pattern", "Pair Speaking", "Say It with Greater Precision",
                "Real Talk Challenge", "Review and Self-Check"]


def main():
    if not os.path.exists(DOCX):
        print("FAIL: manuscript missing:", DOCX)
        return 1
    doc = Document(DOCX)
    texts = [p.text for p in doc.paragraphs]
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                texts.append(c.text)
    blob = "\n".join(texts)
    fails = []

    def check(name, cond):
        print(("  PASS " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    print("=== QA GATES: Grammar for Special Speaking ===")
    # structure
    check("16 lessons", sum(1 for t in texts if re.match(r"^LESSON \d+", t.strip())) == 16)
    for i, lab in enumerate(PARTS_LABELS, 1):
        check(f"framework Part {i} ({lab}) x16",
              sum(1 for t in texts if t.strip() == f"Part {i}  ·  {lab}") == 16)
    check("16 lesson titles match spec",
          all(f"LESSON {i}  ·  {t.upper()}" in blob for i, t in SPEC_TITLES.items()))
    lessons = (content_l1_4.LESSONS_1_4 + content_l5_8.LESSONS_5_8 +
               content_l9_12.LESSONS_9_12 + content_l13_16.LESSONS_13_16)
    completeness = all(
        L.get("intro") and L.get("hook") and L.get("rules") and L.get("differences") and
        all(r.get("text") and r.get("formula") and r.get("examples") and r.get("remember") for r in L.get("rules", [])) and
        L.get("practice_a") and L.get("practice_b") and
        L.get("pair", {}).get("task") and L.get("pair", {}).get("model") and L.get("pair", {}).get("criteria") and
        L.get("advanced", {}).get("intro") and L.get("advanced", {}).get("base") and L.get("advanced", {}).get("upgrade") and
        L.get("realtalk", {}).get("task") and L.get("realtalk", {}).get("feedback") and
        L.get("review", {}).get("points") and L.get("review", {}).get("selfcheck")
        for L in lessons)
    check("all eight lesson functions contain usable content (source-data check)", completeness)
    answer_alignment = all(
        len(L["practice_a"]) == len((L.get("answers") or L["review"].get("answers", {})).get("A", [])) and
        len(L["practice_b"]) == len((L.get("answers") or L["review"].get("answers", {})).get("B", []))
        for L in lessons)
    check("lesson controlled-practice items align with answer-key counts", answer_alignment)
    # document order
    order = []
    for t in texts:
        m = re.match(r"^LESSON (\d+)", t.strip())
        if m:
            order.append(f"L{m.group(1)}")
        m = re.match(r"^REVIEW TEST (\d+)", t.strip())
        if m:
            order.append(f"T{m.group(1)}")
    expected = ["L1", "L2", "L3", "L4", "T1", "L5", "L6", "L7", "L8", "T2",
                "L9", "L10", "L11", "L12", "T3", "L13", "L14", "L15", "L16"]
    check("document order (tests in scope positions)", order == expected)
    # keys
    check("16 quick-answer boxes", sum(1 for t in texts if t.strip().startswith("Quick answers")) == 16)
    check("appendix answer key covers 16 lessons",
          sum(1 for t in texts if re.match(r"^Lesson \d+$", t.strip())) >= 16)
    # assessments
    check("3 review tests", all(f"REVIEW TEST {i}" in blob for i in (1, 2, 3)))
    check("diagnostic present", "DIAGNOSTIC TEST" in blob)
    check("final assessment + rubric + error plan",
          all(k in blob for k in ("FINAL ASSESSMENT", "Evaluation rubric", "improvement plan")))
    check("5 appendices", all(f"APPENDIX {i}" in blob for i in (1, 2, 3, 4, 5)))
    # final assessment covers all 16 lessons (keyword evidence)
    coverage = {
        "L1": "__________ (live) here since 2020", "L2": "(already / have) dinner",
        "L3": "When does the shop close", "L4": "(mustn't / can't)",
        "L5": "Third conditional: 'He didn't revise, so he failed.'",
        "L6": "wish I __________ (not/say) that yesterday",
        "L7": "far + give a reason frame", "L8": "being expensive, the course is worth it",
        "L9": "stolen the documents", "L10": "I paid someone to fix the roof",
        "L11": "look forward to __________ (meet) you", "L12": "The book what I read was amazing",
        "L13": "She advised", "L14": "Because he had studied hard, he passed easily",
        "L15": "Rarely had she felt so confident", "L16": "Speaking task (2 minutes to prepare",
    }
    for k, kw in coverage.items():
        check(f"final assessment covers {k}", kw in blob)

    # review-test scope evidence (no leakage of later-lesson grammar)
    def walk_between(start, end):
        """Collect all text (document order) strictly between two banner markers."""
        collecting = False
        out = []
        for child in doc.element.body:
            tag = child.tag.split('}')[1]
            if tag not in ('p', 'tbl'):
                continue
            t = ''.join(n.text or '' for n in child.iter(qn('w:t')))
            if not collecting and start in t:
                collecting = True
                continue
            if collecting and end in t:
                break
            if collecting:
                out.append(t)
        return '\n'.join(out)

    t1 = walk_between("REVIEW TEST 1", "LESSON 5")
    t2 = walk_between("REVIEW TEST 2", "LESSON 9")
    t3 = walk_between("REVIEW TEST 3", "LESSON 13")
    leak = [("T1", t1, ["reported", "She asked me", "participle", "hedg", "cleft", "inversion",
                        "Never have", "Not only", "causative", "have my", "gerund", "avoid"]),
            ("T2", t2, ["participle", "Having", "hedg", "may well", "cleft", "inversion",
                        "Never have", "Not only", "reported", "promised to", "which were",
                        "avoid", "look forward to", "causative", "have my", "was written",
                        "Not until"]),
            ("T3", t3, ["hedg", "may well", "it could be argued", "inversion", "Never have",
                        "Not only", "Having finished", "Not having", "reported", "She asked me",
                        "denied", "cleft"])]
    for name, scope, banned in leak:
        hits = [w for w in banned if w.lower() in scope.lower()]
        check(f"{name} scope clean (no untaught grammar) {hits if hits else ''}", not hits)
    check("Review Test 1 excludes Lesson 5 conditionals and Lesson 8 concession linkers",
          not re.search(r"\b(despite|although|second conditional|if I were you)\b", t1, re.I))
    check("diagnostic, review-test, and final-test keys are kept separate from test items",
          all("Answer key" not in scope for scope in (walk_between("DIAGNOSTIC TEST", "LESSON 1"), t1, t2, t3,
                                                       walk_between("FINAL ASSESSMENT", "FINAL ASSESSMENT — PART 2"))))
    # banned language & unified classroom checks
    check("no scheduling words", not re.search(r"\b(Day \d|Week \d|MONTH \d|teaching days)\b", blob))
    check("no Master Speaking references", not re.search(r"Master Speaking", blob, re.I))
    check("no unearned claims", not re.search(r"expert-verified|publication-ready|pedagogically validated", blob, re.I))
    check("no student-facing proficiency-track labels or 'The Advanced Upgrade'",
          not re.search(r"The Advanced Upgrade|Intermediate\s*[—–-]\s*build|Advanced\s*[—–-]\s*build|\bBeginner\b|For lower-level students|For advanced students", blob, re.I))
    check("no placeholder text or stray characters",
          not re.search(r"\b(TODO|TBD|FIXME|Lorem ipsum)\b|同伴|droppings", blob))
    check("zero decorative emojis", sum(1 for ch in blob if ord(ch) >= 0x1F300) == 0)
    # comparable assessment and item-level coverage blueprint
    check("diagnostic and final clearly reject raw-total gain claims",
          "do not interpret the difference between their raw totals" in blob.lower() and
          "do not compare the raw grammar totals as a measure of gain" in blob.lower())
    check("baseline and final include matched speaking interaction",
          blob.count("two follow-up questions") >= 2 and "relevant follow-up exchange" in blob)
    matrix_path = os.path.join(ROOT, "docs", "final-assessment-coverage.md")
    matrix = open(matrix_path, encoding="utf-8").read() if os.path.exists(matrix_path) else ""
    check("item-level coverage matrix maps all 16 lessons",
          all(re.search(rf"\|\s*{i}\.\s", matrix) for i in range(1, 17)) and
          "Speaking task" in matrix and all(str(n) in matrix for n in range(1, 31)))
    # DOCX navigation and page geometry
    all_paras = list(doc.paragraphs)
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                all_paras.extend(cell.paragraphs)
    h1_count = sum(p.style.name.startswith("Heading 1") for p in all_paras)
    h2_count = sum(p.style.name.startswith("Heading 2") for p in all_paras)
    h3_count = sum(p.style.name.startswith("Heading 3") for p in all_paras)
    check("DOCX uses semantic heading levels for navigation (H1/H2/H3)",
          h1_count >= 20 and h2_count >= 128 and h3_count >= 48)
    a4 = all(abs(s.page_width.inches - 8.27) < 0.03 and abs(s.page_height.inches - 11.69) < 0.03 for s in doc.sections)
    check("DOCX pages use A4 dimensions", a4)
    check("DOCX publication metadata identifies title and house", doc.core_properties.title == "Grammar for Special Speaking" and doc.core_properties.author == "TOEFL HOUSE")
    check("DOCX contains an updateable page-numbered Word TOC field",
          'TOC \\o "1-1"' in doc.element.xml and "updateFields" in doc.settings.element.xml)
    # known-defect regressions
    check("no 'Although being' error pattern", "Although being" not in blob)
    check("Review Test 2 concession key avoids a dangling modifier",
          "Despite the exam being hard" in blob and "Despite being hard, everyone passed" not in blob)
    check("Diagnostic key accepts valid alternatives", all(x in blob for x in
          ("has been working", "who / that", "may / might / could", "had / got")))
    check("present-perfect guidance qualifies open time and recently", all(x in blob for x in
          ("'Recently' can take either tense", "either tense can be natural")))
    check("ordinary future if-clauses are qualified (not an absolute ban)",
          "Will can occur in if-clauses" in blob and
          "My if-clauses never contain 'will'." not in blob)
    check("comparative/superlative guidance is not reduced to a rigid item count",
          "Comparative for two; superlative for three or more" not in blob and
          "comparatives compare two choices" in blob.lower())
    check("question auxiliary rule allows non-subject exceptions", "Most direct English questions" in blob)
    check("guiding principle present", "Learn the grammar. Use it in conversation." in blob)
    # Lesson 1 approved revision (spec 3.2)
    L1 = lessons[0]
    check("Lesson 1: three core rule groups", len(L1["rules"]) == 3 and "Present tenses:" in L1["rules"][0]["label"])
    check("Lesson 1: five Practice A items and four Practice B tasks", len(L1["practice_a"]) == 5 and len(L1["practice_b"]) == 4)
    check("Lesson 1: present-perfect continuous in Part 6 precision section", "present perfect continuous" in " ".join(L1["advanced"]["upgrade"]).lower())
    check("Pair Speaking carries conversation goal and model exchange", all(L.get("pair", {}).get("output") and L.get("pair", {}).get("model") for L in lessons))
    check("Real Talk Challenge is separate from Pair Speaking (planning + model response)", all(L.get("realtalk", {}).get("plan") and L.get("realtalk", {}).get("model") and L["pair"].get("output") != L["realtalk"]["model"] for L in lessons))
    check("Part 6 provides core consolidation and precision extension", all(L.get("advanced", {}).get("base") and L.get("advanced", {}).get("upgrade") for L in lessons))
    check("Review links back to Simple Rule and Appendix card", "return to Part 2" in blob and "Formula Book card" in blob)
    check("speaking-section headings kept with next content (keepNext)", doc.element.xml.count("w:keepNext") >= 32)

    # Teacher's Book checks
    check("Teacher's Book DOCX exists", os.path.exists(TEACHER_DOCX))
    if os.path.exists(TEACHER_DOCX):
        tdoc = Document(TEACHER_DOCX)
        ttexts = [p.text for p in tdoc.paragraphs]
        for t in tdoc.tables:
            for r in t.rows:
                for c in r.cells:
                    ttexts.append(c.text)
        tblob = "\n".join(ttexts)
        check("Teacher's Book has 16 lesson guides",
              sum(1 for t in ttexts if t.strip() and re.match(r"^LESSON \d+\s+·.*TEACHER GUIDE$", t.splitlines()[0].strip())) == 16)
        check("Teacher's Book uses 'Part 6  ·  Say It with Greater Precision' x16",
              sum(1 for t in ttexts if t.strip() == "Part 6  ·  Say It with Greater Precision") == 16)
        check("Teacher's Book has no stray CJK or broken strings",
              not re.search(r"同伴|droppings|The Advanced Upgrade|Intermediate base:|Advanced upgrade:", tblob))

    print()
    if fails:
        print(f"RESULT: {len(fails)} FAILURES -> {fails}")
        return 1
    print("RESULT: ALL QA GATES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

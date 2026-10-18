# -*- coding: utf-8 -*-
"""Build: Grammar for Special Speaking — Teacher's Book (TOEFL HOUSE).
Output: 'Grammar for Special Speaking — Teacher\\'s Book (TOEFL House).docx' at repository root.
Run: python build_teacher.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from style import setup_doc, page_break
import content_front as front
import content_l1_4, content_l5_8, content_l9_12, content_l13_16
import content_tests as tests
import content_appendix as appendix
import teacher_front
from teacher_render import render_teacher_lesson
import teacher_l1_8 as tl1_8
import teacher_l9_16 as tl9_16
import teacher_l13_16 as tl13_16

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "Grammar for Special Speaking — Teacher's Book (TOEFL House).docx")

MODEL_FINAL_SPEECH = (
    "A decision that changed my life was moving to Kabul for university.\n"
    "At first I had never lived away from my family, and I was not sure I could manage alone. "
    "While I was adjusting, I made mistakes — I spent too much on transport because I had not learned the bus routes. "
    "If I had known the city better, I would have saved both time and money, and I would be more relaxed now. "
    "I believe education is an investment, although it was hard to leave home. "
    "I was told that grades would depend on attendance, so I attended every class. "
    "I have enjoyed meeting people who come from other provinces; the diversity has taught me patience. "
    "I have decided to continue studying even though costs are high. "
    "What I hope to do next is pass the TOEFL and teach English — the course has shown me that speaking every day is the key. "
    "Never have I been more certain that effort, not talent, decides who improves."
)

ALL_LESSONS = (
    content_l1_4.LESSONS_1_4 + content_l5_8.LESSONS_5_8 +
    content_l9_12.LESSONS_9_12 + content_l13_16.LESSONS_13_16
)

ALL_TEACHER_GUIDES = [
    tl1_8.T1, tl1_8.T2, tl1_8.T3, tl1_8.T4, tl1_8.T5, tl1_8.T6, tl1_8.T7, tl1_8.T8,
    tl9_16.T9, tl9_16.T10, tl9_16.T11, tl9_16.T12,
    tl13_16.T13, tl13_16.T14, tl13_16.T15, tl13_16.T16,
]


def main():
    assert len(ALL_LESSONS) == 16
    assert len(ALL_TEACHER_GUIDES) == 16
    for L, T in zip(ALL_LESSONS, ALL_TEACHER_GUIDES):
        assert T is not None

    doc = setup_doc()
    props = doc.core_properties
    props.title = "Grammar for Special Speaking — Teacher's Book"
    props.subject = "Companion to Grammar for Special Speaking: lesson procedures, answers, timing and guidance"
    props.author = "TOEFL HOUSE"
    props.last_modified_by = "TOEFL HOUSE"
    props.keywords = "English grammar, speaking, TOEFL, Intermediate, Advanced, Teacher's Book"
    props.comments = "Teacher companion manuscript generated from build_spec teacher guides and shared lesson sources."

    # Keys registry built the same way as the student book, so answers are guaranteed identical.
    keys_registry = {}
    # Diagnostic + tests need to be registered exactly as in the student build
    # We run through the same front/test/appendix side-effects on a detached doc to populate keys.
    # Simpler: register from the actual sources that build.py uses — import and call with a throwaway doc.
    from docx import Document as _Doc
    # Build keys by re-running the student test registration on a throwaway document with same doc API
    # Instead of duplicating logic, call the same functions that populate keys_registry.
    # Use a minimal doc that satisfies the rendering API.
    tmp_doc = setup_doc()
    front.diagnostic(tmp_doc, keys_registry)
    for L in ALL_LESSONS:
        # Need review-test keys too
        pass
    # Register review and final keys by calling the same builders on tmp_doc
    for n, after in [(1, 4), (2, 8), (3, 12)]:
        tests.review_test(tmp_doc, n, after, keys_registry)
    tests.final_assessment(tmp_doc, keys_registry)
    # Also register lesson keys — lesson_template.render_lesson does this; replicate minimally:
    for L in ALL_LESSONS:
        ans = L.get("answers") or L["review"].get("answers", {})
        keys_registry[f"Lesson {L['n']}"] = ans

    # ---- Teacher front matter ----
    teacher_front.title_page(doc)
    teacher_front.publication_note(doc)
    teacher_front.introduction(doc)
    teacher_front.how_to_use(doc)
    teacher_front.contents(doc)
    teacher_front.course_overview(doc, ALL_LESSONS, front.LESSON_TITLES)
    teacher_front.teaching_principles(doc)
    teacher_front.pacing_and_feedback(doc)

    # ---- Sixteen lesson guides ----
    for L, T in zip(ALL_LESSONS, ALL_TEACHER_GUIDES):
        render_teacher_lesson(doc, L, T)

    # ---- Assessment guidance (includes keys for tests) ----
    teacher_front.assessment_guidance(doc, keys_registry, MODEL_FINAL_SPEECH)

    doc.save(OUT)
    print("SAVED:", OUT)
    print("keys registered:", sorted(keys_registry.keys()))
    total_words = 0
    for p in doc.paragraphs:
        total_words += len(p.text.split())
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                total_words += len(c.text.split())
    print("approx words:", total_words, "| tables:", len(doc.tables))
    # Timing cross-check
    for L, T in zip(ALL_LESSONS, ALL_TEACHER_GUIDES):
        total = sum(m for _, m in T["timing"])
        assert total == 60, f"Lesson {L['n']} timing {total} != 60"


if __name__ == "__main__":
    main()

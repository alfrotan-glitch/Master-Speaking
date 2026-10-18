# -*- coding: utf-8 -*-
"""Build: Grammar for Special Speaking (TOEFL HOUSE).
Output: 'Grammar for Special Speaking (TOEFL House).docx' at repository root.
Run: python build.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from style import setup_doc, page_break
import content_front as front
import content_l1_4, content_l5_8, content_l9_12, content_l13_16
import content_tests as tests
import content_appendix as appendix

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'Grammar for Special Speaking (TOEFL House).docx')


def main():
    doc = setup_doc()
    props = doc.core_properties
    props.title = "Grammar for Special Speaking"
    props.subject = "A practical grammar course for accurate, natural, confident speech"
    props.author = "TOEFL HOUSE"
    props.last_modified_by = "TOEFL HOUSE"
    props.keywords = "English grammar, speaking, TOEFL, Intermediate, Advanced"
    props.comments = "Editable source manuscript generated from build_spec content."
    keys_registry = {}

    # front matter
    front.title_page(doc)
    front.publication_info(doc)
    front.introduction(doc)
    front.how_to_use(doc)
    front.contents(doc)
    front.diagnostic(doc, keys_registry)

    # lessons with review tests at the right points
    all_lessons = (
        content_l1_4.LESSONS_1_4 + content_l5_8.LESSONS_5_8 +
        content_l9_12.LESSONS_9_12 + content_l13_16.LESSONS_13_16
    )
    for L in all_lessons:
        from lesson_template import render_lesson
        render_lesson(doc, L, keys_registry)
        if L['n'] in (4, 8, 12):
            tests.review_test(doc, L['n'] // 4, L['n'], keys_registry)

    # final assessment
    tests.final_assessment(doc, keys_registry)

    # appendices
    appendix.render_all(doc, keys_registry)

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


if __name__ == "__main__":
    main()

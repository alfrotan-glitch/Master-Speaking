# -*- coding: utf-8 -*-
"""Shared renderer for the sixteen lesson guides in the Teacher's Book.

Each guide is built from the same lesson data as the Student Book, so objectives,
practice items, answers and model responses can never drift apart between the two
volumes.
"""
from style import (para, box, table, spacer, section_label, h_banner,
                   page_break, NAVY, TEAL, GOLD, INK, GREY,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY)

PART_LABELS = ["The Speaking Hook", "The Simple Rule", "See the Difference",
               "Practice the Pattern", "Pair Speaking", "The Advanced Upgrade",
               "Real Talk Challenge", "Review and Self-Check"]

PROCEDURE_KEYS = ["hook", "rule", "diff", "practice", "pair", "advanced", "realtalk", "review"]


def _bullets(doc, items, indent=0.12):
    for item in items:
        para(doc, f"•  {item}", size=11, indent=indent)


def _answers_of(L):
    return L.get("answers") or L["review"].get("answers", {})


def _joined(section, values):
    return f"{section}  " + "  ·  ".join(f"{i + 1} {v}" for i, v in enumerate(values))


def render_teacher_lesson(doc, L, T):
    n = L["n"]
    page_break(doc)
    h_banner(doc,
             f"LESSON {n}  ·  {L['title'].upper()}  —  TEACHER GUIDE",
             sub=f"Part {L['part_no']} — {L['part_title']}   |   Speaking goal: {L['goal']}")
    para(doc, "This guide mirrors the Student Book lesson exactly: the same eight functions, the "
              "same practice items and the same answers. Follow the parts in order; adapt the timing "
              "to your class.", size=10.5, italic=True, color=GREY, space_after=4)

    # ---- Outcomes and success criteria ----
    section_label(doc, "Lesson outcomes and measurable success criteria")
    lines = [f"•  {o}" for o in T["objectives"]]
    lines.append(("Success criteria — the learner can:", True))
    lines += [f"✓  {s}" for s in T["success"]]
    box(doc, "By the end of the lesson", lines, fill=FILL_BOX_GREY, label_color=NAVY)

    # ---- Materials and preparation ----
    section_label(doc, "Materials and preparation")
    box(doc, "Before the lesson",
        [f"•  {p}" for p in T["prep"]],
        fill=FILL_BOX_TEAL, label_color=TEAL)

    # ---- Timing ----
    section_label(doc, "Suggested timing (60-minute lesson)")
    total = sum(m for _, m in T["timing"])
    rows = [[label, str(m)] for label, m in T["timing"]]
    rows.append([(f"Total", True), (str(total), True)])
    table(doc, ["Lesson part", "Minutes"], rows, widths=[5.0, 1.3], font_size=10)
    assert total == 60, f"Lesson {n}: timing must total 60 minutes, found {total}"

    # ---- The eight functions ----
    for i, (key, label) in enumerate(zip(PROCEDURE_KEYS, PART_LABELS), 1):
        section_label(doc, f"Part {i}  ·  {label}")
        _bullets(doc, T["procedure"][key])

        if key == "rule":
            box(doc, "Check understanding — quick, whole-class",
                [f"•  {c}" for c in T["checking"]],
                fill=FILL_BOX_GREY, label_color=GOLD)

        if key == "practice":
            ans = _answers_of(L)
            key_lines = [_joined("Practice A.", ans.get("A", [])),
                         _joined("Practice B.", ans.get("B", []))]
            box(doc, "Answer key — Practice A and B (identical to the Student Book key)",
                key_lines, fill=FILL_BOX_GREY, label_color=NAVY)
            box(doc, "Where learners lose marks — teaching notes",
                [f"•  {x}" for x in T["notes"]],
                fill=FILL_BOX_GOLD, label_color=GOLD)

        if key == "pair":
            box(doc, "Model exchange for rehearsal (one possible version)",
                [T["pair_model"]],
                fill=FILL_BOX_GOLD, label_color=GOLD)

        if key == "realtalk":
            box(doc, "Model response (as printed in the Student Book)",
                [L["realtalk"]["model"]],
                fill=FILL_BOX_GOLD, label_color=GOLD)
            box(doc, "Assessing this open-ended task",
                [f"•  {a}" for a in T["assess"]],
                fill=FILL_BOX_GREY, label_color=NAVY)

    # ---- Differentiation ----
    section_label(doc, "Differentiation: Intermediate and Advanced pathways")
    box(doc, "Intermediate — scaffolding and remediation",
        [f"•  {x}" for x in T["inter"]], fill=FILL_BOX_GREY, label_color=GOLD)
    box(doc, "Advanced — extension and discussion guidance",
        [f"•  {x}" for x in T["adv"]], fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Common errors ----
    section_label(doc, "Common learner errors and targeted correction")
    box(doc, "Expect these — and fix them like this",
        [f"•  {e}" for e in T["errors"]],
        fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Shorter session ----
    section_label(doc, "Shorter-session adaptation (45 minutes)")
    box(doc, "Keep the objective, cut the load",
        [f"•  {s}" for s in T["short"]],
        fill=FILL_BOX_TEAL, label_color=TEAL)

    # ---- Review, consolidation and feedback ----
    section_label(doc, "Review, consolidation and feedback")
    box(doc, "Close the loop",
        [f"•  {r}" for r in T["review_note"]],
        fill=FILL_BOX_GREY, label_color=NAVY)
    box(doc, "Feedback for this lesson's speaking",
        [T["feedback"]],
        fill=FILL_BOX_TEAL, label_color=TEAL)

# -*- coding: utf-8 -*-
"""Shared renderer for the sixteen lesson guides in the Teacher's Book.

Each guide is built from the same lesson data as the Student Book, so objectives,
practice items, answers and model responses stay aligned across both volumes.
"""
from style import (para, box, table, spacer, section_label, h_banner,
                   page_break, NAVY, TEAL, GOLD, INK, GREY,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY)

PART_LABELS = ["The Speaking Hook", "The Simple Rule", "See the Difference",
               "Practice the Pattern", "Pair Speaking", "Say It with Greater Precision",
               "Real Talk Challenge", "Review and Self-Check"]

PROCEDURE_KEYS = ["hook", "rule", "diff", "practice", "pair", "advanced", "realtalk", "review"]


def _bullets(doc, items, indent=0.12):
    for item in items:
        para(doc, f"•  {item}", size=10.5, indent=indent, space_before=1.5, space_after=2)


def _answers_of(L):
    return L.get("answers") or L["review"].get("answers", {})


def _joined(section, values):
    return f"{section}  " + "  ·  ".join(f"{i + 1}. {v}" for i, v in enumerate(values))


def render_teacher_lesson(doc, L, T):
    n = L["n"]
    page_break(doc)
    h_banner(doc,
             f"LESSON {n}  ·  {L['title'].upper()}  —  TEACHER GUIDE",
             sub=f"Part {L['part_no']} — {L['part_title']}   |   Speaking goal: {L['goal']}")
    para(doc, "This guide follows the exact eight-part sequence of the Student Book lesson. "
              "Teach the whole class together through the shared explanations and activities, "
              "using the support and extension notes below to help every speaker succeed.",
         size=10.5, italic=True, color=GREY, space_after=4)

    # ---- Outcomes, preparation, and timing ----
    section_label(doc, "Lesson outcomes, preparation, and 60-minute timing")
    lines = [("Lesson objectives:", True, NAVY)]
    lines += [f"•  {o}" for o in T["objectives"]]
    lines.append(("Observable success criteria — listen for learners who:", True, TEAL))
    lines += [f"✓  {s}" for s in T["success"]]
    lines.append(("Before class begins:", True, GOLD))
    lines += [f"•  {p}" for p in T["prep"]]
    box(doc, None, lines, fill=FILL_BOX_GREY, label_color=NAVY)

    total = sum(m for _, m in T["timing"])
    rows = []
    for label, m in T["timing"]:
        display_label = "Say It with Greater Precision" if label == "The Advanced Upgrade" else label
        rows.append([display_label, str(m)])
    rows.append([("Total", True), (str(total), True)])
    table(doc, ["Lesson step", "Minutes"], rows, widths=[5.0, 1.3], font_size=9.5)
    assert total == 60, f"Lesson {n}: timing must total 60 minutes, found {total}"

    # ---- The eight functions ----
    for i, (key, label) in enumerate(zip(PROCEDURE_KEYS, PART_LABELS), 1):
        section_label(doc, f"Part {i}  ·  {label}")
        _bullets(doc, T["procedure"][key])

        if key == "rule":
            box(doc, "Quick concept check — whole class",
                [f"•  {c}" for c in T["checking"]],
                fill=FILL_BOX_GREY, label_color=GOLD)

        if key == "practice":
            ans = _answers_of(L)
            key_lines = [
                (_joined("Practice A:", ans.get("A", [])), False, INK),
                (_joined("Practice B:", ans.get("B", [])), False, INK),
                ("Explanatory notes and common traps:", True, GOLD),
            ] + [f"•  {x}" for x in T["notes"]]
            box(doc, "Answer key and teaching notes (Practice A & B)",
                key_lines, fill=FILL_BOX_GREY, label_color=NAVY)

        if key == "pair":
            box(doc, "Sample partner exchange for classroom demonstration",
                [T["pair_model"]],
                fill=FILL_BOX_TEAL, label_color=TEAL)

        if key == "realtalk":
            rt_lines = [
                ("Student Book model response:", True, GOLD),
                L["realtalk"]["model"],
                ("How to guide and assess this task:", True, NAVY),
            ] + [f"•  {a}" for a in T["assess"]]
            box(doc, None, rt_lines, fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Mixed-classroom support & extension ----
    section_label(doc, "Supporting and stretching one mixed classroom")
    diff_lines = [("Supporting developing speakers within the shared task:", True, NAVY)]
    diff_lines += [f"•  {x}" for x in T["inter"]]
    diff_lines.append(("Stretching confident speakers toward deeper precision:", True, TEAL))
    diff_lines += [f"•  {x}" for x in T["adv"]]
    box(doc, None, diff_lines, fill=FILL_BOX_GREY, label_color=NAVY)

    # ---- Common errors, shorter session, and feedback ----
    section_label(doc, "Common misunderstandings, 45-minute plan, and feedback")
    closing_lines = [("High-frequency slips and rapid board repairs:", True, GOLD)]
    closing_lines += [f"•  {e}" for e in T["errors"]]
    closing_lines.append(("Adapting for a 45-minute session:", True, TEAL))
    closing_lines += [f"•  {s}" for s in T["short"]]
    closing_lines.append(("Closing recall and fluency-protecting feedback:", True, NAVY))
    closing_lines += [f"•  {r}" for r in T["review_note"]]
    closing_lines.append(f"•  Feedback focus: {T['feedback']}")
    box(doc, None, closing_lines, fill=FILL_BOX_TEAL, label_color=TEAL)

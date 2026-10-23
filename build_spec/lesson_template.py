# -*- coding: utf-8 -*-
"""Shared renderer for the 8-part standard lesson (spec section 6)."""
from style import (para, run, box, table, spacer, section_label, h_banner,
                   page_break, NAVY, TEAL, GOLD, INK, GREY, WHITE,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY, FILL_NAVY, FILL_TEAL)


def render_lesson(doc, L, keys_registry):
    n = L['n']
    if n > 1:
        page_break(doc)
    # lesson banner
    h_banner(doc,
             f"LESSON {n}  ·  {L['title'].upper()}",
             sub=f"Part {L['part_no']} — {L['part_title']}   |   Speaking goal: {L['goal']}")
    # intro line
    if L.get('intro'):
        para(doc, L['intro'], size=10.5, italic=True, color=GREY, space_after=4)

    # ---- Part 1: The Speaking Hook ----
    section_label(doc, "Part 1  ·  The Speaking Hook")
    box(doc, "Start here — talk first", L['hook'], fill=FILL_BOX_TEAL, label_color=TEAL)

    # ---- Part 2: The Simple Rule ----
    section_label(doc, "Part 2  ·  The Simple Rule")
    for rule in L['rules']:
        if rule.get('label'):
            para(doc, rule['label'], size=11, bold=True, color=NAVY)
        if rule.get('formula'):
            box(doc, "Formula", rule['formula'], fill=FILL_BOX_GREY, label_color=GOLD, formula=True)
        for line in rule.get('text', []):
            if isinstance(line, tuple):
                para(doc, line[0], size=11, bold=line[1])
            else:
                para(doc, line, size=11)
        if rule.get('examples'):
            box(doc, "Examples", rule['examples'], fill="FFFFFF", label_color=TEAL)
        if rule.get('remember'):
            box(doc, "Remember", rule['remember'], fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Part 3: See the Difference ----
    section_label(doc, "Part 3  ·  See the Difference")
    for d in L['differences']:
        para(doc, d['title'], size=11, bold=True, color=NAVY)
        for line in d.get('text', []):
            para(doc, line, size=11)
        if d.get('rows'):
            table(doc, d.get('headers', ['A', 'B', 'Why']), d['rows'], zebra=True)

    # ---- Part 4: Practice the Pattern ----
    section_label(doc, "Part 4  ·  Practice the Pattern")
    if L.get('practice_a'):
        para(doc, "A.  Complete or correct the sentences.", size=11, bold=True, color=TEAL)
        for i, item in enumerate(L['practice_a'], 1):
            para(doc, f"{i}.  {item}", size=11, indent=0.12)
    if L.get('practice_b'):
        para(doc, "B.  Choose, transform or build.", size=11, bold=True, color=TEAL)
        for i, item in enumerate(L['practice_b'], 1):
            para(doc, f"{i}.  {item}", size=11, indent=0.12)

    # ---- Part 5: Pair Speaking ----
    section_label(doc, "Part 5  ·  Pair Speaking")
    pair = L['pair']
    pair_lines = [pair['intro']] + [f"•  {b}" for b in pair['task']]
    if pair.get('output'):
        pair_lines.append((f"Expected output: {pair['output']}", False))
    box(doc, "Work with a partner", pair_lines,
        fill=FILL_BOX_TEAL, label_color=TEAL)
    box(doc, "Success criteria",
        [f"✓  {c}" for c in pair['criteria']], fill="FFFFFF", label_color=TEAL)

    # ---- Part 6: Strengthen Your Speaking ----
    section_label(doc, "Part 6  ·  Strengthen Your Speaking")
    adv = L['advanced']
    box(doc, "Build the pattern — say it clearly",
        [f"•  {b}" for b in adv['base']], fill=FILL_BOX_GREY, label_color=GOLD)
    box(doc, "Stretch your answer — choose your words",
        [f"•  {b}" for b in adv['upgrade']], fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Part 7: Real Talk Challenge ----
    section_label(doc, "Part 7  ·  Real Talk Challenge")
    rt = L['realtalk']
    if rt.get('plan'):
        box(doc, "Plan first", [rt['plan']], fill=FILL_BOX_GREY, label_color=GOLD)
    box(doc, "Speak now — without reading",
        [rt['task']], fill=FILL_BOX_TEAL, label_color=TEAL)
    if rt.get('model'):
        box(doc, "Model response — speak first, then compare; one strong example, not the only answer",
            [rt['model']], fill=FILL_BOX_GOLD, label_color=GOLD)
    box(doc, "Partner feedback — listen for",
        [f"✓  {c}" for c in rt['feedback']], fill="FFFFFF", label_color=TEAL)

    # ---- Part 8: Review and Self-Check ----
    section_label(doc, "Part 8  ·  Review and Self-Check")
    rv = L['review']
    box(doc, "Key learning points", [f"•  {b}" for b in rv['points']],
        fill=FILL_BOX_GREY, label_color=NAVY)
    if rv.get('retrieval'):
        box(doc, "Retrieval practice — cover the page, then say",
            [f"•  {b}" for b in rv['retrieval']], fill="FFFFFF", label_color=TEAL)
    if rv.get('watch'):
        box(doc, "Watch out", [f"•  {b}" for b in rv['watch']],
            fill=FILL_BOX_GOLD, label_color=GOLD)
    if rv.get('selfcheck'):
        para(doc, "Self-check — can you do this now?", size=11, bold=True, color=NAVY)
        for s in rv['selfcheck']:
            para(doc, f"☐  {s}", size=11, indent=0.12)
        para(doc, f"If a box is unticked: return to Part 2 · The Simple Rule for this lesson, redo the "
                  f"matching practice item, and check Formula Book card {n} in Appendix 1 before you move on.",
             size=10.5, italic=True, color=GREY, space_before=3)
    # quick answers
    ans = L.get('answers') or rv.get('answers', {})
    if ans:
        lines = []
        if ans.get('A'):
            lines.append(("A.  " + "   ".join(ans['A']), False))
        if ans.get('B'):
            lines.append(("B.  " + "   ".join(ans['B']), False))
        box(doc, "Quick answers", lines, fill=FILL_BOX_GREY, label_color=NAVY)
        keys_registry[f"Lesson {n}"] = ans

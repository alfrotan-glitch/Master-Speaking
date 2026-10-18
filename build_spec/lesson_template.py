# -*- coding: utf-8 -*-
"""Shared renderer for the 8-part lesson journey in Grammar for Special Speaking."""
from style import (para, run, box, table, spacer, section_label, h_banner,
                   page_break, NAVY, TEAL, GOLD, INK, GREY, WHITE,
                   FILL_BOX_TEAL, FILL_BOX_GOLD, FILL_BOX_GREY, FILL_NAVY, FILL_TEAL)


def render_lesson(doc, L, keys_registry):
    n = L['n']
    if n > 1:
        page_break(doc)
    # Lesson banner
    h_banner(doc,
             f"LESSON {n}  ·  {L['title'].upper()}",
             sub=f"Part {L['part_no']} — {L['part_title']}   |   Speaking goal: {L['goal']}")

    # Opening narrative
    intro = L.get('intro')
    if intro:
        if isinstance(intro, (list, tuple)):
            for p_text in intro:
                para(doc, p_text, size=11, color=INK, space_after=4)
        else:
            para(doc, intro, size=11, color=INK, space_after=4)

    # ---- Part 1: The Speaking Hook ----
    section_label(doc, "Part 1  ·  The Speaking Hook")
    box(doc, "Start the conversation", L['hook'], fill=FILL_BOX_TEAL, label_color=TEAL)

    # ---- Part 2: The Simple Rule ----
    section_label(doc, "Part 2  ·  The Simple Rule")
    for rule in L['rules']:
        if rule.get('label'):
            para(doc, rule['label'], size=11.5, bold=True, color=NAVY,
                 space_before=6, space_after=3, keep_with_next=True, style_name='Heading 3')
        for line in rule.get('text', []):
            if isinstance(line, tuple):
                para(doc, line[0], size=11, bold=line[1], space_after=3.5)
            else:
                para(doc, line, size=11, space_after=3.5)
        card_lines = []
        if rule.get('formula'):
            card_lines.append(("Pattern:", True, NAVY))
            for f_line in rule['formula']:
                card_lines.append((f"  {f_line}", True, NAVY))
        if rule.get('examples'):
            card_lines.append(("Natural examples:", True, TEAL))
            for ex in rule['examples']:
                card_lines.append(f"  •  {ex}")
        if rule.get('remember'):
            card_lines.append(("Keep in mind:", True, GOLD))
            for rem in rule['remember']:
                card_lines.append(f"  →  {rem}")
        if card_lines:
            box(doc, None, card_lines, fill=FILL_BOX_GREY, label_color=NAVY)

    # ---- Part 3: See the Difference ----
    section_label(doc, "Part 3  ·  See the Difference")
    for d in L['differences']:
        para(doc, d['title'], size=11.5, bold=True, color=NAVY,
             space_before=6, space_after=3, keep_with_next=True, style_name='Heading 3')
        for line in d.get('text', []):
            para(doc, line, size=11, space_after=3.5)
        if d.get('rows'):
            table(doc, d.get('headers', ['A', 'B', 'What changes in meaning']), d['rows'], zebra=True)
        for line in d.get('note', []):
            para(doc, line, size=10.5, italic=True, color=GREY, space_after=3)

    # ---- Part 4: Practice the Pattern ----
    section_label(doc, "Part 4  ·  Practice the Pattern")
    if L.get('practice_a'):
        para(doc, "A.  Complete each sentence with the most natural form, then say it aloud.",
             size=11, bold=True, color=TEAL, keep_with_next=True)
        for i, item in enumerate(L['practice_a'], 1):
            para(doc, f"{i}.  {item}", size=11, indent=0.12)
    if L.get('practice_b'):
        para(doc, "B.  Repair, transform, or build the sentence so the meaning is clear.",
             size=11, bold=True, color=TEAL, space_before=4, keep_with_next=True)
        for i, item in enumerate(L['practice_b'], 1):
            para(doc, f"{i}.  {item}", size=11, indent=0.12)

    # ---- Part 5: Pair Speaking ----
    section_label(doc, "Part 5  ·  Pair Speaking")
    pair = L['pair']
    pair_lines = [pair['intro']] + [f"•  {b}" for b in pair['task']]
    if pair.get('model'):
        pair_lines.append(("How it sounds in conversation:", True, TEAL))
        if isinstance(pair['model'], (list, tuple)):
            pair_lines.extend(pair['model'])
        else:
            pair_lines.append(pair['model'])
    if pair.get('output'):
        pair_lines.append((f"Your conversation goal: {pair['output']}", True, NAVY))
    box(doc, "Speak with a partner", pair_lines, fill=FILL_BOX_TEAL, label_color=TEAL)
    para(doc, "What makes this conversation work:", size=10.5, bold=True, color=TEAL, keep_with_next=True)
    for c in pair['criteria']:
        para(doc, f"✓  {c}", size=10.5, indent=0.12, space_before=1, space_after=1.5)

    # ---- Part 6: Say It with Greater Precision ----
    section_label(doc, "Part 6  ·  Say It with Greater Precision")
    adv = L['advanced']
    if adv.get('intro'):
        para(doc, adv['intro'], size=11, space_after=3.5)
    precision_lines = [("Make the core pattern automatic:", True, NAVY)]
    precision_lines += [f"•  {b}" for b in adv['base']]
    precision_lines.append(("Add nuance, detail, and sharper focus:", True, TEAL))
    precision_lines += [f"•  {b}" for b in adv['upgrade']]
    box(doc, "From clear accuracy to richer expression", precision_lines,
        fill=FILL_BOX_GOLD, label_color=GOLD)

    # ---- Part 7: Real Talk Challenge ----
    section_label(doc, "Part 7  ·  Real Talk Challenge")
    rt = L['realtalk']
    rt_lines = []
    if rt.get('plan'):
        rt_lines.append((f"Prepare: {rt['plan']}", False, INK))
    rt_lines.append((f"Speak without reading: {rt['task']}", True, NAVY))
    box(doc, "Your speaking challenge", rt_lines, fill=FILL_BOX_TEAL, label_color=TEAL)
    if rt.get('model'):
        box(doc, "Model response — speak first, then compare",
            [rt['model']], fill=FILL_BOX_GOLD, label_color=GOLD)
    para(doc, "Partner listening checklist:", size=10.5, bold=True, color=TEAL, keep_with_next=True)
    for c in rt['feedback']:
        para(doc, f"✓  {c}", size=10.5, indent=0.12, space_before=1, space_after=1.5)

    # ---- Part 8: Review and Self-Check ----
    section_label(doc, "Part 8  ·  Review and Self-Check")
    rv = L['review']
    review_lines = [("Core insights to carry with you:", True, NAVY)]
    review_lines += [f"•  {b}" for b in rv['points']]
    if rv.get('watch'):
        review_lines.append(("Common traps to avoid:", True, GOLD))
        review_lines += [f"→  {b}" for b in rv['watch']]
    box(doc, None, review_lines, fill=FILL_BOX_GREY, label_color=NAVY)
    if rv.get('retrieval'):
        para(doc, "Close the book and try this from memory:", size=10.5, bold=True, color=TEAL, keep_with_next=True)
        for b in rv['retrieval']:
            para(doc, f"•  {b}", size=10.5, indent=0.12, space_before=1, space_after=1.5)
    if rv.get('selfcheck'):
        para(doc, "Self-check — can you do this now?", size=10.5, bold=True, color=NAVY,
             space_before=3, keep_with_next=True)
        for s in rv['selfcheck']:
            para(doc, f"☐  {s}", size=10.5, indent=0.12, space_before=1, space_after=1.5)
        para(doc, f"If a box is unticked: return to Part 2 · The Simple Rule for this lesson, redo the "
                  f"matching practice item, and check Formula Book card {n} in Appendix 1 before you move on.",
             size=10, italic=True, color=GREY, space_before=2)
    # Quick answers (cleanly numbered)
    ans = L.get('answers') or rv.get('answers', {})
    if ans:
        lines = []
        if ans.get('A'):
            a_str = "  ·  ".join(f"{i+1}. {v}" for i, v in enumerate(ans['A']))
            lines.append((f"Practice A:   {a_str}", False))
        if ans.get('B'):
            b_str = "  ·  ".join(f"{i+1}. {v}" for i, v in enumerate(ans['B']))
            lines.append((f"Practice B:   {b_str}", False))
        box(doc, "Quick answers", lines, fill=FILL_BOX_GREY, label_color=NAVY)
        keys_registry[f"Lesson {n}"] = ans

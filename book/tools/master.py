#!/usr/bin/env python3
"""master.py — render book/artifacts/book.json into book/master/master.xhtml.

The master is the single editable source of truth: a semantic XHTML document
with a controlled class system. Both the print PDF (pdf.py) and the EPUB
(epub.py) are derived from it.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BUILD = os.path.join(ROOT, 'book', 'artifacts')
book = json.load(open(os.path.join(BUILD, 'book.json'), encoding='utf-8'))

E = html.escape

def esc(s):
    return E(s, quote=False)

def pid(*parts):
    return '-'.join(str(p).lower().replace(' ', '-') for p in parts)

# ----------------------------------------------------------------------------
# grouping of consecutive blocks into semantic lists
# ----------------------------------------------------------------------------
def group_blocks(blocks):
    """Yield (kind, payload) groups from a flat block list."""
    out = []
    i = 0
    n = len(blocks)
    while i < n:
        b = blocks[i]
        k = b.get('k')
        if k == 'q':
            # question possibly followed by its options
            if i + 1 < n and blocks[i+1].get('k') == 'opt':
                item = {'q': b['text'], 'opts': []}
                i += 1
                while i < n and blocks[i].get('k') == 'opt':
                    item['opts'].append(blocks[i]['text'])
                    i += 1
                out.append(('mcq', item))
            else:
                item = {'q': b['text'], 'opts': []}
                i += 1
                out.append(('mcq', item))
            continue
        if k == 'opt':
            # stray options without a question stem (rare)
            opts = []
            while i < n and blocks[i].get('k') == 'opt':
                opts.append(blocks[i]['text'])
                i += 1
            out.append(('options', opts))
            continue
        if k == 'tf':
            lst = []
            while i < n and blocks[i].get('k') == 'tf':
                lst.append(blocks[i]['text'])
                i += 1
            out.append(('tflist', lst))
            continue
        if k == 'fill':
            lst = []
            while i < n and blocks[i].get('k') == 'fill':
                lst.append(blocks[i]['text'])
                i += 1
            out.append(('filllist', lst))
            continue
        if k in ('pair', 'choice', 'li'):
            lst = []
            kk = blocks[i].get('k')
            while i < n and blocks[i].get('k') == kk:
                lst.append(blocks[i]['text'])
                i += 1
            out.append((kk + 'list', lst))
            continue
        if k == 'reading':
            img = b.get('img')
            # collect consecutive reading paragraphs; image rides on first
            paras = []
            while i < n and blocks[i].get('k') == 'reading':
                paras.append({'text': blocks[i]['text'], 'img': blocks[i].get('img')})
                i += 1
            out.append(('readingblock', paras))
            continue
        out.append((k, b))
        i += 1
    return out

def table_html(b, ctx=''):
    role = b['role']
    rows = b['rows']
    cls = f'tbl {role}'
    head = ''
    body_rows = rows
    hdr_first = role in ('vocab', 'preslang', 'notes', 'grid', 'ranking')
    if hdr_first and rows:
        head = '<thead><tr>' + ''.join(
            f'<th scope="col">{esc(c)}</th>' for c in rows[0]) + '</tr></thead>'
        body_rows = rows[1:]
    trs = []
    for r in body_rows:
        tds = []
        for ci, c in enumerate(r):
            tds.append(f'<td>{esc(c)}</td>')
        trs.append('<tr>' + ''.join(tds) + '</tr>')
    return (f'<table class="{cls}">{head}<tbody>' + ''.join(trs) + '</tbody></table>')

def render_blocks(blocks, ctx):
    """Render grouped blocks to HTML lines."""
    h = []
    for kind, payload in group_blocks(blocks):
        if kind == 'sec':
            h.append(f'<h3 class="sec" id="{pid(ctx, payload["text"])}">{esc(payload["text"])}</h3>')
        elif kind == 'sub':
            h.append(f'<h4 class="sub">{esc(payload["text"])}</h4>')
            if payload.get('img'):
                h.append(f'<figure class="inline-figure"><img src="assets/images/{payload["img"]}" alt=""/></figure>')
        elif kind == 'subsub':
            h.append(f'<h5 class="runin">{esc(payload["text"])}</h5>')
            if payload.get('img'):
                h.append(f'<figure class="inline-figure"><img src="assets/images/{payload["img"]}" alt=""/></figure>')
        elif kind == 'instr':
            h.append(f'<p class="instr">{esc(payload["text"])}</p>')
        elif kind == 'label':
            h.append(f'<p class="label">{esc(payload["text"])}</p>')
        elif kind == 'p':
            img = f'<img class="inline-img" src="assets/images/{payload["img"]}" alt=""/>' if payload.get('img') else ''
            h.append(f'<p>{img}{esc(payload["text"])}</p>')
        elif kind == 'topic':
            h.append(f'<p class="topic">{esc(payload["text"])}</p>')
        elif kind == 'titleline':
            h.append(f'<p class="titleline">{esc(payload["text"])}</p>')
        elif kind == 'mediatitle':
            h.append(f'<p class="media-title">{esc(payload["text"])}</p>')
        elif kind == 'readingtitle':
            h.append(f'<h4 class="reading-title">{esc(payload["text"])}</h4>')
            if payload.get('img'):
                h.append(f'<figure class="reading-figure"><img src="assets/images/{payload["img"]}" alt="Illustration for the reading passage"/></figure>')
        elif kind == 'note':
            h.append(f'<div class="note"><p>{esc(payload["text"])}</p></div>')
        elif kind == 'mcq':
            cls = 'mcq' if payload['opts'] else 'questions'
            inner = esc(payload['q'])
            if payload['opts']:
                ol = ''.join(f'<li>{esc(o)}</li>' for o in payload['opts'])
                inner += f'<ol class="options">{ol}</ol>'
            h.append(f'<li class="q">{inner}</li>')
        elif kind == 'options':
            h.append('<ol class="options standalone">' + ''.join(
                f'<li>{esc(o)}</li>' for o in payload) + '</ol>')
        elif kind == 'tflist':
            h.append('<ul class="tf">' + ''.join(
                f'<li>{esc(x)}</li>' for x in payload) + '</ul>')
        elif kind == 'filllist':
            h.append('<ul class="fill">' + ''.join(
                f'<li>{esc(x)}</li>' for x in payload) + '</ul>')
        elif kind == 'pairlist':
            h.append('<ul class="pairs">' + ''.join(
                f'<li>{esc(x)}</li>' for x in payload) + '</ul>')
        elif kind == 'choicelist':
            h.append('<ul class="choices">' + ''.join(
                f'<li>{esc(x)}</li>' for x in payload) + '</ul>')
        elif kind == 'lilist':
            h.append('<ul class="items">' + ''.join(
                f'<li>{esc(x)}</li>' for x in payload) + '</ul>')
        elif kind == 'readingblock':
            parts = []
            started = False
            for pr in payload:
                if pr.get('img') and not started:
                    parts.append(
                        f'<figure class="reading-figure"><img src="assets/images/{pr["img"]}" alt="Illustration for the reading passage"/></figure>')
                parts.append(f'<p class="reading">{esc(pr["text"])}</p>')
                started = True
            h.append('<div class="reading-block">' + ''.join(parts) + '</div>')
        elif kind == 'table':
            h.append(table_html(payload, ctx))
        else:
            h.append(f'<!-- unhandled {kind} -->')
    # wrap consecutive bare <li class="q"> into an <ol class="questions">
    return wrap_mcq(h)

def wrap_mcq(lines):
    out, buf = [], []
    for ln in lines:
        if ln.startswith('<li class="q">'):
            buf.append(ln)
        else:
            if buf:
                out.append('<ol class="questions">' + ''.join(buf) + '</ol>')
                buf = []
            out.append(ln)
    if buf:
        out.append('<ol class="questions">' + ''.join(buf) + '</ol>')
    return out

# ----------------------------------------------------------------------------
# document assembly
# ----------------------------------------------------------------------------
meta = book['meta']
parts = []

# half title
parts.append('<section class="fm" data-part="half-title" id="half-title">\n'
             f'<h1 class="half-title">{esc(meta["title"])}</h1>\n</section>')

# title page
parts.append('<section class="fm" data-part="title-page" id="title-page">\n'
             f'<h1 class="book-title">{esc(meta["title"])}</h1>\n'
             f'<p class="author">{esc(meta["author"])}</p>\n</section>')

# copyright
parts.append('<section class="fm" data-part="copyright" id="copyright">\n'
             f'<p class="copyright-line">Copyright © {meta["year"]} {esc(meta["author"])}</p>\n'
             '<p class="copyright-line">All rights reserved. No part of this publication may be reproduced, '
             'distributed, or transmitted in any form or by any means, without the prior written permission '
             'of the author, except for brief quotations in reviews and academic use.</p>\n'
             '</section>')

# foreword
fw = ['<section class="fm" data-part="foreword" id="foreword">',
      '<h1 class="fm-head">Foreword</h1>']
for b in book['front']['foreword']:
    k, t = b['k'], b['text']
    if k == 'p':
        fw.append(f'<p>{esc(t)}</p>')
    elif k == 'closer':
        fw.append(f'<p class="lead-in">{esc(t)}</p>')
    elif k == 'signature':
        fw.append(f'<p class="signature">{esc(t)}</p>')
    elif k == 'date':
        fw.append(f'<p class="signature-date">{esc(t)}</p>')
fw.append('</section>')
parts.append('\n'.join(fw))

# how to use
ht = book['front']['howto']
lines = ['<section class="fm" data-part="how-to-use" id="how-to-use">',
         '<h1 class="fm-head">How to Use This Book</h1>',
         f'<p class="media-title">{esc(ht["subtitle"])}</p>']
body = list(ht['paras'])
h4_at = None
for j, t in enumerate(body):
    if t == 'How Is Each Unit Organized?':
        h4_at = j
if h4_at is not None:
    for t in body[:h4_at]:
        lines.append(f'<p>{esc(t)}</p>')
    lines.append('<h2 class="fm-sub">How Is Each Unit Organized?</h2>')
    rest = body[h4_at+1:]
else:
    for t in body:
        lines.append(f'<p>{esc(t)}</p>')
    rest = []
for t in rest:
    lines.append(f'<p>{esc(t)}</p>')
for ch in ht['chapters']:
    lines.append(f'<div class="howto-chapter"><h3 class="fm-sub2">Chapter {ch["n"]} — {esc(ch["title"])}</h3>')
    if ch.get('desc'):
        lines.append(f'<p class="instr">{esc(ch["desc"])}</p>')
    lines.append('<ul class="items">' + ''.join(f'<li>{esc(x)}</li>' for x in ch['you_will']) + '</ul></div>')
lines.append(f'<p>{esc(ht["closing"])}</p>')
lines.append('</section>')
parts.append('\n'.join(lines))

# epigraph page (follows How to Use, precedes Unit 1 — as in the manuscript)
epi = book['front']['epigraph']
parts.append('<section class="fm" data-part="epigraph" id="epigraph">\n'
             f'<blockquote><p>{esc(epi)}</p></blockquote>\n</section>')

# units
for u in book['units']:
    up = ['<section class="unit" id="' + pid('unit', u['number']) + f'" data-unit="{u["number"]}">',
          f'<h1 class="unit-title"><span class="unit-kicker">Unit {u["number"]}</span>'
          f'<span class="unit-name">{esc(u["title"])}</span></h1>']
    if u.get('image'):
        up.append(f'<figure class="unit-figure"><img src="assets/images/{u["image"]}" '
                  f'alt="Opening image for Unit {u["number"]}: {esc(u["title"])}"/></figure>')
    w = u.get('warmup', {})
    wl = ['<div class="warmup">', '<h2 class="warmup-head">Think</h2>']
    for p in w.get('paras', []):
        wl.append(f'<p class="instr">{esc(p)}</p>')
    if w.get('table'):
        wl.append(table_html(w['table'], pid('unit', u['number'], 'warmup')))
    wl.append('</div>')
    up.append('\n'.join(wl))
    for c in u['chapters']:
        cp = ['<section class="chapter" id="' + pid('unit', u['number'], 'chapter', c['number']) +
              f'" data-chapter="{c["number"]}">',
              f'<h2 class="chapter-title"><span class="chapter-kicker">Chapter {c["number"]}</span>'
              f'<span class="chapter-name">{esc(c["title"])}</span></h2>']
        cp.extend(render_blocks(c['blocks'], pid('unit', u['number'], 'chapter', c['number'])))
        cp.append('</section>')
        up.append('\n'.join(cp))
    up.append('</section>')
    parts.append('\n'.join(up))

doc = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{esc(meta['title'])}</title>
<meta charset="UTF-8"/>
<meta name="author" content="{esc(meta['author'])}"/>
</head>
<body>
{chr(10).join(parts)}
</body>
</html>
'''
out = os.path.join(ROOT, 'book', 'master', 'master.xhtml')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(doc)
print('master written:', out, f'{len(doc):,} chars')

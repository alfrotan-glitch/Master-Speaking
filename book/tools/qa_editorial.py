#!/usr/bin/env python3
"""qa_editorial.py — editorial QA over the master text.

Text extraction is block-boundary aware (spaces inserted at child block tags)
so that </li><li> and table-cell seams never fuse words. Spellcheck skips
pronunciation lines (IPA / stress respellings), unfolds contractions and
possessives, and auto-accepts hyphenated compounds (logged separately).
Also checks duplicated words, double spaces, straight quotes/apostrophes,
and space-before-punctuation. Writes book/artifacts/qa_editorial.json.
"""
import os, re, json, collections
from lxml import etree
from spellchecker import SpellChecker

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NS = {'x': 'http://www.w3.org/1999/xhtml'}
BLOCK = {'li', 'ol', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'h5',
         'table', 'tr', 'td', 'th', 'div', 'figure'}


def btext(el):
    """itertext with spaces guaranteed at block-child boundaries."""
    parts = []
    if el.text:
        parts.append(el.text)
    for c in el:
        if not isinstance(c.tag, str):
            if c.tail:
                parts.append(c.tail)
            continue
        if etree.QName(c).localname in BLOCK:
            parts.append(' ')
            parts.append(btext(c))
            parts.append(' ')
        else:
            parts.append(btext(c))
        if c.tail:
            parts.append(c.tail)
    return ''.join(parts)


tree = etree.parse(os.path.join(ROOT, 'book/master/master.xhtml'))
texts = []
for el in tree.getroot().iter():
    if isinstance(el.tag, str) and etree.QName(el).localname in (
            'p', 'li', 'th', 'td', 'h1', 'h2', 'h3', 'h4', 'h5'):
        t = btext(el).strip()
        if t:
            texts.append(t)

WHITELIST = set('''TOEFL TED-Ed TED Goldin Acho Goleman Ali Sara Kabul Afghan Afghans
Afghanistan Nazari Abdul Raziq lingua franca ESL B2 NFL Combine quad IPA Khan
UBC Gallup aka et al etc vs per se CD AI GPA IQ OK podcast webinar
reappraisal reappraising systemic gatekeepers gatekeeper
Globalization globalization globalized behavior behavioural
multimedia multitask website websites ebook ebooks online email emails
mindset task-based real-life one-minute two-minute three-minute four-minute
five-minute role-play pair-work Oxford Cambridge British American Australian
Dari Pashto Arabic Francisco Istanbul Tokyo towards toward
self-discipline self-esteem self-fulfilling well-being open-ended follow-up
morph smartphones turnitoff pickitup theez adj unclearly unpkg
pre-internet face-to-face nightmare personify procrastinator procrastination
extrovert introvert ambivert empathy empathize empathetic normalize
prioritise prioritize organise organize colour color'''.split())
WHITELIST |= {w.lower() for w in list(WHITELIST)}

spell = SpellChecker()
unknown = collections.Counter()
hyphenated = collections.Counter()
skipped_pron = 0

CONTRACTIONS = ('’re', '’ve', '’ll', '’d', '’m', "'re", "'ve", "'ll", "'d", "'m")
COMMON_SHORT = {'the', 'a', 'an', 'is', 'of', 'to', 'in', 'on', 'and', 'or', 'it',
                'be', 'as', 'at', 'by', 'do', 'if', 'no', 'so', 'up', 'we', 'he',
                'not', 'are', 'you', 'our', 'out', 'for'}

def check_word(tok):
    """Return True if acceptable."""
    w = tok.lower()
    if w in WHITELIST or tok in WHITELIST:
        return True
    # plural possessive: students’
    if w.endswith(('’', "'")):
        return check_word(w[:-1])
    # possessive: Acho’s -> Acho
    for suf in ('’s', "'s"):
        if w.endswith(suf):
            return check_word(w[:-len(suf)])
    # n’t contractions: shouldn’t -> should, doesn’t -> does
    for suf in ('n’t', "n't"):
        if w.endswith(suf):
            return check_word(w[:-3])          # drops  n  +  apostrophe  (suffix len 3)
    # other contractions: we’ll -> we, they’re -> they
    for suf in CONTRACTIONS:
        if w.endswith(suf):
            return check_word(w[:-len(suf)])
    return w in spell

def is_stress_respelling(t):
    """Syllable-split stress lines like 'fi NAN cial', 'in VEST ment'."""
    toks = re.findall(r"[A-Za-z]+", t)
    has_caps = any(w.isupper() and len(w) >= 2 for w in toks)
    n_short = sum(1 for w in toks
                  if len(w) <= 3 and w.lower() not in COMMON_SHORT)
    frag = any(len(w) <= 4 and not w.isupper()
               and w.lower() not in COMMON_SHORT and w.lower() not in spell
               for w in toks)
    return has_caps and (n_short >= 2 or frag)

for t in texts:
    if ('→' in t) or re.search(r'/[^/]{2,}/', t) or is_stress_respelling(t):
        skipped_pron += 1
        continue
    for tok in re.findall(r"[A-Za-z][A-Za-z’'\-]*", t):
        if len(tok) < 3:
            continue                      # a, an, of, fi, op, ke … fragments
        if '-' in tok:
            hyphenated[tok.lower()] += 1  # compounds accepted; logged
            continue
        if not check_word(tok):
            unknown[tok.lower()] += 1

# ---- duplicated words -----------------------------------------------------
dups = collections.Counter()
for t in texts:
    flat = re.sub(r'\s+', ' ', t)
    for m in re.finditer(r'\b([A-Za-z’\-]+)( \1\b)', flat, re.I):
        if m.group(1).lower() not in ('had', 'that'):  # "had had" rare; check all anyway
            dups[m.group(1)] += 1

# ---- mechanics ------------------------------------------------------------
# double spaces: definitive check on raw master text nodes (extraction may
# legitimately insert spaces at block seams)
raw = open(os.path.join(ROOT, 'book/master/master.xhtml'),
           encoding='utf-8').read()
double_spaces = sum(len(re.findall(r'\S  +\S', m.group(0)))
                    for m in re.finditer(r'>[^<]*<', raw))
straight_quotes = sum(t.count('"') for t in texts)
straight_apos = sum(len(re.findall(r"[A-Za-z]'[A-Za-z]", t)) for t in texts)
space_before_punct = sum(len(re.findall(r'\s+[,.;:!?]', t)) for t in texts)

report = {
    'blocks': len(texts),
    'unknown_words': dict(unknown.most_common()),
    'hyphenated_compounds_accepted': dict(hyphenated.most_common()),
    'pronunciation_lines_skipped': skipped_pron,
    'duplicated_word_hits': dict(dups.most_common()),
    'double_spaces': double_spaces,
    'straight_quotes': straight_quotes,
    'straight_apostrophes': straight_apos,
    'space_before_punct': space_before_punct,
}
report['ok'] = (not unknown and not dups and double_spaces == 0
                and straight_quotes == 0 and straight_apos == 0
                and space_before_punct == 0)

out = os.path.join(ROOT, 'book', 'artifacts', 'qa_editorial.json')
open(out, 'w').write(json.dumps(report, indent=1, ensure_ascii=False))
print(f"blocks: {len(texts)}   pronunciation lines skipped: {skipped_pron}")
print(f"--- unknown words ({len(unknown)}) ---")
for w, c in unknown.most_common(40):
    print(f'{c:4}  {w}')
print(f"--- hyphenated compounds auto-accepted ({len(hyphenated)} types) ---")
print(', '.join(f'{w}×{c}' for w, c in hyphenated.most_common(50)))
print(f"--- duplicated words: {dict(dups)}")
print(f"double spaces: {double_spaces}  straight quotes: {straight_quotes}  "
      f"straight apostrophes: {straight_apos}  space-before-punct: {space_before_punct}")
print('OK' if report['ok'] else 'ISSUES PRESENT')

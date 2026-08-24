#!/usr/bin/env python3
"""qa_content.py — content integrity: every source paragraph must be traceable
in the master (allowing the logged removals and known transforms).

Matching strategy (v3):
  * windowed probes (head / mid / tail / number-stripped head)
  * each probe tried in three variants: exact-normalized, punctuation-loose
    (all non-alnum -> space), and squeezed (alnum only) for len >= 12
  * doubled-text fallback: source artifacts like "Unit 1Unit 1" whose halves
    each occur in the master count as covered (dedup by design, logged)
  * renamed items (Forward -> Foreword) classified, not missed
Short texts (< 60 chars) are probed whole. Writes book/artifacts/qa_content.json.
"""
import json, os, re, unicodedata
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
items = json.load(open(os.path.join(ROOT, 'book/artifacts/dump.json'), encoding='utf-8'))

BLOCK = {'li', 'ol', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'h5',
         'table', 'tr', 'td', 'th', 'div', 'figure'}


def btext(el):
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


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\xa0', ' ')
    s = re.sub(r'[“”]', '"', s)
    s = re.sub(r'[’‘]', "'", s)
    s = re.sub(r'[–—]', '-', s)
    s = re.sub(r'[✅✔❌✗]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


def loose(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', s)).strip()


def squeeze(s):
    return re.sub(r'[^a-z0-9]', '', s)


mt = norm('\n'.join(texts))
mt_loose = loose(mt)
mt_sq = squeeze(mt)
mt_exact = {norm(t) for t in texts}

# changelog originals: misses whose text matches a logged correction are
# classified, not lost
CHANGES = json.load(open(os.path.join(ROOT, 'book/artifacts/changelog.json'),
                         encoding='utf-8'))
change_loose = [loose(norm(re.sub(r'\s+', ' ', str(c.get('original', '')))))
               for c in CHANGES]
change_loose = [c for c in change_loose if len(c) >= 8]


def windows(t):
    out = []
    if len(t) < 60:
        out.append(t)
    else:
        out.append(t[:60])
        out.append(t[20:80])
        out.append(t[len(t) // 2:len(t) // 2 + 60])
        out.append(t[-60:])
    m = re.match(r'^([\divx]+[.)]\s*|[a-d][.)]\s*)+', t)
    if m:
        out.append(t[m.end():m.end() + 50])
    return [p.strip() for p in out if len(p.strip()) >= 5]


def probe_hit(t):
    if t in mt_exact:
        return True
    for w in windows(t):
        if loose(w) in mt_loose:
            return True
        if len(w) >= 8 and squeeze(w) in mt_sq:
            return True
    return False


def logged_correction(t):
    lo, sq = loose(t), squeeze(t)
    return any(c and (c in lo or lo in c or squeeze(c) in sq) for c in change_loose)


# Activity headings renumbered and their generic instructions folded into
# section headings (changelog: U1 Ch2 + each unit's Ch1 renumber entry)
KNOWN_FOLDS = {848, 853, 1169, 1175, 1872, 1878, 2246, 2252, 2619, 2625}


def dedup_covered(t):
    """Doubled source artifacts ('Name Name Unit NUnit N', possibly jammed).
    Collapse repeated substrings on the squeezed text; covered when every
    collapsed unit (or the residual string) occurs in the master."""
    sq = squeeze(t)
    if len(sq) < 12:
        return False
    units, prev = [], None
    while prev != sq:
        prev = sq
        m = re.search(r'(.{4,120}?)\1', sq)
        if m:
            units.append(m.group(1))
            sq = sq[:m.start()] + m.group(1) + sq[m.end():]
    if len(units) >= 2:
        if len(sq) >= 8 and sq in mt_sq:
            return True
        return all(len(u) >= 5 and u in mt_sq for u in units)
    # single large repeat (jam-truncated tail): unit itself must be long & present
    return (len(units) == 1 and len(units[0]) >= 12
            and len(squeeze(t)) >= 40 and units[0] in mt_sq)


# items intentionally dropped or renamed (logged in changelog)
DROPPED = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,   # old TOC + empty H1
           2026,                                    # U8 'Future of Marriage' heading
           2593}                                    # U8 mismatched T/F instruction
RENAMED = {13: 'Forward -> Foreword (locked decision)'}

missing, transforms = [], []
n_cov = n_checked = 0
for x in items:
    if x['type'] == 'table':
        for r in x.get('rows') or []:
            for c in r:
                t = norm(c['text'])
                if len(t) < 4:
                    continue
                n_checked += 1
                if probe_hit(t):
                    n_cov += 1
                elif dedup_covered(t):
                    transforms.append(('table-cell-dedup', x['i'], t[:50]))
                elif logged_correction(t):
                    transforms.append(('table-cell-logged', x['i'], t[:50]))
                else:
                    missing.append(('table-cell', x['i'], t[:70]))
        continue
    i = x['i']
    t = norm(x.get('text') or '')
    if not t or len(t) < 4 or i in DROPPED:
        continue
    n_checked += 1
    if i in RENAMED:
        transforms.append((RENAMED[i], i, t[:50]))
        continue
    if probe_hit(t):
        n_cov += 1
    elif dedup_covered(t):
        transforms.append(('dedup-by-design', i, t[:50]))
    elif logged_correction(t):
        transforms.append(('logged-correction', i, t[:50]))
    elif i in KNOWN_FOLDS:
        transforms.append(('activity-fold (changelog)', i, t[:50]))
    else:
        missing.append(('para', i, t[:90]))

report = {'checked': n_checked, 'covered': n_cov,
          'classified_transforms': transforms,
          'missing': missing, 'ok': not missing}
open(os.path.join(ROOT, 'book/artifacts/qa_content.json'), 'w').write(
    json.dumps(report, indent=1, ensure_ascii=False))
print(f"checked {n_checked} source texts: covered {n_cov}, "
      f"classified transforms {len(transforms)}, missing {len(missing)}")
for kind, i, t in missing[:60]:
    print(f'  MISS {kind} #{i}: {t}')
print('OK' if not missing else 'ISSUES PRESENT')

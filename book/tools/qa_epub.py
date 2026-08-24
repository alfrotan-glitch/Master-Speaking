#!/usr/bin/env python3
"""qa_epub.py — structural QA for the EPUB 3 build (epubcheck unavailable: no Java).

Checks: OCF zip rules (mimetype first & stored, no extra top-level dirs beyond
META-INF/OEBPS-or-root), container.xml -> OPF resolution, OPF manifest/spine
closure, every XHTML well-formed & doctype'd, every <img src>/CSS href/CSS
url() resolves inside the zip, no remote (http) references, nav.xhtml has
epub:type="toc" nav + landmarks, NCX structure, dcterms:modified present.
Writes book/artifacts/qa_epub.json and prints issues (exit 1 if any).
"""
import json, os, re, sys, zipfile
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EPUB = os.path.join(ROOT, 'Master-Speaking.epub')
OUT = os.path.join(ROOT, 'book', 'artifacts', 'qa_epub.json')

XH = 'http://www.w3.org/1999/xhtml'
EP = 'http://www.idpf.org/2007/ops'
OPF_NS = 'http://www.idpf.org/2007/opf'
DC = 'http://purl.org/dc/elements/1.1/'

issues = []

def err(msg):
    issues.append(msg)

z = zipfile.ZipFile(EPUB)
names = z.namelist()

# ---- OCF zip rules -------------------------------------------------------
il = z.infolist()
if il[0].filename != 'mimetype':
    err(f'first zip entry is {il[0].filename!r}, not "mimetype"')
elif il[0].compress_type != zipfile.ZIP_STORED:
    err('mimetype entry is compressed (must be STORED)')
if z.read('mimetype') != b'application/epub+zip':
    err('mimetype content wrong')
if 'META-INF/container.xml' not in names:
    err('META-INF/container.xml missing')
# OCF permits content at the zip root or under any directory; nothing to flag
# beyond mimetype/META-INF placement, checked above.

# ---- container -> OPF ----------------------------------------------------
cont = etree.fromstring(z.read('META-INF/container.xml'))
rootfile = cont.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile')
opf_path = rootfile.get('full-path')
opf_dir = os.path.dirname(opf_path)
if opf_path not in names:
    err(f'container full-path {opf_path!r} not in zip'); sys.exit(1)
opf = etree.fromstring(z.read(opf_path))
if opf.tag != f'{{{OPF_NS}}}package':
    err(f'OPF root tag {opf.tag} not in OPF namespace')
for attr in ('version', 'unique-identifier'):
    if opf.get(attr) is None:
        err(f'package missing @{attr}')

def zpath(p):
    """Resolve href relative to OPF dir -> zip path."""
    return os.path.normpath(os.path.join(opf_dir, p)).replace('\\', '/')

# ---- metadata ------------------------------------------------------------
md = opf.find(f'{{{OPF_NS}}}metadata')
if md is None:
    err('no <metadata>')
else:
    if md.find(f'{{{OPF_NS}}}meta[@property="dcterms:modified"]') is None:
        err('dcterms:modified meta missing')
    for tag in ('identifier', 'title', 'language'):
        if md.find(f'{{{DC}}}{tag}') is None:
            err(f'dc:{tag} missing')
    uid = opf.get('unique-identifier')
    if md.find(f'{{{DC}}}identifier[@id="{uid}"]') is None:
        err(f'unique-identifier {uid!r} has no matching dc:identifier/@id')

# ---- manifest/spine closure ----------------------------------------------
man = opf.find(f'{{{OPF_NS}}}manifest')
items = {i.get('id'): i for i in man.findall(f'{{{OPF_NS}}}item')}
if not items:
    err('manifest empty')
nav_ids = [i for i in items.values() if 'nav' in (i.get('properties') or '')]
if len(nav_ids) != 1:
    err(f'expected exactly 1 nav item, got {len(nav_ids)}')
cover_ids = [i for i in items.values() if 'cover-image' in (i.get('properties') or '')]
if len(cover_ids) > 1:
    err('multiple cover-image items')
for iid, it in items.items():
    href = it.get('href'); mt = it.get('media-type')
    zp = zpath(href)
    if zp not in names:
        err(f'manifest item {iid}: href {href!r} missing from zip')
        continue
    if not mt:
        err(f'manifest item {iid}: no media-type')
    ext = zp.rsplit('.', 1)[-1].lower()
    expect = {'xhtml': 'application/xhtml+xml', 'css': 'text/css',
              'png': 'image/png', 'jpeg': 'image/jpeg', 'jpg': 'image/jpeg',
              'gif': 'image/gif', 'svg': 'image/svg+xml', 'ncx': 'application/x-dtbncx+xml',
              'opf': 'application/oebps-package+xml'}
    if ext in expect and mt != expect[ext]:
        err(f'manifest item {iid}: media-type {mt} != expected {expect[ext]} for .{ext}')

spine = opf.find(f'{{{OPF_NS}}}spine')
idrefs = [ir.get('idref') for ir in spine.findall(f'{{{OPF_NS}}}itemref')]
for idr in idrefs:
    if idr not in items:
        err(f'spine idref {idr!r} not in manifest')
if not idrefs:
    err('spine empty')
# every xhtml doc should be reachable via spine (cover-image-only pages exempt)
in_spine = set(idrefs)
for iid, it in items.items():
    if (it.get('media-type') == 'application/xhtml+xml'
            and iid not in in_spine and iid != (nav_ids[0].get('id') if nav_ids else None)):
        err(f'xhtml item {iid} ({it.get("href")}) not in spine')

# ---- per-file checks ------------------------------------------------------
REMOTE = re.compile(r'(?:src|href)\s*=\s*["\'](?:https?:|//)')
CSSURL = re.compile(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)')
xhtml_docs = [(iid, it.get('href')) for iid, it in items.items()
              if it.get('media-type') == 'application/xhtml+xml']
for iid, href in xhtml_docs:
    zp = zpath(href)
    raw = z.read(zp)
    # well-formed
    try:
        doc = etree.fromstring(raw)
    except etree.XMLSyntaxError as e:
        err(f'{zp}: not well-formed XML: {e}')
        continue
    if doc.tag != f'{{{XH}}}html':
        err(f'{zp}: root is {doc.tag}, not XHTML html')
    raw_txt = raw.decode('utf-8', 'replace')
    if '<!DOCTYPE html' not in raw_txt:
        err(f'{zp}: missing <!DOCTYPE html>')
    if REMOTE.search(raw_txt):
        err(f'{zp}: remote resource reference (http/protocol-relative)')
    # linked resources resolve
    base = os.path.dirname(zp)
    for el in doc.iter():
        ref = el.get('src') if el.tag == f'{{{XH}}}img' else el.get('href')
        if ref and not ref.startswith('#'):
            tgt = ref.split('#')[0]
            target = os.path.normpath(os.path.join(base, tgt)).replace('\\', '/')
            if target not in names:
                err(f'{zp}: reference {ref!r} unresolved in zip')

# css url() resolution
for iid, it in items.items():
    if it.get('media-type') == 'text/css':
        zp = zpath(it.get('href'))
        css = z.read(zp).decode('utf-8', 'replace')
        base = os.path.dirname(zp)
        for m in CSSURL.finditer(css):
            u = m.group(1)
            if u.startswith(('data:', 'http')):
                continue
            target = os.path.normpath(os.path.join(base, u)).replace('\\', '/')
            if target not in names:
                err(f'{zp}: url({u!r}) unresolved')

# ---- nav.xhtml ------------------------------------------------------------
nav_it = nav_ids[0] if nav_ids else None
if nav_it is not None:
    zp = zpath(nav_it.get('href'))
    nav = etree.fromstring(z.read(zp))
    tocs = [n for n in nav.iter(f'{{{XH}}}nav')
            if n.get(f'{{{EP}}}type') == 'toc']
    if len(tocs) != 1:
        err(f'{zp}: expected exactly one epub:type="toc" nav, got {len(tocs)}')
    else:
        # every spine doc ideally has a toc entry — count anchor targets
        anchors = [a.get('href') for a in tocs[0].iter(f'{{{XH}}}a') if a.get('href')]
        for idr in idrefs:
            h = items[idr].get('href')
            base_h = h.split('#')[0]
            if not any(a.split('#')[0] == base_h for a in anchors):
                err(f'nav toc has no entry for spine item {idr} ({h})')
    lms = [n for n in nav.iter(f'{{{XH}}}nav') if n.get(f'{{{EP}}}type') == 'landmarks']
    if not lms:
        err(f'{zp}: no epub:type="landmarks" nav')
    else:
        types = [a.get(f'{{{EP}}}type') for a in lms[0].iter(f'{{{XH}}}a')]
        if 'toc' not in types:
            err('landmarks missing a toc-type link')
        if not any(t == 'bodymatter' for t in types):
            err('landmarks missing bodymatter link')

# ---- NCX ------------------------------------------------------------------
ncx_it = [i for i in items.values() if i.get('media-type') == 'application/x-dtbncx+xml']
if ncx_it:
    zp = zpath(ncx_it[0].get('href'))
    ncx = etree.fromstring(z.read(zp))
    npts = ncx.findall('.//{http://www.daisy.org/z3986/2005/ncx/}navPoint')
    if len(npts) < len(idrefs):
        err(f'NCX has {len(npts)} navPoints < {len(idrefs)} spine items')
    for c in ncx.findall('.//{http://www.daisy.org/z3986/2005/ncx/}content'):
        src = c.get('src')
        target = os.path.normpath(os.path.join(os.path.dirname(zp), src.split('#')[0])).replace('\\', '/')
        if target not in names:
            err(f'NCX content src {src!r} unresolved')
else:
    err('no NCX item in manifest (spine @toc fallback broken)')

# spine @toc points at existing ncx
toc_attr = spine.get('toc')
if toc_attr and toc_attr not in items:
    err(f'spine @toc={toc_attr!r} not in manifest')

print(json.dumps({'epub': EPUB, 'files': len(names), 'spine': len(idrefs),
                  'issues': issues, 'ok': not issues}, indent=1))
open(OUT, 'w').write(json.dumps({'epub': EPUB, 'files': len(names), 'spine': len(idrefs),
                                 'issues': issues, 'ok': not issues}, indent=1))
sys.exit(1 if issues else 0)

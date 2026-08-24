#!/usr/bin/env python3
"""epub.py — build the reflowable EPUB 3 from book/master/master.xhtml.

Structure: one XHTML file per front-matter piece + per unit opener + per
chapter (32 files), EPUB-style stylesheet in em/% units, nav.xhtml (toc +
landmarks), NCX for legacy reading systems, all 24 images (gif -> png).
"""
import os, re, shutil, zipfile, uuid, datetime, html
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER = os.path.join(ROOT, 'book', 'master', 'master.xhtml')
IMAGES_SRC = os.path.join(ROOT, 'book', 'assets', 'images')
OUT = os.path.join(ROOT, 'Master-Speaking.epub')
WORK = os.path.join(ROOT, 'book', 'artifacts', 'epub')

NS = {'x': 'http://www.w3.org/1999/xhtml'}
XH = 'http://www.w3.org/1999/xhtml'
EP = 'http://www.idpf.org/2007/ops'

CSS = '''/* Master Speaking — reflowable EPUB stylesheet */
html { font-size: 100%; }
body { line-height: 1.45; margin: 0 0.2em; padding: 0 0.4em;
       font-family: "Source Serif 4", Georgia, serif; color: #14181A; }
h1, h2, h3, h4, h5 { font-family: "Source Sans 3", Helvetica, sans-serif;
                     color: #14181A; font-weight: 600; line-height: 1.25; }
p { margin: 0 0 0.65em 0; text-align: justify; hyphens: auto; }
/* unit opener */
section.unit { margin-top: 1em; }
h1.unit-title { font-size: 1.7em; margin: 0.2em 0 0.4em 0; }
.unit-kicker { display: block; font-size: 0.85em; letter-spacing: 0.12em;
               text-transform: uppercase; color: #0E6E5C; font-weight: 600; }
.unit-name { display: block; }
figure.unit-figure { margin: 1em 0; text-align: center; }
img { max-width: 100%; height: auto; }
/* chapters */
h2.chapter-title { font-size: 1.35em; margin: 0 0 0.6em 0; }
.chapter-kicker { display: block; font-size: 0.8em; letter-spacing: 0.1em;
                  text-transform: uppercase; color: #0E6E5C; }
.chapter-name { display: block; }
/* sections */
h3.sec { font-size: 1.12em; margin: 1.2em 0 0.35em 0; color: #14181A; }
h4.sub, h4.reading-title { font-size: 1.0em; margin: 0.9em 0 0.3em 0;
                           color: #0E6E5C; }
h4.reading-title { color: #14181A; font-size: 1.15em; font-family: inherit; }
h5.runin { font-size: 0.9em; margin: 0.8em 0 0.2em 0; }
/* content types */
p.instr { font-family: "Source Sans 3", Helvetica, sans-serif; font-style: italic;
          font-size: 0.92em; color: #5A6B66; text-align: left; }
p.label { font-family: "Source Sans 3", Helvetica, sans-serif; font-weight: 600;
          font-size: 0.95em; text-align: left; }
p.topic { font-family: "Source Sans 3", Helvetica, sans-serif; font-weight: 600;
          color: #0E6E5C; text-align: left; }
p.titleline { font-style: italic; text-align: left; }
p.media-title { font-family: "Source Sans 3", Helvetica, sans-serif;
                font-weight: 600; font-size: 1.05em; text-align: left; }
div.reading-block { border-left: 3px solid #0E6E5C; padding-left: 0.7em;
                    margin: 0.5em 0 0.8em 0; }
p.reading { text-align: justify; }
div.note { background-color: #F1F6F4; border-left: 3px solid #0E6E5C;
           padding: 0.5em 0.7em; margin: 0.6em 0; }
div.note p { font-style: italic; color: #44544F; text-align: left; }
/* lists */
ol.questions { margin: 0.3em 0 0.7em 1.4em; padding: 0; }
ol.questions > li { margin-bottom: 0.55em; list-style: decimal; }
ol.options { margin: 0.25em 0 0.2em 1.6em; padding: 0; }
ol.options li { list-style: upper-alpha; margin-bottom: 0.15em; }
ol.options.standalone { margin-left: 0; }
ul.tf, ul.fill { margin: 0.3em 0 0.7em 1.4em; padding: 0; }
ul.tf li, ul.fill li { list-style: none; margin-bottom: 0.45em; }
ul.pairs, ul.choices, ul.items { margin: 0.3em 0 0.7em 1.4em; padding: 0; }
ul.pairs li, ul.choices li, ul.items li { margin-bottom: 0.25em; }
/* tables */
table { border-collapse: collapse; width: 100%; margin: 0.5em 0 0.9em 0;
        font-size: 0.88em; }
th { background-color: #0E6E5C; color: #fff; text-align: left; padding: 0.35em 0.5em;
     font-family: "Source Sans 3", Helvetica, sans-serif; }
td { border: 1px solid #C7D4D0; padding: 0.35em 0.5em; vertical-align: top; }
tbody tr:nth-child(even) td { background-color: #F1F6F4; }
table.questions td { border: none; border-bottom: 1px solid #C7D4D0; }
table.questions td:empty { min-height: 1.6em; }
/* warm-up box */
div.warmup { background-color: #F1F6F4; border-left: 4px solid #0E6E5C;
             padding: 0.6em 0.8em; margin: 0.8em 0; }
h2.warmup-head { font-size: 1.0em; letter-spacing: 0.08em; text-transform: uppercase;
                 color: #0E6E5C; margin: 0 0 0.3em 0; }
/* front matter */
h1.fm-head { font-size: 1.5em; margin: 0.2em 0 0.7em 0; }
h2.fm-sub { font-size: 1.1em; color: #0E6E5C; margin: 1em 0 0.3em 0; }
h3.fm-sub2 { font-size: 1.0em; margin: 0.8em 0 0.2em 0; }
blockquote { margin: 2em 2.5em; font-style: italic; text-align: center; }
p.signature { font-family: "Source Sans 3", Helvetica, sans-serif; font-weight: 600;
              margin-top: 1.2em; }
/* nav */
nav#toc ol { list-style: none; margin-left: 0.6em; }
nav#toc ol ol { list-style: none; }
nav#toc li { margin: 0.2em 0; }
'''

def q(el, p):
    return el.xpath(p, namespaces=NS)

def local(tag):
    return etree.QName(tag).localname

def wrap_doc(title, body_children):
    root = etree.Element(f'{{{XH}}}html', nsmap={None: XH, 'epub': EP})
    root.set('lang', 'en')
    head = etree.SubElement(root, f'{{{XH}}}head')
    t = etree.SubElement(head, f'{{{XH}}}title'); t.text = title
    mt = etree.SubElement(head, f'{{{XH}}}meta'); mt.set('charset', 'utf-8')
    ln = etree.SubElement(head, f'{{{XH}}}link')
    ln.set('rel', 'stylesheet'); ln.set('type', 'text/css'); ln.set('href', 'style.css')
    body = etree.SubElement(root, f'{{{XH}}}body')
    for c in body_children:
        body.append(c)
    return root

def serialize(root):
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8',
                          doctype='<!DOCTYPE html>', pretty_print=True)

def copy_children(sec, tweak=None):
    out = []
    for c in sec:
        if isinstance(c.tag, str):
            out.append(c)
    return out

def fix_img_paths(el, prefix=''):
    for img in el.iter(f'{{{XH}}}img'):
        src = img.get('src') or ''
        base = os.path.basename(src)
        # master may reference .gif; the png twin ships instead (pdf.py does the same)
        if base.endswith('.gif') and os.path.exists(
                os.path.join(IMAGES_SRC, base[:-4] + '.png')):
            base = base[:-4] + '.png'
        img.set('src', prefix + 'images/' + base)

def strip_ids(el):
    for n in el.iter():
        if n.get('id'):
            del n.attrib['id']

def main():
    if os.path.exists(WORK):
        shutil.rmtree(WORK)
    os.makedirs(os.path.join(WORK, 'images'))

    tree = etree.parse(MASTER)
    body = tree.getroot().find('x:body', NS)

    manifest = []          # (id, href, media-type, properties)
    spine = []             # (idref, linear)
    nav_items = []         # (level, label, href)

    def add_xhtml(fname, title, children, toc_label=None, toc_level=None,
                  toc_children=None, landmark=None):
        root = wrap_doc(title, children)
        data = serialize(root)
        open(os.path.join(WORK, fname), 'wb').write(data)
        props = 'svg' if b'<svg' in data else None
        manifest.append((fname.rsplit('.',1)[0], fname,
                         'application/xhtml+xml', props))
        spine.append((fname.rsplit('.',1)[0], 'yes'))
        if toc_label:
            nav_items.append((toc_level or 1, toc_label, fname, toc_children))

    # ---- front matter --------------------------------------------------
    for sec in body:
        part = sec.get('data-part')
        cls = sec.get('class') or ''
        children = copy_children(sec)
        for c in children:
            fix_img_paths(c)
        if part == 'half-title':
            continue                      # not needed in reflowable EPUB
        elif part == 'title-page':
            add_xhtml('title.xhtml', 'Master Speaking', children, 'Title Page', 1)
        elif part == 'copyright':
            add_xhtml('copyright.xhtml', 'Copyright', children, 'Copyright', 1)
        elif part == 'foreword':
            add_xhtml('foreword.xhtml', 'Foreword', children,
                      'Foreword', 1, None, ('bodymatter', None))
            nav_items[-1] = (1, 'Foreword', 'foreword.xhtml', None)
        elif part == 'how-to-use':
            add_xhtml('how-to-use.xhtml', 'How to Use This Book', children,
                      'How to Use This Book', 1)
        elif part == 'epigraph':
            add_xhtml('epigraph.xhtml', 'Epigraph', children, 'Epigraph', 1)

    # ---- units ----------------------------------------------------------
    for unit in q(body, './x:section[@class="unit"]'):
        unum = int(unit.get('data-unit'))
        uid = f'unit{unum}'
        utitle = q(unit, './/x:span[@class="unit-name"]/text()')[0]
        # unit file: opener + warmup
        opener_children = []
        h1 = unit.find('x:h1', NS)
        opener_children.append(h1)
        fig = unit.find('x:figure', NS)
        if fig is not None:
            opener_children.append(fig)
        warm = unit.find('x:div[@class="warmup"]', NS)
        if warm is not None:
            opener_children.append(warm)
        chapters_nav = []
        for ch_sec in q(unit, './x:section[@class="chapter"]'):
            cnum = int(ch_sec.get('data-chapter'))
            cname = q(ch_sec, './x:h2/x:span[@class="chapter-name"]/text()')[0]
            fname = f'unit{unum}-ch{cnum}.xhtml'
            children = copy_children(ch_sec)
            for c in children:
                fix_img_paths(c)
                strip_ids(c)
            add_xhtml(fname, f'Unit {unum} · {cname}', children)
            chapters_nav.append((2, f'Chapter {cnum} · {cname}', fname, None))
        for c in opener_children:
            fix_img_paths(c)
        add_xhtml(f'{uid}.xhtml', f'Unit {unum} — {utitle}', opener_children,
                  f'Unit {unum} · {utitle}', 1, chapters_nav)

    # ---- nav doc ---------------------------------------------------------
    nav_root = etree.Element(f'{{{XH}}}html', nsmap={None: XH, 'epub': EP})
    nav_root.set('lang', 'en')
    head = etree.SubElement(nav_root, f'{{{XH}}}head')
    t = etree.SubElement(head, f'{{{XH}}}title'); t.text = 'Master Speaking'
    mt = etree.SubElement(head, f'{{{XH}}}meta'); mt.set('charset', 'utf-8')
    bodynav = etree.SubElement(nav_root, f'{{{XH}}}body')
    nav = etree.SubElement(bodynav, f'{{{XH}}}nav',
                           {f'{{{EP}}}type': 'toc', 'id': 'toc', 'hidden': 'hidden'})
    h = etree.SubElement(nav, f'{{{XH}}}h1'); h.text = 'Contents'
    def build_ol(items, parent):
        ol = etree.SubElement(parent, f'{{{XH}}}ol')
        for lvl, label, href, children in items:
            li = etree.SubElement(ol, f'{{{XH}}}li')
            a = etree.SubElement(li, f'{{{XH}}}a', href=href); a.text = label
            if children:
                build_ol(children, li)
    build_ol(nav_items, nav)
    lnav = etree.SubElement(bodynav, f'{{{XH}}}nav', {f'{{{EP}}}type': 'landmarks',
                                                      'id': 'landmarks', 'hidden': 'hidden'})
    h2 = etree.SubElement(lnav, f'{{{XH}}}h2'); h2.text = 'Landmarks'
    ol = etree.SubElement(lnav, f'{{{XH}}}ol')
    for typ, label, href in [('ibook', None, None)][:0]:
        pass
    ol_items = [('toc', 'Contents', 'nav.xhtml#toc'),
                ('bodymatter', 'Start of Content', 'foreword.xhtml')]
    for typ, label, href in ol_items:
        li = etree.SubElement(ol, f'{{{XH}}}li')
        a = etree.SubElement(li, f'{{{XH}}}a', {f'{{{EP}}}type': typ, 'href': href})
        a.text = label
    open(os.path.join(WORK, 'nav.xhtml'), 'wb').write(serialize(nav_root))
    manifest.append(('nav', 'nav.xhtml', 'application/xhtml+xml', 'nav'))

    # ---- css + images -----------------------------------------------------
    open(os.path.join(WORK, 'style.css'), 'w').write(CSS)
    manifest.append(('css', 'style.css', 'text/css', None))
    for f in sorted(os.listdir(IMAGES_SRC)):
        if f.endswith('.gif'):
            continue
        shutil.copy(os.path.join(IMAGES_SRC, f), os.path.join(WORK, 'images', f))
        mt = 'image/png' if f.endswith('.png') else 'image/jpeg'
        manifest.append(('img-' + f.rsplit('.',1)[0], 'images/' + f, mt, None))

    # ---- NCX (EPUB2 compat) ----------------------------------------------
    ncx = etree.Element('ncx', nsmap={None: 'http://www.daisy.org/z3986/2005/ncx/'},
                        version='2005-1')
    headn = etree.SubElement(ncx, 'head')
    m = etree.SubElement(headn, 'meta', name='dtb:uid', content=f'urn:uuid:{UID}')
    m2 = etree.SubElement(headn, 'meta', name='dtb:depth', content='2')
    m3 = etree.SubElement(headn, 'meta', name='dtb:totalPageCount', content='0')
    m4 = etree.SubElement(headn, 'meta', name='dtb:maxPageNumber', content='0')
    doc_title = etree.SubElement(ncx, 'docTitle')
    tt = etree.SubElement(doc_title, 'text'); tt.text = 'Master Speaking'
    navmap = etree.SubElement(ncx, 'navMap')
    pid = 0
    def ncx_items(items, parent):
        nonlocal pid
        for lvl, label, href, children in items:
            pid += 1
            np_ = etree.SubElement(parent, 'navPoint',
                                   id=f'np{pid}', playOrder=str(pid))
            nl = etree.SubElement(np_, 'navLabel')
            nlt = etree.SubElement(nl, 'text'); nlt.text = label
            nc = etree.SubElement(np_, 'content', src=href)
            if children:
                ncx_items(children, np_)
    ncx_items(nav_items, navmap)
    open(os.path.join(WORK, 'toc.ncx'), 'wb').write(
        etree.tostring(ncx, xml_declaration=True, encoding='UTF-8', pretty_print=True))
    manifest.append(('ncx', 'toc.ncx', 'application/x-dtbncx+xml', None))

    # ---- OPF ---------------------------------------------------------------
    OPF = 'http://www.idpf.org/2007/opf'
    DC = 'http://purl.org/dc/elements/1.1/'
    opf = etree.Element(f'{{{OPF}}}package', nsmap={None: OPF, 'dc': DC},
                        version='3.0', **{'unique-identifier': 'pub-id'})
    md = etree.SubElement(opf, f'{{{OPF}}}metadata')
    def dc(tag, text, **attrs):
        e = etree.SubElement(md, f'{{{DC}}}{tag}')
        e.text = text
        for k, v in attrs.items():
            e.set(k, v)
        return e
    dc('identifier', f'urn:uuid:{UID}', id='pub-id')
    dc('title', 'Master Speaking')
    dc('creator', 'Abdul Raziq Nazari')
    dc('language', 'en')
    dc('date', datetime.date.today().isoformat())
    dc('description', 'A speaking course for advanced English learners: eight units on communication, goals, emotional intelligence, money, AI, marriage, globalization, and English as a lingua franca.')
    meta = etree.SubElement(md, f'{{{OPF}}}meta', {'property': 'dcterms:modified'})
    meta.text = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    man = etree.SubElement(opf, f'{{{OPF}}}manifest')
    for mid, href, mtype, props in manifest:
        e = etree.SubElement(man, f'{{{OPF}}}item', id=mid, href=href,
                             **{'media-type': mtype})
        if props:
            e.set('properties', props)
    spine_el = etree.SubElement(opf, f'{{{OPF}}}spine', **{'toc': 'ncx'})
    for idref, linear in spine:
        etree.SubElement(spine_el, f'{{{OPF}}}itemref', idref=idref, linear=linear)
    guide = etree.SubElement(opf, f'{{{OPF}}}guide')
    for typ, label, href in [('toc', 'Contents', 'nav.xhtml#toc'),
                             ('text', 'Begin Reading', 'foreword.xhtml')]:
        etree.SubElement(guide, f'{{{OPF}}}reference', type=typ, title=label,
                         href=href)

    opf_data = etree.tostring(opf, xml_declaration=True, encoding='UTF-8',
                              pretty_print=True)
    open(os.path.join(WORK, 'content.opf'), 'wb').write(opf_data)

    # ---- container + zip ----------------------------------------------------
    os.makedirs(os.path.join(WORK, 'META-INF'), exist_ok=True)
    container = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
'''
    open(os.path.join(WORK, 'META-INF', 'container.xml'), 'w').write(container)
    mimetype = 'application/epub+zip'

    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, 'w') as z:
        z.writestr('mimetype', mimetype, compress_type=zipfile.ZIP_STORED)
        for base, dirs, files in os.walk(WORK):
            for f in sorted(files):
                full = os.path.join(base, f)
                rel = os.path.relpath(full, WORK)
                z.write(full, rel, compress_type=zipfile.ZIP_DEFLATED)
    print('EPUB written:', OUT, f'({os.path.getsize(OUT):,} bytes, '
          f'{len(spine)} spine items)')

UID = str(uuid.uuid5(uuid.NAMESPACE_URL, 'Master Speaking / Abdul Raziq Nazari / 2026'))

if __name__ == '__main__':
    main()

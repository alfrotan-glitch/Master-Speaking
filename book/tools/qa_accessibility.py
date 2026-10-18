#!/usr/bin/env python3
"""Defined Word/EPUB accessibility regressions, not accessibility certification."""
from copy import deepcopy
from pathlib import Path, PurePosixPath
import hashlib
import json
import posixpath
import re
import zipfile
from lxml import etree
from image_accessibility import descriptions

ROOT = Path(__file__).resolve().parents[2]
XH = 'http://www.w3.org/1999/xhtml'
NS = {'x': XH, 'o': 'http://www.idpf.org/2007/opf'}
XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'


def parse(data):
    return etree.fromstring(data, etree.XMLParser(resolve_entities=False, no_network=True))


def inspect_epub(files, expected, digests):
    issues = []
    images = 0
    chapters = 0
    seen = []
    for name, data in files.items():
        if not name.endswith('.xhtml'):
            continue
        doc = parse(data)
        if doc.get('lang') != 'en' or doc.get(XML_LANG) != 'en':
            issues.append(f'{name}: missing English language attributes')
        headings = doc.xpath('//x:h1|//x:h2|//x:h3|//x:h4|//x:h5|//x:h6', namespaces=NS)
        if re.search(r'unit\d+-ch\d+\.xhtml$', name):
            chapters += 1
            if not headings or headings[0].tag != f'{{{XH}}}h1':
                issues.append(f'{name}: chapter does not start with h1')
        previous = 0
        for heading in headings:
            level = int(etree.QName(heading).localname[1])
            if level > previous + 1:
                issues.append(f'{name}: skipped heading level {previous} to {level}')
            previous = level
        for image in doc.xpath('//x:img', namespaces=NS):
            images += 1
            base = PurePosixPath(image.get('src', '')).name
            seen.append(base)
            path = posixpath.normpath(posixpath.join(posixpath.dirname(name), image.get('src', '')))
            if path not in files or hashlib.sha256(files[path]).hexdigest() != digests.get(base):
                issues.append(f'{name}: image bytes do not match the reviewed asset: {base}')
            if base not in expected or image.get('alt') != expected.get(base):
                issues.append(f'{name}: missing, generic or stale description: {base}')
        for header in doc.xpath('//x:th', namespaces=NS):
            if header.get('scope') != 'col':
                issues.append(f'{name}: table column header without scope')
    if set(seen) != set(expected) or len(seen) != len(set(seen)):
        issues.append('Each reviewed EPUB image must appear exactly once')
    if images != 25 or chapters != 32:
        issues.append(f'Expected 25 images/32 chapters, found {images}/{chapters}')
    nav = parse(files['nav.xhtml'])
    for section in nav.xpath('//x:nav', namespaces=NS):
        if not section.get('aria-label'):
            issues.append('Navigation region lacks a label')
        for link in section.xpath('.//x:a', namespaces=NS):
            href = link.get('href', '')
            path, _, fragment = href.partition('#')
            path = posixpath.normpath(path or 'nav.xhtml')
            if path not in files:
                issues.append(f'Broken navigation target: {href}')
            elif fragment and not parse(files[path]).xpath('//*[@id=$id]', id=fragment):
                issues.append(f'Broken navigation fragment: {href}')
    opf = parse(files['content.opf'])
    properties = {}
    for element in opf.xpath('./o:metadata/o:meta', namespaces=NS):
        properties.setdefault(element.get('property'), []).append(element.text or '')
    needed = {'alternativeText', 'structuralNavigation', 'tableOfContents'}
    if not needed <= set(properties.get('schema:accessibilityFeature', [])):
        issues.append('Missing implemented accessibility features in metadata')
    summary = ' '.join(properties.get('schema:accessibilitySummary', []))
    if 'not been evaluated' not in summary or 'no recorded audio is supplied' not in summary:
        issues.append('Accessibility summary must explain evaluation and listening limitations')
    if properties.get('dcterms:conformsTo') or properties.get('a11y:certifiedBy'):
        issues.append('Conformance/certification claim requires independent supporting evidence')
    return issues


def main():
    expected = descriptions()  # Also verifies every described source-image hash.
    record = json.loads((ROOT / 'book/master/image-descriptions.json').read_text())
    issues = []
    tree = parse((ROOT / 'book/master/master.xhtml').read_bytes())
    master_images = tree.xpath('//x:img', namespaces=NS)
    if len(master_images) != 24:
        issues.append('Expected 24 interior image placements in master')
    for image in master_images:
        base = PurePosixPath(image.get('src')).name
        if image.get('alt') != expected.get(base):
            issues.append(f'Master description mismatch: {base}')
    with zipfile.ZipFile(ROOT / 'Master-Speaking.epub') as z:
        files = {name: z.read(name) for name in z.namelist()}
    epub_expected = {entry['file']: entry['alt'] for entry in record['images']}
    digests = {entry['file']: entry['sha256'] for entry in record['images']}
    issues += inspect_epub(files, epub_expected, digests)
    # Require correct descriptions on the actual Word image, not just a count
    # of nonempty descriptions that could be attached to the wrong drawings.
    by_hash = {entry['sha256']: entry['alt'] for entry in record['images'] if entry['file'] != 'cover.png'}
    wn = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
          'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
          'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
          'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    with zipfile.ZipFile(ROOT / 'Master-Speaking-7x10.docx') as z:
        document = parse(z.read('word/document.xml'))
        rels = {e.get('Id'): e.get('Target') for e in parse(z.read('word/_rels/document.xml.rels'))}
        drawings = document.xpath('//w:drawing', namespaces=wn)
        if len(drawings) != 24:
            issues.append('Expected 24 described Word drawings')
        seen_word_images = []
        for drawing in drawings:
            prop = drawing.find('.//wp:docPr', wn)
            blip = drawing.find('.//a:blip', wn)
            if prop is None or blip is None:
                issues.append('Word drawing missing description or image reference')
                continue
            target = rels[blip.get(f'{{{wn["r"]}}}embed')]
            path = posixpath.normpath('word/' + target)
            digest = hashlib.sha256(z.read(path)).hexdigest()
            seen_word_images.append(digest)
            if digest not in by_hash or prop.get('descr') != by_hash.get(digest):
                issues.append(f'Word image/description mismatch: {path}')
    if set(seen_word_images) != set(by_hash) or len(seen_word_images) != len(set(seen_word_images)):
        issues.append('Each reviewed interior image must appear exactly once in Word')
    # Negative controls must fail without changing publication files.
    bad_alt = deepcopy(files)
    doc = parse(bad_alt['unit1.xhtml'])
    doc.find('.//x:img', NS).set('alt', 'Illustration')
    bad_alt['unit1.xhtml'] = etree.tostring(doc)
    bad_nav = deepcopy(files)
    nav = parse(bad_nav['nav.xhtml'])
    nav.find('.//x:a', NS).set('href', 'missing-chapter.xhtml')
    bad_nav['nav.xhtml'] = etree.tostring(nav)
    mutations = {'generic_description_rejected': bool(inspect_epub(bad_alt, epub_expected, digests)),
                 'broken_navigation_rejected': bool(inspect_epub(bad_nav, epub_expected, digests))}
    for label, name, xpath, attribute, value in [
        ('missing_language_rejected', 'unit1.xhtml', '.', XML_LANG, None),
        ('chapter_heading_regression_rejected', 'unit1-ch1.xhtml', './/x:h1', None, f'{{{XH}}}h2'),
        ('missing_header_scope_rejected', 'unit1-ch1.xhtml', './/x:th', 'scope', None),
        ('broken_navigation_fragment_rejected', 'nav.xhtml', './/x:a', 'href', 'unit1.xhtml#missing-id')]:
        variant = deepcopy(files)
        doc = parse(variant[name])
        target = doc.find(xpath, NS) if xpath != '.' else doc
        if attribute is None:
            target.tag = value
        elif value is None:
            target.attrib.pop(attribute)
        else:
            target.set(attribute, value)
        variant[name] = etree.tostring(doc)
        mutations[label] = bool(inspect_epub(variant, epub_expected, digests))
    swapped = deepcopy(files)
    a = parse(files['unit1.xhtml']).find('.//x:img', NS).get('src')
    b = parse(files['unit1-ch1.xhtml']).find('.//x:img', NS).get('src')
    swapped[a], swapped[b] = files[b], files[a]
    mutations['wrong_image_bytes_rejected'] = bool(inspect_epub(swapped, epub_expected, digests))
    if not all(mutations.values()):
        issues.append('A negative-control mutation was not detected')
    report = {'ok': not issues, 'reviewed_interior_images': 24, 'reviewed_cover_images': 1,
              'word_drawings_checked': len(drawings), 'epub_chapters_checked': 32,
              'mutations': mutations, 'issues': issues,
              'scope': 'Source-hashed image descriptions matched to Word drawings and EPUB; heading/language/navigation/table/metadata checks. Not screen-reader/device testing, tagged PDF, independent accessibility certification or rights clearance.'}
    (ROOT / 'book/artifacts/qa_accessibility.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Freshness, edition identity, and source-material exclusion checks."""
from pathlib import Path
import hashlib
import json
import uuid
import zipfile

from lxml import etree

ROOT = Path(__file__).resolve().parents[2]
STANDARD = ROOT / 'book/standard'


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def load(name):
    return json.loads((STANDARD / name).read_text())


def image_hashes(package_path):
    image_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tif', '.tiff', '.wdp')
    with zipfile.ZipFile(package_path) as archive:
        return {
            sha_bytes(archive.read(name))
            for name in archive.namelist()
            if name.lower().endswith(image_exts)
        }


manifest = load('build-manifest.json')
issues = []


def check(condition, message):
    if not condition:
        issues.append(message)


check(sha_file(ROOT / manifest['source']) == manifest['source_sha256'],
      'Original manuscript hash mismatch')
for name, expected in manifest['outputs'].items():
    check(sha_file(ROOT / name) == expected, f'Output hash mismatch: {name}')
check(sha_file(STANDARD / 'book.json') == manifest['semantic_sha256'],
      'Semantic book changed since build')
check(sha_file(STANDARD / 'master.xhtml') == manifest['master_sha256'],
      'Master changed since build')
check(manifest.get('publication_status') == 'Review proof; not approved for publication.',
      'Review-only status missing from build manifest')
check('excluded from exports' in manifest.get('scope', ''),
      'Build scope does not describe source-art exclusion')
check('excluded from exports' in manifest.get('rights_status', ''),
      'Build rights status does not describe source-art exclusion')

master_text = (STANDARD / 'master.xhtml').read_text()
check('Review proof; not approved for publication.' in master_text,
      'Review-only notice missing from the semantic master')
for name, expected in load('protected-inputs.json')['sha256'].items():
    check(sha_file(ROOT / name) == expected,
          f'Accepted edition/source changed: {name}')
check(all(item['exit_code'] == 0 for item in load('production-checks.json').values()),
      'A production check failed')
check(load('epubcheck-official.json')['sha256'] ==
      sha_file(ROOT / 'Master-Speaking-Standard.epub'),
      'EPUBCheck report is stale')
check(load('epubcheck-official.json')['valid'], 'Official EPUBCheck failed')

# Verify that every supplied illustration in the protected source is accounted
# for in the exclusion/replacement record, and that its original bytes are not
# copied into the Word or EPUB publication packages.
artwork = load('artwork-provenance.json')
source_hashes = {entry['source_sha256'] for entry in artwork}
check(len(artwork) == 24 and len(source_hashes) == 24,
      'Artwork provenance must cover 24 distinct source illustrations')
check(all(entry.get('source_permission_status', '').startswith('Unverified;')
          for entry in artwork),
      'Source-art permissions were incorrectly recorded as cleared')
check(all('Original geometric illustration' in entry.get('replacement_origin', '')
          for entry in artwork),
      'Replacement-artwork provenance is incomplete')
check(all(entry['source_sha256'] != entry['replacement_sha256'] for entry in artwork),
      'A replacement artwork hash matches its supplied source image')
unmapped_media = load('unmapped-source-media.json')
unmapped_hashes = {entry['source_sha256'] for entry in unmapped_media}
check(all(entry.get('exported') is False for entry in unmapped_media),
      'Additional source-package media was not explicitly excluded')
with zipfile.ZipFile(ROOT / manifest['source']) as original:
    source_package_hashes = {
        sha_bytes(original.read(name))
        for name in original.namelist()
        if name.startswith('word/media/')
    }
check(source_package_hashes == source_hashes | unmapped_hashes,
      'Source-media hashes do not match the artwork and additional-media exclusion records')
for name in ['Master-Speaking-Standard-7x10.docx', 'Master-Speaking-Standard.epub']:
    copied = source_hashes & image_hashes(ROOT / name)
    check(not copied, f'Supplied source-art bytes found in {name}: {len(copied)} image(s)')

audit = load('source-audit-summary.json')
check(audit['unexplained_differences'] == 0, 'Unexplained source differences')
check(audit.get('source_illustrations_excluded') == 24 and
      audit.get('original_replacement_illustrations') == 24,
      'Source-art exclusion/replacement audit is incomplete')
check(all(item.get('disposition') for item in load('source-ledger.json')),
      'Source ledger has unexplained entries')

# The attributed epigraph was removed rather than implicitly cleared.
book = load('book.json')
removed_epigraph = [item for item in load('copyedits.json')
                    if item.get('source_block') == 121 and item.get('action') == 'remove']
check(len(removed_epigraph) == 1, 'Epigraph removal disposition is missing')
check(not book.get('front', {}).get('epigraph'), 'Epigraph remains in the semantic book')
check('Roy T. Bennett' not in master_text and
      'Listen with curiosity. Speak with honesty.' not in master_text,
      'Attributed epigraph remains in the semantic master')

plan = json.loads((ROOT / 'book/master/chapter-titles.json').read_text())
check(len(book.get('research_references', [])) == 8,
      'Selected research-reference appendix is missing or incomplete')
check('data-part="references"' in master_text,
      'References appendix missing from semantic master')
check([unit['number'] for unit in book['units']] == list(range(1, 9)),
      'Unit order changed')
check(sum(len(unit['chapters']) for unit in book['units']) == 32,
      'Chapter count mismatch')
for unit, planned in zip(book['units'], plan):
    check([chapter['title'] for chapter in unit['chapters']] == planned['titles'],
          f"Source-backed chapter titles changed in Unit {unit['number']}")

with zipfile.ZipFile(ROOT / 'Master-Speaking-Standard.epub') as epub:
    opf = etree.fromstring(epub.read('content.opf'))
    namespaces = {
        'o': 'http://www.idpf.org/2007/opf',
        'd': 'http://purl.org/dc/elements/1.1/',
    }
    summary = opf.xpath(
        'string(//o:meta[@property="schema:accessibilitySummary"])',
        namespaces=namespaces,
    )
    check('original external course videos' in summary and
          'fictional scripts' not in summary,
          'EPUB has the wrong edition accessibility summary')
    identifier = opf.xpath('string(//d:identifier)', namespaces=namespaces)
    expected_identifier = 'urn:uuid:' + str(uuid.uuid5(
        uuid.NAMESPACE_URL,
        'Master Speaking / Abdul Raziq Nazari / 2026 / Original-manuscript course edition',
    ))
    check(identifier == expected_identifier, 'EPUB edition identifier mismatch')
    epub_text = []
    epub_alt = []
    for name in epub.namelist():
        if name.endswith('.xhtml'):
            document = etree.fromstring(epub.read(name))
            epub_text.append(' '.join(document.itertext()))
            epub_alt.extend((node.get('alt') or '').strip()
                            for node in document.xpath('.//*[local-name()="img"]'))
    epub_text = '\\n'.join(epub_text)
    check('Roy T. Bennett' not in epub_text and
          'Listen with curiosity. Speak with honesty.' not in epub_text,
          'Attributed epigraph remains in the EPUB')
    check(len(epub_alt) == 25 and all(epub_alt),
          'EPUB image alternatives are missing or incomplete')

with zipfile.ZipFile(ROOT / 'Master-Speaking-Standard-7x10.docx') as word:
    document = etree.fromstring(word.read('word/document.xml'))
    word_text = ' '.join(document.itertext())
    descriptions = [value.strip() for value in
                    document.xpath('.//*[local-name()="docPr"]/@descr')]
    check('Roy T. Bennett' not in word_text and
          'Listen with curiosity. Speak with honesty.' not in word_text,
          'Attributed epigraph remains in the Word output')
    check(len(descriptions) == 24 and all(descriptions),
          'Word image descriptions are missing or incomplete')

result = {
    'status': 'PASS' if not issues else 'FAIL',
    'issues': issues,
    'outputs_checked': len(manifest['outputs']),
    'edition': 'Original-manuscript Standard review proof; not approved for publication',
    'scope': (
        'Freshness, identity, protected-input, source-art exclusion, and epigraph-removal checks; '
        'not editorial, legal, accessibility, or printer clearance'
    ),
}
(STANDARD / 'qa_standard.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
raise SystemExit(bool(issues))

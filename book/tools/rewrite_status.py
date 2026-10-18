#!/usr/bin/env python3
"""Refresh the current revision summary without claiming independent proof."""
from pathlib import Path
import hashlib
import json
import pymupdf

ROOT = Path(__file__).resolve().parents[2]


def write_status():
    load = lambda name: json.loads((ROOT / name).read_text())
    checks = load('book/artifacts/qa_october_run.json')
    coverage = load('book/artifacts/qa_whole_revision.json')
    keys = load('book/artifacts/qa_reading_keys.json')
    proof = load('book/qa/full-revision-proof/index.json')
    files = sorted(ROOT.glob('Master-Speaking*.pdf')) + sorted(ROOT.glob('Master-Speaking*.docx')) + [ROOT / 'Master-Speaking.epub', ROOT / 'Master Speaking.docx']
    with pymupdf.open(ROOT / 'Master-Speaking-print-7x10.pdf') as pdf:
        interior_pages = len(pdf)
        chapters = [{'label': t, 'physical_page': p} for _, t, p in pdf.get_toc() if t.startswith('Chapter ')]
    current_hash = hashlib.sha256((ROOT / 'Master-Speaking-print-7x10.pdf').read_bytes()).hexdigest()
    progress = {
        'date': '2026-10-18',
        'scope': 'All-chapter substantive editorial revision and synchronized editions; separate limited field-level and readable-page proof records.',
        'chapter_revision_pass_complete': coverage['ok'] and coverage['chapters_with_recorded_revisions'] == 32,
        'chapters_with_recorded_revisions': coverage['chapters_with_recorded_revisions'],
        'chapters_without_recorded_revisions': 32-coverage['chapters_with_recorded_revisions'],
        'independent_every_word_proof_complete': False,
        'commercial_release_cleared': False,
        'interior_pages': interior_pages, 'reader_pages': interior_pages+1,
        'guarded_chapter_edits': len(load('book/master/reviewed-edits.json')),
        'guarded_front_edits': len(load('book/master/reviewed-front-edits.json')),
        'initial_detailed_field_record': {'fields': 138, 'scope': 'Foreword and Unit 1 Chapter 1 only; not every retained word across all chapters.'},
        'release_checks': {name: result['exit_code'] for name, result in checks.items()},
        'reading_closed_key_check': keys,
        'self_contained_edition': load('book/artifacts/qa_self_contained.json'),
        'vocabulary_completion_keys': load('book/artifacts/qa_vocabulary_keys.json'),
        'recorded_audio_supplied': False,
        'publication_files_built': all(row['exit_code'] == 0 for row in checks.values()),
        'chapter_starts': chapters,
        'unit_physical_pages': load('book/artifacts/qa_print.json')['unit_pages'],
        'sha256': {file.name: hashlib.sha256(file.read_bytes()).hexdigest() for file in files},
        'semantic_content_sha256': hashlib.sha256((ROOT / 'book/artifacts/book.json').read_bytes()).hexdigest(),
        'visual_proof': {'all_interior_page_overviews_inspected': proof['sha256'] == current_hash,
                         'support_page_overviews_inspected': all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest for name, digest in proof['support_sha256'].items()),
                         'selected_main_readable_pages': proof['selected_main_pages'] if proof['sha256'] == current_hash else [],
                         'selected_teacher_readable_pages': proof['selected_teacher_pages'] if hashlib.sha256((ROOT / 'Master-Speaking-Teacher-Implementation-Pack.pdf').read_bytes()).hexdigest() == proof['support_sha256']['Master-Speaking-Teacher-Implementation-Pack.pdf'] else [],
                         'every_page_read_at_full_size': False},
        'remaining_external_work': ['Independent complete copyedit and factual/pronunciation/key review',
            'Publisher approval of edition metadata, imprint and any ISBN; review authored-content provenance',
            'EPUB-device/accessibility testing and appropriate PDF accessibility remediation',
            'Native Word comparison if using Word rather than the supplied PDF for final pagination',
            'Actual classroom pilot evidence; printer-specific cover wrap, spine/bleed and physical proof']
    }
    (ROOT / 'book/artifacts/rewrite-progress.json').write_text(json.dumps(progress, indent=2)+'\n')
    return progress


if __name__ == '__main__':
    p = write_status()
    print(f"Revision summary: {p['chapters_with_recorded_revisions']} chapters; {len(p['release_checks'])} gates; {p['interior_pages']} interior pages")

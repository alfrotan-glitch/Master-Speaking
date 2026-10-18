#!/usr/bin/env python3
"""Render proof candidates. Rendering is not a claim of human inspection."""
from pathlib import Path
import hashlib
import json

import pymupdf
from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'book/standard/qa'
OUT.mkdir(parents=True, exist_ok=True)

# Remove previous candidates so a shortened, regenerated PDF cannot leave
# stale pages behind. The old artwork sheet contained uncleared source art.
for old in [*OUT.glob('overview-*.jpg'), *OUT.glob('page-*.png')]:
    old.unlink()
legacy_source_art = OUT / 'original-artwork-reviewed.jpg'
if legacy_source_art.exists():
    legacy_source_art.unlink()

pdf_path = ROOT / 'Master-Speaking-Standard-print-7x10.pdf'
doc = pymupdf.open(pdf_path)
for start in range(0, len(doc), 30):
    end = min(start + 30, len(doc))
    sheet = Image.new('RGB', (1100, 1860), '#e8ecea')
    draw = ImageDraw.Draw(sheet)
    for index in range(start, end):
        page = doc[index]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(.4, .4), alpha=False)
        image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        x = ((index - start) % 5) * 220 + 8
        y = ((index - start) // 5) * 310 + 19
        sheet.paste(image, (x, y))
        draw.text((x, y - 15), f'Physical page {index + 1}', fill='#172b2e')
    sheet.save(OUT / f'overview-{start + 1:03d}-{end:03d}.jpg', quality=88)

# Retain prior proof checkpoints where the page still exists, then add every
# image-bearing page plus semantically important front/back matter. This keeps
# the candidate set useful when an editorial change shifts page numbers.
selected = {
    n for n in [2, 3, 8, 9, 10, 14, 15, 25, 26, 30, 31, 32, 44, 48, 49,
                51, 62, 66, 68, 70, 82, 88, 98, 99, 102, 108, 116, 118,
                122, 127, 128, 142, 149, 154, 157, 158]
    if n <= len(doc)
}
selected.update({1, len(doc)})
needles = [
    'Review proof; not approved for publication',
    'Try unfamiliar activities at your own pace',
    'connected speech',
    'schwa',
    'Selected Research References',
]
for number, page in enumerate(doc, 1):
    text = page.get_text().casefold()
    if page.get_images(full=True) or any(word.casefold() in text for word in needles):
        selected.add(number)
selected = sorted(selected)
for number in selected:
    doc[number - 1].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(
        OUT / f'page-{number:03d}.png'
    )

for name in ['Front', 'Back']:
    with pymupdf.open(ROOT / f'Master-Speaking-Standard-{name}-Cover.pdf') as cover:
        if len(cover):
            cover[0].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(
                OUT / f'{name.lower()}-cover.png'
            )

# Make an inspection candidate from the newly generated replacements only.
# This intentionally reads the staged outputs, never the original DOCX media.
artwork_dir = ROOT / 'book/standard/work/book/assets/images'
provenance = json.loads((ROOT / 'book/standard/artwork-provenance.json').read_text())
artwork = Image.new('RGB', (1600, 6 * 300), '#e8ecea')
art_draw = ImageDraw.Draw(artwork)
for index, entry in enumerate(provenance):
    path = artwork_dir / entry['replacement_file']
    if not path.is_file():
        raise FileNotFoundError(f'Missing generated replacement artwork: {path}')
    with Image.open(path) as source:
        if getattr(source, 'is_animated', False):
            source.seek(0)
        image = ImageOps.contain(source.convert('RGB'), (380, 245))
    column = index % 4
    row = index // 4
    x = column * 400 + (400 - image.width) // 2
    y = row * 300 + 34 + (245 - image.height) // 2
    artwork.paste(image, (x, y))
    art_draw.text((column * 400 + 8, row * 300 + 8), entry['replacement_file'], fill='#172b2e')
art_path = OUT / 'replacement-artwork-candidates.jpg'
artwork.save(art_path, quality=92)

sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
(OUT / 'candidates.json').write_text(json.dumps({
    'pdf_sha256': sha(pdf_path),
    'overview_candidates': list(range(1, len(doc) + 1)),
    'full_size_candidates': selected,
    'replacement_artwork_candidate': art_path.name,
    'replacement_artwork_candidate_sha256': sha(art_path),
    'replacement_artwork_count': len(provenance),
    'note': 'Candidate generation only. Actual inspection is recorded separately.'
}, indent=2) + '\n')
print(f'{len(doc)} overview pages; {len(selected)} full-size page candidates; '
      f'{len(provenance)} replacement-artwork candidates generated')

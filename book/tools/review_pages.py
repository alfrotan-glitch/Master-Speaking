#!/usr/bin/env python3
"""Render current-edition layout overviews and selected full-size proof pages.

These are review aids, not evidence that every word has been human-proofread.
Generated images are keyed to the PDF checksum in index.json.
"""
import hashlib
import json
from pathlib import Path
import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / 'Master-Speaking-print-7x10.pdf'
OUT = ROOT / 'book/qa/edition-review'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for pattern in ['overview-*.jpg', 'page-*.png']:
        for path in OUT.glob(pattern):
            path.unlink()
    with pymupdf.open(PDF) as doc:
        for start in range(0, len(doc), 20):
            sheet = Image.new('RGB', (1000, 1240), '#dde2e0')
            draw = ImageDraw.Draw(sheet)
            for index in range(min(20, len(doc) - start)):
                pix = doc[start + index].get_pixmap(matrix=pymupdf.Matrix(.36, .36), alpha=False)
                thumb = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
                x, y = index % 5 * 200 + 9, index // 5 * 310 + 25
                sheet.paste(thumb, (x, y))
                draw.text((x, y - 18), str(start + index + 1), fill='black')
            sheet.save(OUT / f'overview-{start + 1:03d}.jpg', quality=85)
        unit_starts = [page for depth, title, page in doc.get_toc() if depth == 0 or title.startswith('Unit ')]
        selected = sorted(set([1, 4, 5, 7, len(doc)] + [page + 1 for page in unit_starts]))
        for page in selected:
            doc[page - 1].get_pixmap().save(OUT / f'page-{page:03d}.png')
        manifest = {'pdf': PDF.name, 'sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
                    'pages': len(doc), 'all_pages_rendered_as_thumbnails': True,
                    'full_size_pages': selected,
                    'limitation': 'Layout overview only; not a signed human line-by-line proof.'}
    (OUT / 'index.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Rendered {manifest["pages"]} page thumbnails and {len(selected)} selected full-size pages.')


if __name__ == '__main__':
    main()

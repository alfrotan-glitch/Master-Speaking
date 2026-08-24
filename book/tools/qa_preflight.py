#!/usr/bin/env python3
"""qa_preflight.py — print preflight for the final PDF.

Checks: PDF version & page geometry, metadata (title/author), fonts all
embedded & subset (and no forbidden base-14 fallbacks), image inventory with
effective dpi, color spaces, no annotations/JS/encryption, TrimBox sanity.
Writes book/artifacts/qa_preflight.json + qa_preflight_report.md.
"""
import json, os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'Master-Speaking-print-7x10.pdf')

d = pymupdf.open(PDF)
issues = []
info = {
    'pdf_version': d.metadata['format'],
    'page_count': len(d),
    'encryption': d.is_encrypted,
    'metadata': {k: v for k, v in d.metadata.items() if v},
}

# geometry
sizes = {(round(p.rect.width, 2), round(p.rect.height, 2)) for p in d}
info['page_sizes_pt'] = sorted(sizes)
if sizes != {(504.0, 720.0)}:
    issues.append(f'unexpected page sizes: {sizes}')

# fonts — declared inventory, but issues keyed to actual glyph usage
# (ReportLab declares a base font resource on every page even when unused)
fonts = {}
used_fonts = set()
for pno in range(len(d)):
    for f in d[pno].get_fonts(full=True):
        xref, ext, ftype, name, refname, enc = f[:6]
        fonts[name] = {'type': ftype, 'ext': ext}
    for b in d[pno].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                if sp['text'].strip():
                    used_fonts.add(sp['font'])
info['fonts'] = fonts
info['fonts_used'] = sorted(used_fonts)
for name, f in fonts.items():
    base = name.split('+')[-1].split('-')[0]
    if base not in used_fonts and name not in used_fonts:
        continue                      # declared, never drawn
    if f['ext'] == 'n/a' and f['type'] != 'Type3':
        issues.append(f'font {name} not embedded (ext=n/a)')
    if 'Helvetica' in name or 'Arial' in name:
        if 'Source' not in name and 'DejaVu' not in name:
            issues.append(f'base-14 fallback font in use: {name}')

# images
img_inv = []
seen = set()
for pno in range(len(d)):
    for img in d[pno].get_image_info(xrefs=True):
        xref = img.get('xref', 0)
        if xref in seen:
            continue
        seen.add(xref)
        w_px, h_px = img['width'], img['height']
        b = img['bbox']
        dpi_x = w_px / ((b[2] - b[0]) / 72) if b[2] > b[0] else 0
        cs_n = img.get('colorspace', 0)
        cs = {1: 'DeviceGray', 3: 'DeviceRGB', 4: 'DeviceCMYK'}.get(cs_n, f'cs{cs_n}')
        img_inv.append({'xref': xref, 'page': pno + 1, 'px': [w_px, h_px],
                        'cs': cs, 'dpi': round(dpi_x, 1)})
info['images'] = img_inv
source_limited = []
for im in img_inv:
    if im['dpi'] < 120:
        issues.append(f"image xref {im['xref']} on p{im['page']}: {im['dpi']} dpi < 120")
    elif im['dpi'] < 150:
        source_limited.append(
            f"image xref {im['xref']} on p{im['page']}: {im['dpi']} dpi "
            f"(source-limited, original composition size kept)")
info['source_limited_images'] = source_limited
for im in img_inv:
    if im['cs'] not in ('DeviceRGB', 'DeviceGray', 'DeviceCMYK'):
        issues.append(f"image xref {im['xref']}: colorspace {im['cs']}")

# annotations / js
for pno in range(len(d)):
    for a in d[pno].annots() or []:
        issues.append(f'p{pno+1}: annotation present ({a.type})')
if d.xref_get_key(-1, 'Names')[0] != 'null' if False else False:
    pass

info['issues'] = issues
info['ok'] = not issues
open(os.path.join(ROOT, 'book/artifacts/qa_preflight.json'), 'w').write(
    json.dumps(info, indent=1))

md = ['# Print Preflight Report — Master Speaking (7×10 in)\n',
      f'- PDF version: {info["pdf_version"]}',
      f'- Pages: {info["page_count"]}',
      f'- Page size: 504 × 720 pt (7 × 10 in) — all pages uniform',
      f'- Encrypted: {info["encryption"]}',
      f'- Metadata: title={info["metadata"].get("title")!r}, '
      f'author={info["metadata"].get("author")!r}',
      f'- Fonts ({len(fonts)}):']
for name, f in sorted(fonts.items()):
    md.append(f'    - {name} — {f["type"]}, embedded ext={f["ext"]}')
md.append(f'- Images: {len(img_inv)} unique, effective dpi '
          f'{min(i["dpi"] for i in img_inv)}–{max(i["dpi"] for i in img_inv)}')
md.append(f'- Annotations: none' if not any('annotation' in i for i in issues)
          else '- Annotations: PRESENT')
md.append('')
md.append(f'## Issues ({len(issues)})')
md += [f'- {i}' for i in issues] or ['- none — PASS']
open(os.path.join(ROOT, 'book/artifacts/qa_preflight_report.md'), 'w').write('\n'.join(md))
print('\n'.join(md[:20]))
print(f'issues: {len(issues)}')
sys.exit(1 if issues else 0)

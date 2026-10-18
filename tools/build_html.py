# -*- coding: utf-8 -*-
"""Rebuild the browser-friendly HTML edition from the editable DOCX.
Run: python tools/build_html.py   (requires build_spec/requirements.txt)
"""
import os
import re
import mammoth
from lxml import etree, html as lxml_html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'Grammar for Special Speaking (TOEFL House).docx')
OUT = os.path.join(ROOT, 'dist', 'Grammar for Special Speaking (TOEFL House).html')

with open(SRC, 'rb') as f:
    result = mammoth.convert_to_html(f)

# Mammoth preserves Word Heading 1/2 structure. Give the book-level destinations
# stable anchors and build a real browser navigation list, since Word field results
# are not calculated by an HTML conversion.
root = lxml_html.fragment_fromstring(result.value, create_parent='div')
nav_entries = []
seen = set()
pattern = re.compile(r'^(LESSON\s+\d+\b.*|REVIEW TEST\s+\d+|FINAL ASSESSMENT(?:\s+—\s+PART\s+2)?|APPENDIX\s+\d+\b.*|INTRODUCTION|HOW TO USE THIS BOOK|CONTENTS|DIAGNOSTIC TEST)$', re.I)
for heading in root.xpath('.//h1|.//h2'):
    text = ' '.join(' '.join(heading.itertext()).split())
    if not pattern.match(text):
        continue
    key = text.casefold()
    if key in seen:
        continue
    seen.add(key)
    slug = 'nav-' + re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    heading.set('id', slug)
    nav_entries.append((text, slug))

# Remove the non-Word placeholder for the contents field; HTML has its own navigation.
for p in root.xpath('.//p'):
    if 'Update this field to populate the contents and page numbers.' in ' '.join(p.itertext()):
        p.getparent().remove(p)

nav = etree.Element('nav', **{'aria-label': 'Book contents'})
nav_title = etree.SubElement(nav, 'h2')
nav_title.text = 'Contents'
listing = etree.SubElement(nav, 'ol')
for title, slug in nav_entries:
    li = etree.SubElement(listing, 'li')
    link = etree.SubElement(li, 'a', href='#' + slug)
    link.text = title
root.insert(0, nav)
html = lxml_html.tostring(root, encoding='unicode', method='html')

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Grammar for Special Speaking — TOEFL HOUSE</title>
<style>
 body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 46em; margin: 2em auto;
        line-height: 1.5; color: #1a1a1a; padding: 0 1em; }}
 h1,h2,h3 {{ font-family: 'Segoe UI', Arial, sans-serif; color: #1F3A5F; }}
 nav {{ border: 1px solid #d9dde3; padding: 0.7em 1.1em; margin-bottom: 2em; }}
 nav ol {{ columns: 2; column-gap: 2em; padding-left: 1.6em; }}
 nav li {{ break-inside: avoid; margin: 0.15em 0; }}
 a {{ color: #0E6B6B; }}
 table {{ border-collapse: collapse; width: 100%; margin: 0.8em 0; }}
 th {{ background: #1F3A5F; color: #fff; padding: 0.4em 0.6em; text-align: left; }}
 td {{ border: 1px solid #ccc; padding: 0.4em 0.6em; vertical-align: top; }}
 tr:nth-child(even) td {{ background: #f7f8fa; }}
 @media print {{ body {{ margin: 0; max-width: none; }} nav {{ break-after: page; }} }}
</style></head><body>
<p style="text-align:center;color:#0E6B6B;font-family:sans-serif">TOEFL HOUSE</p>
{html}
</body></html>"""
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(page)
print("wrote", OUT, f"({len(html)} chars, {len(result.messages)} conversion messages, {len(nav_entries)} navigation entries)")

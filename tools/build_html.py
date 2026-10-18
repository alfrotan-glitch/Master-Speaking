# -*- coding: utf-8 -*-
"""Rebuild the browser-friendly HTML editions from the editable DOCX files.
Run: python tools/build_html.py   (requires build_spec/requirements.txt)
Builds both Student Book and Teacher's Book if present.
"""
import os
import re
import mammoth
from lxml import etree, html as lxml_html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TITLES = [
    "Grammar for Special Speaking (TOEFL House)",
    "Grammar for Special Speaking — Teacher's Book (TOEFL House)",
]

# Pattern for book-level destinations
PATTERN = re.compile(r'^(LESSON\s+\d+\b.*|REVIEW TEST\s+\d+|FINAL ASSESSMENT(?:\s+—\s+PART\s+2)?|APPENDIX\s+\d+\b.*|INTRODUCTION|HOW TO USE THIS BOOK|CONTENTS|DIAGNOSTIC TEST|COURSE OVERVIEW|TEACHING PRINCIPLES|PACING AND FEEDBACK|ASSESSMENT GUIDANCE|COPYRIGHT)', re.I)


def build_html_for(src_name: str):
    SRC = os.path.join(ROOT, f'{src_name}.docx')
    OUT = os.path.join(ROOT, 'dist', f'{src_name}.html')
    if not os.path.exists(SRC):
        print(f"skip: {src_name}.docx not found")
        return None
    with open(SRC, 'rb') as f:
        result = mammoth.convert_to_html(f)

    root = lxml_html.fragment_fromstring(result.value, create_parent='div')
    nav_entries = []
    seen = set()
    for heading in root.xpath('.//h1|.//h2'):
        text = ' '.join(' '.join(heading.itertext()).split())
        if not PATTERN.match(text):
            continue
        key = text.casefold()
        if key in seen:
            continue
        seen.add(key)
        slug = 'nav-' + re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
        heading.set('id', slug)
        nav_entries.append((text, slug))

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
    html_fragment = lxml_html.tostring(root, encoding='unicode', method='html')

    is_teacher = "Teacher" in src_name
    page_title = src_name + " — TOEFL HOUSE"
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{page_title}</title>
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
{html_fragment}
</body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"wrote {os.path.basename(OUT)} ({len(html_fragment)} chars, {len(result.messages)} conversion messages, {len(nav_entries)} navigation entries)")
    return OUT


if __name__ == "__main__":
    for title in TITLES:
        build_html_for(title)

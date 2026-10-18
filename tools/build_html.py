# -*- coding: utf-8 -*-
"""Rebuild the HTML distribution edition from the docx master.
Run: python tools/build_html.py   (requires: pip install mammoth)"""
import os, mammoth

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'Grammar for Special Speaking (TOEFL House).docx')
OUT = os.path.join(ROOT, 'dist', 'Grammar for Special Speaking (TOEFL House).html')

with open(SRC, 'rb') as f:
    result = mammoth.convert_to_html(f)
html = result.value
page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Grammar for Special Speaking — TOEFL HOUSE</title>
<style>
 body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 46em; margin: 2em auto;
        line-height: 1.5; color: #1a1a1a; padding: 0 1em; }}
 h1,h2,h3 {{ font-family: 'Segoe UI', Arial, sans-serif; color: #1F3A5F; }}
 table {{ border-collapse: collapse; width: 100%; margin: 0.8em 0; }}
 th {{ background: #1F3A5F; color: #fff; padding: 0.4em 0.6em; text-align: left; }}
 td {{ border: 1px solid #ccc; padding: 0.4em 0.6em; vertical-align: top; }}
 tr:nth-child(even) td {{ background: #f7f8fa; }}
 @media print {{ body {{ margin: 0; max-width: none; }} }}
</style></head><body>
<p style="text-align:center;color:#0E6B6B;font-family:sans-serif">TOEFL HOUSE</p>
{html}
</body></html>"""
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    f.write(page)
print("wrote", OUT, f"({len(html)} chars, {len(result.messages)} conversion messages)")

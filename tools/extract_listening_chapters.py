#!/usr/bin/env python3
"""Extract the eight listening chapters into a targeted factual alignment report."""
import re
from pathlib import Path
from docx import Document
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"docs"/"listening-lesson-review.md"

def main():
    paras=[p.text.strip() for p in Document(ROOT/"Master Speaking.docx").paragraphs if p.text.strip()]
    blocks=[]
    current=None
    for paragraph in paras:
        s=re.sub(r"\s+"," ",paragraph)
        if re.match(r"(?i)^chapter\s*2\b",s):
            if current is not None: blocks.append(current)
            current=[s]
        elif current is not None and re.match(r"(?i)^chapter\s*[34]\b",s):
            blocks.append(current)
            current=None
        elif current is not None:
            current.append(s)
    if current is not None: blocks.append(current)
    if not 8<=len(blocks)<=12:
        raise AssertionError(f"Expected 8 listening chapters, found {len(blocks)}")
    lines=["# Listening chapters — content/resource alignment worklist","",
           "Source material from the original Master Speaking manuscript. No audio/video rights or links are inferred.",""]
    for i,block in enumerate(blocks,1):
        lines.extend([f"## Listening lesson {i}",""])
        lines.extend(f"{j+1}. {item}" for j,item in enumerate(block[:110]))
        lines.append("")
    OUT.write_text("\n".join(lines),encoding="utf-8")
    print(f"LISTENING AUDIT: {len(blocks)} sections extracted.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

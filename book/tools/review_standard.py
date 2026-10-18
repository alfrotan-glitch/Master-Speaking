#!/usr/bin/env python3
"""Render proof candidates. Rendering is not a claim of human inspection."""
from pathlib import Path
import hashlib,json
import pymupdf
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'book/standard/qa';OUT.mkdir(parents=True,exist_ok=True)
for old in [*OUT.glob('overview-*.jpg'),*OUT.glob('page-*.png')]:old.unlink()
file=ROOT/'Master-Speaking-Standard-print-7x10.pdf'
doc=pymupdf.open(file)
for start in range(0,len(doc),30):
    sheet=Image.new('RGB',(1100,1860),'#e8ecea');draw=ImageDraw.Draw(sheet)
    for index in range(start,min(start+30,len(doc))):
        page=doc[index];pix=page.get_pixmap(matrix=pymupdf.Matrix(.4,.4),alpha=False)
        image=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        x=((index-start)%5)*220+8;y=((index-start)//5)*310+19
        sheet.paste(image,(x,y));draw.text((x,y-15),f'Physical page {index+1}',fill='#172b2e')
    sheet.save(OUT/f'overview-{start+1:03d}-{min(start+30,len(doc)):03d}.jpg',quality=88)
selected=[9,10,15,25,26,32,44,51,62,68,82,88,102,108,116,122,127,128,142,149,154,157,158]
for number in selected:
    doc[number-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5),alpha=False).save(OUT/f'page-{number:03d}.png')
for name in ['Front','Back']:
    with pymupdf.open(ROOT/f'Master-Speaking-Standard-{name}-Cover.pdf') as cover:
        cover[0].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5),alpha=False).save(OUT/f'{name.lower()}-cover.png')
(OUT/'candidates.json').write_text(json.dumps({'pdf_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
    'overview_candidates':list(range(1,len(doc)+1)),'full_size_candidates':selected,
    'note':'Candidate generation only. Actual inspection is recorded separately.'},indent=2)+'\n')
print(len(doc),'overview pages;',len(selected),'full-size candidates generated')

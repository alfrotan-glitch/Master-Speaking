#!/usr/bin/env python3
"""Render review aids; generation alone does not record visual inspection."""
from pathlib import Path
import json,re,hashlib
import pymupdf
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parents[2];p=r/'book/qa/improvement-review';p.mkdir(exist_ok=True)
for variant in ['opener','reading','listening']:
 for start in [1,5]:
  im=Image.new('RGB',(1400,1650),'#dde2e0')
  for i,n in enumerate(range(start,start+4)):
   a=Image.open(r/f'book/assets/images/edition-unit-{n}-{variant}.png');a.thumbnail((1360,390));im.paste(a,(20,i*410+10))
  im.save(p/f'graphics-{variant}-{start}.jpg',quality=90)
with pymupdf.open(r/'Master-Speaking-print-7x10.pdf') as d:
 scripts=json.loads((r/'book/artifacts/qa_self_contained.json').read_text())['single_page_script_locations']
 tasks=[i+1 for i,page in enumerate(d) if 'Listen More Closely' in page.get_text()]
 openers=[int(i) for i in json.loads((r/'book/artifacts/qa_print.json').read_text())['unit_pages'].values()]
 selected=sorted(set([9,11,36,37]+scripts+tasks+openers))
 for n in selected:d[n-1].get_pixmap().save(p/f'main-{n:03}.png')
 print('main',len(d),'selected',selected)
for short,name in [('student','Master-Speaking-Student-Practice-Pack.pdf'),('teacher','Master-Speaking-Teacher-Implementation-Pack.pdf'),('companion','Master-Speaking-Class-Companion.pdf')]:
 with pymupdf.open(r/name) as d:
  for start in range(0,len(d),20):
   sheet=Image.new('RGB',(1000,1240),'#dde2e0');dr=ImageDraw.Draw(sheet)
   for i in range(min(20,len(d)-start)):
    pix=d[start+i].get_pixmap(matrix=pymupdf.Matrix(.3,.3),alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((180,270));x,y=i%5*200+10,i//5*310+24;sheet.paste(im,(x,y));dr.text((x,y-18),str(start+i+1),fill='black')
   sheet.save(p/f'{short}-overview-{start+1:03}.jpg',quality=88)
  if short=='teacher':
   for n in [10,11,20,21,38,41]:d[n-1].get_pixmap().save(p/f'teacher-{n:03}.png')
(r/'book/qa/improvement-review/selection.json').write_text(json.dumps({'candidate_main_pages':selected,'candidate_teacher_pages':[10,11,20,21,38,41],'script_pages':scripts,'interpretation_pages':tasks},indent=2)+'\n')

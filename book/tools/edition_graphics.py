#!/usr/bin/env python3
"""Draw original course diagrams; no stock images, logos or external artwork."""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw, ImageFont
from design import BANNER, ACCENT, INK, MUTED, RULE, PAPER, COPPER
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / 'book/assets/images'
FONT = ROOT / 'book/assets/fonts'
W, H = 2100, 1200


def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('source-sans-3-latin-600-normal.ttf' if bold else 'source-sans-3-latin-400-normal.ttf')), size)


def lines(text, face, width, draw):
    out=[]; line=''
    for word in text.split():
        candidate=(line+' '+word).strip()
        if line and draw.textlength(candidate, font=face)>width:
            out.append(line); line=word
        else: line=candidate
    return out+[line]


def label(draw, xy, text, size=48, color=INK, width=1750, bold=False):
    face=font(size,bold); x,y=xy
    for line in lines(text,face,width,draw):
        draw.text((x,y),line,font=face,fill='#'+color); y+=int(size*1.25)
    return y


def card(draw, box, number, title, body):
    x,y,x2,y2=box
    draw.rounded_rectangle(box, radius=24, fill='white', outline='#'+RULE, width=3)
    draw.ellipse((x+40,y+40,x+120,y+120),fill='#'+BANNER)
    draw.text((x+65,y+47),str(number),font=font(48,True),fill='white')
    yy=label(draw,(x+40,y+155),title,58,width=x2-x-80,bold=True)
    bottom=label(draw,(x+40,yy+20),body,58,color=MUTED,width=x2-x-80)
    if bottom>y2-8:raise ValueError(f'Graphic card overflows: {title}: {body}')


def main():
    plan=json.loads((ROOT/'book/master/self-contained-edition.json').read_text())
    record={'date':'2026-10-18','review_basis':'Original code-drawn teaching diagrams; labels and alternative text share the reviewed edition plan. No external artwork, stock imagery, screenshots or video logos. Font sources/licenses are recorded separately.','images':[]}
    provenance=[]
    for u in plan['units']:
        for variant in ['opener','reading','listening']:
            data=u['graphics'][variant]
            filename=f'edition-unit-{u["unit"]}-{variant}.png'
            image=Image.new('RGB',(W,H),'#'+PAPER);d=ImageDraw.Draw(image)
            d.rectangle((0,0,W,20),fill='#'+BANNER)
            label(d,(110,85),f'UNIT {u["unit"]}  /  '+data['kicker'],54,color=ACCENT,bold=True)
            label(d,(110,165),data['title'],90,width=1850,bold=True)
            label(d,(110,305),data['subtitle'],58,color=MUTED,width=1850)
            for i,(title,body) in enumerate(data['cards']):
                x=110+i*640
                card(d,(x,470,x+600,1090),i+1,title,body)
            d.line((110,1120,1990,1120),fill='#'+RULE,width=3)

            path=ASSETS/filename;image.save(path,optimize=True)
            alt=data['title']+'. '+data['subtitle']+' '+ ' '.join(f'{i+1}. {t}: {b}' for i,(t,b) in enumerate(data['cards']))
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            record['images'].append({'file':filename,'path':str(path.relative_to(ROOT)),'sha256':digest,'alt':alt})
            provenance.append({'asset':str(path.relative_to(ROOT)),'sha256':digest,'origin':'Original geometric teaching diagram drawn by book/tools/edition_graphics.py from self-contained-edition.json','third_party_artwork':False,'font_license':'SIL Open Font License; see book/assets/fonts/provenance.json','permission_status':'No external artwork used; AI-assisted authored design, not a legal certification'})
    path=ROOT/'book/assets/cover.png'
    old=json.loads((ROOT/'book/master/image-descriptions.json').read_text())
    cover=next(x for x in old['images'] if x['file']=='cover.png')
    cover['sha256']=hashlib.sha256(path.read_bytes()).hexdigest();record['images'].append(cover)
    (ROOT/'book/master/image-descriptions.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'book/publishing/current-artwork-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print('Original course diagrams drawn:',len(provenance))


if __name__=='__main__':main()

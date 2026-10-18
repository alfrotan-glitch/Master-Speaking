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


def scene(draw, unit, variant):
    """Eight conceptual diagrams, not quantitative charts or stock illustrations."""
    import math
    teal='#'+BANNER; pale='#E1ECE9'; copper='#'+COPPER; rule='#'+RULE
    centers=[(410,580),(1050,580),(1690,580)]
    width=9 if variant!='listening' else 6
    def link(a,b,color=teal):
        if variant=='listening':
            for k in range(0,20,2):
                p=tuple(int(a[j]+(b[j]-a[j])*k/20) for j in range(2));q=tuple(int(a[j]+(b[j]-a[j])*(k+1)/20) for j in range(2));draw.line((p,q),fill=color,width=width)
        else:draw.line((a,b),fill=color,width=width)
    if unit==1:
        for i,(x,y) in enumerate(centers):
            draw.rounded_rectangle((x-200,y-115,x+200,y+95),radius=65,fill=pale if i!=1 else '#'+PAPER,outline=teal,width=7)
            draw.polygon([(x-125,y+80),(x-150,y+150),(x-40,y+90)],fill=teal)
            for j,length in enumerate([220,280,150]):draw.line((x-140,y-45+j*45,x-140+length,y-45+j*45),fill=copper if i==2 else teal,width=10)
        link((615,570),(845,570));link((1255,570),(1485,570))
        desc='Three speech shapes exchange a message, then return a clarification.'
    elif unit==2:
        draw.polygon([(120,730),(680,390),(1010,650),(1510,370),(1980,730)],fill=pale)
        points=[(230,695),(570,695),(750,570),(1130,570),(1350,440),(1810,440)]
        draw.line(points,fill=teal,width=12,joint='curve')
        for i,(x,y) in enumerate([(410,695),(1050,570),(1690,440)]):
            draw.ellipse((x-42,y-42,x+42,y+42),fill=copper,outline='white',width=6)
        draw.line((1810,440,1810,330),fill=teal,width=8);draw.polygon([(1810,330),(1930,360),(1810,395)],fill=copper)
        desc='A rising path has three stopping points and a flag: progress involves intermediate steps.'
    elif unit==3:
        draw.ellipse((235,485,585,675),fill=pale,outline=teal,width=9)
        draw.ellipse((355,525,465,635),fill=copper)
        draw.ellipse((390,560,430,600),fill=teal)
        draw.ellipse((910,440,1190,720),fill=pale,outline=teal,width=8)
        draw.text((1000,445),'?',font=font(205,True),fill=teal)
        draw.line([(1530,580),(1640,580),(1780,450),(1870,450)],fill=teal,width=11,joint='curve')
        draw.line([(1640,580),(1780,710),(1870,710)],fill=copper,width=11,joint='curve')
        draw.polygon([(1870,425),(1910,450),(1870,475)],fill=teal)
        draw.polygon([(1870,685),(1910,710),(1870,735)],fill=copper)
        link((610,580),(885,580));link((1210,580),(1500,580))
        desc='An eye, an open question and branching paths distinguish observation, interpretation and a choice of response; they do not rank people.'
    elif unit==4:
        draw.line((1050,400,1050,700),fill=teal,width=14);draw.polygon([(940,735),(1160,735),(1050,610)],fill=teal)
        draw.line((360,465,1740,465),fill=teal,width=12)
        for x in [410,1690]:
            draw.line((x,465,x-125,650),fill=teal,width=7);draw.line((x,465,x+125,650),fill=teal,width=7)
            draw.arc((x-145,540,x+145,750),0,180,fill=teal,width=14)
        for i in range(3):draw.rounded_rectangle((315+i*35,605-i*30,430+i*35,635-i*30),radius=12,fill=copper)
        draw.ellipse((1635,560,1690,615),fill=copper);draw.ellipse((1700,560,1755,615),fill=copper);draw.polygon([(1635,585),(1755,585),(1695,650)],fill=copper)
        desc='A balance holds coins on one side and a heart on the other, inviting comparison rather than assigning a numerical value to happiness.'
    elif unit==5:
        for x,y in centers:
            draw.rounded_rectangle((x-135,y-125,x+135,y+125),radius=20,fill=pale,outline=teal,width=8)
            for dx in [-85,0,85]:
                draw.line((x+dx,y-165,x+dx,y-125),fill=teal,width=7);draw.line((x+dx,y+125,x+dx,y+165),fill=teal,width=7)
            draw.ellipse((x-48,y-48,x+48,y+48),outline=copper,width=12)
        for a,b in zip(centers,centers[1:]):link((a[0]+140,a[1]),(b[0]-140,b[1]))
        draw.arc((300,410,1800,830),190,350,fill=copper,width=7)
        desc='Connected tool modules sit inside a larger human review loop; processing an output and checking it are separate steps.'
    elif unit==6:
        for j,col in enumerate([teal,copper]):
            pts=[]
            for x in range(160,1950,5):pts.append((x,int(580+105*math.sin((x-160)/250+j*math.pi))))
            draw.line(pts,fill=col,width=16,joint='curve')
        for x,y in centers:draw.ellipse((x-52,y-52,x+52,y+52),fill='#'+PAPER,outline=teal,width=9)
        desc='Two distinct paths weave around shared meeting points without becoming a single path.'
    elif unit==7:
        nodes=[(200,450),(400,370),(700,450),(900,350),(1200,410),(1490,350),(1850,420),(310,720),(800,720),(1300,720),(1870,710)]
        nodes=[(x,y+80 if y<500 else y) for x,y in nodes]
        for i,p in enumerate(nodes):
            for q in nodes[i+1:]:
                if 200<math.dist(p,q)<650:draw.line((p,q),fill=rule,width=5)
        for x,y in nodes:draw.ellipse((x-23,y-23,x+23,y+23),fill=copper)
        for x,y in centers:draw.ellipse((x-100,y-100,x+100,y+100),fill=pale,outline=teal,width=8)
        link((510,580),(950,580));link((1150,580),(1590,580))
        desc='Local hubs connect through a wider network, showing links without claiming that access is equal everywhere.'
    else:
        for i,(x,y) in enumerate(centers):
            draw.rounded_rectangle((x-215,y-140,x+215,y+130),radius=90,outline=teal,width=8,fill=pale if i==1 else '#'+PAPER)
            for j in range(9):
                h=[25,55,95,70,120,45,80,35,65][(j+i*2)%9]
                draw.line((x-145+j*36,y-h/2,x-145+j*36,y+h/2),fill=copper if i==1 else teal,width=12)
        link((630,580),(830,580));link((1270,580),(1470,580))
        desc='Different speech waveforms connect through a shared exchange; different voices remain visibly distinct.'
    return desc


def compose_diagram(image, draw, unit, variant, data):
    draw.line((110,60,300,60),fill='#'+COPPER,width=10)
    label(draw,(110,92),f'UNIT {unit}  /  '+data['kicker'],48,color=ACCENT,bold=True)
    label(draw,(110,170),data['title'],82,width=1850,bold=True)
    label(draw,(110,285),data['subtitle'],56,color=MUTED,width=1850)
    description=scene(draw,unit,variant)
    for i,(title,body) in enumerate(data['cards']):
        x=110+i*640
        draw.line((x,805,x+555,805),fill='#'+RULE,width=3)
        y=label(draw,(x,825),title,58,width=555,bold=True)
        bottom=label(draw,(x,y+12),body,55,color=MUTED,width=555)
        if bottom>1180:raise ValueError(f'Diagram label overflows: {title}')
    return description


def main():
    plan=json.loads((ROOT/'book/master/self-contained-edition.json').read_text())
    record={'date':'2026-10-18','review_basis':'Original code-drawn teaching diagrams; labels and alternative text share the reviewed edition plan. No external artwork, stock imagery, screenshots or video logos. Font sources/licenses are recorded separately.','images':[]}
    provenance=[]
    for u in plan['units']:
        for variant in ['opener','reading','listening']:
            data=u['graphics'][variant]
            filename=f'edition-unit-{u["unit"]}-{variant}.png'
            image=Image.new('RGB',(W,H),'#'+PAPER);d=ImageDraw.Draw(image)
            description=compose_diagram(image,d,u['unit'],variant,data)

            path=ASSETS/filename;image.save(path,optimize=True)
            alt=description+' '+data['title']+'. '+data['subtitle']+' '+ ' '.join(f'{i+1}. {t}: {b}' for i,(t,b) in enumerate(data['cards']))
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

#!/usr/bin/env python3
"""Draw source-free, original vector-style illustrations for the Standard edition.

This renderer uses only geometric shapes and type included with the repository.
It deliberately does not import, trace, or imitate the manuscript's supplied art,
third-party thumbnails, video frames, logos, or identifiable speakers.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PAPER = '#F6F3EC'
INK = '#182B30'
TEAL = '#205F67'
BANNER = '#183D44'
BAND = '#EDF3F2'
RULE = '#CBD9D9'
COPPER = '#B77948'
WHITE = '#FFFFFF'
PALE = '#DCEAE5'
PALE_COPPER = '#F1E4D7'

ALT = {
    'image1.png': 'Original vector diagram: speaking and listening are linked by two arrows between two conversation bubbles.',
    'image2.png': 'Original vector illustration of two people exchanging speech bubbles.',
    'image3.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image4.gif': 'Original readable SMART planning graphic listing Specific, Measurable, Attainable, Realistic, and Timed; it does not reproduce the source mind map.',
    'image5.jpeg': 'Original vector illustration of steps leading toward a goal marker.',
    'image6.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image7.jpeg': 'Original vector illustration of a brain-like outline surrounded by simple emotion symbols.',
    'image8.jpeg': 'Original comparison diagram with separate IQ and EI circles; it does not rank either measure.',
    'image9.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image10.jpeg': 'Original vector illustration of a person beside a small group of coins, representing money as a discussion topic.',
    'image11.jpeg': 'Original vector illustration placing a coin, a heart, and a smile on equal footing as discussion symbols.',
    'image12.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image13.png': 'Original vector illustration of a home connected to devices by a simple network.',
    'image14.jpeg': 'Original vector comparison of two simplified face icons, one person-like and one robot-like.',
    'image15.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image16.png': 'Original vector illustration of two paths meeting at a heart.',
    'image17.jpeg': 'Original vector illustration of two people with a heart between them.',
    'image18.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image19.png': 'Original vector globe with lines linking several regions.',
    'image20.jpeg': 'Original vector illustration of a globe beside two generic buildings; no specific landmark is depicted.',
    'image21.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.',
    'image22.jpeg': 'Original vector signpost with neutral language labels pointing in different directions.',
    'image23.jpeg': 'Original vector globe with a question mark and a speech bubble reading English?',
    'image24.jpeg': 'Original generic listening-activity card with a play symbol; it identifies no recording, speaker, or publisher.'
}


def _font(path, size, bold=False):
    root = Path(__file__).resolve().parents[1] / 'assets' / 'fonts'
    name = 'source-sans-3-latin-700-normal.ttf' if bold else 'source-sans-3-latin-400-normal.ttf'
    return ImageFont.truetype(str(root / name), size)


def _bubble(draw, box, fill, text, font, outline=TEAL):
    draw.rounded_rectangle(box, radius=max(12, (box[3]-box[1])//8), fill=fill,
                           outline=outline, width=4)
    x0,y0,x1,y1=box
    draw.polygon([(x0+(x1-x0)//4,y1-2),(x0+(x1-x0)//4+35,y1+40),(x0+(x1-x0)//4+68,y1-2)],
                 fill=fill, outline=outline)
    draw.text(((x0+x1)//2,(y0+y1)//2),text,font=font,fill=INK,anchor='mm',align='center')


def _person(draw, cx, cy, scale=1.0, color=TEAL):
    r=int(45*scale)
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill=PALE_COPPER if color==COPPER else PALE,outline=color,width=max(3,int(5*scale)))
    draw.rounded_rectangle((cx-int(65*scale),cy+int(52*scale),cx+int(65*scale),cy+int(205*scale)),
                           radius=int(55*scale),fill=color)


def _heart(draw, cx, cy, size, color=COPPER):
    half=size//2
    draw.polygon([
        (cx, cy+half),
        (cx-half, cy+size//12),
        (cx-half, cy-size//5),
        (cx-size*3//8, cy-size*9//20),
        (cx-size//8, cy-size*9//20),
        (cx, cy-size//5),
        (cx+size//8, cy-size*9//20),
        (cx+size*3//8, cy-size*9//20),
        (cx+half, cy-size//5),
        (cx+half, cy+size//12),
    ], fill=color)


def _globe(draw, cx, cy, r, label=None):
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill=PALE,outline=TEAL,width=max(4,r//28))
    draw.arc((cx-r*3//4,cy-r,cx+r*3//4,cy+r),90,270,fill=TEAL,width=max(3,r//35))
    draw.arc((cx-r*3//4,cy-r,cx+r*3//4,cy+r),270,90,fill=TEAL,width=max(3,r//35))
    draw.arc((cx-r,cy-r//2,cx+r,cy+r//2),0,180,fill=TEAL,width=max(3,r//35))
    draw.arc((cx-r,cy-r//2,cx+r,cy+r//2),180,360,fill=TEAL,width=max(3,r//35))
    if label:
        draw.text((cx,cy),label,font=_font(None,max(24,r//4),True),fill=BANNER,anchor='mm')


def _resource_card(draw, W, H):
    draw.rounded_rectangle((int(W*.15),int(H*.17),int(W*.85),int(H*.83)),radius=42,
                           fill=WHITE,outline=RULE,width=5)
    cx,cy=int(W*.5),int(H*.48);r=int(min(W,H)*.15)
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill=TEAL)
    draw.polygon([(cx-int(r*.24),cy-int(r*.44)),(cx-int(r*.24),cy+int(r*.44)),
                  (cx+int(r*.5),cy)],fill=WHITE)
    draw.text((cx,int(H*.72)),'EXTERNAL LISTENING ACTIVITY',font=_font(None,int(H*.055),True),
              fill=BANNER,anchor='mm')
    draw.text((cx,int(H*.78)),'Recording details require course-owner confirmation',
              font=_font(None,int(H*.033)),fill=INK,anchor='mm')


def _draw(name, W, H, draw):
    m=min(W,H);cx,cy=W//2,H//2
    # consistent framing; no logos or third-party motifs
    draw.rounded_rectangle((8,8,W-9,H-9),radius=int(m*.035),outline=RULE,width=max(3,m//250))
    if name in {'image3.jpeg','image6.jpeg','image9.jpeg','image12.jpeg','image15.jpeg','image18.jpeg','image21.jpeg','image24.jpeg'}:
        _resource_card(draw,W,H);return
    if name=='image1.png':
        _bubble(draw,(int(W*.08),int(H*.19),int(W*.39),int(H*.54)),BAND,'SPEAK',_font(None,int(H*.09),True))
        _bubble(draw,(int(W*.61),int(H*.19),int(W*.92),int(H*.54)),PALE_COPPER,'LISTEN',_font(None,int(H*.09),True),COPPER)
        draw.line((int(W*.32),int(H*.74),int(W*.68),int(H*.74)),fill=TEAL,width=int(m*.025))
        draw.polygon([(int(W*.68),int(H*.74)),(int(W*.64),int(H*.69)),(int(W*.64),int(H*.79))],fill=TEAL)
        draw.polygon([(int(W*.32),int(H*.74)),(int(W*.36),int(H*.69)),(int(W*.36),int(H*.79))],fill=COPPER)
    elif name=='image2.png':
        _person(draw,int(W*.28),int(H*.57),.7,TEAL);_person(draw,int(W*.72),int(H*.57),.7,COPPER)
        _bubble(draw,(int(W*.09),int(H*.11),int(W*.44),int(H*.30)),BAND,'IDEA',_font(None,int(H*.07),True))
        _bubble(draw,(int(W*.57),int(H*.11),int(W*.91),int(H*.30)),PALE_COPPER,'RESPONSE',_font(None,int(H*.06),True),COPPER)
    elif name=='image4.gif':
        draw.text((cx,int(H*.14)),'SMART GOALS',font=_font(None,int(H*.075),True),fill=BANNER,anchor='mm')
        labels=[('S','SPECIFIC'),('M','MEASURABLE'),('A','ATTAINABLE'),('R','REALISTIC'),('T','TIMED')]
        colors=[TEAL,COPPER,TEAL,COPPER,TEAL]
        left=int(W*.16);right=int(W*.84);top=int(H*.235);row_h=int(H*.125)
        for i,((letter,label),col) in enumerate(zip(labels,colors)):
            y=top+i*row_h
            draw.rounded_rectangle((left,y,right,y+int(H*.105)),radius=22,
                                   fill=BAND if i%2==0 else PALE_COPPER,outline=col,width=4)
            badge=int(H*.075);bcx=left+int(H*.06);bcy=y+int(H*.0525)
            draw.ellipse((bcx-badge//2,bcy-badge//2,bcx+badge//2,bcy+badge//2),fill=col)
            draw.text((bcx,bcy),letter,font=_font(None,int(H*.048),True),fill=WHITE,anchor='mm')
            draw.text((left+int(H*.13),bcy),label,font=_font(None,int(H*.052),True),fill=col,anchor='lm')
    elif name=='image5.jpeg':
        x0=int(W*.14);base=int(H*.79);step=int(W*.1)
        for i in range(6):
            x=x0+i*step;y=base-(i+1)*int(H*.075)
            draw.rectangle((x,y,x+step,y+int(H*.075)),fill=TEAL if i%2==0 else BANNER)
        tx=int(W*.82);ty=int(H*.22)
        draw.ellipse((tx-65,ty-65,tx+65,ty+65),outline=COPPER,width=13)
        draw.ellipse((tx-25,ty-25,tx+25,ty+25),fill=COPPER)
        draw.line((int(W*.69),int(H*.25),tx,ty),fill=TEAL,width=7)
    elif name=='image7.jpeg':
        draw.ellipse((int(W*.37),int(H*.25),int(W*.63),int(H*.68)),fill=BAND,outline=TEAL,width=8)
        draw.line((cx,int(H*.30),cx,int(H*.62)),fill=TEAL,width=5)
        draw.arc((int(W*.39),int(H*.33),cx+10,int(H*.61)),265,95,fill=TEAL,width=5)
        draw.arc((cx-10,int(H*.33),int(W*.61),int(H*.61)),85,275,fill=TEAL,width=5)
        draw.arc((int(W*.42),int(H*.39),int(W*.50),int(H*.50)),70,290,fill=COPPER,width=4)
        draw.arc((int(W*.50),int(H*.39),int(W*.58),int(H*.50)),250,110,fill=COPPER,width=4)
        for ang in range(0,360,45):
            import math
            x=cx+int(W*.31*math.cos(math.radians(ang)));y=int(H*.47)+int(H*.31*math.sin(math.radians(ang)))
            draw.ellipse((x-46,y-46,x+46,y+46),fill=PALE_COPPER if ang%90 else PALE,outline=COPPER if ang%90 else TEAL,width=4)
            draw.arc((x-22,y-18,x+22,y+18),10,170,fill=INK,width=3)
    elif name=='image8.jpeg':
        for x,label,col,sub in [(int(W*.3),'IQ',TEAL,'COGNITIVE TESTS'),(int(W*.7),'EI',COPPER,'EMOTION-RELATED SKILLS')]:
            draw.ellipse((x-int(H*.18),int(H*.2),x+int(H*.18),int(H*.56)),fill=BAND if col==TEAL else PALE_COPPER,outline=col,width=8)
            draw.text((x,int(H*.38)),label,font=_font(None,int(H*.14),True),fill=col,anchor='mm')
            draw.text((x,int(H*.72)),sub,font=_font(None,int(H*.045),True),fill=INK,anchor='mm')
    elif name in {'image10.jpeg','image11.jpeg'}:
        _person(draw,int(W*.30),int(H*.57),.65,TEAL)
        for i in range(3 if name=='image11.jpeg' else 4):
            x=int(W*.52)+i*int(W*.07);y=int(H*.45)+(i%2)*int(H*.09)
            draw.ellipse((x,y,x+int(W*.08),y+int(W*.08)),fill=PALE_COPPER,outline=COPPER,width=5)
            draw.text((x+int(W*.04),y+int(W*.04)),'$',font=_font(None,int(H*.07),True),fill=BANNER,anchor='mm')
        if name=='image11.jpeg':
            _heart(draw,int(W*.80),int(H*.55),int(H*.20),COPPER)
            draw.arc((int(W*.72),int(H*.69),int(W*.88),int(H*.79)),0,180,fill=TEAL,width=8)
    elif name=='image13.png':
        x0=int(W*.28);y0=int(H*.37);x1=int(W*.72);y1=int(H*.78)
        draw.polygon([(x0,y0),(cx,int(H*.15)),(x1,y0)],fill=PALE_COPPER,outline=COPPER)
        draw.rectangle((x0,y0,x1,y1),fill=BAND,outline=TEAL,width=8)
        draw.rectangle((int(W*.45),int(H*.55),int(W*.55),y1),fill=WHITE,outline=TEAL,width=5)
        for px,py in [(int(W*.16),int(H*.27)),(int(W*.84),int(H*.27)),(int(W*.5),int(H*.1))]:
            draw.ellipse((px-35,py-35,px+35,py+35),fill=WHITE,outline=COPPER,width=5)
            draw.line((px,py+35,cx,int(H*.37)),fill=RULE,width=5)
    elif name=='image14.jpeg':
        draw.ellipse((int(W*.18),int(H*.17),int(W*.47),int(H*.75)),fill=BAND,outline=TEAL,width=8)
        draw.ellipse((int(W*.53),int(H*.17),int(W*.82),int(H*.75)),fill=PALE_COPPER,outline=COPPER,width=8)
        draw.arc((int(W*.25),int(H*.4),int(W*.39),int(H*.55)),180,350,fill=INK,width=5)
        draw.arc((int(W*.61),int(H*.4),int(W*.75),int(H*.55)),180,350,fill=INK,width=5)
        draw.line((int(W*.32),int(H*.32),int(W*.36),int(H*.32)),fill=INK,width=8)
        draw.rectangle((int(W*.65),int(H*.30),int(W*.69),int(H*.34)),fill=COPPER)
    elif name=='image16.png':
        draw.arc((int(W*.12),int(H*.15),int(W*.88),int(H*.85)),190,350,fill=TEAL,width=15)
        draw.arc((int(W*.12),int(H*.15),int(W*.88),int(H*.85)),10,170,fill=COPPER,width=15)
        _heart(draw,cx,int(H*.51),int(H*.22),COPPER)
    elif name=='image17.jpeg':
        _person(draw,int(W*.31),int(H*.55),.65,TEAL);_person(draw,int(W*.69),int(H*.55),.65,COPPER)
        _heart(draw,cx,int(H*.46),int(H*.18),COPPER)
    elif name in {'image19.png','image20.jpeg','image22.jpeg','image23.jpeg'}:
        if name=='image19.png':
            _globe(draw,cx,cy,int(H*.28))
            for dx,dy in [(-.29,-.16),(.3,-.18),(-.25,.24),(.31,.25)]:
                x=int(cx+W*dx);y=int(cy+H*dy);draw.ellipse((x-22,y-22,x+22,y+22),fill=COPPER)
                draw.line((cx,cy,x,y),fill=TEAL,width=5)
        elif name=='image20.jpeg':
            _globe(draw,int(W*.75),int(H*.55),int(H*.2))
            draw.rectangle((int(W*.12),int(H*.58),int(W*.26),int(H*.81)),fill=TEAL)
            draw.polygon([(int(W*.09),int(H*.58)),(int(W*.19),int(H*.41)),(int(W*.29),int(H*.58))],fill=COPPER)
            draw.rectangle((int(W*.36),int(H*.47),int(W*.52),int(H*.81)),fill=BANNER)
            draw.polygon([(int(W*.34),int(H*.47)),(int(W*.44),int(H*.29)),(int(W*.54),int(H*.47))],fill=TEAL)
        elif name=='image22.jpeg':
            draw.line((cx,int(H*.2),cx,int(H*.82)),fill=BANNER,width=18)
            labels=['LANGUAGE 1','LANGUAGE 2','LANGUAGE 3','LANGUAGE 4']
            for i,label in enumerate(labels):
                y=int(H*(.28+i*.14));direction=1 if i%2==0 else -1
                x0=cx if direction==1 else int(W*.22);x1=int(W*.76) if direction==1 else cx
                draw.rounded_rectangle((x0,y,x1,y+int(H*.09)),radius=18,fill=TEAL if i%2==0 else COPPER)
                draw.polygon([(x1,y),(x1+direction*32,y+int(H*.045)),(x1,y+int(H*.09))],fill=TEAL if i%2==0 else COPPER)
                draw.text(((x0+x1)//2,y+int(H*.045)),label,font=_font(None,int(H*.038),True),fill=WHITE,anchor='mm')
        else:
            _globe(draw,int(W*.38),cy,int(H*.28))
            draw.rounded_rectangle((int(W*.58),int(H*.34),int(W*.9),int(H*.62)),radius=25,fill=WHITE,outline=COPPER,width=6)
            draw.text((int(W*.74),int(H*.48)),'ENGLISH?',font=_font(None,int(H*.07),True),fill=BANNER,anchor='mm')
    else:
        # Safe generic motif if an image is added to the set later.
        draw.ellipse((int(W*.32),int(H*.18),int(W*.68),int(H*.72)),fill=BAND,outline=TEAL,width=8)
        draw.text((cx,cy),'SPEAK',font=_font(None,int(H*.09),True),fill=BANNER,anchor='mm')


def generate(source_name, destination, source_size=(1200,675)):
    """Write one original flat-vector illustration in the source slot's aspect ratio."""
    width=1600
    height=max(600,round(width*source_size[1]/source_size[0]))
    if source_name.endswith('.gif'):
        height=round(width*source_size[1]/source_size[0])
    image=Image.new('RGB',(width,height),PAPER)
    draw=ImageDraw.Draw(image)
    _draw(source_name,width,height,draw)
    ext=Path(source_name).suffix.lower()
    if ext in ('.jpg','.jpeg'):
        image.save(destination,format='JPEG',quality=94,optimize=True)
    elif ext=='.gif':
        image.save(destination,format='GIF',optimize=True)
    else:
        image.save(destination,format='PNG',optimize=True)
    return ALT[source_name]

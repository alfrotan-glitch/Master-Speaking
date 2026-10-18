#!/usr/bin/env python3
"""Create an original vector front-cover concept and ebook raster asset.

7 x 10 inches, front only, no bleed/spine/back; NOT a printer-ready wrap.
No stock art, invented endorsements, ISBNs, or proficiency certifications.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / 'Master-Speaking-Front-Cover.pdf'
PNG = ROOT / 'book/assets/cover.png'


def build():
    fonts = ROOT / 'book/assets/fonts'
    for name, file in [('CoverSans', 'source-sans-3-latin-400-normal.ttf'),
                       ('CoverBold', 'source-sans-3-latin-700-normal.ttf'),
                       ('CoverSerif', 'source-serif-4-latin-600-normal.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / file)))
    c = canvas.Canvas(str(PDF), pagesize=(504, 720))
    c.setTitle('Master Speaking')
    c.setAuthor('Abdul Raziq Nazari')
    from design import PAPER, BANNER, ACCENT, COPPER, RULE
    c.setFillColor(HexColor('#'+PAPER)); c.rect(0, 0, 504, 720, fill=1, stroke=0)
    c.setFillColor(HexColor('#'+ACCENT)); c.setFont('CoverBold', 10)
    c.drawString(42, 666, 'THE TOEFL HOUSE')
    c.setStrokeColor(HexColor('#'+RULE)); c.setLineWidth(.6); c.line(42, 646, 462, 646)
    c.setFont('CoverSans', 10); c.drawString(42, 619, 'READ  /  LISTEN  /  DISCUSS  /  PRESENT')
    c.setFillColor(HexColor('#'+BANNER)); c.setFont('CoverSerif', 60)
    c.drawString(39, 548, 'Master')
    c.drawString(39, 482, 'Speaking')
    c.setFont('CoverSans', 16); c.drawString(42, 444, 'Think clearly. Speak with purpose.')
    c.setFont('CoverSans', 11)
    c.drawString(42, 419, 'An English speaking course in eight thematic units')
    # Original vector conversation paths: distinct voices meeting in a shared space.
    for index in range(8):
        c.setStrokeColor(HexColor('#'+(COPPER if index == 3 else ACCENT)))
        c.setLineWidth(1.2 if index == 3 else .65)
        offset = index * 12
        path = c.beginPath(); path.moveTo(42, 176+offset)
        path.curveTo(150, 166+offset, 162, 362-offset*.15, 271, 337-offset*.2)
        path.curveTo(363, 318-offset*.12, 365, 195+offset*.25, 462, 219+offset*.65)
        c.drawPath(path)
    c.setFillColor(HexColor('#'+COPPER)); c.circle(271, 330, 5, stroke=0, fill=1)
    c.setFillColor(HexColor('#'+BANNER)); c.rect(0, 0, 504, 108, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF')); c.setFont('CoverSans', 12)
    c.drawString(42, 64, 'ABDUL RAZIQ NAZARI')
    c.setFont('CoverSans', 9)
    c.drawString(42, 39, 'Communication  /  Critical thinking  /  Real-world discussion')
    c.save()
    with pymupdf.open(PDF) as doc:
        doc[0].get_pixmap(matrix=pymupdf.Matrix(3, 3)).save(PNG)
    # Matching original back panel; the printer must still impose the two
    # panels on a template with its confirmed spine and bleed dimensions.
    from reportlab.platypus import Paragraph
    from reportlab.lib.styles import ParagraphStyle
    back = ROOT / 'Master-Speaking-Back-Cover.pdf'
    c = canvas.Canvas(str(back), pagesize=(504, 720))
    c.setTitle('Master Speaking — Back Cover'); c.setAuthor('Abdul Raziq Nazari')
    c.setFillColor(HexColor('#'+PAPER)); c.rect(0, 0, 504, 720, fill=1, stroke=0)
    c.setFillColor(HexColor('#'+BANNER)); c.rect(0, 560, 504, 160, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF')); c.setFont('CoverSerif', 27)
    c.drawString(42, 656, 'Make your meaning clear.')
    c.drawString(42, 616, 'Give another voice room.')
    style = ParagraphStyle('back', fontName='CoverSans', fontSize=12, leading=18,
                           textColor=HexColor('#'+BANNER))
    sections = [
        'Master Speaking brings reading, listening, discussion and short research presentations together across eight themes. Build a clear point, support it with an example, and use feedback to make your next attempt stronger.',
        '<b>READ</b> to explore an idea and explain what a passage supports.<br/>'
        '<b>LISTEN</b> to an original story, recover details and clarify meaning.<br/>'
        '<b>DISCUSS</b> a question from more than one perspective.<br/>'
        '<b>PRESENT</b> a focused answer using identifiable sources.',
        'Eight units. Thirty-two chapters. Topic language, pronunciation practice, reflection and repeatable speaking tasks.',
        'Fictional listening scripts are included for a teacher or partner to read aloud. No external video or subscription is required.'
    ]
    y=520
    for text in sections:
        paragraph=Paragraph(text,style); _,height=paragraph.wrap(420,600)
        paragraph.drawOn(c,42,y-height);y-=height+26
    c.setStrokeColor(HexColor('#'+COPPER));c.setLineWidth(2);c.line(42,132,462,132)
    c.setFillColor(HexColor('#'+ACCENT));c.setFont('CoverBold',11)
    c.drawString(42,100,'ABDUL RAZIQ NAZARI')
    c.setFont('CoverSans',10);c.drawString(42,76,'THE TOEFL HOUSE')
    c.save()
    print(f'Built {PDF.name}, {back.name} and {PNG.relative_to(ROOT)}')


if __name__ == '__main__':
    build()

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
    c.setFillColor(HexColor('#F5F2E9')); c.rect(0, 0, 504, 720, fill=1, stroke=0)
    c.setFillColor(HexColor('#123E35')); c.rect(0, 0, 504, 155, fill=1, stroke=0)
    c.setFillColor(HexColor('#176653')); c.setFont('CoverBold', 10)
    c.drawString(42, 665, 'THE TOEFL HOUSE')
    c.setStrokeColor(HexColor('#176653')); c.setLineWidth(.75); c.line(42, 643, 462, 643)
    c.setFillColor(HexColor('#123E35')); c.setFont('CoverSerif', 58)
    c.drawString(39, 563, 'Master')
    c.drawString(39, 501, 'Speaking')
    c.setFont('CoverSans', 16); c.drawString(42, 459, 'Think clearly. Speak with purpose.')
    c.setFont('CoverSans', 11)
    c.drawString(42, 431, 'An English speaking course in eight thematic units')
    # Interlocking speech shapes express dialogue, not stock imagery.
    c.setFillColor(HexColor('#B5DCCE'))
    c.roundRect(42, 240, 270, 147, 25, fill=1, stroke=0)
    p = c.beginPath(); p.moveTo(77, 246); p.lineTo(77, 214); p.lineTo(117, 246); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(HexColor('#176653'))
    c.roundRect(237, 196, 225, 125, 24, fill=1, stroke=0)
    p = c.beginPath(); p.moveTo(421, 202); p.lineTo(421, 173); p.lineTo(383, 202); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(HexColor('#123E35')); c.setFont('CoverSerif', 23)
    c.drawString(64, 341, 'Ideas worth sharing.')
    c.setFont('CoverSans', 12); c.drawString(65, 306, 'Read. Listen. Discuss. Present.')
    c.setFillColor(HexColor('#FFFFFF')); c.setFont('CoverBold', 14)
    c.drawString(260, 269, 'Your voice matters.')
    c.setFont('CoverSans', 11); c.drawString(260, 239, 'Build understanding together.')
    c.setFillColor(HexColor('#FFFFFF')); c.setFont('CoverSans', 12)
    c.drawString(42, 112, 'ABDUL RAZIQ NAZARI')
    c.setFont('CoverSans', 10)
    c.drawString(42, 77, 'Communication • Critical thinking • Real-world discussion')
    c.setStrokeColor(HexColor('#7EAA98')); c.line(42, 57, 462, 57)
    c.save()
    with pymupdf.open(PDF) as doc:
        doc[0].get_pixmap(matrix=pymupdf.Matrix(3, 3)).save(PNG)
    print(f'Built {PDF.name} and {PNG.relative_to(ROOT)}')


if __name__ == '__main__':
    build()

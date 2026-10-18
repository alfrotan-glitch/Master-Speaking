"""Modern editorial edition: restrained forest/teal, white tables, quiet rules.

Shared across Word, PDF, EPUB and cover. Copper is decorative, not body text.
Contrast checks cover default colors, not whole-book accessibility certification.
"""
BAND = 'EDF3F2'
BANNER = '183D44'
ACCENT = '205F67'
INK = '182B30'
MUTED = '52656A'
RULE = 'CBD9D9'
ZEBRA = 'F5F8F7'
COPPER = 'B77948'
PAPER = 'F6F3EC'


def contrast(fg, bg):
    def luminance(value):
        rgb = [int(value[i:i+2], 16) / 255 for i in (0, 2, 4)]
        rgb = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
        return sum(c * weight for c, weight in zip(rgb, (.2126, .7152, .0722)))
    a, b = sorted((luminance(fg), luminance(bg)))
    return (b + .05) / (a + .05)

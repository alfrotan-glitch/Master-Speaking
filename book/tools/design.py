"""Shared edition palette: dark type, pale bands, high-contrast teal accents.

Original content images/table fills are retained; this is not a claim that
all imagery or all EPUB themes meet an accessibility standard.
"""
BAND = 'E2F2EC'
BANNER = '145C4D'
ACCENT = '176653'
INK = '14181A'


def contrast(fg, bg):
    def luminance(value):
        rgb = [int(value[i:i+2], 16) / 255 for i in (0, 2, 4)]
        rgb = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
        return sum(c * weight for c, weight in zip(rgb, (.2126, .7152, .0722)))
    a, b = sorted((luminance(fg), luminance(bg)))
    return (b + .05) / (a + .05)

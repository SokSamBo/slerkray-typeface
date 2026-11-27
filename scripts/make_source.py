"""Generate a starter UFO source for Slerkray (Regular) with a few placeholder glyphs."""
from pathlib import Path

import ufoLib2
from fontTools.pens.pointPen import SegmentToPointPen

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "sources" / "Slerkray-Regular.ufo"


def rect(glyph, x0, y0, x1, y1):
    pen = SegmentToPointPen(glyph.getPointPen())
    pen.moveTo((x0, y0))
    pen.lineTo((x0, y1))
    pen.lineTo((x1, y1))
    pen.lineTo((x1, y0))
    pen.closePath()


def main():
    font = ufoLib2.Font()
    info = font.info
    info.familyName = "Slerkray"
    info.styleName = "Regular"
    info.unitsPerEm = 1000
    info.ascender = 800
    info.descender = -200
    info.capHeight = 700
    info.xHeight = 500
    info.versionMajor, info.versionMinor = 0, 1
    info.openTypeOS2WeightClass = 400

    g = font.newGlyph(".notdef"); g.width = 500
    rect(g, 50, 0, 450, 700); rect(g, 100, 50, 400, 650)  # inner counter
    g = font.newGlyph("space"); g.width = 250; g.unicodes = [0x20]

    g = font.newGlyph("I"); g.width = 300; g.unicodes = [ord("I")]
    rect(g, 110, 0, 190, 700)
    g = font.newGlyph("H"); g.width = 640; g.unicodes = [ord("H")]
    rect(g, 80, 0, 160, 700); rect(g, 480, 0, 560, 700); rect(g, 160, 310, 480, 390)

    font.glyphOrder = [".notdef", "space", "H", "I"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    font.save(OUT, overwrite=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

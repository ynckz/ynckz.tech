#!/usr/bin/env python3
"""
Растягивает Allo по горизонтали: контуры, метрики и GPOS-кернинг.

Зачем: в макете Figma текст набран Benzin, а он заметно шире Allo. Без этого
строки и меню выглядят уже макета (discord 72 px против 90). Растяжение на 25%
совпадает с ширинами Figma, высота строк при этом не меняется.

Это производная работа по SIL OFL 1.1: шрифт изменён, лицензия та же
(font-source/OFL-Allo.txt). Исходники -- статические OTF из PR #8 к Allo
(font-source/allo-*.otf, см. allo-info.txt).

Запуск:
    python3 font-source/widen-allo.py font-source/allo-medium.otf /tmp/allo-medium-wide.otf 1.25
    python3 -m fontTools.subset /tmp/allo-medium-wide.otf \
        --text-file=font-source/charset-allo.txt --flavor=woff2 \
        --output-file=assets-src/fonts/allo-medium.woff2
"""

import argparse
import pathlib

from fontTools.misc.transform import Transform
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


def scale_value_record(v, sx):
    if v is None:
        return
    for attr in ("XPlacement", "XAdvance"):
        if hasattr(v, attr) and getattr(v, attr) is not None:
            setattr(v, attr, round(getattr(v, attr) * sx))


def scale_anchor(a, sx):
    if a is not None and getattr(a, "XCoordinate", None) is not None:
        a.XCoordinate = round(a.XCoordinate * sx)


def walk_gpos_subtable(st, sx):
    if st is None:
        return
    fmt = st.__class__.__name__
    if fmt == "SinglePos":
        if st.Format == 1:
            scale_value_record(st.Value, sx)
        else:
            for v in st.Value:
                scale_value_record(v, sx)
    elif fmt == "PairPos":
        if st.Format == 1:
            for ps in st.PairSet:
                for rec in ps.PairValueRecord:
                    scale_value_record(rec.Value1, sx)
                    scale_value_record(rec.Value2, sx)
        else:
            for c1 in st.Class1Record:
                for c2 in c1.Class2Record:
                    scale_value_record(c2.Value1, sx)
                    scale_value_record(c2.Value2, sx)
    elif fmt == "CursivePos":
        for rec in st.EntryExitRecord:
            scale_anchor(rec.EntryAnchor, sx)
            scale_anchor(rec.ExitAnchor, sx)
    elif fmt in ("MarkBasePos", "MarkLigPos", "MarkMarkPos"):
        # В тексте сайта нет комбинируемых диакритик; якоря не трогаем.
        pass
    elif fmt == "ExtensionPos":
        walk_gpos_subtable(st.ExtSubTable, sx)


def widen(src: pathlib.Path, dst: pathlib.Path, sx: float):
    font = TTFont(src)
    glyph_set = font.getGlyphSet()
    top = font["CFF "].cff.topDictIndex[0]
    hmtx = font["hmtx"]
    order = font.getGlyphOrder()

    new_cs = {}
    nominal = top.Private.nominalWidthX
    for name in order:
        width, lsb = hmtx[name]
        # T2CharStringPen кладёт переданное число как operand ширины,
        # а CFF-ширина = nominalWidthX + operand.
        pen = T2CharStringPen(round(width * sx) - nominal, glyph_set)
        glyph_set[name].draw(TransformPen(pen, Transform(sx, 0, 0, 1, 0, 0)))
        new_cs[name] = pen.getCharString(top.Private, top.GlobalSubrs)

    for name, cs in new_cs.items():
        top.CharStrings[name] = cs
        width, lsb = hmtx[name]
        hmtx[name] = (round(width * sx), round(lsb * sx))

    # GPOS: ширины и горизонтальные позиции тоже в юнитах шрифта.
    if "GPOS" in font:
        gpos = font["GPOS"].table
        if gpos.FeatureList:
            for fr in gpos.FeatureList.FeatureRecord:
                for li in fr.Feature.LookupListIndex:
                    lookup = gpos.LookupList.Lookup[li]
                    for st in lookup.SubTable:
                        walk_gpos_subtable(st, sx)

    font["OS/2"].xAvgCharWidth = round(font["OS/2"].xAvgCharWidth * sx)

    dst.parent.mkdir(parents=True, exist_ok=True)
    font.save(dst)
    print(f"saved {dst} sx={sx}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src", type=pathlib.Path)
    ap.add_argument("dst", type=pathlib.Path)
    ap.add_argument("sx", type=float, help="horizontal scale, e.g. 1.25")
    a = ap.parse_args()
    widen(a.src, a.dst, a.sx)

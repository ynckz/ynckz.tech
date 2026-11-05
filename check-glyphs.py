#!/usr/bin/env python3
"""
Проверяет, что каждый символ, который рисуется на странице, есть в сабсете шрифта.

Зачем: шрифты в assets-src/fonts/ урезаны до нужных символов. Если в index.smd
появится буква/знак, которого в сабсете нет, браузер молча нарисует его
системным шрифтом -- вёрстка поедет, а ошибки никто не увидит.

Запуск:   python3 check-glyphs.py            # проверить content/index.smd
          python3 check-glyphs.py другой.smd # проверить другой файл
Код выхода 1, если чего-то не хватает.

Нужен fonttools:  pip install fonttools brotli
"""

import pathlib
import re
import sys

from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).parent
FONTS = ROOT / "assets-src" / "fonts"


def glyphs(path: pathlib.Path) -> set[str]:
    return {chr(c) for c in TTFont(path).getBestCmap()}


def main() -> int:
    smd_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "content" / "index.smd"
    smd = smd_path.read_text(encoding="utf-8")

    # // комментарии не рендерятся -- выкидываем
    smd = re.sub(r"^\s*//.*$", "", smd, flags=re.M)

    # prompt рисуется Nova Mono, всё остальное -- Benzin
    prompt_m = re.search(r'\.prompt\s*=\s*"((?:[^"\\]|\\.)*)"', smd)
    prompt = prompt_m.group(1) if prompt_m else ""
    rest = smd.replace(prompt_m.group(0), "") if prompt_m else smd

    # .description и .title попадают только в <head>, не на экран
    rest = re.sub(r'\.(?:description|title|date)\s*=\s*"(?:[^"\\]|\\.)*"', "", rest)
    # url/copy/badge/icon/soon не рисуются как текст (.title у бейджей -- это
    # подсказка при наведении, она уже вырезана выше вместе с остальными .title)
    rest = re.sub(r'\.(?:url|copy|badge|icon|soon)\s*=\s*"(?:[^"\\]|\\.)*"', "", rest)

    benzin_text = "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', rest))

    # статический текст в шаблоне (например "/")
    shtml = (ROOT / "layouts" / "index.shtml").read_text(encoding="utf-8")
    benzin_text += "".join(re.findall(r">([^<>$\n]+)<", shtml))

    checks = [
        ("benzin-regular", benzin_text),
        ("benzin-medium", benzin_text),
        ("novamono-regular", prompt),
    ]

    bad = False
    for name, text in checks:
        have = glyphs(FONTS / f"{name}.woff2")
        missing = sorted({c for c in text if not c.isspace()} - have)
        if missing:
            bad = True
            print(f"НЕТ в {name}: {' '.join(missing)}  "
                  f"({' '.join('U+%04X' % ord(c) for c in missing)})")
        else:
            print(f"ok   {name}")

    if bad:
        print("\nДобавь недостающие символы в font-source/charset-*.txt и пересобери "
              "шрифты (команды -- в docs/FONTS.md).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

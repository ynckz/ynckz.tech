#!/usr/bin/env python3
"""
Собирает assets/assets.css из файлов в assets-src/.

Всё (шрифты, аватар, бейджи, эмодзи) инлайнится в один CSS как base64,
чтобы страница грузилась за минимум запросов.

Запуск:  python3 build-assets.py
Потом:   zine release

Чтобы добавить/заменить бейдж:
  1. положи .webp (88x31) в assets-src/badges/ с именем вида "04-название.webp"
  2. запусти этот скрипт
  3. пропиши .badge = "04" в content/index.smd

Чтобы заменить эмодзи:
  1. положи .webp в assets-src/emoji/имя.webp
  2. в content/index.smd укажи .icon = "имя"
"""

import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "assets-src"
OUT = ROOT / "assets" / "assets.css"

# размер, до которого ужимаются эмодзи в вёрстке
EMOJI_PX = 20


def data_uri(path: pathlib.Path) -> str:
    mime = {
        ".webp": "image/webp",
        ".png": "image/png",
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".woff2": "font/woff2",
    }[path.suffix.lower()]
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def main() -> int:
    if not SRC.is_dir():
        print(f"нет папки {SRC}", file=sys.stderr)
        return 1

    out: list[str] = []
    report: list[tuple[str, int]] = []

    # --- шрифты ---
    fonts = [
        ("Benzin", 400, SRC / "fonts" / "benzin-regular.woff2"),
        ("Benzin", 500, SRC / "fonts" / "benzin-medium.woff2"),
        ("Nova Mono", 400, SRC / "fonts" / "novamono-regular.woff2"),
    ]
    for family, weight, path in fonts:
        if not path.exists():
            print(f"пропущен шрифт (нет файла): {path}", file=sys.stderr)
            continue
        out.append(
            f'@font-face{{font-family:"{family}";'
            f"src:url({data_uri(path)}) format('woff2');"
            f"font-weight:{weight};font-style:normal;font-display:swap}}"
        )
        report.append((path.name, path.stat().st_size))

    # --- аватар ---
    avatar = SRC / "avatar.webp"
    if avatar.exists():
        out.append(f".avatar{{background-image:url({data_uri(avatar)})}}")
        report.append((avatar.name, avatar.stat().st_size))

    # --- бейджи: имя файла "00-scclie.webp" -> класс .badge-00 ---
    for path in sorted((SRC / "badges").glob("*.webp")):
        key = path.stem.split("-", 1)[0]
        out.append(f'.badge[data-badge="{key}"]{{background-image:url({data_uri(path)})}}')
        report.append((path.name, path.stat().st_size))

    # --- эмодзи: "fire.webp" -> класс .emoji-fire ---
    for path in sorted((SRC / "emoji").glob("*.webp")):
        out.append(f'.emoji[data-icon="{path.stem}"]{{background-image:url({data_uri(path)})}}')
        report.append((path.name, path.stat().st_size))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")

    total_src = sum(size for _, size in report)
    print(f"собрано {len(report)} ассетов ({total_src / 1024:.1f} KB исходников)")
    print(f"-> {OUT.relative_to(ROOT)}: {OUT.stat().st_size / 1024:.1f} KB")
    print(f"   (+~33% от base64; gzip вернёт почти всё обратно)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

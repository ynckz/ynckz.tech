# NOTICE

Copyright (c) 2026 ynckz.

`LICENSE` (MIT) распространяется только на исходный код и документацию:
`layouts/`, `*.py`, `zine.ziggy`, `wrangler.jsonc`, `.github/`, `README.md`.

Всё, что перечислено ниже, **не** покрыто MIT. Права остаются у авторов
и правообладателей.

## Контент сайта

`content/index.smd` (тексты, ссылки, ники), `assets-src/badges/mine-ynckz.webp`,
`assets/ynckz.webp` — © ynckz, all rights reserved.

`assets-src/avatar-original.jpg`, `assets-src/avatar.webp` — перекрашенный
и сжатый кадр из аниме; права на исходное изображение принадлежат его
правообладателям. MIT на аватар не распространяется.

Смотреть и ссылаться можно. Копировать тексты и картинки и выдавать за свои —
нельзя. `assets/age.txt` — публичный ключ, прав на него нет ни у кого.

## Шрифты

**Benzin** — `font-source/benzin-*.ttf`, `assets-src/fonts/benzin-*.woff2`.
Free for Personal Use (см. `font-source/info.txt`,
источник: <https://fontlot.com/benzin-font-family/>). Лицензия MIT на шрифт
не распространяется, права у автора шрифта. Для коммерческого использования
или распространения вне личного проекта нужна отдельная лицензия.

**Nova Mono** — `font-source/novamono.ttf`,
`assets-src/fonts/novamono-regular.woff2`. SIL Open Font License 1.1,
текст лицензии — `font-source/OFL.txt`. © 2011 wmk69, Reserved Font Name
NovaMono.

## Эмодзи

`assets-src/emoji/*.webp` — изображения Apple Color Emoji, © Apple Inc.
Взяты из открытого датасета [iamcal/emoji-data](https://github.com/iamcal/emoji-data).
MIT их не покрывает. Для коммерческого проекта замени на открытый набор
(Noto Emoji, Twemoji) — код сайта от этого не меняется.

## Чужие 88×31

`assets-src/badges/` — бейджи, права у их авторов:

| файл | откуда |
|---|---|
| `00-scclie.webp` | <https://sccl.cc> |
| `01-alina.webp` | <https://tei.pet> |
| `02-zine-beta.webp` | <https://zine-ssg.io> |
| `03-aseprite.webp` | <https://www.aseprite.org> |
| `04-otomir.webp` | <https://otomir23.me> |

Они лежат здесь как ссылки/превью и не лицензируются этим репозиторием.

## Сгенерированные файлы

`assets/assets.css` и `public/` собираются скриптами и содержат base64
тех же шрифтов, эмодзи и бейджей. На встроенные данные действуют лицензии
выше, а не MIT. Скрипты сборки (`build-assets.py`) — часть исходников.

## Zine

Сайт собран на [Zine](https://zine-ssg.io) (MIT). Бинарник скачивается
в CI и в репозитории не лежит.

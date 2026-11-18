# NOTICE

Copyright (c) 2026 ynckz.

`LICENSE` (MIT) распространяется только на исходный код и документацию:
`layouts/`, `*.py`, `zine.ziggy`, `wrangler.jsonc`, `.github/`, `README.md`.

Всё, что перечислено ниже, **не** покрыто MIT. Права остаются у авторов
и правообладателей.

## Контент сайта

`content/index.smd` (тексты, ссылки, ники), `assets-src/badges/mine-ynckz.webp`,
`assets/ynckz.webp`, `assets-src/favicon.png`, `assets/favicon.webp` — © ynckz,
all rights reserved.

`assets-src/avatar-original.jpg`, `assets-src/avatar.webp` — перекрашенный
и сжатый кадр из аниме; права на исходное изображение принадлежат его
правообладателям. MIT на аватар не распространяется.

`assets-src/ogcontacts.webp`, `assets/ogcontacts.webp` — фанарт (Kurisu Makise из
Steins;Gate). Источник — пост [@DailySteinsGate](https://x.com/DailySteinsGate/status/2057524578092560685)
от 21.05.2026 («El psy congroo.»). Это фан-аккаунт-агрегатор: **автор самой иллюстрации
в посте не указан**, так что credit стоит на аккаунте-публикаторе, а не на художнике.
Права принадлежат автору иллюстрации и правообладателям франшизы; MIT не покрывает.

Смотреть и ссылаться можно. Копировать тексты и картинки и выдавать за свои —
нельзя. `assets/age.txt` — публичный ключ, прав на него нет ни у кого.

## Шрифты

**Allo** — `font-source/allo-medium.otf`, `font-source/allo-bold.otf`,
`assets-src/fonts/allo-*.woff2`. Оригинальный Allo © 2026 Josh Puckett
(<https://allo.joshpuckett.me/>, <https://github.com/joshpuckett/allo>),
кириллица © 2026 Degroshi (<https://github.com/degroshi>), часть глифов из
Inter © 2016 The Inter Project Authors. Кириллицу добавили в исходники Allo
в PR #8 (<https://github.com/joshpuckett/allo/pull/8>, ветка `degroshi:cyrillic`,
коммит `9623d58`); оттуда взяты статические OTF Medium и Bold. Сабсеты собраны
из модифицированной версии: контуры, метрики и кернинг растянуты по горизонтали
на 25% (`font-source/widen-allo.py`), чтобы ширина текста совпадала с макетом,
набранным Benzin. Это производная работа по OFL, имя шрифта не зарезервировано.
Лицензия SIL Open Font License 1.1, текст — `font-source/OFL-Allo.txt`. MIT на
шрифт не распространяется; OFL разрешает использование, изменение и встраивание,
но не продажу шрифта отдельно.

**Benzin** — `font-source/benzin-regular.ttf`,
`assets-src/fonts/benzin-regular.woff2`. © Roman Postovoy (Supremat).
Free for Personal Use (см. `font-source/info.txt`,
источник: <https://fontlot.com/benzin-font-family/>). Лицензия MIT на шрифт
не распространяется, права у автора шрифта. Для коммерческого использования
или распространения вне личного проекта нужна отдельная лицензия. На сайте
Benzin набран только текст в фигурных скобках (`{contacts}`, `{ age key }` …).

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

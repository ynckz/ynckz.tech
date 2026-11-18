# ynckz.tech


## шо где как

```
content/index.smd              ← контент индех страницы
layouts/index.shtml            ← каркас страницы (циклы по данным из .smd)
layouts/templates/base.shtml   ← <head> + весь ксс инлайном
assets-src/                    ← исходники: avatar, badges/, emoji/, fonts/
font-source/                   ← лицензии и справка по шрифтам (сами OTF — в ynckz/allo)
assets/assets.css              ← СГЕНЕРИРОВАН build-assets.py, руками НЕ ТРОГАТЬ СУКАА
build-assets.py                ← собирает assets.css из assets-src/
check-glyphs.py                ← проверяет шо все символы страницы есть в шрифтах
```


## частые правки

**добавить контакт** — строка в `.contacts` в `content/index.smd` ( ахиреть штоо):

```zig
.{ .service = "mastodon", .url = "https://…", .value = "@ynckz", .copy = "@ynckz", .icon = "fire" },
```

- `service` — кликается, ведёт на `url`
- `value` — что показано; по клику в буфер копируется `copy` (удобно для длинных
  адресов: показываешь `0x4Ead1...31735F`, копируется весь)
- `icon` — имя файла из `assets-src/emoji/` без `.webp`

**добавить эмодзи:** надо положить 40×40 webp в `assets-src/emoji/`, запустить `build-assets.py`
и указать имя в `.icon`. ток эппл эмоджи, иначе еще больше говняшка безвкусная будет 

**добавить 88×31:** положить webp в `assets-src/badges/` с именем `**-название.webp`,
запустиьб `build-assets.py` и добавить в `.badges`:

```zig
.{ .badge = "04", .url = "https://…", .title = "подпись" },
```
анимированные работают (вебп умеет анимацию):
`magick in.gif -coalesce +repage -define webp:lossless=true out.webp`

**свой бейдж на скачивание:** файл лежит в `assets/ynckz.webp` (тот же, что
`assets-src/badges/mine-ynckz.webp`), добавлен в `.static_assets` и отдаётся по
`/ynckz.webp`. В `.badges_mine` у ссылки есть `download="ynckz.webp"` —
клик скачивает файл, а не открывает картинку.

**цвета, отступы и говно:** цсс-переменные в начале `layouts/templates/base.shtml`

**фон страницы:** камуфляжные пятна + зерно, оба на `<canvas>`. камуфляж собран из
прежних 9ти шаблонов и 50ти расстановок ичето там еще но мне пох

## вес, скорость, победа

| файл | gzip |
|---|---|
| `index.html` (HTML + критический CSS и JS) | **10.5 KB** |
| `assets.css` (шрифты + картинки, base64) | 97.2 KB |

`index.html` влезает в первое окно TCP (≤14.6 KB), `assets.css` грузится без блокировки рендера.

## деплойчик

- `main` / `master` → боевой `ynckz.tech` (`deploy.yml` + `wrangler.jsonc`).
- `feat/allo-cyr` → тестовый `test.ynckz.tech` (`deploy-test.yml` +
  `wrangler.test.jsonc`, отдельный Worker `ynckz-tech-test`, чтобы не трогать боевые маршруты).

## Лицензия (наслоплено. не разбираюсь, пох мне)

Код и документация — **MIT** (см. `LICENSE`): бери вёрстку, скрипты, CSS и конфиги.
Контент, аватар, шрифты, эмодзи и чужие бейджи MIT **не** покрыты — права у их
владельцев, подробности и точные пути в `NOTICE.md`.

Шрифт Allo — SIL OFL 1.1, можно использовать и в коммерческих проектах
(кириллица — из PR #8 к исходникам Allo; в проекте шрифт растянут по
горизонтали на 25%, это разрешено OFL — растянутые исходники и скрипт лежат
в <https://github.com/ynckz/allo>, ветка `wide`). Benzin (им набран только текст
в `{}`) — Free for Personal Use, для коммерции нужна отдельная лицензия.
Apple-эмодзи — серая зона: для коммерческого проекта замени их на Noto Emoji
или Twemoji.

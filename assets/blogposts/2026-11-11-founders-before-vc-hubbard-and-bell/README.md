# Hubbard and Bell post assets

Images for `_posts/2026-11-11-founders-before-vc-hubbard-and-bell.md` (en) and `-zh.md` (zh).

```text
cover-en.svg / cover-en.jpg   1200x630 OpenGraph card, English title
cover-zh.svg / cover-zh.jpg   1200x630 OpenGraph card, Chinese title
```

The covers are hand-written SVG, rendered with `rsvg-convert` and converted to JPG with `sips`. The lease card on the right repeats only terms from Hubbard's May 1877 circular: $20 a year for two social telephones, $40 for business, $10 for each extra instrument, kept in order by the lessors.

```bash
rsvg-convert -w 1200 -h 630 cover-en.svg -o /tmp/cover-en.png
sips -s format jpeg -s formatOptions 80 /tmp/cover-en.png --out cover-en.jpg
```

## Section illustrations still to make

No image-generation key worked in this session, so the section images are a plan only.

| Section | File | Picture |
| --- | --- | --- |
| Telegraph side project | `01-telegraph.jpg` | A telegraph key and a wire with several message slips, one slip shaped like a sound wave |
| Rent, don't sell | `02-lease.jpg` | The 1877 lease card beside a wooden box telephone tagged "property of the lessors" |
| Hardware as a service | `03-territories.jpg` | A map of New England split into agent territories, with one city already wired |
| Stories that fail checking | `04-memo.jpg` | An unsigned typed memo with a red question mark next to a dated 1913 speech booklet |
| Lesson | `05-price-list.jpg` | A price list next to a modern subscription invoice, same layout, different century |

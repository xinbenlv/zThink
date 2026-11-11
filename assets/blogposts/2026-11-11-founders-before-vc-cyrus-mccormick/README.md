---
sitemap: false
---

# Cyrus McCormick post assets

Images for `_posts/2026-11-11-founders-before-vc-cyrus-mccormick.md` (en) and its `-zh` twin.

```text
cover-en.svg / cover-en.jpg   1200x630 cover + OpenGraph card, English title
cover-zh.svg / cover-zh.jpg   1200x630 cover + OpenGraph card, Chinese title
```

The covers are hand-written SVG timelines; every date and number on them is cited in the post
(1831 trial, 1834 patent, 1842 warranty, fewer than 100 sold by end of 1846, Chicago 1847,
500 built for 1848, about 1,600 built for 1850). No image model was used.

Regenerate a JPG after editing its SVG:

```bash
rsvg-convert -w 1200 -h 630 cover-en.svg -o cover-en.png && sips -s format jpeg -s formatOptions 82 cover-en.png --out cover-en.jpg && rm cover-en.png
```

## Section illustrations not yet made

| Section | Planned image |
| --- | --- |
| Move one: warranty and credit | A printed 1849-style order form: "$30 on delivery, balance Dec. 1", beside a sheaf of wheat |
| Move two: Chicago | Map of Illinois between Lake Michigan and the Mississippi, with the Chicago factory on the river |
| Move three: agents | An agent's ledger page: machines set up, cash collected, commission column |
| Move four: trials and medals | Two reapers in a green field at Tiptree, judges at the edge, a medal without a ribbon |

Use the palette from the covers (`#faf9f5`, `#141413`, `#d97757`, `#6a9bcc`, `#788c5d`) and keep
labels to what the post already states.

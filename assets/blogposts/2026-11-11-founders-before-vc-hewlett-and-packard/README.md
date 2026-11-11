# Images for the Hewlett and Packard post

These images belong to `_posts/2026-11-11-founders-before-vc-hewlett-and-packard.md` and its Chinese version (`-zh.md`).

| File | Use | Size |
| --- | --- | --- |
| `hp-cover-en.jpg`, `hp-cover-zh.jpg` | Cover, OpenGraph card and square thumbnail | 1200×630 |
| `hp-timeline-en.jpg`, `hp-timeline-zh.jpg` | Timeline in the garage section | 1200×675 |

The images are hand-written SVG, not AI-generated. Every number in them comes from the article's cited sources. The $200–$600 competitor range is HP's own figure, and the cover labels it that way.

To change an image, edit `src/make.py` and rebuild:

```bash
cd src && python3 make.py
for f in cover-en cover-zh timeline-en timeline-zh; do rsvg-convert -o $f.png $f.svg; sips -s format jpeg -s formatOptions 82 $f.png --out ../hp-$f.jpg; rm $f.png; done
```

# Boulton and Watt article images

Images for `_posts/2026-11-11-founders-before-vc-boulton-and-watt.md` (en) and `…-zh.md` (zh).
The images are hand-authored SVG, rendered to JPG. No image model was used.

```text
src/make_svgs.py                      writes the four SVG sources
src/*.svg                             SVG sources (generated, kept for edits)
boulton-watt-00-cover[-zh].jpg        1200x630 cover and OpenGraph card, title in the image
boulton-watt-01-one-third[-zh].jpg    1200x675 inline diagram: coal saved, split 1/3 and 2/3
```

## Rebuild the images

```bash
python3 -I src/make_svgs.py
for f in src/*.svg; do b=$(basename "$f" .svg); rsvg-convert "$f" -o "/tmp/$b.png"; sips -s format jpeg -s formatOptions 82 "/tmp/$b.png" --out "$b.jpg"; done
```

## Images not made yet

The illustration plan also had one image per remaining section. These images are optional.

| Section | Proposed image |
| --- | --- |
| The customers already owned engines | A drowned mine shaft with an old fire engine and a coal bill |
| A bad debt bought two thirds | A ledger page: Roebuck's debt crossed out, a patent share handed over |
| Parliament gave twenty-five years | A timeline bar: 1769 patent to 1783, extended by the 1775 Act to 1800 |
| Popular claims | Boswell's line beside Smiles's altered version, with the added words marked |

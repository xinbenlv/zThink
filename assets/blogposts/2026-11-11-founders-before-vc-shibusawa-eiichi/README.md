# Images for the Shibusawa Eiichi post

Images for `_posts/2026-11-11-founders-before-vc-shibusawa-eiichi.md` (en) and its `-zh.md` twin.
They are hand-written SVG, rendered to PNG. No image model was used.

```text
cover.png / cover-zh.png                       1200x630  OpenGraph card and cover_image
first-national-bank-capital.png / -zh.png      1200x675  inline chart in "The first offering fell short"
src/*.svg                                      sources for the four PNGs
```

The chart numbers come from the post's references: planned capital ¥3,000,000, Mitsui and Ono
¥2,000,000, final capital ¥2,440,800, 71 shareholders, 24,408 shares
(*Shibusawa Eiichi denki shiryō*, vol. 4, pp. 22–24 and 33). Change the post and the SVG together.

Regenerate a PNG after editing its SVG:

```bash
cd assets/blogposts/2026-11-11-founders-before-vc-shibusawa-eiichi/src
for f in *.svg; do rsvg-convert "$f" -o "../${f%.svg}.png"; done
```

The Chinese files use PingFang SC; the English files use Georgia and Avenir Next. Other machines may
substitute fonts, so check the output by eye.

Not made yet: section illustrations for Paris in 1867 and the 1880 Iwasaki dispute. A plan for them,
in the house palette (#faf9f5, #141413, #d97757, #6a9bcc): a ledger of French bond and railway-bond
certificates beside a Bourse ticket; a riverside restaurant at Mukōjima with two empty cushions and
a share register between them. Both should be text-free.

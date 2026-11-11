# Henry Ford (founders before VC) — image notes

Images for `_posts/2026-11-11-founders-before-vc-henry-ford.md` (en) and `-zh.md` (zh).

```text
cover-en.svg / cover-en.jpg   1200x630, English cover, also og_image
cover-zh.svg / cover-zh.jpg   1200x630, Chinese cover, also og_image
```

The covers are hand-written SVG, rendered with:

```bash
rsvg-convert -w 1200 -h 630 cover-en.svg -o /tmp/cover-en.png
sips -s format jpeg -s formatOptions 80 /tmp/cover-en.png --out cover-en.jpg
```

Every label on the cover comes from a sourced sentence in the article: the three
companies and their dates, the 1908/1913/1914 milestones, and the 1903 checkbook
balances ($14,500 on 26 June, $223.65 on 10 July, first car sold on 15 July).
The checkbook line has three points only; it does not show daily balances.

## Planned section images (not made)

No image-generation key was used for this post. If section images are added later,
keep them to sourced facts and the cover palette (#faf9f5, #141413, #d97757,
#6a9bcc, #788c5d):

| Section | Idea |
| --- | --- |
| First company | Detroit Automobile Company letterhead as a document still life, officers' titles visible, Ford listed as Mechanical Superintendent |
| Race and second company | Grosse Pointe oval track from above, two cars, a letter on Henry Ford Company paper in the foreground |
| Memoir rewrites | Two columns: memoir claim vs archive record, three rows |
| Stockholders | Twelve share certificates sized by share count (255 ... 10) |
| Model T price | Bar pairs of price vs production, 1909–10 to 1916–17, from Ford's chapter X table |
| Moving line | Magneto line: 20 min to 13 min 10 s to 5 min |
| Faster horse | A quotation card with a question mark and the 1999 / 2001 first-appearance dates |

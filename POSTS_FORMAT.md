---
sitemap: false
---

# Posts Format

This repository expects every post in [`_posts`](/Users/zzn/ws/znotes/zThink/_posts) to use YAML frontmatter.

## Required fields

- `title`: post title
- `excerpt`: short summary used in lists
- `date`: publish date
- `lang`: `en` or `zh`
- `categories`: YAML list
- `tags`: YAML list

## Optional author and editors

- `author`: who wrote the post. Omit it and the post is credited to **Zainan Victor Zhou**.
- `editors`: who edited the post. Omit it and the post is credited to **Zainan Victor Zhou** —
  including posts written by a guest author.

Both fields take a single name or a YAML list. Use an id or any name registered in
`src/data/authors.yaml` in the parent site (`zzn-im-2026`); an unregistered name still
renders, just without an avatar or profile link. `authors` / `editor` are accepted as
alternate spellings.

Known contributors:

| id | name | profile |
| --- | --- | --- |
| `zainan-victor-zhou` | Zainan Victor Zhou (aka Victor Zhou, Zainan Zhou) | https://zzn.im |
| `aileen-wright` | Aileen Wright — Art & History Writer, Namefi | https://namefi.io/r/en/authors/aileen-wright |

```yaml
# Written by a guest, edited by Zainan Victor Zhou (the default editor)
author: Aileen Wright

# Explicit editors
author: Aileen Wright
editors:
  - Zainan Victor Zhou
```

An editor who is also an author is not printed twice: a post Victor wrote and edited
himself shows a plain "By Zainan Victor Zhou" byline. Guest-authored posts also show
their byline in the blog index; posts by the site owner do not.

Attribution flows into the post byline, the `BlogPosting` JSON-LD (`author` / `editor`),
and the RSS feeds (`dc:creator` / `dc:contributor`).

## Optional cover image

Use `cover_image` when a post should provide a cropped square thumbnail for the home page loose list.

```yaml
cover_image:
  src: /assets/blogposts/example/cover.png
  x: 608
  y: 0
  size: 1536
```

Meaning:

- `src`: image path or URL
- `x`: left edge of the crop, in source-image pixels
- `y`: top edge of the crop, in source-image pixels
- `size`: square crop size in source-image pixels

Notes:

- The crop is always square.
- Prefer the largest useful square from an existing article image.
- For local assets, prefer paths under `/assets/...`.
- If `cover_image` is absent, the home page falls back to an identicon generated from the post title.
- If a post has a strong illustration image, set `og_image` (or `cover_image`) to that local asset so social cards use it.
- Posts with `og_image` / `cover_image` automatically get large-image social cards (`summary_large_image`) in the parent site.

## Example

```yaml
---
title: "Example Post"
excerpt: "A short summary."
date: 2026-03-20
lang: en
author: Aileen Wright
editors:
  - Zainan Victor Zhou
categories:
  - blog
tags:
  - example
cover_image:
  src: /assets/blogposts/example/cover.png
  x: 256
  y: 0
  size: 1024
---
```

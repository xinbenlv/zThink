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

## Example

```yaml
---
title: "Example Post"
excerpt: "A short summary."
date: 2026-03-20
lang: en
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

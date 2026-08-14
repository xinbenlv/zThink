# zThink Agents Guide

## Scope
This file is for blog-content rules only. Site-wide web app rules belong in `~/ws/zzn-im-2026/AGENTS.md`.

## Blog image rules
- Images used only by blog posts should live in this repo under `assets/blogposts/...`.
- For explanatory illustrations, prefer elegant analogy-based editorial images over literal tech charts when the goal is conceptual understanding.
- When a post has a strong illustration image, use it for social cards / OpenGraph / Twitter image.
- When a post has a strong illustration image, prefer a large-image social card (`summary_large_image`) over a plain summary card.

## Attribution
- Posts default to Zainan Victor Zhou as both author and editor. Only set `author` / `editors`
  when someone else is involved — e.g. `author: Aileen Wright`, whose default editor is still Victor.
- Field reference and the contributor list live in `POSTS_FORMAT.md`.

## Post frontmatter guidance
- Use `cover_image` for article artwork that should also drive social sharing and list thumbnails when appropriate.
- Prefer local asset paths under `/assets/blogposts/...` instead of parent-repo-only paths.
- Keep labels, diagrams, and terminology in article illustrations consistent with the article text; no gibberish, no stray UI chrome, no random extra words.

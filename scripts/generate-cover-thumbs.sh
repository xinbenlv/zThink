#!/bin/zsh

set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p assets/blogposts/thumbs

magick 'assets/blogposts/载友圈最佳书籍奖-300x193.png' \
  -crop 193x193+54+0 +repage \
  -resize 168x168 \
  'assets/blogposts/thumbs/zfriend-awards-book-168.webp'

magick 'assets/blogposts/2026-02-02-prettysafe-address-poison-prevention/image1-spot-the-fake.png' \
  -crop 1536x1536+608+0 +repage \
  -resize 168x168 \
  'assets/blogposts/thumbs/prettysafe-spot-the-fake-168.webp'

magick 'assets/blogposts/2026-03-11-改名即改命-20个域名故事/cover.png' \
  -crop 1536x1536+608+0 +repage \
  -resize 168x168 \
  'assets/blogposts/thumbs/domain-story-cover-168.webp'

ls -lh assets/blogposts/thumbs

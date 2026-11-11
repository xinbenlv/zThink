# "I have it now!" artwork

Images for [_posts/2026-11-11-edison-i-have-it-now.md](../../../_posts/2026-11-11-edison-i-have-it-now.md) and its Chinese twin [_posts/2026-11-11-edison-i-have-it-now-zh.md](../../../_posts/2026-11-11-edison-i-have-it-now-zh.md). The illustrations are conceptual artwork, not historical reconstructions; the newspaper clipping is a real 1878 scan.

| File | Use | Dimensions | Brief |
| --- | --- | --- | --- |
| `cover.jpg` | English post cover, social card, list thumbnail | 1200 × 630 | Exact English title beside a night laboratory bench with an unlit, empty glass bulb, a newspaper, and a gas lamp. |
| `cover-zh.jpg` | Chinese post cover, social card, list thumbnail | 1200 × 630 | Same scene with the Chinese subtitle. |
| `promise.jpg` | Section: the announcement | 1200 × 675 | Newspaper with a lamp sketched in its margin beside an empty bulb. |
| `money.jpg` | Section: investors | 1200 × 675 | Subscription ledger, blank share certificates, quill, top hat, telegraph wires outside. |
| `gas.jpg` | Section: gas shares | 1200 × 675 | Gas street lamp with blank share certificates blowing away and ticker tape around the post. |
| `wait.jpg` | Section: the delay | 1200 × 675 | Long bench of failed bulbs and torn calendar pages; one bulb glows at the far end. |
| `chicago-tribune-1878-10-17.jpg` | Section: gas shares (figure) | 500 × 580 | *Chicago Daily Tribune*, Oct. 17, 1878, p. 4, "The Electric Light." Library of Congress, Chronicling America, public domain. Cropped by the LOC IIIF image service (region `1628,2012,500,580`). |

## Generation and production

The six illustrations were generated on November 11, 2026 with Codex CLI 0.166.0-alpha.6 (`codex exec -m gpt-6.1-sol`) calling its built-in `image_gen` tool, one call per image, at 1536 × 1024. The Chinese cover used the English cover as a reference image. Shared prompt direction: hand-drawn ink with light watercolour wash, pale warm paper, terracotta / dusty blue / sage accents, full bleed, no digits, no logos, no legible text except the cover titles. Each image was inspected before use; cover lettering was checked character by character.

Post-processing was limited to `sips`: resize to 1200 px wide, centre-crop to the target height, JPEG quality 40. The original PNGs are not included. The screw-base bulbs in the artwork are a modern convention, not a period detail; the captions label every illustration as conceptual.

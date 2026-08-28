---
title: "Every Speech-to-Text Benchmark Has a Winner. It's Usually the Publisher."
excerpt: "Five roundups of the best speech-to-text APIs, five different winners, each published by the winner. What survives once you label who paid for each number."
date: 2026-08-27
lang: en
published: true
cover_image:
  src: /assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-00-cover.jpg
  x: 285
  y: 0
  size: 630
og_image: /assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-00-cover.jpg
categories:
  - blog
tags:
  - ai
  - speech-to-text
  - transcription
  - benchmarks
  - tooling
---

*A survey of the speech-to-text API market as of August 2026, for a developer who has to pick one. Every number below is attributed to whoever published it, because in this category that turns out to be the load-bearing fact. Prices were read off vendor pricing pages on 2026-08-27 and move fast.*

## The bug that started this

![Two teacups facing each other across a desk beside an open ledger in which every single line has been marked with the same identical stamp, and a stereo cable whose two strands merge into one](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-01-dual-mono.jpg)

An 87-minute two-person phone call, recorded through a meeting bot, came back as a clean transcript: 777 sentences, correct words, good punctuation. Every single sentence was attributed to one speaker.

The transcription was fine. The diarization, the part that decides who spoke when, had collapsed on the phone leg and merged both people into one. The usual escape hatch is to split the stereo channels and transcribe each separately, but that failed too: the file was dual-mono, with the left-minus-right difference sitting around −84 dB. Two identical channels wearing a stereo container.

Nothing in a headline word error rate predicts this. WER told me the words were right. What broke was everything downstream that depends on knowing who said them.

So I went looking for a benchmark that would tell me which API to use instead. That is where the real problem started.

## Five roundups, five winners

![Five identical brass trophies in a row, each with a hand reaching from behind it to pin a blank award rosette onto itself](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-02-five-winners.jpg)

Search for the best speech-to-text API in 2026 and you will get a well-written, confident, comparison-table-bearing article. It will almost always be published by one of the companies in the comparison.

Here is what I found, with the publisher named in every row:

| Article | Published by | Ranks first | Metric used |
|---|---|---|---|
| ["8 Best Speaker Diarization Solutions & APIs in 2026"](#ref-assemblyai-diarization-roundup) | AssemblyAI | AssemblyAI, 30.17 | cpWER, internal dataset |
| ["Speaker Diarization DER performance comparison"](#ref-pyannote-benchmark) | pyannoteAI | pyannoteAI Precision-2 | DER, DIHARD |
| ["Best Speech-to-Text APIs 2026"](#ref-deepgram-guide) | Deepgram | Deepgram, of ten listed | WER, mixed sourcing |
| ["Best speech-to-text APIs in 2026"](#ref-gladia-roundup) | Gladia | Gladia Solaria-3 | WER, mixed sourcing |
| ["State of Speaker Diarization"](#ref-picovoice-diarization) | Picovoice | Picovoice Falcon, on JER | JER and DER, VoxConverse |

This is not five independent measurements converging on a truth. It is five marketing assets.

The clearest illustration is what two of these say about the same company. On [AssemblyAI's chart](#ref-assemblyai-diarization-roundup), AssemblyAI places first. On [pyannoteAI's DIHARD Broadcast chart](#ref-pyannote-benchmark), AssemblyAI's Universal-3 places **last of twelve systems**, at 31.1% DER against pyannoteAI's own 9.4%. On DIHARD Clinical it is last again, at 48.1% against 13.3%.

Same two companies. Opposite conclusions. Both charts are real, and I opened both.

## Why the metric decides the ranking

![One waveform card measured on the left by a tape measure and stopwatch and on the right by word tiles sorted with tweezers, with three ranking ribbons pinned below each in a different order](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-03-der-vs-cpwer.jpg)

The two charts disagree partly because they measure different things, and the difference is the single most useful concept here.

**DER (diarization error rate)** is measured in *time*. Take the audio timeline, add up every second that was missed, falsely detected as speech, or attributed to the wrong speaker, and divide by total speech time. It scores the segmentation and says nothing about the words.

**cpWER (concatenated minimum-permutation word error rate)** is measured in *words*. Concatenate everything each speaker said, try every possible mapping of your speaker labels onto the true speakers, keep the best one, then compute word error rate against it. It charges you for transcription mistakes and speaker-attribution mistakes together.

AssemblyAI's own framing is the clearest published statement of the distinction, and worth quoting despite the source — or rather, because of it:

> DER is a fine academic metric, but [it measures diarization in isolation from the transcript](#ref-assemblyai-diarization-roundup). In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks.

That last sentence is doing a lot of work. It changes how the leaderboard looks, and it changes it in the direction of the company that wrote it.

To be fair to everyone: this is not necessarily bad faith. pyannoteAI sells diarization alone, with no transcript of its own, so DER is the only metric its product can be scored on. AssemblyAI sells transcription and diarization as one pipeline, so cpWER is the honest metric for what it ships. **The metric follows the product.** That is exactly why you cannot read any single vendor's chart as a ranking of the field.

Two details are worth noticing in AssemblyAI's table anyway. The dataset is undisclosed: the numbers ["come from our internal diarization benchmark, run across a mix of real-world datasets"](#ref-assemblyai-diarization-roundup), which is unreproducible by construction. And of the eight systems listed, cpWER is reported only for the four commercial competitors it beats; pyannote, NeMo, and Kaldi are marked "DER-reported only." The one system most likely to win on diarization quality is the one left without a comparable number.

Credit where it is due: the author states outright that he runs Voice AI at AssemblyAI. That is more disclosure than most of the genre offers.

## The reality check nobody markets

![Four glass jars holding progressively more tangled coloured thread, the last overflowing, with a magnifying glass showing the tangle is no clearer up close](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-04-hard-audio.jpg)

The most useful number I found in a vendor benchmark is one that makes the whole category look bad.

[pyannoteAI's streaming benchmark](#ref-pyannote-streaming) measures streaming diarization on DIHARD III. Its own results, which it is naturally presenting in the best light:

| System | DER, all languages | Missed speech |
|---|---|---|
| pyannote API | 19.8% | 7.7% |
| Speechmatics real-time v2 | 31.3% | 19.7% |
| Deepgram Nova 3 | 39.1% | 25.3% |
| AssemblyAI Universal Streaming v3 | 39.2% | 20.4% |

The winner's number is 19.8% DER. Roughly one speech-second in five is still wrong, from the system whose vendor built the chart to flatter it.

It gets worse on hard audio. Even pyannote, on its own benchmark, records [54.4% DER on restaurant audio](#ref-pyannote-streaming), 44.6% on meetings, and 44.9% on web video. Its competitors land between 51% and 76% across those three domains.

If you are building on noisy multi-party audio in 2026, no vendor has solved this. The honest planning assumption is that streaming diarization on hard audio is unreliable for every provider, and your product needs to degrade gracefully rather than depend on speaker labels being right.

## The closest thing to a neutral scoreboard

The [Hugging Face Open ASR Leaderboard](#ref-open-asr-leaderboard) is the only ranking here not published by a competitor. Models are submitted by pull request, evaluation scripts are public, and part of the average comes from private datasets held by Appen and DataoceanAI. That matters, because a test set nobody can download is a test set nobody can train on.

Standings as of its 25 August 2026 update, average WER across the default dataset mix, lower better:

| Rank | Model | Avg WER |
|---|---|---|
| 1 | modulate/vfast | 5.14 |
| 2 | reson8/resonant-1 | 5.17 |
| 3 | microsoft/azure-speech-06-2026 | 5.17 |
| 5 | elevenlabs/scribe_v2 | 5.24 |
| 7 | Qwen/Qwen3-ASR-1.7B | 5.31 |
| 8 | assemblyai/universal-3-5-pro | 5.40 |
| 11 | gladia/solaria-3 | 5.58 |
| 12 | nvidia/canary-qwen-2.5b | 5.63 |

Two things fall out of this.

First, the spread across the top twelve is half a percentage point. Whatever separates these products in practice, it is not headline English accuracy.

Second, compare it against Gladia's own post. [Gladia reports Solaria-3 first on Earnings22 at 6.4% WER](#ref-gladia-solaria3), ahead of AssemblyAI at 6.9% and ElevenLabs at 7.7%. On the leaderboard's Earnings22 column, ElevenLabs Scribe v2 scores 4.8, Gladia Solaria-3 scores 5.94, and AssemblyAI scores 6.05. The ordering inverts, and the absolute numbers do not match either. The two evaluation harnesses are not the same, which makes a vendor's "we rank #1 on Earnings22" a statement about its own harness.

One more data point on incentives. [Coval's 2026 provider guide](#ref-coval-guide) is the only other comparison I found written by a company that does not sell a speech-to-text model; it sells evaluation tooling. It is also the only one that declines to name a winner, reporting instead that the top providers sit "within 1-2 percentage points of each other." The correlation between having a horse in the race and finding a clear winner is close to perfect.

The leaderboard has one limitation you must not overlook: it covers **English and European languages only**. There is no Chinese, no Japanese, no Arabic, no Hindi. If your audio is not English or Western European, this scoreboard has nothing to say to you.

## What it actually costs

![A row of blank paper price tags hanging from a string, some with a second smaller tag tied beneath as an add-on and others with a wax seal already pressed into the tag itself](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-05-price-tags.jpg)

Prices normalized to US dollars per hour of audio, read from each vendor's pricing page on 2026-08-27. The diarization column is the one people get wrong.

| Provider / model | Batch $/hr | Realtime $/hr | Diarization |
|---|---|---|---|
| [AssemblyAI Universal-2](#ref-assemblyai-pricing) | $0.15 | — | **Add-on, +$0.02/hr** |
| [AssemblyAI Universal-3.5 Pro](#ref-assemblyai-pricing) | $0.21 | $0.45 | **Add-on, +$0.02/hr** |
| [Deepgram Nova-3 mono](#ref-deepgram-pricing) | $0.26 | $0.29 promo, $0.46 list | **Bundled on batch; add-on +$0.12/hr on streaming** |
| [ElevenLabs Scribe v2](#ref-elevenlabs-pricing) | $0.22 | $0.39 | Bundled (no add-on line) |
| [Gladia, Starter](#ref-gladia-pricing) | $0.61 | $0.75 | Bundled |
| [Gladia, Growth commit](#ref-gladia-pricing) | from $0.20 | from $0.25 | Bundled |
| [Google Cloud STT v2 standard](#ref-google-stt-pricing) | $0.96 | — | No separate line |
| [Google Cloud STT v2 dynamic batch](#ref-google-stt-pricing) | $0.18 | — | No separate line |
| [Gemini 3.5 Transcribe](#ref-gemini-pricing) | ~$0.30 | ~$0.54 (Live) | Bundled, verbatim mode only |
| [Qwen3-ASR, self-hosted](#ref-qwen3-asr) | your compute | your compute | None — pair with pyannote |

Notes that change the arithmetic:

- **Diarization bundling is inconsistent in both directions.** Deepgram includes it free on pre-recorded audio but charges $0.0020/min for it on streaming. AssemblyAI charges $0.02/hr in both modes. If you compare base rates only, you will misprice whichever one you pick.
- **Gladia's list price is the highest batch rate here at $0.61/hr**, roughly triple Deepgram's, and reaches $0.20/hr only on a committed-volume Growth plan. Its bundled diarization is [pyannoteAI's Precision-2](#ref-gladia-pyannote), which is a genuinely strong pairing, but "cheap" is not the right word for the pay-as-you-go tier.
- **Google Cloud's dynamic batch at $0.18/hr is the lowest hosted price in this table**, at the cost of processing "at a lower level of urgency."
- **Gemini's figure is an estimate.** It is billed by tokens, $0.003/min of audio in plus $0.002/min of text out at Google's assumed 175 text tokens per minute. Talkative audio costs more.
- AssemblyAI's free tier is unusually large: 185 hours pre-recorded and 333 hours streaming. Gladia grants €50 once, roughly 80 hours of batch.
- Deepgram's streaming discount is explicitly a "limited-time promotional rate," so the $0.46 list price is what you should model for next year.

## Google is three products, and people conflate them

- **Chirp 3**, in Cloud Speech-to-Text v2, covers [24 generally-available and 76 preview languages](#ref-chirp3-docs). Diarization works only in `BatchRecognize`, and word-level timestamps are listed as **not supported at all**. That single gap disqualifies it for subtitling and most editing tools.
- **Gemini 3.5 Transcribe** entered [public preview on 2026-08-26](#ref-gemini-blog), one day before I wrote this. Two models, `gemini-3.5-transcribe` and `gemini-3.5-transcribe-live`, 85+ locales, custom vocabulary of [up to 1,000 terms](#ref-gemini-transcribe-docs). Google claims 4.0% WER streaming and 2.6% non-streaming. Because the thing is a day old, there are no third-party numbers at all. Treat Google's as a vendor claim like every other in this post, and wait for the leaderboard.
- **General Gemini multimodal prompting**, which transcribes flexibly but returns whatever shape the prompt implies.

Gemini 3.5 Transcribe carries the sharpest gotcha I found anywhere in this research. Its "smart" mode is the one that removes filler words and cleans up self-corrections, and the documentation states plainly:

> Note: Smart transcription ("smart") is [incompatible with `timestamp_granularities` and `diarization_mode`](#ref-gemini-transcribe-docs). If you need word timestamps or speaker diarization, configure mode with `{"type": "verbatim", ...}`.

You can have clean readable text, or you can know who spoke when and at what timestamp. Not both, in the same call. For a meeting-notes product, which wants exactly both, that is a real architectural constraint and not a footnote.

Two more from the same page: diarization supports [up to 8 speakers, with 3 or more marked experimental](#ref-gemini-transcribe-docs), where the launch blog says three and the docs say eight; the docs are more specific. And "enabling word-level timestamps may degrade overall transcription accuracy."

## Chinese, and what the leaderboards will not tell you

![An open ledger whose ruled columns end at a torn page edge, beside a carved stone Chinese name seal and an open pot of red seal paste on an unmarked desk](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-06-missing-column.jpg)

The neutral scoreboard covers no Chinese. The vendor pages that do are the weakest evidence in this entire survey, and ElevenLabs' Mandarin page is the clearest example of why.

Its marketing copy claims Scribe achieves ["a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice"](#ref-elevenlabs-chinese). The benchmark table on the same page, a few hundred pixels below, lists **Scribe v1 at 7.2% WER on FLEURS**. The page contradicts itself by more than a factor of two. The same table credits Deepgram Nova 2 with "98.2% WER," a number that would mean near-total failure and much more likely means Nova 2 did not support the language at all. The table is also still labeled v1 while the shipping product is v2.

I am not citing that page for Chinese accuracy. I am citing it as a demonstration that a vendor benchmark table can go unchecked on a live pricing-adjacent page for months.

The more interesting option for Chinese is [**Qwen3-ASR**](#ref-qwen3-asr), Alibaba's Apache-2.0 release from 2026-01-29, in 0.6B and 1.7B sizes plus a forced aligner for timestamps. It covers 52 languages and dialects, including 22 Chinese dialects. Cantonese, Wu, and Minnan are among them, which essentially nothing else in this survey addresses.

Alibaba's own reported numbers, and they are Alibaba's: 2.71 on AISHELL-2 against Whisper large-v3's 5.06, and 3.98 on Cantonese Fleurs-yue against Whisper's 9.18. Roughly half the error rate of Whisper on Chinese, from a model you can run yourself.

Two independent signals make me take that seriously rather than filing it with the other vendor claims. On the Open ASR Leaderboard, Qwen3-ASR-1.7B sits **7th overall on English** at 5.31, ahead of AssemblyAI's flagship, and takes the best score in the field on the private conversational set at 13.9, a dataset it cannot have trained on. And it is the highest-ranked model on that board with a measurable throughput figure, meaning everything above it is an API you cannot self-host. Separately, [Brown University's research computing center](#ref-brown-ccv), which sells nothing here, recommends Qwen3-ASR for noisy environments and non-English dialects in its own transcription service.

Qwen3-ASR does no diarization. Pair it with pyannote.

## Code-switching: mostly an unverified claim

For audio that mixes languages inside a sentence, the marketing is ahead of the evidence.

Gladia advertises Solaria-1 as covering [100+ languages with native code-switching](#ref-gladia-roundup), including 42 it says are unavailable elsewhere. AssemblyAI describes Universal-3.5 Pro as working ["across 18 languages, with native code switching"](#ref-assemblyai-pricing). Gemini 3.5 Transcribe auto-detects across 85+ locales.

I could not find a single neutral benchmark that scores any of these on code-switched audio. The public research resource that exists is [CS-Dialogue](#ref-cs-dialogue), 104 hours of spontaneous Mandarin-English conversation from 200 speakers, released for academic use. Its authors note that pre-trained models like Whisper still have room to improve on it. There is also a [2025 systematic literature review](#ref-cs-survey) of code-switching in end-to-end ASR, useful for framing, though it reports no single headline improvement figure.

If you need English-Chinese-Spanish code-switching, no published number will decide this for you. Run CS-Dialogue, or a sample of your own audio, against two or three candidates. That is the whole recommendation.

## How I would actually choose

No single winner, because the honest answer differs by use case.

**Multi-speaker English where attribution matters.** Diarization quality is the binding constraint, not WER, and the specialist beats the bundles on it. Route transcription and diarization separately: a strong ASR API for words, pyannoteAI for speakers. If you want one vendor, Gladia bundles Precision-2 at $0.61/hr and saves you the integration. Budget for failure on overlapping speech regardless: 19.8% DER is the *best* published streaming number.

**Many speakers talking over each other.** [Brown's CCV documentation](#ref-brown-ccv) points at Microsoft Azure for exactly this case. It is the only non-vendor recommendation I found on the question, and Azure's June 2026 model sits third on the leaderboard.

**Chinese-heavy.** Qwen3-ASR-1.7B, self-hosted, plus pyannote. It is the only option in this survey with real Chinese dialect coverage, its English is competitive on a neutral board, and it costs compute rather than per-hour fees. Do not pick from the vendor Mandarin pages; they are the least reliable pages in the category.

**English + Chinese + Spanish code-switching.** Nothing published resolves this. Shortlist Gladia and Gemini 3.5 Transcribe on their claims, then benchmark on your own audio. Treat any vendor's code-switching claim as untested until you test it.

**Lowest cost.** Google Cloud STT v2 dynamic batch at $0.18/hr if latency is negotiable, or AssemblyAI Universal-2 at $0.15 + $0.02 diarization = $0.17/hr if it is not. Deepgram at $0.26/hr with diarization included is the better default before you optimize, and its free-diarization-on-batch policy makes small workloads simpler to reason about.

**Self-hosted or private.** Qwen3-ASR under Apache-2.0, with pyannote for diarization. This is also the only row in the cost table where your bill does not scale linearly with audio hours forever.

**And on the original bug:** if you control the recording, capture separate channels per participant and never ask a diarizer to solve a problem your capture pipeline could have avoided. Diarization is a recovery mechanism for audio you failed to segment at the source. It is currently a lossy one, for everybody.

## How to read any of these numbers

Three habits, learned the hard way over this research:

1. **Find the publisher before you read the chart.** In this category it predicts the winner with high reliability.
2. **Check which metric was chosen**, because DER and cpWER produce different rankings from the same audio, and vendors choose the one their product is built to win.
3. **Ask whether the dataset is nameable.** "Our internal benchmark across a mix of real-world datasets" is not a result you can check, reproduce, or hold anyone to.

Several of the leads I started from turned out to be wrong when I opened the sources: a cpWER table I had attributed to the wrong publisher, an "included" diarization that is a paid add-on, a price off by a factor of three, a leaderboard whose #1 had dropped to #12, and a "55% WER reduction" that appears nowhere in the paper it was credited to. Every one of those errors would have survived a confident rewrite. None survived opening the page.

## References and source passages

### Vendor-published benchmarks and roundups

- <span id="ref-assemblyai-diarization-roundup"></span>AssemblyAI (vendor in the comparison) — Original source: ["8 Best Speaker Diarization Solutions & APIs in 2026"](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=it%20measures%20diarization%20in%20isolation%20from%20the%20transcript), by Kelsey Foster, dated August 4, 2026. Supporting passages: "DER is a fine academic metric, but it measures diarization in isolation from the transcript. In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks." The comparison table lists AssemblyAI 30.17, ElevenLabs Scribe v2 35.26, Gladia 36.87, Deepgram Nova-3 EN 37.92, with PyAnnote, NVIDIA NeMo and Kaldi/SpeechBrain marked "DER-reported only." Dataset disclosure: ["The cpWER numbers come from our internal diarization benchmark, run across a mix of real-world datasets."](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=The%20cpWER%20numbers%20come%20from%20our%20internal%20diarization%20benchmark) Author disclosure: "I run Voice AI at AssemblyAI." — fetched [2026-08-27](https://web.archive.org/web/20260827231553/https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis)
- <span id="ref-pyannote-benchmark"></span>pyannoteAI (vendor in the comparison) — Original source: [Speaker Diarization DER performance comparison](https://www.pyannote.ai/benchmark). Reports DER only, across ten DIHARD domains, 259 recordings and roughly 67 hours. The per-domain results are published as chart images without text alternatives; values below were read from those images. DIHARD Broadcast (12 conversations, 3 or 4 speakers): pyannoteAI Precision-2 9.4%, pyannoteAI OSS Community-1 10.5%, NVIDIA 10.3%, AWS 16.5%, Speechmatics Enhanced 16.8%, Gladia Solaria 22.0%, Mistral Voxtral Mini 22.7%, Speechmatics Standard 24.5%, Soniox 25.2%, ElevenLabs Scribe-v2 26.4%, Deepgram Nova-3 26.9%, AssemblyAI Universal-3 31.1%. DIHARD Clinical (51 conversations, 2 or 3 speakers): Precision-2 13.3%, AssemblyAI Universal-3 48.1%. Methodology note: "We did not provide the number of speakers for any of them." — fetched [2026-08-27](https://web.archive.org/web/20260827231649/https://www.pyannote.ai/benchmark)
- <span id="ref-pyannote-streaming"></span>pyannoteAI (vendor in the comparison) — Original source: ["How accurate is streaming speaker diarization?"](https://www.pyannote.ai/blog/streaming-diarization-benchmark#:~:text=pyannote%20leaves%207.71%25%20of%20speech%20unattributed). Undated on the page. DER on DIHARD III across all languages: pyannote API 19.8% (false alarm 4.8, missed 7.7, confusion 7.3); Speechmatics real-time v2 31.3% (6.2 / 19.7 / 5.5); Deepgram Nova 3 39.1% (4.6 / 25.3 / 9.3); AssemblyAI Universal Streaming v3 39.2% (6.9 / 20.4 / 11.8). Supporting passage: "pyannote leaves 7.71% of speech unattributed, while the other systems miss between 19.70% and 25.26%, roughly 2.5 to 3 times more." Hard-domain figures for pyannote Live-1: restaurant 54.4%, webvideo 44.9%, meeting 44.6%. Methodology caveat: "measured on DIHARD without special scoring for overlapped speech." — fetched [2026-08-27](https://web.archive.org/web/20260827231613/https://www.pyannote.ai/blog/streaming-diarization-benchmark)
- <span id="ref-deepgram-guide"></span>Deepgram (vendor in the comparison) — Original source: ["Best Speech-to-Text APIs 2026"](https://deepgram.com/learn/best-speech-to-text-apis-2026). Ranks ten APIs with Deepgram first, followed by OpenAI Whisper, Microsoft Azure, Google Cloud, AssemblyAI, Amazon Transcribe, Rev AI, Speechmatics, IBM Watson and Kaldi. Cites Nova-3 at 5.26% WER and AssemblyAI Universal-2 at 10.7% WER. No publication date is stated on the page — fetched [2026-08-27](https://web.archive.org/web/20260827231713/https://deepgram.com/learn/best-speech-to-text-apis-2026)
- <span id="ref-gladia-solaria3"></span>Gladia (vendor in the comparison) — Original source: ["Introducing Solaria-3"](https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages), by Ani Ghazaryan, dated June 10, 2026. Claims Solaria-3 ranks first on Earnings22 at 6.4% WER, ahead of AssemblyAI 6.9%, ElevenLabs 7.7%, Speechmatics 7.8%, Mistral 7.9% and Deepgram 12.0%; 9.6% WER on Gladia's internal English production dataset, a 26% improvement over Solaria-1's 12.9%. Solaria-1 is described as covering "100+ languages and native code-switching across all of them, including 42 languages unavailable elsewhere." — fetched [2026-08-27](https://web.archive.org/web/20260827231734/https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages)
- <span id="ref-gladia-roundup"></span>Gladia (vendor in the comparison) — Original source: ["Best speech-to-text APIs in 2026"](https://www.gladia.io/blog/best-speech-to-text-apis#:~:text=including%2042%20languages%20unavailable%20elsewhere), by Ani Ghazaryan, "Published on Jul 9, 2026". The post opens: "Every speech-to-text vendor claims the lowest word error rate, the lowest lat[ency]…" and then ranks Gladia first. Supporting passages: "Solaria-1 is our breadth model, the most multilingual in the lineup, with 100+ languages and native code-switching across all of them, including 42 languages unavailable elsewhere"; Solaria-3 "ranks #1 across English and core European languages (EN, FR, DE, ES, IT), ahead of AssemblyAI, ElevenLabs, Deepgram, Mistral, and Speechmatics"; Solaria-1 "leads outright on speaker diarization accuracy: 3x more accurate diarization error rate (DER) than alternatives"; and "Gladia's audio intelligence features are bundled into base pricing, covering code switching, speaker diarization…" — fetched [2026-08-27](https://web.archive.org/web/20260827233025/https://www.gladia.io/blog/best-speech-to-text-apis)
- <span id="ref-picovoice-diarization"></span>Picovoice (vendor in the comparison; sells Falcon) — Original source: ["State of Speaker Diarization"](https://picovoice.ai/blog/state-of-speaker-diarization/), published December 18, 2023 and updated March 11, 2026. On VoxConverse: pyannote 9.0% DER against Falcon 10.3%; Falcon 19.9% JER against pyannote 27.4%. Picovoice leads on the metric it selected for emphasis — fetched [2026-08-27](https://web.archive.org/web/20260827231752/https://picovoice.ai/blog/state-of-speaker-diarization/)
- <span id="ref-elevenlabs-chinese"></span>ElevenLabs (vendor) — Original source: [Mandarin Chinese speech-to-text page](https://elevenlabs.io/speech-to-text/chinese#:~:text=a%20word%20error%20rate%20of%20just%203.1%25%20on%20the%20FLEURS%20benchmark%20and%205.5%25%20on%20Common%20Voice). The prose claims "a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice." The "Mandarin Chinese Transcription Benchmark" table on the same page lists Scribe v1 at 7.2% WER on FLEURS, Gemini Flash 2 at 17.6%, Whisper Large v3 at 23.6%, and Deepgram Nova 2 at 98.2%. Cited here as evidence of an internally inconsistent vendor benchmark, not as a Chinese accuracy figure — fetched 2026-08-27; nearest archive snapshot [2026-07-25](https://web.archive.org/web/20260725123551/https://elevenlabs.io/speech-to-text/chinese)

### Independent and non-vendor sources

- <span id="ref-open-asr-leaderboard"></span>Hugging Face — Original source: [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard), last updated 25 August 2026. Ranking read from the live Gradio app: modulate/vfast 5.14, reson8/resonant-1 5.17, microsoft/azure-speech-06-2026 5.17, reson8/resonant-1-flash 5.20, elevenlabs/scribe_v2 5.24, zoom/scribe_v1 5.24, Qwen/Qwen3-ASR-1.7B-hf 5.31, assemblyai/universal-3-5-pro 5.40, HojoAI/Hojo-ASR-V1 5.47, AutoArk-AI/ARK-ASR-3B 5.58, gladia/solaria-3 5.58, nvidia/canary-qwen-2.5b 5.63. Earnings22-Cleaned-AA-chunked column: elevenlabs/scribe_v2 4.80, gladia/solaria-3 5.94, assemblyai/universal-3-5-pro 6.05. Qwen3-ASR-1.7B holds the best Private (conversational) score at 13.9. Scope statement: "evaluates open-source and proprietary speech recognition models on English and multiple European languages." Private datasets are credited to Appen Inc. and DataoceanAI. Every model ranked above Qwen3-ASR-1.7B reports "NA" throughput, consistent with API-only access — fetched [2026-08-27](https://web.archive.org/web/20260827231830/https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- <span id="ref-coval-guide"></span>Coval — Original source: ["Best Speech-to-Text Providers in 2026"](https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/), dated June 4, 2026. Coval sells voice-agent simulation and evaluation tooling, not a speech-to-text model, so it does not compete in its own comparison — though it does benefit from readers concluding they should evaluate more. Notably, it declines to name a single winner, reporting that top providers cluster "within 1-2 percentage points of each other" — fetched [2026-08-27](https://web.archive.org/web/20260827231856/https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/)
- <span id="ref-brown-ccv"></span>Brown University Center for Computation and Visualization — Original source: [Comparing Speech-to-text Models](https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models#:~:text=please%20choose%20the%20Microsoft%20Azure%20model%20for%20better%20performance). A university research-computing service that sells no speech-to-text product. Supporting passage: "if the accuracy of speaker diarization is a priority and/or the audio includes many speakers talking over each other, please choose the Microsoft Azure model for better performance." The page also recommends Qwen3-ASR for noisy environments and non-English dialects. Note one internal inconsistency: Azure is recommended in the text but does not appear in the page's own model table — fetched [2026-08-27](https://web.archive.org/web/20260827231924/https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models)

### Pricing pages

- <span id="ref-assemblyai-pricing"></span>AssemblyAI — Original source: [Pricing](https://www.assemblyai.com/pricing#:~:text=works%20across%2018%20languages%2C%20with%20native%20code%20switching). Pre-recorded: Universal-3.5 Pro $0.21/hr, Universal-2 $0.15/hr. Streaming: Universal-3.5 Pro Realtime $0.45/hr, Universal-Streaming $0.15/hr. Under the "Add-On Features" tab, Speaker Diarization is priced at $0.02/hr on both Universal-3.5 Pro and Universal-2; keyterms prompting is $0.05/hr on Universal-3.5 Pro and included on Universal-2. Universal-3.5 Pro "works across 18 languages, with native code switching"; Universal-2 "supports 99 languages." Free tier: 185 hours pre-recorded and 333 hours streaming — fetched [2026-08-27](https://web.archive.org/web/20260827231946/https://www.assemblyai.com/pricing)
- <span id="ref-deepgram-pricing"></span>Deepgram — Original source: [Pricing](https://deepgram.com/pricing). Pre-Recorded tab: Nova-3 Monolingual $0.0043/min ($0.258/hr), Nova-3 Multilingual $0.0052/min, and Speaker Diarization listed as "Included." Streaming tab: Nova-3 Monolingual $0.0048/min promotional against a $0.0077/min regular price, with Speaker Diarization at $0.0020/min ($0.12/hr). The page states "Limited-time promotional rates on streaming." — fetched [2026-08-27](https://web.archive.org/web/20260827232006/https://deepgram.com/pricing)
- <span id="ref-gladia-pricing"></span>Gladia — Original source: [Pricing](https://www.gladia.io/pricing#:~:text=Async%20at%20%240.61%2Fhr). Starter: "Async at $0.61/hr", "Real-time at $0.75/hr", with "50€ in free credits". Growth: "Async as low as $0.20/hr", "Real-time as low as $0.25/hr". Speaker diarization, 100+ languages and word-level timestamps are listed as included on every tier. The FAQ describes the free credits as "a one-time grant with no monthly reset. That's roughly 80+ hours of pre-recorded transcription" — fetched [2026-08-27](https://web.archive.org/web/20260827232027/https://www.gladia.io/pricing)
- <span id="ref-elevenlabs-pricing"></span>ElevenLabs — Original source: [API pricing](https://elevenlabs.io/pricing/api). Scribe v2 $0.22/hr, Scribe v2 Realtime $0.39/hr. Add-ons listed are entity detection at $0.070/hr and keyterm prompting at $0.050/hr; no separate speaker-diarization charge appears — fetched [2026-08-27](https://web.archive.org/web/20260827232044/https://elevenlabs.io/pricing/api)
- <span id="ref-google-stt-pricing"></span>Google Cloud — Original source: [Speech-to-Text pricing](https://cloud.google.com/speech-to-text/pricing#:~:text=%240.016%20%2F%201%20minute). Speech-to-Text V2 standard recognition: $0.016/min for the first 500,000 minutes per month ($0.96/hr), falling to $0.010, $0.008 and $0.004/min at higher volume tiers. Standard dynamic batch recognition: $0.003/min ($0.18/hr), described as processing "audio at a lower level of urgency." Chirp is listed among the "Standard" models. No separate diarization charge appears on the page — fetched 2026-08-27; Archive.org's save endpoint declined this URL, nearest existing snapshot [2026-08-25](https://web.archive.org/web/20260825164556/https://cloud.google.com/speech-to-text/pricing)
- <span id="ref-gemini-pricing"></span>Google — Original source: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing). `gemini-3.5-transcribe`: $0.003/min audio input and $0.002/min text output, quoted as roughly $0.005/min blended. `gemini-3.5-transcribe-live`: $0.005/min audio input and $0.004/min text output, roughly $0.009/min blended. Token accounting is 25 audio tokens per second in and 175 text tokens per minute out, so output cost varies with speech density. A free tier is available for both — fetched [2026-08-27](https://web.archive.org/web/20260827232123/https://ai.google.dev/gemini-api/docs/pricing)

### Google product documentation

- <span id="ref-gemini-blog"></span>Google — Original source: [Gemini 3.5 Transcribe announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/), posted August 26, 2026. Announces `gemini-3.5-transcribe` and `gemini-3.5-transcribe-live` in public preview, "over 85 languages," a claimed average WER of 4.0% streaming and 2.6% non-streaming, 5.50%/5.04% on FLEURS, and a 70% latency improvement over Chirp 3. The post describes multi-speaker identification for up to three speakers with 3+ experimental, which is narrower than the API documentation's figure — fetched 2026-08-27; archive snapshot [2026-08-27](https://web.archive.org/web/20260827151836/https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)
- <span id="ref-gemini-transcribe-docs"></span>Google — Original source: [Gemini API audio transcription documentation](https://ai.google.dev/gemini-api/docs/transcribe#:~:text=is%20incompatible%20with%20timestamp_granularities%20and%20diarization_mode). Supporting passages, verbatim: "Note: Smart transcription (\"smart\") is incompatible with timestamp_granularities and diarization_mode. If you need word timestamps or speaker diarization, configure mode with {\"type\": \"verbatim\", ...}."; "Up to 8 speakers are supported (attribution for 3 or more speakers is experimental)."; "Supply up to 1,000 terms in the custom_vocabulary array (best results are typically achieved with up to 100 terms)"; "Note: Enabling word-level timestamps may degrade overall transcription accuracy." — fetched [2026-08-27](https://web.archive.org/web/20260827232104/https://ai.google.dev/gemini-api/docs/transcribe)
- <span id="ref-chirp3-docs"></span>Google — Original source: [Chirp 3 model documentation](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3). Lists 24 generally-available languages and 76 in preview. Diarization is marked "Available only in Speech.BatchRecognize"; utterance-level timestamps are available only in `StreamingRecognize`; word-level timestamps are listed as unsupported — fetched [2026-08-27](https://web.archive.org/web/20260827232206/https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)

### Open models and research

- <span id="ref-qwen3-asr"></span>Alibaba / Qwen team (vendor for its own model) — Original source: [Qwen3-ASR repository](https://github.com/QwenLM/Qwen3-ASR). Apache-2.0. Released January 29, 2026 in 0.6B and 1.7B sizes, with Qwen3-ForcedAligner-0.6B for timestamps; native Transformers support added June 26, 2026. Covers 52 languages and dialects, including 22 Chinese dialects (Mandarin, Cantonese, Wu, Minnan). Qwen's own reported results for Qwen3-ASR-1.7B against Whisper large-v3: AISHELL-2 2.71 vs 5.06; Fleurs-yue 3.98 vs 9.18; LibriSpeech clean 1.63 vs 1.51. Against GPT-4o-Transcribe on M4Singer: 5.98 vs 16.77. No speaker diarization is documented — fetched 2026-08-27; Archive.org's save endpoint declined this URL, nearest existing snapshot [2026-07-29](https://web.archive.org/web/20260729105533/https://github.com/QwenLM/Qwen3-ASR)
- <span id="ref-gladia-pyannote"></span>Gladia — Original source: ["Gladia x pyannoteAI: Speaker diarization and the future of voice AI"](https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai), dated March 11, 2025. Supporting passage: "Our speaker diarization pipeline is now powered by pyannoteAI's Precision-2, their most accurate model to date." The post does not address whether diarization is bundled or metered; the bundling in this article's cost table comes from Gladia's pricing page — fetched 2026-08-27; Archive.org's save endpoint declined this URL, nearest existing snapshot [2025-06-17](https://web.archive.org/web/20250617234345/https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai)
- <span id="ref-cs-dialogue"></span>Jiaming Zhou et al. — Original source: ["CS-Dialogue: A 104-Hour Dataset of Spontaneous Mandarin-English Code-Switching Dialogues for Speech Recognition"](https://arxiv.org/abs/2502.18913), arXiv, submitted February 26, 2025 and revised March 12, 2025. 104 hours of spontaneous conversation from 200 speakers, with full-length dialogue recordings and complete transcriptions, to be made freely available for academic purposes. The abstract notes that "existing pre-trained models such as Whisper still have the space to improve" — fetched [2026-08-27](https://web.archive.org/web/20260827232224/https://arxiv.org/abs/2502.18913)
- <span id="ref-cs-survey"></span>Maha Tufail Agro, Atharva Kulkarni, Karima Kadaoui, Zeerak Talat and Hanan Aldarmaki — Original source: ["Code-Switching in End-to-End Automatic Speech Recognition: A Systematic Literature Review"](https://arxiv.org/abs/2507.07741), arXiv, submitted July 10, 2025. A systematic review covering languages, datasets, metrics, model choices and open challenges. Cited here for framing only: the abstract reports no single headline WER-reduction figure — fetched [2026-08-27](https://web.archive.org/web/20260827232243/https://arxiv.org/abs/2507.07741)

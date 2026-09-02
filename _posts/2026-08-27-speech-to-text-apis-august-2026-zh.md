---
title: "2026 年的语音转文字：托管 API 与自部署开源模型对比"
excerpt: "对比托管 API 和可以自己部署的开源模型，涵盖准确率、每音频小时价格、说话人分离能力，以及自托管的实际成本。"
date: 2026-08-31
lang: zh
published: true
cover_image:
  src: /assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-00-cover-zh.jpg
  x: 285
  y: 0
  size: 630
og_image: /assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-00-cover-zh.jpg
translationKey: speech-to-text-apis-2026-08-27
categories:
  - blog
tags:
  - ai
  - speech-to-text
  - transcription
  - benchmarks
  - tooling
---

*在 2026 年 8 月这个时间点，我调研了语音转文字的各种可用方案，包括托管 API 和可以在自己机器上运行的开源模型。本文对比这两条路线的准确率、价格、说话人分离能力，以及自托管的实际成本。文中价格于 2026-08-27 当天从各厂商定价页读取，榜单数据取自 8 月 28 日那次更新，两者的变动都很快。每一个数字我都注明了发布方，原因见文章末尾。*

## 起因：一个转写 bug

![两只面对面的茶杯放在桌上，旁边摊开一本账簿，每一行都盖着同一个印章；一根立体声线的两股并成了一股](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-01-dual-mono.jpg)

事情起于一份 87 分钟的双人电话录音，由会议机器人自动录制。转写稿一共 777 句，用词准确，标点也没有问题。但是我很快发现，这 777 句全部被标记成了同一个人说的。

问题出在说话人分离（diarization）。这一层负责判断谁在什么时候说话，在电话录音上完全失效，把两个人合并成了一个。按照通常的补救办法，这时候可以把立体声的左右声道拆开分别转写，但是这条路同样走不通：这份文件虽然是立体声格式，左右声道相减以后只剩下大约 −84 dB，说明两个声道的内容完全相同。

这类故障有一个麻烦之处，就是词错误率（WER）完全反映不出来。识别出的文字确实是对的，受影响的是后续所有依赖说话人归属的环节。

于是我开始寻找替代方案，最后把这个领域的主要选项都比了一遍，包括托管 API 和可以自己部署的开源模型。调研下来，2026 年这两条路线的差距已经很小，比我原先预想的要小得多。

## 第一个决定：托管，还是自己部署

在比较具体产品之前，需要先确定自己站在哪一边，因为这个决定会直接排除掉大部分选项。

**适合用托管 API 的情况：**用量小或者波动大；希望直接获得说话人分离和流式转写，不想自己实现；需要覆盖长尾语种；不想自己维护 GPU。

**适合自己部署模型的情况：**音频不能离开自有基础设施；用量大且稳定；希望成本固定，而不是随用量浮动；希望锁定模型版本，避免哪天被厂商下线。

这两条路线的成本差距很大，而且随负载剧烈变化，后文会详细计算。这里先给出结论：在 GPU 满负载的前提下，自托管的每音频小时成本大约是最便宜的托管 API 的三十分之一；一旦负载不足，自托管反而贵得多。

## 中立榜单：Open ASR Leaderboard

[Hugging Face Open ASR Leaderboard](#ref-open-asr-leaderboard) 是本文涉及的排名里，唯一一份不由参赛厂商自己发布的。模型通过 pull request 提交，评测脚本公开，平均分中有一部分来自 Appen、DataoceanAI 和 Voice Arena 持有的私有数据集。这一点很重要，因为谁都下载不到的测试集，也就没有人能拿去训练。

该榜单最近一次更新是 2026 年 8 月 28 日，下面是默认数据集组合上的平均 WER，数值越低越好：

| 排名 | 模型 | 平均 WER | 许可证 |
|---|---|---|---|
| 1 | reson8/resonant-1 | 4.77 | 专有 |
| 2 | modulate/vfast | 4.78 | 专有 |
| 4 | elevenlabs/scribe_v2 | 4.84 | 专有 |
| 6 | microsoft/azure-speech-06-2026 | 4.91 | 专有 |
| **7** | **Qwen/Qwen3-ASR-1.7B** | **4.95** | **apache-2.0** |
| 8 | assemblyai/universal-3-5-pro | 5.02 | 专有 |
| 11 | gladia/solaria-3 | 5.22 | 专有 |
| 12 | nvidia/canary-qwen-2.5b | 5.23 | cc-by-4.0 |

这张表有两点值得注意。第一，前十二名之间的差距不到半个百分点，因此这些产品在实际使用中的区别，无论是什么，都不会是英文的整体识别准确率。第二，排名最高的开源模型位列第七，排在 AssemblyAI 的旗舰产品之前。也就是说，一个可以直接下载的 2 GB 文件，在一份双方都无法操控的榜单上赢过了商业 API。

另一处出人意料的是 Whisper 的位置。前 40 名里，Whisper 家族只剩下 [`distil-whisper/distil-large-v3.5` 一个条目，排在第 37 位](#ref-open-asr-leaderboard)，WER 为 6.2。如果你上一次认真了解这个领域还是在 2024 年，至今仍然习惯性地首选 Whisper，那么这个习惯现在已经要付出代价了。

这份榜单还有一个必须说明的局限：它只覆盖英语和欧洲语言，不包含中文、日语、阿拉伯语和印地语。

## 可以自己部署的开源模型

榜单上的 40 个模型里有 30 个采用开放许可证。下面列出其中值得关注的几个，并附上吞吐和体积，因为真正决定能否部署的正是这两栏：

| 模型 | 平均 WER | RTFx | 许可证 | 参数量 | 语言数 |
|---|---|---|---|---|---|
| [Qwen3-ASR-1.7B](#ref-qwen3-asr) | 4.95 | 820 | apache-2.0 | 2.04B | 52 |
| AutoArk ARK-ASR-3B | 5.18 | 482 | apache-2.0 | 3.75B | 19 |
| NVIDIA canary-qwen-2.5b | 5.23 | 867 | cc-by-4.0 | 2.5B | 1 |
| [MOSS-Transcribe-Diarize](#ref-moss-diarize) | 5.52 | 381 | apache-2.0 | 0.91B | 50+ |
| NVIDIA parakeet-tdt-0.6b-v2 | 5.48 | 6025 | cc-by-4.0 | 0.6B | 1 |
| NVIDIA parakeet-tdt-0.6b-v3 | 5.66 | 6076 | cc-by-4.0 | 0.6B | 26 |
| IBM granite-speech-4.1-2b | 5.43 | 546 | apache-2.0 | 2B | 6 |
| Mistral Voxtral-Small-24B | 5.79 | 101 | apache-2.0 | 24B | 8 |
| Microsoft Phi-4-multimodal | 5.72 | 163 | mit | 6B | 8 |
| IBM granite-5.0-470m-turboctc | 5.78 | 12946 | apache-2.0 | 0.47B | 1 |

RTFx 指每一秒实际耗时能够转写多少秒音频，也就是单卡吞吐。这一栏的跨度极大：parakeet 比 Qwen3-ASR 快大约七倍，代价是 0.7 个 WER 点；granite-470m 还要更快。

**在选定某个模型之前，务必先看许可证那一栏。**有几个系列会同时发布一个快速版和一个大同小异的非商用版本，两者的名字只差几个字符：

- `granite-speech-5.0-470m-turboctc` 是 apache-2.0；`granite-speech-5.0-470m-turboctc-nc` 是 **cc-by-nc-sa-4.0**。
- `canary-1b-flash` 是 cc-by-4.0；不带 flash 的 `canary-1b` 是 **cc-by-nc-4.0**。
- `Zipformer-cr-ctc-transducer-XL-290M` 是 **cc-by-nc-4.0**。

如果你的产品是商用的，榜单上看起来最快的几个选项里有三个不能用，而 WER 那一栏对此只字不提。

本地模型普遍还有一件事做不到，就是说话人分离。只有一个例外，后文会提到。

## 托管 API 一侧

| 厂商 / 模型 | 语言 | 说话人分离 | 流式 |
|---|---|---|---|
| [AssemblyAI Universal-3.5 Pro](#ref-assemblyai-pricing) | 18，原生语言混说 | 需另购 | 有 |
| [AssemblyAI Universal-2](#ref-assemblyai-pricing) | 99 | 需另购 | — |
| [Deepgram Nova-3](#ref-deepgram-pricing) | 45+ | 离线免费，流式收费 | 有 |
| [ElevenLabs Scribe v2](#ref-elevenlabs-pricing) | 90+ | 已包含 | 有（Realtime） |
| [Gladia Solaria-1 / -3](#ref-gladia-roundup) | 100+ / 5 | [已包含，用 pyannoteAI Precision-2](#ref-gladia-pyannote) | 有 |
| [Google Chirp 3](#ref-chirp3-docs) | 29 正式 + 82 预览 | 仅 `BatchRecognize` | 有 |
| [Gemini 3.5 Transcribe](#ref-gemini-transcribe-docs) | 85+ | 最多 8 人 | 有（Live） |

谷歌这边实际上是三个产品，很容易被混为一谈。[Chirp 3](#ref-chirp3-docs) 覆盖 111 种语言，但只有 `BatchRecognize` 支持说话人分离。词级时间戳的文档则自相矛盾：它出现在一张标题为“Chirp 3 doesn't support the following features”的表格里，而[同一行的说明](#ref-chirp3-docs)却写着可以在 `Speech.Recognize` 和 `Speech.BatchRecognize` 中开启，只是会带来“some transcription degradation”。[Gemini 3.5 Transcribe](#ref-gemini-blog) 于 2026-08-26 进入公开预览，就在我动笔的前一天，因此目前还没有任何第三方数据。除此之外，直接用 Gemini 的多模态提示词也可以转写，只是输出结构完全取决于提示词怎么写。

Gemini 3.5 Transcribe 的 `smart` 模式会自动去掉口头禅、整理说话人的自我更正。但是开启它是有代价的，文档里说得很直白：

> Note: Smart transcription ("smart") is [incompatible with `timestamp_granularities` and `diarization_mode`](#ref-gemini-transcribe-docs). If you need word timestamps or speaker diarization, configure mode with `{"type": "verbatim", ...}`.

也就是说，清理后的文字和说话人标定不可兼得，同一次调用只能取其一。而会议纪要类产品偏偏两样都要。

## 成本：两条路线各要花多少钱

![一排挂在绳子上的空白纸质价签，有些下面另挂了一个小签，有些则已经压了火漆封印，用来表示“另收费”与“已包含”的区别](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-05-price-tags.jpg)

先看托管一侧。下表单位为每音频小时的美元，数据于 2026-08-27 当天从各厂商定价页读取：

| 厂商 / 模型 | 离线 $/小时 | 实时 $/小时 | 说话人分离 |
|---|---|---|---|
| [AssemblyAI Universal-2](#ref-assemblyai-pricing) | $0.15 | — | **另收 +$0.02/小时** |
| [AssemblyAI Universal-3.5 Pro](#ref-assemblyai-pricing) | $0.21 | $0.45 | **另收 +$0.02/小时** |
| [Deepgram Nova-3 单语](#ref-deepgram-pricing) | $0.26 | $0.29 促销 / $0.46 标价 | **离线免费；流式 +$0.12/小时** |
| [ElevenLabs Scribe v2](#ref-elevenlabs-pricing) | $0.22 | $0.39 | 已包含（无单独计费项） |
| [Gladia Starter](#ref-gladia-pricing) | $0.61 | $0.75 | 已包含 |
| [Gladia Growth 承诺量](#ref-gladia-pricing) | 低至 $0.20 | 低至 $0.25 | 已包含 |
| [Google Cloud STT v2 标准](#ref-google-stt-pricing) | $0.96 | — | 无单独计费项 |
| [Google Cloud STT v2 动态批处理](#ref-google-stt-pricing) | $0.18 | — | 无单独计费项 |
| [Gemini 3.5 Transcribe](#ref-gemini-pricing) | 约 $0.30 | 约 $0.54（Live） | 已包含，仅 verbatim 模式 |

说话人分离是否包含在基础价里，各家的做法并不一致，算错账通常就错在这一点上。Deepgram 的离线分离免费，流式则按 $0.0020/分钟 计费；AssemblyAI 两种模式都收 $0.02/小时。Gladia 的 $0.61/小时 是表中最贵的离线价，大约是 Deepgram 的三倍，只有承诺用量的方案才能降到 $0.20。Google Cloud 的动态批处理 $0.18/小时 是表中最低的托管价，代价是按照“较低的紧急程度”排队处理。Gemini 那一格是谷歌自己的估算，因为它按 token 计费，页面把它折算成了[“an effective blended rate of ~$0.005 per min for Transcribe”](#ref-gemini-pricing)。

自托管也可以按同一个口径计算，因为榜单同时公布了吞吐和测试硬件。前面那些 RTFx 数字来自[单张 NVIDIA H200 的运行结果，而 Hugging Face Jobs 对这张卡的标价是 $5.00/小时](#ref-asr-leaderboard-hardware)。既然 RTFx 表示每一实际小时能处理多少音频小时，那么每音频小时的成本就是 $5.00 ÷ RTFx：

| 模型 | RTFx | 租用 H200 时的 $/音频小时 |
|---|---|---|
| IBM granite-5.0-470m-turboctc | 12946 | $0.0004 |
| NVIDIA parakeet-tdt-0.6b-v3 | 6076 | $0.0008 |
| NVIDIA canary-qwen-2.5b | 867 | $0.006 |
| Qwen3-ASR-1.7B | 820 | $0.006 |
| MOSS-Transcribe-Diarize | 381 | $0.013 |
| Mistral Voxtral-Small-24B | 101 | $0.049 |

与最便宜的托管价 $0.18/小时 相比，自托管 Qwen3-ASR 大约便宜三十倍，parakeet 便宜两百倍以上。榜单维护者公布的实际运行开销也在同一个量级：[parakeet-tdt-0.6b-v3 跑完一整轮英文短音频评测花费 $2.92，Qwen3-ASR-1.7B 花费 $5.58](#ref-asr-leaderboard-hardware)。

但是这些数字有一个前提，就是 GPU 一刻不闲，而利用率恰恰是整件事的决定因素。按 $5.00/小时 包一张 H200 一个月要花 $3,600，无论你喂给它 3000 小时音频还是 3 小时，这个数字都不变。用 Qwen3-ASR 对比谷歌 $0.18/小时 的批处理档位，盈亏平衡点大约落在每月两万音频小时。低于这个用量，托管更便宜，而且还省掉了运维。如果把工程师的时间也算进去，这条线还要再往上抬。

## 真正的瓶颈在说话人分离

![左边用卷尺和秒表丈量一张波形卡片，右边把同样的内容拆成词块用镊子分拣，两边下方各别着三条排序不同的绶带](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-03-der-vs-cpwer.jpg)

前面讨论的都是识别准确率，这个问题基本已经解决了；真正悬而未决的是说话人归属。

常被引用的指标有两个，两者给出的排名往往并不一致，所以至少要清楚眼前这份用的是哪一个。**DER**（分离错误率）按时间计算，把漏检、误检成语音、以及归错人的秒数加起来，除以总语音时长。它只衡量切分，完全不管词。**cpWER**（拼接后取最优置换的词错误率）按词计算，把每个说话人说的内容各自拼起来，穷举输出标签到真实说话人的所有映射，取其中最好的一种，再计算 WER。转写错误和归属错误都算在这一个数字里。

关于这个区别，AssemblyAI 讲得比我读到的其他任何人都清楚：

> DER is a fine academic metric, but [it measures diarization in isolation from the transcript](#ref-assemblyai-diarization-roundup). In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks.

这个说法本身是对的，同时对它自己也很有利，因为在它发布的那张 cpWER 表上，AssemblyAI 排第一。指标的选择往往跟着产品走：pyannoteAI 只卖分离、不产出转写稿，所以 DER 本来就是它的产品唯一能被打分的指标。

更有参考价值的，是各家究竟差到什么程度。在 [pyannoteAI 自己发布的流式评测](#ref-pyannote-streaming)中，图表由最终的冠军亲手绘制，而冠军的成绩是 19.8% DER，也就是大约每五秒语音里仍有一秒归错了人。在难处理的音频上还要更差：[餐厅场景 54.4% DER](#ref-pyannote-streaming)、会议 44.6%、网络视频 44.9%，竞品在这三个场景里落在 51% 到 76% 之间。

![四个玻璃罐里的彩色线团一个比一个乱，最后一个已经溢出罐口，旁边的放大镜显示凑近看也依然理不清](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-04-hard-audio.jpg)

这个问题没有任何一家解决。产品设计必须能够容忍说话人标签时常出错。

本地部署的选择更少，但是确实存在。[pyannote 的开源 Community-1](#ref-pyannote-benchmark) 是给自身不带分离的 ASR 模型配用的标准搭档，在 pyannoteAI 自家的 DIHARD Broadcast 图上是 10.5% DER，付费的 Precision-2 是 9.4%，两者差距小到可以直接把免费版当作默认选项。更值得注意的是 [MOSS-Transcribe-Diarize](#ref-moss-diarize)：Apache-2.0 许可、0.9B 参数，端到端一遍就能同时完成转写和分离，覆盖 50 多种语言，支持最长 90 分钟的录音，直接输出带时间戳和 `[S01]`／`[S02]` 标签的稿件。它在 INTERSPEECH 2026 第二届 MLC-SLM 挑战赛中获得第一名。

这一条正好回答了开头那通电话的问题：87 分钟、两个说话人，一个可以在自己机器上运行的 0.9B 模型，一遍就能处理完。

## 中文与多语言支持

![一本摊开的账簿，纵栏在撕裂的纸边处戛然而止；纸外的桌面上立着一枚刻字的石印，旁边是一盒从未打开过的印泥](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-06-missing-column.jpg)

中立榜单根本没有中文这一栏，所以这部分最需要自己动手验证，而厂商页面恰恰在这里最不可靠。

ElevenLabs 的普通话页面就是最清楚的例子。宣传文案称 Scribe 达到[“a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice”](#ref-elevenlabs-chinese)，而同一个页面往下几百像素的评测表里写的是 **Scribe v1 在 FLEURS 上 7.2% WER**。同一页自相矛盾，两个数字差了两倍多。那张表还给 Deepgram Nova 2 记了“98.2% WER”，这个数字意味着几乎全错，更合理的解释是当时根本不支持这个语种。此外表里标注的还是 v1，而在售产品已经是 v2 了。

中文场景下最好的选择在本地。[Qwen3-ASR](#ref-qwen3-asr) 是阿里巴巴于 2026-01-29 发布的 Apache-2.0 模型，提供 0.6B 和 1.7B 两个尺寸，另有一个用于时间戳的强制对齐模型，覆盖 52 种语言和方言，其中包含 22 种中国方言，粤语、吴语、闽南语都在内，这一点这里基本没有别的选项能做到。阿里自己报告的数字，也确实是阿里自己报告的：AISHELL-2 上 2.71，Whisper large-v3 是 5.06；粤语 Fleurs-yue 上 3.98 对 9.18。

有两个理由让我没有把它归进厂商宣传那一类。第一，在 Open ASR Leaderboard 上，它英文总榜排第七、4.95，位于 AssemblyAI 旗舰产品之前，并且在私有对话集上拿到了全场最好成绩，而那是它不可能训练过的数据。第二，[布朗大学的科研计算中心](#ref-brown-ccv)在自己的转写服务里推荐用 Qwen3-ASR 处理嘈杂环境和非英语方言，而他们在这件事上不销售任何产品。

## 语码转换（一句话里混用多种语言）

在一句话里混用多种语言的音频上，厂商的宣传远远走在证据前面。Gladia 宣称 Solaria-1 覆盖 [100 多种语言并原生支持语码转换](#ref-gladia-roundup)，其中 42 种“别处没有”。AssemblyAI 称 Universal-3.5 Pro [“across 18 languages, with native code switching”](#ref-assemblyai-pricing)。Gemini 3.5 Transcribe 能在 85 个以上的语言区自动检测。

我没有找到任何一份中立评测，对这些产品在混说音频上打过分。目前公开的研究资源是 [CS-Dialogue](#ref-cs-dialogue)，包含 200 位说话人贡献的 104 小时中英混说自然对话，供学术使用；作者也指出 Whisper 这类预训练模型在这份数据上仍有提升空间。另外还有一篇 [2025 年的系统性文献综述](#ref-cs-survey)，适合用来建立整体框架。

如果你要做这件事，没有任何已发表的数字能替你做决定。可行的办法是拿 CS-Dialogue 或者你自己的音频样本，去实测两三家候选。

## 我会怎么选

这个领域没有单一的冠军，所以下面按场景分开说。

**用量大且稳定，英文。**自托管 `parakeet-tdt-0.6b-v2`，每音频小时约 $0.0008。它只支持英文、采用 cc-by-4.0，RTFx 6025 意味着一张卡就能覆盖极大的用量。需要多语种就换成 `-v3`，代价约 0.2 个 WER 点。

**用量大且稳定，多语种。**Qwen3-ASR-1.7B，Apache-2.0，52 种语言，中立榜单第七，自托管每音频小时约 $0.006。

**用量小或波动大。**留在托管这一侧，因为 GPU 空转会把模型本身的成本优势全部抵消掉。Deepgram $0.26/小时、离线自带分离，是最不容易出意外的默认选择；如果能接受旧一代模型，AssemblyAI Universal-2 的 $0.15 加 $0.02 更便宜。

**多人音频，且归属重要。**瓶颈在分离质量，不在 WER。走托管就交给 pyannoteAI，或者用打包了 Precision-2 的 Gladia；本地就用 MOSS-Transcribe-Diarize，或者给任意 ASR 模型配上 pyannote Community-1。无论选哪条路，都要为重叠语音的失败预留余量，因为 19.8% DER 已经是公开可查的**最好**流式成绩。

**很多人同时抢话。**[布朗大学 CCV 的文档](#ref-brown-ccv)推荐微软 Azure，这是我在这个问题上找到的唯一一条非厂商建议；Azure 2026 年 6 月的模型在榜单上排第六。

**以中文为主。**自托管 Qwen3-ASR-1.7B，再配一个分离模型。它是这里唯一真正覆盖中国方言的选项。不要照着厂商的普通话页面来选型。

**音频不能出网。**选本地表里任何一行 Apache-2.0 或 MIT 的模型。这也是唯一一种账单不再随音频时长线性增长的情况。

**只要最便宜。**留在托管就选 Google Cloud STT v2 动态批处理 $0.18/小时；自托管就选 `granite-5.0-470m-turboctc`，每音频小时 $0.0004，但记得确认你拿到的是 apache-2.0 那个版本，而不是 `-nc`。

**最后回到开头那个 bug。**如果录制环节在你自己手里，就按参与者分轨录制，不要把采集阶段本来就能保留的信息，交给分离模型去事后还原。

## 读这些数字时该有的怀疑

![五座一模一样的铜奖杯排成一行，每一座背后都伸出一只手，把空白绶带别在自己身上](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-02-five-winners.jpg)

除了上面这些表格之外，还有一件事值得记住：几乎每一篇“2026 最佳语音转文字 API”都由参与对比的某一家厂商自己发布，而我查阅的五份里有四份把自家排在第一。[AssemblyAI 的榜单](#ref-assemblyai-diarization-roundup)在 cpWER 上把 AssemblyAI 排第一。[pyannoteAI 的评测](#ref-pyannote-benchmark)在 DER 上把 pyannoteAI 排第一，并且把 AssemblyAI 的 Universal-3 排在十二个系统的最后，31.1% DER 对上 pyannoteAI 自己的 9.4%。[Deepgram 的指南](#ref-deepgram-guide)在十家里把 Deepgram 排第一。[Gladia 的那篇](#ref-gladia-roundup)把 Gladia 排第一。

即使是同一个评测的名字，底下的结论也会互相矛盾。[Gladia 报告 Solaria-3 在 Earnings22 上以 6.4% WER 排名第一](#ref-gladia-solaria3)，领先 AssemblyAI 的 6.9% 和 ElevenLabs 的 7.7%。而在中立榜单的 Earnings22 那一栏里，ElevenLabs 是 4.8，Gladia 是 5.94，AssemblyAI 是 6.05。排序完全颠倒，绝对值也对不上，因为这本来就是两套不同的评测流程。

有两个例外。[Coval 的选型指南](#ref-coval-guide)出自一家销售评测工具而非模型的公司，它干脆不点名冠军，只说头部厂商彼此相差“within 1-2 percentage points”。另一个例外是 [Picovoice](#ref-picovoice-diarization)。它销售 Falcon，拿 Falcon 和 pyannote 做对比，却明确表示不评冠军：“Our goal was not to crown a single ‘winner’, but to understand tradeoffs between research accuracy and production efficiency.”在它自己的数字里，[pyannote 的 DER 优于 Falcon，9.0% 对 10.3%](#ref-picovoice-diarization)。这是这次调研中唯一一家发布了自家产品落败结果的厂商。

所以实际的做法是：先看发布方，再看图表；确认它选用了哪个指标；然后追问数据集能不能被指名。“我们内部的、跨多个真实数据集的评测”不是任何人能够核对的结果。

我最初拿到的线索里，有好几条在打开原始出处之后就站不住了：一张 cpWER 表被归给了错误的发布方；一项标称“包含在内”的分离其实要另外付费；一个价格差了三倍；一份榜单的第一名早已掉到第十二；还有一个“WER 下降 55%”的说法，在被引用的那篇论文里根本找不到。这些说法读起来全都合情合理，而这正是这个品类最麻烦的地方。合理是很廉价的，真数字和编出来的数字之间，唯一的区别就在于有没有真的去看一眼。

## 参考资料与原文定位

### 厂商发布的评测与选型文章

- <span id="ref-assemblyai-diarization-roundup"></span>AssemblyAI（对比中的厂商）——原始出处：["8 Best Speaker Diarization Solutions & APIs in 2026"](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=it%20measures%20diarization%20in%20isolation%20from%20the%20transcript)，作者 Kelsey Foster，日期 2026 年 8 月 4 日。支持段落：“DER is a fine academic metric, but it measures diarization in isolation from the transcript. In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks.”对比表列出 AssemblyAI 30.17、ElevenLabs Scribe v2 35.26、Gladia 36.87、Deepgram Nova-3 EN 37.92，而 PyAnnote、NVIDIA NeMo、Kaldi/SpeechBrain 一律标为“DER-reported only”。数据集说明：[“The cpWER numbers come from our internal diarization benchmark, run across a mix of real-world datasets.”](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=The%20cpWER%20numbers%20come%20from%20our%20internal%20diarization%20benchmark)作者披露：“I run Voice AI at AssemblyAI.”——读取于 [2026-08-27](https://web.archive.org/web/20260827231553/https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis)
- <span id="ref-pyannote-benchmark"></span>pyannoteAI（对比中的厂商）——原始出处：[Speaker Diarization DER performance comparison](https://www.pyannote.ai/benchmark)。只报告 DER，覆盖十个 DIHARD 场景、259 段录音、约 67 小时音频。各场景结果以图片形式发布，没有文字替代内容，以下数值系从图片中读取。DIHARD Broadcast（12 段对话，3 至 4 人）：pyannoteAI Precision-2 9.4%、pyannoteAI OSS Community-1 10.5%、NVIDIA 10.3%、AWS 16.5%、Speechmatics Enhanced 16.8%、Gladia Solaria 22.0%、Mistral Voxtral Mini 22.7%、Speechmatics Standard 24.5%、Soniox 25.2%、ElevenLabs Scribe-v2 26.4%、Deepgram Nova-3 26.9%、AssemblyAI Universal-3 31.1%。DIHARD Clinical（51 段对话，2 至 3 人）：Precision-2 13.3%，AssemblyAI Universal-3 48.1%。方法说明：“We did not provide the number of speakers for any of them.”——读取于 [2026-08-27](https://web.archive.org/web/20260827231649/https://www.pyannote.ai/benchmark)
- <span id="ref-pyannote-streaming"></span>pyannoteAI（对比中的厂商）——原始出处：["How accurate is streaming speaker diarization?"](https://www.pyannote.ai/blog/streaming-diarization-benchmark#:~:text=pyannote%20leaves%207.71%25%20of%20speech%20unattributed)，页面未标注日期。DIHARD III 全语种 DER：pyannote API 19.8%（误报 4.8、漏检 7.7、混淆 7.3）；Speechmatics real-time v2 31.3%（6.2 / 19.7 / 5.5）；Deepgram Nova 3 39.1%（4.6 / 25.3 / 9.3）；AssemblyAI Universal Streaming v3 39.2%（6.9 / 20.4 / 11.8）。支持段落：“pyannote leaves 7.71% of speech unattributed, while the other systems miss between 19.70% and 25.26%, roughly 2.5 to 3 times more.”pyannote Live-1 在难场景的数值：餐厅 54.4%、网络视频 44.9%、会议 44.6%。方法学提示：“measured on DIHARD without special scoring for overlapped speech”——读取于 [2026-08-27](https://web.archive.org/web/20260827231613/https://www.pyannote.ai/blog/streaming-diarization-benchmark)
- <span id="ref-deepgram-guide"></span>Deepgram（对比中的厂商）——原始出处：["Best Speech-to-Text APIs 2026"](https://deepgram.com/learn/best-speech-to-text-apis-2026#:~:text=ranking%20them%20based%20on%20accuracy%2C%20features%2C%20and%20real-world%20performance)。作者 Jose Nicholas Francisco，产品市场经理，页面标注“UPDATED Feb 19, 2026”。导语称文章对主流 API 进行比较，“ranking them based on accuracy, features, and real-world performance”。排序由带编号的小标题承载，这些标题存在于页面标记中但不出现在渲染后的正文文本里，因此文内链接落在导语上：1. Deepgram、2. OpenAI Whisper、3. Microsoft Azure、4. Google Cloud、5. AssemblyAI、6. Amazon Transcribe、7. Rev AI、8. Speechmatics、9. IBM Watson、10. Kaldi。我在页面上找不到任何支撑该排序的分厂商 WER 数值——读取于 [2026-08-27](https://web.archive.org/web/20260827231713/https://deepgram.com/learn/best-speech-to-text-apis-2026)
- <span id="ref-gladia-roundup"></span>Gladia（对比中的厂商）——原始出处：["Best speech-to-text APIs in 2026"](https://www.gladia.io/blog/best-speech-to-text-apis#:~:text=including%2042%20languages%20unavailable%20elsewhere)，作者 Ani Ghazaryan，标注“Published on Jul 9, 2026”。文章开篇即写“Every speech-to-text vendor claims the lowest word error rate…”，随后把 Gladia 排在第一。支持段落：“Solaria-1 is our breadth model, the most multilingual in the lineup, with 100+ languages and native code-switching across all of them, including 42 languages unavailable elsewhere”；Solaria-3“ranks #1 across English and core European languages (EN, FR, DE, ES, IT), ahead of AssemblyAI, ElevenLabs, Deepgram, Mistral, and Speechmatics”；Solaria-1“leads outright on speaker diarization accuracy: 3x more accurate diarization error rate (DER) than alternatives”；以及“Gladia's audio intelligence features are bundled into base pricing, covering code switching, speaker diarization…”——读取于 [2026-08-27](https://web.archive.org/web/20260827233025/https://www.gladia.io/blog/best-speech-to-text-apis)
- <span id="ref-gladia-solaria3"></span>Gladia（对比中的厂商）——原始出处：["Introducing Solaria-3"](https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages)，作者 Ani Ghazaryan，日期 2026 年 6 月 10 日。称 Solaria-3 在 Earnings22 上以 6.4% WER 排名第一，领先 AssemblyAI 6.9%、ElevenLabs 7.7%、Speechmatics 7.8%、Mistral 7.9%、Deepgram 12.0%；在 Gladia 内部英语生产数据集上 9.6% WER，较 Solaria-1 的 12.9% 提升 26%。本文引用的 Solaria-1 语言与语码转换宣称出自 Gladia 另一篇选型文章，不在本篇——读取于 [2026-08-27](https://web.archive.org/web/20260827231734/https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages)
- <span id="ref-picovoice-diarization"></span>Picovoice（对比中的厂商，销售 Falcon）——原始出处：["State of Speaker Diarization"](https://picovoice.ai/blog/state-of-speaker-diarization/#:~:text=not%20to%20crown%20a%20single)，发布于 2023 年 12 月 18 日，2026 年 3 月 11 日更新。在 VoxConverse 上：pyannote DER 9.0%，Falcon 10.3%；Falcon JER 19.9%，pyannote 27.4%。支持段落：“Our goal was not to crown a single ‘winner’, but to understand tradeoffs between research accuracy and production efficiency.”在本文涉及的厂商里，只有 Picovoice 发布了一份自家产品在主指标上落后的评测——读取于 [2026-08-27](https://web.archive.org/web/20260827231752/https://picovoice.ai/blog/state-of-speaker-diarization/)
- <span id="ref-elevenlabs-chinese"></span>ElevenLabs（厂商）——原始出处：[普通话语音转文字页面](https://elevenlabs.io/speech-to-text/chinese#:~:text=a%20word%20error%20rate%20of%20just%203.1%25%20on%20the%20FLEURS%20benchmark%20and%205.5%25%20on%20Common%20Voice)。正文声称“a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice”。同一页的“Mandarin Chinese Transcription Benchmark”表格则列出 Scribe v1 在 FLEURS 上 7.2% WER、Gemini Flash 2 17.6%、Whisper Large v3 23.6%、Deepgram Nova 2 98.2%。本文引用它是作为“厂商评测自相矛盾”的证据，而非作为中文准确率数据——读取于 2026-08-27；最近的存档快照为 [2026-07-25](https://web.archive.org/web/20260725123551/https://elevenlabs.io/speech-to-text/chinese)

### 独立与非厂商来源

- <span id="ref-open-asr-leaderboard"></span>Hugging Face——原始出处：[Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)，页面标注“Last updated on 28 August 2026”。排名于实时 Gradio 应用中读取，并开启 License、Size (B)、# Languages 三列：reson8/resonant-1 4.77、modulate/vfast 4.78、reson8/resonant-1-flash 4.79、elevenlabs/scribe_v2 4.84、zoom/scribe_v1 4.90、microsoft/azure-speech-06-2026 4.91、Qwen/Qwen3-ASR-1.7B-hf 4.95（apache-2.0，2.04B，52 种语言，RTFx 819.96）、assemblyai/universal-3-5-pro 5.02、AutoArk-AI/ARK-ASR-3B 5.18、HojoAI/Hojo-ASR-V1 5.21、gladia/solaria-3 5.22、nvidia/canary-qwen-2.5b 5.23。再往下：ibm-granite/granite-speech-4.1-2b 5.43（RTFx 545.65）、nvidia/parakeet-tdt-0.6b-v2 5.48（RTFx 6024.67，cc-by-4.0，0.6B，1 种语言）、OpenMOSS-Team/MOSS-Transcribe-Diarize 5.52（RTFx 381.16，apache-2.0，0.91B，50 种语言）、ibm-granite/granite-speech-5.0-470m-turboctc-nc 5.55（cc-by-nc-sa-4.0）、nvidia/parakeet-tdt-0.6b-v3 5.66（RTFx 6076.07，26 种语言）、Qwen/Qwen3-ASR-0.6B-hf 5.70、nvidia/canary-1b-flash 5.71（cc-by-4.0）、microsoft/Phi-4-multimodal-instruct 5.72（mit）、nvidia/canary-1b 5.76（cc-by-nc-4.0）、ibm-granite/granite-speech-5.0-470m-turboctc 5.78（apache-2.0，RTFx 12945.54）、mistralai/Voxtral-Small-24B-2507 5.79（RTFx 101.27），以及排在第 37 位的 distil-whisper/distil-large-v3.5 6.20，这是表中唯一的 Whisper 家族条目。40 行中有 30 行为非专有许可证。范围说明：“evaluates open-source and proprietary speech recognition models on English and multiple European languages.”私有数据集来自 Appen Inc.、DataoceanAI 与 Voice Arena——读取于 [2026-08-31](https://web.archive.org/web/20260831232538/https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- <span id="ref-coval-guide"></span>Coval——原始出处：["Best Speech-to-Text Providers in 2026"](https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/)，日期 2026 年 6 月 4 日。Coval 卖的是语音智能体的仿真与评测工具，不卖语音转文字模型，因此不在自己的对比中参赛——不过读者若因此认为“应该多做评测”，它同样受益。值得注意的是，它没有点名冠军，而是称头部厂商彼此相差“within 1-2 percentage points of each other”——读取于 [2026-08-27](https://web.archive.org/web/20260827231856/https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/)
- <span id="ref-brown-ccv"></span>布朗大学计算与可视化中心（Brown University Center for Computation and Visualization）——原始出处：[Comparing Speech-to-text Models](https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models#:~:text=please%20choose%20the%20Microsoft%20Azure%20model%20for%20better%20performance)。这是一所大学的科研计算服务，不销售任何语音转文字产品。支持段落：“if the accuracy of speaker diarization is a priority and/or the audio includes many speakers talking over each other, please choose the Microsoft Azure model for better performance.”该页同时推荐用 Qwen3-ASR 处理嘈杂环境与非英语方言。有一处内部不一致值得记下：正文推荐 Azure，但该页自己的对比表里并没有 Azure——读取于 [2026-08-27](https://web.archive.org/web/20260827231924/https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models)

### 定价页面

- <span id="ref-assemblyai-pricing"></span>AssemblyAI——原始出处：[Pricing](https://www.assemblyai.com/pricing#:~:text=works%20across%2018%20languages%2C%20with%20native%20code%20switching)。离线：Universal-3.5 Pro $0.21/小时，Universal-2 $0.15/小时。流式：Universal-3.5 Pro Realtime $0.45/小时，Universal-Streaming $0.15/小时。在“Add-On Features”标签页下，Speaker Diarization 在 Universal-3.5 Pro 与 Universal-2 上均为 $0.02/小时；keyterms prompting 在 Universal-3.5 Pro 上为 $0.05/小时，在 Universal-2 上包含。Universal-3.5 Pro“works across 18 languages, with native code switching”；Universal-2“supports 99 languages”。免费额度：离线 185 小时、流式 333 小时——读取于 [2026-08-27](https://web.archive.org/web/20260827231946/https://www.assemblyai.com/pricing)
- <span id="ref-deepgram-pricing"></span>Deepgram——原始出处：[Pricing](https://deepgram.com/pricing)。Pre-Recorded 标签页：Nova-3 单语 $0.0043/分钟（$0.258/小时），Nova-3 多语 $0.0052/分钟，Speaker Diarization 标注为“Included”。Streaming 标签页：Nova-3 单语促销价 $0.0048/分钟，原价 $0.0077/分钟，Speaker Diarization 为 $0.0020/分钟（$0.12/小时）。页面写明“Limited-time promotional rates on streaming.”——读取于 [2026-08-27](https://web.archive.org/web/20260827232006/https://deepgram.com/pricing)
- <span id="ref-gladia-pricing"></span>Gladia——原始出处：[Pricing](https://www.gladia.io/pricing#:~:text=Async%20at%20%240.61%2Fhr)。Starter：“Async at $0.61/hr”“Real-time at $0.75/hr”，附“50€ in free credits”。Growth：“Async as low as $0.20/hr”“Real-time as low as $0.25/hr”。说话人分离、100 多种语言与词级时间戳在所有档位均列为包含。FAQ 说明免费额度为“a one-time grant with no monthly reset. That's roughly 80+ hours of pre-recorded transcription”——读取于 [2026-08-27](https://web.archive.org/web/20260827232027/https://www.gladia.io/pricing)
- <span id="ref-elevenlabs-pricing"></span>ElevenLabs——原始出处：[API pricing](https://elevenlabs.io/pricing/api)。Scribe v2 $0.22/小时，Scribe v2 Realtime $0.39/小时。列出的附加项为实体识别 $0.070/小时与 keyterm prompting $0.050/小时；页面上没有出现任何单独的说话人分离收费项——读取于 [2026-08-27](https://web.archive.org/web/20260827232044/https://elevenlabs.io/pricing/api)
- <span id="ref-google-stt-pricing"></span>Google Cloud——原始出处：[Speech-to-Text pricing](https://cloud.google.com/speech-to-text/pricing#:~:text=%240.016%20%2F%201%20minute)。Speech-to-Text V2 标准识别：每月前 50 万分钟 $0.016/分钟（$0.96/小时），随用量分档降至 $0.010、$0.008 与 $0.004/分钟。标准动态批处理识别：$0.003/分钟（$0.18/小时），页面描述为以“a lower level of urgency”处理音频。Chirp 列在“Standard”模型之中。页面上没有出现单独的说话人分离收费项——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2026-08-25](https://web.archive.org/web/20260825164556/https://cloud.google.com/speech-to-text/pricing)
- <span id="ref-gemini-pricing"></span>Google——原始出处：[Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing#:~:text=effective%20blended%20rate%20of%20~%240.005%20per%20min%20for%20Transcribe)。语音转文字按 token 计费而非按分钟，页面只给出折算后的综合费率。支持段落：“Estimated pricing is based on 25 audio tokens per second for input and 175 text tokens per minute for output, for an effective blended rate of ~$0.005 per min for Transcribe”；`gemini-3.5-transcribe-live` 则为“~$0.009 per min for Live Transcribe”。本文的每小时价格即由上述综合费率乘以 60 得出；页面并未公布这两个转写模型的输入/输出分项单价，因此本文也不引用任何分项数字——读取于 [2026-08-27](https://web.archive.org/web/20260827232123/https://ai.google.dev/gemini-api/docs/pricing)

### 谷歌产品文档

- <span id="ref-gemini-blog"></span>Google——原始出处：[Gemini 3.5 Transcribe 发布公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/#:~:text=As%20measured%20by%20Artificial%20Analysis)，发布于 2026 年 8 月 26 日。宣布 `gemini-3.5-transcribe` 与 `gemini-3.5-transcribe-live` 进入公开预览，支持“over 85 languages”；并称“As measured by Artificial Analysis”，流式平均 WER 4.0%、非流式 2.6%，FLEURS 上 5.50%/5.04%——这些数字由谷歌归于第三方评测方而非自家流程——以及相对 Chirp 3 有 70% 的延迟改进。该文描述多说话人识别“for up to three speakers (support for 3+ speakers is experimental)”，比 API 文档给出的数字更窄——读取于 2026-08-27；存档快照 [2026-08-27](https://web.archive.org/web/20260827151836/https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)
- <span id="ref-gemini-transcribe-docs"></span>Google——原始出处：[Gemini API 音频转写文档](https://ai.google.dev/gemini-api/docs/transcribe#:~:text=is%20incompatible%20with%20timestamp_granularities%20and%20diarization_mode)。逐字支持段落：“Note: Smart transcription ("smart") is incompatible with timestamp_granularities and diarization_mode. If you need word timestamps or speaker diarization, configure mode with {"type": "verbatim", ...}.”；“Up to 8 speakers are supported (attribution for 3 or more speakers is experimental).”；“Supply up to 1,000 terms in the custom_vocabulary array (best results are typically achieved with up to 100 terms)”；“Note: Enabling word-level timestamps may degrade overall transcription accuracy.”——读取于 [2026-08-27](https://web.archive.org/web/20260827232104/https://ai.google.dev/gemini-api/docs/transcribe)
- <span id="ref-chirp3-docs"></span>Google——原始出处：[Chirp 3 模型文档](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3#:~:text=Available%20only%20in%20Speech.Recognize%20and%20Speech.BatchRecognize)。语言表共 111 行：29 行标记 GA、82 行标记 Preview（由表格直接计数得出）。Speaker Diarization 标注为“Available only in Speech.BatchRecognize”，状态 GA；句级时间戳为“Available only in Speech.StreamingRecognize”。词级时间戳出现在一张以“Chirp 3 doesn't support the following features”为引导的表中，但该行自身的说明写着“Automatically generated by the model and can be optionally enabled, which some transcription degradation is expected. Available only in Speech.Recognize and Speech.BatchRecognize”——页面自相矛盾，本文如实并列两种说法，不作裁定——读取于 [2026-08-27](https://web.archive.org/web/20260827232206/https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)

### 开源模型与研究文献

- <span id="ref-qwen3-asr"></span>阿里巴巴通义千问团队（就其自家模型而言属厂商）——原始出处：[Qwen3-ASR 代码仓库](https://github.com/QwenLM/Qwen3-ASR)。Apache-2.0 许可。2026 年 1 月 29 日发布 0.6B 与 1.7B 两个尺寸，另有用于时间戳的 Qwen3-ForcedAligner-0.6B；2026 年 6 月 26 日加入原生 Transformers 支持。覆盖 52 种语言与方言，其中 22 种为中文方言（含粤语港澳口音与广东口音、吴语、闽南语）。Qwen 自报的 Qwen3-ASR-1.7B 对 Whisper large-v3 成绩：AISHELL-2-test 2.71 对 5.06；Fleurs-yue 3.98 对 9.18；Librispeech clean 1.63 对 1.51。对 GPT-4o-Transcribe 的 M4Singer：5.98 对 16.77。文档未提及说话人分离——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2026-07-29](https://web.archive.org/web/20260729105533/https://github.com/QwenLM/Qwen3-ASR)
- <span id="ref-gladia-pyannote"></span>Gladia——原始出处：["Gladia x pyannoteAI: Speaker diarization and the future of voice AI"](https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai)，日期 2025 年 3 月 11 日。支持段落：“Our speaker diarization pipeline is now powered by pyannoteAI's Precision‑2, their most accurate model to date.”该文未说明分离是打包还是另计费；本文价格表中的打包信息来自 Gladia 的定价页——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2025-06-17](https://web.archive.org/web/20250617234345/https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai)
- <span id="ref-cs-dialogue"></span>周家鸣（Jiaming Zhou）等——原始出处：["CS-Dialogue: A 104-Hour Dataset of Spontaneous Mandarin-English Code-Switching Dialogues for Speech Recognition"](https://arxiv.org/abs/2502.18913)，arXiv，2025 年 2 月 26 日提交，3 月 12 日修订。包含 200 位说话人的 104 小时自发对话，提供完整长对话录音与全部转写文本，面向学术用途免费开放。摘要指出“existing pre-trained models such as Whisper still have the space to improve”——读取于 [2026-08-27](https://web.archive.org/web/20260827232224/https://arxiv.org/abs/2502.18913)
- <span id="ref-cs-survey"></span>Maha Tufail Agro、Atharva Kulkarni、Karima Kadaoui、Zeerak Talat、Hanan Aldarmaki——原始出处：["Code-Switching in End-to-End Automatic Speech Recognition: A Systematic Literature Review"](https://arxiv.org/abs/2507.07741)，arXiv，2025 年 7 月 10 日提交。系统综述，覆盖语言、数据集、指标、模型选择与开放挑战。本文仅将其用作背景：其摘要并未给出单一的 WER 下降幅度数字——读取于 [2026-08-27](https://web.archive.org/web/20260827232243/https://arxiv.org/abs/2507.07741)
- <span id="ref-asr-leaderboard-hardware"></span>Hugging Face——原始出处：[open_asr_leaderboard 代码仓库](https://github.com/huggingface/open_asr_leaderboard)。在“Evaluate a model (as of 24 July 2026)”一节中：英文与多语种短音频评测“use Hugging Face Jobs to guarantee reproducibility: every run executes a Docker image on the same hardware”。硬件表只列出一种规格——“h200 | Nvidia H200 | 23 vCPU | 256 GB | 3000 GB | 1x H200 (141 GB) | $0.0833［每分钟］| $5.00［每小时］”。文中还给出英文短音频完整评测的实际开销示例：“$2.92 for nvidia/parakeet-tdt-0.6b-v3”“$4.75 for openai/whisper-large-v3-turbo”“$5.58 for Qwen/Qwen3-ASR-1.7B”。本文自托管的每音频小时成本，是用 $5.00 除以各模型公布的 RTFx 得出，前提是 GPU 持续满载——读取于 2026-08-31；Archive.org 的保存接口拒绝 github.com，故未附快照
- <span id="ref-moss-diarize"></span>OpenMOSS Team——原始出处：[MOSS-Transcribe-Diarize 模型卡](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)，许可证 apache-2.0。原文：“MOSS-Transcribe-Diarize 0.9B is an end-to-end audio understanding model for long-form multi-speaker transcription, diarization, timestamps, and acoustic event awareness”；“It supports transcription and diarization across 50+ languages, single-pass inference on audio recordings up to 90 minutes long, and custom hotword prompting for domain-specific terms”；模型“generates a compact speaker-aware transcript in one pass, including timestamps and anonymous speaker labels such as [S01], [S02], and beyond”。模型卡记载它“won first place in the 2nd MLC-SLM Challenge at INTERSPEECH 2026”——读取于 [2026-08-31](https://web.archive.org/web/20260831232520/https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)

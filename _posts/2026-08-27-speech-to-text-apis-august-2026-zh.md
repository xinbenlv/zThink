---
title: "每个语音转文字榜单都有赢家，通常就是发榜的人"
excerpt: "五份「2026 最佳语音转文字 API」榜单，四份把发榜的厂商排在第一。标注清楚每个数字由谁发布之后，还剩下多少可信的东西。"
date: 2026-08-27
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

*2026 年 8 月的语音转文字市场是什么样子，写给需要挑一家、然后赶紧把活干完的人。每个数字我都标了是谁发布的，因为在这个品类里，这大概是你最需要知道的一件事。价格是 2026-08-27 当天从各家定价页读的，变动很快。*

## 起因：777 句话，只有一个说话人

一通 87 分钟的双人电话，用会议机器人录下来，转写结果看上去很干净：777 个句子，用词准确，标点也对。但全部 777 句，都被标成了同一个人说的。

转写本身没问题，出问题的是**说话人分离**（speaker diarization）——判断「谁在什么时候说话」的那一层。它在电话这一路音频上整个塌掉了，把两个人合并成了一个。通常的补救办法是把左右声道拆开分别转写，但这条路也断了：文件是伪立体声，左右声道相减的差值大约在 −84 dB，两条完全相同的声道套了个立体声的壳。

这种故障，看词错误率（WER）是看不出来的。用词确实是对的，坏掉的是下游所有需要知道「这句话是谁说的」的环节。

于是我去找一份评测，想看看该换哪家。

![两条波形完全相同的立体声轨道，下方左减右的差值是一条死平的直线；右侧的转写稿每一行都盖着同一个说话人印章](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-01-dual-mono.jpg)

## 五份榜单，四个自封的第一

搜索 2026 年最好的语音转文字 API，你会得到一篇文笔不错、语气笃定、还带对比表格的文章。而它几乎总是由表格里的某一家公司发布的。

下面是我找到的五份，每一行都写明发布方：

| 文章 | 发布方 | 排第一的是谁 | 用的指标 |
|---|---|---|---|
| ["8 Best Speaker Diarization Solutions & APIs in 2026"](#ref-assemblyai-diarization-roundup) | AssemblyAI | AssemblyAI，30.17 | cpWER，内部数据集 |
| ["Speaker Diarization DER performance comparison"](#ref-pyannote-benchmark) | pyannoteAI | pyannoteAI Precision-2 | DER，DIHARD |
| ["Best Speech-to-Text APIs 2026"](#ref-deepgram-guide) | Deepgram | Deepgram，十家里的第一 | WER，来源混杂 |
| ["Best speech-to-text APIs in 2026"](#ref-gladia-roundup) | Gladia | Gladia Solaria-3 | WER，来源混杂 |
| ["State of Speaker Diarization"](#ref-picovoice-diarization) | Picovoice | **没有人**——pyannote 在 DER 上赢了它自家的 Falcon | JER 与 DER |

其中四份是营销材料，每一份都把发布方放在最上面。

第五份我特意留着，因为它不合这个规律。Picovoice 卖 Falcon，拿它和 pyannote 对比，然后[明确拒绝评出赢家](#ref-picovoice-diarization)：「Our goal was not to crown a single "winner", but to understand tradeoffs between research accuracy and production efficiency.」按它自己给的数字，[DER 上 pyannote 9.0%、Falcon 10.3%](#ref-picovoice-diarization)，pyannote 领先；Falcon 只在 Jaccard 错误率上占优。这是这次调研里唯一一家发布了自家产品输掉的评测的厂商。

![五座一模一样的奖杯，每座后面伸出一只手，给它自己别上空白绶带](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-02-five-winners.jpg)

其中两份对同一家公司的判断，反差最大。在 [AssemblyAI 自己的表里](#ref-assemblyai-diarization-roundup)，AssemblyAI 第一。在 [pyannoteAI 的 DIHARD Broadcast 图里](#ref-pyannote-benchmark)，AssemblyAI 的 Universal-3 **在十二个系统里垫底**，DER 31.1%，而 pyannoteAI 自己是 9.4%。换到 DIHARD Clinical，它还是最后一名，48.1% 对 13.3%。两张图我都打开看过，说的是同一家公司，结论完全相反。

## 为什么换个指标就换个排名

两张图打架，有一部分原因是它们量的根本不是同一件事。这大概是全文唯一值得记住的一点理论。

**DER（diarization error rate，分离错误率）以「时间」计**。把音频时间轴摊开，把漏检的、误检成人声的、以及分给错误说话人的秒数加起来，除以总语音时长。它衡量切分，完全不管文字。

**cpWER（concatenated minimum-permutation word error rate）以「词」计**。把每个说话人说过的话各自拼接起来，穷举你的说话人标签映射到真实说话人的所有排列，取最优的一种，再算词错误率。转写错误和说话人归属错误，它一起罚。

这个区别，AssemblyAI 讲得比我读到的任何人都清楚。考虑到这段话最后导向哪里，这一点有点尴尬：

> DER is a fine academic metric, but [it measures diarization in isolation from the transcript](#ref-assemblyai-diarization-roundup). In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks.

（大意：DER 是个不错的学术指标，但它把分离和转写稿割裂开来衡量。生产环境里你真正在意的，是正确的说话人标签有没有落在正确的词上——这正是 cpWER 衡量的。记住这个区别，因为它会改变榜单的样子。）

它确实会改变榜单的样子，而且是朝着有利于 AssemblyAI 的方向改变——这句话大概就是为此而写的。

![同一段录音，左边用卷尺和秒表按时间量，右边被拆成词块用镊子分拣；两边下方的排名绶带顺序并不相同](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-03-der-vs-cpwer.jpg)

这些都未必是恶意。pyannoteAI 只卖分离，本身不产出转写稿，DER 根本就是它的产品唯一能被打分的指标；AssemblyAI 把转写和分离作为一条流水线卖，cpWER 才是对它实际交付内容更诚实的度量。指标是跟着产品走的。这也是为什么任何单独一家的图表都不能当成行业排名来读。

即便如此，那张表还是有两处扎眼。一是数据集不公开——这些数字[「come from our internal diarization benchmark, run across a mix of real-world datasets」](#ref-assemblyai-diarization-roundup)，这样的结果无从复现。二是表里列了八个系统，只有它赢过的那四家商业竞品有 cpWER 数值，pyannote、NeMo、Kaldi 一律标注为「DER-reported only」。于是最有可能在分离质量上赢过它的那个系统，旁边恰好没有可比的数字。

公道地说，作者在文中直接写明自己在 AssemblyAI 负责语音 AI 业务，这比同类文章里的大多数都坦率。

## 没人拿去做营销的那个数字

这次调研里最有用的一个数字来自一份厂商评测，而它让整个品类都不好看。

[pyannoteAI 的流式评测](#ref-pyannote-streaming)在 DIHARD III 上衡量流式说话人分离。以下是它自己的结果，当然是按对自己最有利的方式呈现的：

| 系统 | DER（全语种） | 漏掉的语音 |
|---|---|---|
| pyannote API | 19.8% | 7.7% |
| Speechmatics real-time v2 | 31.3% | 19.7% |
| Deepgram Nova 3 | 39.1% | 25.3% |
| AssemblyAI Universal Streaming v3 | 39.2% | 20.4% |

冠军的成绩是 19.8% DER，也就是大约每五秒语音里仍有一秒是错的，而这张图还是它自家做的。

难音频上更糟。即便是 pyannote，在自己的评测里，[餐厅场景 DER 54.4%](#ref-pyannote-streaming)、会议 44.6%、网络视频 44.9%。竞品在这三个场景落在 51% 到 76% 之间。

如果你要在嘈杂的多人音频上做产品，没有任何一家解决了这个问题。稳妥的假设是：无论选谁，难音频上的流式说话人分离都不可靠，产品得能扛住标签有时候是错的。

![四个玻璃罐里的彩色线团一个比一个缠得厉害，最后一个溢出罐口，放大镜下依然理不清](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-04-hard-audio.jpg)

## 最接近中立的一份记分牌

[Hugging Face Open ASR Leaderboard](#ref-open-asr-leaderboard) 是这里唯一一份不由竞争对手发布的排名。模型通过 pull request 提交，评测脚本公开，平均分里还有一部分来自 Appen 和 DataoceanAI 持有的私有数据集。这一点很重要，因为没人能下载的测试集，也就没人能拿去训练。

以下是它 2026 年 8 月 25 日更新时的名次，按默认数据集组合的平均 WER 排序，越低越好：

| 名次 | 模型 | 平均 WER |
|---|---|---|
| 1 | modulate/vfast | 5.14 |
| 2 | reson8/resonant-1 | 5.17 |
| 3 | microsoft/azure-speech-06-2026 | 5.17 |
| 5 | elevenlabs/scribe_v2 | 5.24 |
| 7 | Qwen/Qwen3-ASR-1.7B | 5.31 |
| 8 | assemblyai/universal-3-5-pro | 5.40 |
| 11 | gladia/solaria-3 | 5.58 |
| 12 | nvidia/canary-qwen-2.5b | 5.63 |

前十二名的差距只有半个百分点。这些产品在实际使用中的区别，无论是什么，都不会是英文的整体识别准确率。

把这份榜单和 Gladia 自己那篇文章对照，也很有意思。[Gladia 称 Solaria-3 在 Earnings22 上以 6.4% WER 排第一](#ref-gladia-solaria3)，领先 AssemblyAI 的 6.9% 和 ElevenLabs 的 7.7%。而在榜单的 Earnings22 那一列，ElevenLabs Scribe v2 是 4.8，Gladia Solaria-3 是 5.94，AssemblyAI 是 6.05。名次倒过来了，绝对数值也对不上——两套评测流程本来就不是同一套，所以厂商说的「我们在 Earnings22 排第一」，说的其实是它自己那套流程里的第一。

还有一个关于动机的旁证。[Coval 的 2026 年选型指南](#ref-coval-guide)是我找到的另一篇由「不卖语音转文字模型」的公司写的对比，它卖的是评测工具。它也是唯一一篇不点名冠军的，只说头部厂商彼此相差「within 1-2 percentage points」。自家有产品下场，和最后能评出一个明确冠军，这两件事似乎总是一起出现。

有一个局限比其余的都重要：这份榜单只覆盖英语和欧洲语言。没有中文，没有日语，没有阿拉伯语，没有印地语。如果你的音频不在其中，它帮不上什么忙。

## 真实价格是多少

下表统一折算成「每小时音频多少美元」，2026-08-27 从各家定价页读取。最容易搞错的是最后一列。

| 厂商 / 模型 | 离线 $/小时 | 实时 $/小时 | 说话人分离 |
|---|---|---|---|
| [AssemblyAI Universal-2](#ref-assemblyai-pricing) | $0.15 | — | **单独计费，+$0.02/小时** |
| [AssemblyAI Universal-3.5 Pro](#ref-assemblyai-pricing) | $0.21 | $0.45 | **单独计费，+$0.02/小时** |
| [Deepgram Nova-3 单语](#ref-deepgram-pricing) | $0.26 | 促销 $0.29，原价 $0.46 | **离线包含；流式单独计费 +$0.12/小时** |
| [ElevenLabs Scribe v2](#ref-elevenlabs-pricing) | $0.22 | $0.39 | 包含（无单独收费项） |
| [Gladia，Starter](#ref-gladia-pricing) | $0.61 | $0.75 | 包含 |
| [Gladia，Growth 承诺量](#ref-gladia-pricing) | 低至 $0.20 | 低至 $0.25 | 包含 |
| [Google Cloud STT v2 标准](#ref-google-stt-pricing) | $0.96 | — | 无单独收费项 |
| [Google Cloud STT v2 动态批处理](#ref-google-stt-pricing) | $0.18 | — | 无单独收费项 |
| [Gemini 3.5 Transcribe](#ref-gemini-pricing) | 约 $0.30 | 约 $0.54（Live） | 包含，但只能在 verbatim 模式下用 |
| [Qwen3-ASR，自建](#ref-qwen3-asr) | 自付算力 | 自付算力 | 没有，需搭配 pyannote |

几条关于账最后怎么算出来的注意事项：

- **说话人分离的打包方式两个方向都不一致。**Deepgram 离线免费送，流式却按 $0.0020/分钟收；AssemblyAI 两种模式都收 $0.02/小时。只比基础价，选哪家都会算错。
- Gladia 的 $0.61/小时 是表里最贵的离线价，大约是 Deepgram 的三倍，而且只有承诺量的 Growth 方案才降到 $0.20。它打包的分离用的是 [pyannoteAI 的 Precision-2](#ref-gladia-pyannote)，组合确实强，但按量付费这一档实在谈不上便宜。
- Google Cloud 的动态批处理 $0.18/小时 是表里最低的托管价，代价是按「较低的紧急程度」排队处理。
- Gemini 那一格是谷歌自己的估算。它按 token 计费，页面把它折算成[「an effective blended rate of ~$0.005 per min for Transcribe」](#ref-gemini-pricing)，假设输入每秒 25 个音频 token、输出每分钟 175 个文本 token。话密的音频输出 token 更多、更贵，所以 $0.30/小时 应当当作下限而不是报价。
- AssemblyAI 的免费额度意外地大：离线 185 小时、流式 333 小时。Gladia 给一次性 50 欧元额度，大约相当于 80 小时离线转写。
- Deepgram 的流式折扣页面上明写是「limited-time promotional rate」，所以做明年的预算时应该按 $0.46 算。

![一排空白纸质吊牌，有些底下另挂了一个小吊牌，有些则已在牌面上压了火漆印](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-05-price-tags.jpg)

## 谷歌其实是三个产品，很多人混为一谈

- **Chirp 3**，在 Cloud Speech-to-Text v2 里，覆盖 [29 个正式发布和 82 个预览状态的语言](#ref-chirp3-docs)，合计 111 个。分离只在 `BatchRecognize` 里可用。词级时间戳的处境比较尴尬：它被放在一张标题为「Chirp 3 doesn't support the following features」的表里，但[同一行自己的说明](#ref-chirp3-docs)又写着可以在 `Speech.Recognize` 和 `Speech.BatchRecognize` 里启用，代价是「some transcription degradation」。文档自相矛盾；无论按哪种读法，流式里都用不了。
- **Gemini 3.5 Transcribe** 于 [2026-08-26 进入公开预览](#ref-gemini-blog)，比我写这篇文章早一天。两个模型 `gemini-3.5-transcribe` 和 `gemini-3.5-transcribe-live`，85 种以上语言，自定义词表[最多 1000 条](#ref-gemini-transcribe-docs)。谷歌给出流式 4.0%、非流式 2.6% 的 WER，并[把这两个数字归给 Artificial Analysis](#ref-gemini-blog) 而不是自家评测流程。因为它才上线一天，目前没有任何第三方复测，这一点应当直说。
- **直接用 Gemini 多模态提示词转写**，灵活，但输出结构取决于提示词。

Gemini 3.5 Transcribe 有一个坑，我觉得在照着它做设计之前最好先知道。它的 `smart` 模式负责去掉口头禅、整理自我更正，文档对代价写得很直白：

> Note: Smart transcription ("smart") is [incompatible with `timestamp_granularities` and `diarization_mode`](#ref-gemini-transcribe-docs). If you need word timestamps or speaker diarization, configure mode with `{"type": "verbatim", ...}`.

也就是说，干净好读的文字，和「谁在什么时间说了什么」，同一次调用里只能二选一。而会议纪要类产品恰恰两样都要，所以这是个架构决策，不是脚注。

同一页还有两点：分离[最多支持 8 个说话人，3 个及以上标为实验性](#ref-gemini-transcribe-docs)（发布博客写的是三个，文档写的是八个，以文档为准）；以及「enabling word-level timestamps may degrade overall transcription accuracy」。

## 中文，以及榜单不会告诉你的事

中立记分牌不含中文。而含中文的那些厂商页面，是整篇调研里证据强度最弱的，ElevenLabs 的普通话页面就是最好的例子。

它的营销正文声称 Scribe 达到[「a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice」](#ref-elevenlabs-chinese)。而同一页往下几百像素的评测表格里写着 **Scribe v1 在 FLEURS 上 7.2% WER**。同一个页面，自己和自己差了两倍多。这张表还给 Deepgram Nova 2 记了「98.2% WER」——这个数字意味着几乎全错，更可能的解释是 Nova 2 当时根本不支持这门语言。而且表格标的仍是 v1，在售的产品已经是 v2 了。

我引用这一页，不是为了说明中文准确率，而是因为一张厂商评测表居然可以在活跃页面上挂好几个月都没人核对。

中文这边更值得认真看的是 [**Qwen3-ASR**](#ref-qwen3-asr)，阿里 2026-01-29 以 Apache-2.0 发布，有 0.6B 和 1.7B 两个尺寸，外加一个做时间戳的强制对齐模型。它覆盖 52 种语言和方言，其中包含 22 种中文方言——粤语、吴语、闽南语都在内，这是本文其他任何一家基本都不碰的部分。

阿里自己报的数字，也确实是阿里自己报的：AISHELL-2 上 Qwen3-ASR-1.7B 2.71，Whisper large-v3 是 5.06；粤语 Fleurs-yue 上 3.98 对 9.18。中文错误率大约是 Whisper 的一半，而且这个模型你可以自己跑起来。

有两件事让我没把它归进厂商宣传那一堆。一是在 Open ASR Leaderboard 上，Qwen3-ASR-1.7B **英文总榜第 7**，5.31，排在 AssemblyAI 旗舰型号前面；在私有对话数据集那一列它拿到全场最好成绩 13.9，而那份数据它不可能训练过。同时，它是榜上最靠前的、有实测吞吐数字的模型——排在它前面的都是你无法自建的 API。二是[布朗大学的科研计算中心](#ref-brown-ccv)在自家转写服务的文档里推荐用 Qwen3-ASR 处理嘈杂环境和非英语方言，而他们在这里没有任何东西要卖。

它本身不做说话人分离，所以还得配一个 pyannote。

![账簿的表格栏在撕裂的纸边处戛然而止，边外的桌面上立着一枚刻着「榜」字的石印，红色印泥盒开着，桌面却干干净净](/assets/blogposts/2026-08-27-speech-to-text-apis-august-2026/speech-to-text-apis-2026-06-missing-column.jpg)

## 中英混说：宣传跑在证据前面

对于一句话里混用多种语言的音频，营销话术远远走在证据前面。

Gladia 宣传 Solaria-1 覆盖 [100 多种语言并原生支持语码转换](#ref-gladia-roundup)，其中 42 种「别处没有」。AssemblyAI 把 Universal-3.5 Pro 描述为[「works across 18 languages, with native code switching」](#ref-assemblyai-pricing)。Gemini 3.5 Transcribe 则宣称自动识别 85 种以上语言。

我没有找到任何一份中立评测，对上述任何一家在语码转换音频上打过分。公开的研究资源是 [CS-Dialogue](#ref-cs-dialogue)：104 小时、200 位说话人的中英自发对话语料，面向学术用途开放；论文作者也指出，Whisper 这类预训练模型在这项任务上仍有提升空间。另有一篇 [2025 年的系统性文献综述](#ref-cs-survey)可作背景，但它并没有给出一个可引用的总体提升幅度。

所以如果你要做中英西三语混说，没有任何已发表的数字能替你做决定。拿 CS-Dialogue，或者你自己的音频样本，去跑两三家候选。

## 如果是我，会怎么选

这里没有单一冠军，所以按场景分开说。

**多人英语、且说话人归属重要。**瓶颈是分离质量而不是 WER，在这件事上专业厂商胜过打包方案。把转写和分离分开走：用一家强的 ASR API 出文字，用 pyannoteAI 出说话人。如果一定要一家搞定，Gladia 以 $0.61/小时 打包了 Precision-2，可以省掉自己做集成。无论选谁，都要为重叠语音的失败留余地：19.8% DER 已经是公开的**最好**流式成绩。

**很多人同时抢话。**[布朗大学 CCV 的文档](#ref-brown-ccv)针对的正是这个场景，建议用 Microsoft Azure。这是我在这个问题上找到的唯一一条非厂商建议，而 Azure 2026 年 6 月的模型在榜单上排第三。

**以中文为主。**自建 Qwen3-ASR-1.7B，配 pyannote。它是本文里唯一真正覆盖中文方言的选项，英文成绩在中立榜单上也有竞争力，成本是算力而不是按小时计费。不要照着厂商的中文页面选型，那是这个品类里最不可靠的一批页面。

**中英西混说。**没有任何公开结果能定论。按各家宣称先圈定 Gladia 和 Gemini 3.5 Transcribe，然后拿自己的音频实测。在你测过之前，把任何厂商的语码转换宣称都当作未经验证。

**只想便宜。**能接受延迟就用 Google Cloud STT v2 动态批处理，$0.18/小时；不能接受就用 AssemblyAI Universal-2，$0.15 加 $0.02 分离等于 $0.17/小时。在你开始抠成本之前，Deepgram $0.26/小时含分离是更省心的默认值，离线免费送分离也让小规模场景更好算账。

**自建或数据不出内网。**Qwen3-ASR，Apache-2.0，分离交给 pyannote。它也是价格表里唯一一行：账单不会随音频时长无止境地线性增长。

**最后回到开头那个 bug：**如果录制端在你手里，就按参与者分轨录，别把采集阶段本来就能留住的信息，丢给分离模型去还原。说话人分离是对「源头没分好轨」的一种修补，而目前对所有厂商来说，这种修补都是有损的。

## 怎么读这些数字

在相信任何一张图之前，有三件事值得先确认：

1. **先看发布方，再看图表。**在这个品类里，发布方对冠军的预测力高得离谱。
2. **确认它选了哪个指标。**同一段音频，DER 和 cpWER 会给出不同的排名，而厂商会挑自家产品天生擅长的那个。
3. **问数据集能不能被指名。**「我们内部的、跨多个真实数据集的评测」不是一个你能核对、复现或据以追责的结果。

我起初拿到的线索里，有好几条打开原始出处后就散了：一张 cpWER 表被归给了错误的发布方；一项「包含在内」的分离其实要另外付费；一个价格差了三倍；一份榜单的第一名早已掉到第十二；还有一个「WER 下降 55%」的说法，在被引用的那篇论文里根本找不到。这些说法读起来都完全合理。这正是这个品类最麻烦的地方——合理是很廉价的，真数字和编出来的数字之间，唯一的区别就是你有没有真的去看一眼。

## 参考资料与原文定位

### 厂商发布的评测与选型文章

- <span id="ref-assemblyai-diarization-roundup"></span>AssemblyAI（对比中的厂商）——原始出处：["8 Best Speaker Diarization Solutions & APIs in 2026"](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=it%20measures%20diarization%20in%20isolation%20from%20the%20transcript)，作者 Kelsey Foster，日期 2026 年 8 月 4 日。支持段落：「DER is a fine academic metric, but it measures diarization in isolation from the transcript. In production what you care about is whether the right speaker label lands on the right words—which is what cpWER measures. Keep that distinction in mind, because it changes how the leaderboard looks.」对比表列出 AssemblyAI 30.17、ElevenLabs Scribe v2 35.26、Gladia 36.87、Deepgram Nova-3 EN 37.92，而 PyAnnote、NVIDIA NeMo、Kaldi/SpeechBrain 一律标为「DER-reported only」。数据集说明：[「The cpWER numbers come from our internal diarization benchmark, run across a mix of real-world datasets.」](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis#:~:text=The%20cpWER%20numbers%20come%20from%20our%20internal%20diarization%20benchmark)作者披露：「I run Voice AI at AssemblyAI.」——读取于 [2026-08-27](https://web.archive.org/web/20260827231553/https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis)
- <span id="ref-pyannote-benchmark"></span>pyannoteAI（对比中的厂商）——原始出处：[Speaker Diarization DER performance comparison](https://www.pyannote.ai/benchmark)。只报告 DER，覆盖十个 DIHARD 场景、259 段录音、约 67 小时音频。各场景结果以图片形式发布，没有文字替代内容，以下数值系从图片中读取。DIHARD Broadcast（12 段对话，3 至 4 人）：pyannoteAI Precision-2 9.4%、pyannoteAI OSS Community-1 10.5%、NVIDIA 10.3%、AWS 16.5%、Speechmatics Enhanced 16.8%、Gladia Solaria 22.0%、Mistral Voxtral Mini 22.7%、Speechmatics Standard 24.5%、Soniox 25.2%、ElevenLabs Scribe-v2 26.4%、Deepgram Nova-3 26.9%、AssemblyAI Universal-3 31.1%。DIHARD Clinical（51 段对话，2 至 3 人）：Precision-2 13.3%，AssemblyAI Universal-3 48.1%。方法说明：「We did not provide the number of speakers for any of them.」——读取于 [2026-08-27](https://web.archive.org/web/20260827231649/https://www.pyannote.ai/benchmark)
- <span id="ref-pyannote-streaming"></span>pyannoteAI（对比中的厂商）——原始出处：["How accurate is streaming speaker diarization?"](https://www.pyannote.ai/blog/streaming-diarization-benchmark#:~:text=pyannote%20leaves%207.71%25%20of%20speech%20unattributed)，页面未标注日期。DIHARD III 全语种 DER：pyannote API 19.8%（误报 4.8、漏检 7.7、混淆 7.3）；Speechmatics real-time v2 31.3%（6.2 / 19.7 / 5.5）；Deepgram Nova 3 39.1%（4.6 / 25.3 / 9.3）；AssemblyAI Universal Streaming v3 39.2%（6.9 / 20.4 / 11.8）。支持段落：「pyannote leaves 7.71% of speech unattributed, while the other systems miss between 19.70% and 25.26%, roughly 2.5 to 3 times more.」pyannote Live-1 在难场景的数值：餐厅 54.4%、网络视频 44.9%、会议 44.6%。方法学提示：「measured on DIHARD without special scoring for overlapped speech」——读取于 [2026-08-27](https://web.archive.org/web/20260827231613/https://www.pyannote.ai/blog/streaming-diarization-benchmark)
- <span id="ref-deepgram-guide"></span>Deepgram（对比中的厂商）——原始出处：["Best Speech-to-Text APIs 2026"](https://deepgram.com/learn/best-speech-to-text-apis-2026#:~:text=ranking%20them%20based%20on%20accuracy%2C%20features%2C%20and%20real-world%20performance)。作者 Jose Nicholas Francisco，产品市场经理，页面标注「UPDATED Feb 19, 2026」。导语称文章对主流 API 进行比较，「ranking them based on accuracy, features, and real-world performance」。排序由带编号的小标题承载，这些标题存在于页面标记中但不出现在渲染后的正文文本里，因此文内链接落在导语上：1. Deepgram、2. OpenAI Whisper、3. Microsoft Azure、4. Google Cloud、5. AssemblyAI、6. Amazon Transcribe、7. Rev AI、8. Speechmatics、9. IBM Watson、10. Kaldi。我在页面上找不到任何支撑该排序的分厂商 WER 数值——读取于 [2026-08-27](https://web.archive.org/web/20260827231713/https://deepgram.com/learn/best-speech-to-text-apis-2026)
- <span id="ref-gladia-roundup"></span>Gladia（对比中的厂商）——原始出处：["Best speech-to-text APIs in 2026"](https://www.gladia.io/blog/best-speech-to-text-apis#:~:text=including%2042%20languages%20unavailable%20elsewhere)，作者 Ani Ghazaryan，标注「Published on Jul 9, 2026」。文章开篇即写「Every speech-to-text vendor claims the lowest word error rate…」，随后把 Gladia 排在第一。支持段落：「Solaria-1 is our breadth model, the most multilingual in the lineup, with 100+ languages and native code-switching across all of them, including 42 languages unavailable elsewhere」；Solaria-3「ranks #1 across English and core European languages (EN, FR, DE, ES, IT), ahead of AssemblyAI, ElevenLabs, Deepgram, Mistral, and Speechmatics」；Solaria-1「leads outright on speaker diarization accuracy: 3x more accurate diarization error rate (DER) than alternatives」；以及「Gladia's audio intelligence features are bundled into base pricing, covering code switching, speaker diarization…」——读取于 [2026-08-27](https://web.archive.org/web/20260827233025/https://www.gladia.io/blog/best-speech-to-text-apis)
- <span id="ref-gladia-solaria3"></span>Gladia（对比中的厂商）——原始出处：["Introducing Solaria-3"](https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages)，作者 Ani Ghazaryan，日期 2026 年 6 月 10 日。称 Solaria-3 在 Earnings22 上以 6.4% WER 排名第一，领先 AssemblyAI 6.9%、ElevenLabs 7.7%、Speechmatics 7.8%、Mistral 7.9%、Deepgram 12.0%；在 Gladia 内部英语生产数据集上 9.6% WER，较 Solaria-1 的 12.9% 提升 26%。本文引用的 Solaria-1 语言与语码转换宣称出自 Gladia 另一篇选型文章，不在本篇——读取于 [2026-08-27](https://web.archive.org/web/20260827231734/https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages)
- <span id="ref-picovoice-diarization"></span>Picovoice（对比中的厂商，销售 Falcon）——原始出处：["State of Speaker Diarization"](https://picovoice.ai/blog/state-of-speaker-diarization/#:~:text=not%20to%20crown%20a%20single)，发布于 2023 年 12 月 18 日，2026 年 3 月 11 日更新。在 VoxConverse 上：pyannote DER 9.0%，Falcon 10.3%；Falcon JER 19.9%，pyannote 27.4%。支持段落：「Our goal was not to crown a single "winner", but to understand tradeoffs between research accuracy and production efficiency.」在本文涉及的厂商里，只有 Picovoice 发布了一份自家产品在主指标上落后的评测——读取于 [2026-08-27](https://web.archive.org/web/20260827231752/https://picovoice.ai/blog/state-of-speaker-diarization/)
- <span id="ref-elevenlabs-chinese"></span>ElevenLabs（厂商）——原始出处：[普通话语音转文字页面](https://elevenlabs.io/speech-to-text/chinese#:~:text=a%20word%20error%20rate%20of%20just%203.1%25%20on%20the%20FLEURS%20benchmark%20and%205.5%25%20on%20Common%20Voice)。正文声称「a word error rate of just 3.1% on the FLEURS benchmark and 5.5% on Common Voice」。同一页的「Mandarin Chinese Transcription Benchmark」表格则列出 Scribe v1 在 FLEURS 上 7.2% WER、Gemini Flash 2 17.6%、Whisper Large v3 23.6%、Deepgram Nova 2 98.2%。本文引用它是作为「厂商评测自相矛盾」的证据，而非作为中文准确率数据——读取于 2026-08-27；最近的存档快照为 [2026-07-25](https://web.archive.org/web/20260725123551/https://elevenlabs.io/speech-to-text/chinese)

### 独立与非厂商来源

- <span id="ref-open-asr-leaderboard"></span>Hugging Face——原始出处：[Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)，最后更新 2026 年 8 月 25 日。名次从运行中的 Gradio 应用读取：modulate/vfast 5.14、reson8/resonant-1 5.17、microsoft/azure-speech-06-2026 5.17、reson8/resonant-1-flash 5.20、elevenlabs/scribe_v2 5.24、zoom/scribe_v1 5.24、Qwen/Qwen3-ASR-1.7B-hf 5.31、assemblyai/universal-3-5-pro 5.40、HojoAI/Hojo-ASR-V1 5.47、AutoArk-AI/ARK-ASR-3B 5.58、gladia/solaria-3 5.58、nvidia/canary-qwen-2.5b 5.63。Earnings22-Cleaned-AA-chunked 一列：elevenlabs/scribe_v2 4.80、gladia/solaria-3 5.94、assemblyai/universal-3-5-pro 6.05。Qwen3-ASR-1.7B 在 Private (conversational) 上取得全场最佳 13.9。覆盖范围说明：「evaluates open-source and proprietary speech recognition models on English and multiple European languages.」私有数据集来自 Appen Inc. 与 DataoceanAI。排在 Qwen3-ASR-1.7B 之前的模型吞吐一栏均为「NA」，与只能通过 API 访问的情况一致——读取于 [2026-08-27](https://web.archive.org/web/20260827231830/https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- <span id="ref-coval-guide"></span>Coval——原始出处：["Best Speech-to-Text Providers in 2026"](https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/)，日期 2026 年 6 月 4 日。Coval 卖的是语音智能体的仿真与评测工具，不卖语音转文字模型，因此不在自己的对比中参赛——不过读者若因此认为「应该多做评测」，它同样受益。值得注意的是，它没有点名冠军，而是称头部厂商彼此相差「within 1-2 percentage points of each other」——读取于 [2026-08-27](https://web.archive.org/web/20260827231856/https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/)
- <span id="ref-brown-ccv"></span>布朗大学计算与可视化中心（Brown University Center for Computation and Visualization）——原始出处：[Comparing Speech-to-text Models](https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models#:~:text=please%20choose%20the%20Microsoft%20Azure%20model%20for%20better%20performance)。这是一所大学的科研计算服务，不销售任何语音转文字产品。支持段落：「if the accuracy of speaker diarization is a priority and/or the audio includes many speakers talking over each other, please choose the Microsoft Azure model for better performance.」该页同时推荐用 Qwen3-ASR 处理嘈杂环境与非英语方言。有一处内部不一致值得记下：正文推荐 Azure，但该页自己的对比表里并没有 Azure——读取于 [2026-08-27](https://web.archive.org/web/20260827231924/https://docs.ccv.brown.edu/ai-tools/services/transcribe/comparing-speech-to-text-models)

### 定价页面

- <span id="ref-assemblyai-pricing"></span>AssemblyAI——原始出处：[Pricing](https://www.assemblyai.com/pricing#:~:text=works%20across%2018%20languages%2C%20with%20native%20code%20switching)。离线：Universal-3.5 Pro $0.21/小时，Universal-2 $0.15/小时。流式：Universal-3.5 Pro Realtime $0.45/小时，Universal-Streaming $0.15/小时。在「Add-On Features」标签页下，Speaker Diarization 在 Universal-3.5 Pro 与 Universal-2 上均为 $0.02/小时；keyterms prompting 在 Universal-3.5 Pro 上为 $0.05/小时，在 Universal-2 上包含。Universal-3.5 Pro「works across 18 languages, with native code switching」；Universal-2「supports 99 languages」。免费额度：离线 185 小时、流式 333 小时——读取于 [2026-08-27](https://web.archive.org/web/20260827231946/https://www.assemblyai.com/pricing)
- <span id="ref-deepgram-pricing"></span>Deepgram——原始出处：[Pricing](https://deepgram.com/pricing)。Pre-Recorded 标签页：Nova-3 单语 $0.0043/分钟（$0.258/小时），Nova-3 多语 $0.0052/分钟，Speaker Diarization 标注为「Included」。Streaming 标签页：Nova-3 单语促销价 $0.0048/分钟，原价 $0.0077/分钟，Speaker Diarization 为 $0.0020/分钟（$0.12/小时）。页面写明「Limited-time promotional rates on streaming.」——读取于 [2026-08-27](https://web.archive.org/web/20260827232006/https://deepgram.com/pricing)
- <span id="ref-gladia-pricing"></span>Gladia——原始出处：[Pricing](https://www.gladia.io/pricing#:~:text=Async%20at%20%240.61%2Fhr)。Starter：「Async at $0.61/hr」「Real-time at $0.75/hr」，附「50€ in free credits」。Growth：「Async as low as $0.20/hr」「Real-time as low as $0.25/hr」。说话人分离、100 多种语言与词级时间戳在所有档位均列为包含。FAQ 说明免费额度为「a one-time grant with no monthly reset. That's roughly 80+ hours of pre-recorded transcription」——读取于 [2026-08-27](https://web.archive.org/web/20260827232027/https://www.gladia.io/pricing)
- <span id="ref-elevenlabs-pricing"></span>ElevenLabs——原始出处：[API pricing](https://elevenlabs.io/pricing/api)。Scribe v2 $0.22/小时，Scribe v2 Realtime $0.39/小时。列出的附加项为实体识别 $0.070/小时与 keyterm prompting $0.050/小时；页面上没有出现任何单独的说话人分离收费项——读取于 [2026-08-27](https://web.archive.org/web/20260827232044/https://elevenlabs.io/pricing/api)
- <span id="ref-google-stt-pricing"></span>Google Cloud——原始出处：[Speech-to-Text pricing](https://cloud.google.com/speech-to-text/pricing#:~:text=%240.016%20%2F%201%20minute)。Speech-to-Text V2 标准识别：每月前 50 万分钟 $0.016/分钟（$0.96/小时），随用量分档降至 $0.010、$0.008 与 $0.004/分钟。标准动态批处理识别：$0.003/分钟（$0.18/小时），页面描述为以「a lower level of urgency」处理音频。Chirp 列在「Standard」模型之中。页面上没有出现单独的说话人分离收费项——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2026-08-25](https://web.archive.org/web/20260825164556/https://cloud.google.com/speech-to-text/pricing)
- <span id="ref-gemini-pricing"></span>Google——原始出处：[Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing#:~:text=effective%20blended%20rate%20of%20~%240.005%20per%20min%20for%20Transcribe)。语音转文字按 token 计费而非按分钟，页面只给出折算后的综合费率。支持段落：「Estimated pricing is based on 25 audio tokens per second for input and 175 text tokens per minute for output, for an effective blended rate of ~$0.005 per min for Transcribe」；`gemini-3.5-transcribe-live` 则为「~$0.009 per min for Live Transcribe」。本文的每小时价格即由上述综合费率乘以 60 得出；页面并未公布这两个转写模型的输入/输出分项单价，因此本文也不引用任何分项数字——读取于 [2026-08-27](https://web.archive.org/web/20260827232123/https://ai.google.dev/gemini-api/docs/pricing)

### 谷歌产品文档

- <span id="ref-gemini-blog"></span>Google——原始出处：[Gemini 3.5 Transcribe 发布公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/#:~:text=As%20measured%20by%20Artificial%20Analysis)，发布于 2026 年 8 月 26 日。宣布 `gemini-3.5-transcribe` 与 `gemini-3.5-transcribe-live` 进入公开预览，支持「over 85 languages」；并称「As measured by Artificial Analysis」，流式平均 WER 4.0%、非流式 2.6%，FLEURS 上 5.50%/5.04%——这些数字由谷歌归于第三方评测方而非自家流程——以及相对 Chirp 3 有 70% 的延迟改进。该文描述多说话人识别「for up to three speakers (support for 3+ speakers is experimental)」，比 API 文档给出的数字更窄——读取于 2026-08-27；存档快照 [2026-08-27](https://web.archive.org/web/20260827151836/https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)
- <span id="ref-gemini-transcribe-docs"></span>Google——原始出处：[Gemini API 音频转写文档](https://ai.google.dev/gemini-api/docs/transcribe#:~:text=is%20incompatible%20with%20timestamp_granularities%20and%20diarization_mode)。逐字支持段落：「Note: Smart transcription ("smart") is incompatible with timestamp_granularities and diarization_mode. If you need word timestamps or speaker diarization, configure mode with {"type": "verbatim", ...}.」；「Up to 8 speakers are supported (attribution for 3 or more speakers is experimental).」；「Supply up to 1,000 terms in the custom_vocabulary array (best results are typically achieved with up to 100 terms)」；「Note: Enabling word-level timestamps may degrade overall transcription accuracy.」——读取于 [2026-08-27](https://web.archive.org/web/20260827232104/https://ai.google.dev/gemini-api/docs/transcribe)
- <span id="ref-chirp3-docs"></span>Google——原始出处：[Chirp 3 模型文档](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3#:~:text=Available%20only%20in%20Speech.Recognize%20and%20Speech.BatchRecognize)。语言表共 111 行：29 行标记 GA、82 行标记 Preview（由表格直接计数得出）。Speaker Diarization 标注为「Available only in Speech.BatchRecognize」，状态 GA；句级时间戳为「Available only in Speech.StreamingRecognize」。词级时间戳出现在一张以「Chirp 3 doesn't support the following features」为引导的表中，但该行自身的说明写着「Automatically generated by the model and can be optionally enabled, which some transcription degradation is expected. Available only in Speech.Recognize and Speech.BatchRecognize」——页面自相矛盾，本文如实并列两种说法，不作裁定——读取于 [2026-08-27](https://web.archive.org/web/20260827232206/https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)

### 开源模型与研究文献

- <span id="ref-qwen3-asr"></span>阿里巴巴通义千问团队（就其自家模型而言属厂商）——原始出处：[Qwen3-ASR 代码仓库](https://github.com/QwenLM/Qwen3-ASR)。Apache-2.0 许可。2026 年 1 月 29 日发布 0.6B 与 1.7B 两个尺寸，另有用于时间戳的 Qwen3-ForcedAligner-0.6B；2026 年 6 月 26 日加入原生 Transformers 支持。覆盖 52 种语言与方言，其中 22 种为中文方言（含粤语港澳口音与广东口音、吴语、闽南语）。Qwen 自报的 Qwen3-ASR-1.7B 对 Whisper large-v3 成绩：AISHELL-2-test 2.71 对 5.06；Fleurs-yue 3.98 对 9.18；Librispeech clean 1.63 对 1.51。对 GPT-4o-Transcribe 的 M4Singer：5.98 对 16.77。文档未提及说话人分离——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2026-07-29](https://web.archive.org/web/20260729105533/https://github.com/QwenLM/Qwen3-ASR)
- <span id="ref-gladia-pyannote"></span>Gladia——原始出处：["Gladia x pyannoteAI: Speaker diarization and the future of voice AI"](https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai)，日期 2025 年 3 月 11 日。支持段落：「Our speaker diarization pipeline is now powered by pyannoteAI's Precision‑2, their most accurate model to date.」该文未说明分离是打包还是另计费；本文价格表中的打包信息来自 Gladia 的定价页——读取于 2026-08-27；Archive.org 的保存接口拒绝了该网址，最近的既有快照为 [2025-06-17](https://web.archive.org/web/20250617234345/https://www.gladia.io/blog/gladia-x-pyannoteai-speaker-diarization-and-the-future-of-voice-ai)
- <span id="ref-cs-dialogue"></span>周家鸣（Jiaming Zhou）等——原始出处：["CS-Dialogue: A 104-Hour Dataset of Spontaneous Mandarin-English Code-Switching Dialogues for Speech Recognition"](https://arxiv.org/abs/2502.18913)，arXiv，2025 年 2 月 26 日提交，3 月 12 日修订。包含 200 位说话人的 104 小时自发对话，提供完整长对话录音与全部转写文本，面向学术用途免费开放。摘要指出「existing pre-trained models such as Whisper still have the space to improve」——读取于 [2026-08-27](https://web.archive.org/web/20260827232224/https://arxiv.org/abs/2502.18913)
- <span id="ref-cs-survey"></span>Maha Tufail Agro、Atharva Kulkarni、Karima Kadaoui、Zeerak Talat、Hanan Aldarmaki——原始出处：["Code-Switching in End-to-End Automatic Speech Recognition: A Systematic Literature Review"](https://arxiv.org/abs/2507.07741)，arXiv，2025 年 7 月 10 日提交。系统综述，覆盖语言、数据集、指标、模型选择与开放挑战。本文仅将其用作背景：其摘要并未给出单一的 WER 下降幅度数字——读取于 [2026-08-27](https://web.archive.org/web/20260827232243/https://arxiv.org/abs/2507.07741)

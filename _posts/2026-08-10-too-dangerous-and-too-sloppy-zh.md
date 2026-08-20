---
title: "翰墨贞洁、铅梓荒淫"
excerpt: "五百年前，印刷术也曾同时被指控危险而粗劣；它留下的答案不是封死生产工具，而是让验证也变得便宜。"
date: 2026-08-10
lang: zh
published: true
cover_image:
  src: /assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/cover-wechat-zh.jpg
  x: 200
  y: 0
  size: 383
og_image: /assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/cover-wechat-zh.jpg
translationKey: printing-press-ai-2026-08-10
categories:
  - blog
tags:
  - ai
  - history
  - wikipedia
  - trust
  - policy
---

> **你应当奸淫。**<br>
> *Thou shalt commit adultery.*

1631 年，伦敦的一部英文《圣经》在第七诫里漏掉了一个只有三个字母的词：*not*。负责这批书的御用印刷商巴克（Robert Barker）和卢卡斯（Martin Lucas）被判罚 300 英镑，书也遭到扣押。几百年里，故事越讲越狠：这一版书被尽数销毁，两人的印刷牌照也被吊销。

[档案却记录了另一个结局](#ref-moseley-wicked-bible)：扣押的书后来退回给印刷商修正；他们没有失去牌照；300 英镑罚款也以自费建立希腊文印刷所为条件获免（论文第 17–18、54 页；PDF 文件第 18–19、55 页）。那个漏掉的 *not* 是真的，后来附着其上的严惩故事却是传说。

这是印刷术留下的一场双重事故：机器抢在校对之前复制了错误，故事又抢在考证之前复制了自己。

## 五百年后，轮到我了

前几天，我以一种不太舒服的方式，看见同一套机制在 AI 时代重演。

我在英文维基百科创建了一篇题为《“容易取消”规定》（*Easy-to-cancel mandate*）的条目，讨论一类要求“取消订阅必须像开通订阅一样容易”的法律。后来，这篇条目被提交到维基百科的 [人工智能公告板（AI noticeboard）](#ref-wikipedia-ai-noticeboard)。编辑们怀疑我借助了 AI 起草，事实也确实如此。其中一位编辑核对引用时发现了一处措辞上的瑕疵：稿件中某项“两步取消”要求本来已由德国法律确立，我的写法却可能让人误以为，那是研究者自行设定的测试标准。

我本来就无意隐瞒——甚至觉得，到了 2026 年，写作时使用 AI 辅助，难道不已经是默认了吗？作为软件工程师，我的工作流早已从自动补全（auto-complete），逐步走到让 AI 修正语法和拼写、重构代码、生成单个文件与测试；到 2023—2025 年，它已经参与我大部分代码库的生成和新项目的规划。

我在公告板上甚至给出了一个直白的数字：[新增代码行中“almost 90–95%”由 AI 生成](#ref-wikipedia-ai-noticeboard)。那句话现在看并不精确：90–95% 不是逐行统计出来的字符比例，而是我按信息生产过程中投入的“劳动时间”作出的粗略估算。我花大约一分钟写提示词，AI 往往接着运行十到二十分钟；按这个口径，绝大部分时间发生在机器一侧。如果改按最终文本或代码的字符量计算，我估计 AI 生成的部分超过 99%——毕竟它生成文字远比人快。

这篇条目的制作方式也是如此：我向 Claude Code 和 Codex 下指令，让它们研究、引注和事实核查；发现问题时，我通常修改提示、要求继续修订，而不是直接改写输出。我把文章先放在草稿命名空间，主动向相关维基专题寻求编辑审阅和指导，得到反馈后才移入条目空间；连草稿讨论页也借助了 LLM。问题不是我藏起了 AI，而是我没有意识到，这个社区已经对这种制作过程本身划下了一条新界线。

我当时并不知道，英文维基百科在 2026 年 3 月通过了一项内容指引：除少数例外，[不得使用大语言模型生成或改写条目内容](#ref-wikipedia-llm-guideline)。我说明了自己的工作方式，道了歉，撤回“你知道吗”（Did You Know）栏目的提名，也暂停了编辑。

我写这些，不是为了抱怨维基百科。那些编辑谨慎、克制，也很讲道理——而且正如后面会说的，在当前条件下，他们的做法是理性的。但理性不等于先进。我仍然惊讶于：到了 2026 年，一个以开放协作著称的知识项目，面对 AI 时首先依赖的仍是一道针对制作过程的禁令。在我看来，它的制度反应已经落在了技术现实后面。

维基百科并不孤单。创业孵化器 Y Combinator 旗下的黑客新闻（Hacker News）在评论规则里同样明令禁止生成文本，连经过 AI 编辑的文字也不接受，理由是：[“HN is for conversation between humans”](#ref-hacker-news-ai-rule)。这条规则不是在处罚一段文字里具体的错误，而是直接把一种制作方式挡在门外。

内容平台的做法则更像一条光谱，不能笼统说成“全面禁 AI”。短视频平台 TikTok [要求对包含写实图像、音频或视频的 AIGC 作出标识](#ref-tiktok-aigc-policy)，并会删除未标识、冒充他人或可能造成伤害性误导的内容。小红书一面欢迎把 AI 当作提高质量和信息价值的创作工具，一面把自动托管账号、造假、侵权和批量生产同质化低质内容列为违规，并可采取[限制分发或封禁账号](#ref-xiaohongshu-ai-governance)。它们也会删除或降权一部分 AI 内容；不同之处在于，公开规则至少试图区分可接受的创作与具体的滥用。

对我而言，问题不在于给 slop 降权，而在于把“用了什么工具”当成质量和责任的替代指标。

真正让我在难堪过后反复琢磨的，是同一周里信息流上两种看似互相矛盾的 AI 叙事。一种说 AI **太危险**：它能寻找安全漏洞、入侵系统，甚至可能帮助人制造生物武器。另一种说 AI 只是 **垃圾内容（slop）**：廉价、粗劣、不可靠，任何认真经营内容的社区都应该见到就拒绝。

既危险得必须严防，又愚蠢得不值一看。怎么会同时成立？

因为我们以前做过一次近似的实验。它始于印刷机，而人类为管理它建立制度，花了几个世纪。

## 威尼斯最早提交了“垃圾内容”投诉

![一支蘸水笔与早期印刷机隔桌相对，成堆的小册子从印刷机中涌出，淹过威尼斯抄写室的桌面](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/01-venice.jpg)

《古腾堡圣经》很可能在 [1455 年末](#ref-loc-gutenberg-bible)于今德国美因茨完成。到 1500 年，欧洲已有[约 250 个地点出现印刷作坊](#ref-dnb-printing-spread)。我们今天熟悉的两种抱怨——危险与劣化——很早就出现了，只是它们并非来自同一个阵营，也不是在同一时刻整齐登场。

关于“垃圾内容”的抱怨，听上去几乎就是今天的原话。15 世纪末，在今意大利威尼斯，[天主教道明会（亦称多明我会；正式名“宣道会”，拉丁文 *Ordo Praedicatorum*，简称 O.P.）](#ref-dominican-order-name)修士兼抄写员斯特拉塔（Filippo da Strada；文献中亦作 Filippo di Strata 或 Filippo de Strata）批评印刷术。

1473 年 8 月，尼科洛·马尔切洛（Nicolò Marcello）当选威尼斯总督。此后不久，斯特拉塔向他呈上一部手抄的《黄金传奇》（*Legenda aurea*）意大利文译本，并在卷首附上一篇拉丁诗，请求禁止在威尼斯从事印刷业。这不是一句孤立的辱骂：他把印刷商比作伪币制造者，指责他们为了利润生产错漏与淫秽作品、败坏青年，也担心抄写员因此失去生计。题目所化用的那句话，就出自[这首呈给总督的诗](#ref-strata-title-quote)：

> [*Est virgo hec penna, meretrix est stampificata.*](#ref-strata-title-quote)
>
> [常见英译](#ref-chartier-writing)：**“The pen is a virgin; the printing press a whore.”**

这里保留原话，不是认同它的性别秩序，而是让它作为一件历史原物呈现在读者面前：手写被塑造成纯洁而克制，印刷则被描绘成逐利而无度。

他的论点不只是印刷术力量太大。他说，为逐利而仓促赶工的版本会败坏文本；不道德和异端作品会逃出教会控制；知识落到他认为没有资格的读者手中，也会因此贬值。历史学家夏蒂埃（Roger Chartier）在[《书写的实际影响》（*The Practical Impact of Writing*）](#ref-chartier-writing)中概括了这套指控（PDF 第 6 页；原书第 123 页）。

二十年后，本笃会修道院长特里特米乌斯（Johannes Trithemius）写了《赞美抄写员》（*De laude scriptorum manualium*）。这部作品写于 1492 年，[1494 年印刷出版](#ref-ddb-de-laude)。人们通常把它讲成一个笑话：反对印刷的人，最后把自己的反印刷宣言送去印了。

真实历史更有意思。特里特米乌斯维护的是手抄作为修道纪律的价值；他[并不从原则上敌视印刷](#ref-brann-monastic-dilemma)。一旦不再强迫他站进现代的“支持技术 / 反对技术”二分法，所谓的虚伪就消失了。

宗教改革期间，“危险”这条指控越来越难以轻视。印刷术没有单独造成宗教改革，但它改变了观点传播的速度、规模，也把一个作者变成可识别的公共人物。1517 年，路德（Martin Luther）还默默无闻；[到 1520 年，他已经是当时在世作者中出版量最高的一位](#ref-uchicago-luther)。芝加哥大学图书馆称他为书籍史上的第一位畅销书作者。

“教会”也并非天然站在印刷机的对面。教会机构本来就是它的早期客户。1454 年，在《古腾堡圣经》尚未完成时，一场教宗赎罪券募款活动便委托古腾堡（Johannes Gutenberg）印制了[数以千计的表格](#ref-princeton-mainz)。后来试图约束这项技术的天主教权威，早已帮助出资并使它成为常态。

所以，印刷机完全可以同时危险而粗劣。这两种判断并不矛盾，它们只是从不同位置描述了同一场经济变化：复制变得更快、更便宜，也更难被任何一家机构控制。

## 禁令，以及禁令实际造成了什么

![盖着红色蜡印的王室敕令像礁石一样立在河中，印刷小册子的洪流从它两侧继续奔涌而过](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/02-bans.jpg)

机构最先伸手去拿的，是一种熟悉的工具：控制生产过程。

法国尝试了最纯粹的版本。1535 年 1 月 13 日，法国国王弗朗索瓦一世（François Ier）颁布敕令，在法国境内全面停止印刷，并威胁把任何擅自印书的人处以绞刑。但那道著名禁令并不是原封不动地维持到所有人承认它荒唐为止。[大约六周后便出现了一道修订命令](#ref-farge-france-ban)（PDF 第 7–8 页；期刊第 179–180 页），把全面禁止改成了对获准印刷商和获准书目的严厉限额。

罗马教廷选择了清单。教宗的《禁书目录》（*Index Librorum Prohibitorum*）[首次颁布于 1559 年](#ref-upenn-index)，此后修订了几个世纪。1966 年，梵蒂冈宣布它[不再具有教会法效力](#ref-vatican-index)，同时仍把这份目录描述为一种道德警示。

英国选择了同业公会与牌照制度。书商公会在 [1557 年的特许状中取得印刷业的独占控制权](#ref-stationers-charter)；后来由 1662 年《印刷法》承载的法定许可制度，在 1695 年到期。即使[法案失效](#ref-cambridge-printing-acts)，书商公会本身也没有随之消失。

这些控制措施并非无害的失败。它们限制印刷商，迫使出版活动转移，有时也确实惩罚人；其中一些维持了几个世纪。它们没能做到的，是让廉价复制重新消失。

开篇那本《邪恶圣经》（*Wicked Bible*）正好说明，禁令之外，质量问题也绝非虚构。一处漏字进入可重复使用的版面，印刷机便能在任何人发现之前把它复制到整批书里。更微妙的是，关于这批书“被销毁”、印刷商“被吊销牌照”的传说，后来也被反复复制。生产先快过校对，传说又快过档案：生成已经比验证更便宜。

## 真正改善信息供给的东西

![正版扉页上的海豚与锚印记和一册粗糙仿本并排放置，中间是一枚用于辨认真伪的放大镜](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/03-anchor.jpg)

没有哪一道禁令驯服了洪水，也没有哪一位英雄式发明家独自解决信任问题。许多做法在不同地方、不同时间逐渐叠加起来：印刷商署名、出版地与日期、特许权、可识别的商标、编辑、勘误表、期刊，最终还有更正式的审查制度。

威尼斯出版家马努提乌斯（Aldus Manutius）提供了最好的象征。他的印刷所推动了斜体字和小开本古典作品的流行。竞争者——尤其是法国里昂的印刷商——制作了[冒牌的阿尔丁版图书](#ref-cambridge-manutius-counterfeits)，有时连他的海豚与锚标志也一并照抄。

这个标志并非单纯的装饰：它把一本书与马努提乌斯的印刷所和校勘声誉联系起来，帮助买家辨认来源。用今天的话说，它确实近似商标；耶鲁法学院图书馆称这类印刷商标志为[“一种商标”](#ref-yale-printers-devices-function)，既是营销工具，也像一则版权声明。

1503 年，马努提乌斯公开发出警告。他列出正版与仿本之间的差异，还附上[一张排印错误清单](#ref-manutius-warning)，让买家可以据此识别赝品。标志本身并非证明——盗版商也能复制——但标志、具名印刷商和可以复核的差异放在一起，构成了一套原始的验证系统。

马努提乌斯并没有发明出版品牌。已知最早的印刷商标志出现在 [1457 年的《美因茨诗篇》](#ref-yale-printers-devices)，比他的警告早了几十年。他真正做到的，是让学术校勘、视觉身份和公开防伪互相加强。

但不能因此把十五世纪写成一个完全没有版权或商标观念的世界。马努提乌斯已经持有威尼斯授予的印刷特许；问题在于，这些权利不是自动产生、普遍适用的财产权，而是政府逐案授予、受期限、对象和疆域限制的垄断。威尼斯早在 [1469 年授予第一项印刷垄断特许，1486 年又出现已知第一项直接授予作者的特许](#ref-sabellico-privilege)。里昂处在威尼斯管辖之外，那里的印刷商并不受[威尼斯元老院授予马努提乌斯的特许](#ref-cambridge-manutius-counterfeits)约束。海豚与锚可以告诉读者“这是谁的书”，却还没有一套稳定而跨境的法律机制阻止别人冒用。

1710 年的《安妮法令》（*Statute of Anne*）通常被视为[世界第一部版权成文法](#ref-statute-anne)。它不是把版权从无到有地发明出来，而是把此前零散的印刷特许、行会规则和书商惯例，推进成具有一般适用性和固定期限的法律。商标也走过相似的道路：商人和印刷商很早就在使用来源标记，现代的全国商标注册制度却要到十九世纪才逐渐形成；法国在 1857 年建立存放制度，英国则由 [1875 年《商标注册法》建立全国统一的注册簿](#ref-modern-trademark-registration)。

所以，更准确的历史因果并不是“先有盗版，后来才发明版权和商标”，而是：**来源标记和有限的排他权已经出现，跨境市场却跑得比统一的权利和执法更快。**

故事另一端也需要同样的校正。1665 年，奥尔登堡（Henry Oldenburg）创办《皇家学会哲学汇刊》（*Philosophical Transactions*），由此建立了一份长寿的科学期刊；现代同行评审并不是在这一刻凭空完成的。皇家学会到 1752 年才引入委员会集体遴选，到 [19 世纪 30 年代才采用更系统的专家同行评审](#ref-royal-society-philosophical-transactions)。从古腾堡到科学期刊，大约用了两个世纪；到系统化的专家评审，则接近四个世纪。

这个更慢的时间表很重要。信任基础设施从来不是一次设计完成的，它是在每项解决方案暴露出新的失败方式之后逐层堆积起来。商标可以伪造，特许权可以变成审查，编辑可能漏掉错误，期刊也可能保护一个封闭的小圈子。整个系统之所以改善，恰恰因为任何一个组件单独拿出来都不够。

从这个意义上说，维基百科也是同一传统的后代。可验证性、引用来源、修订记录和具名问责，就是被改造成公共协议的“海豚与锚”。

## 两种恐慌背后的经济学

![印刷机喷涌出纸页洪流，旁边仅有一张阅读桌，一页纸在放大镜和暖光灯下等待缓慢核查](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/04-economics.jpg)

如果从 1500 年回望，我们眼前的悖论就会消失。“危险”和“垃圾”不是对质量作出的两种矛盾判断，而是同一场经济事件的两个后果：**一种技术抬高了能力上限，同时把生产的边际成本砸向地板。**

强而昂贵，像一件由军需官看管的武器。弱而便宜，只是遍地垃圾。强而便宜，则会同时触发两套免疫系统：安全专家看见的是能力上限，内容社区看见的是洪水。

两种恐慌面对同一个瓶颈：生成变便宜了，验证依然昂贵。

维基百科依靠志愿者完成验证。当 AI 把生成貌似可信、带着引用外观的文字成本降下来时，志愿者的核查能力并没有同步上升。发现我那处错误的编辑，必须打开学术论文，把条目中的说法和相关章节逐一对照。我的草稿因为 AI 而变便宜，并没有让这项工作也随之变便宜。

所以，英文维基百科的规则比“AI 很坏”具体得多。它是在限制一种可能把无上限核查成本转嫁给别人的生产过程。按照这个项目目前的成本结构，这是一条理性的规则。历史只是提醒我们：禁止某个过程，通常不会是最终均衡。

## 海豚与锚旁边的空位

![印刷工坊的空椅旁放着一枚海豚与锚手印，木制工作台的纹理逐渐化作电路走线](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/05-empty-seat.jpg)

抄写员并没有简单地消失。早期印刷书仍需要手工描红和插图，手抄本艺术家也继续为偏爱[色彩华丽奢侈书籍](#ref-princeton-illumination)的赞助人工作。失去价值的是大规模的例行复制；判断、校正、排印和装帧，则迁移进新的职业形态。

今天的 AI 辅助工作，还没有一枚被普遍接受的“海豚与锚”：没有一种便宜、标准、难以伪造的方法，能表明**这项主张由这个需要负责的人，对照这个来源核查过**。我曾以一种业余的方式，假装这样的制度已经存在。我联系引用论文的作者，请他们检查我有没有准确转述他们的研究。结果仍有一处真实错误穿了过去。这恰好说明问题有多难。

我们缺少的产品不是另一台生成器，而是账本的核查侧：出处、逐项事实审查、可见的修正、具名签署，以及让陌生人不必重做整套研究便能审计这一切的工具。

印刷机从未变得无害，印刷品也从未变得干净。真正改变的，是我们判断一段文字背后站着谁、它来自哪里、哪里改过、又该如何质疑它的成本。AI 也需要自己的这一整套基础设施。

空位不在下一台印刷机旁，而在那枚锚旁。

## 来源与延伸阅读

- <span id="ref-wikipedia-ai-noticeboard"></span>英文维基百科 — 原始来源：[AI noticeboard: “Easy-to-cancel mandate”](https://en.wikipedia.org/wiki/Wikipedia:AI_noticeboard#Easy-to-cancel_mandate)。原文：“using AI to generate almost 90-95% of the new lines of code” — fetched [2026-08-20](https://web.archive.org/web/20260817234253/https://en.wikipedia.org/wiki/Wikipedia:AI_noticeboard)
- <span id="ref-wikipedia-llm-guideline"></span>英文维基百科 — 原始来源：[Writing articles with large language models](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models#:~:text=the%20use%20of%20LLMs%20to%20generate%20or%20rewrite%20article%20content%20is%20prohibited) — fetched [2026-08-20](https://web.archive.org/web/20260817234323/https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models)
- <span id="ref-hacker-news-ai-rule"></span>黑客新闻（Hacker News）— 原始来源：[Hacker News Guidelines](https://news.ycombinator.com/newsguidelines.html#generated)。原文：“Don't post generated text or AI-edited text. HN is for conversation between humans.” — fetched [2026-08-20](https://web.archive.org/web/20260815185918/https://news.ycombinator.com/newsguidelines.html)
- <span id="ref-tiktok-aigc-policy"></span>TikTok — 原始来源：[AI-generated content](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content#:~:text=We%20also%20require%20creators%20to%20label%20all%20AI-generated%20content)。原文：“We also require creators to label all AI-generated content that contains realistic images, audio, and video.” — fetched [2026-08-20](https://web.archive.org/web/20260809142917/https://www.tiktok.com/support/faq_detail?id=7636670084747893268)
- <span id="ref-xiaohongshu-ai-governance"></span>新浪科技 — 原始来源：[小红书发布 AI 治理规则公告](https://finance.sina.com.cn/2026-04-27/doc-inhvxtre9124679.shtml#:~:text=AI低质：套用模板批量生产同质化内容)。原文：“平台欢迎创作者以AI为创意工具，提升内容质量与信息价值”；违规行为可被“限制分发、封禁账号” — fetched [2026-08-20](https://web.archive.org/web/20260818000000/https://finance.sina.com.cn/2026-04-27/doc-inhvxtre9124679.shtml)
- <span id="ref-loc-gutenberg-bible"></span>美国国会图书馆 — 原始来源：[The Gutenberg Bible](https://www.loc.gov/exhibits/bibles/the-gutenberg-bible.html#:~:text=The%20printing%20of%20the%20Bible%20was%20probably%20completed%20late%20in%201455) — fetched [2026-08-20](https://web.archive.org/web/20260817234136/https://www.loc.gov/exhibits/bibles/the-gutenberg-bible.html)
- <span id="ref-dnb-printing-spread"></span>德国书籍与文字博物馆 — 原始来源：[Spread of printing](https://mediengeschichte.dnb.de/DBSMZBN/Content/EN/Printing/04-ausbreitung-des-buchdrucks-en.html#:~:text=By%201500%20printing%20offizins%20had%20emerged%20at%20around%20250%20locations) — fetched [2026-08-20](https://web.archive.org/web/20260817234356/https://mediengeschichte.dnb.de/DBSMZBN/Content/EN/Printing/04-ausbreitung-des-buchdrucks-en.html)
- <span id="ref-dominican-order-name"></span>何雅钦，《公教报》（天主教香港教区周报）— 原始来源：[《道明会的神恩（上）》](https://kkp.org.hk/past/detail/51094/#:~:text=%E8%81%96%E9%81%93%E6%98%8E%E6%89%80%E5%89%B5%E7%AB%8B%E7%9A%84%E3%80%8C%E9%81%93%E6%98%8E%E6%9C%83%E3%80%8D%E5%8F%88%E5%8F%AF%E8%AD%AF%E7%82%BA%E3%80%8C%E5%A4%9A%E6%98%8E%E6%88%91%E6%9C%83%E3%80%8D)，文中说明“道明会”亦译“多明我会”，正式名称为“宣道会”（*Ordo Praedicatorum*，O.P.）— fetched [2026-08-20](https://web.archive.org/web/20260820192205/https://kkp.org.hk/past/detail/51094/)
- <span id="ref-strata-title-quote"></span>佩特雷拉（Giancarlo Petrella）— 原始来源：[“Domenicani contro l’arte della stampa: Non comprate quei libri!”](https://bibliotecadiviasenato.it/wp-content/uploads/BVS_N12_DICEMBRE_2022-web_abbass.pdf#page=30)，载 *la Biblioteca di via Senato Milano*，2022 年 12 月。身份、呈递背景见 PDF 第 29 页（刊物第 27 页，约全文 27%）；禁印请求与引文见 PDF 第 30 页（刊物第 28 页，约全文 28%）。该文将文本定位为威尼斯马尔恰纳国家图书馆（Biblioteca Nazionale Marciana）手稿 It. I 72，原文：“Est virgo hec penna, meretrix est stampificata.” — fetched [2026-08-20](https://web.archive.org/web/20230209030303/https://bibliotecadiviasenato.it/wp-content/uploads/BVS_N12_DICEMBRE_2022-web_abbass.pdf)。另见菊池（Catherine Kikuchi）的[手稿书目信息与异文](https://arche.unistra.fr/websites/arche/Productions/Publications/Source_s/Numeros_et_couvertures/sources_13_web.pdf#page=24)，PDF 第 24 页（刊物第 23 页，约全文 11%），定位至 Marciana, Mss. Italiani, cl. I, cod. 72, n° 5054, fol. 2r，并转写作 “meretrix que est stampificata” — fetched [2026-08-20](https://web.archive.org/web/20260820192504/https://arche.unistra.fr/websites/arche/Productions/Publications/Source_s/Numeros_et_couvertures/sources_13_web.pdf)
- <span id="ref-chartier-writing"></span>夏蒂埃（Roger Chartier）— 原始来源：[“The Practical Impact of Writing”](https://users.manchester.edu/Facstaff/SSNaragon/Online/LP/Readings/11-Chartier%2C%20Practical%20Impact%20of%20Writing%20%28abridged%29.pdf#page=6)，PDF 第 6 页；原书第 123 页。原文：“The pen is a virgin, the printing press a whore”；“texts, which were circulated in hastily manufactured, faulty editions composed solely for profit.” — fetched [2026-08-20](https://web.archive.org/web/20260817234425/https://users.manchester.edu/Facstaff/SSNaragon/Online/LP/Readings/11-Chartier%2C%20Practical%20Impact%20of%20Writing%20%28abridged%29.pdf)
- <span id="ref-brann-monastic-dilemma"></span>Noel L. Brann — 原始来源：[“A Monastic Dilemma Posed by the Invention of Printing”](https://www.journals.uc.edu/index.php/vl/article/view/5268) — fetched [2026-08-20](https://web.archive.org/web/20260817234438/https://www.journals.uc.edu/index.php/vl/article/view/5268)
- <span id="ref-ddb-de-laude"></span>德国数字图书馆 — 原始来源：[*De laude scriptorum* bibliographic record](https://www.deutsche-digitale-bibliothek.de/item/Y7EKMZBKNWE5OYMA2SIROTFG2PWURZV4) — fetched [2026-08-20](https://web.archive.org/web/20260817234501/https://www.deutsche-digitale-bibliothek.de/item/Y7EKMZBKNWE5OYMA2SIROTFG2PWURZV4)
- <span id="ref-uchicago-luther"></span>芝加哥大学图书馆 — 原始来源：[Martin Luther as print media’s first influencer](https://www.lib.uchicago.edu/collex/exhibits/media-revolutions-then-now-martin-luther-and-the-making-of-modern-communication/type-casting-selves/#:~:text=Unknown%20in%201517%2C%20by%201520%20he%20was%20the%20most%20published%20author) — fetched [2026-08-20](https://web.archive.org/web/20260817234534/https://www.lib.uchicago.edu/collex/exhibits/media-revolutions-then-now-martin-luther-and-the-making-of-modern-communication/type-casting-selves/)
- <span id="ref-princeton-mainz"></span>普林斯顿大学图书馆 — 原始来源：[The beginning of printing in Mainz](https://dpul.princeton.edu/gutenberg/feature/the-beginning-of-printing-in-mainz#:~:text=presumably%20thousands%20of%20such%20forms%20were%20printed) — fetched [2026-08-20](https://web.archive.org/web/20260817234602/https://dpul.princeton.edu/gutenberg/feature/the-beginning-of-printing-in-mainz)
- <span id="ref-farge-france-ban"></span>James K. Farge — 原始来源：[“The University of Paris, the Parlement of Paris, and the French Reformation”](https://jps.library.utoronto.ca/index.php/renref/article/download/12038/8915#page=7)，PDF 第 7–8 页；期刊第 179–180 页。原文：“no one, under pain of death by hanging, is hereafter to print … any book”；“He ordered the Parlement to designate twenty-four printers.” — fetched [2026-08-20](https://web.archive.org/web/20260817234627/https://jps.library.utoronto.ca/index.php/renref/article/download/12038/8915)
- <span id="ref-stationers-charter"></span>Primary Sources on Copyright — 原始来源：[The Stationers’ Company charter](https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=record_uk_1557) — fetched [2026-08-20](https://web.archive.org/web/20260817234650/https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=record_uk_1557)
- <span id="ref-cambridge-printing-acts"></span>剑桥大学出版社 — 原始来源：[The Stationers and the Printing Acts at the end of the seventeenth century](https://www.cambridge.org/core/books/abs/cambridge-history-of-the-book-in-britain/stationers-and-the-printing-acts-at-the-end-of-the-seventeenth-century/4999BBB8F8581DE94B9C2AAD75A01D75) — fetched [2026-08-20](https://web.archive.org/web/20260817234716/https://www.cambridge.org/core/books/abs/cambridge-history-of-the-book-in-britain/stationers-and-the-printing-acts-at-the-end-of-the-seventeenth-century/4999BBB8F8581DE94B9C2AAD75A01D75)
- <span id="ref-upenn-index"></span>宾夕法尼亚大学图书馆 — 原始来源：[The *Index Librorum Prohibitorum*](https://specialcollectionsprocessing.exhibits.library.upenn.edu/exhibits/show/bythebook/library_rules#:~:text=The%20Index%20librorum%20prohibitorum%20was%20first%20issued%20in%201559) — fetched [2026-08-20](https://web.archive.org/web/20260817234804/https://specialcollectionsprocessing.exhibits.library.upenn.edu/exhibits/show/bythebook/library_rules)
- <span id="ref-vatican-index"></span>梵蒂冈信理部 — 原始来源：[1966 notification regarding the Index](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_19660614_de-indicis-libr-prohib_en.html#:~:text=it%20no%20longer%20has%20the%20force%20of%20ecclesiastical%20law) — fetched [2026-08-20](https://web.archive.org/web/20260817234825/https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_19660614_de-indicis-libr-prohib_en.html)
- <span id="ref-moseley-wicked-bible"></span>莫斯利（David Moseley），坎特伯雷大学 — 原始来源：[*“Not” Funny? Humour, Embarrassment, and the “Wicked Bible”*](https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content#page=18)，论文第 17–18、54 页（PDF 文件第 18–19、55 页）。原文：“There is however no evidence that the Bibles were ordered to be destroyed”；“the printers did not lose their licence”；“the £300 fine … be remitted.” — fetched [2026-08-20](https://web.archive.org/web/20260813145200/https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content)
- <span id="ref-cambridge-manutius-counterfeits"></span>剑桥大学图书馆 — 原始来源：[Enchiridia, counterfeits, and the dolphin-and-anchor device](https://exhibitions.lib.cam.ac.uk/manutius/case/enchiridia/#:~:text=counterfeit%20editions%20by%20both%20Italian%20and%20foreign%20competitors) — fetched [2026-08-20](https://web.archive.org/web/20260211181353/https://exhibitions.lib.cam.ac.uk/manutius/case/enchiridia/)
- <span id="ref-manutius-warning"></span>Primary Sources on Copyright — 原始来源：[Aldus Manutius’s warning against the printers of Lyon](https://copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_i_1503#:~:text=He%20even%20furnishes%20a%20list%20of%20typographical%20errors) — fetched [2026-08-20](https://web.archive.org/web/20260817234940/https://copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_i_1503)
- <span id="ref-yale-printers-devices-function"></span>耶鲁大学法学院图书馆 — 原始来源：[Printers’ devices as source marks](https://library.law.yale.edu/news/printers-devices-law-books#:~:text=A%20printer%E2%80%99s%20device%20is%20a%20trademark%20of%20sorts)。原文：“A printer’s device is a trademark of sorts, serving both as a marketing tool and a copyright notice of sorts” — fetched [2026-08-20](https://web.archive.org/web/20260817235011/https://library.law.yale.edu/news/printers-devices-law-books)
- <span id="ref-yale-printers-devices"></span>耶鲁大学法学院图书馆 — 原始来源：[Printers’ devices from law books](https://library.law.yale.edu/news/printers-devices-law-books#:~:text=The%20very%20first%20printer%E2%80%99s%20device) — fetched [2026-08-20](https://web.archive.org/web/20260817235011/https://library.law.yale.edu/news/printers-devices-law-books)
- <span id="ref-sabellico-privilege"></span>科斯蒂洛（Joanna Kostylo），Primary Sources on Copyright — 原始来源：[Commentary on Marcantonio Sabellico’s privilege (1486)：1469 年印刷垄断与 1486 年作者特许](https://www.copyrighthistory.org/cam/commentary/i_1486/i_1486_com_2162008205354.html#:~:text=The%20printing%20monopoly%20granted%20to%20Johannes%20of%20Speyer%20in%201469)；[特许权的性质](https://www.copyrighthistory.org/cam/commentary/i_1486/i_1486_com_2162008205354.html#:~:text=In%20contrast%20to%20modern%20copyright%2C%20printing%20privileges%20were%20not%20conceived%20as%20the%20inherent%20right)。原文：“the first known privilege to an author”；“printing privileges were not conceived as the inherent right” — fetched [2026-08-20](https://web.archive.org/web/20260514232223/https://www.copyrighthistory.org/cam/commentary/i_1486/i_1486_com_2162008205354.html)
- <span id="ref-statute-anne"></span>德兹利（Ronan Deazley），Primary Sources on Copyright — 原始来源：[Commentary on the Statute of Anne 1710](https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_uk_1710#:~:text=on%205%20April%201710%2C%20the%20world%27s%20first%20copyright%20statute%20was%20passed)。原文：“the world's first copyright statute was passed”；法令规定新书专有权的首个期限为 14 年 — fetched [2026-08-20](https://web.archive.org/web/20241013225756/https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_uk_1710)
- <span id="ref-modern-trademark-registration"></span>英国知识产权局 — 原始来源：[The red triangle that made history: celebrating 150 years of UK trade mark no. 1](https://ipo.blog.gov.uk/2026/01/08/the-red-triangle-that-made-history-celebrating-150-years-of-uk-trade-mark-no-1/#:~:text=France%20introduced%20a%20deposit%20system%20in%201857)。原文：“France introduced a deposit system in 1857”；英国 1875 年法令建立了 “a systematic, nationally centralised register” — fetched [2026-08-20](https://web.archive.org/web/20260421133909/https://ipo.blog.gov.uk/2026/01/08/the-red-triangle-that-made-history-celebrating-150-years-of-uk-trade-mark-no-1/)
- <span id="ref-royal-society-philosophical-transactions"></span>英国皇家学会 — 原始来源：[History of *Philosophical Transactions*](https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/#:~:text=The%20Royal%20Society%20responded%20by%20introducing%20more%20rigorous%20and%20systematic%20expert%20peer%20review) — fetched [2026-08-20](https://web.archive.org/web/20260609032321/https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/)
- <span id="ref-princeton-illumination"></span>普林斯顿大学图书馆 — 原始来源：[Inside the Milberg Gallery: Illumination](https://library.princeton.edu/about/library-news/2019/inside-milberg-gallery-illumination#:~:text=continued%20to%20find%20work%20for%20patrons%20with%20a%20taste%20for%20brilliantly%20colored%20luxury%20books) — fetched [2026-08-20](https://web.archive.org/web/20251220020759/https://library.princeton.edu/about/library-news/2019/inside-milberg-gallery-illumination)

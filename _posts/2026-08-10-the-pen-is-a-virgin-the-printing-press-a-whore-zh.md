---
title: "翰墨贞洁、铅梓荒淫"
excerpt: "回看五百年前围绕印刷术的争论，许多场景似曾相识。未来究竟会怎样？历史或许能提供一些启发；也可能，这一次不同。"
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

1631 年，英格兰伦敦的一部英文《圣经》在第七诫里漏掉了一个只有三个字母的词：*not*。负责这批书的御用印刷商巴克（Robert Barker）和卢卡斯（Martin Lucas）被判罚 300 英镑，书也遭到扣押。几百年里，故事越讲越狠：这一版书被尽数销毁，两人的印刷牌照也被吊销。[现存档案与这些后来的说法并不相同](#ref-moseley-wicked-bible)。

[档案却记录了另一个结局](#ref-moseley-wicked-bible)：扣押的书后来退回给印刷商修正；他们没有失去牌照；300 英镑罚款也以自费建立希腊文印刷所为条件获免。那个漏掉的 *not* 是真的，后来附着其上的严惩故事却是传说。

这段历史里先后发生了两种传播：印刷机成批复制了漏字，后来的转述又反复复制了档案不支持的惩罚情节。

## 五百年后，一场争论让我想起印刷史

前几天，我在 AI 时代的一场争论里，以一种不太舒服的方式想起了这个故事。

我在英文维基百科创建了一篇题为《“容易取消”规定》（*Easy-to-cancel mandate*）的条目，讨论一类要求“取消订阅必须像开通订阅一样容易”的法律。后来，这篇条目被提交到维基百科的 [人工智能公告板（AI noticeboard）](#ref-wikipedia-ai-noticeboard)。编辑们怀疑我借助了 AI 起草，事实也确实如此。其中一位编辑核对引用时发现了一处措辞上的瑕疵：稿件中某项“两步取消”要求本来已由德国法律确立，我的写法却可能让人误以为，那是研究者自行设定的测试标准。

我本来就无意隐瞒——甚至觉得，到了 2026 年，写作时使用 AI 辅助，难道不已经是默认了吗？作为软件工程师，我的工作流早已从自动补全（auto-complete），逐步走到让 AI 修正语法和拼写、重构代码、生成单个文件与测试；到 2023—2025 年，它已经参与我大部分代码库的生成和新项目的规划。

我在公告板上甚至给出了一个直白的数字：[新增代码行中“almost 90–95%”由 AI 生成](#ref-wikipedia-ai-noticeboard)。那句话现在看并不精确：90–95% 不是逐行统计出来的字符比例，而是我按信息生产过程中投入的“劳动时间”作出的粗略估算。我花大约一分钟写提示词，AI 往往接着运行十到二十分钟；按这个口径，绝大部分时间发生在机器一侧。如果改按最终文本或代码的字符量计算，我估计 AI 生成的部分超过 99%——毕竟它生成文字远比人快。

这篇条目的制作方式也是如此：我向 Claude Code 和 Codex 下指令，让它们研究、引注和事实核查；发现问题时，我通常修改提示、要求继续修订，而不是直接改写输出。我把文章先放在草稿命名空间，主动向相关维基专题寻求编辑审阅和指导，得到反馈后才移入条目空间；连草稿讨论页也借助了 LLM。问题不是我藏起了 AI，而是我没有意识到，这个社区已经对这种制作过程本身划下了一条新界线。

我当时并不知道，英文维基百科在 2026 年 3 月通过了一项内容指引：除少数例外，[不得使用大语言模型生成或改写条目内容](#ref-wikipedia-llm-guideline)。我说明了自己的工作方式，道了歉，撤回“你知道吗”（Did You Know）栏目的提名，也暂停了编辑。

我写这些，不是为了抱怨维基百科。那些编辑谨慎、克制，也很讲道理。公告板上的编辑关注的是：对依靠志愿者核查来源的社区来说，大量迅速生成、外观可信的文字可能把审阅成本转嫁给别人；从这个位置看，限制制作过程是在保护稀缺的编辑时间。站在我的位置，AI 辅助早已成为日常工作流，我原以为主动披露、逐项引注和接受审阅，比是否使用某种工具更重要。这场争论涉及的不只是 AI 好不好，也包括谁应当承担验证成本，以及怎样留下可以追责的编辑记录。

维基百科并不孤单。创业孵化器 Y Combinator 旗下的黑客新闻（Hacker News）在评论规则里同样明令禁止生成文本，连经过 AI 编辑的文字也不接受，理由是：[“HN is for conversation between humans”](#ref-hacker-news-ai-rule)。这项规则优先保护人与人交谈的场合，因此直接以制作方式划界，而不是逐条判断生成文字的质量。

内容平台采用了不同的划线方式。短视频平台 TikTok [要求对包含写实图像、音频或视频的 AIGC 作出标识](#ref-tiktok-aigc-policy)，鼓励标识完全生成或经过显著 AI 编辑的其他内容；违反社区规则、构成有害误导或未按要求标识的内容可能被移除，某些人物冒充类内容即使标识也不允许发布。小红书一面欢迎把 AI 当作提高质量和信息价值的创作工具，一面把自动托管账号、造假、侵权和批量生产同质化低质内容列为违规，并可采取[限制分发或封禁账号](#ref-xiaohongshu-ai-governance)。这些规则分别以制作过程、身份披露、内容风险或分发后果作为判断标准。

真正让我在难堪过后反复琢磨的，是同一周里信息流上两种看似互相矛盾的 AI 叙事。一种强调 AI **太危险**。2026 年《国际人工智能安全报告》（*International AI Safety Report*）认为，通用 AI 已能协助发现软件漏洞和编写恶意代码，也可能提供与生化武器开发有关的技术信息；报告同时反复提醒，这些能力究竟把现实风险提高了多少，[仍有很大不确定性](#ref-international-ai-safety-report)。另一种批评则把 AI 内容称为 **垃圾内容（slop）**：廉价、粗劣、不可靠，并且把筛选与核查的压力留给接收者。

既危险得必须严防，又愚蠢得不值一看。怎么会同时成立？

把这组争论放到印刷术的历史旁边，并不能证明 AI 会重演同一条道路。它至少提供了一批可以比较的材料：新工具出现后，谁感到受威胁，谁从中获益，各类机构又尝试了什么办法。

## 威尼斯的一场早期印刷争论

![一支蘸水笔与早期印刷机隔桌相对，成堆的小册子从印刷机中涌出，淹过威尼斯抄写室的桌面](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/01-venice.jpg)

《古腾堡圣经》很可能在 [1455 年末](#ref-loc-gutenberg-bible)于今德国美因茨完成。到 1500 年，欧洲已有[约 250 个地点出现印刷作坊](#ref-dnb-printing-spread)。我们今天熟悉的两种抱怨——危险与劣化——很早就出现了，只是它们并非来自同一个阵营，也不是在同一时刻整齐登场。

关于粗劣印刷品的抱怨，很早便出现在今意大利威尼斯。15 世纪 70 年代，[天主教道明会（亦称多明我会；正式名“宣道会”，拉丁文 *Ordo Praedicatorum*，简称 O.P.）](#ref-dominican-order-name)修士兼抄写员[斯特拉塔（Filippo da Strada；文献中亦作 Filippo di Strata 或 Filippo de Strata）](#ref-strata-title-quote)批评印刷术。

1473 年 8 月，尼科洛·马尔切洛（Nicolò Marcello）当选威尼斯总督。此后不久，斯特拉塔向他呈上一部手抄的《黄金传奇》（*Legenda aurea*）意大利文译本，并在卷首附上一篇拉丁诗，请求禁止在威尼斯从事印刷业。这不是一句孤立的辱骂：他把印刷商比作伪币制造者，指责他们为了利润生产错漏与淫秽作品、败坏青年，也担心抄写员因此失去生计。题目所化用的那句话，就出自[这首呈给总督的诗](#ref-strata-title-quote)：

> [*Est virgo hec penna, meretrix est stampificata.*](#ref-strata-title-quote)
>
> 通常在[英文里被译为](#ref-chartier-writing)：**“The pen is a virgin, the printing press a whore.”**

这里保留原话，不是认同它的性别秩序，而是让它作为一件历史原物呈现在读者面前：手写被塑造成纯洁而克制，印刷则被描绘成逐利而无度。

他的论点不只是印刷术力量太大。他说，为逐利而仓促赶工的版本会败坏文本；不道德和异端作品会逃出教会控制；知识落到他认为没有资格的读者手中，也会因此贬值。历史学家夏蒂埃（Roger Chartier）在[《书写的实际影响》（*The Practical Impact of Writing*）](#ref-chartier-writing)中概括了这套指控。

二十年后，本笃会修道院长特里特米乌斯（Johannes Trithemius）写了《赞美抄写员》（*De laude scriptorum manualium*）。这部作品[写于 1492 年](#ref-brann-monastic-dilemma)，1494 年在[今德国美因茨印刷出版](#ref-ddb-de-laude)。人们通常把它讲成一个笑话：反对印刷的人，最后把自己的反印刷宣言送去印了。

但这层反讽省略了作品的具体场合。特里特米乌斯维护的是手抄作为修道纪律的价值；研究者布兰（Noel L. Brann）指出，他[并不从原则上敌视印刷](#ref-brann-monastic-dilemma)，反而把印刷看成传播修道学问的工具。《赞美抄写员》针对的是修士是否还应继续抄写，而不是一项要求全社会弃用印刷的主张。

批评也不只来自以手抄为业的人。人文学者伊拉斯谟（Desiderius Erasmus）深度参与印刷出版：1508 年，他在威尼斯与马努提乌斯合作扩充《格言集》（*Adagiorum chiliades*）。在其中“欲速则不达”（*Festina lente*）一条的评注里，他先赞扬阿尔丁印刷所扩大古典学问的传播，随后又攻击那些宁愿让好书塞满六千处错误、也不肯花钱请人校样的印刷商，并抱怨“成群的新书”及其数量[有害于学术](#ref-willinsky-erasmus)。他同时是印刷传播的受益者、参与者和批评者。

宗教改革期间，关于印刷术政治与宗教影响的争论有了新的现实背景。印刷术并非宗教改革的单一原因；在路德（Martin Luther）身上，可以直接看到出版数量和公共身份的迅速变化。1517 年，他还默默无闻；[到 1520 年，他已经是当时出版量最高的作者](#ref-uchicago-luther)。芝加哥大学图书馆称他为书籍史上的第一位畅销书作者。

宗教权威与印刷的关系也不只有抵制。1454 年，在《古腾堡圣经》尚未完成时，教宗赎罪券募款活动的组织者便委托古腾堡（Johannes Gutenberg）印制了[可能数以千计的表格](#ref-princeton-mainz)。同一宗教体系既在早年委托印刷，后来也对印刷内容设限。

这些材料呈现的并不是一个整齐划分的“支持印刷”或“反对印刷”阵营。斯特拉塔关心文本质量、宗教道德和抄写员的生计；特里特米乌斯关心修道实践；路德及其支持者利用印刷扩大传播；教会机构既购买印刷品，也试图约束它。不同参与者所说的“危险”或“粗劣”，指向的风险、利益与责任并不相同。

## 各地如何约束印刷

![盖着红色蜡印的王室敕令像礁石一样立在河中，印刷小册子的洪流从它两侧继续奔涌而过](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/02-bans.jpg)

面对迅速增加的印刷活动，欧洲的王权、教会和同业组织采用过禁令、书目审查、特许与牌照等不同办法。

法国一度采用非常严厉的方案。1535 年 1 月 13 日，法国国王弗朗索瓦一世（François Ier）颁布敕令，在法国境内全面停止印刷，并威胁把任何擅自印书的人处以绞刑。[大约六周后便出现了一道修订命令](#ref-farge-france-ban)，把全面禁止改成了对获准印刷商和获准书目的严厉限额。

罗马教廷选择了清单。教宗的《禁书目录》（*Index Librorum Prohibitorum*）[首次颁布于 1559 年](#ref-upenn-index)，此后修订了几个世纪。1966 年，梵蒂冈宣布它[不再具有教会法效力](#ref-vatican-index)，同时仍把这份目录描述为一种道德警示。

英格兰选择了同业公会与牌照制度。书商公会在 [1557 年的特许状中取得英格兰印刷业的独占控制权](#ref-stationers-charter)；1662 年《印刷法》（*Printing Act*，后世也常称 *Licensing Act*）建立的法定许可制度，曾到期又恢复，最后在 [1695 年失效](#ref-cambridge-printing-acts)。

这三种制度的存续时间并不相同：法国的全面禁令大约六周便被修订；英格兰的法定许可制度在 1695 年失效；罗马教廷的目录直到 1966 年才失去教会法效力。把它们统称为“禁令”，容易遮住各自不同的对象、执行方式与寿命。

开篇那本《邪恶圣经》（*Wicked Bible*）正好说明，禁令之外，质量问题也绝非虚构。一处漏字进入可重复使用的版面，印刷机便能在任何人发现之前把它复制到整批书里。更微妙的是，关于这批书“被销毁”、印刷商“被吊销牌照”的传说，后来也被反复转述。在这一事件里，错误先被成批复制；发现、修正与追溯都发生在传播之后。

## 印刷世界逐渐形成的制度

![正版扉页上的海豚与锚印记和一册粗糙仿本并排放置，中间是一枚用于辨认真伪的放大镜](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/03-anchor.jpg)

在禁令和牌照之外，印刷世界还逐渐形成了另一批做法：印刷商署名、出版地与日期、特许权、可识别的标志、期刊，以及后来更正式的审稿程序。这些制度有的帮助读者判断来源，有的保护商业利益，有的服务于行政管理或审查；同一种制度也可能同时承担几种功能。

今意大利威尼斯的出版家马努提乌斯（Aldus Manutius）提供了一个具体案例。他的印刷所从 1501 年起推出以斜体字排印的袖珍本（*enchiridia*），收录拉丁、希腊古典作者和意大利俗语诗人；剑桥大学图书馆称这是他[最成功的编辑创新](#ref-cambridge-manutius)。竞争者——尤其是法国里昂的印刷商——制作了冒牌的阿尔丁版图书；一部仿冒 1502 年但丁版本的里昂印本，[连海豚与锚标志也试图照抄](#ref-cambridge-manutius-counterfeits)。

海豚与锚印在阿尔丁版图书上，标明它与马努提乌斯印刷所的关联。耶鲁法学院图书馆把这类印刷商标志称为[“一种商标”](#ref-yale-printers-devices)：它既用来营销，也像一则版权声明。

1503 年，马努提乌斯公开发出警告。他列出正版与仿本之间的差异，还附上[一张排印错误清单](#ref-manutius-warning)，让买家可以据此识别赝品。标志本身并非证明——仿冒者也能复制——但买家至少可以同时核对标志、印刷商、出版地、日期、纸张、字体和具体错字。

马努提乌斯并没有发明印刷商标志。已知最早的实例出现在 [1457 年的《美因茨诗篇》](#ref-yale-printers-devices)，比他的警告早了几十年；海豚与锚只是后来影响很大的一个实例。

但不能因此把十五世纪写成一个完全没有版权或商标观念的世界。马努提乌斯已经持有威尼斯授予的印刷特许；这些权利不是自动产生、普遍适用的财产权，而是政府逐案授予、受期限、对象和疆域限制的垄断。威尼斯早在 [1469 年授予第一项印刷垄断特许，1486 年又出现已知第一项直接授予作者的特许](#ref-sabellico-privilege)。[剑桥展览的说明](#ref-cambridge-manutius-counterfeits)特别指出，里昂的竞争者处在威尼斯疆域和马努提乌斯特许的适用范围之外；仿本仍在法国被印出，海豚与锚标志也遭到仿冒。

1710 年的《安妮法令》（*Statute of Anne*）通常被视为[世界第一部版权成文法](#ref-statute-anne)。与旧制度相比，法令允许书商公会成员之外的作者或受让人持有书籍复制权，并给尚未出版的新书规定了十四年的初始期限。商人和印刷商此前已经使用来源标记；现代的全国商标注册制度则到十九世纪才逐渐形成。法国在 1857 年建立商标存放制度，英国由 [1875 年《商标注册法》建立全国统一的注册簿](#ref-modern-trademark-registration)。

因此，来源标记和有限的排他权早于全国注册制度和一般版权法；早期特许的范围、期限与跨境执行能力仍很有限。

故事另一端也需要同样的校正。1665 年，奥尔登堡（Henry Oldenburg）创办《皇家学会哲学汇刊》（*Philosophical Transactions*），由此建立了一份长寿的科学期刊；现代同行评审并不是在这一刻凭空完成的。皇家学会到 1752 年才引入委员会集体遴选，到 [19 世纪 30 年代才采用更系统的专家同行评审](#ref-royal-society-philosophical-transactions)。从古腾堡到科学期刊，大约用了两个世纪；到系统化的专家评审，则接近四个世纪。

这些做法并非一次设计完成，也没有消除所有问题：印刷标志可以被仿冒，特许权既用于保护投资也用于管制印刷，编辑仍会漏掉错误，皇家学会的集体遴选与系统化专家评审也相隔近一个世纪。

## 抄写员后来做了什么

![印刷工坊的空椅旁放着一枚海豚与锚手印，木制工作台的纹理逐渐化作电路走线](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/05-empty-seat.jpg)

抄写员并没有在印刷机出现后同时消失。以英格兰为例，剑桥大学出版社的一部文学史概括说，在卡克斯顿（William Caxton）1476 年于威斯敏斯特开设印刷所后的许多年里，多数文本仍通过手写和口述“出版”；印刷较适合篇幅较长、需求量较大的文本，短篇和面向专门读者的文本仍常由笔来传播。识字人口增加时，[两套生产方式一度同时扩张](#ref-cambridge-manuscript-print)，并不只是新技术立即挤掉旧技术。

早期印本本身也没有完全离开手工劳动。印刷商会为首字母和红字留下空白，再由人手描红或装饰；普林斯顿大学图书馆还记录到，原先为手抄本作画的艺术家继续替偏爱[华丽奢侈书籍](#ref-princeton-illumination)的赞助人工作，无论书中文字是手写还是印刷。到了 1470 年代，木刻首字母和印刷标题逐渐减少了部分手工描红的需要，但并未在一个时间点消灭整套职业。

这些材料能够证明共存、分工和市场变化，却不足以支持一个过于整齐的结局，例如“抄写员普遍转行做了校对员和排字师”。不同地区的修道院、行政机构、商业书坊和奢侈品市场经历并不相同；英格兰修道院抄写室在 1530 年代末的消失，还与宗教改革造成的修道院解散相连，不能只归因于印刷机。

## 历史留下的问题

![印刷机喷涌出纸页洪流，旁边仅有一张阅读桌，一页纸在放大镜和暖光灯下等待缓慢核查](/assets/blogposts/2026-08-10-too-dangerous-and-too-sloppy/04-economics.jpg)

印刷术与生成式 AI 并不是同一种技术。印刷机主要复制已经排定的文本；生成式模型可以在回应指令时重组和生成新的表达。十五世纪的信息通过作坊、运输和实体市场扩散，今天的内容可以借助全球网络即时分发。法律、教育程度、平台权力和社会规模也都不同。类比能帮助我们提出问题，却不能替我们预测答案。

从维基百科志愿编辑的位置看，以制作过程划线可以解释为一种工作量规则：生成内容可以迅速增加，社区的审阅时间却有限。从已经把 AI 纳入日常工作的创作者位置看，同一条界线又可能忽略披露工具、证据能否复核与作者是否承担责任之间的差别。TikTok、小红书和黑客新闻的规则分别针对写实合成内容的标识与误导、自动运营与批量低质内容，以及生成文字进入人际讨论。为什么这些平台划出不同界线，它们各自的用途和审核条件起了多大作用，仍可继续讨论。

于是，值得继续追问的也许不是“应该支持还是禁止 AI”这一道总题，而是一些更具体的问题。

谁应当为核查一项主张付出时间：作者、平台、编辑，还是读者？哪些内容可以先发布再修正，哪些风险需要事前限制？披露 AI 使用能提供多少真实信息，什么时候又会退化成一个容易伪造的标签？来源记录、修订历史和具名签署能否降低复核成本，又会不会建立新的门槛与权力中心？以制作过程划线的禁令会成为长期制度，还是在其他做法出现后改变形态？

印刷史本身没有给出单一答案。法国的全面禁令很快被修订，《禁书目录》却维持了几个世纪；出版标志帮助读者辨认来源，也被竞争者仿冒；期刊先后采用编辑个人选择、委员会遴选和更系统的专家评审。不同制度处理的是不同问题，存续时间和适用范围也各不相同。

斯特拉塔的诗不是关于 AI 的预言。它记录的是一位十五世纪抄写员如何理解眼前的新机器。把它放在今天重新阅读，或许可以让问题变得更清楚：哪些恐惧指向真实风险，哪些判断也可能受既有身份与利益影响？我们看见的相似，究竟来自技术的一般规律，还是来自人们面对变化时反复出现的语言？而这一次真正不同的地方，又会把历史推向哪里？

## 参考资料与原文定位

- <span id="ref-wikipedia-ai-noticeboard"></span>英文维基百科 — 原始来源：[人工智能公告板：“容易取消”规定（AI noticeboard: “Easy-to-cancel mandate”）](https://en.wikipedia.org/wiki/Wikipedia:AI_noticeboard#Easy-to-cancel_mandate)。讨论中，编辑核查后写道：“the ‘two-step test’ is a requirement of the law, not the researchers’”；我的披露包括：“using AI to generate almost 90-95% of the new lines of code”。同一回复还逐项说明了提示、研究、引注、草稿审阅和移入条目空间的过程 — fetched [2026-08-20](https://web.archive.org/web/20260817234253/https://en.wikipedia.org/wiki/Wikipedia:AI_noticeboard)
- <span id="ref-wikipedia-llm-guideline"></span>英文维基百科 — 原始来源：[《使用大语言模型撰写条目》（Writing articles with large language models）](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models#:~:text=the%20use%20of%20LLMs%20to%20generate%20or%20rewrite%20article%20content%20is%20prohibited)。原文：“the use of LLMs to generate or rewrite article content is prohibited”；脚注将相关征求意见定位为 2026 年 3 月，正文列出校对与翻译等例外 — fetched [2026-08-20](https://web.archive.org/web/20260817234323/https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models)
- <span id="ref-hacker-news-ai-rule"></span>黑客新闻（Hacker News）— 原始来源：[《黑客新闻规则》（Hacker News Guidelines）](https://news.ycombinator.com/newsguidelines.html#generated)。原文：“Don't post generated text or AI-edited text. HN is for conversation between humans.” — fetched [2026-08-20](https://web.archive.org/web/20260815185918/https://news.ycombinator.com/newsguidelines.html)
- <span id="ref-tiktok-aigc-policy"></span>TikTok — 原始来源：[《AI 生成内容》（AI-generated content）](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content#:~:text=We%20also%20require%20creators%20to%20label%20all%20AI-generated%20content)。原文：“We also require creators to label all AI-generated content that contains realistic images, audio, and video.” 同页另行区分鼓励标识、可能移除和完全禁止的类别 — fetched [2026-08-20](https://web.archive.org/web/20260813143254/https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)
- <span id="ref-xiaohongshu-ai-governance"></span>新浪科技（转述小红书公告）— 原始来源：[小红书发布 AI 治理规则公告](https://finance.sina.com.cn/2026-04-27/doc-inhvxtre9124679.shtml#:~:text=AI低质：套用模板批量生产同质化内容)。原文：“平台欢迎创作者以AI为创意工具，提升内容质量与信息价值”；违规行为可被“限制分发、封禁账号” — fetched [2026-08-20](https://web.archive.org/web/20260820202256/https://finance.sina.com.cn/2026-04-27/doc-inhvxtre9124679.shtml)
- <span id="ref-international-ai-safety-report"></span>国际人工智能安全报告专家组 — 原始来源：[《2026 年国际人工智能安全报告》（*International AI Safety Report 2026*）](https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026.pdf#page=58)，共 221 个 PDF 页面。网络攻击能力见 PDF 第 58 页（报告第 57 页，约全文 26%），原文称系统擅长 “discovering software vulnerabilities and writing malicious code”；[生物与化学风险](https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026.pdf#page=65)见 PDF 第 65 页（报告第 64 页，约全文 29%），同时强调现实影响仍有 “substantial uncertainty” — fetched [2026-08-20](https://web.archive.org/web/20260819002125/https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026.pdf)
- <span id="ref-loc-gutenberg-bible"></span>美国国会图书馆 — 原始来源：[《古腾堡圣经》（The Gutenberg Bible）](https://www.loc.gov/exhibits/bibles/the-gutenberg-bible.html#:~:text=The%20printing%20of%20the%20Bible%20was%20probably%20completed%20late%20in%201455)。原文：“The printing of the Bible was probably completed late in 1455 at Mainz, Germany.” — fetched [2026-08-20](https://web.archive.org/web/20260817234136/https://www.loc.gov/exhibits/bibles/the-gutenberg-bible.html)
- <span id="ref-dnb-printing-spread"></span>德国国家图书馆下属德国书籍与文字博物馆 — 原始来源：[《印刷术的传播》（Spread of printing）](https://mediengeschichte.dnb.de/DBSMZBN/Content/EN/Printing/04-ausbreitung-des-buchdrucks-en.html#:~:text=By%201500%20printing%20offizins%20had%20emerged%20at%20around%20250%20locations)。原文：“By 1500 printing offizins had emerged at around 250 locations.” — fetched [2026-08-20](https://web.archive.org/web/20260817234356/https://mediengeschichte.dnb.de/DBSMZBN/Content/EN/Printing/04-ausbreitung-des-buchdrucks-en.html)
- <span id="ref-dominican-order-name"></span>何雅钦，《公教报》（天主教香港教区周报）— 原始来源：[《道明会的神恩（上）》](https://kkp.org.hk/node/detail/51094/#:~:text=%E8%81%96%E9%81%93%E6%98%8E%E6%89%80%E5%89%B5%E7%AB%8B%E7%9A%84%E3%80%8C%E9%81%93%E6%98%8E%E6%9C%83%E3%80%8D%E5%8F%88%E5%8F%AF%E8%AD%AF%E7%82%BA%E3%80%8C%E5%A4%9A%E6%98%8E%E6%88%91%E6%9C%83%E3%80%8D)。原文说明“道明会”亦译“多明我会”，正式名称为“宣道会”（*Ordo Praedicatorum*，O.P.）— fetched [2026-08-20](https://web.archive.org/web/20260820201309/https://kkp.org.hk/node/detail/51094/)
- <span id="ref-strata-title-quote"></span>佩特雷拉（Giancarlo Petrella）— 原始来源：[《道明会反对印刷术：别买那些书！》（“Domenicani contro l’arte della stampa: Non comprate quei libri!”）](https://bibliotecadiviasenato.it/wp-content/uploads/BVS_N12_DICEMBRE_2022-web_abbass.pdf#page=30)，载《米兰参议院街图书馆》（*la Biblioteca di via Senato Milano*），2022 年 12 月，共 108 个 PDF 页面。身份、呈递对象与场合见 PDF 第 29 页（刊物第 27 页，约全文 27%）；禁印请求、伪币比喻、错漏与淫秽指控及题引见 PDF 第 30 页（刊物第 28 页，约全文 28%）。文章把诗定位为威尼斯马尔恰纳国家图书馆手稿 It. I 72，转写：“Est virgo hec penna, meretrix est stampificata.” — fetched [2026-08-20](https://web.archive.org/web/20230209030303/https://bibliotecadiviasenato.it/wp-content/uploads/BVS_N12_DICEMBRE_2022-web_abbass.pdf)。另见菊池（Catherine Kikuchi）的[书目定位与异文](https://arche.unistra.fr/websites/arche/Productions/Publications/Source_s/Numeros_et_couvertures/sources_13_web.pdf#page=24)，共 226 个 PDF 页面；PDF 第 24 页（刊物第 23 页，约全文 11%）定位至 Marciana, Mss. Italiani, cl. I, cod. 72, n° 5054, fol. 2r，并作 “meretrix que est stampificata” — fetched [2026-08-20](https://web.archive.org/web/20260820192504/https://arche.unistra.fr/websites/arche/Productions/Publications/Source_s/Numeros_et_couvertures/sources_13_web.pdf)
- <span id="ref-chartier-writing"></span>夏蒂埃（Roger Chartier）— 原始来源：[《书写的实际影响》（“The Practical Impact of Writing”）](https://users.manchester.edu/Facstaff/SSNaragon/Online/LP/Readings/11-Chartier%2C%20Practical%20Impact%20of%20Writing%20%28abridged%29.pdf#page=6)，共 12 个 PDF 页面；引文在 PDF 第 6 页（原书第 123 页，约全文 50%）。原文：“The pen is a virgin, the printing press a whore”；并概括逐利赶印为 “hastily manufactured, faulty editions” — fetched [2026-08-20](https://web.archive.org/web/20260817234425/https://users.manchester.edu/Facstaff/SSNaragon/Online/LP/Readings/11-Chartier%2C%20Practical%20Impact%20of%20Writing%20%28abridged%29.pdf)
- <span id="ref-brann-monastic-dilemma"></span>布兰（Noel L. Brann）— 原始来源：[《印刷术发明带给修道院的两难》（“A Monastic Dilemma Posed by the Invention of Printing”）](https://journals.uc.edu/index.php/vl/article/download/5268/4132/6945#page=1)，载《可视语言》（*Visible Language*）XIII.2（1979），共 18 个 PDF 页面。PDF 第 1 页（期刊第 150 页，约全文 6%）写明作品作于 1492 年，并称 “the author was not hostile to the printing art in principle”；[手稿交给印刷商的记载](https://journals.uc.edu/index.php/vl/article/download/5268/4132/6945#page=2)见 PDF 第 2 页（期刊第 151 页，约全文 11%），原文说特里特米乌斯这样做是 “to assure the greatest possible circulation of this tract” — fetched [2026-08-20](https://web.archive.org/web/20260817234456/https://journals.uc.edu/index.php/vl/article/download/5268/4132/6945)
- <span id="ref-ddb-de-laude"></span>德国数字图书馆 — 原始来源：[*De laude scriptorum* 书目记录](https://www.deutsche-digitale-bibliothek.de/item/Y7EKMZBKNWE5OYMA2SIROTFG2PWURZV4#:~:text=Maguntinu%5Bm%5D%20%3A%20Peter%20Friedberg%20%2C%201494)。书目原文列为：“Maguntinu[m] : Peter Friedberg , 1494” — fetched [2026-08-20](https://web.archive.org/web/20260817234501/https://www.deutsche-digitale-bibliothek.de/item/Y7EKMZBKNWE5OYMA2SIROTFG2PWURZV4)
- <span id="ref-willinsky-erasmus"></span>威林斯基（John Willinsky），《学习的知识产权：从圣哲罗姆到约翰·洛克的前史》（*The Intellectual Properties of Learning*）第八章“人文主义复兴”（*Humanist Revival*）— 原始来源：[开放获取终稿](https://intellectualproperties.stanford.edu/sites/g/files/sbiybj24701/files/media/file/8._humanist_learning.pdf#page=20)。全书由芝加哥大学出版社于 2018 年出版；此处使用作者提供的 35 页开放获取终稿，作者注明它经过评审和修订、但与最终出版文本仍有差异。[伊拉斯谟 1508 年与马努提乌斯合作](https://intellectualproperties.stanford.edu/sites/g/files/sbiybj24701/files/media/file/8._humanist_learning.pdf#page=12)见 PDF 第 12 页（本章第 12 页，约全文 34%）；[“欲速则不达”评注中先褒后贬的语境](https://intellectualproperties.stanford.edu/sites/g/files/sbiybj24701/files/media/file/8._humanist_learning.pdf#page=19)见 PDF 第 19–20 页（本章第 19–20 页，约全文 54–57%）。原文：“a good book get choked up with six thousand mistakes”；“these swarms of new books”；“the very multitude of them is harmful to scholarship” — fetched [2026-08-20](https://web.archive.org/web/20251206063737/https://intellectualproperties.stanford.edu/sites/g/files/sbiybj24701/files/media/file/8._humanist_learning.pdf)
- <span id="ref-uchicago-luther"></span>芝加哥大学图书馆 — 原始来源：[《作为印刷媒体第一位影响者的马丁·路德》（Martin Luther as print media’s first influencer）](https://www.lib.uchicago.edu/collex/exhibits/media-revolutions-then-now-martin-luther-and-the-making-of-modern-communication/type-casting-selves/#:~:text=Unknown%20in%201517%2C%20by%201520%20he%20was%20the%20most%20published%20author)。原文：“Unknown in 1517, by 1520 he was the most published author in the medium of print”；馆方另称他为 “book history’s first bestseller author” — fetched [2026-08-20](https://web.archive.org/web/20260817234534/https://www.lib.uchicago.edu/collex/exhibits/media-revolutions-then-now-martin-luther-and-the-making-of-modern-communication/type-casting-selves/)
- <span id="ref-princeton-mainz"></span>普林斯顿大学图书馆 — 原始来源：[《美因茨印刷业的开端》（The beginning of printing in Mainz）](https://dpul.princeton.edu/gutenberg/feature/the-beginning-of-printing-in-mainz#:~:text=presumably%20thousands%20of%20such%20forms%20were%20printed)。原文：“Chappe contracted with Gutenberg to print the indulgence forms in great quantity”；馆方估计 “presumably thousands” — fetched [2026-08-20](https://web.archive.org/web/20260817234602/https://dpul.princeton.edu/gutenberg/feature/the-beginning-of-printing-in-mainz)
- <span id="ref-farge-france-ban"></span>法尔热（James K. Farge）— 原始来源：[《巴黎大学、巴黎高等法院与法国宗教改革》（“The University of Paris, the Parlement of Paris, and the French Reformation”）](https://jps.library.utoronto.ca/index.php/renref/article/download/12038/8915#page=7)，共 11 个 PDF 页面。禁令与修订见 PDF 第 7–8 页（期刊第 179–180 页，约全文 64–73%）。原文：“no one, under pain of death by hanging, is hereafter to print … any book”；修订命令要求议会先指定 24 名印刷商，再由国王择 12 名 — fetched [2026-08-20](https://web.archive.org/web/20260817234627/https://jps.library.utoronto.ca/index.php/renref/article/download/12038/8915)
- <span id="ref-upenn-index"></span>宾夕法尼亚大学图书馆 — 原始来源：[《禁书目录》（*Index Librorum Prohibitorum*）](https://specialcollectionsprocessing.exhibits.library.upenn.edu/exhibits/show/bythebook/library_rules#:~:text=The%20Index%20librorum%20prohibitorum%20was%20first%20issued%20in%201559)。原文：“was first issued in 1559 by the Catholic Church under the authority of Pope Paul IV”；同页记载其后持续增补修订，直到 1966 年 — fetched [2026-08-20](https://web.archive.org/web/20260817234804/https://specialcollectionsprocessing.exhibits.library.upenn.edu/exhibits/show/bythebook/library_rules)
- <span id="ref-vatican-index"></span>梵蒂冈信理部 — 原始来源：[《关于〈禁书目录〉的通知》（1966 notification regarding the Index）](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_19660614_de-indicis-libr-prohib_en.html#:~:text=it%20no%20longer%20has%20the%20force%20of%20ecclesiastical%20law)。原文一面称目录 “remains morally binding”，一面宣布它 “no longer has the force of ecclesiastical law” — fetched [2026-08-20](https://web.archive.org/web/20260817234825/https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_19660614_de-indicis-libr-prohib_en.html)
- <span id="ref-stationers-charter"></span>版权史原始资料库（Primary Sources on Copyright）— 原始来源：[1557 年书商公会王室特许状](https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=record_uk_1557#:~:text=exclusive%20control%20over%20printing%20within%20England)。特许状规定，除公会成员或取得王室牌照者外，不得在英格兰及其领地从事印刷；德兹利的概括是 “exclusive control over printing within England” — fetched [2026-08-20](https://web.archive.org/web/20260817234650/https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=record_uk_1557)
- <span id="ref-cambridge-printing-acts"></span>剑桥大学出版社 — 原始来源：[《17 世纪末的书商公会与印刷法》（The Stationers and the Printing Acts at the end of the seventeenth century）](https://www.cambridge.org/core/books/abs/cambridge-history-of-the-book-in-britain/stationers-and-the-printing-acts-at-the-end-of-the-seventeenth-century/4999BBB8F8581DE94B9C2AAD75A01D75#:~:text=The%20Act%20of%20Parliament%20whose%20expiry%20on%203%20May%201695)。书章概述确认 1662 年法令于 1695 年 5 月 3 日失效，并说明当时人称其为 *Printing Act*，后世常称 *Licensing Act* — fetched [2026-08-20](https://web.archive.org/web/20260817234716/https://www.cambridge.org/core/books/abs/cambridge-history-of-the-book-in-britain/stationers-and-the-printing-acts-at-the-end-of-the-seventeenth-century/4999BBB8F8581DE94B9C2AAD75A01D75)
- <span id="ref-moseley-wicked-bible"></span>莫斯利（David Moseley），坎特伯雷大学 — 原始来源：[《“不”好笑？幽默、难堪与〈邪恶圣经〉》（*“Not” Funny? Humour, Embarrassment, and the “Wicked Bible”*）](https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content#page=3)，共 79 个 PDF 页面；PDF 第 2 页为空白。漏字及完整误句见 PDF 第 3 页（论文第 1 页，约全文 4%），原文：“Thou shalt commit adultery.”；[没被销毁及退回修正](https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content#page=18)见 PDF 第 18 页（论文第 16 页，约全文 23%）；[牌照未撤](https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content#page=19)见 PDF 第 19 页（论文第 17 页，约全文 24%）；[罚款与希腊文印刷所](https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content#page=55)见 PDF 第 55 页（论文第 53 页，约全文 70%）。原文：“no evidence that the Bibles were ordered to be destroyed”；“the printers did not lose their licence” — fetched [2026-08-20](https://web.archive.org/web/20260813145200/https://ir.canterbury.ac.nz/server/api/core/bitstreams/7e8a0935-0cdc-4f4c-ae4e-8a1e332fe695/content)
- <span id="ref-cambridge-manutius"></span>剑桥大学图书馆 — 原始来源：[《袖珍本、仿本与海豚锚标志》（Enchiridia, counterfeits and the dolphin-and-anchor device）](https://exhibitions.lib.cam.ac.uk/manutius/case/enchiridia/#:~:text=published%20as%20pocket-size%20books%20(enchiridia)%20was%20Aldus%E2%80%99s%20most%20successful%20editorial%20innovation)。原文把 1501 年开始的袖珍古典版本称为 “Aldus’s most successful editorial innovation”；展览导言另说明这些书使用斜体字 — fetched [2026-08-20](https://web.archive.org/web/20260211181353/https://exhibitions.lib.cam.ac.uk/manutius/case/enchiridia/)
- <span id="ref-cambridge-manutius-counterfeits"></span>剑桥大学图书馆 — 原始来源：[《但丁〈神曲〉仿本标志》（Dante *Commedia* counterfeit device）](https://exhibitions.lib.cam.ac.uk/manutius/artifacts/dante-1265-1321-commedia-counterfeit-device/#:~:text=The%20forgers%20also%20attempted%20to%20copy%20Aldus%E2%80%99s%20dolphin-and-anchor%20device)。该里昂仿本约印于 1502–1503 年，原文：“The forgers also attempted to copy Aldus’s dolphin-and-anchor device.” 展览总览并说明里昂竞争者处在威尼斯疆域及其印刷特许之外 — fetched [2026-08-20](https://web.archive.org/web/20230924211011/https://exhibitions.lib.cam.ac.uk/manutius/artifacts/dante-1265-1321-commedia-counterfeit-device/)
- <span id="ref-yale-printers-devices"></span>耶鲁大学法学院图书馆 — 原始来源：[《法律书籍中的印刷商标志》（Printers’ devices from law books）](https://library.law.yale.edu/news/printers-devices-law-books#:~:text=A%20printer%E2%80%99s%20device%20is%20a%20trademark%20of%20sorts)。原文称印刷商标志是 “a trademark of sorts”，兼具营销和类似版权声明的功能；同页称最早的已知实例 “first appeared in their 1457 Mainz Psalter” — fetched [2026-08-20](https://web.archive.org/web/20260817235011/https://library.law.yale.edu/news/printers-devices-law-books)
- <span id="ref-manutius-warning"></span>马努提乌斯，版权史原始资料库（Primary Sources on Copyright）— 原始来源：[1503 年《告里昂印刷商书》英译与转写](https://www.copyrighthistory.org/cam/tools/request/showRepresentation.php?id=representation_i_1503#:~:text=It%20happens%20that%20in%20the%20city%20of%20Lyon%20our%20books%20appeared%20both%20full%20of%20errors%20and%20under%20my%20name)，原件定位为法国国家图书馆 BN, Ms. Gr. 3064, fol. 85。原文称里昂书 “full of errors and under my name”，随后列出印刷商、出版地、日期、标志、纸张和字体差异及逐书错字 — fetched [2026-08-20](https://web.archive.org/web/20251207185927/https://www.copyrighthistory.org/cam/tools/request/showRepresentation.php?id=representation_i_1503)
- <span id="ref-sabellico-privilege"></span>科斯蒂洛（Joanna Kostylo），版权史原始资料库（Primary Sources on Copyright）— 原始来源：[《评 1486 年萨贝利科特许》（Commentary on Marcantonio Sabellico’s privilege）](https://www.copyrighthistory.org/cam/commentary/i_1486/i_1486_com_2162008205354.html#:~:text=The%20printing%20monopoly%20granted%20to%20Johannes%20of%20Speyer%20in%201469)。原文称 1469 年约翰内斯·德·斯皮拉（Johannes de Speyer）所得为 “printing monopoly”，1486 年萨贝利科所得是 “the first known privilege to an author”；这些权利 “were not conceived as the inherent right” — fetched [2026-08-20](https://web.archive.org/web/20260514232223/https://www.copyrighthistory.org/cam/commentary/i_1486/i_1486_com_2162008205354.html)
- <span id="ref-statute-anne"></span>德兹利（Ronan Deazley），版权史原始资料库（Primary Sources on Copyright）— 原始来源：[《评 1710 年〈安妮法令〉》（Commentary on the Statute of Anne 1710）](https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_uk_1710#:~:text=not%20just%20the%20members%20of%20the%20company%2C%20but%20also%20any%20author)。德兹利称它是世界第一部版权成文法，并指出 “not just the members of the company, but also any author … was free to own and deal in the copies of books”；未出版新书的首个期限为 “Fourteen Years” — fetched [2026-08-20](https://web.archive.org/web/20241013225756/https://www.copyrighthistory.org/cam/tools/request/showRecord.php?id=commentary_uk_1710)
- <span id="ref-modern-trademark-registration"></span>英国知识产权局 — 原始来源：[《创造历史的红色三角》（The red triangle that made history）](https://ipo.blog.gov.uk/2026/01/08/the-red-triangle-that-made-history-celebrating-150-years-of-uk-trade-mark-no-1/#:~:text=France%20introduced%20a%20deposit%20system%20in%201857)。原文：“France introduced a deposit system in 1857”；英国 1875 年法令建立 “a systematic, nationally centralised register” — fetched [2026-08-20](https://web.archive.org/web/20260421133909/https://ipo.blog.gov.uk/2026/01/08/the-red-triangle-that-made-history-celebrating-150-years-of-uk-trade-mark-no-1/)
- <span id="ref-royal-society-philosophical-transactions"></span>英国皇家学会 — 原始来源：[《〈皇家学会哲学汇刊〉史》（History of *Philosophical Transactions*）](https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/#:~:text=The%20Royal%20Society%20responded%20by%20introducing%20more%20rigorous%20and%20systematic%20expert%20peer%20review)。原文记载期刊由奥尔登堡于 1665 年创办；1752 年改由 21 人委员会集体选稿；到 1830 年代才引入 “more rigorous and systematic expert peer review” — fetched [2026-08-20](https://web.archive.org/web/20260609032321/https://royalsociety.org/journals/publishing-activities/publishing350/history-philosophical-transactions/)
- <span id="ref-cambridge-manuscript-print"></span>剑桥大学出版社 — 原始来源：[《手稿的传播与流通》（“Manuscript transmission and circulation”）](https://www.cambridge.org/core/books/abs/cambridge-history-of-early-modern-english-literature/manuscript-transmission-and-circulation/687E02660235B6AACCC317AD783C406E#:~:text=it%20was%20not%20a%20matter%20of%20the%20new%20one%20expanding%20at%20the%20expense%20of%20the%20old)。书章概述限定在英格兰，称印刷出现后许多年仍有大量手写与口述传播，并总结：“it was not a matter of the new one expanding at the expense of the old.” 同一概述把 1530 年代末修道院抄写室的消失放在宗教改革背景下 — fetched [2026-08-20](https://web.archive.org/web/20240411165002/https://www.cambridge.org/core/books/abs/cambridge-history-of-early-modern-english-literature/manuscript-transmission-and-circulation/687E02660235B6AACCC317AD783C406E)
- <span id="ref-princeton-illumination"></span>普林斯顿大学图书馆 — 原始来源：[《米尔伯格展厅内：彩饰》（Inside the Milberg Gallery: Illumination）](https://library.princeton.edu/about/library-news/2019/inside-milberg-gallery-illumination#:~:text=continued%20to%20find%20work%20for%20patrons%20with%20a%20taste%20for%20brilliantly%20colored%20luxury%20books)。同页说明早期印本为首字母和红字留白，之后手工完成；到 1470 年代，木刻和印刷标题逐渐减少描红需求。原文称手抄本彩饰者仍 “continued to find work” 于手写或印刷的奢侈书市场 — fetched [2026-08-20](https://web.archive.org/web/20251220020759/https://library.princeton.edu/about/library-news/2019/inside-milberg-gallery-illumination)

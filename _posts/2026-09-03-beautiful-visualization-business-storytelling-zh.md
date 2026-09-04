---
title: "怎样做出好看的可视化，把生意讲清楚"
excerpt: "纽约时报、The Pudding、金融时报和 3Blue1Brown 的共同点是什么，为什么图表库替你解决不了好看，以及怎样让交互真的在解释，而不是只在演示。"
date: 2026-09-03
lang: zh
published: true
cover_image:
  src: /assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-00-cover-zh.jpg
  x: 570
  y: 0
  size: 630
og_image: /assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-00-cover-zh.jpg
translationKey: beautiful-visualization-business-storytelling-2026-09-03
categories:
  - blog
tags:
  - data-visualization
  - storytelling
  - design
  - d3
  - explainers
---

*上周我做了一张会动的示意图，自己看了几遍，然后发现它什么也没教会人。本文写的是我事后想明白的事情：一张图要替你把观点扛下来，靠的是哪些做法。读者设定为需要用一张图或者一个交互来支撑商业判断的创业者、产品经理和顾问。文中每一个链接都在 2026-09-03 当天打开读过。*

## 五家风格毫无共同点的出版方

![五张挂成一排的画框，每一张的视觉风格都完全不同，一条橙色的对齐线从它们背后连续穿过，只在框与框的间隙里露出来](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-01-five-houses.jpg)

把这个领域里做得最好的几家放在一起看，第一个反应往往是：它们之间没有任何共同的风格。

纽约时报 Upshot 用的是冷灰底色加一个编辑强调色。[The Pudding](#ref-pudding-pockets) 的文章开头是大号标题字，上面还放一首诗。金融时报印在三文鱼色的纸上。[Distill](#ref-distill-momentum) 看上去像一篇学会了 CSS 的物理论文。[3Blue1Brown](#ref-manim) 是深蓝底上的粉笔字数学。[Nicky Case](#ref-polygons) 画的是歪歪扭扭的卡通形状，用的是原色。

配色不统一，字体不统一，网格也不统一。可是这些作品都能让一个素不相识的人停下来看完，而大多数商业图表连拿工资的同事都会跳过。它们也不是靠庞大的专业部门堆出来的。The Pudding 自己介绍工作方式时写道，团队规模不大，成员都是通才，靠的是[“一堆杂七杂八的技能”](#ref-pudding-process)：批判性思考、设计、写作和编程。

所以那种“哇”的感觉并不来自某种外观，而来自一套做法，这套做法能在风格差异极大的团队之间通用。

接下来是让人有点扫兴的部分：如果你指望花钱买一个好看的结果，恐怕买不到。这个领域里名气最大的工具本身完全不提供设计。D3 的官方文档写得很直白，它[不是传统意义上的图表库，“没有图表这个概念”](#ref-d3-what-is)，你用它拼装的是各种基础构件，出来的东西有多好，取决于你做了哪些决定。同一页文档还专门提醒读者不要被示例画廊迷惑，因为其中许多作品[“实现起来花了极大的力气”](#ref-d3-what-is)，并且说明 D3 适合[纽约时报或者 The Pudding 这类机构](#ref-d3-what-is)，因为那里一张图会被上百万人看到，背后还有一整个编辑团队。

这就是本文的前提。没有主题可以安装，只有决定需要做，而这些决定最后能收进一份清单，也就是文章结尾的那一份。

## 图表的标题应该是一句结论

![同一张图的两个版本：一个角上系着一枚档案标签，另一个在顶部横着一条写好的横幅，并有一条引线指向折线拐弯的那一点](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-02-title-claim.jpg)

大多数人能做的、回报最高的一处改动，完全不需要设计能力：**把结论写进标题，而不是把话题写进标题。**

“各地区收入，Q1 至 Q3”是一个档案标签。“欧洲现在扛着增长，北美已经连续三个季度持平”是一句别人可以反驳的话。后者告诉读者该看什么，同时也在替你检验这张图是不是画对了，因为如果这句话写不出来，说明你还没有观点。

这条规矩是我自己的做法，算不上什么定论，但是可以看一家新闻编辑室怎样成规模地执行它。Upshot 那篇《How the Recession Reshaped the Economy, in 255 Charts》，各个小节的标题分别是“A Mixed Recovery”“The Medical Economy”“A Long Housing Bust”和“Grooming Boom”。没有一个标题在说变量名，每一个都是一句判断，下面的小图组是证据。这篇文章还专门放了一段[“How to read this chart”](#ref-nyt-255)，逐条说明两个轴分别编码了什么。默认读者是陌生人，不是画图的分析师，才会这样写。

由此还能推出两条。

**一张图只讲一件事。**人的注意力是单线程的。一张图同时承载三个结论，等于一个也没传达出去，因为读者得自己挑一个来找，而且多半会挑错。

**按你想展示的关系来选图形，不要按菜单来选。**金融时报把内部培训用的那张 Visual Vocabulary 海报公开了，用途正是如此：帮记者[为数据可视化挑选最合适的图形语汇](#ref-ft-visual-vocabulary)，并且把所有图表类型按它们表达的关系归类，包括偏离、相关、排名、分布以及占比等等。金融时报自己的说法值得借用，这张海报[不打算教所有人画图，而是教人认出哪些场合适合让图和文字配合使用](#ref-ft-visual-vocabulary)。其中关于相关性的那条提醒，是我在董事会材料里见过最多人违反的一条：除非你明说，否则[读者会默认你展示的关系是因果关系](#ref-ft-visual-vocabulary)。

## 五条通用的纪律

![左边是六条同样粗细、六种互相竞争的颜色的折线，配一个图例方块；右边是同一批数据，五条淡灰色线加一条橙色线，一条引线连着标注框，序列名直接标在线的末端](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-03-disciplines.jpg)

下面这几条，在前面提到的每一家都能看到，跟各家的外观差异无关。

### 一个强调色，其余一律灰掉

外行的图表给每条线都上色，专业的图表只给论点上色，背景一律灰掉。

Datawrapper 是做图表工具的厂商，它那份被广泛引用的配色指南把话说得比我还重：它要求把灰色当作[数据可视化里最重要的颜色](#ref-datawrapper-colors)，因为只有把不重要的元素灰掉，强调色才立得住。同一份指南还给了一个上限，一张图里如果需要[超过七种颜色](#ref-datawrapper-colors)，该换图形或者合并类目，而不是扩充调色板。

语义色要和强调色分开。如果红色在这份材料里代表“有风险”，那么红色就不能同时用作 EMEA 这条序列的颜色。连续色阶和发散色阶也请取自经过检验的方案，不要自己配。D3 的配色模块正是[取自 Cynthia Brewer 的 ColorBrewer](#ref-d3-scale-chromatic)。

改法很具体：原来是六条线六种颜色外加一个图例，读者得在图例和线之间来回对照；改完是一条深色线代表你要论证的那条序列，另外五条淡灰色垫在后面，序列名直接写在自己那条线的末端。图例删掉。数据没变，但是这张图有主角了。

### 一次只变一件事

这条纪律说得最清楚的出处不在数据领域，而在动画。Lasseter 1987 年那篇 SIGGRAPH 论文，复述了 Frank Thomas 和 Ollie Johnston 在迪士尼总结出的原则，把 staging 定义为[把一个想法呈现得“完全、明确、不会被误解”](#ref-lasseter-staging)，接着直接给出规则：在安排一个动作时，[同一时刻只应让观众看到一个想法](#ref-lasseter-staging)，因为一次发生太多事情，眼睛就不知道该往哪里看，主要的意思会被漏掉。论文里把动画师的做法形容成在说：[“看这里，现在看这里，现在再看这里。”](#ref-lasseter-staging)

这其实就是分步呈现。如果你的示意图需要加一层数据、按分段重新着色、再显示一条标注，那是三步，不是一页。放在静态材料里，这就是那种被人嫌土的逐项出现动画；只要做到每一拍只变一件事，它就是观众跟得上和观众自己往下翻之间的区别。

### 同一个元素要移动，不要删掉重画

图表切换状态时，凡是前后含义相同的元素，都必须是**同一个元素**在移动。这是 Mike Bostock 说的 object constancy，他那篇文章至今仍是讲得最清楚的：代表某个具体数据点的图形元素[可以在过渡中被视线一路跟住](#ref-bostock-constancy)，读者的工作因此从逐个扫标签变成了看运动。

在 D3 里，实现它的机制是 key function：告诉数据绑定用哪个字段标识一行，俄亥俄州在更新前后就还是俄亥俄州。省掉它的后果，Bostock 也写了，[默认按索引绑定会产生误导](#ref-bostock-constancy)，因为第三根柱子更新后仍然是第三根柱子，无论它现在代表哪个州。你会得到一段流畅、自信而错误的动画。

不用 D3 的话，界面动画里有对应的说法。FLIP 这个技术[由 Paul Lewis 命名](#ref-gsap-flip)，先量出元素当前的位置，让布局照常变化，再把差值动画掉。GSAP 的实现是这样描述的：记录位置、尺寸和旋转，你随便改，然后加上偏移量，[让它们看起来从来没有动过](#ref-gsap-flip)。

Bostock 还划了一条界线，这条界线比技术本身更要紧：[动画只应该在能增进理解的时候使用](#ref-bostock-constancy)，两组互不相干的量之间切换，应该用切换或者淡入淡出，而不是毫无意义的位移。柱子在两个不相干的指标之间飞来飞去，看着很贵，其实什么也没说。

### 专业感来自标注

图表库负责画图元。指着异常值把话写出来的那句，没有哪个库会替你写，而观感上的差距，多半就落在这句话上。

一条引线加一个说明，在折线拐弯的那个月写上“合同在这里重谈了”，对理解的帮助超过任何渐变效果。这件事不体面、要手工做，也正是新闻图表看上去是成品、而看板图表看上去是半成品的原因。如果你用 D3，Susie Lu 的 d3-annotation 就是为此而做的，内置了若干标注类型，也可以[扩展出自定义的标注](#ref-d3-annotation)。

我自己的规矩是：凡是要给别人看的图，至少配一条标注；如果一条也想不出来，说明这张图没有结论，应该改成一句话。

### 留白就是层级

留白是你告诉读者先看哪里的方式。The Pudding 那篇讲口袋的文章，开头是一首诗和一个用大号字排出来的单词，然后才把 80 条牛仔裤摆到你面前；结论落地时，是单独占一块空间的一句话：女装牛仔裤的口袋比男装[短 48%、窄 6.5%](#ref-pudding-pockets)。

那篇文章里还有一处小体贴值得学。滚动驱动的部分开始之前，它先说明接下来会有滚动动画，并且给出一个链接，让[不想看的人直接跳到最终状态](#ref-pudding-pockets)。照顾那些不想看你动画的读者，本身就是一个设计决定，而几乎没有人做。

## 那个什么也没解释的播放按钮

![左边是一条流程示意图，播放按钮让一个圆点沿着它走了一遍，下方的图表面板毫无变化；右边是同一条流程，滑块的手柄一动，下方的图表面板就明显被重画了](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-04-play-button.jpg)

下面是我的检讨。

上周我在做一份交互式讲义，讲一个大型社交信息流怎样决定内容排序，里面有手绘的架构图和一张延迟图表。我加了一个播放按钮，按下去会有一个发光的圆点沿着流程走：先召回，再排序，再过滤，然后输出。看着挺好，我自己看了四遍。

然后我问自己，观众看完之后知道了哪些原先不知道的事情，答案是没有。那个圆点没有揭示任何关系，它只是把图上已经画好的箭头又慢慢重述了一遍。我做出来的是演示，却当成了解释。

Bret Victor 在 2011 年就把这个区别讲清楚了，而且至今没有过时。他那篇关于 explorable explanations 的文章态度很明确：[交互性本身并不是重点](#ref-bret-victor)；那些把读者丢进沙盒、让他自己琢磨的小控件，[根本算不上解释](#ref-bret-victor)。他的文章首先能当静态文字读，[读者不必动手也能学到东西](#ref-bret-victor)，动手只是为了看得更深。2024 年他补了一段后记，语气里带着明显的失望：这个词现在被用得太宽，[几乎等于“任何配了交互图片的文章”](#ref-bret-victor)。

所以我现在动手做任何交互之前，先做一个检验：**说出观众通过它会发现的那个关系。**如果“拖动这个，他们会发现……”这句话补不完整，就把交互砍掉，改成一张更好的静态图。

有三类能通过这个检验，按我使用的优先次序排列。

**第一类，因果联动：拖动一样东西，看另一样怎么反应。**Upshot 那个租房还是买房的计算器是典型。它把自己猜不到的变量交给你，写着[请调整这些数字，得到符合你自己情况的估算](#ref-nyt-rent-buy)，并且谨慎地界定了自己在断言什么，说明所谓更划算的选择指的是[长期来看在财务上更合算的那一个](#ref-nyt-rent-buy)，而不是你眼下负担得起的那一个。读者发现的是一个关系，不是一个数字：你打算住多久，几乎压过了其他所有因素。放到商业材料里，这就是你的定价模型、转化漏斗和招人计划。把那个能改变结论的滑块交给对方。

**第二类，反事实移除：拿掉一部分，看什么会坏。**Nicky Case 的 Parable of the Polygons 整篇都建立在这上面。它让你[用滑块调整每个形状自身的偏好程度](#ref-polygons)，接着做了一件比演示更进一步的事：把世界设成已经隔离的状态，请你把偏好完全去掉，然后问会发生什么。答案就是全文的论点。[看见什么没有发生了吗？](#ref-polygons)什么也没动。把原因去掉，并不能消除结果。这一点，任何一段文字的说服力都比不上眼看着那片格子纹丝不动。

一个设计细节：拿掉一个部件时，在原处留一个虚线轮廓。留下空洞会被当成 bug，留下轮廓才会被读成论证。

Case 另一篇有名的可玩文章[《The Evolution of Trust》](#ref-explorables)把同样的形式用在了博弈论上。它和其余几十篇一起收在 [explorabl.es](#ref-explorables) 这个目录里，该站自称是“一个通过玩来学习的聚集地”，也是我知道的最适合去搬交互套路的地方。

**第三类，聚焦收拢：把除了一条线索以外的东西都压暗。**三类里最弱的一类，不过当序列很多、而每位读者关心的那条又各不相同时，它仍然有用。口袋那篇文章把这招用在了物件上：点一个物件，装不下它的品牌就淡掉，因为[品牌变淡就表示这件东西放不进去](#ref-pudding-pockets)。读者自己挑问题，图来回答。

Distill 那篇讲动量的文章是面向技术读者的同一类做法：两个滑块，步长和动量，底下摆着一个判断，说[通行的那套说法解释不了动量的许多重要行为](#ref-distill-momentum)。你不是在看一段流程播放，而是拿到了那两个能让这个判断成立或者不成立的旋钮。

## 别把地图撤下去

![一张系统示意图，其中三个节点被橙色圈出，各自用虚线引到右侧放大的细节面板，同一个绿色小标记在总图和每个面板里都出现了一次](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-05-map-and-zoom.jpg)

讲得细的材料最常见的翻车方式，是听众大约在第四页就跟丢了，而且不会开口说。

这个问题最老的解法至今仍然最好用。Ben Shneiderman 1996 年的论文《The Eyes Have It》给出的视觉信息检索箴言是[“先总览，再缩放和过滤，然后按需查看细节”](#ref-shneiderman)，它所在的分类框架一共列了七项任务：总览、缩放、过滤、按需细节、关联、历史和提取。

落到一份材料或者一个看板上，可以拆成三个习惯。

整个系统先完整画一次，而且一直留着。后面每一张细节图都是这张总图上某个节点的放大，并且要说清楚是哪个节点。如果你见过深入讲解时会场突然安静下来的场面，缺的往往就是这个：他们不知道自己现在在哪里。

给读者一个**主角**。挑一个具体的单位，一位客户、一次请求、一笔交易，让它贯穿每一张图。身份能够反复辨认，别人才有可能把各个局部拼回整体。这跟 object constancy 是同一个道理，只不过落在叙述上，不落在像素上。

细节等人问了再给，不要默认铺开。悬浮提示、点击展开、可展开的行都行。总览是承诺，细节是兑现。

## 工具，老实说

![货架上立着七张卡片：其中三张已经印好了成品图表，上面还夹着模板板；另外四张是空白方格纸，各放着一支绘图笔、一把刻刀、一副分规和一支细毛笔](/assets/blogposts/2026-09-03-beautiful-visualization-business-storytelling/beautiful-visualization-06-toolbox.jpg)

正确的顺序是：先定结论，再定要展示的关系，最后才挑工具。先挑工具的典型下场，是给一组根本不构成占比关系的数据画了一张堆叠面积图。

| 工具 | 自带外观？ | 什么时候用 |
|---|---|---|
| [Observable Plot](#ref-observable-plot) | 是 | 快速出一张常规图表。默认值合理，D3 官方文档也提到，在 D3 里要 50 行的直方图，[用 Plot 一行就够](#ref-d3-what-is) |
| [Apache ECharts](#ref-echarts) | 是 | 看板和大量需要保持一致外观的图表；它主打开箱即用的[高度可定制图表](#ref-echarts) |
| [D3](#ref-d3-what-is) | **否** | 你要的形状还不存在。比例尺、过渡、[标注](#ref-d3-annotation)、[流向图](#ref-d3-sankey) |
| 手写 SVG 加 CSS | 否 | 自己画的两张示意图之间做一次状态切换。能用的办法里最省事的一个 |
| [Motion](#ref-motion) 或 [GSAP Flip](#ref-gsap-flip) | 否 | 布局变化时元素必须保持身份 |
| [Scrollama](#ref-scrollama) | 否 | 论证需要随着读者滚动逐段推进；它是一个[轻量的滚动叙事库](#ref-scrollama) |
| [Mermaid](#ref-mermaid) | 是 | 需要以文本形式和代码放在一起的静态示意图；它[把类 Markdown 的文本定义渲染成图](#ref-mermaid)，也是这里唯一只做静态的一项 |

关于这张表有两点要补充。

D3 那一格的“否”是重点。它是一套工具箱，不是一种风格；同一份介绍它有多强的文档也直说了，拿它来做内部看板或者一次性分析属于杀鸡用牛刀。除非你要的形状没人做过，否则用 Plot 或者 ECharts。

另外，如果想知道“一次只变一件事”这条纪律能被机器推到什么程度，可以看 3Blue1Brown 的视频，它们由 manim 渲染，作者对它的描述是一个用于精确程序化动画、[专门用来制作数学讲解视频](#ref-manim)的引擎。精确本身就是重点，每一帧都只有一处是刻意改动的。

## 一份清单

拿它对着你下一份材料或者看板过一遍，大约十分钟，收益主要就在这里。

1. 每张图的标题写的是结论，不是话题。
2. 每张图只承载一个结论。两个结论就画两张图。
3. 图形类型是按你要展示的关系挑的。
4. 只用一个强调色，凡是背景信息一律灰掉。
5. 语义色（风险、状态）没有被拿去当序列色用。
6. 类目色不超过七种。超了就合并。
7. 每张图至少有一条标注，点明你希望对方看到的东西。
8. 序列直接标在图上，能删的图例都删掉。
9. 动画保持身份：元素是移动的，不是删掉重画的。
10. 每一个交互都对应一个说得出口的关系，是读者自己发现的。说不出来就砍掉。
11. 有一张总览图，并且每张细节图都说明自己是总览的哪一部分。

第 10 条是我上周没做到的那条，也是砍掉工作量最多的一条。商业材料里的交互，大部分本来就不该存在；经得起这个问题的那几个，往往是整份材料里最好的东西。

## 参考资料与原文定位

### 原则的一手出处

- <span id="ref-bostock-constancy"></span>Mike Bostock（D3 作者，本人发布）——原始出处：[“Object Constancy”](https://bost.ocks.org/mike/constancy/#:~:text=can%20be%20tracked%20visually%20through%20the%20transition)，日期 2012 年 5 月 16 日。支持段落：“Animated transitions are pretty, but they also serve a purpose: they make it easier to follow the data. This is known as object constancy: a graphical element that represents a particular data point (such as Ohio) can be tracked visually through the transition. This lessens the cognitive burden by using preattentive processing of motion rather than sequential scanning of labels.”；“Above all, animation should be meaningful. While it may be visually impressive for bars to fly around the screen during transitions, animation should only be used when it enhances understanding. Transitions between unrelated datasets or dimensions (e.g., from temperature to stock price) should use a simpler cross-fade or cut rather than gratuitous, nonsensical movement.”；“If you forget to specify a key function, the default join-by-index can be misleading!”——读取于 [2026-09-03](https://web.archive.org/web/20260903183741/https://bost.ocks.org/mike/constancy/)
- <span id="ref-shneiderman"></span>Ben Shneiderman，马里兰大学——原始出处：[“The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations”](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf#page=2)，载《Proceedings of the 1996 IEEE Symposium on Visual Languages》第 336 至 343 页（DOI [10.1109/VL.1996.545307](https://doi.org/10.1109/VL.1996.545307)）。作者本人托管的 PDF，可公开阅读；DOI 指向的 IEEE Xplore 页面需要付费，因此请点作者托管的这一份。箴言在 PDF 第 2 页、原刊第 337 页，即第 2 节“Visual Information Seeking Mantra”。支持段落原文：“Overview first, zoom and filter, then details-on-demand”。摘要中的表述为“overview first, zoom and filter, then details on demand.”。同页列出的七项任务为：“Overview: Gain an overview of the entire collection. Zoom: Zoom in on items of interest”，其后依次是 filter、details-on-demand、relate、history 和 extract。七种数据类型为一维、二维、三维、时序、多维、树和网络——读取于 2026-09-03；最近的存档快照为 [2026-08-25](https://web.archive.org/web/20260825061316/https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf)
- <span id="ref-bret-victor"></span>Bret Victor（本人发布；为这一形式命名的文章）——原始出处：[“Explorable Explanations”](https://worrydream.com/ExplorableExplanations/#:~:text=the%20interactivity%20itself%20is%20not%20really%20the%20point)，日期 2011 年 3 月 10 日，2024 年 2 月补有后记。支持段落：“It's tempting to be impressed by the novelty of an interactive widget such as this, but the interactivity itself is not really the point.”；“Most interactive widgets dump the user in a sandbox and say 'figure it out for yourself'. Those are not explanations.”；“The reader is not forced to interact in order to learn. The reader interacts if they wants to go deeper, if they have piqued curiosity or unanswered questions.”（原文语法有误，此处照录）；2024 年后记：“It has now been applied so broadly that it seems to mean 'any article with interactive pictures'.”。需要说明的是，Victor 本人的定义比本文使用的更窄：“a written argument whose assertions are backed by explorable computational models, whose facts, assumptions, and calculations are all visible and editable”——读取于 [2026-09-03](https://web.archive.org/web/20260903183731/https://worrydream.com/ExplorableExplanations/)
- <span id="ref-lasseter-staging"></span>John Lasseter——原始出处：[“Principles of Traditional Animation Applied to 3D Computer Animation”](http://graphics.cs.cmu.edu/nsp/course/15-464/Fall05/papers/lasseter.pdf#page=4)，载《ACM SIGGRAPH Computer Graphics》第 21 卷第 4 期，1987 年 7 月，第 35 至 44 页（DOI [10.1145/37402.37407](https://doi.org/10.1145/37402.37407)）。此处读的是卡内基梅隆大学课程网站公开托管的副本，因为 ACM 数字图书馆的版本需要付费。Staging 是第 2.4 节，PDF 第 4 页、原刊第 38 页。支持段落原文（在 PDF 中跨行排布）：“Staging is the presentation of an idea so it is completely and unmistakably clear; this principle translates directly from 2-D hand drawn animation.”；“It is important, when staging an action, that only one idea be seen by the audience at a time. If a lot of action is happening at once, the eye does not know where to look and the main idea of the action will be 'upstaged' and overlooked.”；“Each idea or action must be staged in the strongest and the simplest way before going on to the next idea or action. The animator is saying, in effect, 'Look at this, now look at this, and now look at this.'”。Lasseter 在原刊第 35 页列出了十一条原则，并在全文中将其归于参考文献 [26]，即 Frank Thomas 与 Ollie Johnston 的《The Illusion of Life: Disney Animation》（1981），那才是这套原则最初的成文出处。该书没有可以公开阅读的版本，因此本文引用的是这篇 SIGGRAPH 论文的复述，也只从其中取句。另需说明，这份 PDF 是 OCR 扫描件，正文别处有个别字符识别错误，此处所引的几段是干净的——读取于 2026-09-03；最近的存档快照为 [2024-08-06](https://web.archive.org/web/20240806020326/http://graphics.cs.cmu.edu/nsp/course/15-464/Fall05/papers/lasseter.pdf)

### 作为做法示例引用的作品，而非权威

- <span id="ref-nyt-rent-buy"></span>《纽约时报》The Upshot——原始出处：[“Is It Better to Rent or Buy? A Financial Calculator.”](https://www.nytimes.com/interactive/2024/upshot/buy-rent-calculator.html#:~:text=Adjust%20these%20numbers%20to%20get%20an%20estimate%20for%20your%20situation)，作者 Mike Bostock、Shan Carter、Archie Tse 和 Francesca Paris，日期 2024 年 5 月 10 日。页面上标注“This calculator was updated in July 2025 to reflect current tax law”，页脚写明“This calculator was originally published in 2014.”。2014 年的旧网址现在会跳转到这个 2024 年的地址。支持段落：“Adjust these numbers to get an estimate for your situation. These are some of the most important factors in your decision, and they're the only ones we can't estimate for you.”；“Note that the 'winning choice' is the one that makes more financial sense over the long run, not necessarily what you can afford today.”。读取当天该页无需订阅即可打开，不过 nytimes.com 会间歇性地对自动请求返回 403，因此下面的存档快照是更稳妥的备用入口——读取于 2026-09-03；最近的存档快照为 [2026-07-26](https://web.archive.org/web/20260726072824/https://www.nytimes.com/interactive/2024/upshot/buy-rent-calculator.html)
- <span id="ref-nyt-255"></span>《纽约时报》The Upshot——原始出处：[“How the Recession Reshaped the Economy, in 255 Charts”](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html#:~:text=Each%20line%20on%20the%20chart%20represents%20a%20private-sector%20industry)，作者 Jeremy Ashkenas 和 Alicia Parlapiano，2014 年 6 月 5 日发布，6 月 6 日更新。支持段落：“How to read this chart”一节写道“Each line on the chart represents a private-sector industry and shows that industry's change in employment over the last decade. The lines are placed on the x axis (horizontally) based on the average wages paid in that industry.”。本文引作结论式标题例子的各节标题依次为“A Mixed Recovery”“More Bad — and Good — Jobs”“The Medical Economy”“A Long Housing Bust”“Made in America”“Black Gold Rush”“Digital Revolution”和“Grooming Boom”。该文另附有一则 2014 年 6 月 5 日的更正，说明此前的一处计算错误——读取于 2026-09-03；最近的存档快照为 [2026-01-12](https://web.archive.org/web/20260112033109/https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html)
- <span id="ref-polygons"></span>Vi Hart 与 Nicky Case——原始出处：[“Parable of the Polygons”](https://ncase.me/polygons/#:~:text=See%20what%20doesn%27t%20happen%3F)，一篇以 Thomas Schelling 1971 年论文《Dynamic Models of Segregation》为基础的可玩文章。支持段落：“use the slider to adjust the shapes' individual bias”；“world starts segregated. what happens when you lower the bias?”，随后是“See what doesn't happen? No change. No mixing back together. In a world where bias ever existed, being unbiased isn't enough!”；结论部分为“Small individual bias → Large collective bias.”。本文引用的是它的交互设计，也就是反事实移除这一模式，不涉及其社会科学结论——读取于 [2026-09-03](https://web.archive.org/web/20260903183924/https://ncase.me/polygons/)
- <span id="ref-pudding-pockets"></span>The Pudding，作者 Jan Diehm 和 Amber Thomas——原始出处：[“Women's Pockets are Inferior”](https://pudding.cool/2018/08/pockets/#:~:text=48%25%20shorter%20and%206.5%25%20narrower)，2018 年 8 月。支持段落：“On average, the pockets in women's jeans are 48% shorter and 6.5% narrower than men's pockets.”（据其 Methods 一节，样本为 20 个品牌共 80 条牛仔裤，腰围统一为 32 英寸）；“Heads up, you're about to experience some scroll-driven animations. If you'd like to skip that, you can jump ahead to the final state.”；“Click an item below to test the fit in each pocket.”以及“If the brand is faded, the item does not fit.”。同一页面上有该站的自我介绍：“The Pudding explains ideas debated in culture with visual essays.”——读取于 2026-09-03；最近的存档快照为 [2026-08-19](https://web.archive.org/web/20260819080447/https://pudding.cool/2018/08/pockets/)
- <span id="ref-distill-momentum"></span>Gabriel Goh，发表于 Distill——原始出处：[“Why Momentum Really Works”](https://distill.pub/2017/momentum/#:~:text=it%20fails%20to%20explain%20many%20important%20behaviors%20of%20momentum)，2017 年 4 月 4 日。支持段落：“This standard story isn't wrong, but it fails to explain many important behaviors of momentum. In fact, momentum can be understood far more precisely if we study it on the right model.”。该文的控件是两个带标签的滑块，“Step-size α”和“Momentum β”，全文所有图形都由它们驱动——读取于 2026-09-03；最近的存档快照为 [2026-08-27](https://web.archive.org/web/20260827070055/https://distill.pub/2017/momentum/)
- <span id="ref-ft-visual-vocabulary"></span>《金融时报》视觉新闻团队——原始出处：[Visual Vocabulary，位于金融时报 chart-doctor 仓库](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary#:~:text=select%20the%20optimal%20symbology%20for%20data%20visualisations)。支持段落：这张海报的用途是“to assist designers and journalists to select the optimal symbology for data visualisations”；“This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words.”；以及 Correlation 一节下的“Show the relationship between two or more variables. Be mindful that, unless you tell them otherwise, many readers will assume the relationships you show them to be causal (i.e. one causes the other).”。该 README 把图表类型归入九个关系类目，包括 deviation、correlation、ranking、distribution、change over time、magnitude、part-to-whole、spatial 以及 flow——读取于 [2026-09-03](https://web.archive.org/web/20260903184404/https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
- <span id="ref-explorables"></span>Explorable Explanations 目录站——原始出处：[explorabl.es](https://explorabl.es/#:~:text=a%20hub%20for%20learning%20through%20play)，一个收录可玩式讲解的目录。页面正文中的支持段落：“Welcome to Explorable Explanations, a hub for learning through play!”。Nicky Case 的[《The Evolution of Trust》](https://ncase.me/trust/)收录于此；2026-09-03 当天在浏览器中打开其首页，署名为“by nicky case, july 2017”，标注“playing time: 30 min”，首屏只有一个 PLAY 控件。该作品其余内容由脚本逐屏绘制，因此本文只描述它的形式，不对其中的具体交互作任何论断——读取于 [2026-09-03](https://web.archive.org/web/20260903184932/https://explorabl.es/)

### 工具，仅引用关于工具本身的事实

- <span id="ref-d3-what-is"></span>Observable（D3 的维护方）——原始出处：[“What is D3?”](https://d3js.org/what-is-d3#:~:text=It%20has%20no%20concept%20of)，官方文档。支持段落：“D3 is a low-level toolbox”；“D3 is not a charting library in the traditional sense. It has no concept of 'charts'. When you visualize data with D3, you compose a variety of primitives.”；“Don't get seduced by whizbang examples: many of them took an immense effort to implement!”；“D3 makes sense for media organizations such as The New York Times or The Pudding, where a single graphic may be seen by a million readers”；“On the other hand, D3 is overkill for throwing together a private dashboard or a one-off analysis.”；“Whereas a histogram in D3 might require 50 lines of code, Plot can do it in one!”。该页由厂商发布，本文只引用 D3 对自身的描述——读取于 [2026-09-03](https://web.archive.org/web/20260903183739/https://d3js.org/what-is-d3)
- <span id="ref-observable-plot"></span>Observable——原始出处：[Observable Plot 仓库](https://github.com/observablehq/plot#:~:text=focused%20on%20accelerating%20exploratory%20data%20analysis)。支持段落：“Observable Plot is a free, open-source, JavaScript library for visualizing tabular data, focused on accelerating exploratory data analysis. It has a concise, memorable, yet expressive API, featuring scales and layered marks in the *grammar of graphics* style.”——读取于 [2026-09-03](https://web.archive.org/web/20260903184554/https://github.com/observablehq/plot)
- <span id="ref-echarts"></span>Apache 软件基金会——原始出处：[Apache ECharts 仓库](https://github.com/apache/echarts#:~:text=highly%20customizable%20charts)。支持段落：“Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, interactive, and highly customizable charts to your commercial products.”——读取于 [2026-09-03](https://web.archive.org/web/20260903184551/https://github.com/apache/echarts)
- <span id="ref-d3-scale-chromatic"></span>D3——原始出处：[d3-scale-chromatic 仓库](https://github.com/d3/d3-scale-chromatic#:~:text=ColorBrewer)。支持段落：“This module provides sequential, diverging and categorical color schemes designed to work with d3-scale's scaleOrdinal and scaleSequential. Most of these schemes are derived from Cynthia A. Brewer's ColorBrewer.”——读取于 [2026-09-03](https://web.archive.org/web/20260903184415/https://github.com/d3/d3-scale-chromatic)
- <span id="ref-d3-annotation"></span>Susie Lu——原始出处：[d3-annotation 仓库](https://github.com/susielu/d3-annotation#:~:text=extend%20it%20to%20make%20custom%20annotations)。仓库简介：“Use d3-annotation with built-in annotation types, or extend it to make custom annotations. It is made for d3-v4 in SVG.”。完整文档位于 [d3-annotation.susielu.com](https://d3-annotation.susielu.com/)，该页正文由脚本渲染——读取于 [2026-09-03](https://web.archive.org/web/20260903184449/https://github.com/susielu/d3-annotation)
- <span id="ref-d3-sankey"></span>D3——原始出处：[d3-sankey 仓库](https://github.com/d3/d3-sankey#:~:text=the%20directed%20flow%20between%20nodes%20in%20an%20acyclic%20network)。支持段落：“Sankey diagrams visualize the directed flow between nodes in an acyclic network.”——读取于 2026-09-03；最近的存档快照为 [2026-08-05](https://web.archive.org/web/20260805223544/https://github.com/d3/d3-sankey)
- <span id="ref-gsap-flip"></span>GSAP（厂商文档）——原始出处：[Flip 插件文档](https://gsap.com/docs/v3/Plugins/Flip/#:~:text=make%20them%20look%20like%20they%20never%20moved)。支持段落：“Flip records the current position/size/rotation of your elements, you make whatever changes you want, and then Flip applies offsets to make them look like they never moved... Lastly FLIP animates the removal of those offsets!”；“'FLIP' is an animation technique that stands for 'First', 'Last', 'Invert', 'Play' and was coined by Paul Lewis.”——读取于 2026-09-03；最近的存档快照为 [2026-08-28](https://web.archive.org/web/20260828224750/https://gsap.com/docs/v3/Plugins/Flip/)
- <span id="ref-motion"></span>Motion（厂商文档）——原始出处：[motion.dev](https://motion.dev/#:~:text=Production-grade)。自我描述为面向 Web 的“Production-grade animation library”，MIT 许可，前身是 Framer Motion，列出的特性中包含布局动画和基于硬件加速的滚动联动动画——读取于 [2026-09-03](https://web.archive.org/web/20260903184802/https://motion.dev/)
- <span id="ref-scrollama"></span>Russell Goldenberg——原始出处：[Scrollama 仓库](https://github.com/russellsamora/scrollama#:~:text=lightweight%20JavaScript%20library%20for%20scrollytelling)。支持段落：“Scrollama is a modern & lightweight JavaScript library for scrollytelling using IntersectionObserver in favor of scroll events.”以及“The goal of this library is to provide a simple interface for creating scroll-driven interactives.”——读取于 2026-09-03；最近的存档快照为 [2026-08-21](https://web.archive.org/web/20260821224319/https://github.com/russellsamora/scrollama)
- <span id="ref-mermaid"></span>Mermaid——原始出处：[Mermaid 介绍页](https://mermaid.js.org/intro/#:~:text=renders%20Markdown-inspired%20text%20definitions)。支持段落：“It is a JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions to create and modify diagrams dynamically.”——读取于 2026-09-03；最近的存档快照为 [2026-08-30](https://web.archive.org/web/20260830050752/https://mermaid.js.org/intro/)
- <span id="ref-manim"></span>Grant Sanderson（3Blue1Brown）——原始出处：[manim 仓库](https://github.com/3b1b/manim#:~:text=designed%20for%20creating%20explanatory%20math%20videos)。支持段落：“Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.”。README 中说明该仓库“began as a personal project by the author of 3Blue1Brown for the purpose of animating those videos”，并且社区版是 2020 年从中分叉出去的——读取于 [2026-09-03](https://web.archive.org/web/20260903184619/https://github.com/3b1b/manim)
- <span id="ref-datawrapper-colors"></span>Datawrapper（厂商博客；Datawrapper 出售图表工具，因此这是从业者观点，不是中立权威）——原始出处：[“What to consider when choosing colors for data visualization”](https://www.datawrapper.de/blog/colors#:~:text=the%20most%20important%20color%20in%20Data%20Vis)，作者 Lisa Charlotte Muth，2018 年 5 月 29 日。支持段落：“Consider the color grey as the most important color in Data Vis. Using grey for less important elements in your chart makes your highlight colors (which should be reserved for your most important data points) stick out even more.”；“If you need more than seven colors in a chart, consider using another chart type or to group categories together.”；以及建议“Use an online tool or Datawrapper's automatic colorblind-check to make sure that color-blind users can distinguish the colors on your chart.”。该文现位于 datawrapper.de/blog/colors，旧的 blog.datawrapper.de 地址会跳转过来——读取于 [2026-09-03](https://web.archive.org/web/20260903184241/https://www.datawrapper.de/blog/colors)
- <span id="ref-pudding-process"></span>Ilia Blinderman，The Pudding——原始出处：[“How to Make Dope Shit, Part 1: Working with Data”](https://pudding.cool/process/how-to-make-dope-shit-part-1/)。这是该团队对自身工作流程的自述，属于自行发布的内容，本文引用的是他们怎样工作，而不是把它当作“什么才算好”的证据。支持段落：这类工作依赖“an odd grab-bag of skills — critical thought, design, writing, and programming”——读取于 [2026-09-03](https://web.archive.org/web/20260903184132/https://pudding.cool/process/how-to-make-dope-shit-part-1/)

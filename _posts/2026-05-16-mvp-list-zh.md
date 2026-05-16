---
title: "MVP List — 基于 GBrain 与 GStack 的家庭周末出行规划助手"
excerpt: "两个疲惫的爸妈，一个一岁的娃，还有一份越攒越长的「想去但还没去」清单。这是我们为自己写的一个小型规划 agent，让每个周六的开头不再是同一个问题：「那……今天去哪？」"
date: 2026-05-16
lang: zh
permalink: /blog/mvp-list-zh/
cover_image:
  src: /assets/blogposts/2026-05-16-mvp-list/deck-1-title-problem.png
  x: 384
  y: 0
  size: 864
og_image: /assets/blogposts/2026-05-16-mvp-list/deck-1-title-problem.png
translationKey: mvp-list-2026-05-16
categories:
  - blog
tags:
  - ai
  - gbrain
  - gstack
  - agents
  - product
  - family
---

![MVP List 标题卡片](/assets/blogposts/2026-05-16-mvp-list/deck-1-title-problem.png)

> 由周载南（Victor Zhou）与贾米雅（Mia Jia）在 YC GBrain & GStack 黑客松上构建，2026 年 5 月 16 日。联系我们：mvp@zzn.im。

我们家有个一岁的娃。我们还有一份慢慢累积起来的「想带她去的地方」清单——朋友顺口提到的一家面包店、有人在 Instagram 上打卡过的博物馆、一个一直「下次再去」的国家公园。

到了周五晚上，这份清单不再让人兴奋，反而让人压力很大。等到周六早上，我们已经累了，娃比算法吵得多，最后大概率还是去了上周去过的那个游乐场。

**MVP List** 就是我们为解决这个问题做的小工具。它不是一个旅游 App，而是一条悄悄在后台运行的个人规划流水线：它会记住我们曾经收藏过的所有地方，并自动在**每周三**为接下来的周末生成一两个具体的出行方案。

这篇文章来说说它是怎么工作的。

## 1. Curate（收集）—— 把长尾捞起来

![收集](/assets/blogposts/2026-05-16-mvp-list/deck-2-curate.png)

第一步是最「人」的一步。我们没打算用算法去「发现」新地点；我们继续做我们本来就在做的事——存一条 Instagram、截一张 TikTok、转发一个 Reddit 帖、把朋友的推荐复制下来。

按真实情况估计，一个像我们这样的家庭，在这套系统真正发挥作用之前，差不多会攒下 **100 到 1,000 个候选地点**。这条流水线从第一天起就是按这个量级设计的。**难的不是找到地方，难的是不把它们弄丢。**

## 2. Index（索引）—— 用 GBrain 结构化

![用 GBrain 索引](/assets/blogposts/2026-05-16-mvp-list/deck-3-index-gbrain.png)

收藏只是一个名字，而一次出行需要的是一份结构化的画像。所以每一个候选地点都会被送进 [GBrain](https://github.com/garrytan/gbrain)，补充足够多的字段，直到它能够和其他候选项一起被排序：

- **通用信息** —— Google Maps / Apple Maps ID、经纬度、营业时间、大致预算。
- **餐厅专项** —— 招牌菜、菜系类型、氛围（适合 date night 的安静感 vs. 推得动婴儿车的热闹感）。
- **景点专项** —— 博物馆或公园的主展品 / 主步道，再加一段三十秒能读完、给爸妈用的背景介绍。

上图展示了我们最常依赖的八个数据源：Google Maps、Apple Maps、Yelp、TripAdvisor、Lonely Planet、OpenTable、Instagram、Eater。GBrain 位于正中心，因为价值不在于「某一个」数据源，而在于有**一个可长期沉淀、可搜索、可索引**的地方，让所有这些来源最终都指向同一条规范化记录。

## 3. Trigger & Ranking（触发与排序）—— 每周三，从 1,000 漏到 2

![触发与排序漏斗](/assets/blogposts/2026-05-16-mvp-list/deck-4-trigger-ranking.png)

每周三早上，规划器会自己醒过来。

它会依次做四件事：

1. **Proposal（候选池）。** 把全部候选地点拉出来——一千个也没关系。
2. **Filtering（过滤）。** 去掉已经去过的、本周末不开门的、和本周日历不匹配的（如果周五排得很满，那周六我们就更想要一个安静点的安排）。
3. **Ranking（排序）。** 把剩下的按氛围契合度、距离、天气、是否对娃友好等维度打分。
4. **Two Options（两个方案）。** 漏成**两个具体的出行方案**，并排呈现。每个方案以两个**没去过**的新地方为主，剩下的位置要么再放一个新的，要么放一个我们已经去过并且喜欢的「老朋友」。

「两个方案」这个数量是故意的：一个像「命令」，三个又回到选择疲劳，**两个刚好是可以一边喝咖啡一边讨论的对话**。

## 4. Output（输出）—— 一份行程 + 一张当天的图

![输出](/assets/blogposts/2026-05-16-mvp-list/deck-5-output.png)

每个方案最终以一个小小的「包」交付：

- **一份行程（Agenda）**，按时间分块（10:00 博物馆、12:30 午餐、15:00 公园），并配上简短的 **「选址理由（Reason for Picking）」** 和 **「亮点（Highlights）」**，让另一半三十秒能扫完然后点头说「行」。
- **一张概览图（Overview Image）**，用 GPT Image 生成，从俯视角度展示路线地图、餐厅的招牌菜、主要景点的代表景观——基本上就是**一张「周六还没发生时的明信片」**。

那份行程是真正有用的产出，而那张图，才是真正能把我们从家里挪出门去的东西。

## 为什么需要 GBrain

![为什么 GBrain](/assets/blogposts/2026-05-16-mvp-list/deck-6-why-gbrain.png)

「周末规划」乍一听像是一条 LLM prompt 就能搞定的事，其实不是。

它是一个需要**多年记忆**的系统：要记住我们曾经收藏过的每一个地方、每一次去完之后的真实感受、哪些已经被我们「消耗」掉了、以及我们的口味**真正**是什么样（而不是我们嘴上说的那样）。这其实是四件事穿了一件大衣：**长期收集、长期记忆、可搜索的索引、个人化排序**。

GBrain 把这四件事放在了同一个地方。没有它，整条流水线就会塌回成一个「有美好初衷的 Notes App」。

## 为什么需要 TheHog

![为什么 TheHog](/assets/blogposts/2026-05-16-mvp-list/deck-7-why-thehog.png)

一个真实周末的另一半，是规划器**提前没法知道**的那些事。

一场山火封了一条路；那家面包店其实两个月前就关门了但商家信息没更新；周六下午突然下雨，原本的徒步变成了热可可咖啡馆。**[TheHog](https://thehog.ai)** 就是这条流水线的「实时网络层」：在方案最终敲定之前，它会去查天气、查路况、查道路封闭、查最新评论，并在**现实已经变了**的时候，相应地改写行程。

**GBrain 负责记住，TheHog 负责注意到。** 这两件事合起来，正好覆盖了我们之前所有版本都翻过车的那两个失败模式。

## 整个东西跑起来是什么样的

![MVP List 动画](/assets/blogposts/2026-05-16-mvp-list/mvp-list-animation.gif)

这就是 MVP 的全部：**一条流水线，不是一个产品。** Curate → Index → Trigger & Rank → Output，跑在一个安静的周三 cron 上，由 GBrain 提供记忆、由 TheHog 提供对真实世界的感知。

如果你也是个小宝宝的爸妈，看到这些场景觉得很熟悉——或者你只是想要那份 deck——欢迎来信 **mvp@zzn.im**。我们正在维护一个小名单，准备让最早一批家庭试用下一个版本。

—— Victor & Mia

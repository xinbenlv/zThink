---
title: "如何准备软件工程师的系统面试——资料篇"
excerpt: "准备系统设计面试该读哪些经典教材：从 DDIA 打根基，到架构权衡、领域建模、可靠性和经典模式，最后读 MIT 分布式系统课程的原始论文。每本书的作者、版本和中文版都已对照出版方页面核实。"
date: 2026-10-30
lang: zh
author: aileen-wright
categories: [engineering]
tags: [system-design, interview, books]
translationKey: system-design-interview-resources
published: true
cover_image:
  src: /assets/blogposts/2026-10-30-system-design-interview-resources/sdi-00-cover-zh.jpg
  x: 520
  y: 0
  size: 630
og_image: /assets/blogposts/2026-10-30-system-design-interview-resources/sdi-00-cover-zh.jpg
---

系统设计面试考的是设计大型软件系统的功夫：数据怎么存，请求怎么分发，机器坏了怎么办，以及每个选择要付出什么代价。这些功夫来自这个领域的经典教材。这篇文章只收教材和经典著作，不收专门讲面试题的书。书单分成六组，最后给出我建议的阅读顺序。

每本书的作者、版本和出版时间，我都在 2026 年 10 月 30 日对照了出版社或作者本人的页面；中文版的信息来自豆瓣读书的书目页和作者本人的页面。书单里有几本出了新版，买书之前最好再确认一下版本。

## 第一组书讲数据系统和分布式系统的原理

![一座正在打地基的房子，石块砌成的地基里嵌着一本蓝色封面的厚书，当作基石](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-01-foundation.jpg)

### 《Designing Data-Intensive Applications》是整份书单的根基

Martin Kleppmann 的《Designing Data-Intensive Applications》，大家习惯简称 DDIA。第二版的目录从数据模型、存储和编码讲起，再讲到[复制、分片、事务和分布式系统的种种麻烦](#ref-oreilly-ddia2-toc)。系统设计面试里常被追问的取舍，大多能在这几章里找到原理。

DDIA 现在有两个版本。第二版由 Kleppmann 和 Chris Riccomini 合写，O'Reilly 的页面把[出版时间标为 2026 年 2 月](#ref-oreilly-ddia2)，Kleppmann 个人主页的著作列表写的是 [2026 年 3 月](#ref-kleppmann-home)，两处差一个月。第一版由 Kleppmann 一人撰写，[2017 年 3 月出版](#ref-oreilly-ddia1)，中文版[《数据密集型应用系统设计》](#ref-ddia-translations)由中国电力出版社在 [2018 年 9 月出版](#ref-douban-ddia)，译自第一版。读得惯英文的读者，我建议直接读第二版；只读中文的读者，第一版的中文版仍然够用，书里讲的基本原理没有过时。

### 《Understanding Distributed Systems》适合先过一遍全局

Roberto Vitillo 的《Understanding Distributed Systems》比 DDIA 薄。作者网站上写着，这本书现在是[第二版，共 33 章、328 页](#ref-uds-edition)，全书分成[通信、协调、扩展性、韧性和可维护性五个部分](#ref-uds-parts)。前两章可以在作者网站上[免费阅读](#ref-uds-free)。

作者在网站上说，这本书[重广度、不重深度](#ref-uds-breadth)。网络协议栈、数据一致性模型、扩展性和可靠性模式、可观测性，后端工程师要用到的知识大致都讲到了。工作经验少、没做过大规模后端的读者，可以先读这本，再啃 DDIA。

### 《Database Internals》往存储引擎深处再走一步

Alex Petrov 的《Database Internals》由 O'Reilly 在 [2019 年 10 月出版](#ref-oreilly-dbint)。作者网站介绍，全书分为[存储引擎和分布式系统两部分](#ref-databass-parts)：前一部分讲 B 树、LSM 树、预写日志这些数据结构，后一部分讲故障检测、领导者选举、一致性和共识算法。

面试很少问到这么深。但面试官追问“这个数据库为什么写得快”“你选的存储为什么适合这个读写比例”的时候，读过这本书的人能答到数据结构那一层。

## 第二组书帮读者建立架构权衡的框架

![绘图桌上的一架黄铜天平，一边放着一栋大楼的模型，另一边放着一群相连小房子的模型，两边几乎持平](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-02-tradeoffs.jpg)

### 《Fundamentals of Software Architecture》教人系统地比较架构风格

Mark Richards 和 Neal Ford 的《Fundamentals of Software Architecture》已经出到第二版，O'Reilly 在 [2025 年 3 月出版](#ref-oreilly-fosa2)，比第一版[新增了五章](#ref-oreilly-fosa2-new)。全书前几章先定义“架构特征”，也就是扩展性、可用性这类功能以外的要求，然后逐一讲[微服务、模块化单体、微内核、分层等架构风格](#ref-oreilly-fosa2-styles)。系统设计面试最常见的追问是“为什么选这个方案而不选那个”，这本书给了一套比较方案的词汇和步骤。

### 《Software Architecture: The Hard Parts》专讲没有标准答案的难题

《Software Architecture: The Hard Parts》的作者有四位：Neal Ford、Mark Richards、Pramod Sadalage 和 Zhamak Dehghani，O'Reilly 在 [2021 年 10 月出版](#ref-oreilly-hardparts)。第一章的标题就叫[“没有‘最佳实践’的时候怎么办？”](#ref-oreilly-hardparts-ch1)。全书讨论[服务该拆多细、服务之间的契约怎么管、分布式事务怎么处理](#ref-oreilly-hardparts-topics)，这几样也是面试里容易被追问的地方。

### 两本讲代码层面设计的书可以选读

下面两本书讲的是模块和代码层面的设计，和分布式系统的关系不大，属于选读。

Robert C. Martin 的《Clean Architecture》由 Pearson 在 [2017 年 9 月出版](#ref-informit-cleanarch)，目录依次是[设计原则、组件原则和架构](#ref-informit-cleanarch-toc)三大部分，其中一章专讲怎么划定边界。中文版叫[《架构整洁之道》](#ref-douban-cleanarch)，电子工业出版社 2018 年出版，孙宇聪翻译。

斯坦福大学教授 John Ousterhout 的《A Philosophy of Software Design》在 [2021 年 7 月出了第二版](#ref-aposd-2nd)。第二版在两章里新增了几节，专门拿本书的观点和 Robert Martin 的《Clean Code》对比，作者说两人[在函数长度和注释的作用这些问题上分歧很大](#ref-aposd-cleancode)。两本书对照着读，比只读一本更能看清设计取舍。

## 第三组书讲领域建模和服务拆分

![一张手绘的小镇地图，彩色铅笔把小镇分成几个街区，每个街区里放着一座小木屋](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-03-boundaries.jpg)

面试题一旦涉及“这个系统要拆成哪几个服务”，就要用到领域建模的概念。

Eric Evans 的《Domain-Driven Design》由 Addison-Wesley 在 [2003 年 8 月出版](#ref-informit-ddd)，Evans 任教的培训公司 Domain Language 把这本书称作[“蓝皮书”（The Big Blue Book）](#ref-domainlanguage-ddd)。通用语言（Ubiquitous Language）、聚合（Aggregate）、限界上下文（Bounded Context）这些面试里常听到的概念，[书里都有专门的章节](#ref-informit-ddd-toc)。中文版[《领域驱动设计：软件核心复杂性应对之道》](#ref-douban-ddd)由人民邮电出版社出版，豆瓣上的版本是 2016 年 6 月。

Vaughn Vernon 的《Implementing Domain-Driven Design》由 Addison-Wesley 在 [2013 年 2 月出版](#ref-informit-iddd)，讲的是怎么在项目里落实 Evans 提出的概念。中文版[《实现领域驱动设计》](#ref-douban-iddd)由电子工业出版社在 2014 年出版，滕云翻译。

Sam Newman 的《Building Microservices》第二版由 O'Reilly 在 [2021 年 8 月出版](#ref-oreilly-bm2)。作者说第二版是对第一版的[完全重写](#ref-newman-bm2-rewrite)，第一章可以在作者网站上[免费下载](#ref-newman-bm2-free)。中文版[《微服务设计（第2版）》](#ref-douban-bm2)由人民邮电出版社在 2024 年 4 月出版。

## 第四组书讲可靠性和上线运维

![一艘帆船的剖面图，船舱被竖直的隔舱壁分成几格，进水的舱格被隔住，船身仍然平稳，远处有一座灯塔](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-04-bulkheads.jpg)

### Google 免费公开了三本 SRE 的书

Google 的《Site Reliability Engineering》第一版由 O'Reilly 在 [2016 年 4 月出版](#ref-oreilly-sre1)。Google 在 sre.google 上[免费公开了这本书的全文](#ref-sre-book-toc)，同样可以在线读全文的还有配套的[《The Site Reliability Workbook》](#ref-sre-workbook-toc)和[《Building Secure & Reliable Systems》](#ref-sre-books-bsrs)。服务等级目标（SLO）、前端和数据中心的负载均衡、过载处理这些面试常见话题，书里都有专门的章节。

Google 现在又推出了[完全重写的第二版](#ref-sre-books-2nd)。sre.google 书目页上，第二版只给了 Google Books 的购买链接，没有在线阅读的入口；免费公开的仍然是第一版。第一版的中文版叫[《SRE：Google运维解密》](#ref-douban-sre)，电子工业出版社 2016 年出版，孙宇聪翻译。

### 《Release It!》讲系统在生产环境里怎么出故障

Michael Nygard 的《Release It!》第二版由 Pragmatic Bookshelf 在 [2018 年 1 月出版](#ref-pragprog-releaseit)。书里有一章专讲[稳定性模式](#ref-pragprog-releaseit-patterns)，包括超时、断路器和舱壁隔离。面试时被问到“下游服务挂了怎么办”，这一章的模式可以直接拿来回答。

## 第五组书是经典的模式目录，适合查阅

![图书馆的卡片目录柜拉开一个抽屉，桌上摊着几张只画了方框和箭头的卡片，旁边有台灯和眼镜](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-05-catalog.jpg)

这三本书出版时间都在二十年以上，书里的技术例子比较老。我把它们当成工具书：遇到不熟悉的模式名，再翻到对应的章节去读。

Martin Fowler 的《Patterns of Enterprise Application Architecture》出版于 [2002 年](#ref-fowler-poeaa)。Fowler 介绍，这本书前一部分是约 100 页的教程，[其余部分是四十个左右模式的参考](#ref-fowler-poeaa-patterns)，主题包括[企业应用怎么分层、怎么组织领域逻辑、怎么把领域逻辑接到关系数据库上](#ref-fowler-poeaa-topics)。

Gregor Hohpe 和 Bobby Woolf 的《Enterprise Integration Patterns》由 Addison-Wesley 在 [2003 年 10 月出版](#ref-informit-eip)，收录了 [65 个集成模式](#ref-eip-site)，讲的是系统之间怎么通过消息传递协作。网站上的模式目录列有[发布订阅通道、死信通道和幂等接收者](#ref-eip-toc)等模式，面试里设计消息队列时常用到这些概念。

Erich Gamma、Richard Helm、Ralph Johnson 和 John Vlissides 合写的《Design Patterns》由 Addison-Wesley 在 [1994 年 10 月出版](#ref-informit-gof)。这本书讲面向对象代码层面的模式，对系统设计面试帮助有限。中文版[《设计模式：可复用面向对象软件的基础》](#ref-douban-gof)由机械工业出版社在 2000 年出版。

## 第六组资料是公开课程和原始论文

![一本摊开的速写本，同一座桥被反复画了很多遍，旁边立着一个沙漏](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-06-practice.jpg)

MIT 的分布式系统课程 6.5840（[原课号 6.824](#ref-mit-6824-2022)）把课表、阅读材料和实验都公开在网上。2026 年春季学期的课表要求学生[课前读 GFS（2003）](#ref-mit-schedule-gfs)、[Raft（2014）](#ref-mit-schedule-raft)和 [Spanner（2012）](#ref-mit-schedule-spanner)等论文，实验要动手实现 MapReduce 和 Raft。想知道 DDIA 里那些原理出自哪篇论文，可以照着这份课表去读原文。

## 我建议按这个顺序读

1. **先读 DDIA 打根基。** 工作经验少的读者，可以先用《Understanding Distributed Systems》过一遍全局，再读 DDIA。
2. **再读《Fundamentals of Software Architecture》，建立比较架构方案的框架。** 读完之后，回答“为什么选这个方案”就有了章法。
3. **按需选读领域驱动设计、微服务和 SRE 的书。** 目标岗位偏业务系统，多读 Evans、Vernon 和 Newman；偏基础设施，多读 SRE 的书、《Release It!》和《Database Internals》。
4. **最后照着 MIT 6.5840 的课表读原始论文。** 读 GFS、Raft、Spanner 这些论文的时候，回头对照 DDIA 的相应章节，弄清楚书里的结论从哪里来。

第五组的模式书不必通读，遇到不熟悉的模式名再去查。时间紧的读者，最少读 DDIA 和《Fundamentals of Software Architecture》；时间充裕的读者，再做几个 MIT 课程的实验，面试时说起复制和共识会更有底气。

## 参考来源

出版社页面、作者本人的页面和课程主页是一手来源。豆瓣读书是书目数据库，只用来核实中文版信息。

**数据系统和分布式系统**

- <span id="ref-oreilly-ddia2"></span>O'Reilly — [Designing Data-Intensive Applications, 2nd Edition](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)，书目信息：“by Martin Kleppmann, Chris Riccomini”，“February 2026”，672 页 — fetched [2026-10-30](https://web.archive.org/web/20260616232347/https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
- <span id="ref-oreilly-ddia2-toc"></span>O'Reilly — [Designing Data-Intensive Applications, 2nd Edition，目录](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)，第 3 至 9 章：“Data Models and Query Languages”“Storage and Retrieval”“Encoding and Evolution”“Replication”“Sharding”“Transactions”“The Trouble with Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20260616232347/https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
- <span id="ref-oreilly-ddia1"></span>O'Reilly — [Designing Data-Intensive Applications（第一版）](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/)，书目信息：“by Martin Kleppmann”，“March 2017”，616 页 — fetched 2026-10-30（无存档）
- <span id="ref-kleppmann-home"></span>Martin Kleppmann 个人主页 — [著作列表](https://martin.kleppmann.com/#:~:text=2nd%20edition%20co-authored%20with%20Chris%20Riccomini%20appeared%20in%202026)，原文：“Designing Data-Intensive Applications, 2nd Edition. O'Reilly Media, March 2026.” — fetched [2026-10-30](https://web.archive.org/web/20261019064754/https://martin.kleppmann.com/)
- <span id="ref-ddia-translations"></span>dataintensive.net — [DDIA 译本列表，Chinese (Simplified) 一项](https://dataintensive.net/translations.html#:~:text=%E6%95%B0%E6%8D%AE%E5%AF%86%E9%9B%86%E5%9E%8B%E5%BA%94%E7%94%A8%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1)，原文：“数据密集型应用系统设计 ISBN: 9787519821968” — fetched [2026-10-30](https://web.archive.org/web/20260920180400/https://dataintensive.net/translations.html)
- <span id="ref-douban-ddia"></span>豆瓣读书 — [《数据密集型应用系统设计》书目](https://book.douban.com/subject/30329536/)，出版社：中国电力出版社，出版年：2018-9-1，原作名：Designing Data-Intensive Applications — fetched [2026-10-30](https://web.archive.org/web/20261023173030/https://book.douban.com/subject/30329536/)
- <span id="ref-uds-edition"></span>Roberto Vitillo — [Understanding Distributed Systems 官网，版本说明](https://understandingdistributed.systems/#:~:text=2nd%20edition%20with%2033%20packed%20chapters%20and%20328%20pages)，原文：“2nd edition with 33 packed chapters and 328 pages in PDF and EPUB format” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-parts"></span>Roberto Vitillo — [Understanding Distributed Systems 官网，全书结构](https://understandingdistributed.systems/#:~:text=The%20book%20is%20divided%20into%205%20parts)，原文：“The book is divided into 5 parts: communication, coordination, scalability, resiliency, and maintainability.” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-free"></span>Roberto Vitillo — [Understanding Distributed Systems 官网，试读](https://understandingdistributed.systems/#:~:text=Read%20the%20first%20two%20chapters%20for%20free)，原文：“Read the first two chapters for free” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-breadth"></span>Roberto Vitillo — [Understanding Distributed Systems 官网，适合的读者](https://understandingdistributed.systems/#:~:text=looking%20for%20depth%20rather%20than%20breadth)，原文：“As an expert, you are likely looking for depth rather than breadth, and this book focuses more on the latter”；同页：“you need to be familiar with the network stack, data consistency models, scalability and reliability patterns, observability best practices, and much more” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-oreilly-dbint"></span>O'Reilly — [Database Internals](https://www.oreilly.com/library/view/database-internals/9781492040330/)，书目信息：“by Alex Petrov”，“October 2019”，370 页 — fetched [2026-10-30](https://web.archive.org/web/20260601001713/https://www.oreilly.com/library/view/database-internals/9781492040330/)
- <span id="ref-databass-parts"></span>Alex Petrov — [Database Internals 官网，全书结构](https://www.databass.dev/#:~:text=The%20book%20consists%20of%20two%20parts)，原文：“The book consists of two parts: Storage Engines and Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20261012194439/https://www.databass.dev/)

**软件架构**

- <span id="ref-oreilly-fosa2"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)，书目信息：“by Mark Richards, Neal Ford”，“March 2025”，546 页 — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-fosa2-new"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition，内容简介](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/#:~:text=with%20five%20new%20chapters)，原文：“This updated edition provides a comprehensive overview of software architecture's many aspects, with five new chapters covering the latest insights from the field.” — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-fosa2-styles"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition，内容简介](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/#:~:text=Microservices%2C%20modular%20monoliths%2C%20microkernels%2C%20layered%20architectures)，原文：“Architecture styles and patterns: Microservices, modular monoliths, microkernels, layered architectures, and many more”；目录第 4 章：“Architectural Characteristics Defined” — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-hardparts"></span>O'Reilly — [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)，书目信息：“by Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani”，“October 2021”，462 页 — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-oreilly-hardparts-ch1"></span>O'Reilly — [Software Architecture: The Hard Parts，目录第 1 章](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/#:~:text=What%20Happens%20When%20There%20Are%20No)，原文：“1. What Happens When There Are No ‘Best Practices’?” — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-oreilly-hardparts-topics"></span>O'Reilly — [Software Architecture: The Hard Parts，内容简介](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/#:~:text=how%20to%20determine%20service%20granularity)，原文：“they examine everything from how to determine service granularity, manage workflows and orchestration, manage and decouple contracts, and manage distributed transactions” — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-informit-cleanarch"></span>InformIT（Pearson）— [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166#:~:text=Published%20Sep%2010%2C%202017)，书目信息：“By Robert C. Martin”，“Published Sep 10, 2017 by Pearson” — fetched [2026-10-30](https://web.archive.org/web/20261003133541/https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166)
- <span id="ref-informit-cleanarch-toc"></span>InformIT（Pearson）— [Clean Architecture，目录](https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166#:~:text=Part%20III%3A%20Design%20Principles)，原文：“Part III: Design Principles”“Part IV: Component Principles”“Part V: Architecture”，以及章节“Boundaries: Drawing Lines” — fetched [2026-10-30](https://web.archive.org/web/20261003133541/https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166)
- <span id="ref-douban-cleanarch"></span>豆瓣读书 — [《架构整洁之道》书目](https://book.douban.com/subject/30333919/)，译者：孙宇聪，出版社：电子工业出版社，出版年：2018-9，原作名：Clean Architecture — fetched [2026-10-30](https://web.archive.org/web/20260829035057/https://book.douban.com/subject/30333919/)
- <span id="ref-aposd-2nd"></span>John Ousterhout — [Software Design Book 页面](https://web.stanford.edu/~ouster/cgi-bin/book.php#:~:text=In%20July%20of%202021%20I%20released%20the%20Second%20Edition)，原文：“In July of 2021 I released the Second Edition of A Philosophy of Software Design.”页眉署名：“John Ousterhout, Professor, Department of Computer Science” — fetched [2026-10-30](https://web.archive.org/web/20260930000611/https://www.web.stanford.edu/~ouster/cgi-bin/book.php)
- <span id="ref-aposd-cleancode"></span>John Ousterhout — [Software Design Book 页面，与 Clean Code 的比较](https://web.stanford.edu/~ouster/cgi-bin/book.php#:~:text=we%20have%20significant%20differences%20of%20opinion)，原文：“we have significant differences of opinion on topics such as the length of methods and the role of comments” — fetched [2026-10-30](https://web.archive.org/web/20260930000611/https://www.web.stanford.edu/~ouster/cgi-bin/book.php)

**领域建模和服务拆分**

- <span id="ref-informit-ddd"></span>InformIT（Addison-Wesley）— [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217#:~:text=Published%20Aug%2020%2C%202003)，书目信息：“By Eric Evans”，“Published Aug 20, 2003 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20261018122420/https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217)
- <span id="ref-informit-ddd-toc"></span>InformIT（Addison-Wesley）— [Domain-Driven Design，目录](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217#:~:text=UBIQUITOUS%20LANGUAGE)，目录中的小节：“UBIQUITOUS LANGUAGE”“AGGREGATES”“BOUNDED CONTEXT” — fetched [2026-10-30](https://web.archive.org/web/20261018122420/https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217)
- <span id="ref-domainlanguage-ddd"></span>Domain Language — [DDD Resources](https://www.domainlanguage.com/ddd/#:~:text=The%20Big%20Blue%20Book)，原文：“The Big Blue Book. Domain-Driven Design, by Eric Evans, provides a broad framework for making design decisions”；同页：“In addition to offering training, Eric Evans and the other instructors are active speakers and writers” — fetched [2026-10-30](https://web.archive.org/web/20261005171737/https://www.domainlanguage.com/ddd/)
- <span id="ref-douban-ddd"></span>豆瓣读书 — [《领域驱动设计》书目](https://book.douban.com/subject/26819666/)，译者：赵俐、盛海艳、刘霞，出版社：人民邮电出版社，出版年：2016-6-1 — fetched [2026-10-30](https://web.archive.org/web/20260419090910/https://book.douban.com/subject/26819666/)
- <span id="ref-informit-iddd"></span>InformIT（Addison-Wesley）— [Implementing Domain-Driven Design](https://www.informit.com/store/implementing-domain-driven-design-9780321834577#:~:text=Published%20Feb%206%2C%202013)，书目信息：“By Vaughn Vernon”，“Published Feb 6, 2013 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20260710111237/https://www.informit.com/store/implementing-domain-driven-design-9780321834577)
- <span id="ref-douban-iddd"></span>豆瓣读书 — [《实现领域驱动设计》书目](https://book.douban.com/subject/25844633/)，译者：滕云，出版社：电子工业出版社，出版年：2014-3 — fetched [2026-10-30](https://web.archive.org/web/20240807224953/https://book.douban.com/subject/25844633/)
- <span id="ref-oreilly-bm2"></span>O'Reilly — [Building Microservices, 2nd Edition](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/)，书目信息：“by Sam Newman”，“August 2021”，612 页 — fetched [2026-10-30](https://web.archive.org/web/20260628082224/https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/)
- <span id="ref-newman-bm2-rewrite"></span>Sam Newman — [Building Microservices, 2nd Edition 页面](https://samnewman.io/books/building_microservices_2nd_edition/#:~:text=The%202nd%20edition%20is%20a%20complete%20rewrite)，原文：“The 2nd edition is a complete rewrite of the previous best selling edition” — fetched [2026-10-30](https://web.archive.org/web/20260919013741/https://samnewman.io/books/building_microservices_2nd_edition/)
- <span id="ref-newman-bm2-free"></span>Sam Newman — [Building Microservices, 2nd Edition 页面，免费章节](https://samnewman.io/books/building_microservices_2nd_edition/#:~:text=The%20first%20chapter%20of%20the%20book%20is%20available%20for%20free)，原文：“The first chapter of the book is available for free.” — fetched [2026-10-30](https://web.archive.org/web/20260919013741/https://samnewman.io/books/building_microservices_2nd_edition/)
- <span id="ref-douban-bm2"></span>豆瓣读书 — [《微服务设计（第2版）》书目](https://book.douban.com/subject/36855388/)，译者：钟健鑫、张沙沙、智伟，出版社：人民邮电出版社，出版年：2024-4-15 — fetched [2026-10-30](https://web.archive.org/web/20260513074324/https://book.douban.com/subject/36855388/)

**可靠性和运维**

- <span id="ref-oreilly-sre1"></span>O'Reilly — [Site Reliability Engineering（第一版）](https://www.oreilly.com/library/view/site-reliability-engineering/9781491929117/)，书目信息：“by Niall Richard Murphy, Betsy Beyer, Chris Jones, Jennifer Petoff”，“April 2016” — fetched [2026-10-30](https://web.archive.org/web/20260706162528/https://www.oreilly.com/library/view/site-reliability-engineering/9781491929117/)
- <span id="ref-sre-book-toc"></span>Google — [Site Reliability Engineering 在线全文目录](https://sre.google/sre-book/table-of-contents/)，第 4 章“Service Level Objectives”、第 19 章“Load Balancing at the Frontend”、第 20 章“Load Balancing in the Datacenter”、第 21 章“Handling Overload” — fetched [2026-10-30](https://web.archive.org/web/20261023010553/https://sre.google/sre-book/table-of-contents/)
- <span id="ref-sre-workbook-toc"></span>Google — [The Site Reliability Workbook 在线全文目录](https://sre.google/workbook/table-of-contents/)，第 2 章“Implementing SLOs” — fetched [2026-10-30](https://web.archive.org/web/20261002021106/https://sre.google/workbook/table-of-contents/)
- <span id="ref-sre-books-bsrs"></span>Google — [sre.google 书目页，Building Secure & Reliable Systems 一项](https://sre.google/books/#:~:text=Building%20Secure%20%26%20Reliable%20Systems)，该项附有“Read online”链接 — fetched [2026-10-30](https://web.archive.org/web/20261015174024/https://sre.google/books/)
- <span id="ref-sre-books-2nd"></span>Google — [sre.google 书目页，第二版](https://sre.google/books/#:~:text=In%20this%20completely%20rewritten%20edition)，原文：“In this completely rewritten edition, we explore current SRE practices and how they've evolved in the decade since the book's initial publication”；该项只附有“Buy from Google Books”链接 — fetched [2026-10-30](https://web.archive.org/web/20261015174024/https://sre.google/books/)
- <span id="ref-douban-sre"></span>豆瓣读书 — [《SRE：Google运维解密》书目](https://book.douban.com/subject/26875239/)，译者：孙宇聪，出版社：电子工业出版社，出版年：2016-10-1，原作名：Site Reliability Engineering: How Google Runs Production Systems — fetched [2026-10-30](https://web.archive.org/web/20240720103207/https://book.douban.com/subject/26875239/)
- <span id="ref-pragprog-releaseit"></span>The Pragmatic Bookshelf — [Release It! Second Edition](https://pragprog.com/titles/mnee2/release-it-second-edition/)，书目信息：“by Michael Nygard”，Pages: 376，Published: January 2018 — fetched [2026-10-30](https://web.archive.org/web/20260919013804/https://pragprog.com/titles/mnee2/release-it-second-edition/)
- <span id="ref-pragprog-releaseit-patterns"></span>The Pragmatic Bookshelf — [Release It! Second Edition，目录](https://pragprog.com/titles/mnee2/release-it-second-edition/#:~:text=Stability%20Patterns)，章节“Stability Patterns”下列有“Timeouts”“Circuit Breaker”“Bulkheads” — fetched [2026-10-30](https://web.archive.org/web/20260919013804/https://pragprog.com/titles/mnee2/release-it-second-edition/)

**经典模式**

- <span id="ref-fowler-poeaa"></span>Martin Fowler — [Patterns of Enterprise Application Architecture 书籍页](https://martinfowler.com/books/eaa.html)，书目信息：“by Martin Fowler, with Dave Rice, Matthew Foemmel, Edward Hieatt, Robert Mee, and Randy Stafford”，“2002” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-fowler-poeaa-patterns"></span>Martin Fowler — [Patterns of Enterprise Application Architecture 书籍页，全书结构](https://martinfowler.com/books/eaa.html#:~:text=the%20reference%20to%20forty%20or%20so%20patterns)，原文：“The first part is a short (100 page) tutorial on enterprise application architecture. The bulk of the book is the reference to forty or so patterns.” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-fowler-poeaa-topics"></span>Martin Fowler — [Patterns of Enterprise Application Architecture 书籍页，主题](https://martinfowler.com/books/eaa.html#:~:text=how%20to%20layer%20an%20enterprise%20application)，原文：“The main topic areas are: how to layer an enterprise application, how to organize domain logic, how to tie that logic to a relational database” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-informit-eip"></span>InformIT（Addison-Wesley）— [Enterprise Integration Patterns](https://www.informit.com/store/enterprise-integration-patterns-designing-building-9780321200686#:~:text=Published%20Oct%2010%2C%202003)，书目信息：“By Gregor Hohpe, Bobby Woolf”，“Published Oct 10, 2003 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20260614033829/https://www.informit.com/store/enterprise-integration-patterns-designing-building-9780321200686)
- <span id="ref-eip-site"></span>Gregor Hohpe — [Enterprise Integration Patterns 网站](https://www.enterpriseintegrationpatterns.com/#:~:text=This%20pattern%20language%20consisting%20of%2065%20integration%20patterns)，原文：“This pattern language consisting of 65 integration patterns helps developers design and build distributed applications or integrate existing ones.” — fetched [2026-10-30](https://web.archive.org/web/20261005180019/https://www.enterpriseintegrationpatterns.com/)
- <span id="ref-eip-toc"></span>Gregor Hohpe — [Enterprise Integration Patterns 模式目录](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html)，目录中列有“Publish-Subscribe Channel”“Dead Letter Channel”“Idempotent Receiver” — fetched [2026-10-30](https://web.archive.org/web/20261019172151/https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html)
- <span id="ref-informit-gof"></span>InformIT（Addison-Wesley）— [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610#:~:text=Published%20Oct%2031%2C%201994)，书目信息：“By Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides”，“Published Oct 31, 1994 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20261010172538/https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610)
- <span id="ref-douban-gof"></span>豆瓣读书 — [《设计模式：可复用面向对象软件的基础》书目](https://book.douban.com/subject/1052241/)，译者：李英军等，出版社：机械工业出版社，出版年：2000-9 — fetched [2026-10-30](https://web.archive.org/web/20260923015143/https://book.douban.com/subject/1052241/)

**公开课程**

- <span id="ref-mit-6824-2022"></span>MIT — [6.824 课程主页，Spring 2022](http://nil.csail.mit.edu/6.824/2022/)，页面标题：“6.824: Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20260208023554/http://nil.csail.mit.edu/6.824/2022/)
- <span id="ref-mit-schedule-gfs"></span>MIT 6.5840 — [Spring 2026 课表，第 3 讲](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20GFS%20%282003%29)，原文：“LEC 3 (fk): GFS. Preparation: Read GFS (2003)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)
- <span id="ref-mit-schedule-raft"></span>MIT 6.5840 — [Spring 2026 课表，第 6 讲](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20Raft%20%28extended%29%20%282014%29)，原文：“LEC 6 (fk): Fault Tolerance: Raft (1). Preparation: Read Raft (extended) (2014)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)
- <span id="ref-mit-schedule-spanner"></span>MIT 6.5840 — [Spring 2026 课表，第 12 讲](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20Spanner%20%282012%29)，原文：“LEC 12 (rtm): Spanner. Preparation: Read Spanner (2012)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)

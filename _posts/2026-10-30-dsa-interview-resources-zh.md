---
title: "如何准备软件工程师的算法与数据结构面试——资料篇"
excerpt: "算法面试只看经典资料：一门课、一本入门教材、两本案头参考书、三本面试专书和一份题单。"
date: 2026-10-30
lang: zh
author: aileen-wright
categories: [blog]
tags: [algorithms, data-structures, interview, books]
translationKey: dsa-interview-resources
published: true
og_image: /assets/blogposts/2026-10-30-dsa-interview-resources/01-four-steps.jpg
cover_image:
  src: /assets/blogposts/2026-10-30-dsa-interview-resources/01-four-steps.jpg
  x: 512
  y: 0
  size: 1024
---

这份清单只收经典。每一项都已经用了很多年，每一项在准备过程里也各有分工。我按建议的使用顺序分成四步：先打基础，再备两本参考书，然后读面试专书，最后靠一份题单天天练。

清单一共八项，不必全读。每一步挑一项就够了。

![四级浅色石阶：最低一级放着台灯和笔记本，第二级立着两本厚参考书，第三级叠着三本夹书签的面试书，最高一级是一本画满对勾的台历](/assets/blogposts/2026-10-30-dsa-interview-resources/01-four-steps.jpg)

## 第一步：一门课或一本教材打好基础

**MIT 6.006 Introduction to Algorithms（2020 年春季）。** 这门课由 Erik Demaine、Jason Ku 和 Justin Solomon [讲授](#ref-mit-6006)，MIT OpenCourseWare 公开了课程录像、讲义、习题和考试。没上过算法课，或者算法课已经上了很多年的读者，适合从这门课开始。录像要看，习题也要做。

**《Algorithms》第 4 版（Robert Sedgewick、Kevin Wayne）。** 这本书的[配套网站](#ref-algs4)链接了 Princeton 在 Coursera 上的两门课：Algorithms Part I 和 Part II。Coursera 课程页写明[课程的全部功能免费](#ref-coursera-algs)。喜欢边写代码边学的读者，适合用这一套：书和课都用 Java 把每种数据结构实现一遍。

## 第二步：两本参考书放在手边备查

**《Introduction to Algorithms》第 4 版（Cormen、Leiserson、Rivest、Stein）。** 这本书通常简称 CLRS，MIT Press 在 [2022 年 4 月 5 日](#ref-clrs)出版了第 4 版。准备面试不必通读 CLRS。上课或者做题遇到没弄懂的地方，再翻到对应章节读证明。

**《The Algorithm Design Manual》第 3 版（Steven Skiena）。** Springer 在 2020 年出版了[第 3 版](#ref-skiena)。全书第二部分是一份常见算法问题的目录，习题里还收了软件公司的[面试题](#ref-skiena)。认得出题型却叫不出名字的时候，就去查这份目录。

## 第三步：三本面试专书讲清面试本身

**《Cracking the Coding Interview》第 6 版（Gayle Laakmann McDowell）。** 第 6 版收了 [189 道面试题](#ref-ctci)，每道题都有提示和解法推导。做题时先合上答案，卡住了再看提示。

**《Elements of Programming Interviews》（Adnan Aziz、Tsung-Hsien Lee、Amit Prakash）。** EPI 分 C++、Java 和 Python [三个语言版本](#ref-epi)。读完 CTCI 还想多练，再读 EPI。版本按面试时要用的语言挑。

**《剑指 Offer：名企面试官精讲典型编程题（第 2 版）》（何海涛）。** 电子工业出版社在 [2017 年 3 月](#ref-jianzhi-offer)出版了这本书，书里剖析了 [80 道典型编程面试题](#ref-jianzhi-offer)。准备国内公司面试的读者，适合读这一本。

## 第四步：一份题单保证每天都在练

**Blind 75（Yangshun Tay）。** Yangshun Tay 从 LeetCode 里挑了 75 道重要的题，发在了 Blind 上。别人把这份题单转到 LeetCode 论坛后流传开来，大家给它起名 [Blind 75](#ref-blind75)。打完第一步的基础再刷这份题单；哪个专题做不出来，就回到第二步和第三步补那个专题。

这篇文章只谈算法面试。姊妹篇《如何准备软件工程师的系统面试——资料篇》专门谈系统设计面试。

## 参考来源

- <span id="ref-mit-6006"></span>MIT OpenCourseWare — [6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/#:~:text=Prof.%20Erik%20Demaine) — fetched [2026-10-30](https://web.archive.org/web/20261014174214/https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- <span id="ref-algs4"></span>Robert Sedgewick、Kevin Wayne — [Algorithms, 4th Edition 配套网站](https://algs4.cs.princeton.edu/home/#:~:text=You%20can%20take%20our%20free%20Coursera%20MOOCs) — fetched [2026-10-30](https://web.archive.org/web/20261017122534/https://algs4.cs.princeton.edu/home/)
- <span id="ref-coursera-algs"></span>Coursera — [Algorithms, Part I](https://www.coursera.org/learn/algorithms-part1#:~:text=All%20the%20features%20of%20this%20course%20are%20available%20for%20free) — fetched [2026-10-30](https://web.archive.org/web/20261020163814/https://www.coursera.org/learn/algorithms-part1)
- <span id="ref-clrs"></span>The MIT Press — [Introduction to Algorithms, Fourth Edition](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/#:~:text=Pub%20date%3A%20April%205%2C%202022) — fetched [2026-10-30](https://web.archive.org/web/20261013115332/https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- <span id="ref-skiena"></span>Springer — [The Algorithm Design Manual, third edition](https://link.springer.com/book/10.1007/978-3-030-54256-6#:~:text=Exercises%20include%20%22job%20interview%20problems%22&text=updated%20third%20edition) — fetched [2026-10-30](https://web.archive.org/web/20260523084335/https://link.springer.com/book/10.1007/978-3-030-54256-6)
- <span id="ref-ctci"></span>Gayle Laakmann McDowell — [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/#:~:text=The%206th%20edition%20of%20Cracking%20the%20Coding%20Interview&text=189%20programming%20interview%20questions) — fetched [2026-10-30](https://web.archive.org/web/20260917072542/https://www.crackingthecodinginterview.com/)
- <span id="ref-epi"></span>Adnan Aziz、Tsung-Hsien Lee、Amit Prakash — [Elements of Programming Interviews](https://elementsofprogramminginterviews.com/#:~:text=There%20are%20two%20basic%20printed%20variants)（首页写明 C++ 和 Java 两种印刷版本，同页的 “EPI in Python” 一文宣布了 Python 版）和 [About Us](https://elementsofprogramminginterviews.com/about#:~:text=Adnan%20Aziz) — fetched [2026-10-30](https://web.archive.org/web/20260928151058/https://elementsofprogramminginterviews.com/)
- <span id="ref-jianzhi-offer"></span>电子工业出版社 — [剑指Offer：名企面试官精讲典型编程题（第2版）](https://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=49304#:~:text=%E6%9C%AC%E4%B9%A6%E5%89%96%E6%9E%90%E4%BA%8680%E4%B8%AA%E5%85%B8%E5%9E%8B%E7%9A%84%E7%BC%96%E7%A8%8B%E9%9D%A2%E8%AF%95%E9%A2%98)。书页原文：“出版时间：2017-03”“本书剖析了80个典型的编程面试题”。 — fetched 2026-10-30（无存档快照）
- <span id="ref-blind75"></span>Yangshun Tay，Tech Interview Handbook — [Best practice questions](https://www.techinterviewhandbook.org/best-practice-questions/#:~:text=people%20even%20gave%20it%20a%20name) — fetched [2026-10-30](https://web.archive.org/web/20260526010814/https://www.techinterviewhandbook.org/best-practice-questions/)

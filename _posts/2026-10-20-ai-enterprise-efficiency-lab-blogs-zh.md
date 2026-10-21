---
title: "前沿实验室怎么说：用 AI 提升企业效率的方法与证据"
excerpt: "综述 Anthropic、OpenAI、xAI、Google 和各家 neo lab 的官方博客，整理企业用 AI 提效的做法；neo lab 部分只收有独立证据的案例。"
date: 2026-10-20
lang: zh
categories: [AI]
tags: [AI, 企业效率, Agent, Anthropic, OpenAI, xAI, Gemini, DeepMind]
published: true
cover_image:
  src: /assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-00-cover.jpg
  x: 560
  y: 0
  size: 630
og_image: /assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-00-cover.jpg
---

*本文写给准备在公司里落地 AI 的管理者和工程负责人。我在 2026-10-20 读了 Anthropic、OpenAI、xAI 和 Google 的官方博客、研究报告和客户案例。我还查了十几家 neo lab 的官网和外部报道。文中每个数字都链接到文末的参考条目，参考条目再链接到原文的具体段落和存档。厂商的数字变化很快，读者引用之前请再看一遍原文。*

![一张分成四栏的工作台，四栏分别放着代码、客服工单、文档和账本，一盏台灯照着中间的一张检查清单](/assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-01-four-workflows.jpg)

## 我先给出五条结论

1. **提效集中在容易验证的工作上。** 编码、客服工单、文档处理和后台流程的证据最多。Anthropic 的工程师说，他们最先交出去的是[容易验证的任务](#ref-ant-work-verify)。
2. **自报的省时数字普遍偏大。** GDPval 论文只算模型推理时，GPT-5 比专家[快 90 倍](#ref-oai-gdpval-table)。论文把专家审核和返工算进去以后，GPT-5 只快 1.39 倍。
3. **各家给出的落地方法几乎一致。** 团队先用最简单的方案，先建评测，把高风险动作留给人审批，再逐步放权。
4. **瓶颈已经从模型转到组织。** OpenAI 的企业报告写道，主要约束[不再是模型性能或工具](#ref-oai-sea-org)，而是组织的准备程度。Anthropic 认为复杂任务[更受信息获取的限制](#ref-ant-ei-sep25-ctx)。
5. **neo lab 几乎拿不出经独立证据确认的效果。** 我找到的是少数客户自己公布的数字、港交所文件和媒体报道的“预期”。

## 本文按三条规则收录来源

**Anthropic、OpenAI 和 xAI。** 三家的官方博客、研究报告和客户案例，本文直接采信，照常标注来源。三家的数字仍然出自厂商，所以我在正文里写明每个数字是怎样测出来的。

**Google。** 本文直接引用 Gemini、Google DeepMind 和 Google Research 三个博客的方法和研究结论。Google 转述的客户提效数字，本文写成“Google 称”。我找到客户自己或第三方的佐证时，才把数字写成事实。

Google Brain 已经不是独立团队。Sundar Pichai 在 [2023 年 4 月 20 日宣布](#ref-g-merge)合并两个团队。Google Research 的 Brain 团队和 DeepMind 从此合并成 Google DeepMind。所以本文不单列 Google Brain。

**neo lab。** 本文的 neo lab 指 2017 年以后成立、自己训练基础模型的 AI 实验室。上面四家和其他大型科技公司的实验室不算 neo lab。Cohere 和 AI21 成立得早，但两家的业务全在企业市场，本文也收进来。neo lab 的效果只在有下面四种证据之一时成立：

- 客户自己署名发布的数据；
- 上市公司的财报或监管文件；
- 同行评审或可以复现的独立评测；
- 可信媒体的独立报道。

有的说法只出现在 neo lab 自家的博客和新闻稿里。本文把这类说法放进“只有自述”表，并写明原因。

xAI 的网站现在以 SpaceXSI 的名义发文，本文仍称 xAI。

## 企业用 AI 提效的工作集中在四类工作流

先看企业员工把 AI 用在哪里。Anthropic 在 2026 年 6 月的报告里统计了工作对话的产出。最常见的产出是[文档和报告（20%）、解释（9%）和邮件草稿（7%）](#ref-ant-ei-jun26)。OpenAI 统计消费者版 ChatGPT 的工作消息，[写作占 40%](#ref-oai-usage-writing)。

企业通过 API 调用模型的方式不一样。Anthropic 看到 [77% 的 API 对话属于自动化模式](#ref-ant-ei-sep25)，只有 12% 属于增强模式。企业在 API 上更常把整件任务交给模型。

| 工作流 | 适合先交给 AI 的环节 | 本文引用的例子 | 证据类型 |
| --- | --- | --- | --- |
| 编码和软件维护 | 代码迁移、补全、测试、构建优化 | Anthropic 内部、Stripe、Cisco、Google 内部 | 内部实测、随机对照试验、厂商案例 |
| 客服和工单处理 | 分类、退款、批量关闭重复工单 | Klarna、Intercom、Zendesk、xAI 自用 | 厂商案例 |
| 文档、检索和分析 | 查找内部文档、合同审阅、调研报告 | Morgan Stanley、Spellbook、BBVA | 厂商案例 |
| 后台流程 | 开票、对账、采购审查、邮件管理 | Qonto、xAI 自用、Anthropic 的 API 统计 | 厂商案例、用量统计 |

### 编码和软件维护积累了最多的证据

在本文引用的材料里，只有编码同时有内部实测和随机对照试验。

- **Anthropic 内部。** Anthropic 在 2025 年 8 月[调查了 132 名工程师和研究员](#ref-ant-work-n)。受访者[自报 Claude 承担了 60% 的工作，生产率提高 50%](#ref-ant-work-survey)。Anthropic 说，自报数字和工程团队[每人每天合并的 PR 增加 67%](#ref-ant-work-pr) 大致相符。受访者还估计，[27% 的 Claude 辅助工作原本不会去做](#ref-ant-work-new)。
- **Claude Code 的用法。** Anthropic 统计了编码对话。Claude Code 里 [79% 的对话属于某种自动化，Claude.ai 上是 49%](#ref-ant-swdev)。另一项研究发现，人做了[约 70% 的规划决策，只做 20% 的执行决策](#ref-ant-cc-expertise)。
- **Stripe。** Stripe 用 4 天[把 1 万行 Scala 迁移到 Java](#ref-ant-stripe)。Anthropic 的案例说，人工做估计要 10 个工程周。
- **Cisco。** Cisco 用 Codex 优化构建。OpenAI 的案例说，构建时间[缩短约 20%，每月省下 1,500 多个工程小时](#ref-oai-cisco)。
- **Google 内部。** Google 工程师做了一项[有 96 名 Google 全职工程师参加的随机对照试验](#ref-g-rct-96)。AI 功能让任务用时缩短约 21%，但作者说明[置信区间很大](#ref-g-rct)。Google Research 报告，代码里[由 AI 补全的字符已经和手打的一样多](#ref-g-research-se)。在一次 ID 类型迁移中，落地的改动里 [80% 由 AI 写成](#ref-g-migration-80)。参与的工程师[估计总时间减少一半](#ref-g-migration)。
- **Google 称。** Pichai 在 2024 年 10 月说，Google [超过四分之一的新代码由 AI 生成](#ref-g-code25)。2026 年 4 月，Pichai 说 AI 生成的新代码[已经占 75%](#ref-g-code75)。Google 没有说明比例的分母是字符、行还是提交。

OpenAI 的 Codex 指南也提醒，AI 代码审查[不一定让 PR 流程变快](#ref-oai-codex-review)。

### 客服和工单处理已经有大规模的自动化案例

客服工单量大、格式相近、结果容易核对，适合交给 AI 处理。

- **Klarna。** OpenAI 的案例只写了上线第一个月的数据。客户[解决问题的时间从 11 分钟降到 2 分钟以内](#ref-oai-klarna)。案例标题说，Klarna 的 AI 助手做了相当于 700 名全职客服的工作。
- **Intercom。** Intercom 的语音客服叫 Fin Voice。OpenAI 的报告说，Fin Voice [平均端到端解决 53% 的来电](#ref-oai-sea-intercom)。
- **Zendesk。** Anthropic 的案例统计了使用自建智能体的 Zendesk 客户。这些客户的[自动解决率最多提高 10%，人工处理时间最多减少 80%](#ref-ant-zendesk)。
- **xAI 自用。** xAI 说，合并后的客服团队[工单增加了 175%，没有新招一个人](#ref-x-support)。xAI 在上线初期[只让 Grok Bot 写内部备注，每个写操作都要人工批准](#ref-x-support-method)。另一个智能体在一次事故中[约 10 分钟清完 204 张工单，由一名客服工程师审批整批操作](#ref-x-incident)。
- **Carvana。** Carvana 让 Claude 修掉告警的根因。Anthropic 的案例说，一个频道的[告警减少了 56%](#ref-ant-carvana)。

### 文档、检索和分析类工作占了用量的大头

文档类工作在用量里占比最大，但结果不容易自动打分。

- **Morgan Stanley。** OpenAI 的指南说，Morgan Stanley 的顾问[能查到的文档从 20% 升到 80%](#ref-oai-aie-ms)。Morgan Stanley 的做法放在下文第三步里讲。
- **Spellbook。** Spellbook 用 Claude 审合同。一份协议的完成时间[从律师约 10 小时缩短到约 1 小时](#ref-ant-spellbook)。
- **BBVA。** BBVA 墨西哥做了一个法务聊天机器人。机器人[每年自动处理 9,000 多次查询，相当于腾出 3 名全职员工](#ref-oai-sea-bbva)。
- **Anthropic 的调研智能体。** Anthropic 让多个子智能体并行检索，复杂查询的[调研时间最多减少 90%](#ref-ant-multi-90)。代价是多智能体系统的 [token 用量约为普通对话的 15 倍](#ref-ant-multi)。

### 后台流程正在从对话转向自动执行

后台流程的特点是规则明确、金额敏感。本节的 Qonto 和 xAI 两个例子都把“执行”和“审批”分开。

- **Anthropic 的统计。** Anthropic 在 2026 年 1 月写道，企业[越来越多地用 Claude 自动处理后台流程](#ref-ant-ei-jan26-admin)，例如邮件管理。
- **Qonto。** Qonto 的智能体让[开票时间缩短到三分之一，每张发票都由客户确认后才发出](#ref-ant-qonto)。
- **xAI 自用。** xAI 的采购智能体[已经找出超过 10 万美元的直接节省](#ref-x-proc)。智能体发现某个产品有 [43 个付费席位 90 天没人用](#ref-x-proc-seats)。花钱、接受条款和给供应商发东西，[都要人明确批准](#ref-x-proc-approval)。

## 各家实验室的落地方法可以归成六个步骤

我对照读了各家的工程文章和企业指南。各家的建议可以归成六个步骤。下面每一步都只列原文支持的做法。

![六级编号台阶，依次标着挑任务、简单方案、先评测、接数据、人审批和共享，台阶上分别放着筛子、齿轮、尺子、插头、印章和一本打开的手册](/assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-02-six-steps.jpg)

### 第一步：团队先挑出高影响、低投入、容易验证的任务

OpenAI 的用例指南建议从三类工作里找机会：[重复的低价值任务、技能瓶颈和模糊的问题](#ref-oai-usecases-3)。指南分析了 600 多个客户用例。大多数用例属于[六类基本用例](#ref-oai-usecases-prim)：内容创作、自动化、研究、构思和策略、编码、数据分析。

指南建议团队按影响和投入给用例打分，先做[影响大、投入小的项目](#ref-oai-usecases-quick)。团队要[每个季度重新打一次分](#ref-oai-usecases-q)。模型能力提高以后，原来投入大的用例可能变得容易。指南还建议骨干用户[把工作流拆成一个个任务](#ref-oai-usecases-map)。

挑任务时还要看整条工作流。Anthropic 指出，AI 提速少的环节[可能变成瓶颈](#ref-ant-prod-bottle)。OpenAI 的智能体指南也说，用例不满足条件时，[确定性的程序可能就够了](#ref-oai-agents-det)。

### 第二步：团队先用最简单的方案，不够用再加智能体

《Building effective agents》建议[先找最简单的方案，需要时才加复杂度](#ref-ant-bea)。很多场景用一次模型调用加检索就够了。OpenAI 的智能体指南给出同样的建议：[先把单个智能体的能力用足](#ref-oai-agents-single)。

Anthropic 把常见的工作流写成五种模式。下表的“适用的情况”一栏转述原文：

| 模式 | 做法 | 适用的情况 |
| --- | --- | --- |
| 提示词链 | [把任务拆成固定的几步](#ref-ant-bea-chain)，每一步处理上一步的输出 | 任务能干净地拆成固定子任务 |
| 路由 | [先给输入分类，再交给专门的后续流程](#ref-ant-bea-route) | 输入有明显不同的类别，并且分类准确 |
| 并行 | 把子任务同时跑，或者让同一任务跑多次再投票 | [子任务能并行提速](#ref-ant-bea-par)，或者需要多个视角 |
| 编排者和执行者 | [一个模型动态拆分任务，交给执行者，再汇总结果](#ref-ant-bea-orch) | 事先无法预测需要哪些子任务 |
| 评估者和优化者 | [一个模型生成，另一个模型评价并反馈](#ref-ant-bea-eval) | 有清楚的评价标准，迭代能带来可测的改进 |

Rocket Money 是路由模式的例子。Rocket Money [先用 Haiku 4.5 给请求分类，再交给职责单一的子智能体](#ref-ant-rocket)。

多智能体系统要算成本。多智能体系统的 token 用量约为普通对话的 15 倍。我的看法是：只有任务价值高、并且能并行时，多智能体系统才值得做。

### 第三步：团队在上线之前先建评测

《AI in the Enterprise》列了七条经验。第一条经验是[用系统的评测流程衡量模型在自己用例上的表现](#ref-oai-aie-evals)。Morgan Stanley [在每个 AI 用例上线前先跑评测](#ref-oai-ms-eval)。Morgan Stanley 还[每天用一组示例问题跑回归测试](#ref-oai-ms-reg)。

评测集不必一开始就很大：

- Anthropic 的评测文章说，[20 到 50 个取自真实失败的简单任务](#ref-ant-evals)就足够起步。
- Anthropic 的多智能体团队起步时只用了[约 20 个代表真实用法的查询](#ref-ant-multi-20)。
- 回归评测的[通过率应该接近 100%](#ref-ant-evals-reg)；能力评测衡量的是智能体还做不稳的事情。

评测还能加快换模型。[没有评测的团队要花几周测试新模型](#ref-ant-evals-days)。有评测的团队很快就能判断。OpenAI 建议[先用最强的模型做原型，建立性能基线](#ref-oai-agents-base)，再换小模型省钱。Indeed 微调了一个小模型，[用少 60% 的 token 得到相近的结果](#ref-oai-aie-indeed)。

编码场景的评测就是测试。OpenAI 的 Codex 指南说，[先写好测试往往是让智能体开发功能的第一步](#ref-oai-codex-tests)。Claude Code 的文档建议[给 Claude 一个能运行的检查](#ref-ant-ccbp)，例如测试、构建或截图对比。

### 第四步：团队把数据和工具接给模型

Anthropic 推测，复杂任务[更受信息获取的限制](#ref-ant-ei-sep25-ctx)，模型能力倒在其次。OpenAI 统计了企业版的月活用户。[19% 没用过数据分析，14% 没用过推理，12% 没用过搜索](#ref-oai-sea-unused)。

接数据和接工具有三条具体建议：

- **上下文要精简。** Anthropic 说，上下文是[边际收益递减的有限资源](#ref-ant-ctx)。
- **工具要少而准。** Anthropic 建议[先做几个面向高影响工作流的工具](#ref-ant-tools)，不要把每个 API 都包一层。Anthropic 做 SWE-bench 智能体时，[花在工具上的时间比提示词还多](#ref-ant-bea-tools)。
- **权限要先设好。** OpenAI 建议管理者[把智能体接上完成工作所需的上下文和工具，并设清权限、审核和治理](#ref-oai-signals-agenda)。

### 第五步：团队把高风险动作留给人审批，再逐步放权

OpenAI 写道，[敏感、不可逆或高风险的动作应该触发人工监督](#ref-oai-agents-human)。团队信任智能体以后，才逐步放开。xAI 的三个例子都照此执行：

- Grok Bot [默认没有任何权限](#ref-x-ent-access)，只能进入用户替 Grok Bot 登录的账户。
- 客服智能体先只写内部备注；第一天人工复核以后，xAI 才[让智能体直接回复客户](#ref-x-support-direct)。
- 采购智能体花钱、接受条款前都要人批准。

放权的节奏可以按智能体的表现调整。Claude Code 连续执行的动作也在变多。需要人介入之前，Claude Code [连续执行的动作从约 10 个增加到约 20 个](#ref-ant-work-steps)。OpenAI 的 Codex 指南写明了分工：[智能体做第一遍实现，工程师负责审阅、修改和定方向](#ref-oai-codex-roles)。

### 第六步：团队把个人用法整理成共享的工作流

OpenAI 说，[约 20% 的企业版消息经由 Custom GPT 或 Project 处理](#ref-oai-sea-gpts)。BBVA 的员工在五个月里[建了 2,900 多个 Custom GPT](#ref-oai-aie-bbva)。

员工也需要时间学。Anthropic 发现，使用 Claude 六个月以上的用户，[对话成功率高 10%](#ref-ant-ei-mar26)。OpenAI 总结了领先企业的做法：[衡量使用深度、建立治理、投入培训、推广有效的做法](#ref-oai-signals-leading)。领先企业还把工作从对话转给智能体。

## 企业度量提效时要把审核和返工的时间算进去

各家报告里的数字可以分成三类。三类数字能证明的东西不一样。

| 数据类型 | 例子 | 能证明什么 | 不能证明什么 |
| --- | --- | --- | --- |
| 用量数据 | 消息数、token 数、席位数 | 员工在用、用得多深 | 业务价值 |
| 自报数据 | 问卷里的“每天省了多少分钟” | 员工的感受 | 实际省下的时间 |
| 实测数据 | 合并 PR 数、处理时长、随机对照试验 | 指标的真实变化 | 别的团队能否复现 |

**用量数据。** OpenAI 自己承认，[token 不是业务价值的直接度量](#ref-oai-signals-tokens)。OpenAI 说前沿企业每个活跃用户的输出 token [是普通企业的 8.3 倍](#ref-oai-signals-83)。OpenAI 在 2025 年 12 月也用过“前沿”一词。那份报告的“前沿员工”指[第 95 百分位的员工](#ref-oai-sea-6x)。几份报告的倍数不能放在一起比较。

**自报数据。** OpenAI [调查了近 100 家企业的 9,000 名员工](#ref-oai-sea-n)。受访者[自报每个活跃日省下 40 到 60 分钟](#ref-oai-sea-time)。Google 称 Workspace 用户[每周平均省下 105 分钟](#ref-g-ws105)，依据是 [3,200 多份员工问卷](#ref-g-ws105-n)。Anthropic 的问卷里，[86%、82% 和 69% 的受访者说速度、范围和质量提高了](#ref-ant-ei-jun26-survey)。Anthropic 也承认问卷[不能代表总体人群](#ref-ant-ei-jun26-rep)。

**模型估算。** Anthropic 让 Claude 估算对话里的任务用时。没有 AI 时任务[平均要 90 分钟，Claude 把用时缩短约 80%](#ref-ant-prod)。估算没有计入对话之外的时间，[包括核对 Claude 工作的质量和准确性](#ref-ant-prod-caveat)。

![一个漏斗，顶端写着 90× 和“只算推理”，中段写着“审核 + 返工”，底部写着 1.39×；漏斗左边是一把放大镜，右边是一叠打了叉的稿纸](/assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-03-measurement-funnel.jpg)

### GDPval 的两组速度数字相差 60 多倍

GDPval 是 OpenAI 在 2025 年 9 月发布的评测。[完整版有 1,320 个专业任务](#ref-oai-gdpval-scope)，专家[平均要 7 小时完成一个任务](#ref-oai-gdpval-7h)。首批结果里，Claude Opus 4.1 表现最好，[47.6% 的交付物被评为不差于专家](#ref-oai-gdpval-476)。

OpenAI 在发布文章里说前沿模型完成任务比专家快约 100 倍、便宜约 100 倍。同一篇文章说明，100 倍[只算模型推理时间和 API 价格，没有计入人工监督](#ref-oai-gdpval-100x)。论文的表 2 把审核和返工算了进去，结果如下：

| 模型 | 只算推理 | 审核一次，不合格就自己做 | 反复让模型重做，最后自己做 |
| --- | --- | --- | --- |
| GPT-5 | 快 90 倍 | 快 1.12 倍 | 快 1.39 倍 |
| GPT-4o | 快 327 倍 | 快 0.87 倍（更慢） | 快 0.46 倍（更慢） |

表中数字取自[论文第 15 页的表 2](#ref-oai-gdpval-table)。论文写道，算上审核和返工，[用模型的收益会缩水](#ref-oai-gdpval-table)。在 GPT-5 输给专家的评分里，[约 29% 被评为差或灾难性](#ref-oai-gdpval-cat)。2025 年 12 月，OpenAI 说 GPT-5.2 [在 70.9% 的比较中胜过或打平专家](#ref-oai-gpt52)。读 GPT-5.2 的数字时，也要对照论文的审核场景。

Anthropic 的估算有同样的问题。Anthropic 按任务成功率调整了估算。[隐含的生产率提升大约减半，从 1.8 个百分点降到约 1.0 个百分点](#ref-ant-ei-jan26)。Claude.ai 上的任务成功率估计是 67%，[API 上是 49%](#ref-ant-ei-jan26-succ)。

### 管理者可以按五条规则设计度量

下面五条规则是我根据上面的材料整理的，不是某一家实验室的原话：

1. **上线前先测基线。** 团队记录任务现在的用时、错误率和返工次数，否则上线后的数字没有参照。
2. **把审核和返工计入用时。** GDPval 的表 2 说明，漏掉审核时间会把收益放大几十倍。
3. **能做对照就做对照。** Google 的随机对照试验只有 96 人，作者仍然提醒置信区间很大。Google Research 也把[在线 A/B 实验](#ref-g-research-ab)当作上线 AI 功能的关键做法。
4. **记录失败的严重程度。** 平均分会掩盖少数灾难性错误。GDPval 专门统计了灾难性错误。
5. **自报、用量和实测分开报告。** 三类数字混在一张表里，管理层会把感受当成结果。

## Google 转述的客户提效数字只有少数找得到佐证

Google DeepMind 的公开成果大多发生在 Google 自己的基础设施上。DeepMind 称，AlphaEvolve 找到的调度方法[平均收回 Google 全球 0.7% 的算力](#ref-g-alphaevolve)。DeepMind 在 2016 年称，机器学习把数据中心的制冷能耗最多降低 40%。降幅[相当于 PUE 开销降低 15%](#ref-g-cooling)。

Google Cloud 维护了一份[客户用例清单，现在列了 1,302 个用例](#ref-g-usecases)。清单里的数字大多是一句话，没有说明测量方法。我抽查了四条：

| 客户 | Google 称 | 我找到的佐证 | 本文的处理 |
| --- | --- | --- | --- |
| Macquarie Bank | [省下超过 10 万小时](#ref-g-usecases) | iTnews 报道，Macquarie 的高管在 Google Cloud Next 大会上说[已经省下 13 万小时](#ref-g-macq-itnews) | 有佐证，但数字不同，场合是厂商大会 |
| Virgin Voyages | [部署 1,000 多个智能体，活动制作时间减少 40%](#ref-g-usecases-vv) | Virgin Voyages 自己的新闻稿说[内容制作时间平均减少 60%](#ref-g-vv-press) | 有客户自己的佐证，数字不同 |
| CME Group | [多数开发者自报每月至少省 10.5 小时](#ref-g-usecases-cme) | 没有找到 | 只写成“Google 称” |
| Deloitte | [分析师效率提高 60% 以上](#ref-g-usecases-deloitte) | 没有找到 | 只写成“Google 称” |

Google Cloud 的高管问卷也要小心读。Google 称，在报告生产率提升的高管里，[39% 说生产率至少翻了一倍](#ref-g-roi)。分母只包括已经报告提升的高管，并不是全部受访者。

## neo lab 的效果数字大多缺少独立证据

我按上文的定义检索了 15 家 neo lab。15 家分别是Mistral AI、Cohere、Thinking Machines Lab、Sakana AI、智谱、MiniMax、DeepSeek、月之暗面、Safe Superintelligence、Reflection AI、Poolside、Magic、AI21、Aleph Alpha 和 AMI Labs。阶跃星辰和零一万物的官网无法正常抓取，本文没有覆盖。

![一个筛子上方散落着写有百分比和“预计”的纸条，筛子下方只落下两张盖了对勾印章的纸条](/assets/blogposts/2026-10-20-ai-enterprise-efficiency/ai-efficiency-04-evidence-sieve.jpg)

### 只有少数说法满足本文的证据规则

| 实验室 | 说法 | 证据 | 本文的判断 |
| --- | --- | --- | --- |
| DeepSeek | 深圳福田区说，基于 DeepSeek 的 AI“数智员工”让公文[审核时间缩短 90%](#ref-nl-futian) | 客户（区政府）自己发布 | 成立，但原文没有基线和测量方法 |
| Thinking Machines Lab | Glean 说，用 Tinker 训练的 Waldo 模型带来[约 50% 的延迟下降和约 25% 的 token 节省，质量不降](#ref-nl-glean) | 客户自己发布 | 成立，但衡量的是系统效率，不是员工效率 |
| Thinking Machines Lab | Bridgewater 的研究人员说，微调模型让每个任务的[推理成本降到约十四分之一](#ref-nl-bridgewater) | 客户署名，但文章发在 Thinking Machines 的网站上 | 部分成立 |
| 智谱 | 招股章程说，为一家金融集团定制的模型在新规问答上的[AI 自动化率超过 50%](#ref-nl-zhipu-prosp) | 港交所招股章程 | 成立，但客户匿名，“自动化率”没有定义 |
| 智谱 | 2026 年中期公告说，网络安全试点进展最快，法律、金融、教育等试点[还没有带来实质收入](#ref-nl-zhipu-h1) | 港交所公告 | 成立，是一条反向证据 |
| MiniMax | 开放平台和企业服务收入[增长 703.1%](#ref-nl-minimax-h1) | 港交所公告 | 证明需求增长，不证明效率提升 |
| Mistral AI | CMA CGM 说，基于 Mistral 的平台面向[近 8 万名员工](#ref-nl-cmacgm)；路透社 2025 年报道的是 CMA CGM 的[预期](#ref-nl-gcaptain) | 客户自己发布、媒体报道 | 只证明部署规模，没有效果数字 |

福田区的数字需要配一条警示。JMIR 上的一篇同行评审综述统计了中国医院部署 DeepSeek 的公开信息。只有 [22% 的部署给出了评估结果](#ref-nl-jmir)。作者还发现，医院[倾向于报告更高的性能和更少的风险](#ref-nl-jmir-over)。

### 本文把只有自述的说法列在一张表里

| 实验室 | 自述的说法 | 剔除原因 |
| --- | --- | --- |
| Mistral AI | Cisco 制作续约方案的时间[最多减少 20%](#ref-nl-mistral-cisco) | 原文标明“估计”，没有找到 Cisco 自己的来源 |
| Mistral AI | SAP 为瑞士铁路 SBB 做的客服机器人[减少约 80% 的重复咨询](#ref-nl-mistral-sap) | 原文标明“估计”，没有找到 SAP 或 SBB 的来源 |
| Mistral AI | 欧洲专利局的识别系统[每天转写 40 万页](#ref-nl-mistral-epo) | 欧洲专利局的新闻稿只确认了部署，[没有给出数字](#ref-nl-epo-press) |
| Mistral AI | Capgemini 开发者的[采用率从 30% 升到 100%](#ref-nl-mistral-capg) | 只出现在 Mistral 的网站上 |
| Cohere | CoreWeave 的工单[处理时间从 4–8 天降到 2–5 天](#ref-nl-cohere-cw) | 原文把改进同时归于内部流程，效果没有单独测出 |
| Sakana AI | 三井住友银行的提案书制作[预计从一两周缩短到几十分钟到几小时](#ref-nl-sakana-smbc) | 原文写的是“预计” |
| Sakana AI | 三菱 UFJ 银行的验证[确认了融资流程的效率提升](#ref-nl-sakana-mufg) | 没有数字 |
| Thinking Machines Lab | Chroma 的检索智能体[推理最多快 10 倍](#ref-nl-tml-chroma) | 我没有找到 Chroma 自己的来源 |
| Aleph Alpha | 一家全球芯片厂商的[检索时间缩短 90%](#ref-nl-aleph) | 客户没有具名 |

### 几家 neo lab 没有公开企业提效的内容

Safe Superintelligence 的官网说公司只有[一个目标和一个产品：安全的超级智能](#ref-nl-ssi)。我查了 DeepSeek、Reflection AI、Poolside、Magic 和 AMI Labs 的官网和新闻页。五家都没有企业提效的案例或数字。

我的判断是：neo lab 公开的多是部署规模和采用情况，客户也常常确认部署。但客户亲自确认的、实测的提效数字，我只找到上面那几条。

## 管理者可以按这份清单启动第一个项目

下面的清单是我综合上文各家建议整理的：

1. **选一条工作流，不选一个工具。** 团队写下工作流的每一步，标出哪几步重复、哪几步容易验证。
2. **先测基线。** 团队记录现在每件任务的用时、错误率和返工次数。
3. **先做最简单的版本。** 一次模型调用加检索能解决的问题，团队不做智能体。
4. **先写 20 到 50 条评测。** 评测题取自真实的失败案例，每次改提示词或换模型都重新跑一遍。
5. **只接必要的数据和工具。** 团队给智能体最小的权限，并且记录每一次调用。
6. **花钱、对外发送、不可逆的动作留给人批准。** 智能体先只出草稿，团队按评测结果逐步放权。
7. **用时要包括审核和返工。** 团队分开报告用量、自报和实测三类数字。
8. **把有效的做法做成共享模板。** 团队每个季度重新给用例打分，把投入大的用例往前排。

## 本文引用了以下来源

所有链接都在 2026-10-20 读取；“fetched”后的日期链接到 Internet Archive 的存档。厂商客户案例里的数字都由厂商或客户自报，原文大多没有说明测量方法。

- <span id="ref-ant-ei-jun26"></span>Anthropic — [Anthropic Economic Index report: Cadences（2026-06-26）](https://www.anthropic.com/research/economic-index-june-2026-report#:~:text=Work%20conversations%20most%20often%20produce%20documents%20and%20reports%20%2820%25%29%2C%20followed%20by%20explanations%20%289%25%29%2C%20email%20drafts%20%287%25%29) — fetched [2026-10-20](https://web.archive.org/web/20260928060629/https://www.anthropic.com/research/economic-index-june-2026-report)
- <span id="ref-ant-ei-jun26-survey"></span>Anthropic — [Anthropic Economic Index report: Cadences，问卷部分（约 9,700 名受访者）](https://www.anthropic.com/research/economic-index-june-2026-report#:~:text=large%20majorities%20of%20people%20report%20productivity%20gains%20in%20speed%2C%20scope%2C%20and%20quality%20of%20their%20work%20%2886%25%2C%2082%25%2C%20and%2069%25%2C%20respectively%29) — fetched [2026-10-20](https://web.archive.org/web/20260928060629/https://www.anthropic.com/research/economic-index-june-2026-report)
- <span id="ref-ant-ei-jun26-rep"></span>Anthropic — [Anthropic Economic Index report: Cadences，问卷的局限](https://www.anthropic.com/research/economic-index-june-2026-report#:~:text=The%20Economic%20Index%20Survey%20is%20not%20representative%20of%20the%20general%20population.) — fetched [2026-10-20](https://web.archive.org/web/20260928060629/https://www.anthropic.com/research/economic-index-june-2026-report)
- <span id="ref-ant-ei-sep25"></span>Anthropic — [Anthropic Economic Index report: Uneven geographic and enterprise AI adoption（2025-09-15）](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report#:~:text=In%20our%20data%2C%2077%25%20of%20API%20transcripts%20show%20automation%20patterns%20%28especially%20full%20task%20delegation%29%20versus%20just%2012%25%20for%20augmentation) — fetched [2026-10-20](https://web.archive.org/web/20261014102035/https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)
- <span id="ref-ant-ei-sep25-ctx"></span>Anthropic — [Anthropic Economic Index report（2025-09-15），关于上下文瓶颈的段落](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report#:~:text=deploying%20AI%20for%20complex%20tasks%20might%20be%20constrained%20more%20by%20access%20to%20information%20than%20on%20underlying%20model%20capabilities) — fetched [2026-10-20](https://web.archive.org/web/20261014102035/https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)
- <span id="ref-ant-ei-jan26"></span>Anthropic — [Anthropic Economic Index report: Economic primitives（2026-01-15）](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report#:~:text=Adjusting%20productivity%20estimates%20for%20task%20reliability%20roughly%20halves%20the%20implied%20gains%2C%20from%201.8%20to%20about%201.0%20percentage%20points) — fetched [2026-10-20](https://web.archive.org/web/20261012013735/https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- <span id="ref-ant-ei-jan26-succ"></span>Anthropic — [Anthropic Economic Index report: Economic primitives，任务成功率](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report#:~:text=Claude.ai%20also%20shows%20higher%20task%20success%20rates%20%2867%25%20vs.%2049%25%29) — fetched [2026-10-20](https://web.archive.org/web/20261012013735/https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- <span id="ref-ant-ei-jan26-admin"></span>Anthropic — [Anthropic Economic Index report: Economic primitives，后台流程](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report#:~:text=businesses%20are%20increasingly%20using%20Claude%20to%20automate%20routine%20back%2Doffice%20workflows%20such%20as%20email%20management) — fetched [2026-10-20](https://web.archive.org/web/20261012013735/https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- <span id="ref-ant-ei-mar26"></span>Anthropic — [Anthropic Economic Index report: Learning curves（2026-03-24）](https://www.anthropic.com/research/economic-index-march-2026-report#:~:text=people%20in%20this%20higher%2Dtenure%20group%20have%20a%2010%25%20higher%20success%20rate%20in%20their%20conversations) — fetched [2026-10-20](https://web.archive.org/web/20261020234941/https://www.anthropic.com/research/economic-index-march-2026-report)
- <span id="ref-ant-cc-expertise"></span>Anthropic — [Agentic coding and persistent returns to expertise（2026-06-16）](https://www.anthropic.com/research/claude-code-expertise#:~:text=On%20average%2C%20people%20make%20about%2070%25%20of%20the%20planning%20decisions%20but%20only%2020%25%20of%20the%20execution%20decisions) — fetched [2026-10-20](https://web.archive.org/web/20261017031605/https://www.anthropic.com/research/claude-code-expertise)
- <span id="ref-ant-swdev"></span>Anthropic — [Anthropic Economic Index: AI's impact on software development（2025-04-28）](https://www.anthropic.com/research/impact-software-development#:~:text=79%25%20of%20conversations%20involved%20some%20form%20of%20automation%2C%20compared%20to%2049%25%20on%20Claude.ai) — fetched [2026-10-20](https://web.archive.org/web/20261016085937/https://www.anthropic.com/research/impact-software-development)
- <span id="ref-ant-prod"></span>Anthropic — [Estimating AI productivity gains from Claude conversations（2025-11-25）](https://www.anthropic.com/research/estimating-productivity-gains#:~:text=these%20tasks%20would%20take%20on%20average%20about%2090%20minutes%20to%20complete%20without%20AI%20assistance%2C%20and%20Claude%20speeds%20up%20individual%20tasks%20by%20about%2080%25) — fetched [2026-10-20](https://web.archive.org/web/20261016223053/https://www.anthropic.com/research/estimating-productivity-gains)
- <span id="ref-ant-prod-caveat"></span>Anthropic — [Estimating AI productivity gains，估算没有计入的时间](https://www.anthropic.com/research/estimating-productivity-gains#:~:text=including%20validating%20the%20quality%20or%20accuracy%20of%20Claude%27s%20work) — fetched [2026-10-20](https://web.archive.org/web/20261016223053/https://www.anthropic.com/research/estimating-productivity-gains)
- <span id="ref-ant-prod-bottle"></span>Anthropic — [Estimating AI productivity gains，关于瓶颈的段落](https://www.anthropic.com/research/estimating-productivity-gains#:~:text=Where%20AI%20makes%20less%20of%20a%20difference%2C%20these%20tasks%20might%20become%20bottlenecks) — fetched [2026-10-20](https://web.archive.org/web/20261016223053/https://www.anthropic.com/research/estimating-productivity-gains)
- <span id="ref-ant-work-n"></span>Anthropic — [How AI is transforming work at Anthropic（2025-12-02），调查方法](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=in%20August%202025%20we%20surveyed%20132%20Anthropic%20engineers%20and%20researchers) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-work-survey"></span>Anthropic — [How AI is transforming work at Anthropic，自报数字](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=Employees%20self%2Dreport%20using%20Claude%20in%2060%25%20of%20their%20work%20and%20achieving%20a%2050%25%20productivity%20boost) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-work-pr"></span>Anthropic — [How AI is transforming work at Anthropic，合并 PR 数据](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=the%2067%25%20increase%20in%20merged%20pull%20requests) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-work-new"></span>Anthropic — [How AI is transforming work at Anthropic，新增工作](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=Employees%20estimated%20that%2027%25%20of%20their%20Claude%2Dassisted%20work%20wouldn%27t%20have%20been%20done%20without%20it.) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-work-verify"></span>Anthropic — [How AI is transforming work at Anthropic，委派习惯](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=Engineers%20tend%20to%20delegate%20tasks%20that%20are%20easily%20verifiable) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-work-steps"></span>Anthropic — [How AI is transforming work at Anthropic，连续动作数](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic#:~:text=Now%2C%20it%20generally%20handles%20around%2020%2C%20needing%20less%20frequent%20human%20steering) — fetched [2026-10-20](https://web.archive.org/web/20261018120721/https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- <span id="ref-ant-bea"></span>Anthropic — [Building effective agents（2024-12-19；现行页面已注明部分工具有变化）](https://www.anthropic.com/research/building-effective-agents#:~:text=we%20recommend%20finding%20the%20simplest%20solution%20possible%2C%20and%20only%20increasing%20complexity%20when%20needed) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-chain"></span>Anthropic — [Building effective agents，提示词链](https://www.anthropic.com/research/building-effective-agents#:~:text=Prompt%20chaining%20decomposes%20a%20task%20into%20a%20sequence%20of%20steps%2C%20where%20each%20LLM%20call%20processes%20the%20output%20of%20the%20previous%20one.) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-route"></span>Anthropic — [Building effective agents，路由](https://www.anthropic.com/research/building-effective-agents#:~:text=Routing%20classifies%20an%20input%20and%20directs%20it%20to%20a%20specialized%20followup%20task.) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-par"></span>Anthropic — [Building effective agents，并行](https://www.anthropic.com/research/building-effective-agents#:~:text=Parallelization%20is%20effective%20when%20the%20divided%20subtasks%20can%20be%20parallelized%20for%20speed) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-orch"></span>Anthropic — [Building effective agents，编排者和执行者](https://www.anthropic.com/research/building-effective-agents#:~:text=a%20central%20LLM%20dynamically%20breaks%20down%20tasks%2C%20delegates%20them%20to%20worker%20LLMs%2C%20and%20synthesizes%20their%20results) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-eval"></span>Anthropic — [Building effective agents，评估者和优化者](https://www.anthropic.com/research/building-effective-agents#:~:text=one%20LLM%20call%20generates%20a%20response%20while%20another%20provides%20evaluation%20and%20feedback%20in%20a%20loop) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-bea-tools"></span>Anthropic — [Building effective agents，附录：工具设计](https://www.anthropic.com/research/building-effective-agents#:~:text=we%20actually%20spent%20more%20time%20optimizing%20our%20tools%20than%20the%20overall%20prompt) — fetched [2026-10-20](https://web.archive.org/web/20250304092058/https://www.anthropic.com/research/building-effective-agents)
- <span id="ref-ant-multi"></span>Anthropic — [How we built our multi-agent research system（2025-06-13），token 用量](https://www.anthropic.com/engineering/multi-agent-research-system#:~:text=multi%2Dagent%20systems%20use%20about%2015%C3%97%20more%20tokens%20than%20chats) — fetched [2026-10-20](https://web.archive.org/web/20261019054922/https://www.anthropic.com/engineering/multi-agent-research-system)
- <span id="ref-ant-multi-90"></span>Anthropic — [How we built our multi-agent research system，并行带来的提速](https://www.anthropic.com/engineering/multi-agent-research-system#:~:text=These%20changes%20cut%20research%20time%20by%20up%20to%2090%25%20for%20complex%20queries) — fetched [2026-10-20](https://web.archive.org/web/20261019054922/https://www.anthropic.com/engineering/multi-agent-research-system)
- <span id="ref-ant-multi-20"></span>Anthropic — [How we built our multi-agent research system，评测起步](https://www.anthropic.com/engineering/multi-agent-research-system#:~:text=We%20started%20with%20a%20set%20of%20about%2020%20queries%20representing%20real%20usage%20patterns.) — fetched [2026-10-20](https://web.archive.org/web/20261019054922/https://www.anthropic.com/engineering/multi-agent-research-system)
- <span id="ref-ant-ctx"></span>Anthropic — [Effective context engineering for AI agents（2025-09-29）](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents#:~:text=must%20be%20treated%20as%20a%20finite%20resource%20with%20diminishing%20marginal%20returns) — fetched [2026-10-20](https://web.archive.org/web/20261018164445/https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- <span id="ref-ant-tools"></span>Anthropic — [Writing effective tools for agents — with agents（2025-09-11）](https://www.anthropic.com/engineering/writing-tools-for-agents#:~:text=We%20recommend%20building%20a%20few%20thoughtful%20tools%20targeting%20specific%20high%2Dimpact%20workflows) — fetched [2026-10-20](https://web.archive.org/web/20261019034237/https://www.anthropic.com/engineering/writing-tools-for-agents)
- <span id="ref-ant-evals"></span>Anthropic — [Demystifying evals for AI agents（2026-01-09）](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#:~:text=20%2D50%20simple%20tasks%20drawn%20from%20real%20failures%20is%20a%20great%20start) — fetched [2026-10-20](https://web.archive.org/web/20261017091633/https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- <span id="ref-ant-evals-reg"></span>Anthropic — [Demystifying evals for AI agents，回归评测](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#:~:text=should%20have%20a%20nearly%20100%25%20pass%20rate) — fetched [2026-10-20](https://web.archive.org/web/20261017091633/https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- <span id="ref-ant-evals-days"></span>Anthropic — [Demystifying evals for AI agents，换模型的速度](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents#:~:text=teams%20without%20evals%20face%20weeks%20of%20testing%20while%20competitors%20with%20evals%20can%20quickly%20determine) — fetched [2026-10-20](https://web.archive.org/web/20261017091633/https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- <span id="ref-ant-ccbp"></span>Anthropic — [Claude Code 文档：Best practices（页面未标日期；原 anthropic.com 工程博客文章已跳转到这里）](https://code.claude.com/docs/en/best-practices#:~:text=Give%20Claude%20a%20check%20it%20can%20run%3A%20tests%2C%20a%20build%2C%20a%20screenshot%20to%20compare.) — fetched [2026-10-20](https://web.archive.org/web/20261020140348/https://code.claude.com/docs/en/best-practices)
- <span id="ref-ant-stripe"></span>Anthropic — [客户案例：Stripe（页面未标日期）](https://claude.com/customers/stripe#:~:text=Migrated%2010%2C000%20lines%20of%20Scala%20to%20Java%20in%20four%20days%2C%20a%20project%20estimated%20at%20ten%20engineering%20weeks%20without%20AI%20assistance) — fetched [2026-10-20](https://web.archive.org/web/20261014104614/https://claude.com/customers/stripe)
- <span id="ref-ant-zendesk"></span>Anthropic — [客户案例：Zendesk（页面未标日期）](https://claude.com/customers/zendesk#:~:text=Raised%20automated%20resolution%20by%20up%20to%2010%25%20while%20cutting%20human%20handle%20times%20by%20up%20to%2080%25%20for%20customers%20running%20custom%20agents) — fetched [2026-10-20](https://web.archive.org/web/20261016211414/https://claude.com/customers/zendesk)
- <span id="ref-ant-carvana"></span>Anthropic — [客户案例：Carvana（页面未标日期）](https://claude.com/customers/carvana#:~:text=Cut%20alerts%20in%20its%20retail%20science%20channel%20by%2056%25%20by%20resolving%20the%20root%20causes) — fetched [2026-10-20](https://web.archive.org/web/20261017013134/https://claude.com/customers/carvana)
- <span id="ref-ant-qonto"></span>Anthropic — [客户案例：Qonto（页面未标日期）](https://claude.com/customers/qonto#:~:text=Cuts%20client%20invoice%20creation%20time%203X%2C%20with%20its%20AI%20agents%20drafting%20every%20invoice%20and%20the%20customer%20confirming%20before%20it) — fetched [2026-10-20](https://web.archive.org/web/20261017044900/https://claude.com/customers/qonto)
- <span id="ref-ant-spellbook"></span>Anthropic — [客户案例：Spellbook（页面未标日期）](https://claude.com/customers/spellbook#:~:text=Cuts%20the%20time%20to%20complete%20an%20agreement%2010x%2C%20from%20roughly%2010%20hours%20of%20lawyer%20work%20to%20about%20one) — fetched [2026-10-20](https://web.archive.org/web/20260929202106/https://claude.com/customers/spellbook)
- <span id="ref-ant-rocket"></span>Anthropic — [客户案例：Rocket Money（页面未标日期）](https://claude.com/customers/rocket-money#:~:text=routes%20each%20request%20through%20a%20Haiku%204.5%20classifier%20to%20single%2Dresponsibility%20subagents) — fetched [2026-10-20](https://web.archive.org/web/20260929202106/https://claude.com/customers/rocket-money)
- <span id="ref-oai-sea-n"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），方法说明](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=4)，PDF 第 4 页，原文：“An OpenAI survey of 9,000 workers across almost 100 enterprises” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-time"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），自报省时](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=7)，PDF 第 7 页，原文：“On average, ChatGPT Enterprise users attribute 40–60 minutes of time saved per active day to their use of AI” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-gpts"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），Custom GPT 和 Project](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=5)，PDF 第 5 页，原文：“approximately 20% of all Enterprise messages were processed via a Custom GPT or Project.” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-6x"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），前沿员工的定义](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=13)，PDF 第 13 页，原文：“Frontier workers generate 6x more messages than the median worker.” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-unused"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），未用功能](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=15)，PDF 第 15 页，原文：“Of monthly active users, 19% have never used data analysis, 14% have never used reasoning, and 12% have never used search.” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-intercom"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），Intercom 案例](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=17)，PDF 第 17 页，原文：“customers are seeing Fin Voice resolve 53% of calls end-to-end on average” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-bbva"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），BBVA 案例](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=20)，PDF 第 20 页，原文：“automates more than 9,000 queries annually and has enabled BBVA to redeploy the equivalent of 3 FTE” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-sea-org"></span>OpenAI — [The state of enterprise AI: 2025 report（发布页日期 2025-12-08），结论](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf#page=23)，PDF 第 23 页，原文：“The primary constraints for organizations are no longer model performance or tooling, but rather organizational readiness.” — fetched [2026-10-20](https://web.archive.org/web/20260905101442/https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf)
- <span id="ref-oai-gdpval-scope"></span>OpenAI — [Measuring the performance of our models on real-world tasks（GDPval，2025-09-25），任务规模](https://openai.com/index/gdpval/#:~:text=The%20GDPval%20full%20set%20includes%201%2C320%20specialized%20tasks%20%28220%20in%20the%20gold%20open%2Dsourced%20set%29) — fetched [2026-10-20](https://web.archive.org/web/20261017004644/https://openai.com/index/gdpval/)
- <span id="ref-oai-gdpval-100x"></span>OpenAI — [GDPval 发布文章，速度和成本的说明](https://openai.com/index/gdpval/#:~:text=these%20figures%20reflect%20pure%20model%20inference%20time%20and%20API%20billing%20rates%2C%20and%20therefore%20do%20not%20capture%20the%20human%20oversight) — fetched [2026-10-20](https://web.archive.org/web/20261017004644/https://openai.com/index/gdpval/)
- <span id="ref-oai-gdpval-7h"></span>OpenAI — [GDPval 论文，任务时长](https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf#page=2)，PDF 第 2 页，原文：“Tasks require an average of 7 hours of work for an expert professional to complete.” — fetched [2026-10-20](https://web.archive.org/web/20261011210010/https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf)
- <span id="ref-oai-gdpval-476"></span>OpenAI — [GDPval 论文，首批结果](https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf#page=6)，PDF 第 6 页，原文：“47.6% of deliverables by Claude Opus 4.1 were graded as better than (wins) or as good as (ties) the human deliverable.” — fetched [2026-10-20](https://web.archive.org/web/20261011210010/https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf)
- <span id="ref-oai-gdpval-table"></span>OpenAI — [GDPval 论文，表 2：不同审核策略下的速度和成本改善（gpt-5 一行：Naive 90x，Try nx 1.39x；成本 Try nx 1.63x；gpt-4o 一行 Try nx 0.46x）](https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf#page=15)，PDF 第 15 页，原文：“When incorporating time to review and redo work, the payoff from using a model shrinks.” — fetched [2026-10-20](https://web.archive.org/web/20261011210010/https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf)
- <span id="ref-oai-gdpval-cat"></span>OpenAI — [GDPval 论文，失败的严重程度](https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf#page=15)，PDF 第 15 页，原文：“roughly 29% of ratings were for bad or catastrophic (with roughly 3% of failures marked as catastrophic)” — fetched [2026-10-20](https://web.archive.org/web/20261011210010/https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf)
- <span id="ref-oai-gpt52"></span>OpenAI — [Introducing GPT-5.2（2025-12-11）](https://openai.com/index/introducing-gpt-5-2/#:~:text=beats%20or%20ties%20top%20industry%20professionals%20on%2070.9%25%20of%20comparisons%20on%20GDPval%20knowledge%20work%20tasks) — fetched [2026-10-20](https://web.archive.org/web/20261016235949/https://openai.com/index/introducing-gpt-5-2/)
- <span id="ref-oai-aie-evals"></span>OpenAI — [AI in the Enterprise（PDF，未标日期），第一条经验](https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf#page=5)，PDF 第 5 页，原文：“Use a systematic evaluation process to measure how models perform against your use cases.” — fetched [2026-10-20](https://web.archive.org/web/20261002212454/https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf)
- <span id="ref-oai-aie-ms"></span>OpenAI — [AI in the Enterprise（PDF，未标日期），Morgan Stanley](https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf#page=7)，PDF 第 7 页，原文：“access to documents has jumped from 20% to 80%” — fetched [2026-10-20](https://web.archive.org/web/20261002212454/https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf)
- <span id="ref-oai-aie-indeed"></span>OpenAI — [AI in the Enterprise（PDF，未标日期），Indeed](https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf#page=10)，PDF 第 10 页，原文：“deliver similar results with 60% fewer tokens.” — fetched [2026-10-20](https://web.archive.org/web/20261002212454/https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf)
- <span id="ref-oai-aie-bbva"></span>OpenAI — [AI in the Enterprise（PDF，未标日期），BBVA](https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf#page=16)，PDF 第 16 页，原文：“In five months, BBVA employees created over 2,900 custom GPTs” — fetched [2026-10-20](https://web.archive.org/web/20261002212454/https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf)
- <span id="ref-oai-usecases-3"></span>OpenAI — [Identifying and scaling AI use cases（PDF，未标日期），三类机会](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf#page=6)，PDF 第 6 页，原文：“focus on common workplace challenges in these three key areas” — fetched [2026-10-20](https://web.archive.org/web/20261006055303/https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)
- <span id="ref-oai-usecases-prim"></span>OpenAI — [Identifying and scaling AI use cases（PDF，未标日期），六类基本用例（名称列在第 11 页）](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf#page=10)，PDF 第 10 页，原文：“Most use cases fall into one of six” — fetched [2026-10-20](https://web.archive.org/web/20261006055303/https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)
- <span id="ref-oai-usecases-quick"></span>OpenAI — [Identifying and scaling AI use cases（PDF，未标日期），影响和投入矩阵](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf#page=26)，PDF 第 26 页，原文：“Quick wins with strong impact and low effort” — fetched [2026-10-20](https://web.archive.org/web/20261006055303/https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)
- <span id="ref-oai-usecases-q"></span>OpenAI — [Identifying and scaling AI use cases（PDF，未标日期），每季度重新打分](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf#page=28)，PDF 第 28 页，原文：“Re-evaluate this scoring each quarter” — fetched [2026-10-20](https://web.archive.org/web/20261006055303/https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)
- <span id="ref-oai-usecases-map"></span>OpenAI — [Identifying and scaling AI use cases（PDF，未标日期），拆解工作流](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf#page=30)，PDF 第 30 页，原文：“Encourage power users to break workflows into individual tasks” — fetched [2026-10-20](https://web.archive.org/web/20261006055303/https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)
- <span id="ref-oai-agents-det"></span>OpenAI — [A practical guide to building agents（PDF，未标日期），何时值得做智能体](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf#page=6)，PDF 第 6 页，原文：“Otherwise, a deterministic solution may suffice.” — fetched [2026-10-20](https://web.archive.org/web/20261010054944/https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- <span id="ref-oai-agents-base"></span>OpenAI — [A practical guide to building agents（PDF，未标日期），选模型](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf#page=8)，PDF 第 8 页，原文：“build your agent prototype with the most capable model for every task to establish a performance baseline.” — fetched [2026-10-20](https://web.archive.org/web/20261010054944/https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- <span id="ref-oai-agents-single"></span>OpenAI — [A practical guide to building agents（PDF，未标日期），先用足单个智能体](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf#page=16)，PDF 第 16 页，原文：“Our general recommendation is to maximize a single agent” — fetched [2026-10-20](https://web.archive.org/web/20261010054944/https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- <span id="ref-oai-agents-human"></span>OpenAI — [A practical guide to building agents（PDF，未标日期），人工介入](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf#page=31)，PDF 第 31 页，原文：“Actions that are sensitive, irreversible, or have high stakes should trigger human oversight” — fetched [2026-10-20](https://web.archive.org/web/20261010054944/https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- <span id="ref-oai-codex-roles"></span>OpenAI — [Building an AI-Native Engineering Team（页面未标日期），角色分工](https://learn.chatgpt.com/guides/build-ai-native-engineering-team#:~:text=The%20agent%20becomes%20the%20first%2Dpass%20implementer%3B%20the%20engineer%20becomes%20the%20reviewer%2C%20editor%2C%20and%20source%20of%20direction.) — fetched [2026-10-20](https://web.archive.org/web/20261020234937/https://learn.chatgpt.com/guides/build-ai-native-engineering-team)
- <span id="ref-oai-codex-tests"></span>OpenAI — [Building an AI-Native Engineering Team，测试先行](https://learn.chatgpt.com/guides/build-ai-native-engineering-team#:~:text=defining%20high%20quality%20tests%20is%20often%20the%20first%20step%20to%20allowing%20an%20agent%20to%20build%20a%20feature.) — fetched [2026-10-20](https://web.archive.org/web/20261020234937/https://learn.chatgpt.com/guides/build-ai-native-engineering-team)
- <span id="ref-oai-codex-review"></span>OpenAI — [Building an AI-Native Engineering Team，代码审查](https://learn.chatgpt.com/guides/build-ai-native-engineering-team#:~:text=Code%20review%20doesn%E2%80%99t%20necessarily%20make%20the%20pull%20request%20process%20faster) — fetched [2026-10-20](https://web.archive.org/web/20261020234937/https://learn.chatgpt.com/guides/build-ai-native-engineering-team)
- <span id="ref-oai-usage-writing"></span>OpenAI — [How People Use ChatGPT（工作论文，2025-09-15；只统计消费者版）](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf#page=3)，PDF 第 3 页，原文：“Writing is the most common use case at work, accounting for 40% of work-related messages” — fetched [2026-10-20](https://web.archive.org/web/20261005155133/https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf)
- <span id="ref-oai-ms-eval"></span>OpenAI — [客户案例：Morgan Stanley（页面未标日期）](https://openai.com/index/morgan-stanley/#:~:text=implementing%20an%20evaluation%20%28eval%29%20framework%20to%20test%20every%20AI%20use%20case%20before%20deployment.) — fetched [2026-10-20](https://web.archive.org/web/20261014180350/https://openai.com/index/morgan-stanley/)
- <span id="ref-oai-ms-reg"></span>OpenAI — [客户案例：Morgan Stanley，回归测试](https://openai.com/index/morgan-stanley/#:~:text=Daily%20testing%20with%20a%20regression%20suite%20of%20sample%20questions%20identified%20potential%20weaknesses) — fetched [2026-10-20](https://web.archive.org/web/20261014180350/https://openai.com/index/morgan-stanley/)
- <span id="ref-oai-klarna"></span>OpenAI — [客户案例：Klarna（页面未标日期；数字取自上线第一个月）](https://openai.com/index/klarna/#:~:text=Customers%20now%20resolve%20their%20errands%20in%20less%20than%202%20mins%20compared%20to%2011%20mins%20previously) — fetched [2026-10-20](https://web.archive.org/web/20260927022703/https://openai.com/index/klarna/)
- <span id="ref-oai-cisco"></span>OpenAI — [客户案例：Cisco（2026-05-27）](https://openai.com/index/cisco/#:~:text=a%20~20%25%20reduction%20in%20build%20times%20and%20more%20than%201%2C500%20engineering%20hours%20saved%20per%20month%20across%20global%20environments.) — fetched [2026-10-20](https://web.archive.org/web/20261014104616/https://openai.com/index/cisco/)
- <span id="ref-oai-signals-83"></span>OpenAI — [From assistance to execution: How enterprises put AI to work（2026-08-12）](https://openai.com/index/how-enterprises-put-ai-to-work/#:~:text=now%20generate%208.3%C3%97%20as%20many%20output%20tokens%20per%20active%20user%20as%20typical%20firms%2C%20up%20from%202.6%C3%97%20in%20January) — fetched [2026-10-20](https://web.archive.org/web/20261014080430/https://openai.com/index/how-enterprises-put-ai-to-work/)
- <span id="ref-oai-signals-agenda"></span>OpenAI — [From assistance to execution，给管理者的建议](https://openai.com/index/how-enterprises-put-ai-to-work/#:~:text=connect%20agents%20to%20the%20context%20and%20tools%20needed%20to%20complete%20valuable%20work%3B%20establish%20clear%20permissions%2C%20review%2C%20and%20governance) — fetched [2026-10-20](https://web.archive.org/web/20261014080430/https://openai.com/index/how-enterprises-put-ai-to-work/)
- <span id="ref-oai-signals-tokens"></span>OpenAI — [How frontier firms are pulling ahead（2026-05-06）](https://openai.com/index/introducing-b2b-signals/#:~:text=Tokens%20are%20not%20a%20direct%20measure%20of%20business%20value) — fetched [2026-10-20](https://web.archive.org/web/20260620030248/https://openai.com/index/introducing-b2b-signals/)
- <span id="ref-oai-signals-leading"></span>OpenAI — [How frontier firms are pulling ahead，领先企业的做法](https://openai.com/index/introducing-b2b-signals/#:~:text=Leading%20firms%20measure%20depth%2C%20build%20governance%20for%20production%20use%2C%20invest%20in%20enablement%2C%20scale%20what%20works) — fetched [2026-10-20](https://web.archive.org/web/20260620030248/https://openai.com/index/introducing-b2b-signals/)
- <span id="ref-x-proc"></span>xAI — [Setting Grok Bot loose on procurement（2026-09-04）](https://x.ai/news/grok-bot-procurement#:~:text=So%20far%2C%20it%20has%20identified%20more%20than%20%24100%2C000%20in%20direct%20savings) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-procurement)
- <span id="ref-x-proc-seats"></span>xAI — [Setting Grok Bot loose on procurement，闲置席位](https://x.ai/news/grok-bot-procurement#:~:text=For%20one%20product%2C%20it%20found%2043%20paid%20seats%20with%20no%20activity%20in%20the%20previous%2090%20days) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-procurement)
- <span id="ref-x-proc-approval"></span>xAI — [Setting Grok Bot loose on procurement，审批规则](https://x.ai/news/grok-bot-procurement#:~:text=required%20explicit%20approval%20for%20spending%20money%2C%20accepting%20terms%2C%20or%20sending%20something%20to%20a%20vendor) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-procurement)
- <span id="ref-x-support"></span>xAI — [How SpaceXSI is using Grok Bot to scale customer support（2026-09-22）](https://x.ai/news/grok-bot-customer-support#:~:text=Our%20new%20combined%20team%20has%20seen%20a%20175%25%20increase%20in%20support%20tickets%2C%20but%20we%20have%20not%20had%20to%20hire%20any%20new%20people) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-customer-support)
- <span id="ref-x-support-method"></span>xAI — [How SpaceXSI is using Grok Bot to scale customer support，上线方式](https://x.ai/news/grok-bot-customer-support#:~:text=while%20limiting%20it%20to%20internal%20notes%20and%20requiring%20human%20approval%20for%20every%20write%20action) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-customer-support)
- <span id="ref-x-support-direct"></span>xAI — [How SpaceXSI is using Grok Bot to scale customer support，放权过程](https://x.ai/news/grok-bot-customer-support#:~:text=we%20had%20enough%20confidence%20to%20let%20it%20begin%20responding%20directly%20to%20customers) — fetched [2026-10-20](https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-customer-support)
- <span id="ref-x-incident"></span>xAI — [Using Grok Bot to detect and respond to incidents（2026-10-20）](https://x.ai/news/incident-sweep#:~:text=IncidentSweep%2C%20cleared%20204%20tickets%20in%20about%2010%20minutes%20with%20a%20support%20engineer%20reviewing%20and%20approving%20the%20batch) — fetched [2026-10-20](https://web.archive.org/web/20261020235138/https://x.ai/news/incident-sweep)
- <span id="ref-x-ent-access"></span>xAI — [Grok Bot for Enterprise（2026-09-03）](https://x.ai/news/grok-bot-for-enterprise#:~:text=A%20Bot%20has%20no%20access%20by%20default%20and%20reaches%20only%20the%20accounts%20you%20sign%20it%20into.) — fetched [2026-10-20](https://web.archive.org/web/20261001153009/https://x.ai/news/grok-bot-for-enterprise)
- <span id="ref-g-merge"></span>Google（Sundar Pichai） — [Google DeepMind: Bringing together two world-class AI teams（2023-04-20）](https://blog.google/innovation-and-ai/technology/ai/april-ai-update/#:~:text=will%20bring%20together%20two%20leading%20research%20groups%20in%20the%20AI%20field%3A%20the%20Brain%20team%20from%20Google%20Research%2C%20and%20DeepMind) — fetched [2026-10-20](https://web.archive.org/web/20261012131320/https://blog.google/innovation-and-ai/technology/ai/april-ai-update/)
- <span id="ref-g-research-se"></span>Google Research — [AI in software engineering at Google: Progress and the path ahead（2024-06-06）](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/#:~:text=the%20same%20amount%20of%20characters%20in%20the%20code%20are%20now%20completed%20with%20AI%2Dbased%20assistance%20as%20are%20manually%20typed%20by%20developers) — fetched [2026-10-20](https://web.archive.org/web/20260929012956/https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/)
- <span id="ref-g-research-ab"></span>Google Research — [AI in software engineering at Google，上线原则](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/#:~:text=Quick%20iterations%20with%20online%20A%2FB%20experiments%20are%20key) — fetched [2026-10-20](https://web.archive.org/web/20260929012956/https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/)
- <span id="ref-g-migration-80"></span>Google Research — [Accelerating code migrations with AI（2024-07-18）](https://research.google/blog/accelerating-code-migrations-with-ai/#:~:text=we%20found%20that%2080%25%20of%20the%20code%20modifications%20in%20the%20landed%20CLs%20were%20AI%2Dauthored%2C%20the%20rest%20were%20human%2Dauthored) — fetched [2026-10-20](https://web.archive.org/web/20260917101552/https://research.google/blog/accelerating-code-migrations-with-ai/)
- <span id="ref-g-migration"></span>Google Research — [Accelerating code migrations with AI，省时估计](https://research.google/blog/accelerating-code-migrations-with-ai/#:~:text=The%20total%20time%20spent%20on%20the%20migration%20was%20reduced%20by%20an%20estimated%2050%25%20as%20reported%20by%20the%20engineers%20doing%20the%20migration.) — fetched [2026-10-20](https://web.archive.org/web/20260917101552/https://research.google/blog/accelerating-code-migrations-with-ai/)
- <span id="ref-g-rct-96"></span>Google 工程师（arXiv 论文） — [Paradis 等，How much does AI impact development speed? An enterprise-based randomized controlled trial（2024-10 提交）](https://arxiv.org/abs/2410.12944#:~:text=Our%20randomized%20controlled%20trial%20with%2096%20full%2Dtime%20Google%20software%20engineers) — fetched [2026-10-20](https://web.archive.org/web/20261001074701/https://arxiv.org/abs/2410.12944)
- <span id="ref-g-rct"></span>Google 工程师（arXiv 论文） — [Paradis 等，同上，摘要中的效应量：约 21%](https://arxiv.org/abs/2410.12944#:~:text=although%20our%20confidence%20interval%20is%20large) — fetched [2026-10-20](https://web.archive.org/web/20261001074701/https://arxiv.org/abs/2410.12944)
- <span id="ref-g-code25"></span>Google（Sundar Pichai） — [Q3 2024 earnings call remarks（2024-10-29）](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2024/#:~:text=more%20than%20a%20quarter%20of%20all%20new%20code%20at%20Google%20is%20generated%20by%20AI%2C%20then%20reviewed%20and%20accepted%20by%20engineers) — fetched [2026-10-20](https://web.archive.org/web/20261013055346/https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2024/)
- <span id="ref-g-code75"></span>Google（Sundar Pichai） — [Cloud Next 2026 演讲稿（2026-04-22）](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/#:~:text=75%25%20of%20all%20new%20code%20at%20Google%20is%20now%20AI%2Dgenerated%20and%20approved%20by%20engineers%2C%20up%20from%2050%25%20last%20fall) — fetched [2026-10-20](https://web.archive.org/web/20261006134736/https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)
- <span id="ref-g-alphaevolve"></span>Google DeepMind — [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms（2025-05-14）](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/#:~:text=continuously%20recovers%2C%20on%20average%2C%200.7%25%20of%20Google%E2%80%99s%20worldwide%20compute%20resources) — fetched [2026-10-20](https://web.archive.org/web/20261019155250/https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- <span id="ref-g-cooling"></span>Google DeepMind — [DeepMind AI reduces Google data centre cooling bill by 40%（2016-07-20）](https://deepmind.google/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/#:~:text=which%20equates%20to%20a%2015%20percent%20reduction%20in%20overall%20PUE%20overhead) — fetched [2026-10-20](https://web.archive.org/web/20261015131834/https://deepmind.google/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/)
- <span id="ref-g-ws105"></span>Google Workspace — [Google Workspace extends Gemini benefits to more customers（2024-09-24）](https://workspace.google.com/blog/product-announcements/google-workspace-extends-gemini-benefits-to-more-customers#:~:text=users%20save%20an%20average%20of%20105%20minutes%20per%20week%2C%20according%20to%20our%20recent%20study%20of%20enterprise%20customers) — fetched [2026-10-20](https://web.archive.org/web/20261012005642/https://workspace.google.com/blog/product-announcements/google-workspace-extends-gemini-benefits-to-more-customers)
- <span id="ref-g-ws105-n"></span>Google Workspace — [同上，脚注中的方法说明](https://workspace.google.com/blog/product-announcements/google-workspace-extends-gemini-benefits-to-more-customers#:~:text=We%20looked%20at%20more%20than%203%2C200%20responses%20from%20employees%20across%20a%20broad%20range%20of%20industries) — fetched [2026-10-20](https://web.archive.org/web/20261012005642/https://workspace.google.com/blog/product-announcements/google-workspace-extends-gemini-benefits-to-more-customers)
- <span id="ref-g-usecases"></span>Google Cloud — [1,302 real-world gen AI use cases（最后更新 2026-04-22），Macquarie Bank 条目](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=reclaiming%20over%20100%2C000%20hours%20of%20team%20member) — fetched [2026-10-20](https://web.archive.org/web/20261010233327/https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- <span id="ref-g-usecases-vv"></span>Google Cloud — [同上，Virgin Voyages 条目](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Virgin%20Voyages%20have%20already%20deployed%20more%20than%201%2C000%20specialized%20agents%20to%20reduce%20campaign%20creation%20times%20by%2040%25) — fetched [2026-10-20](https://web.archive.org/web/20261010233327/https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- <span id="ref-g-usecases-cme"></span>Google Cloud — [同上，CME Group 条目](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=most%20developers%20using%20Gemini%20Code%20Assist%20report%20a%20productivity%20gain%20of%20at%20least%2010.5%20hours%20a%20month) — fetched [2026-10-20](https://web.archive.org/web/20261010233327/https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- <span id="ref-g-usecases-deloitte"></span>Google Cloud — [同上，Deloitte 条目](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Deloitte%20increased%20analyst%20efficiency%20by%20more%20than%2060%25%20using%20Gemini%20in%20Security%20Operations) — fetched [2026-10-20](https://web.archive.org/web/20261010233327/https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- <span id="ref-g-macq-itnews"></span>iTnews — [Macquarie Bank saves 130,000 hours in seven months of Gemini Enterprise use（2026-04-29）](https://www.itnews.com.au/news/macquarie-bank-saves-130000-hours-in-seven-months-of-gemini-enterprise-use-625385#:~:text=delivered%20130%2C000%20productivity%20hours%20back%20to%20people) — fetched [2026-10-20](https://web.archive.org/web/20260927213217/https://www.itnews.com.au/news/macquarie-bank-saves-130000-hours-in-seven-months-of-gemini-enterprise-use-625385)
- <span id="ref-g-vv-press"></span>Virgin Voyages — [Virgin Voyages 新闻稿：超过 1,500 个 AI 智能体（2026-03-09）](https://www.virginvoyages.com/press/latest-releases/virgin-voyages-exceeds-1500-ai-agents-travel-ai-leader#:~:text=Content%20production%20time%20reduced%20by%2060%25%20on%20average) — fetched [2026-10-20](https://web.archive.org/web/20261009213115/https://www.virginvoyages.com/press/latest-releases/virgin-voyages-exceeds-1500-ai-agents-travel-ai-leader)
- <span id="ref-g-roi"></span>Google Cloud — [ROI of AI 2025 摘要文章（2025-09-04；问卷对象 3,466 名高管）](https://cloud.google.com/transform/roi-of-ai-how-agents-help-business#:~:text=Among%20those%20executives%20who%20report%20productivity%20gains%20in%20their%20organizations%2C%2039%25%20have%20seen%20productivity%20at%20least%20double) — fetched [2026-10-20](https://web.archive.org/web/20261020235156/https://cloud.google.com/transform/roi-of-ai-how-agents-help-business)
- <span id="ref-nl-futian"></span>深圳市人民政府网站（信息来源：福田区） — [福田区以DeepSeek为引擎加快政务智能化转型 70名AI“数智员工”上岗（2025-02-18）](https://www.sz.gov.cn/cn/xxgk/zfxxgj/gqdt/content/post_12006997.html#:~:text=%E5%AE%A1%E6%A0%B8%E6%97%B6%E9%97%B4%E7%BC%A9%E7%9F%AD90%25) — fetched [2026-10-20](https://web.archive.org/web/20250804141335/http://www.sz.gov.cn/cn/xxgk/zfxxgj/gqdt/content/post_12006997.html)
- <span id="ref-nl-jmir"></span>Journal of Medical Internet Research（PMC 全文） — [DeepSeek 在中国医院部署情况的范围综述（J Med Internet Res 2025;27:e80770）](https://pmc.ncbi.nlm.nih.gov/articles/PMC12680131/#:~:text=22%25%20%2813%2F58%29%20presenting%20assessment%20results) — fetched [2026-10-20](https://web.archive.org/web/20261021000218/https://pmc.ncbi.nlm.nih.gov/articles/PMC12680131/)
- <span id="ref-nl-jmir-over"></span>Journal of Medical Internet Research（PMC 全文） — [同上，关于医院自报效果的结论](https://pmc.ncbi.nlm.nih.gov/articles/PMC12680131/#:~:text=they%20were%20likely%20to%20report%20higher%20performance%20and%20fewer%20risks%20for%20DeepSeek) — fetched [2026-10-20](https://web.archive.org/web/20261021000218/https://pmc.ncbi.nlm.nih.gov/articles/PMC12680131/)
- <span id="ref-nl-glean"></span>Glean — [Waldo 发布文章（最后更新 2026-04-28）](https://www.glean.com/blog/waldo-launch#:~:text=~50%25%20lower%20latency%20and%20~25%25%20fewer%20tokens%20with%20no%20quality%20regression) — fetched [2026-10-20](https://web.archive.org/web/20261007060732/https://www.glean.com/blog/waldo-launch)
- <span id="ref-nl-bridgewater"></span>Thinking Machines Lab 网站（作者为 Bridgewater AIA Labs 研究人员） — [Learning to replicate expert judgment in financial tasks（2026-06-30）](https://thinkingmachines.ai/news/learning-to-replicate-expert-judgment-in-financial-tasks/#:~:text=a%2013.8x%20reduction%20in%20inference%20costs%20per%20task) — fetched [2026-10-20](https://web.archive.org/web/20261017005553/https://thinkingmachines.ai/news/learning-to-replicate-expert-judgment-in-financial-tasks/)
- <span id="ref-nl-cmacgm"></span>CMA CGM — [AI Now Summit 新闻稿（2026-05-27）](https://www.cmacgm-group.com/en/news-media/ai-now-summit-ai-deployment-across-cma-cgm-group-operations#:~:text=designed%20to%20support%20nearly%2080%2C000%20employees%20across%20CMA%20CGM%2C%20CEVA%20Logistics%2C%20and%20CMA%20Media.) — fetched [2026-10-20](https://web.archive.org/web/20260701173352/https://www.cmacgm-group.com/en/news-media/ai-now-summit-ai-deployment-across-cma-cgm-group-operations)
- <span id="ref-nl-gcaptain"></span>Reuters（gCaptain 转载） — [CMA CGM and French AI startup target customer service（2025-04-06）](https://gcaptain.com/cma-cgm-and-french-ai-startup-target-customer-service/#:~:text=would%20slash%20response%20times%20for%20customer%20advisers%20receiving%201%20million%20emails%20a%20week) — fetched [2026-10-20](https://web.archive.org/web/20260609152133/https://gcaptain.com/cma-cgm-and-french-ai-startup-target-customer-service/)
- <span id="ref-nl-zhipu-prosp"></span>智谱（港交所披露易） — [招股章程（2025-12-30）](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000017.pdf#page=185)，PDF 第 185 页，原文：“achieves an AI automation rate exceeding 50% in Q&A on new financial regulations” — fetched [2026-10-20](https://web.archive.org/web/20261002230645/https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000017.pdf)
- <span id="ref-nl-zhipu-h1"></span>智谱（港交所披露易） — [2026 年中期业绩公告（2026-08-31）](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0831/2026083101539.pdf#page=12)，PDF 第 12 页，原文：“have not yet generated material revenue” — fetched [2026-10-20](https://web.archive.org/web/20260909223213/https://www.hkexnews.hk/listedco/listconews/sehk/2026/0831/2026083101539.pdf)
- <span id="ref-nl-minimax-h1"></span>MiniMax（港交所披露易） — [2026 年中期业绩公告（2026-08-26）](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600680.pdf#page=2)，PDF 第 2 页，原文：“Revenue from our Open Platform and other AI-based enterprise services increased by 703.1%” — fetched [2026-10-20](https://web.archive.org/web/20260907164804/https://www.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600680.pdf)
- <span id="ref-nl-mistral-cisco"></span>Mistral AI — [客户案例：Cisco（页面未标日期）](https://mistral.ai/customers/cisco/#:~:text=Up%20to%2020%25%20time%20reduction%20%28estimated%29%20in%20creating%20renewal%20proposals) — fetched [2026-10-20](https://web.archive.org/web/20261006132756/https://mistral.ai/customers/cisco/)
- <span id="ref-nl-mistral-sap"></span>Mistral AI — [客户案例：SAP（页面未标日期）](https://mistral.ai/customers/sap/#:~:text=SBB%20achieved%20an%20estimated%2080%25%20reduction%20in%20repetitive%20support%20queries) — fetched [2026-10-20](https://web.archive.org/web/20260923121036/https://mistral.ai/customers/sap/)
- <span id="ref-nl-mistral-epo"></span>Mistral AI — [客户案例：European Patent Office（页面未标日期）](https://mistral.ai/customers/epo/#:~:text=the%20system%20achieved%20a%20throughput%20of%20400%2C000%20pages%20transcribed%20per%20day) — fetched [2026-10-20](https://web.archive.org/web/20261016083545/https://mistral.ai/customers/epo/)
- <span id="ref-nl-epo-press"></span>European Patent Office — [新闻稿（2026-03-11）](https://www.epo.org/en/news-events/press-centre/press-release/2026/1362048#:~:text=to%20further%20enhance%20the%20quality%20and%20efficiency%20of%20the%20patent%20granting%20process) — fetched [2026-10-20](https://web.archive.org/web/20260412232101/https://www.epo.org/en/news-events/press-centre/press-release/2026/1362048)
- <span id="ref-nl-mistral-capg"></span>Mistral AI — [客户案例：Capgemini（页面未标日期）](https://mistral.ai/customers/capgemini/#:~:text=Developer%20adoption%20jumped%20from%2030%25%20to%20100%25) — fetched [2026-10-20](https://web.archive.org/web/20261007203859/https://mistral.ai/customers/capgemini/)
- <span id="ref-nl-cohere-cw"></span>Cohere — [客户案例：CoreWeave（2026-02-03）](https://cohere.com/customer-stories/coreweave#:~:text=resolution%20time%20decreased%20from%204%2D8%20days%20to%202%2D5%20days%20due%20to%20improved%20internal%20procedures%20coupled%20with%20North%20automation) — fetched [2026-10-20](https://web.archive.org/web/20261015184739/https://cohere.com/customer-stories/coreweave)
- <span id="ref-nl-sakana-smbc"></span>Sakana AI — [三井住友銀行の提案書作成 AI（2026-04-30）](https://sakana.ai/smbc-proposal-ai/#:~:text=%E6%95%B0%E5%8D%81%E5%88%86%E3%81%8B%E3%82%89%E6%95%B0%E6%99%82%E9%96%93%E3%81%AB%E7%9F%AD%E7%B8%AE%E3%81%99%E3%82%8B%E8%A6%8B%E9%80%9A%E3%81%97%E3%81%A7%E3%81%99) — fetched [2026-10-20](https://web.archive.org/web/20261015011830/https://sakana.ai/smbc-proposal-ai/)
- <span id="ref-nl-sakana-mufg"></span>Sakana AI — [三菱UFJ銀行 AI 融資エキスパート（2026-03-06）](https://sakana.ai/mufg-ai-lending/#:~:text=%E4%B8%80%E9%80%A3%E3%81%AE%E8%A4%87%E9%9B%91%E3%81%AA%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9%E3%81%AE%E5%8A%B9%E7%8E%87%E5%8C%96%E3%82%92%E6%94%AF%E6%8F%B4%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E7%A2%BA%E8%AA%8D%E3%81%95%E3%82%8C%E3%81%BE%E3%81%97%E3%81%9F) — fetched [2026-10-20](https://web.archive.org/web/20261007190859/https://sakana.ai/mufg-ai-lending/)
- <span id="ref-nl-tml-chroma"></span>Thinking Machines Lab — [Tinker 页面（2026-10-15 版本）](https://thinkingmachines.ai/tinker/#:~:text=up%20to%2010%C3%97%20faster%20inference) — fetched [2026-10-20](https://web.archive.org/web/20261016150418/https://thinkingmachines.ai/tinker/)
- <span id="ref-nl-aleph"></span>Aleph Alpha — [官网首页](https://aleph-alpha.com/#:~:text=verk%C3%BCrzte%20Suchzeiten%20um%2090) — fetched [2026-10-20](https://web.archive.org/web/20261018233051/https://aleph-alpha.com/)
- <span id="ref-nl-ssi"></span>Safe Superintelligence — [官网首页](https://ssi.inc/#:~:text=one%20goal%20and%20one%20product%3A%20a%20safe%20superintelligence) — fetched [2026-10-20](https://web.archive.org/web/20261012142426/https://ssi.inc/)

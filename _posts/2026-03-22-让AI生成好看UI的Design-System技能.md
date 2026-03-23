---
title: "让 AI 生成好看 UI 的 Design System 技能：X 上最热的五种方案"
excerpt: "Figma 对 AI Agent 是隐形的。过去两周，X 上讨论 Agentic Development 的开发者们找到了答案：把设计原则显性化，让 Agent 读得懂、执行得了。"
date: 2026-03-22
lang: zh
categories:
  - learning-notes
tags:
  - ai
  - design
  - developer-tools
---

> **TL;DR：** Figma 对 AI Agent 是隐形的。解法不是抛弃设计系统，而是把它翻译成 Agent 能 100% 执行的格式——DESIGN.md、skill 包、Tailwind。

---

过去两周（2026年3月8日至今），X 上讨论 AI Agentic Development 时，一提到 Design System，几乎所有人都在说同一件事：

> **AI 生成的 UI 要么"AI slop"（泛紫渐变、无聊卡片堆叠），要么视觉不一致。根本原因是 Figma 文件对 Agent 是隐形的。**

这个问题让开发者和设计师都很痛苦。于是社区开始密集讨论解法，以下是目前被反复推荐、讨论热度最高的五种方案。

---

## 1. DESIGN.md（最火 — Google Stitch 官方推）

这是目前讨论量最大的方案，被称为 **"AGENTS.md for design tokens"**。

核心思路很简单：写一个纯文本 Markdown 文件，结构固定为六大节：

```
Overview / Colors / Typography / Elevation / Components / Do's & Don'ts
```

工作流程：

1. 在 Figma 里做好人类设计
2. 导出 / 提炼成 `DESIGN.md`
3. 放进 repo，跟组件一起做版本管理
4. AI Agent（Claude Code、Cursor、Pencil.dev 等）每次生成 UI 前强制读这个文件

**Google Stitch** 最近新增了一键导出 DESIGN.md 的功能，还支持 vibe-based prompt（"温暖科技感、苹果级精致"）快速生成起点文件。

很多人说：未来的 design handoff 不再是 Figma → 开发者，而是：

```
Figma → DESIGN.md → AI Agent → 生产代码
```

---

## 2. Impeccable.style + Design Skills（中文圈推得最猛的"全家桶"）

专门解决"AI 生成丑 UI"的工具，被多位中文开发者（如 @VikingAviator）疯狂安利。

它是一整套可安装的 design skill，包含 20+ slash command：

| 命令 | 作用 |
|---|---|
| `/audit` | 抓技术问题 |
| `/critique` | 抓 UX / taste 问题 |
| `/polish` | 自动美化 |
| `/normalize` | 统一视觉规范 |
| `/delight` | 增加令人愉悦的细节 |
| `/animate` | 加微交互 |
| `/colorize` | 色彩优化 |
| `/typeset` | 排版优化 |

标准工作流：`/audit` → `/critique` → `/polish` → `/animate`

内置 anti-patterns，直接告诉 Agent 要避免：
- 紫色渐变
- 默认卡片堆叠
- 过度嵌套
- 无意义 shadow

还能一键 extract design tokens。使用过的开发者普遍反馈：**AI 的 visual taste 直接起飞。**

---

## 3. skill.md / Design Skill Packs（typeui.sh 和 GitHub 现成 skill）

这一类方案把 design tokens 升级成**可执行的 runtime skill**：

- **[typeui.sh](https://typeui.sh)**：开源 CLI 工具，专门管理 `design skill.md` 文件。一键创建、组织、apply design system，AI 生成 UI 时自动套用。
- **ui-ux-pro-max-skill**（GitHub）：直接 plug 进 Claude / Cursor，内置 UI 动画模式、component thinking、clean interface 原则。
- **Emil Kowalski's Design Engineering Skill**：设计工程师视角，强调 motion、细节、系统性。
- **Aesthetic Skills Hub**：把颜色、排版、spacing、motion 打包成"可安装依赖"，Agent 直接 `install your-visual-DNA` 就能生成 on-brand 界面。

---

## 4. Tailwind CSS（企业级落地最快）

Gumroad 最近分享了一个决策：**把整个自定义 CSS design system 全部删掉，切换 Tailwind**。

原因很直接：

- 新人和 AI Agent 都能瞬间看懂 class
- 改 UI 速度飞起
- 视觉一致性天然保证

现在很多人把 **Tailwind + DESIGN.md** 组合使用，作为 agentic 项目的标配底座。

---

## 5. Figma + Prompt Engineering（过渡期必备）

很多设计师还在用 Figma 做初始 design system，但立刻会转成上面那些 agent-readable 格式。

新一代 UI/UX 设计师的 stack 正在变成：

```
设计原则 → Accessibility → Component 架构 → Figma Design System
→ 导出 tokens → 结构化 prompt → AI Agent → 生产 MVP
```

还有人更直接：截图 Dribbble / 真实 App → 丢给 AI（"pixel-perfect replication + extract exact HEX + spacing rules"），几秒出生产级代码。

---

## 核心转变

这场讨论背后是一个更大的范式转移：

**好看的 UI 不再只靠 color theory / typography 美学，而是把这些原则显性化、结构化成 AI 能 100% 执行的规则。**

- 传统 Figma 还是起点
- 但最终必须落地成 **agent-native 格式**

使用这些 skill 之后，大家普遍反馈：AI 生成的 UI 从"能用"直接进化到"惊艳、一致、可直接上线"。

---

## 推荐上手顺序

1. **先试 [Impeccable.style](https://impeccable.style)**：最快看到视觉提升
2. **配合 Google Stitch 生成 DESIGN.md**：建立项目级设计规范
3. **接 Tailwind / typeui.sh 落地到代码里**：完成 agent-native 闭环

---

你在 Agentic 项目里现在用哪套？欢迎在评论区聊聊你的实践。

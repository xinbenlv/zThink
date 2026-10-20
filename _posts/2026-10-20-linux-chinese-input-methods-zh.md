---
title: "2026 年 Linux 上打中文：输入法、语音输入和微信输入法的现状"
excerpt: "fcitx5 加拼音或雾凇拼音仍是主流；Typeless 9 月出了只有 x64 的 Linux 版，fcitx5 社区已经长出一批本地和云端识别的语音插件；微信输入法只有灰色的社区移植。"
date: 2026-10-20
lang: zh
translationKey: linux-chinese-input-methods-2026
published: true
cover_image:
  src: /assets/blogposts/2026-10-20-linux-chinese-input-methods/linux-chinese-input-00-cover.jpg
  x: 570
  y: 0
  size: 630
og_image: /assets/blogposts/2026-10-20-linux-chinese-input-methods/linux-chinese-input-00-cover.jpg
categories:
  - blog
tags:
  - Linux
  - 输入法
  - fcitx5
  - 语音输入
  - Whisper
  - 微信
---

*我在 Mac 上用 Lima 跑了一台 Debian 12 arm64 虚拟机，专门用来开 Linux 版微信。装好微信之后，我发现自己在虚拟机里打不了中文，于是把 2026 年 Linux 上的中文输入法和语音输入翻了一遍。本文写给想在 Linux 桌面（包括 Mac 上的 Linux 虚拟机）里顺畅打中文的工程师。文中的版本号、提交日期和下载链接都是我在 2026-10-20 当天读取的，这些数据变得很快。*

## 我先给出四条结论

1. **打字：** fcitx5 加官方拼音或者 Rime（中州韵）仍然是 Linux 上打中文的主流做法，Debian 官方源里直接就有。
2. **说话：** Typeless 在 [2026 年 9 月发布了 Linux 版](#ref-typeless-linux-notes)，但是[只提供 x64 的 deb 包](#ref-typeless-download)。另一条路是 fcitx5 的语音插件，社区已经写出了至少六个，本地识别和云端识别都有。
3. **微信输入法：** 腾讯[没有出 Linux 版](#ref-wetype-official)。社区有三个移植项目，都要求用户自己从腾讯的安装包里取出引擎，有媒体评论认为这种做法在合规上属于灰色地带。
4. **虚拟机：** 在 Mac 的 Linux 虚拟机里打中文，除了输入法本身，还要处理按键转发、剪贴板和麦克风三件事。

![一块键盘和一支麦克风同时连向一个写着 fcitx5 的中枢，中枢再把文字送进应用窗口](/assets/blogposts/2026-10-20-linux-chinese-input-methods/linux-chinese-input-01-fcitx5-hub.jpg)

## fcitx5 加拼音或雾凇拼音仍然是 Linux 打中文的主流

### Debian 装一个元包就能打拼音

Debian 12（bookworm）的官方源里有 fcitx5 [5.0.21](#ref-debian-fcitx5-src)。中文支持在 `fcitx5-chinese-addons` 这个[元包](#ref-debian-chinese-addons)里，元包会拉进 `fcitx5-pinyin`、`fcitx5-table` 等几个子包。`fcitx5-pinyin` 在 bookworm 里提供 [arm64 在内的九种架构](#ref-debian-fcitx5-pinyin)，所以 Apple Silicon 上的 arm64 虚拟机也能直接装。

```bash
sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-frontend-gtk3 fcitx5-frontend-qt5
```

### 雾凇拼音给 Rime 配上了长期维护的词库

想要更多定制的人可以换 Rime（中州韵）。Debian 12 的源里有 [`fcitx5-rime`](#ref-debian-fcitx5-rime)，同样提供 arm64 构建。很多人会给 Rime 装[雾凇拼音（rime-ice）](#ref-rime-ice)，这套方案自带长期维护的词库。雾凇拼音的 README 写明它[适配 Fcitx5](#ref-rime-ice)，并且给出了[把方案装进 `~/.config/fcitx5/rime` 的命令](#ref-rime-ice-install)。截至 2026-10-20，雾凇拼音在 GitHub 上有将近两万颗星，最近一次提交在 10 月 5 日。

### 搜狗输入法 Linux 版支持 arm64，但是官网没有列出 Debian

搜狗输入法 Linux 版是闭源软件。官网写明当前版本是 [V4.2.1](#ref-sogou-linux)，支持 x86_64、arm64、mips64el 和 loongarch64 四种架构。官网列出的系统是 Ubuntu（最新到 20.04）、优麒麟、深度、麒麟、统信 UOS 和中科方德，没有列出 Debian。我没有在 Debian 12 arm64 上试装搜狗。

### 应用要靠三个环境变量连上 fcitx5

装好输入法以后，应用还要知道去找 fcitx5。fcitx 官方 wiki 给出的[基本设置](#ref-fcitx-setup)是下面三个环境变量：

```bash
XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
```

wiki 同时提醒，这三行[只是演示变量的取值](#ref-fcitx-setup)，具体写进哪个文件要看用户的登录方式。Wayland 会话的规则不同：在 KDE Plasma 的 Wayland 会话里，wiki 建议[不要设置 `GTK_IM_MODULE` 和 `QT_IM_MODULE`](#ref-fcitx-wayland)。Debian 用户也可以运行 `im-config`，让系统替自己写好这些变量。

## Typeless 已经出了 Linux 版，但是只有 x64 的 deb

Typeless 是一款 AI 语音听写软件：用户说一段话，Typeless [去掉口头禅和重复](#ref-typeless-linux-notes)，整理成通顺的文字，再填进当前应用。2026 年 7 月，AUR 上出现过一个[非官方的 typeless 包](#ref-aur-typeless)，描述写着“unofficial Linux compatibility build”，到 10 月 20 日仍然是零票。

两个月后情况变了。Typeless 官网的 Linux 发布说明里，第一条记录是 [2026-09-24 的 2.2.0 版](#ref-typeless-linux-notes)，标题是“Introducing Typeless for Linux”。官网下载页现在有 [“Download for Linux”按钮](#ref-typeless-download)。我点了这个按钮，页面跳到的下载地址是 `linux-deb-x64`，最终文件是 `Typeless-2.2.1-x64.deb`，大小约 145 MB。我又按同样的命名规则试了 arm64 的 deb、AppImage 和 rpm，这几个地址都返回 404。

所以在 2026-10-20 这个时间点，x86_64 的 Debian 和 Ubuntu 用户可以直接装官方 Typeless。Apple Silicon 上的 arm64 虚拟机装不了 Typeless，只能看 fcitx5 的语音插件。

## fcitx5 社区已经长出一批语音输入插件

### 语音插件做成 fcitx5 模块，是为了借用输入法的上屏通道

fcitx5 仓库里有一个从 2021 年开到现在的讨论，标题是[“支持语音输入扩展插件”](#ref-fcitx-discussion)。fcitx5 提交数最多的开发者[翁学天（wengxt）](#ref-fcitx-contributors)当天就回复：语音在 PC 上[应该和普通输入法引擎并行](#ref-fcitx-wengxt)，就像手机键盘上多出一个语音按钮，用户随时可以回到键盘模式。

这个思路解释了为什么插件要做进 fcitx5。独立的语音工具要把文字“打”进应用，只能模拟按键或者借用剪贴板。fcitx5 模块直接走输入法的提交通道，nextless 的 README 把这一点写成[“it *is* the input method”](#ref-nextless-im)。对中文来说，这条通道意味着汉字不需要经过键盘布局翻译。

讨论区里 2026 年以后的回复，基本都在介绍各自的插件。我把能找到的六个项目列在下表里。下表的“识别”一列来自各项目的 README，属于项目自述；我没有实测这些插件的中文准确率，也没有找到第三方的横向对比数据。

| 项目 | 识别方式（项目自述） | 许可证 | 最近提交 | 对 arm64 Debian 12 的提示 |
| --- | --- | --- | --- | --- |
| [xifan2333/fcitx5-vinput](#ref-vinput) | 本地 sherpa-onnx；云端豆包、阿里云百炼、ElevenLabs、OpenAI 兼容接口；可选 LLM 改写 | GPL-3.0 | 2026-10-20 | 发布页直接提供 Debian 12 arm64 的 deb |
| [GavinLiuOnline/fcitx5-voiceinput](#ref-voiceinput) | 纯本地 SenseVoiceSmall INT8 加 Silero VAD | MIT | 2026-10-10 | 预编译 deb 只有 amd64，arm64 要从源码编译 |
| [WenYin-Community/fcitx5-voice-input](#ref-wenyin) | 云端 OpenAI 兼容接口、火山引擎豆包流式识别、小米 MiMo；本地只做 VAD | LGPL-3.0 | 2026-09-29 | Debian 12 源里没有 onnxruntime，要自己装 |
| [RevolutionLA/nextless](#ref-nextless) | 本地 Zipformer 或 FireRed；云端豆包流式 2.0、Qwen3-ASR | MIT | 2026-10-12 | 模型不随包分发，约 360 MB 或 1.2 GB |
| [xander-lin/ainput](#ref-ainput) | 云端通义千问、豆包；本地 Zipformer 或 FireRed | MIT | 2026-10-17 | AUR 预编译包要求 glibc 2.39 以上 |
| [diginatu/fcitx5-voice-input](#ref-diginatu) | 不带识别，把录音发给用户自建的 Whisper 服务或 OpenAI 兼容接口 | MIT | 2026-09-21 | 架构无关，识别服务可以放在宿主机上 |

### 六个插件各有取舍

**fcitx5-vinput** 是六个项目里星数最多、打包最全的一个。它在 GitHub 上有 593 颗星，打包覆盖 [Arch、Fedora、Ubuntu/Debian、Nix 和 Flatpak](#ref-vinput)，按右 Alt 录音，还能把识别结果交给 LLM 纠错或翻译。10 月 14 日发布的 v2.4.2 里有 [`debian12_arm64` 的 deb 包](#ref-vinput-release)，Lima 里的 Debian 12 arm64 可以直接装。fcitx5 讨论区里推荐它的回复写的是[“安装简单，使用效果好”](#ref-fcitx-vinput-rec)。GitHub 上还有一个同名分叉 littlechai/fcitx5-vinput，最近一次提交停在 2026 年 5 月。

**fcitx5-voiceinput** 走纯本地路线。项目自称[所有识别都在本机完成](#ref-voiceinput)，用 SenseVoiceSmall 识别、Silero VAD 断句，模型合计约 290 MB。这个项目 10 月 9 日才建仓，作者只在 [Ubuntu 22.04 上测试过](#ref-voiceinput-req)，预编译的 deb 包[只有 amd64](#ref-voiceinput-deb)。

**WenYin-Community/fcitx5-voice-input** 分叉自 devcxl/fcitx5-voice-input，只接云端识别。它支持 OpenAI 兼容接口、[小米 MiMo 和豆包流式识别](#ref-wenyin)；用豆包时，预编辑区会[实时显示中间结果](#ref-wenyin-partial)。这个插件有两个坑：Debian 12 的源里[没有 onnxruntime](#ref-wenyin-onnx)，用户要自己装；API 密钥[以明文存放](#ref-wenyin-key)在 `~/.config/fcitx5/conf/` 下。

**nextless** 在 README 里自称 [Typeless 风格的听写工具](#ref-nextless)，它分叉自 xander-lin/vinput，这个仓库现在已经[改名为 ainput](#ref-ainput)。nextless 允许把右 Ctrl 这类单独的修饰键设为录音键。README 写明中英混说在 Zipformer 上[“可用但不完美”](#ref-nextless-limits)，FireRed 更准但更慢。

**ainput** 的玩法是按住 CapsLock 说话，松开后上屏。本地引擎加模型[合计约 1.3 GB](#ref-ainput-size)。AUR 包和 [GitHub 发布页的压缩包](#ref-ainput-release)都[提供 x86_64 和 aarch64 两种预编译版本](#ref-ainput-aur)，但是要求 [glibc 2.39 或更新](#ref-ainput-glibc)。Debian 12 的 glibc 是 [2.36](#ref-debian-glibc)，所以 Debian 12 用户只能用 Meson 从源码编译。

**diginatu/fcitx5-voice-input** 是六个里最早的一个，2025 年 10 月建仓。它把自己定位成[“Quick Phrase”式的模块](#ref-diginatu)，不需要切换输入法；默认按 F12 录音，把音频 POST 给 [`localhost:9000` 上的 Whisper 服务](#ref-diginatu-endpoint)。这种设计适合虚拟机：识别服务可以跑在性能更好的宿主机上，虚拟机里只留录音和上屏。

### fcitx5 之外的语音工具靠模拟按键或剪贴板上屏

不走 fcitx5 的开源语音工具也不少。下面四个都支持 Linux，但是在中文场景里各有短板：

- **[OpenTypeless](#ref-opentypeless)** 是一个 Tauri 桌面应用，提供 Linux ARM64 包，输出方式是[模拟键盘或剪贴板粘贴](#ref-opentypeless-output)。
- **[Vocalinux](#ref-vocalinux)** 完全离线，基于 whisper.cpp，[通过 xdotool、IBus、wtype、ydotool 或剪贴板注入文字](#ref-vocalinux)。
- **[whisrs](#ref-whisrs)** 用 Rust 写成，做的是[按键盘布局模拟按键](#ref-whisrs)，同时提供 x86_64 和 aarch64 的预编译包。
- **[YazSes](#ref-yazses)** 基于 faster-whisper，默认完全离线，但是 README 自己写明：需要[开箱即用的非英语模型](#ref-yazses)的用户不适合用它。

按我的理解，模拟按键本来是为键盘上有的字符设计的，汉字要么借剪贴板粘贴，要么依赖特定的 Wayland 合成器助手。所以打中文时我更推荐 fcitx5 插件。

## 微信输入法只有社区移植，没有官方 Linux 版

微信输入法官网列出的下载只有 [macOS、iOS、Android、Windows 和 HarmonyOS](#ref-wetype-official) 五个平台。微信本身倒是有 [Linux 版](#ref-weixin-linux)，4.1.13 版提供 x86、ARM 和 LoongArch 三种架构，但是 Linux 版微信不带输入法。

社区目前有三个移植项目，思路都是在 Linux 上运行微信输入法的原版引擎：

![一个写着 APK 的包裹，箭头指向一块写着“引擎”的芯片，芯片再送进 fcitx5 的插槽，插槽下挂着“非官方”的标签](/assets/blogposts/2026-10-20-linux-chinese-input-methods/linux-chinese-input-02-wetype-port.jpg)

| 项目 | 引擎来源 | 架构 | 联网情况（项目自述） |
| --- | --- | --- | --- |
| [yu1745/wetype-ime-linux](#ref-wetype-ime-linux) | Android 版 3.5.4 的原生库 | x86_64 走 QEMU；ARM64 原生运行 | README 声明不保证专有引擎的网络行为 |
| [zhl-HFUT/vtype-linux](#ref-vtype) | 同上，基于 wetype-ime-linux | x86_64 有实机反馈；ARM64 的云功能未验证 | 不关联设备时不联网；云候选会发送拼音 |
| [panxuc/fcitx5-wetypex](#ref-wetypex) | macOS 版 2.2.3.657 的输入核心 | 只有 x86_64 | README 警告可能包含官方遥测 |

**wetype-ime-linux** 是三个项目里星数最多的一个。2026 年 9 月 24 日，V2EX 上一位用户发帖介绍这个项目，帖子说它[“不联网”，内存“平均 80M 峰值 160M”](#ref-v2ex-wetype)，80aj 当天转述了这组数字。我要提醒一点：80MB 和“不联网”都来自帖子，项目 README 本身写的是[功能清单“不构成对专有引擎内部网络行为的保证”](#ref-wetype-ime-linux-net)。

这个项目对 Mac 虚拟机用户有一个好消息：引擎本来就是 Android ARM64 版，所以 [ARM64 主机原生运行，不需要 QEMU](#ref-wetype-ime-linux)。坏消息是预编译的 fcitx5 插件[要求 glibc 2.38 以上和 Fcitx5 5.1.x](#ref-wetype-ime-linux-glibc)，Debian 12 的 glibc 是 2.36、fcitx5 是 5.0.21，所以要用项目里的 `build.sh` 从源码编译插件。

版权方面，这个项目[不分发任何微信输入法文件](#ref-wetype-ime-linux-apk)，安装脚本从腾讯官方服务器下载 APK，在本机打补丁。80aj 的评论认为，用户直接使用腾讯闭源组件的[合规性“仍处灰色地带”](#ref-80aj)。这是媒体的看法，不是法律结论。

**vtype-linux** 在 wetype-ime-linux 的基础上[补上了云候选、个人词库同步和常用语](#ref-vtype-upstream)。云功能要和手机或 Mac 上的微信输入法关联，README 列出了[会发给官方服务器的内容](#ref-vtype-net)，并提醒设备身份文件[“相当于你的登录凭据”](#ref-vtype-net)。

**WeTypeX** 走了另一条路，它用的是 macOS 版的输入核心，功能最全，连语音输入和“问 AI”都接上了。代价是 README 顶部的三条警告：[可能包含官方遥测](#ref-wetypex-warn)、处于早期开发阶段、要求[下载后 24 小时内删除](#ref-wetypex-warn)。WeTypeX 目前只支持 x86_64。

## 在 Mac 的 Linux 虚拟机里打中文还要再过三关

下面是我自己在 Lima 虚拟机里踩到的问题。我的环境是 Apple Silicon Mac 加 Lima 的 `vz` 驱动，客户机是 Debian 12 arm64。这些是我的观察，换一套虚拟化软件结论可能不同。

![Mac 和 Linux 虚拟机之间隔着一道墙，按键编号能穿过墙，汉字、剪贴板和麦克风声音被挡在墙外](/assets/blogposts/2026-10-20-linux-chinese-input-methods/linux-chinese-input-03-vm-wall.jpg)

### Mac 上的输入法打不进虚拟机窗口

我先试了最省事的办法：在 Mac 上用系统输入法或者 Typeless，对着 Lima 的原生窗口打字。结果一个汉字都进不去。我的理解是，Lima `vz` 的窗口只把按键编号转给客户机，Mac 输入法合成好的汉字没有通道进去。所以输入法必须装在虚拟机里面。

### Lima 没有剪贴板共享

退一步的办法是在 Mac 上打好字，再粘贴进虚拟机。这条路也不通：Lima 仓库里询问剪贴板共享的 [issue #424](#ref-lima-424) 从 2021 年 11 月开到现在，状态仍然是 open。

### Lima 的麦克风选项还在测试版里

在虚拟机里做语音输入，前提是客户机能收到麦克风的声音。Lima 在 2026 年 9 月 8 日合并了 [PR #5462](#ref-lima-5462)，给 `vz` 驱动加了实验性的 `audio.microphone` 选项。按照默认模板里的注释，这个选项[默认关闭，需要先设置 `audio.device`](#ref-lima-template)，开启后 macOS 会以 Lima 的名义申请麦克风权限。

这个改动包含在 [v2.3.0-beta.1](#ref-lima-beta) 里，没有进入当前的稳定版 v2.2.1。想用的人要装测试版，或者等 2.3.0 正式发布。另一个办法是用 diginatu 插件的思路，把识别服务放在宿主机上，但是录音仍然要在客户机里完成。

### Ctrl+空格会被 macOS 截走

fcitx5 在非 Apple 系统上的默认切换键是 [`Ctrl+空格`](#ref-fcitx-globalconfig)，而 macOS 把 [Control-空格设成了切换输入源的快捷键](#ref-apple-shortcut)。我在虚拟机窗口里按 Ctrl+空格，触发的是 Mac 的输入法切换。fcitx5 还有一个默认的临时切换键 [`Shift_L`](#ref-fcitx-globalconfig)，也就是左 Shift。所以我建议在虚拟机里只用左 Shift 切换中英，避开 macOS 的快捷键。

## 我会这样搭一台能打中文的 Linux 虚拟机

结合上面的调研，我给 Apple Silicon 上的 Debian 12 arm64 虚拟机排了一个顺序：

1. 在虚拟机里装 `fcitx5` 和 `fcitx5-chinese-addons`，用 `im-config` 设好环境变量，中英切换改用左 Shift。
2. 想要更好的词库，就加装 `fcitx5-rime` 和雾凇拼音。
3. 想要微信输入法的候选，就从源码编译 wetype-ime-linux 的插件，引擎在 arm64 上原生运行。
4. 语音输入先等 Lima 2.3.0 带上麦克风选项，再装 fcitx5-vinput 的 Debian 12 arm64 包试用。
5. 如果打算升级到 Debian 13，glibc 会升到 [2.41](#ref-debian-glibc)，fcitx5 会升到 [5.1.12](#ref-debian-fcitx5-src)，wetype-ime-linux 的预编译插件就满足版本要求了。

## 参考资料

- <span id="ref-debian-fcitx5-src"></span>Debian Sources — [fcitx5 各版本所在的发行版](https://sources.debian.org/src/fcitx5/)，bookworm 为 5.0.21-3，trixie 为 5.1.12-2 — fetched [2026-10-20](https://web.archive.org/web/20261020230758/https://sources.debian.org/src/fcitx5/)
- <span id="ref-debian-chinese-addons"></span>Debian Packages — [bookworm 的 fcitx5-chinese-addons 元包及其依赖](https://packages.debian.org/bookworm/fcitx5-chinese-addons) — fetched [2026-10-20](https://web.archive.org/web/20261020230640/https://packages.debian.org/bookworm/fcitx5-chinese-addons)
- <span id="ref-debian-fcitx5-pinyin"></span>Debian Packages — [bookworm 的 fcitx5-pinyin，下载区列出 arm64 等九种架构](https://packages.debian.org/bookworm/fcitx5-pinyin) — fetched [2026-10-20](https://web.archive.org/web/20261020230706/https://packages.debian.org/bookworm/fcitx5-pinyin)
- <span id="ref-debian-fcitx5-rime"></span>Debian Packages — [bookworm 的 fcitx5-rime](https://packages.debian.org/bookworm/fcitx5-rime) — fetched [2026-10-20](https://web.archive.org/web/20261020230732/https://packages.debian.org/bookworm/fcitx5-rime)
- <span id="ref-debian-glibc"></span>Debian Sources — [glibc 各版本所在的发行版](https://sources.debian.org/src/glibc/)，bookworm 为 2.36，trixie 为 2.41 — fetched [2026-10-20](https://web.archive.org/web/20261020230824/https://sources.debian.org/src/glibc/)
- <span id="ref-rime-ice"></span>iDvel — [雾凇拼音 README 第 7 行](https://github.com/iDvel/rime-ice/blob/da1fbe602e38f26db846fa10120ee64c2b0324c0/README.md#L7)：“适配小狼毫 Weasel、鼠须管 Squirrel、Fcitx5、iBus 等几乎所有 Rime 应用” — fetched [2026-10-20](https://web.archive.org/web/20261020232417/https://github.com/iDvel/rime-ice/blob/da1fbe602e38f26db846fa10120ee64c2b0324c0/README.md)
- <span id="ref-rime-ice-install"></span>iDvel — [雾凇拼音 README 第 36 行](https://github.com/iDvel/rime-ice/blob/da1fbe602e38f26db846fa10120ee64c2b0324c0/README.md#L36)：`rime_dir="$HOME/.config/fcitx5/rime" bash rime-install iDvel/rime-ice` — fetched [2026-10-20](https://web.archive.org/web/20261020232417/https://github.com/iDvel/rime-ice/blob/da1fbe602e38f26db846fa10120ee64c2b0324c0/README.md)
- <span id="ref-sogou-linux"></span>搜狗输入法 — [Linux 版首页](https://shurufa.sogou.com/linux)：“支持架构：x86_64、arm64、mips64el、loongarch64”“版本：V4.2.1” — fetched [2026-10-20](https://web.archive.org/web/20261020231008/https://shurufa.sogou.com/linux)
- <span id="ref-fcitx-setup"></span>Fcitx Wiki — [Setup Fcitx 5](https://fcitx-im.org/wiki/Setup_Fcitx_5#:~:text=the%20snippet%20above%20is%20just%20to%20demonstrate%20what%20these%20value%20gonna%20be)：“the snippet above is just to demonstrate what these value gonna be” — fetched [2026-10-20](https://web.archive.org/web/20261020230913/https://fcitx-im.org/wiki/Setup_Fcitx_5)
- <span id="ref-fcitx-wayland"></span>Fcitx Wiki — [Using Fcitx 5 on Wayland](https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#KDE_Plasma)，KDE Plasma 一节 — fetched [2026-10-20](https://web.archive.org/web/20261020230942/https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland)
- <span id="ref-aur-typeless"></span>AUR — [typeless 2.1.0-2](https://aur.archlinux.org/packages/typeless)：“AI voice dictation for any application (unofficial Linux compatibility build)”，首次提交 2026-07-22，0 票 — fetched [2026-10-20](https://web.archive.org/web/20261020231127/https://aur.archlinux.org/packages/typeless)
- <span id="ref-typeless-linux-notes"></span>Typeless — [Linux app release notes](https://www.typeless.com/help/release-notes/linux)，版本 2.2.0，日期 2026-09-24，标题“Introducing Typeless for Linux”；页面正文由 [JSON 数据](https://www.typeless.com/article-data/typeless-release-notes--v3--linux/en-us.json)渲染 — fetched [2026-10-20](https://web.archive.org/web/20261020231059/https://www.typeless.com/help/release-notes/linux)
- <span id="ref-typeless-download"></span>Typeless — [下载页](https://www.typeless.com/downloads)的“Download for Linux”按钮跳到 [`/desktop/linux-deb-x64/download`](https://www.typeless.com/desktop/linux-deb-x64/download)，重定向到 `Typeless-2.2.1-x64.deb`（145,036,432 字节）；作者同日按同样规则请求 `linux-deb-arm64`、`linux-appimage-x64`、`linux-rpm-x64`，均返回 404 — fetched [2026-10-20](https://web.archive.org/web/20261020231033/https://www.typeless.com/downloads)
- <span id="ref-fcitx-discussion"></span>fcitx/fcitx5 — [Discussion #358：支持语音输入扩展插件](https://github.com/fcitx/fcitx5/discussions/358)，2021-10-11 发起 — fetched 2026-10-20
- <span id="ref-fcitx-wengxt"></span>wengxt — [Discussion #358 的第一条回复](https://github.com/fcitx/fcitx5/discussions/358#discussioncomment-1460262)：“语音在 PC 上来说应该作为和普通的输入法引擎并行的系统” — fetched 2026-10-20
- <span id="ref-fcitx-contributors"></span>GitHub API — [fcitx/fcitx5 贡献者列表](https://api.github.com/repos/fcitx/fcitx5/contributors)，wengxt（Weng Xuetian）以 1814 次提交居首 — fetched [2026-10-20](https://web.archive.org/web/20261020232540/https://api.github.com/repos/fcitx/fcitx5/contributors)
- <span id="ref-fcitx-vinput-rec"></span>catcherxuefeng — [Discussion #358 的 2026-03-14 回复](https://github.com/fcitx/fcitx5/discussions/358#:~:text=%E5%AE%89%E8%A3%85%E7%AE%80%E5%8D%95%EF%BC%8C%E4%BD%BF%E7%94%A8%E6%95%88%E6%9E%9C%E5%A5%BD)：“安装简单，使用效果好” — fetched 2026-10-20
- <span id="ref-vinput"></span>xifan2333 — [fcitx5-vinput README 第 22–26 行](https://github.com/xifan2333/fcitx5-vinput/blob/065819ec430ac32060bf68511955196a2983b49e/README.md#L22-L26)，功能与打包；[第 88 行](https://github.com/xifan2333/fcitx5-vinput/blob/065819ec430ac32060bf68511955196a2983b49e/README.md#L88)：“Supports `x86_64-linux` and `aarch64-linux`” — fetched [2026-10-20](https://web.archive.org/web/20261020232555/https://github.com/xifan2333/fcitx5-vinput/blob/065819ec430ac32060bf68511955196a2983b49e/README.md)
- <span id="ref-vinput-release"></span>xifan2333 — [fcitx5-vinput v2.4.2 发布页](https://github.com/xifan2333/fcitx5-vinput/releases/tag/v2.4.2)，2026-10-14，附件含 `fcitx5-vinput_2.4.2-1_debian12_arm64.deb` — fetched [2026-10-20](https://web.archive.org/web/20261020232621/https://github.com/xifan2333/fcitx5-vinput/releases/tag/v2.4.2)
- <span id="ref-voiceinput"></span>GavinLiuOnline — [fcitx5-voiceinput README 第 10–11 行](https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md#L10-L12)：“Everything runs **locally**” — fetched [2026-10-20](https://web.archive.org/web/20261020232647/https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md)
- <span id="ref-voiceinput-req"></span>GavinLiuOnline — [fcitx5-voiceinput README 第 55 行](https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md#L55)：“tested on Ubuntu 22.04 / fcitx5 5.0.14” — fetched [2026-10-20](https://web.archive.org/web/20261020232647/https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md)
- <span id="ref-voiceinput-deb"></span>GavinLiuOnline — [fcitx5-voiceinput README 第 64 行](https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md#L64)：“Grab `fcitx5-voiceinput_<version>_amd64.deb`” — fetched [2026-10-20](https://web.archive.org/web/20261020232647/https://github.com/GavinLiuOnline/fcitx5-voiceinput/blob/f5ebcd85df55f003ce9f81c45ccba25fc9dc040b/README.md)
- <span id="ref-wenyin"></span>WenYin-Community — [fcitx5-voice-input README 第 23 行](https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md#L23)：“Volcengine Doubao streaming ASR, or Xiaomi MiMo ASR” — fetched [2026-10-20](https://web.archive.org/web/20261020232749/https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md)
- <span id="ref-wenyin-partial"></span>WenYin-Community — [fcitx5-voice-input README 第 26 行](https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md#L26)：“Real-time partial transcript update during speech (Volcengine, or OpenAI Realtime `ApiMode=realtime`)” — fetched [2026-10-20](https://web.archive.org/web/20261020232749/https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md)
- <span id="ref-wenyin-onnx"></span>WenYin-Community — [fcitx5-voice-input README 第 48 行](https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md#L48)：“Ubuntu 24.04 and Debian 12 do not ship onnxruntime in their repositories” — fetched [2026-10-20](https://web.archive.org/web/20261020232749/https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md)
- <span id="ref-wenyin-key"></span>WenYin-Community — [fcitx5-voice-input README 第 226 行](https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md#L226)：“API keys are stored in plain text” — fetched [2026-10-20](https://web.archive.org/web/20261020232749/https://github.com/WenYin-Community/fcitx5-voice-input/blob/a3df50268980779134dff78a90875b8ebe019fee/README.md)
- <span id="ref-nextless"></span>RevolutionLA — [nextless README 第 10–11 行](https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md#L10-L12)：“a Typeless-style dictation tool for Linux desktops”“It is a fork of xander-lin/vinput” — fetched [2026-10-20](https://web.archive.org/web/20261020232834/https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md)
- <span id="ref-nextless-im"></span>RevolutionLA — [nextless README 第 53 行](https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md#L53)：“yes — it *is* the input method” — fetched [2026-10-20](https://web.archive.org/web/20261020232834/https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md)
- <span id="ref-nextless-limits"></span>RevolutionLA — [nextless README 第 111–113 行](https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md#L111-L113)：“workable on Zipformer bilingual but imperfect” — fetched [2026-10-20](https://web.archive.org/web/20261020232834/https://github.com/RevolutionLA/nextless/blob/9364bb4cc35a4016bc75d7aa8982ded30427e760/README.md)
- <span id="ref-ainput"></span>xander-lin — [ainput 仓库](https://github.com/xander-lin/ainput)；旧地址 [github.com/xander-lin/vinput](https://github.com/xander-lin/vinput) 返回 301 跳转到 ainput — fetched [2026-10-20](https://web.archive.org/web/20261020231940/https://github.com/xander-lin/ainput)
- <span id="ref-ainput-size"></span>xander-lin — [ainput README 第 34–35 行](https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md#L34-L35)：“roughly 1.3 GB total” — fetched [2026-10-20](https://web.archive.org/web/20261020232901/https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md)
- <span id="ref-ainput-aur"></span>xander-lin — [ainput README 第 42 行](https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md#L42)：“prebuilt; x86_64 and aarch64” — fetched [2026-10-20](https://web.archive.org/web/20261020232901/https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md)
- <span id="ref-ainput-release"></span>xander-lin — [ainput 0.1.0 发布页](https://github.com/xander-lin/ainput/releases/tag/0.1.0)，附件为 `fcitx5-ainput-0.1.0-aarch64.tar.zst` 和 `fcitx5-ainput-0.1.0-x86_64.tar.zst` — fetched [2026-10-20](https://web.archive.org/web/20261020232927/https://github.com/xander-lin/ainput/releases/tag/0.1.0)
- <span id="ref-ainput-glibc"></span>xander-lin — [ainput README 第 46 行](https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md#L46)：“The prebuilt package needs glibc 2.39 or newer” — fetched [2026-10-20](https://web.archive.org/web/20261020232901/https://github.com/xander-lin/ainput/blob/6f515fc017af39334c06774ff59cde8a65c5e584/README.md)
- <span id="ref-diginatu"></span>diginatu — [fcitx5-voice-input README 第 3 行](https://github.com/diginatu/fcitx5-voice-input/blob/c5898a1b2776c189a0e92dc0c6b1d554593e6576/README.md#L3)：“designed as a "Quick Phrase" style module” — fetched [2026-10-20](https://web.archive.org/web/20261020233035/https://github.com/diginatu/fcitx5-voice-input/blob/c5898a1b2776c189a0e92dc0c6b1d554593e6576/README.md)
- <span id="ref-diginatu-endpoint"></span>diginatu — [fcitx5-voice-input README 第 33 行](https://github.com/diginatu/fcitx5-voice-input/blob/c5898a1b2776c189a0e92dc0c6b1d554593e6576/README.md#L33)：默认地址 `http://localhost:9000/asr?output=txt&encode=false` — fetched [2026-10-20](https://web.archive.org/web/20261020233035/https://github.com/diginatu/fcitx5-voice-input/blob/c5898a1b2776c189a0e92dc0c6b1d554593e6576/README.md)
- <span id="ref-opentypeless"></span>tover0314-w — [OpenTypeless README 第 54 行](https://github.com/tover0314-w/opentypeless/blob/f5ad60298f535e0fff716a749802138ee409dea7/README.md#L54)：“including Linux ARM64 packages” — fetched [2026-10-20](https://web.archive.org/web/20261020233102/https://github.com/tover0314-w/opentypeless/blob/f5ad60298f535e0fff716a749802138ee409dea7/README.md)
- <span id="ref-opentypeless-output"></span>tover0314-w — [OpenTypeless README 第 172 行](https://github.com/tover0314-w/opentypeless/blob/f5ad60298f535e0fff716a749802138ee409dea7/README.md#L172)：“Keyboard simulation, clipboard paste/copy-only” — fetched [2026-10-20](https://web.archive.org/web/20261020233102/https://github.com/tover0314-w/opentypeless/blob/f5ad60298f535e0fff716a749802138ee409dea7/README.md)
- <span id="ref-vocalinux"></span>VocaHQ — [Vocalinux README 第 47 行](https://github.com/VocaHQ/vocalinux/blob/4799f06bd246c2c38e8d2dd33f8e15710994fbca/README.md#L47)：“Text injection via xdotool, IBus, wtype, ydotool, or clipboard fallback” — fetched [2026-10-20](https://web.archive.org/web/20261020233129/https://github.com/VocaHQ/vocalinux/blob/4799f06bd246c2c38e8d2dd33f8e15710994fbca/README.md)
- <span id="ref-whisrs"></span>y0sif — [whisrs README 第 26 行](https://github.com/y0sif/whisrs/blob/a1923a786added0af05179d1ed6bef31eddf3caa/README.md#L26)：“layout-aware keyboard injection”；[第 32 行](https://github.com/y0sif/whisrs/blob/a1923a786added0af05179d1ed6bef31eddf3caa/README.md#L32)：“Quick install (Linux x86_64 / aarch64)” — fetched [2026-10-20](https://web.archive.org/web/20261020233155/https://github.com/y0sif/whisrs/blob/a1923a786added0af05179d1ed6bef31eddf3caa/README.md)
- <span id="ref-yazses"></span>MSKazemi — [YazSes README 第 73 行](https://github.com/MSKazemi/yazses/blob/ac44c1073c7517efb7bd9b646abc780bad0a1265/README.md#L73)：“**not** recommended if you need … non-English models out of the box” — fetched [2026-10-20](https://web.archive.org/web/20261020233222/https://github.com/MSKazemi/yazses/blob/ac44c1073c7517efb7bd9b646abc780bad0a1265/README.md)
- <span id="ref-wetype-official"></span>微信输入法 — [官网](https://z.weixin.qq.com/)，下载入口为 macOS 版、iOS 版、Android 版、Windows 版、HarmonyOS 版 — fetched [2026-10-20](https://web.archive.org/web/20261020231203/https://z.weixin.qq.com/)
- <span id="ref-weixin-linux"></span>微信 — [微信 Linux 版下载页](https://linux.weixin.qq.com/)，版本 4.1.13，提供 X86、ARM、LoongArch 版 — fetched [2026-10-20](https://web.archive.org/web/20261020231228/https://linux.weixin.qq.com/en)
- <span id="ref-wetype-ime-linux"></span>yu1745 — [wetype-ime-linux README 第 3 行](https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md#L3)：“x86_64 主机通过 QEMU user 模式运行，ARM64 主机原生运行，不需要 QEMU” — fetched [2026-10-20](https://web.archive.org/web/20261020233248/https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md)
- <span id="ref-wetype-ime-linux-apk"></span>yu1745 — [wetype-ime-linux README 第 7 行](https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md#L7)：“不包含任何 WeType 文件。安装时会从腾讯官方服务器下载 WeType 3.5.4 APK” — fetched [2026-10-20](https://web.archive.org/web/20261020233248/https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md)
- <span id="ref-wetype-ime-linux-glibc"></span>yu1745 — [wetype-ime-linux README 第 29 行](https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md#L29)：“要求宿主有 glibc ≥ 2.38 和 Fcitx5 5.1.x” — fetched [2026-10-20](https://web.archive.org/web/20261020233248/https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md)
- <span id="ref-wetype-ime-linux-net"></span>yu1745 — [wetype-ime-linux README 第 29 行](https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md#L29)：“上述功能清单不构成对专有引擎内部网络行为的保证” — fetched [2026-10-20](https://web.archive.org/web/20261020233248/https://github.com/yu1745/wetype-ime-linux/blob/3a127ef2cb5a9d9754e6307f462b188d8f31b878/README.md)
- <span id="ref-v2ex-wetype"></span>V2EX — [《微信输入法已被移植到 Linux》](https://www.v2ex.com/t/1244377)，2026 年 9 月 24 日，正文：“不联网”“平均 80M 峰值 160M” — fetched 2026-10-20
- <span id="ref-80aj"></span>80aj — [《微信输入法被移植到 Linux：基于 QEMU 运行安卓引擎，离线可用》](https://www.80aj.com/2026/09/24/wechat-input-linux-qemu/#:~:text=%E5%90%88%E8%A7%84%E6%80%A7%E4%BB%8D%E5%A4%84%E7%81%B0%E8%89%B2%E5%9C%B0%E5%B8%A6)，2026-09-24：“用户直接使用腾讯闭源组件的合规性仍处灰色地带” — fetched [2026-10-20](https://web.archive.org/web/20261020231259/https://www.80aj.com/2026/09/24/wechat-input-linux-qemu/)
- <span id="ref-vtype"></span>zhl-HFUT — [vtype-linux README 第 53 行](https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md#L53)：“ARM64 | 上游支持原生运行，本项目的云功能没验证” — fetched [2026-10-20](https://web.archive.org/web/20261020233315/https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md)
- <span id="ref-vtype-upstream"></span>zhl-HFUT — [vtype-linux README 第 40 行](https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md#L40)：“这里补上了云候选、二级词库、个人词库同步、常用语” — fetched [2026-10-20](https://web.archive.org/web/20261020233315/https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md)
- <span id="ref-vtype-net"></span>zhl-HFUT — [vtype-linux README 第 57–68 行](https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md#L57-L68)，“会发送什么”一节：“只用本地输入、不关联设备时，不会联网”“相当于你的登录凭据” — fetched [2026-10-20](https://web.archive.org/web/20261020233315/https://github.com/zhl-HFUT/vtype-linux/blob/f24a73f4f326271cf5a0ffedde7ebb67c22fa22c/README.md)
- <span id="ref-wetypex"></span>panxuc — [fcitx5-wetypex README 第 36 行](https://github.com/panxuc/fcitx5-wetypex/blob/f25300dc8775f4e840148d596b56c560c988ba4e/README.md#L36)：“使用原版 macOS 2.2.3.657 输入核心和词典” — fetched [2026-10-20](https://web.archive.org/web/20261020233414/https://github.com/panxuc/fcitx5-wetypex/blob/f25300dc8775f4e840148d596b56c560c988ba4e/README.md)
- <span id="ref-wetypex-warn"></span>panxuc — [fcitx5-wetypex README 第 17–24 行](https://github.com/panxuc/fcitx5-wetypex/blob/f25300dc8775f4e840148d596b56c560c988ba4e/README.md#L17-L24)：“可能包含微信输入法官方服务的遥测”“请于下载后 24 小时内删除” — fetched [2026-10-20](https://web.archive.org/web/20261020233414/https://github.com/panxuc/fcitx5-wetypex/blob/f25300dc8775f4e840148d596b56c560c988ba4e/README.md)
- <span id="ref-lima-424"></span>lima-vm/lima — [Issue #424: Is it possible to share clipboard with host?](https://github.com/lima-vm/lima/issues/424)，2021-11-18 开启，状态 open — fetched [2026-10-20](https://web.archive.org/web/20261020231420/https://github.com/lima-vm/lima/issues/424)
- <span id="ref-lima-5462"></span>lima-vm/lima — [PR #5462: vz: add audio.microphone to attach a capture stream](https://github.com/lima-vm/lima/pull/5462)，2026-09-08 合并 — fetched [2026-10-20](https://web.archive.org/web/20261020231530/https://github.com/lima-vm/lima/pull/5462)
- <span id="ref-lima-template"></span>lima-vm/lima — [templates/default.yaml 第 487–494 行](https://github.com/lima-vm/lima/blob/f08bbaf5331ebcce809cc23c076a4c1354bbf543/templates/default.yaml#L487-L494)：“Off by default: an input stream makes macOS ask for microphone permission on behalf of Lima” — fetched [2026-10-20](https://web.archive.org/web/20261020233443/https://github.com/lima-vm/lima/blob/f08bbaf5331ebcce809cc23c076a4c1354bbf543/templates/default.yaml)
- <span id="ref-lima-beta"></span>lima-vm/lima — [v2.3.0-beta.1 发布页](https://github.com/lima-vm/lima/releases/tag/v2.3.0-beta.1)，2026-10-03；作者用 GitHub compare 接口确认 PR #5462 的合并提交包含在 v2.3.0-beta.1 中、不在 v2.2.1 中 — fetched 2026-10-20
- <span id="ref-fcitx-globalconfig"></span>fcitx/fcitx5 — [src/lib/fcitx/globalconfig.cpp 第 41–46 行与第 87–91 行](https://github.com/fcitx/fcitx5/blob/0605ec5c26a183af5e61a8871f82eee6f1a7d740/src/lib/fcitx/globalconfig.cpp#L41-L91)：`isApple() ? Key("Control+Shift_L") : Key("Control+space")`；`AltTriggerKeys` 默认 `Key("Shift_L")` — fetched [2026-10-20](https://web.archive.org/web/20261020232321/https://github.com/fcitx/fcitx5/blob/0605ec5c26a183af5e61a8871f82eee6f1a7d740/src/lib/fcitx/globalconfig.cpp)
- <span id="ref-apple-shortcut"></span>Apple — [在 Mac 上使用键盘快捷键更改输入源](https://support.apple.com/guide/mac-help/use-keyboard-shortcuts-to-change-input-sources-mchlp1406/mac#:~:text=Press%20Control%2DSpace%20bar%20to%20select%20the%20last%20input%20source%20you%20used)：“Press Control-Space bar to select the last input source you used” — fetched [2026-10-20](https://web.archive.org/web/20261020231705/https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac)

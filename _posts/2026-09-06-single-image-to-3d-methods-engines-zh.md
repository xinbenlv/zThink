---
title: "一张图如何变成高保真 3D 模型：AI 方法、工具与引擎对比"
excerpt: "比较单图生成、多视图重建、法线约束、Gaussian Splatting 与 Blender 混合流程，厘清 LLM 和 3D 引擎的作用，以及速度、还原度和可编辑性的取舍。"
date: 2026-09-06
lang: zh
categories:
  - engineering
tags:
  - AI
  - LLM
  - image-to-3d
  - Blender
  - Unity
  - Unreal-Engine
  - Three.js
published: true
cover_image:
  src: /assets/blogposts/single-image-to-3d/cover.jpg
  x: 570
  y: 0
  size: 630
og_image: /assets/blogposts/single-image-to-3d/cover.jpg
---

最近，我想复刻《红色警戒 2》里的电厂和盟军建造厂。先生成高清参考，再让 AI 编程助手写 Blender Python，把建筑逐件搭出来，这条路让我觉得效率不高：既然已经有了图片，为什么还要把每根管子、每块屋顶重新描述一遍？

于是我去查现成应用、论文和制作案例。本文是截至 **2026 年 9 月 6 日的资料研究**，没有用这些服务对我的建筑图片做横向实验。下文的速度属于作者或厂商报告，配图也只是原创解释图。

我目前更愿意尝试的分工是：专用图生 3D 模型先出初稿，Blender 修正决定辨识度的构件，AI 编程助手负责调用工具和编写局部操作脚本。这是待检验的工程判断。它是否比从头脚本建模省事，要把重试和修模时间一起算进去。

## 先说清楚“高保真”要保住什么

对于同一张建筑图，我至少可以提出四种不同要求。

| 我想得到什么 | 应该怎样验收 |
| --- | --- |
| 从原来的角度看起来像 | 固定参考相机，比轮廓、比例、构件位置和颜色 |
| 可以围着建筑走一圈 | 检查侧面、背面、顶部及遮挡关系是否合理 |
| 可以拆掉烟囱、换材质、重新打光 | 实际选择和修改部件，检查几何与材质是否支持这些操作 |
| 尺寸和连接关系精确 | 用尺寸资料、更多实拍视角或原始 3D 数据验证 |

单张图片没有给出全部答案。屋顶后面有多深、被挡住的管道通向哪里，都可能有不止一种解释。[Hi3DGen 论文也把光照、阴影和纹理带来的 RGB 歧义列为几何恢复的困难](#ref-hi3dgen)。因此，“背面看着合理”和“背面恢复正确”应当分开；只有前一项能在缺少额外资料时直接评价。

<figure>
  <img src="/assets/blogposts/single-image-to-3d/ambiguity.jpg" alt="单图三维歧义示意：相近的工坊正面可以对应不同纵深的建筑，隐藏部分需要额外证据" width="1200" height="675" loading="lazy" />
  <figcaption>原创 AI 解释图：同一可见立面可以有不同的隐藏结构；图中建筑不是任何图生 3D 工具的测试结果。</figcaption>
</figure>

这里也需要澄清“LLM 从图生成模型”的说法。本文把看图分析、规划步骤、编写 Blender 脚本、调用生成接口的工作交给多模态 LLM；把输出三维形状的工作称为图生 3D。后者可以使用扩散、流匹配或专门的重建网络。例如 [TRELLIS.2 的三维表示与生成流程](#ref-trellis)，就不能仅因为受 AI 助手调用而统称为语言模型。Unity 官方的助手流程也明确区分了[准备参考图、预处理与调用 3D 生成](#ref-unity)。

## 从一张图出发，有六种走法

下面按制作流程分类。它们不是互斥的算法家族：法线可以加入多视图流程，Gaussian 也可能只是生成网格前的中间表示。

| 路线 | 中间过程与交付物 | 适合尝试的目标 | 必须接受的边界 |
| --- | --- | --- | --- |
| 直接生成完整网格 | 图片进入专用生成模型，再解码或提取网格；可附材质 | 尽快得到可导入的物体初稿 | 完整不等于忠实，隐藏结构仍靠推断 |
| 生成一致多视图，再重建 | 先合成不同方向的图，再恢复三维 | 希望利用成熟的多视图生成与重建流程 | 合成视图可能彼此矛盾，也可能一致地猜错 |
| 用法线约束几何 | 预测表面朝向，以此辅助生成或融合 | 想保留棱边、凹凸等形状线索 | 错误法线也会误导几何 |
| 自动初稿＋相机匹配＋局部修模 | 保留可用体块，人工或脚本修改关键部件 | 对构件数量、间距、连接有明确要求 | 修模成本需要实测，不能只看生成耗时 |
| 深度、投影贴图或单图 Gaussian | 有限深度的表面、投影外观或 splat 表示 | 固定镜头、轻微视差、附近视角展示 | 不自动得到完整、可拆件的常规网格 |
| 真实多照片摄影测量 | 从实际拍摄的不同视角求对应关系和几何 | 能接触到实物并补拍 | 输入已经超出单图任务，不能套到仅有概念图的情形 |

表中的前三条可以从 [TRELLIS.2](#ref-trellis)、[Wonder3D](#ref-wonder3d) 与 [Hi3DGen](#ref-hi3dgen) 看到具体实现；后面三条分别可参考 [KeenTools 的制作示例](#ref-keentools)、[Blender UV Project](#ref-uv-project)／[SHARP](#ref-sharp) 和 [RealityScan](#ref-realityscan)。适用目标是我的选型建议。

### 多视图和法线，分别补了什么

[Wonder3D 原版](#ref-wonder3d)联合生成不同方向的彩色图和法线图，再用法线融合重建网格。它公开说明了六视图、256×256 分辨率和正交相机假设。这些限制属于原版，不能不加版本地套到后续工作。对开发者更有用的启发是：重建前要让各方向的图共同描述同一个物体。

[InstantMesh](#ref-instantmesh)采用多视图扩散模型与稀疏视图重建模型组合；[Unique3D](#ref-unique3d)则结合多视图、法线、逐级提高分辨率和 ISOMER 网格重建。这些较早工作的价值在于说明流程如何组织，本文不把它们当成 2026 年的保真度冠军。

Hi3DGen 更强调从 RGB 到法线，再到几何的桥接。法线表达表面朝向，让模型有机会把颜色变化与形状线索分开处理。[作者的消融显示，法线桥接和训练中的法线正则有帮助；错误或过平滑的法线也会使结果变差](#ref-hi3dgen)。这说明值得检查中间法线，不能假设“多加一张法线图”必然改善任何生成器。

由同一张图合成的背面图，仍然是模型的预测。即使把它们交给一个叫“多视图重建”的模块，也没有增加独立的真实观测。若能补拍实物，才进入了另一种证据条件。

### 只想让画面有立体感，可以少做一些几何

对于只需轻微转动镜头的展示，完整物体网格未必是必需品。[Apple SHARP](#ref-sharp)从单张照片预测 3D Gaussian 表示，项目强调的是附近视角的高质量合成。它适合作为这类需求的候选，但 splat 文件本身不承诺烟囱、屋顶等语义部件的网格编辑能力。官方代码还区分了[支持 CPU／CUDA／MPS 的预测，与需要 CUDA 的轨迹视频渲染](#ref-sharp-code)。

如果采用深度驱动的表面或把原图投到粗几何上，我会预先限定镜头活动范围，并逐个检查新暴露的区域。[Blender 的 UV Project 可以按透视或正交相机投影](#ref-uv-project)，但投影只是赋予表面外观，不会凭空补出背面的构件。手册还提醒，低面数几何上的透视投影可能产生插值伪影。若还要重新打光，应另行检查材质，避免把原图里的阴影当成表面颜色。

反过来，也不要认为 Gaussian 路线都只能输出 splat。[DreamGaussian 的流程包括 Gaussian 优化、网格提取和 UV 空间纹理细化](#ref-dreamgaussian)。选型时应该查看最终交付物，而不只看方法名字。

## 现成工具与开放模型怎么选

下面列的是可继续比较的入口。产品参数表示接口或项目声明了什么能力，不能证明它能忠实还原某一张建筑图。

| 工具／模型 | 已核实的能力或入口 | 对这次建筑复刻的意义 |
| --- | --- | --- |
| Meshy 7 | Image to 3D API 可明确指定 `meshy-7`；纹理与 PBR 有单独开关。来源：[官方 API](#ref-meshy-api) | 适合列入云服务候选；记录确切模式，避免只写 `latest` |
| Tripo H3.1 | 文档列出 `v3.1-20260211`，支持单图／多视图，输出 Mesh＋PBR，最多 200 万面。来源：[官方模型页](#ref-tripo) | 可比较几何、贴图和拓扑选项，但高面数不能替代结构检查 |
| TRELLIS.2 | 4B 模型，以 O-Voxel 表示处理几何和 PBR 属性，提供代码、权重及 GLB 导出示例。来源：[项目 README](#ref-trellis) | 适合需要固定代码和权重的实验；先确认机器能运行 |
| Hunyuan3D 2.1 | 公开形状与 PBR 纹理生成流程；README 列出形状 10 GB、纹理 21 GB、组合 29 GB 的显存需求。来源：[2.1 项目](#ref-hunyuan) | 开放版本便于记录环境；不能把 2.1 的结果写成在线服务新版本的表现 |
| Hi3DGen | 重点是法线辅助的几何生成。来源：[作者论文](#ref-hi3dgen) | 可作为几何路线候选；不能凭名字把它与 Hitem3D 或 Hi3D 商业版本视为同一模型 |
| Rodin Gen-2.5 | 专用文档支持 1–5 图及 Raw／Quad 网格选项，要求显式发送 Gen-2.5 `tier`。来源：[官方文档](#ref-rodin) | 有可记录的输入与输出控制；省略 `tier` 会回退到 Gen-1／1.5，应避免误测版本 |
| Hitem3D 2.0 | 团队论文将生成多视图与原生 3D 纹理结合，处理覆盖、跨视图一致性和几何贴合。来源：[2026 年 4 月论文](#ref-hitem) | 可列入纹理流程研究；论文版本不能自动等同于网站当前服务，团队实验也不算独立评测 |

速度同样需要附上条件。[Tripo 模型页](#ref-tripo)标称无贴图约 40 秒、带贴图约 120 秒；页面没有给出供本文复现的统一硬件测试环境。[TRELLIS.2 README](#ref-trellis)报告在 H100 上，512³、1024³、1536³ 对应约 3、17、60 秒，官方代码目前仅在 Linux 上测试，要求 NVIDIA 显存至少 24 GB。这些是三维表示分辨率，不是贴图像素，也不是 Mac 上的通用耗时。README 声明模型和代码采用 MIT 许可，部分依赖另有条款。

若输入是一整个杂乱场景，还可以研究 [SAM 3D Objects](#ref-sam3d)：它从带掩码的对象生成形状、纹理、姿态与布局，重点包括遮挡和杂乱的自然图像。这里的“对象与布局”能力值得关注，却不能据此认定工业建筑的管道连接会恢复正确。

## 比榜单更有用的是：它到底怎么测

我会把证据分成三类来看。

**厂商自测可以揭示问题，但有选样和指标设计偏差。** [Meshy 在 2026 年 8 月 12 日发布的报告](#ref-meshy-benchmark)，用有真值的 3D 模型和已知相机制作输入，比较整体比例、空间分布和表面细节。分数是生成几何与参考几何的测量结果，不能读成“用户图片相似度百分比”。该页面称完整基准将另行公开；本文没有据此核实到可独立复跑的完整基准包。

报告中对失败的描述尤其值得建筑复刻者留意：[细结构会粘连，重复楼层的间距和窗格排列会漂移](#ref-meshy-benchmark)。据此，我会优先检查细管、镂空、重复构件的数量与连接，而不是先看贴图有多清晰。这是从失败类型作出的工程推断，不代表报告测试过我的建筑。

**原作者论文实验能说明方法贡献，但不等于跨年代总排名。** [Hi3DGen 的用户研究](#ref-hi3dgen)从 300×6 个结果中抽样，请 50 名普通用户与 10 名专业艺术家分别评价；对照包含 Hunyuan3D-2.0、Tripo-2.5 和 TRELLIS。不可见部分评的是合理性与风格一致性。作者也承认仍有细节与输入不一致，把重建级生成列为后续目标。因此，它支持法线路线值得研究，不能证明它胜过本文所有新版本。

**独立领域研究也有适用范围。** [2026 年 1 月发表于《Plant Methods》的植物研究](#ref-plants)比较六种方法，以 10 株 Bean 做定量评价，mint 和 kale 用于补充定性观察。在这个实验里，Hunyuan3D 2.0 的 Chamfer Distance 和 F-score 较好，Direct3D 的 LPIPS 较好。研究使用不同在线平台，部分方法的输入另做去背景处理；这不是统一硬件测速，也不足以外推建筑或 2026 年新模型的优劣。

这三类证据共同支持把几何与外观分开验收。面数增加，只表示有更多面；四边形输出，只描述拓扑形式。“能把这根管子单独选出来，改粗一点而不影响屋顶”仍然要实际操作才能确认。

<figure>
  <img src="/assets/blogposts/single-image-to-3d/inspection.jpg" alt="建筑资产验收的原创示意：带颜色外观、灰色几何、独立管道与重复通风构件分别接受检查" width="1200" height="675" loading="lazy" />
  <figcaption>原创 AI 解释图：先看结构，再看外观，并实际检查部件能否独立修改；不表示任何模型的实测输出。</figcaption>
</figure>

## Blender、Unity、Unreal、Three.js 分别做哪一段

这四个平台不宜与图生 3D 模型放在同一张保真度榜单上。我的分工建议如下，平台能力依据列在各行。

| 平台 | 可以承担的工作与学习入口 | 需要注意的限制 |
| --- | --- | --- |
| Blender | 整理初稿、调参考相机、修改关键构件、检查材质。[KeenTools 的 GeoTracker／Blender 示例](#ref-keentools)提供 ComfyUI、SAM 3D 模型生成相关项目；[UV Project 手册](#ref-uv-project)可学习相机投影 | 制作与跟踪示例不等于结构精度测试；投影也不负责完整几何恢复 |
| Unity | 官方在 2026 年 5 月的[AI beta 介绍](#ref-unity)中已提供编辑器内图生 3D，生成静态 mesh prefab；可直接放入场景做原型 | 官方定位包括简单、单部件道具和占位资产，不能据此期待复杂建筑精确复刻 |
| Unreal Engine | 用来导入资产、布置场景，并检查材质、碰撞和 LOD；[FBX 静态网格文档](#ref-unreal)给出制作与导入约定。若有实物多照片，可另学 [RealityScan 样例](#ref-realityscan)和 [CLI](#ref-realityscan-cli) | 网格可导入，不代表比例、部件或碰撞已经正确；RealityScan 是独立的摄影测量流程，不能当成 Unreal 的单图精准恢复按钮 |
| Three.js | 用 [GLTFLoader](#ref-gltf)加载网格资产，搭建可旋转、换光的网页检查器；社区也有 [splat 加载与渲染实现分享](#ref-three-splat) | 加载器负责读取三维数据；[MeshDepthMaterial](#ref-depth-material)按已有几何绘制深度，不能从普通照片估计深度 |

Blender 中我会先处理相机，再判断哪些形状需要修改。对于透视照片，[fSpy](#ref-fspy)利用消失点估计相机参数；它明确不适合正交渲染图。遇到等轴测风格的建筑参考，应该先判断投影类型，不能照搬照片教程。

还可以借鉴可微渲染的思路：渲染候选模型，比较输入，再调整形状和外观。不过，[NVIDIA 的 nvdiffrec](#ref-nvdiffrec)联合优化几何、材质和光照的工作以多视图观测为条件，项目示例使用 100 张图。借鉴这类优化时，必须保留其对输入观测的要求。

## 用一个小比较决定下一步

面对电厂、建造厂这样的目标，我会从一个云服务候选和一个能运行的开放模型开始，每种保留三次输出。这个数量只是控制首轮成本的建议，不能用来宣称统计显著性。验收标准在生成前写好，避免挑出一张最漂亮的结果就宣布胜出。

1. **固定输入。** 保存同一个图像文件及哈希，记录裁切、去背景和分辨率。若测试“先生成高清参考”，单独作为一组，并记录它改动了哪些可见结构。补画出的细节不能当原图证据。
2. **固定版本和条件。** 记录服务日期、模型标识、模式、参数、种子（若有）、硬件或云平台。服务强制的预处理和无法获知的条件也写下来。
3. **先评结构。** 所有候选换成统一灰色材质，在统一参考相机下检查轮廓、比例、构件位置；另存各自最佳相机匹配结果，避免把相机误差全算到几何上。对关键构件记录数量、间距、镂空是否保留、管道是否误连。
4. **再评外观与编辑。** 恢复贴图，换光、转动视角，再实际修改一个部件。背面只评合理性。高分辨率贴图、PBR 标签或四边形网格，都不能代替这些操作。
5. **记录完整耗时。** 从准备输入到可接受资产，分别记排队、生成、失败重试、导入、修模和导出；同时保留未通过的结果与原因。

没有原始 3D 真值时，我不会计算所谓“恢复准确率”或冒充有意义的 Chamfer Distance。后者需要可比较的三维参考；[植物研究的做法](#ref-plants)也是先准备真值，再对齐和测量。如果只能对照一张图，就报告可见结构检查结果和具体偏差；即使另算二维轮廓或图像指标，也只称为当前视角的图像一致性。

对建筑，我想验证的具体做法是保留生成初稿里已经像的主体，将窗格、栏杆、细管等关键构件改成可控制数量和间距的独立部件，让编程助手编写这些局部操作。若初稿连主体比例都不对，修模可能比重搭更慢；如果主要问题只剩重复构件，局部替换才有机会节省工作。

因此，下一次比较要回答的是一个具体问题：哪条流程能以较少的总耗时，保住这张图里我在意的结构？这个答案必须从同一输入的结果和修改记录里得出，不能从产品展示页代为推断。

## 参考资料

以下条目均于 2026-09-06 回读原文。每条正文引用先定位到本节，再指向原始来源与具体章节。带日期的本地摘录、证据类型和核验记录收在[资料归档](/assets/blogposts/single-image-to-3d/research/sources.html)；归档保留短摘录，不含完整网页快照。

- <span id="ref-hi3dgen" style="scroll-margin-top: 6rem"></span>[Hi3DGen: High-fidelity 3D Geometry Generation from Images via Normal Bridging](https://stable-x.github.io/Hi3DGen/hi3dgen_paper.pdf#page=7)。作者论文；定位：PDF pp. 1–3：RGB 歧义与法线桥接；pp. 6–8 §4.1、4.3、4.4、Limitations：对照版本、用户研究、消融与限制。原文短语：“reconstruction-level 3D generations”。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#hi3dgen)。
- <span id="ref-trellis" style="scroll-margin-top: 6rem"></span>[TRELLIS.2 README](https://github.com/microsoft/TRELLIS.2#-features)。作者项目文档；定位：Features §1–3；Installation / Prerequisites；Usage / Export to GLB；License。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#trellis)。
- <span id="ref-unity" style="scroll-margin-top: 6rem"></span>[Unity’s AI tools in beta: Create props with the 3D Object Generator](https://unity.com/blog/unity-ai-3d-object-generator)。厂商技术介绍；定位：2026-05-21；What the 3D Object Generator produces；Using the in-editor AI Assistant。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#unity)。
- <span id="ref-wonder3d" style="scroll-margin-top: 6rem"></span>[Wonder3D README（原版）](https://github.com/xxlong0/Wonder3D#common-questions)。作者项目文档；定位：开篇流程；Inference / Mesh Extraction；Common questions 条目2及 focal length。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#wonder3d)。
- <span id="ref-instantmesh" style="scroll-margin-top: 6rem"></span>[InstantMesh（arXiv v2）](https://arxiv.org/abs/2404.07191v2)。作者论文摘要；定位：2024-04-14 v2，Abstract。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#instantmesh)。
- <span id="ref-unique3d" style="scroll-margin-top: 6rem"></span>[Unique3D（arXiv v3）](https://arxiv.org/abs/2405.20343v3)。作者论文摘要；定位：2024-10-28 v3，Abstract。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#unique3d)。
- <span id="ref-keentools" style="scroll-margin-top: 6rem"></span>[KeenTools Examples](https://keentools.io/help/examples)。厂商制作案例目录；定位：GeoTracker / Blender。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#keentools)。
- <span id="ref-uv-project" style="scroll-margin-top: 6rem"></span>[Blender UV Project Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/modify/uv_project.html#options)。官方手册；定位：Options / Projectors；Known Limitations；通过浏览器成功读取；页面更新时间2026-09-06。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#uv-project)。
- <span id="ref-sharp" style="scroll-margin-top: 6rem"></span>[SHARP 项目页](https://apple.github.io/ml-sharp/)。作者项目；定位：Abstract 首段及展示说明。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#sharp)。
- <span id="ref-sharp-code" style="scroll-margin-top: 6rem"></span>[SHARP README](https://github.com/apple/ml-sharp#rendering-trajectories-cuda-gpu-only)。作者项目文档；定位：Using the CLI；Rendering trajectories (CUDA GPU only)。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#sharp-code)。
- <span id="ref-dreamgaussian" style="scroll-margin-top: 6rem"></span>[DreamGaussian（arXiv v2）](https://arxiv.org/abs/2309.16653v2)。作者论文摘要；定位：2024-03-29 v2，Abstract。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#dreamgaussian)。
- <span id="ref-meshy-api" style="scroll-margin-top: 6rem"></span>[Meshy Image to 3D API](https://docs.meshy.ai/en/api/image-to-3d)。官方API文档；定位：Create / ai_model、model_type、should_texture、enable_pbr。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#meshy-api)。
- <span id="ref-tripo" style="scroll-margin-top: 6rem"></span>[Tripo H3.1](https://developers.tripo3d.ai/en/models/v3-1)。官方模型文档；定位：顶部参数卡；Parameters；Snapshots。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#tripo)。
- <span id="ref-hunyuan" style="scroll-margin-top: 6rem"></span>[Hunyuan3D 2.1 README](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1#-models-zoo)。作者项目文档；定位：Models Zoo；Introduction。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#hunyuan)。
- <span id="ref-rodin" style="scroll-margin-top: 6rem"></span>[Rodin Gen-2.5](https://docs.hyper3d.ai/en/api-specification/rodin-gen2-5#tier)。官方API文档；定位：Input / Image-to-3D；Tier；mesh_mode。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#rodin)。
- <span id="ref-hitem" style="scroll-margin-top: 6rem"></span>[Hitem3D 2.0: Multi-View Guided Native 3D Texture Generation](https://arxiv.org/html/2604.09231v1#S3)。团队论文；定位：2026-04-10 v1；Abstract；§3.1–3.4。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#hitem)。
- <span id="ref-sam3d" style="scroll-margin-top: 6rem"></span>[SAM 3D Objects README](https://github.com/facebookresearch/sam-3d-objects#single-or-multi-object-3d-generation)。作者项目文档；定位：SAM 3D Objects 简介；Single or Multi-Object 3D Generation。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#sam3d)。
- <span id="ref-meshy-benchmark" style="scroll-margin-top: 6rem"></span>[Meshy 7: Pushing the frontier of 3D alignment](https://www.meshy.ai/blog/meshy-7-image-to-3d-geometry-alignment)。厂商自建基准；定位：2026-08-12；How to Measure 3D Geometry Alignment；Building the Benchmark；Where Quality Is Still Limited；Availability。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#meshy-benchmark)。
- <span id="ref-plants" style="scroll-margin-top: 6rem"></span>[Evaluation of one-image 3D reconstruction for plant model generation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888700/)。Zihe Gao、Zane K J Hartley、Andrew P French，诺丁汉大学；独立领域研究；定位：Plant Methods 22:18，2026-01-13；Methods / Dataset characteristics、Evaluated generative methods；Tables 1–2；Results 对CD尺度的说明。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#plants)。
- <span id="ref-unreal" style="scroll-margin-top: 6rem"></span>[Unreal Engine FBX Static Mesh Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine)。官方文档；定位：开篇支持列表；General Setup；Collision。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#unreal)。
- <span id="ref-realityscan" style="scroll-margin-top: 6rem"></span>[RealityScan 官网：功能、教程及样例](https://www.realityscan.com/)。官方产品与教程目录；定位：开篇；Get started in RealityScan；Sample datasets。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#realityscan)。
- <span id="ref-realityscan-cli" style="scroll-margin-top: 6rem"></span>[RealityScan Project and Image Commands](https://dev.epicgames.com/documentation/realityscan/project-and-image-commands)。官方文档；定位：Commands 表的 add、addFolder；Examples。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#realityscan-cli)。
- <span id="ref-gltf" style="scroll-margin-top: 6rem"></span>[Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html#load)。官方API文档；定位：开篇；Code Example；load。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#gltf)。
- <span id="ref-three-splat" style="scroll-margin-top: 6rem"></span>[Another Splat implementation for Threejs](https://discourse.threejs.org/t/another-splat-implementation-for-threejs/58883)。实现作者社区分享；定位：drcmda，2023-12-04，首帖及后续代码示例。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#three-splat)。
- <span id="ref-depth-material" style="scroll-margin-top: 6rem"></span>[Three.js MeshDepthMaterial](https://threejs.org/docs/pages/MeshDepthMaterial.html)。官方API文档；定位：开篇定义。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#depth-material)。
- <span id="ref-fspy" style="scroll-margin-top: 6rem"></span>[fSpy Basics](https://fspy.io/basics/)。官方教程；定位：Camera matching；Vanishing points；Limitations。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#fspy)。
- <span id="ref-nvdiffrec" style="scroll-margin-top: 6rem"></span>[Extracting Triangular 3D Models, Materials, and Lighting From Images](https://nvlabs.github.io/nvdiffrec/)。作者项目／CVPR 2022论文介绍；定位：Abstract；3D model reconstruction and intrinsic decomposition from images。fetched [2026-09-06](/assets/blogposts/single-image-to-3d/research/sources.html#nvdiffrec)。

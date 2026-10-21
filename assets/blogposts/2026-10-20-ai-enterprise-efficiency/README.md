# 2026-10-20 企业 AI 提效综述的配图

本目录存放《前沿实验室怎么说：用 AI 提升企业效率的方法与证据》一文的封面和四张插图。

```text
gen.py                                   生成五个 SVG 的脚本
cover.svg 01.svg 02.svg 03.svg 04.svg    gen.py 的输出
ai-efficiency-00-cover.jpg               封面和社交卡片，1200×630
ai-efficiency-01-four-workflows.jpg      编码、客服、文档、后台四类工作流，1200×675
ai-efficiency-02-six-steps.jpg           落地的六个步骤，1200×675
ai-efficiency-03-measurement-funnel.jpg  GDPval 表 2：90× 缩到 1.39×，1200×675
ai-efficiency-04-evidence-sieve.jpg      neo lab 说法经过证据规则筛选，1200×675
```

五张图都是手写 SVG，没有用图像生成模型。重新生成的步骤：

```bash
python3 gen.py
for n in cover 01 02 03 04; do rsvg-convert -w 2400 -f png -o $n.png $n.svg; done
```

PNG 缩到上表的尺寸，转成渐进式 JPG（质量 85）。中文字体用 macOS 自带的苹方（PingFang SC）。

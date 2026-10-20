# 2026-10-20 Linux 中文输入法文章的配图

本目录存放《2026 年 Linux 上打中文》一文的封面和三张插图。

```text
gen.py                                  生成四个 SVG 的脚本
cover.svg 01.svg 02.svg 03.svg          gen.py 的输出，可以直接改
linux-chinese-input-00-cover.jpg        封面和社交卡片，1200×630
linux-chinese-input-01-fcitx5-hub.jpg   键盘和麦克风都汇入 fcitx5，1200×675
linux-chinese-input-02-wetype-port.jpg  微信输入法引擎从 APK 取出、装进 fcitx5，1200×675
linux-chinese-input-03-vm-wall.jpg      Mac 和 Lima 虚拟机之间只有按键编号能通过，1200×675
```

四张图都是手写 SVG，没有用图像生成模型。重新生成的步骤：

```bash
python3 gen.py
for n in cover 01 02 03; do rsvg-convert -f png -o $n.png $n.svg; done
```

PNG 转成渐进式 JPG（质量 85）以后，按上表的文件名替换。中文字体用的是 macOS 自带的苹方（PingFang SC）。

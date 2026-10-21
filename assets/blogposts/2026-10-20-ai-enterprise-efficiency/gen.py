import os, math
S = os.path.dirname(os.path.abspath(__file__))
BG = "#faf9f5"; INK = "#141413"; G1 = "#e8e6dc"; G2 = "#b0aea5"; OR = "#d97757"; BL = "#6a9bcc"; GR = "#788c5d"; SUB = "#3d3d3a"
ZH = 'font-family="PingFang SC, Hiragino Sans GB, sans-serif"'
LA = 'font-family="Avenir Next, Helvetica, sans-serif"'

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'

def paper(w, h):
    s = f'<rect width="{w}" height="{h}" fill="{BG}"/>'
    for y in range(0, h, 30):
        s += f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{G1}" stroke-width="1"/>'
    for x in range(0, w, 30):
        s += f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{G1}" stroke-width="0.6" opacity="0.6"/>'
    return s

def text(x, y, t, fs=30, col=INK, anchor="middle", w="500", font=ZH):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{fs}" {font} font-weight="{w}" fill="{col}">{t}</text>'

def card(x, y, w, h, fill=BG, rx=14, sw=4):
    return (f'<rect x="{x+7}" y="{y+9}" width="{w}" height="{h}" rx="{rx}" fill="{G2}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"/>')

def lines(x, y, w, n, gap=22, col=G2, sw=6):
    return "".join(f'<line x1="{x}" y1="{y+i*gap}" x2="{x+w*(0.6 if i==n-1 else 1)}" y2="{y+i*gap}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>' for i in range(n))

def check(x, y, s=1, col=GR):
    return f'<path d="M {x} {y} l {14*s} {14*s} l {26*s} {-30*s}" fill="none" stroke="{col}" stroke-width="{7*s}" stroke-linecap="round" stroke-linejoin="round"/>'

def magnifier(cx, cy, r, col=INK):
    a = math.radians(45)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BG}" fill-opacity="0.55" stroke="{col}" stroke-width="7"/>'
            f'<line x1="{cx+r*math.cos(a)}" y1="{cy+r*math.sin(a)}" x2="{cx+r*1.9*math.cos(a)}" y2="{cy+r*1.9*math.sin(a)}" stroke="{col}" stroke-width="14" stroke-linecap="round"/>')

# ---------- cover 1200x630 ----------
b = paper(1200, 630)
b += f'<rect x="70" y="150" width="96" height="8" fill="{OR}"/>'
b += text(70, 240, "前沿实验室怎么说", 64, INK, "start", "700")
b += text(70, 310, "用 AI 提升企业效率的", 38, SUB, "start", "400")
b += text(70, 362, "方法与证据", 38, SUB, "start", "400")
b += text(70, 450, "Anthropic · OpenAI · xAI · Google · neo lab", 22, SUB, "start", "500", LA)
b += text(70, 540, "zzn.im", 24, G2, "start", "500", LA)
# document stack
for i, (dx, dy, col) in enumerate([(0, 0, BG), (-28, 26, BG), (-56, 52, BG)]):
    b += card(760 + dx, 120 + dy, 300, 380, col)
x0, y0 = 704, 172
b += lines(x0 + 40, y0 + 50, 210, 3)
b += f'<rect x="{x0+40}" y="{y0+130}" width="60" height="110" fill="{BL}"/>'
b += f'<rect x="{x0+115}" y="{y0+170}" width="60" height="70" fill="{OR}"/>'
b += f'<rect x="{x0+190}" y="{y0+200}" width="60" height="40" fill="{GR}"/>'
b += f'<line x1="{x0+30}" y1="{y0+242}" x2="{x0+265}" y2="{y0+242}" stroke="{INK}" stroke-width="4"/>'
b += lines(x0 + 40, y0 + 290, 210, 2)
b += magnifier(1040, 470, 70)
b += check(1010, 470, 1.2)
open(f"{S}/cover.svg", "w").write(svg(1200, 630, b))

# ---------- 01 four workflows 1200x675 ----------
b = paper(1200, 675)
b += f'<rect x="0" y="470" width="1200" height="205" fill="{G1}"/>'
b += f'<line x1="0" y1="470" x2="1200" y2="470" stroke="{INK}" stroke-width="4"/>'
cols = [("编码", BL), ("客服", OR), ("文档", GR), ("后台", BL)]
for i, (lab, col) in enumerate(cols):
    x = 70 + i * 280
    b += card(x, 150, 220, 290)
    b += f'<rect x="{x}" y="150" width="220" height="44" rx="14" fill="{col}" stroke="{INK}" stroke-width="4"/>'
    b += f'<rect x="{x}" y="176" width="220" height="18" fill="{col}"/><line x1="{x}" y1="194" x2="{x+220}" y2="194" stroke="{INK}" stroke-width="4"/>'
    b += text(x + 110, 182, lab, 28, BG, "middle", "700")
    if i == 0:
        b += text(x + 110, 320, "&lt;/&gt;", 86, INK, "middle", "700", LA)
        b += lines(x + 40, 370, 140, 2, 24)
    elif i == 1:
        b += f'<rect x="{x+40}" y="230" width="140" height="80" rx="8" fill="{BG}" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>'
        b += f'<circle cx="{x+40}" cy="270" r="12" fill="{G1}" stroke="{INK}" stroke-width="4"/><circle cx="{x+180}" cy="270" r="12" fill="{G1}" stroke="{INK}" stroke-width="4"/>'
        b += text(x + 110, 282, "#204", 30, INK, "middle", "700", LA)
        b += lines(x + 40, 350, 140, 3, 24)
    elif i == 2:
        b += f'<path d="M {x+60} 225 h 80 l 30 30 v 150 h -110 z" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
        b += f'<path d="M {x+140} 225 v 30 h 30" fill="none" stroke="{INK}" stroke-width="4"/>'
        b += lines(x + 78, 290, 74, 4, 26, G2, 5)
    else:
        for r in range(5):
            yy = 235 + r * 36
            b += f'<line x1="{x+35}" y1="{yy}" x2="{x+185}" y2="{yy}" stroke="{G2}" stroke-width="3"/>'
            b += text(x + 180, yy - 8, ["120", "85", "43", "310", "558"][r], 22, INK, "end", "600", LA)
        b += f'<line x1="{x+35}" y1="{235+5*36-10}" x2="{x+185}" y2="{235+5*36-10}" stroke="{INK}" stroke-width="4"/>'
# lamp + checklist
b += f'<path d="M 520 0 L 560 70" stroke="{INK}" stroke-width="5"/><path d="M 505 70 h 110 l -25 -40 h -60 z" fill="{OR}" stroke="{INK}" stroke-width="4"/>'
b += card(470, 500, 260, 150, BG)
for r in range(3):
    yy = 545 + r * 36
    b += f'<rect x="495" y="{yy-18}" width="26" height="26" rx="4" fill="{BG}" stroke="{INK}" stroke-width="3"/>' + check(499, yy - 6, 0.6) + lines(540, yy - 5, 160, 1, 0, G2, 6)
open(f"{S}/01.svg", "w").write(svg(1200, 675, b))

# ---------- 02 six steps 1200x675 ----------
b = paper(1200, 675)
labels = ["挑任务", "简单方案", "先评测", "接数据", "人审批", "共享"]
cols = [GR, BL, OR, BL, OR, GR]
pts = []
for i in range(6):
    x = 40 + i * 190; top = 560 - i * 75
    b += f'<rect x="{x}" y="{top}" width="190" height="{675-top}" fill="{G1}" stroke="{INK}" stroke-width="4"/>'
    b += text(x + 95, top + 52, str(i + 1), 34, INK, "middle", "700", LA)
    b += text(x + 95, top + 98, labels[i], 26, SUB, "middle", "600")
    cx, cy = x + 95, top - 60
    c = cols[i]
    if i == 0:  # sieve
        b += f'<path d="M {cx-55} {cy-20} h 110 l -20 50 h -70 z" fill="{c}" stroke="{INK}" stroke-width="4"/>'
        for k in range(4):
            b += f'<circle cx="{cx-27+k*18}" cy="{cy+5}" r="4" fill="{BG}"/>'
    elif i == 1:  # gear
        for k in range(8):
            a = k * math.pi / 4
            b += f'<rect x="{cx-9}" y="{cy-52}" width="18" height="22" fill="{c}" stroke="{INK}" stroke-width="3" transform="rotate({k*45} {cx} {cy})"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="36" fill="{c}" stroke="{INK}" stroke-width="4"/><circle cx="{cx}" cy="{cy}" r="12" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
    elif i == 2:  # ruler
        b += f'<rect x="{cx-70}" y="{cy-18}" width="140" height="36" fill="{c}" stroke="{INK}" stroke-width="4"/>'
        for k in range(9):
            hh = 16 if k % 2 == 0 else 9
            b += f'<line x1="{cx-60+k*15}" y1="{cy-18}" x2="{cx-60+k*15}" y2="{cy-18+hh}" stroke="{INK}" stroke-width="3"/>'
    elif i == 3:  # plug
        b += f'<rect x="{cx-30}" y="{cy-25}" width="60" height="50" rx="10" fill="{c}" stroke="{INK}" stroke-width="4"/>'
        b += f'<line x1="{cx-14}" y1="{cy-25}" x2="{cx-14}" y2="{cy-50}" stroke="{INK}" stroke-width="7"/><line x1="{cx+14}" y1="{cy-25}" x2="{cx+14}" y2="{cy-50}" stroke="{INK}" stroke-width="7"/>'
        b += f'<path d="M {cx} {cy+25} q 0 40 50 40" fill="none" stroke="{INK}" stroke-width="6"/>'
    elif i == 4:  # stamp
        b += f'<rect x="{cx-14}" y="{cy-55}" width="28" height="40" rx="10" fill="{INK}"/>'
        b += f'<rect x="{cx-45}" y="{cy-18}" width="90" height="26" rx="6" fill="{c}" stroke="{INK}" stroke-width="4"/>'
        b += f'<rect x="{cx-50}" y="{cy+8}" width="100" height="12" fill="{INK}"/>'
    else:  # handbook
        b += f'<path d="M {cx} {cy-30} q -40 -14 -70 0 v 70 q 30 -14 70 0 z" fill="{c}" stroke="{INK}" stroke-width="4"/>'
        b += f'<path d="M {cx} {cy-30} q 40 -14 70 0 v 70 q -30 -14 -70 0 z" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
        b += lines(cx + 12, cy - 10, 44, 3, 16, G2, 4)
open(f"{S}/02.svg", "w").write(svg(1200, 675, b))

# ---------- 03 measurement funnel 1200x675 ----------
b = paper(1200, 675)
b += f'<path d="M 330 90 H 870 L 660 420 V 600 H 540 V 420 Z" fill="{G1}" stroke="{INK}" stroke-width="5"/>'
b += f'<path d="M 330 90 H 870 L 812 181 H 388 Z" fill="{OR}" stroke="{INK}" stroke-width="5"/>'
b += text(600, 160, "90×", 64, BG, "middle", "700", LA)
b += text(600, 228, "只算推理", 28, SUB, "middle", "600")
b += f'<path d="M 470 300 H 730 L 700 345 H 500 Z" fill="{BL}" stroke="{INK}" stroke-width="4"/>'
b += text(600, 333, "审核 + 返工", 26, BG, "middle", "700")
b += f'<rect x="540" y="470" width="120" height="130" fill="{GR}" stroke="{INK}" stroke-width="5"/>'
b += text(600, 548, "1.39×", 32, BG, "middle", "700", LA)
b += text(600, 645, "GPT-5 · GDPval 表 2", 24, SUB, "middle", "500")
b += magnifier(185, 300, 75)
for k in range(4):
    b += card(940 + k * 10, 260 + k * 22, 170, 210, BG, 8, 3)
b += lines(965, 360, 110, 2, 24, G2, 6)
b += f'<line x1="985" y1="430" x2="1060" y2="505" stroke="{OR}" stroke-width="7" stroke-linecap="round"/><line x1="1060" y1="430" x2="985" y2="505" stroke="{OR}" stroke-width="7" stroke-linecap="round"/>'
open(f"{S}/03.svg", "w").write(svg(1200, 675, b))

# ---------- 04 evidence sieve 1200x675 ----------
b = paper(1200, 675)
b += f'<ellipse cx="600" cy="330" rx="430" ry="70" fill="{G2}"/>'
b += f'<ellipse cx="600" cy="320" rx="430" ry="70" fill="{G1}" stroke="{INK}" stroke-width="5"/>'
for r in range(-3, 4):
    b += f'<line x1="{600+r*110}" y1="{262 + abs(r)*6}" x2="{600+r*110}" y2="{378 - abs(r)*6}" stroke="{G2}" stroke-width="3"/>'
b += f'<line x1="190" y1="320" x2="1010" y2="320" stroke="{G2}" stroke-width="3"/>'
b += f'<rect x="1025" y="305" width="150" height="30" rx="15" fill="{OR}" stroke="{INK}" stroke-width="4"/>'
b += f'<rect x="25" y="305" width="150" height="30" rx="15" fill="{OR}" stroke="{INK}" stroke-width="4"/>'
slips = [(260, 120, "90%", -8), (390, 90, "80%", 6), (520, 135, "20%", -4), (660, 95, "10×", 8), (800, 150, "400K", -6), (960, 95, "30→100%", 5), (330, 210, "50%", 4), (760, 215, "预计", -5)]
for x, y, t, rot in slips:
    w = 120 if len(t) < 5 else 160
    b += f'<g transform="rotate({rot} {x} {y})"><rect x="{x-w/2+5}" y="{y-28+7}" width="{w}" height="56" fill="{G2}"/><rect x="{x-w/2}" y="{y-28}" width="{w}" height="56" fill="{BG}" stroke="{INK}" stroke-width="3"/>' + text(x, y + 12, t, 30, INK, "middle", "700", LA if t != "预计" else ZH) + '</g>'
for x, y, rot in [(470, 520, -5), (720, 560, 6)]:
    b += f'<g transform="rotate({rot} {x} {y})"><rect x="{x-80+6}" y="{y-34+8}" width="160" height="68" fill="{G2}"/><rect x="{x-80}" y="{y-34}" width="160" height="68" fill="{BG}" stroke="{INK}" stroke-width="3"/>' + lines(x - 60, y - 8, 80, 2, 20, G2, 6) + f'<circle cx="{x+48}" cy="{y}" r="24" fill="none" stroke="{OR}" stroke-width="5"/>' + check(x + 33, y, 0.55, OR) + '</g>'
b += f'<path d="M 600 400 v 60" stroke="{INK}" stroke-width="4" stroke-dasharray="8 8"/>'
open(f"{S}/04.svg", "w").write(svg(1200, 675, b))

# ---------- 05 parallel lanes + shift relay 1200x675 ----------
def clock(cx, cy, r, hh, mm):
    s = f'<circle cx="{cx+6}" cy="{cy+8}" r="{r}" fill="{G2}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{BG}" stroke="{INK}" stroke-width="5"/>'
    for k in range(12):
        a = math.radians(k * 30)
        s += f'<line x1="{cx+(r-12)*math.sin(a)}" y1="{cy-(r-12)*math.cos(a)}" x2="{cx+(r-4)*math.sin(a)}" y2="{cy-(r-4)*math.cos(a)}" stroke="{INK}" stroke-width="3"/>'
    ah, am = math.radians(hh * 30 + mm / 2), math.radians(mm * 6)
    s += f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.45*math.sin(ah)}" y2="{cy-r*0.45*math.cos(ah)}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    s += f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.7*math.sin(am)}" y2="{cy-r*0.7*math.cos(am)}" stroke="{OR}" stroke-width="5" stroke-linecap="round"/>'
    return s + f'<circle cx="{cx}" cy="{cy}" r="6" fill="{INK}"/>'

def notebook(x, y, rot):
    s = f'<g transform="rotate({rot} {x} {y})"><rect x="{x-62+6}" y="{y-44+8}" width="124" height="88" rx="6" fill="{G2}"/>'
    s += f'<rect x="{x-62}" y="{y-44}" width="124" height="88" rx="6" fill="{GR}" stroke="{INK}" stroke-width="4"/>'
    s += f'<rect x="{x-48}" y="{y-30}" width="96" height="40" rx="4" fill="{BG}" stroke="{INK}" stroke-width="3"/>'
    s += text(x, y - 1, "进度", 26, INK, "middle", "700") + lines(x - 40, y + 26, 80, 1, 0, BG, 5)
    return s + '</g>'

b = paper(1200, 675)
b += f'<rect x="0" y="372" width="1200" height="303" fill="{G1}"/><line x1="0" y1="372" x2="1200" y2="372" stroke="{INK}" stroke-width="4"/>'
# three parallel lanes forking from one line and merging back
lanes = [(110, BL), (195, OR), (280, GR)]
b += f'<line x1="0" y1="195" x2="150" y2="195" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
for y, col in lanes:
    b += f'<path d="M 150 195 C 220 195 220 {y} 290 {y} H 860 C 930 {y} 930 195 1000 195" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>'
    b += f'<path d="M 150 195 C 220 195 220 {y} 290 {y} H 860 C 930 {y} 930 195 1000 195" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round"/>'
for i, (y, col) in enumerate(lanes):
    x = 360 + i * 150
    b += card(x, y - 34, 150, 68, BG, 10, 4) + lines(x + 20, y - 8, 110, 2, 20, G2, 6)
    b += f'<rect x="{x+150-30}" y="{y-56}" width="40" height="34" rx="6" fill="{col}" stroke="{INK}" stroke-width="3"/><path d="M {x+150-20} {y-56} v -10 a 10 10 0 0 1 20 0 v 10" fill="none" stroke="{INK}" stroke-width="3"/>'
b += f'<line x1="1000" y1="195" x2="1200" y2="195" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
b += f'<circle cx="1060" cy="195" r="36" fill="{BG}" stroke="{INK}" stroke-width="5"/>' + check(1042, 196, 0.85)
# shift timeline with a progress notebook passed between clocks
b += f'<line x1="0" y1="600" x2="1200" y2="600" stroke="{INK}" stroke-width="4" stroke-dasharray="14 10"/>'
for cx, (hh, mm) in zip([150, 470, 790], [(9, 0), (3, 0), (11, 0)]):
    b += f'<line x1="{cx}" y1="545" x2="{cx}" y2="600" stroke="{INK}" stroke-width="4"/>' + clock(cx, 480, 62, hh, mm)
for x in [310, 630]:
    b += f'<path d="M {x-70} 440 Q {x} 400 {x+70} 440" fill="none" stroke="{INK}" stroke-width="4"/><path d="M {x+70} 440 l -18 -4 l 9 -14 z" fill="{INK}"/>'
    b += notebook(x, 515, -4 if x == 310 else 4)
# pause button: a human can stop the run
b += f'<circle cx="{1040+7}" cy="{490+9}" r="70" fill="{G2}"/><circle cx="1040" cy="490" r="70" fill="{OR}" stroke="{INK}" stroke-width="5"/>'
b += f'<rect x="1012" y="456" width="18" height="68" rx="4" fill="{BG}"/><rect x="1050" y="456" width="18" height="68" rx="4" fill="{BG}"/>'
open(f"{S}/05.svg", "w").write(svg(1200, 675, b))
print("ok")

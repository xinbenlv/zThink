import os
S=os.path.dirname(os.path.abspath(__file__))
BG="#faf9f5";INK="#141413";G1="#e8e6dc";G2="#b0aea5";OR="#d97757";BL="#6a9bcc";GR="#788c5d"
F="font-family=\"PingFang SC, Hiragino Sans GB, sans-serif\""
def paper(w,h):
    s=f'<rect width="{w}" height="{h}" fill="{BG}"/>'
    for y in range(0,h,30):
        s+=f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{G1}" stroke-width="1"/>'
    for x in range(0,w,30):
        s+=f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{G1}" stroke-width="0.6" opacity="0.6"/>'
    return s
def key(x,y,s,label,fill=BG,fs=None,col=INK):
    fs=fs or int(s*0.5)
    return (f'<rect x="{x+6}" y="{y+8}" width="{s}" height="{s}" rx="{s*0.14}" fill="{G2}"/>'
            f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*0.14}" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
            f'<text x="{x+s/2}" y="{y+s/2+fs*0.36}" text-anchor="middle" font-size="{fs}" {F} font-weight="600" fill="{col}">{label}</text>')
def mic(cx,cy,sc=1,col=OR):
    w=46*sc;h=92*sc
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{w/2}" fill="{col}" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M {cx-40*sc} {cy+5*sc} Q {cx-40*sc} {cy+70*sc} {cx} {cy+70*sc} Q {cx+40*sc} {cy+70*sc} {cx+40*sc} {cy+5*sc}" fill="none" stroke="{INK}" stroke-width="4"/>'
            f'<line x1="{cx}" y1="{cy+70*sc}" x2="{cx}" y2="{cy+100*sc}" stroke="{INK}" stroke-width="4"/>'
            f'<line x1="{cx-30*sc}" y1="{cy+100*sc}" x2="{cx+30*sc}" y2="{cy+100*sc}" stroke="{INK}" stroke-width="4"/>')
def hub(cx,cy,r,label="fcitx5"):
    return (f'<circle cx="{cx+6}" cy="{cy+8}" r="{r}" fill="{G2}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BL}" stroke="{INK}" stroke-width="4"/>'
            f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="{int(r*0.42)}" font-family="Avenir Next, sans-serif" font-weight="700" fill="{BG}">{label}</text>')
def window(x,y,w,h,text):
    return (f'<rect x="{x+6}" y="{y+8}" width="{w}" height="{h}" rx="12" fill="{G2}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
            f'<line x1="{x}" y1="{y+40}" x2="{x+w}" y2="{y+40}" stroke="{INK}" stroke-width="3"/>'
            + ''.join(f'<circle cx="{x+24+i*22}" cy="{y+20}" r="6" fill="{c}"/>' for i,c in enumerate([OR,G2,GR]))
            + f'<text x="{x+30}" y="{y+40+(h-40)/2+18}" font-size="52" {F} font-weight="600" fill="{INK}">{text}</text>'
            + f'<line x1="{x+30+len(text)*54}" y1="{y+40+(h-40)/2-26}" x2="{x+30+len(text)*54}" y2="{y+40+(h-40)/2+28}" stroke="{OR}" stroke-width="5"/>')
def arrow(x1,y1,x2,y2,col=INK,dash=""):
    import math
    a=math.atan2(y2-y1,x2-x1);L=18
    p1=(x2-L*math.cos(a-0.45),y2-L*math.sin(a-0.45));p2=(x2-L*math.cos(a+0.45),y2-L*math.sin(a+0.45))
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="5"{d}/>'
            f'<polygon points="{x2},{y2} {p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="{col}"/>')
def label(x,y,t,fs=30,col=INK,anchor="middle",w="500"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{fs}" {F} font-weight="{w}" fill="{col}">{t}</text>'
def svg(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'

# cover 1200x630
b=paper(1200,630)
b+=f'<rect x="0" y="0" width="560" height="630" fill="{BG}" opacity="0.92"/>'
b+=f'<rect x="60" y="150" width="90" height="8" fill="{OR}"/>'
b+=label(60,230,"2026 年",54,INK,"start","700")
b+=label(60,305,"Linux 上打中文",62,INK,"start","700")
b+=label(60,380,"输入法、语音输入",34,"#3d3d3a","start","400")
b+=label(60,428,"和微信输入法的现状",34,"#3d3d3a","start","400")
b+=label(60,520,"zzn.im",24,G2,"start","500")
b+=key(640,110,150,"中",BG,84)
b+=mic(1030,170,1.25)
b+=hub(885,430,95)
b+=arrow(735,275,835,355); b+=arrow(1030,310,945,365,OR)
b+=window(1000,470,240,150,"你好")
b+=arrow(975,470,1000,500)
open(f"{S}/cover.svg","w").write(svg(1200,630,b))

# 01 hub 1200x675
b=paper(1200,675)
b+=key(110,120,150,"拼",BG,80); b+=label(185,330,"拼音 / Rime",30)
b+=mic(185,450,1.0); b+=label(185,615,"语音插件",30)
b+=hub(560,337,120)
b+=arrow(275,200,450,290); b+=arrow(240,470,450,385,OR)
b+=window(760,200,380,260,"你好")
b+=arrow(685,337,750,337)
b+=label(950,520,"应用",30)
open(f"{S}/01.svg","w").write(svg(1200,675,b))

# 02 wetype port
b=paper(1200,675)
# parcel
b+=f'<rect x="96" y="238" width="270" height="220" rx="10" fill="{G2}"/>'
b+=f'<rect x="90" y="230" width="270" height="220" rx="10" fill="{G1}" stroke="{INK}" stroke-width="4"/>'
b+=f'<path d="M 90 230 L 140 170 L 410 170 L 360 230" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
b+=f'<line x1="120" y1="230" x2="120" y2="450" stroke="{OR}" stroke-width="6" stroke-dasharray="14 10"/>'
b+=label(225,365,"APK",56,INK,"middle","700")
# chip
b+=arrow(380,340,500,340)
b+=f'<rect x="526" y="248" width="180" height="180" rx="14" fill="{G2}"/>'
b+=f'<rect x="520" y="240" width="180" height="180" rx="14" fill="{GR}" stroke="{INK}" stroke-width="4"/>'
for i in range(5):
    y=262+i*34
    b+=f'<line x1="500" y1="{y}" x2="520" y2="{y}" stroke="{INK}" stroke-width="4"/><line x1="700" y1="{y}" x2="720" y2="{y}" stroke="{INK}" stroke-width="4"/>'
b+=label(610,345,"引擎",44,BG,"middle","700")
b+=arrow(735,330,840,330)
# slot
b+=f'<rect x="856" y="198" width="260" height="270" rx="16" fill="{G2}"/>'
b+=f'<rect x="850" y="190" width="260" height="270" rx="16" fill="{BL}" stroke="{INK}" stroke-width="4"/>'
b+=f'<rect x="895" y="260" width="170" height="140" rx="10" fill="{BG}" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>'
b+=f'<text x="980" y="238" text-anchor="middle" font-size="34" font-family="Avenir Next, sans-serif" font-weight="700" fill="{BG}">fcitx5</text>'
# tag
b+=f'<g transform="rotate(-8 980 540)"><rect x="880" y="505" width="200" height="70" rx="8" fill="{OR}" stroke="{INK}" stroke-width="4"/>'
b+=label(980,553,"非官方",36,BG,"middle","700")+'</g>'
b+=f'<line x1="980" y1="460" x2="975" y2="505" stroke="{INK}" stroke-width="3"/>'
open(f"{S}/02.svg","w").write(svg(1200,675,b))

# 03 vm wall
b=paper(1200,675)
# mac laptop
b+=f'<rect x="76" y="168" width="300" height="200" rx="12" fill="{G2}"/>'
b+=f'<rect x="70" y="160" width="300" height="200" rx="12" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
b+=f'<path d="M 40 360 L 400 360 L 380 392 L 60 392 Z" fill="{G1}" stroke="{INK}" stroke-width="4"/>'
b+=label(220,280,"Mac",44,INK,"middle","700")
# wall
for r in range(9):
    y=60+r*62; off=0 if r%2==0 else 40
    for c in range(-1,2):
        x=520+off+c*80
        if 500<=x+80 and x<=660:
            xx=max(x,520); ww=min(x+80,640)-xx
            if ww>0: b+=f'<rect x="{xx}" y="{y}" width="{ww}" height="58" fill="{OR}" stroke="{INK}" stroke-width="3"/>'
# linux window
b+=window(780,170,360,240,"")
b+=f'<text x="960" y="320" text-anchor="middle" font-size="44" font-family="Avenir Next, sans-serif" font-weight="700" fill="{INK}">Linux</text>'
# passing arrow
b+=arrow(390,470,760,470,GR)
b+=label(395,455,"按键编号",28,INK,"start")
# blocked
for i,(t,y) in enumerate([("汉字",110),("剪贴板",555),("麦克风",625)]):
    b+=arrow(300,y,505,y,INK,"12 8")
    b+=label(300,y-14,t,26,INK,"start")
    b+=f'<g stroke="{INK}" stroke-width="6"><line x1="470" y1="{y-18}" x2="500" y2="{y+12}"/><line x1="500" y1="{y-18}" x2="470" y2="{y+12}"/></g>'
open(f"{S}/03.svg","w").write(svg(1200,675,b))

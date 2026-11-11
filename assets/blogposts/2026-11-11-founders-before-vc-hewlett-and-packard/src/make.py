# Generates the cover and timeline SVGs for the Hewlett and Packard post (en and zh).
BG,INK,G1,G2,OR,BL,GR="#faf9f5","#141413","#e8e6dc","#b0aea5","#d97757","#6a9bcc","#788c5d"
SANS="Avenir Next, Helvetica Neue, PingFang SC, sans-serif"

def paper(w,h):
    lines="".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{G1}" stroke-width="1"/>' for y in range(30,h,30))
    return f'<rect width="{w}" height="{h}" fill="{BG}"/>{lines}'

def oscillator(x,y,s=1.0):
    # front panel of a 1939-style audio oscillator: big frequency dial, two knobs, price tag
    p=f'<g transform="translate({x},{y}) scale({s})">'
    p+=f'<rect x="0" y="0" width="420" height="250" rx="10" fill="#d9d5c7" stroke="{INK}" stroke-width="4"/>'
    p+=f'<circle cx="210" cy="115" r="78" fill="{BG}" stroke="{INK}" stroke-width="4"/>'
    for i in range(0,181,15):
        import math
        a=math.radians(200+i*0.78*1.8)
        x1,y1=210+70*math.cos(a),115+70*math.sin(a); x2,y2=210+58*math.cos(a),115+58*math.sin(a)
        p+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="3"/>'
    p+=f'<circle cx="210" cy="115" r="26" fill="{INK}"/><line x1="210" y1="115" x2="262" y2="70" stroke="{OR}" stroke-width="6" stroke-linecap="round"/>'
    for cx in (70,350):
        p+=f'<circle cx="{cx}" cy="125" r="28" fill="{INK}"/><circle cx="{cx}" cy="125" r="8" fill="{G2}"/>'
    p+=f'<rect x="150" y="210" width="120" height="22" rx="3" fill="{BG}" stroke="{INK}" stroke-width="2"/><text x="210" y="226" font-family="{SANS}" font-size="15" font-weight="700" text-anchor="middle" fill="{INK}">200A</text>'
    p+='</g>'
    return p

def tag(x,y,txt,fill,rot=-8,w=170):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><path d="M0 0 L{w} 0 L{w} 70 L0 70 L-30 35 Z" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="-12" cy="35" r="6" fill="{BG}" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{w/2-5}" y="47" font-family="{SANS}" font-size="34" font-weight="700" text-anchor="middle" fill="{INK}">{txt}</text></g>')

def cover(kicker,title_lines,comp_label,fn):
    W,H=1200,630
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{paper(W,H)}'
    s+=f'<rect x="0" y="0" width="{W}" height="{H}" fill="none"/>'
    s+=f'<rect x="70" y="120" width="70" height="6" fill="{OR}"/>'
    s+=f'<text x="70" y="100" font-family="{SANS}" font-size="26" font-weight="600" fill="{OR}">{kicker}</text>'
    y=185
    for ln in title_lines:
        s+=f'<text x="70" y="{y}" font-family="{SANS}" font-size="50" font-weight="700" fill="{INK}">{ln}</text>'; y+=64
    s+=oscillator(680,170,1.1)
    s+=tag(780,445,"$54.40",OR,-6)
    s+=f'<g transform="translate(900,60)"><rect x="0" y="0" width="190" height="56" rx="6" fill="{G1}" stroke="{G2}" stroke-width="2"/><text x="95" y="37" font-family="{SANS}" font-size="24" font-weight="600" text-anchor="middle" fill="#5e5d59" text-decoration="line-through">$200–$600</text></g>'
    s+=f'<text x="995" y="142" font-family="{SANS}" font-size="20" text-anchor="middle" fill="#5e5d59">{comp_label}</text>'
    s+=f'<text x="70" y="575" font-family="{SANS}" font-size="24" fill="#5e5d59">367 Addison Avenue · Palo Alto · 1938–1940</text>'
    s+='</svg>'
    open(fn,'w').write(s)

def timeline(items,fn):
    W,H=1200,675
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{paper(W,H)}'
    s+=f'<line x1="0" y1="340" x2="{W}" y2="340" stroke="{INK}" stroke-width="5"/>'
    n=len(items); xs=[150+i*(900/(n-1)) for i in range(n)]
    for i,(yr,l1,l2,col) in enumerate(items):
        x=xs[i]; up=(i%2==0); ly=140 if up else 430
        s+=f'<circle cx="{x}" cy="340" r="16" fill="{col}" stroke="{INK}" stroke-width="4"/>'
        s+=f'<line x1="{x}" y1="{324 if up else 356}" x2="{x}" y2="{ly+ (95 if up else 0)}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 6"/>'
        s+=f'<rect x="{x-115}" y="{ly}" width="230" height="95" rx="8" fill="{BG}" stroke="{INK}" stroke-width="3"/>'
        s+=f'<text x="{x}" y="{ly+34}" font-family="{SANS}" font-size="28" font-weight="700" text-anchor="middle" fill="{col if col!=G2 else INK}">{yr}</text>'
        s+=f'<text x="{x}" y="{ly+62}" font-family="{SANS}" font-size="19" text-anchor="middle" fill="{INK}">{l1}</text>'
        s+=f'<text x="{x}" y="{ly+85}" font-family="{SANS}" font-size="19" text-anchor="middle" fill="{INK}">{l2}</text>'
    s+='</svg>'; open(fn,'w').write(s)

cover("Founders Before Venture Capital",["Hewlett and Packard","started a company","before they chose","a product"],"competitors (HP's figure)","cover-en.svg")
cover("风投诞生之前的创业者",["休利特和帕卡德","先开公司，","后定产品"],"竞品价格（惠普的说法）","cover-zh.svg")
timeline([("1937","First meeting:","product postponed",G2),("1938","Garage and","$538 capital",BL),("1939","200A $54.40,","200B $71.50",OR),("1940","Move to","481 Page Mill Rd",GR),("1947","Incorporated","Aug 18",G2)],"timeline-en.svg")
timeline([("1937","首次会议：","产品暂且搁置",G2),("1938","车库起步，","本钱 538 美元",BL),("1939","200A 54.40 美元","200B 71.50 美元",OR),("1940","搬到","佩奇米尔路 481 号",GR),("1947","8 月 18 日","注册为公司",G2)],"timeline-zh.svg")

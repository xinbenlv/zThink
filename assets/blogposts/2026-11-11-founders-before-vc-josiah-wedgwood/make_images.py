import subprocess,sys,os
from PIL import Image
OUT=sys.argv[1]; S=sys.argv[2]
PAPER='#faf9f5';INK='#141413';G1='#e8e6dc';G2='#b0aea5';OR='#d97757';BL='#6a9bcc';GR='#788c5d'
def plate(cx,cy,r,fill=PAPER):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.28}" fill="{fill}" stroke="{INK}" stroke-width="2"/><ellipse cx="{cx}" cy="{cy}" rx="{r*0.6}" ry="{r*0.17}" fill="none" stroke="{G2}" stroke-width="1.5"/>'
def vase(x,y,h,col):
    w=h*0.45
    return (f'<path d="M{x-w*0.25},{y-h} L{x+w*0.25},{y-h} Q{x+w*0.15},{y-h*0.8} {x+w*0.5},{y-h*0.45} Q{x+w*0.6},{y-h*0.15} {x+w*0.2},{y} L{x-w*0.2},{y} Q{x-w*0.6},{y-h*0.15} {x-w*0.5},{y-h*0.45} Q{x-w*0.15},{y-h*0.8} {x-w*0.25},{y-h} Z" fill="{col}" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{x-w*0.42},{y-h*0.42} L{x+w*0.42},{y-h*0.42}" stroke="{PAPER}" stroke-width="2"/>')
def scene(x0,W,H):
    s=[]
    # wall panel and shelves
    s.append(f'<rect x="{x0}" y="0" width="{W-x0}" height="{H}" fill="{G1}"/>')
    s.append(f'<rect x="{x0}" y="{H*0.62}" width="{W-x0}" height="{H*0.38}" fill="#d9d5c7"/>')
    cols=[OR,BL,GR,'#c9a96b',OR,BL]
    for row,yy in enumerate([H*0.20,H*0.40]):
        s.append(f'<rect x="{x0+30}" y="{yy}" width="{W-x0-30}" height="8" fill="{INK}"/>')
        n=6; step=(W-x0-60)/n
        for i in range(n):
            s.append(vase(x0+60+step*i+step/2-10, yy, 70 if (i+row)%2 else 56, cols[(i+row*2)%6]))
    # two ranges of tables with services
    for t,ty in enumerate([H*0.70,H*0.88]):
        s.append(f'<rect x="{x0+10}" y="{ty}" width="{W-x0}" height="14" fill="{INK}"/>')
        s.append(f'<rect x="{x0+10}" y="{ty-4}" width="{W-x0}" height="6" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>')
        n=7; step=(W-x0-40)/n
        for i in range(n):
            s.append(plate(x0+40+step*i+step/2, ty-14, 30+ (i%2)*6))
    return ''.join(s)
def cover(lang):
    W,H=1200,630; x0=640
    if lang=='en':
        txt=(f'<text x="64" y="120" font-family="Avenir Next" font-weight="600" font-size="22" letter-spacing="3" fill="{OR}">FOUNDERS BEFORE VC</text>'
             f'<text font-family="Georgia" font-size="60" fill="{INK}"><tspan x="64" y="215">Josiah</tspan><tspan x="64" y="285">Wedgwood</tspan></text>'
             f'<rect x="64" y="318" width="90" height="5" fill="{OR}"/>'
             f'<text font-family="Georgia" font-size="27" fill="{INK}"><tspan x="64" y="380">A royal order, a showroom,</tspan><tspan x="64" y="418">a catalogue, and a partner</tspan><tspan x="64" y="456">in London, 1765–1774</tspan></text>')
    else:
        txt=(f'<text x="64" y="120" font-family="PingFang SC" font-weight="600" font-size="26" letter-spacing="4" fill="{OR}">风投诞生之前的创业者</text>'
             f'<text font-family="Songti SC" font-weight="bold" font-size="64" fill="{INK}"><tspan x="64" y="220">韦奇伍德</tspan></text>'
             f'<text x="64" y="268" font-family="Georgia" font-size="28" fill="{G2}">Josiah Wedgwood</text>'
             f'<rect x="64" y="300" width="90" height="5" fill="{OR}"/>'
             f'<text font-family="PingFang SC" font-size="28" fill="{INK}"><tspan x="64" y="365">王室订单、伦敦展厅、</tspan><tspan x="64" y="408">印刷目录和驻伦敦的合伙人</tspan><tspan x="64" y="451">1765–1774</tspan></text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{PAPER}"/>{scene(x0,W,H)}{txt}</svg>'
def names(lang):
    W,H=1200,675
    labels=['Cream-colour',"Queen's Ware",'Ivory']; cols=[G2,OR,BL]
    s=[f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',f'<rect y="{H*0.72}" width="{W}" height="{H*0.28}" fill="{G1}"/>']
    s.append(plate(600,470,230,PAPER)); s.append(f'<ellipse cx="600" cy="470" rx="80" ry="22" fill="#efe6c8" stroke="{INK}" stroke-width="2"/>')
    for i,(lab,c) in enumerate(zip(labels,cols)):
        x=170+i*430
        s.append(f'<line x1="{x}" y1="250" x2="600" y2="430" stroke="{c}" stroke-width="3" stroke-dasharray="8 6"/>')
        s.append(f'<rect x="{x-150}" y="150" width="300" height="100" rx="6" fill="{PAPER}" stroke="{c}" stroke-width="4"/>')
        s.append(f'<text x="{x}" y="212" text-anchor="middle" font-family="Georgia" font-size="38" fill="{INK}">{lab}</text>')
    cap='“alias … alias …”, Wedgwood to Bentley, 1767' if lang=='en' else '韦奇伍德致本特利，1767 年：同一种奶油色陶器的三个名字'
    font='Georgia' if lang=='en' else 'PingFang SC'
    s.append(f'<text x="600" y="90" text-anchor="middle" font-family="{font}" font-size="30" fill="{INK}">{cap}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(s)}</svg>'
def render(svg,name,size):
    p=os.path.join(S,name+'.svg'); open(p,'w').write(svg)
    png=os.path.join(S,name+'.png'); subprocess.run(['rsvg-convert','-w',str(size[0]*2),p,'-o',png],check=True)
    Image.open(png).convert('RGB').resize(size,Image.LANCZOS).save(os.path.join(OUT,name+'.jpg'),'JPEG',quality=84,optimize=True,progressive=True)
for lang in ['en','zh']:
    render(cover(lang),f'cover-{lang}',(1200,630))
    render(names(lang),f'names-{lang}',(1200,675))

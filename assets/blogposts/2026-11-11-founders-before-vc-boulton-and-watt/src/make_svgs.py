"""Write the hand-authored SVG sources for the Boulton and Watt article images.

Run: python3 make_svgs.py, then render each SVG with rsvg-convert and cjpeg
(see ../README.md).
"""
import pathlib

OUT = pathlib.Path(__file__).parent
BG, INK, GRAY, GRAY2 = "#faf9f5", "#141413", "#e8e6dc", "#b0aea5"
ORANGE, BLUE, GREEN = "#d97757", "#6a9bcc", "#788c5d"

PAPER = f"""
<defs>
  <pattern id="grain" width="6" height="6" patternUnits="userSpaceOnUse">
    <rect width="6" height="6" fill="{BG}"/>
  </pattern>
</defs>
"""


def coal(cx, cy, w, h, color):
    """A heap of coal lumps drawn as a stack of small polygons."""
    parts = []
    rows = int(h // 22)
    for r in range(rows):
        y = cy - r * 20
        width = w * (1 - r / (rows + 1))
        n = max(1, int(width // 26))
        for i in range(n):
            x = cx - width / 2 + i * (width / n) + 4
            parts.append(
                f'<polygon points="{x},{y} {x+10},{y-14} {x+22},{y-11} {x+24},{y} " '
                f'fill="{color}" stroke="{INK}" stroke-width="1.5"/>'
            )
    return "\n".join(parts)


def beam_engine(x, y, s=1.0):
    """A simplified beam engine: house, beam, cylinder, pump rod, and counter dial."""
    def t(v):
        return v * s
    return f"""
<g transform="translate({x},{y}) scale({s})" stroke="{INK}" stroke-width="3" fill="none" stroke-linejoin="round">
  <rect x="40" y="120" width="170" height="260" fill="{GRAY}"/>
  <polygon points="30,120 125,60 220,120" fill="{GRAY2}"/>
  <rect x="85" y="250" width="70" height="130" fill="{BG}"/>
  <line x1="-60" y1="150" x2="330" y2="110" stroke-width="10"/>
  <circle cx="135" cy="130" r="9" fill="{INK}"/>
  <line x1="-50" y1="150" x2="-50" y2="470" stroke-width="5"/>
  <line x1="320" y1="112" x2="320" y2="250" stroke-width="5"/>
  <rect x="290" y="250" width="60" height="110" fill="{BLUE}"/>
  <rect x="-90" y="470" width="80" height="40" fill="{BLUE}"/>
  <g transform="translate(175,180)">
    <rect x="-34" y="-34" width="68" height="68" rx="6" fill="{BG}"/>
    <circle cx="0" cy="0" r="24" fill="{BG}"/>
    <line x1="0" y1="0" x2="14" y2="-14" stroke="{ORANGE}" stroke-width="4"/>
    <circle cx="0" cy="0" r="3" fill="{INK}"/>
    <rect x="16" y="20" width="14" height="12" fill="{ORANGE}" stroke-width="2"/>
  </g>
</g>"""


def cover(lang):
    if lang == "en":
        title = ["Boulton and Watt", "Priced Steam Power", "by the Coal It Saved"]
        sub = "Founders Before VC · Soho, 1775"
        font = "Georgia, serif"
        lab_a, lab_b = "⅔ to the mine owner", "⅓ to Boulton &amp; Watt"
        size = 58
    else:
        title = ["博尔顿与瓦特：", "按省下的煤", "给蒸汽机定价"]
        sub = "风投诞生之前的创业者 · Soho，1775"
        font = "PingFang SC, Songti SC, sans-serif"
        lab_a, lab_b = "⅔ 归矿主", "⅓ 归博尔顿与瓦特"
        size = 60
    lines = "\n".join(
        f'<text x="70" y="{170 + i * (size + 18)}" font-family="{font}" font-size="{size}" '
        f'font-weight="700" fill="{INK}">{l}</text>'
        for i, l in enumerate(title)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
{PAPER}
<rect width="1200" height="630" fill="url(#grain)"/>
<rect x="0" y="560" width="1200" height="70" fill="{GRAY}"/>
<rect x="70" y="100" width="90" height="8" fill="{ORANGE}"/>
{lines}
<text x="70" y="440" font-family="{font}" font-size="28" fill="{INK}">{sub}</text>
{beam_engine(760, 70, 0.95)}
{coal(560, 558, 170, 90, INK)}
<g>
  <rect x="980" y="455" width="150" height="16" fill="{GREEN}" stroke="{INK}" stroke-width="2"/>
  <rect x="1130" y="455" width="75" height="16" fill="{ORANGE}" stroke="{INK}" stroke-width="2"/>
  <text x="980" y="505" font-family="{font}" font-size="22" fill="{INK}">{lab_a}</text>
  <text x="980" y="537" font-family="{font}" font-size="22" fill="{INK}">{lab_b}</text>
</g>
</svg>"""


def deal(lang):
    if lang == "en":
        font = "Georgia, serif"
        L = dict(old="Old engine: coal burned", new="Watt engine: coal burned",
                 saved="Coal saved", a="⅔ kept by the owner", b="⅓ to the patentees",
                 counter1="Stroke counter,", counter2="under lock and key")
    else:
        font = "PingFang SC, Songti SC, sans-serif"
        L = dict(old="旧机器烧的煤", new="瓦特机器烧的煤", saved="省下的煤",
                 a="⅔ 留给矿主", b="⅓ 付给专利权人", counter1="冲程计数器", counter2="上锁记录")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
{PAPER}
<rect width="1200" height="675" fill="url(#grain)"/>
<rect x="0" y="560" width="1200" height="115" fill="{GRAY}"/>
{coal(260, 555, 330, 300, INK)}
<text x="100" y="610" font-family="{font}" font-size="30" fill="{INK}">{L['old']}</text>
{coal(640, 555, 220, 130, INK)}
<text x="520" y="610" font-family="{font}" font-size="30" fill="{INK}">{L['new']}</text>
<g stroke="{INK}" stroke-width="2.5">
  <rect x="800" y="300" width="80" height="54" fill="{ORANGE}"/>
  <rect x="800" y="354" width="80" height="106" fill="{GREEN}"/>
</g>
<line x1="270" y1="300" x2="795" y2="300" stroke="{INK}" stroke-width="2" stroke-dasharray="8 8"/>
<line x1="650" y1="460" x2="795" y2="460" stroke="{INK}" stroke-width="2" stroke-dasharray="8 8"/>
<text x="800" y="285" font-family="{font}" font-size="28" font-weight="700" fill="{INK}">{L['saved']}</text>
<text x="895" y="335" font-family="{font}" font-size="24" fill="{INK}">{L['b']}</text>
<text x="895" y="415" font-family="{font}" font-size="24" fill="{INK}">{L['a']}</text>
<g transform="translate(940,150)" stroke="{INK}" stroke-width="3">
  <rect x="-50" y="-50" width="100" height="100" rx="8" fill="{BG}"/>
  <circle cx="0" cy="0" r="36" fill="{BG}"/>
  <line x1="0" y1="0" x2="22" y2="-20" stroke="{ORANGE}" stroke-width="5"/>
  <circle cx="0" cy="0" r="4" fill="{INK}"/>
  <rect x="26" y="30" width="20" height="16" fill="{ORANGE}" stroke-width="2"/>
</g>
<text x="1005" y="140" font-family="{font}" font-size="22" fill="{INK}">{L['counter1']}</text>
<text x="1005" y="170" font-family="{font}" font-size="22" fill="{INK}">{L['counter2']}</text>
</svg>"""


for lang in ("en", "zh"):
    suffix = "" if lang == "en" else "-zh"
    (OUT / f"boulton-watt-00-cover{suffix}.svg").write_text(cover(lang), encoding="utf-8")
    (OUT / f"boulton-watt-01-one-third{suffix}.svg").write_text(deal(lang), encoding="utf-8")

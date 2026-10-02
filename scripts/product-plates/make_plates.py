"""Instrument Plates: one product thumbnail per course and bundle.

Rendered at 2x and reduced for crisp lines. Output: plates/<id>.png, 1200x1200.
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = Path("/Users/alejandro.ingle/Library/Application Support/Claude/local-agent-mode-sessions/"
                "skills-plugin/013eb5bf-9ab3-450b-9208-2973dac78625/5f40fe1c-0d62-49ca-b349-877747edd5c1/"
                "skills/canvas-design/canvas-fonts")
OUT = Path(__file__).resolve().parents[2] / "img" / "products"
OUT.mkdir(exist_ok=True)

SIZE = 1200
SCALE = 2
S = SIZE * SCALE
MARGIN = 96 * SCALE
GROUND = (11, 16, 15)
LATTICE = (40, 52, 49)
MUTED = (78, 96, 91)
FAINT = (52, 66, 62)
TEXT = (214, 224, 220)
TEXT_DIM = (122, 140, 135)
LINE_W = 3 * SCALE

FAMILY = {
    "foundations": (126, 255, 92),
    "strategy": (77, 159, 255),
    "markets": (95, 224, 201),
    "systematic": (245, 200, 66),
}

# id, title, family, level, motif
COURSES = [
    ("foundations", "Stock Market Foundations", "foundations", "Beginner", "ladder"),
    ("technical", "Technical Analysis Complete", "foundations", "Beginner", "candles"),
    ("portfolio-build", "Building Your First Portfolio", "foundations", "Beginner", "rings"),
    ("psychology", "Trading Psychology & Process", "foundations", "Beginner", "damped"),
    ("momentum", "Momentum & Swing Trading", "strategy", "Intermediate", "steps"),
    ("options", "Options Trading Complete", "strategy", "Intermediate", "payoff"),
    ("day-trading", "Day Trading: Opening Range, VWAP & Scalps", "strategy", "Intermediate", "range"),
    ("options-income", "Options Income: Spreads, the Wheel, Condors", "strategy", "Intermediate", "condor"),
    ("mean-reversion", "Mean Reversion & Pairs", "strategy", "Intermediate", "bands"),
    ("event-trading", "Earnings & Event Trading", "strategy", "Intermediate", "spike"),
    ("tax-course", "Tax Strategy for Traders", "strategy", "Intermediate", "split"),
    ("futures", "Futures: ES/NQ, Margin & Contract Specs", "markets", "Intermediate", "curve"),
    ("forex", "Forex: Pairs, Sessions & Carry", "markets", "Intermediate", "sessions"),
    ("crypto", "Crypto: Spot, Perpetuals & Funding", "markets", "Intermediate", "funding"),
    ("order-flow", "Market Structure & Order Flow", "markets", "Intermediate", "depth"),
    ("risk-mgmt", "Portfolio Risk Management", "systematic", "Advanced", "tail"),
    ("algo", "Systematic Trading & Backtesting", "systematic", "Advanced", "folds"),
    ("institutional", "Institutional Portfolio Management", "systematic", "Advanced", "allocation"),
    ("macro-regimes", "Macro & Market Regimes", "systematic", "Advanced", "quadrants"),
    ("data-gate-stack", "Data, Backtests & the Gate Stack", "systematic", "Advanced", "gates"),
]
BUNDLES = [
    ("bundle-beginner", "Beginner Bundle", ["foundations", "technical", "portfolio-build", "psychology"], "4 courses"),
    ("bundle-intermediate", "Intermediate Bundle",
     ["foundations", "technical", "portfolio-build", "psychology", "momentum", "options", "day-trading",
      "options-income", "mean-reversion", "event-trading", "tax-course"], "11 courses"),
    ("bundle-markets", "Markets Bundle", ["futures", "forex", "crypto", "order-flow"], "4 courses"),
    ("bundle-expert", "Expert All-Access", [c[0] for c in COURSES], "All 20 courses"),
]


def font(name, px):
    return ImageFont.truetype(str(FONT_DIR / name), px * SCALE)


MONO = "GeistMono-Regular.ttf"
SERIF = "InstrumentSerif-Regular.ttf"


def polyline(draw, pts, fill, width=LINE_W):
    draw.line(pts, fill=fill, width=width, joint="curve")
    r = width / 2
    for x, y in (pts[0], pts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def dot(draw, x, y, r, fill):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def mapper(box, xmin, xmax, ymin, ymax):
    x0, y0, x1, y1 = box
    return lambda x, y: (x0 + (x - xmin) / (xmax - xmin) * (x1 - x0), y1 - (y - ymin) / (ymax - ymin) * (y1 - y0))


# ── Motifs: each draws inside box with the plate accent ────────────────────
def m_ladder(d, box, a):
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    rows = 14
    h = (y1 - y0) / rows
    for i in range(rows):
        depth = 0.25 + 0.7 * abs(math.sin(i * 1.7 + 0.4)) * (1 - abs(i - rows / 2 + 0.5) / rows)
        w = depth * (x1 - x0) / 2 * 0.92
        y = y0 + i * h + h * 0.22
        if i < rows / 2:
            d.rectangle([cx + 6 * SCALE, y, cx + 6 * SCALE + w, y + h * 0.56], fill=a if i == rows // 2 - 1 else FAINT)
        else:
            d.rectangle([cx - 6 * SCALE - w, y, cx - 6 * SCALE, y + h * 0.56], fill=a if i == rows // 2 else MUTED)
    d.line([cx, y0, cx, y1], fill=MUTED, width=SCALE)


def m_candles(d, box, a):
    x0, y0, x1, y1 = box
    rnd = random.Random(7)
    n = 22
    price = 50.0
    bars = []
    for i in range(n):
        o = price
        c = o + rnd.gauss(0.6 if i > 8 else -0.4, 2.2)
        hi = max(o, c) + abs(rnd.gauss(0, 1.3))
        lo = min(o, c) - abs(rnd.gauss(0, 1.3))
        bars.append((o, hi, lo, c))
        price = c
    ymin = min(b[2] for b in bars) - 2
    ymax = max(b[1] for b in bars) + 2
    f = mapper(box, -0.5, n - 0.5, ymin, ymax)
    bw = (x1 - x0) / n * 0.46
    for i, (o, hi, lo, c) in enumerate(bars):
        col = a if c >= o else MUTED
        x, yh = f(i, hi)
        _, yl = f(i, lo)
        d.line([x, yh, x, yl], fill=col, width=SCALE * 2)
        _, yo = f(i, o)
        _, yc = f(i, c)
        d.rectangle([x - bw / 2, min(yo, yc), x + bw / 2, max(yo, yc) + SCALE], fill=col)


def m_rings(d, box, a):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    weights = [0.32, 0.22, 0.18, 0.16, 0.12]
    for k, rad in enumerate([0.46, 0.36, 0.26]):
        r = rad * (y1 - y0)
        start = -90 + k * 14
        for j, w in enumerate(weights):
            sweep = w * 360 - 4
            col = a if (j == 0 and k == 0) else (MUTED if j % 2 == 0 else FAINT)
            d.arc([cx - r, cy - r, cx + r, cy + r], start, start + sweep, fill=col, width=LINE_W * (3 if k == 0 else 2))
            start += w * 360
    dot(d, cx, cy, 5 * SCALE, a)


def m_damped(d, box, a):
    f = mapper(box, 0, 10, -1.25, 1.25)
    pts = [f(t / 40, math.exp(-0.28 * t / 40) * math.sin(t / 40 * 3.1)) for t in range(401)]
    ghost = [f(t / 40, 0.9 * math.sin(t / 40 * 3.1)) for t in range(401)]
    polyline(d, ghost, FAINT, SCALE * 2)
    x0, _, x1, _ = box
    _, ym = f(0, 0)
    d.line([x0, ym, x1, ym], fill=MUTED, width=SCALE)
    polyline(d, pts, a)


def m_steps(d, box, a):
    rnd = random.Random(3)
    v, pts = 0.0, []
    for i in range(120):
        v += rnd.gauss(0.11, 0.5)
        pts.append((i, v))
    f = mapper(box, 0, 119, min(p[1] for p in pts) - 1, max(p[1] for p in pts) + 1)
    hi = -1e9
    highs = []
    for x, y in pts:
        hi = max(hi, y)
        highs.append(f(x, hi))
    polyline(d, highs, FAINT, SCALE * 2)
    polyline(d, [f(x, y) for x, y in pts], a)


def m_payoff(d, box, a):
    f = mapper(box, 0, 10, -2.2, 6.2)
    x0, _, x1, _ = box
    _, y0 = f(0, 0)
    d.line([x0, y0, x1, y0], fill=MUTED, width=SCALE)
    for k, strike in enumerate([5.6, 5.0, 4.4]):
        prem = 1.0 + 0.25 * k
        col = a if k == 1 else FAINT
        polyline(d, [f(0, -prem), f(strike, -prem), f(10, 10 - strike - prem)], col, LINE_W if k == 1 else SCALE * 2)
    sx, sy = f(5.0, -1.25)
    dot(d, sx, sy, 6 * SCALE, a)


def m_range(d, box, a):
    rnd = random.Random(11)
    v, pts = 0.0, []
    for i in range(160):
        v += rnd.gauss(0.02 if i > 30 else 0, 0.55)
        pts.append((i, v))
    early = [p[1] for p in pts[:30]]
    lo, hi = min(early), max(early)
    f = mapper(box, 0, 159, min(p[1] for p in pts) - 1, max(p[1] for p in pts) + 1)
    (bx0, by0), (bx1, by1) = f(0, hi), f(29, lo)
    d.rectangle([bx0, by0, bx1, by1], outline=MUTED, width=SCALE * 2)
    for y in (hi, lo):
        xa, ya = f(29, y)
        xb, _ = f(159, y)
        for xx in range(int(xa), int(xb), 14 * SCALE):
            d.line([xx, ya, min(xx + 6 * SCALE, xb), ya], fill=FAINT, width=SCALE * 2)
    vw, cum = [], 0.0
    for i, (_, y) in enumerate(pts):
        cum += y
        vw.append(f(i, cum / (i + 1)))
    polyline(d, vw, MUTED, SCALE * 2)
    polyline(d, [f(x, y) for x, y in pts], a)


def m_condor(d, box, a):
    f = mapper(box, 0, 10, -3.2, 2.6)
    x0, _, x1, _ = box
    _, yz = f(0, 0)
    d.line([x0, yz, x1, yz], fill=MUTED, width=SCALE)
    polyline(d, [f(0, -2.4), f(2.6, -2.4), f(3.8, 1.2), f(6.2, 1.2), f(7.4, -2.4), f(10, -2.4)], a)
    for xx in (3.8, 6.2):
        px, py = f(xx, 1.2)
        _, pz = f(xx, -2.9)
        for yy in range(int(py) + 10 * SCALE, int(pz), 12 * SCALE):
            d.line([px, yy, px, yy + 5 * SCALE], fill=FAINT, width=SCALE * 2)


def m_bands(d, box, a):
    rnd = random.Random(5)
    v, pts = 0.0, []
    for i in range(200):
        v = v * 0.93 + rnd.gauss(0, 0.42)
        pts.append((i, v))
    span = max(abs(y) for _, y in pts) * 1.08
    f = mapper(box, 0, 199, -span, span)
    x0, _, x1, _ = box
    for lvl, col in ((2, FAINT), (-2, FAINT), (0, MUTED)):
        _, y = f(0, lvl)
        d.line([x0, y, x1, y], fill=col, width=SCALE * 2)
    polyline(d, [f(x, y) for x, y in pts], a)
    for x, y in pts:
        if abs(y) >= 1.9:
            px, py = f(x, y)
            dot(d, px, py, 4 * SCALE, a)


def m_spike(d, box, a):
    rnd = random.Random(2)
    f = mapper(box, 0, 60, -0.5, 10)
    for i in range(60):
        h = abs(rnd.gauss(1.2, 0.5))
        if i == 41:
            h = 9.2
        elif i in (40, 42):
            h = 3.4
        x, y = f(i, h)
        _, yb = f(i, 0)
        col = a if i == 41 else (MUTED if i in (40, 42) else FAINT)
        d.rectangle([x - 4 * SCALE, y, x + 4 * SCALE, yb], fill=col)


def m_split(d, box, a):
    x0, y0, x1, y1 = box
    n = 12
    w = (x1 - x0) / n
    rnd = random.Random(9)
    for i in range(n):
        h = (0.35 + 0.6 * rnd.random()) * (y1 - y0)
        xa = x0 + i * w + w * 0.18
        xb = x0 + (i + 1) * w - w * 0.18
        d.rectangle([xa, y1 - h, xb, y1 - h * 0.4], fill=MUTED)
        d.rectangle([xa, y1 - h * 0.4 + 3 * SCALE, xb, y1], fill=a)


def m_curve(d, box, a):
    f = mapper(box, 0, 12, 60, 100)
    pts = [(m, 92 - 18 * (1 - math.exp(-m / 4.5))) for m in range(13)]
    ghost = [(m, 70 + 14 * (1 - math.exp(-m / 4.0))) for m in range(13)]
    polyline(d, [f(x, y) for x, y in ghost], FAINT, SCALE * 2)
    polyline(d, [f(x, y) for x, y in pts], a)
    for x, y in pts:
        px, py = f(x, y)
        dot(d, px, py, 6 * SCALE, a)
        gx, gy = f(x, ghost[x][1])
        dot(d, gx, gy, 4 * SCALE, MUTED)


def m_sessions(d, box, a):
    x0, y0, x1, y1 = box
    w = (x1 - x0) / 24
    for start, end, col in ((0, 9, FAINT), (7, 16, MUTED), (13, 22, MUTED)):
        d.rectangle([x0 + start * w, y1 - 14 * SCALE, x0 + end * w, y1 - 4 * SCALE], fill=col)
    f = mapper((x0, y0, x1, y1 - 40 * SCALE), 0, 240, -1.6, 1.6)
    p1 = [f(t, math.sin(t / 22) * 0.9 + 0.25 * math.sin(t / 5)) for t in range(241)]
    p2 = [f(t, math.sin(t / 22 + 2.6) * 0.7 + 0.2 * math.sin(t / 7)) for t in range(241)]
    polyline(d, p2, MUTED, SCALE * 2)
    polyline(d, p1, a)


def m_funding(d, box, a):
    x0, y0, x1, y1 = box
    rnd = random.Random(4)
    n = 30
    w = (x1 - x0) / n
    _, ym = mapper(box, 0, 1, -1, 1)(0, 0)
    d.line([x0, ym, x1, ym], fill=MUTED, width=SCALE)
    for i in range(n):
        v = math.sin(i / 4.2) * 0.75 + rnd.gauss(0, 0.12)
        h = v * (y1 - y0) / 2 * 0.9
        col = a if v > 0 else MUTED
        xa = x0 + i * w + w * 0.2
        d.rectangle([xa, min(ym, ym - h), x0 + (i + 1) * w - w * 0.2, max(ym, ym - h)], fill=col)


def m_depth(d, box, a):
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    levels = 10
    w = (x1 - x0) / 2 / levels
    for i in range(levels):
        h = (0.18 + 0.075 * i) * (y1 - y0)
        gap = w * 0.14
        d.rectangle([cx - (i + 1) * w + gap, y1 - h, cx - i * w - gap, y1], fill=MUTED)
        hh = (0.14 + 0.08 * i) * (y1 - y0)
        d.rectangle([cx + i * w + gap, y1 - hh, cx + (i + 1) * w - gap, y1], fill=a if i == 0 else FAINT)
    d.line([cx, y0, cx, y1], fill=MUTED, width=SCALE)


def m_tail(d, box, a):
    x0, y0, x1, y1 = box
    n = 36
    w = (x1 - x0) / n
    for i in range(n):
        z = (i - n * 0.58) / 5.2
        h = math.exp(-z * z / 2) + (0.06 if i < 6 else 0)
        col = a if i < 7 else MUTED
        gap = w * 0.14
        d.rectangle([x0 + i * w + gap, y1 - h * (y1 - y0) * 0.9, x0 + (i + 1) * w - gap, y1], fill=col)
    vx = x0 + 7 * w
    for yy in range(int(y0), int(y1), 14 * SCALE):
        d.line([vx, yy, vx, yy + 6 * SCALE], fill=TEXT_DIM, width=SCALE * 2)


def m_folds(d, box, a):
    x0, y0, x1, y1 = box
    rows = 5
    h = (y1 - y0) / rows
    for r in range(rows):
        train_end = 0.35 + 0.12 * r
        y = y0 + r * h + h * 0.3
        d.rectangle([x0, y, x0 + train_end * (x1 - x0) - 4 * SCALE, y + h * 0.4], fill=FAINT)
        d.rectangle([x0 + train_end * (x1 - x0), y, x0 + (train_end + 0.12) * (x1 - x0), y + h * 0.4], fill=a)


def m_allocation(d, box, a):
    x0, y0, x1, y1 = box
    n = 10
    cell = (x1 - x0) / n
    rows = int((y1 - y0) // cell)
    counts = [40, 15, 5, 5, 25, 5, 5]
    cols = [a, MUTED, FAINT, MUTED, TEXT_DIM, FAINT, MUTED]
    seq = [c for c, k in zip(cols, counts) for _ in range(k)]
    oy = y0 + ((y1 - y0) - rows * cell) / 2
    for idx in range(min(100, rows * n)):
        r, c = divmod(idx, n)
        col = seq[idx] if idx < len(seq) else FAINT
        d.rectangle([x0 + c * cell + 3 * SCALE, oy + r * cell + 3 * SCALE,
                     x0 + (c + 1) * cell - 3 * SCALE, oy + (r + 1) * cell - 3 * SCALE], fill=col)


def m_quadrants(d, box, a):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    g = 6 * SCALE
    quads = [(x0, y0, cx - g, cy - g, FAINT), (cx + g, y0, x1, cy - g, a),
             (x0, cy + g, cx - g, y1, MUTED), (cx + g, cy + g, x1, y1, FAINT)]
    for qx0, qy0, qx1, qy1, col in quads:
        d.rectangle([qx0, qy0, qx1, qy1], outline=col, width=SCALE * 2)
        step = 18 * SCALE
        for yy in range(int(qy0) + step, int(qy1), step):
            for xx in range(int(qx0) + step, int(qx1), step):
                dot(d, xx, yy, 2 * SCALE, col)


def m_gates(d, box, a):
    x0, y0, x1, y1 = box
    n = 7
    h = (y1 - y0) / n
    cx = (x0 + x1) / 2
    for i in range(n):
        w = (x1 - x0) * (0.96 - i * 0.12)
        y = y0 + i * h + h * 0.24
        col = a if i == n - 1 else (MUTED if i % 2 == 0 else FAINT)
        d.rectangle([cx - w / 2, y, cx + w / 2, y + h * 0.5], fill=col)


MOTIFS = {k[2:]: v for k, v in globals().items() if k.startswith("m_")}


def lattice(d):
    pitch = 24 * SCALE
    for y in range(MARGIN, S - MARGIN + 1, pitch):
        for x in range(MARGIN, S - MARGIN + 1, pitch):
            dot(d, x, y, 1.4 * SCALE, LATTICE)


def wrap(text, fnt, width, d):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def frame(d, plate_no, accent, title, meta):
    mono = font(MONO, 17)
    d.text((MARGIN, MARGIN - 34 * SCALE), "PHANTOM TRADERS · EDUCATION", font=mono, fill=TEXT_DIM)
    label = f"PLATE {plate_no}"
    d.text((S - MARGIN - d.textlength(label, font=mono), MARGIN - 34 * SCALE), label, font=mono, fill=TEXT_DIM)
    d.line([MARGIN, MARGIN - 8 * SCALE, S - MARGIN, MARGIN - 8 * SCALE], fill=FAINT, width=SCALE)
    serif = font(SERIF, 66)
    lines = wrap(title, serif, S - 2 * MARGIN, d)
    if len(lines) > 2:
        serif = font(SERIF, 56)
        lines = wrap(title, serif, S - 2 * MARGIN, d)
    line_h = serif.size * 1.08
    base = S - MARGIN - 40 * SCALE
    top = base - line_h * len(lines) - 18 * SCALE
    d.line([MARGIN, top - 22 * SCALE, MARGIN + 56 * SCALE, top - 22 * SCALE], fill=accent, width=SCALE * 3)
    for i, ln in enumerate(lines):
        d.text((MARGIN, top + i * line_h), ln, font=serif, fill=TEXT)
    d.text((MARGIN, base + 8 * SCALE), meta.upper(), font=mono, fill=TEXT_DIM)
    return top - 60 * SCALE


def plate(file_id, plate_no, accent, title, meta, draw_fn):
    img = Image.new("RGB", (S, S), GROUND)
    d = ImageDraw.Draw(img)
    draw_rectangle = d.rectangle

    def rectangle_or_skip(xy, **kwargs):
        # Fixed gaps can exceed a bar's width inside the small bundle tiles.
        x0, y0, x1, y1 = xy
        if x1 >= x0 and y1 >= y0:
            draw_rectangle([x0, y0, x1, y1], **kwargs)

    d.rectangle = rectangle_or_skip
    lattice(d)
    figure_bottom = frame(d, plate_no, accent, title, meta)
    box = (MARGIN + 24 * SCALE, MARGIN + 60 * SCALE, S - MARGIN - 24 * SCALE, figure_bottom)
    draw_fn(d, box, accent)
    img.resize((SIZE, SIZE), Image.LANCZOS).save(OUT / f"{file_id}.png", optimize=True)


def bundle_fn(members):
    def draw(d, box, accent):
        x0, y0, x1, y1 = box
        n = len(members)
        cols = 2 if n == 4 else (4 if n <= 12 else 5)
        rows = math.ceil(n / cols)
        gap = 18 * SCALE
        cw = (x1 - x0 - gap * (cols - 1)) / cols
        ch = (y1 - y0 - gap * (rows - 1)) / rows
        side = min(cw, ch)
        ox = x0 + ((x1 - x0) - (side * cols + gap * (cols - 1))) / 2
        oy = y0 + ((y1 - y0) - (side * rows + gap * (rows - 1))) / 2
        for k, cid in enumerate(members):
            course = next(c for c in COURSES if c[0] == cid)
            r, c = divmod(k, cols)
            bx0 = ox + c * (side + gap)
            by0 = oy + r * (side + gap)
            d.rectangle([bx0, by0, bx0 + side, by0 + side], outline=FAINT, width=SCALE)
            pad = side * 0.16
            MOTIFS[course[4]](d, (bx0 + pad, by0 + pad, bx0 + side - pad, by0 + side - pad), FAMILY[course[2]])
    return draw


for i, (cid, title, family, level, motif) in enumerate(COURSES, start=1):
    plate(cid, f"{i:02d} / 20", FAMILY[family], title, f"{level} · 12 lessons + capstone", MOTIFS[motif])
for j, (bid, title, members, meta) in enumerate(BUNDLES):
    accent = {"bundle-beginner": FAMILY["foundations"], "bundle-intermediate": FAMILY["strategy"],
              "bundle-markets": FAMILY["markets"], "bundle-expert": FAMILY["systematic"]}[bid]
    plate(bid, f"B{j + 1} / 4", accent, title, f"Bundle · {meta}", bundle_fn(members))
print("wrote", len(list(OUT.glob("*.png"))), "plates to", OUT)

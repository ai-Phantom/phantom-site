"""svgfig — dependency-free SVG charts for course lessons.

Every lesson figure on the site is generated from data by a small script in
content/courses/<id>/figures/make_figures.py that imports this module, so a
chart can be regenerated when its numbers change and reviewed as code.

Charts use the site's dark palette with a transparent background, fixed
760x400 viewBox (scaled by CSS), and plain SVG text. No external fonts, no
scripts, nothing fetched at view time.

    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))  # repo-root scripts/
    from svgfig import line_chart, bar_chart, candle_chart, payoff_chart, flow_diagram
    line_chart("spy-sma.svg", {"SPY close": pts, "50-day SMA": sma}, title="SPY, 2024",
               y_label="$", x_labels=dates)
"""
from __future__ import annotations
import math
from html import escape
from pathlib import Path

W, H = 760, 400
PAD_L, PAD_R, PAD_T, PAD_B = 64, 20, 44, 52
COLORS = ["#7eff5c", "#4d9fff", "#f5c842", "#ff4d6a", "#a78bfa", "#ff9f43"]
TEXT, MUTED, GRID, AXIS = "#c9d1cc", "#8a948e", "#2a3138", "#3a434b"
FONT = "font-family='ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif'"


def _nice_ticks(lo, hi, n=5):
    if hi == lo:
        hi = lo + 1
    raw = (hi - lo) / max(n - 1, 1)
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        step = m * mag
        if raw <= step:
            break
    start = math.floor(lo / step) * step
    ticks = []
    t = start
    while t <= hi + step * 0.5:
        ticks.append(round(t, 10))
        t += step
    return ticks


def _fmt(v):
    if abs(v) >= 1000:
        return f"{v:,.0f}"
    if abs(v) >= 100:
        return f"{v:.0f}"
    if abs(v) >= 10:
        return f"{v:.1f}".rstrip("0").rstrip(".")
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _svg(parts, title=None):
    head = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' {FONT} font-size='12'>"]
    if title:
        head.append(f"<title>{escape(title)}</title>")
        head.append(f"<text x='{PAD_L}' y='24' fill='{TEXT}' font-size='15' font-weight='700'>{escape(title)}</text>")
    return "\n".join(head + parts + ["</svg>\n"])


def _axes(lo, hi, y_label=None, y_fmt=_fmt, x_labels=None, n_x=None, pad=0.08):
    """Return (parts, y_of) for a left axis spanning lo..hi with gridlines.
    `pad` adds headroom above and below the data so a value that lands exactly
    on a tick still has room for its label."""
    plot_h = H - PAD_T - PAD_B
    if pad and hi > lo:
        span = hi - lo
        lo_p, hi_p = lo - span * pad, hi + span * pad
        # Never pad a non-negative range below zero (RSI, prices, counts).
        lo = lo_p if lo < 0 else max(lo_p, 0)
        hi = hi_p
    elif pad:
        lo, hi = lo - abs(lo) * pad - 1, hi + abs(hi) * pad + 1
    ticks = _nice_ticks(lo, hi)
    lo, hi = min(lo, ticks[0]), max(hi, ticks[-1])
    parts = []

    def y_of(v):
        return PAD_T + plot_h - (v - lo) / (hi - lo) * plot_h

    for t in ticks:
        y = y_of(t)
        parts.append(f"<line x1='{PAD_L}' y1='{y:.1f}' x2='{W - PAD_R}' y2='{y:.1f}' stroke='{GRID}' stroke-width='1'/>")
        parts.append(f"<text x='{PAD_L - 8}' y='{y + 4:.1f}' fill='{MUTED}' text-anchor='end'>{escape(y_fmt(t))}</text>")
    parts.append(f"<line x1='{PAD_L}' y1='{PAD_T}' x2='{PAD_L}' y2='{H - PAD_B}' stroke='{AXIS}'/>")
    parts.append(f"<line x1='{PAD_L}' y1='{H - PAD_B}' x2='{W - PAD_R}' y2='{H - PAD_B}' stroke='{AXIS}'/>")
    if y_label:
        parts.append(f"<text x='{PAD_L}' y='{PAD_T - 10}' fill='{MUTED}' font-size='11'>{escape(y_label)}</text>")
    if x_labels and n_x:
        plot_w = W - PAD_L - PAD_R
        step = max(1, math.ceil(n_x / 8))
        for i in range(0, n_x, step):
            x = PAD_L + (i / max(n_x - 1, 1)) * plot_w
            parts.append(f"<text x='{x:.1f}' y='{H - PAD_B + 18}' fill='{MUTED}' text-anchor='middle'>{escape(str(x_labels[i]))}</text>")
    return parts, y_of, (lo, hi)


def _legend(names, y=None):
    parts = []
    x = PAD_L
    y = y or (H - 12)
    for i, name in enumerate(names):
        c = COLORS[i % len(COLORS)]
        parts.append(f"<rect x='{x}' y='{y - 9}' width='12' height='12' fill='{c}' rx='2'/>")
        parts.append(f"<text x='{x + 17}' y='{y + 1}' fill='{TEXT}'>{escape(name)}</text>")
        x += 17 + 7 * len(name) + 24
    return parts


def line_chart(path, series: dict, title=None, y_label=None, x_labels=None, y_fmt=_fmt, annotations=None, hlines=None, pad=0.08):
    """series: {name: [y0, y1, ...]} (all same length) — x is the index.
    annotations: [(index, text)]; hlines: [(y, label)]."""
    ys = [v for vals in series.values() for v in vals if v is not None]
    lo, hi = min(ys), max(ys)
    if hlines:
        lo, hi = min([lo] + [h for h, _ in hlines]), max([hi] + [h for h, _ in hlines])
    n = max(len(v) for v in series.values())
    parts, y_of, _ = _axes(lo, hi, y_label, y_fmt, x_labels, n, pad=pad)
    plot_w = W - PAD_L - PAD_R

    def x_of(i):
        return PAD_L + (i / max(n - 1, 1)) * plot_w

    for h, label in (hlines or []):
        y = y_of(h)
        parts.append(f"<line x1='{PAD_L}' y1='{y:.1f}' x2='{W - PAD_R}' y2='{y:.1f}' stroke='{MUTED}' stroke-dasharray='4 4'/>")
        parts.append(f"<text x='{W - PAD_R - 4}' y='{y - 5:.1f}' fill='{MUTED}' text-anchor='end' font-size='11'>{escape(label)}</text>")
    for i, (name, vals) in enumerate(series.items()):
        c = COLORS[i % len(COLORS)]
        pts = " ".join(f"{x_of(j):.1f},{y_of(v):.1f}" for j, v in enumerate(vals) if v is not None)
        parts.append(f"<polyline points='{pts}' fill='none' stroke='{c}' stroke-width='2' stroke-linejoin='round'/>")
    for idx, text in (annotations or []):
        name, vals = next(iter(series.items()))
        v = vals[idx]
        x, y = x_of(idx), y_of(v)
        parts.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='4' fill='{COLORS[3]}'/>")
        anchor = "end" if x > W * 0.6 else "start"
        parts.append(f"<text x='{x + (-8 if anchor == 'end' else 8):.1f}' y='{y - 8:.1f}' fill='{TEXT}' text-anchor='{anchor}' font-size='11'>{escape(text)}</text>")
    parts += _legend(list(series.keys()))
    Path(path).write_text(_svg(parts, title))


def bar_chart(path, labels, values, title=None, y_label=None, y_fmt=_fmt, colors=None, baseline=0, pad=0.12):
    lo, hi = min(min(values), baseline), max(max(values), baseline)
    parts, y_of, _ = _axes(lo, hi, y_label, y_fmt, pad=pad)
    plot_w = W - PAD_L - PAD_R
    n = len(values)
    slot = plot_w / n
    bw = slot * 0.62
    for i, (lab, v) in enumerate(zip(labels, values)):
        c = (colors[i] if colors else (COLORS[0] if v >= baseline else COLORS[3]))
        x = PAD_L + i * slot + (slot - bw) / 2
        y0, y1 = y_of(baseline), y_of(v)
        top, hgt = min(y0, y1), abs(y0 - y1)
        parts.append(f"<rect x='{x:.1f}' y='{top:.1f}' width='{bw:.1f}' height='{max(hgt, 1):.1f}' fill='{c}' rx='2'/>")
        parts.append(f"<text x='{x + bw / 2:.1f}' y='{(top - 6) if v >= baseline else (top + hgt + 14):.1f}' fill='{TEXT}' text-anchor='middle' font-size='11'>{escape(y_fmt(v))}</text>")
        parts.append(f"<text x='{x + bw / 2:.1f}' y='{H - PAD_B + 18}' fill='{MUTED}' text-anchor='middle' font-size='11'>{escape(str(lab))}</text>")
    Path(path).write_text(_svg(parts, title))


def candle_chart(path, ohlc, title=None, y_label=None, x_labels=None, overlays: dict | None = None, marks=None, pad=0.06):
    """ohlc: [(o, h, l, c), ...]; overlays: {name: [values or None]}; marks: [(index, text)]."""
    lows = [l for _, _, l, _ in ohlc]; highs = [h for _, h, _, _ in ohlc]
    ov_vals = [v for vals in (overlays or {}).values() for v in vals if v is not None]
    lo, hi = min(lows + ov_vals), max(highs + ov_vals)
    n = len(ohlc)
    parts, y_of, _ = _axes(lo, hi, y_label, _fmt, x_labels, n, pad=pad)
    plot_w = W - PAD_L - PAD_R
    slot = plot_w / n
    bw = max(2, slot * 0.6)
    for i, (o, h, l, c) in enumerate(ohlc):
        x = PAD_L + i * slot + slot / 2
        col = COLORS[0] if c >= o else COLORS[3]
        parts.append(f"<line x1='{x:.1f}' y1='{y_of(h):.1f}' x2='{x:.1f}' y2='{y_of(l):.1f}' stroke='{col}' stroke-width='1'/>")
        top, hgt = y_of(max(o, c)), abs(y_of(o) - y_of(c))
        parts.append(f"<rect x='{x - bw / 2:.1f}' y='{top:.1f}' width='{bw:.1f}' height='{max(hgt, 1):.1f}' fill='{col}'/>")
    for j, (name, vals) in enumerate((overlays or {}).items()):
        col = COLORS[(j + 1) % len(COLORS)]
        pts = " ".join(f"{PAD_L + i * slot + slot / 2:.1f},{y_of(v):.1f}" for i, v in enumerate(vals) if v is not None)
        parts.append(f"<polyline points='{pts}' fill='none' stroke='{col}' stroke-width='2'/>")
    for idx, text in (marks or []):
        x = PAD_L + idx * slot + slot / 2
        y = y_of(ohlc[idx][1]) - 10
        parts.append(f"<text x='{x:.1f}' y='{y:.1f}' fill='{TEXT}' text-anchor='middle' font-size='11'>{escape(text)}</text>")
        parts.append(f"<line x1='{x:.1f}' y1='{y + 3:.1f}' x2='{x:.1f}' y2='{y_of(ohlc[idx][1]) - 2:.1f}' stroke='{TEXT}'/>")
    if overlays:
        parts += _legend(["Price"] + list(overlays.keys()))
    Path(path).write_text(_svg(parts, title))


def payoff_chart(path, legs, title=None, lo=None, hi=None, label="Strategy"):
    """legs: [(kind, strike, premium, qty)] with kind in call/put/stock; premium paid positive,
    received negative; qty positive long, negative short. Payoff at expiry per share."""
    strikes = [k for kind, k, _, _ in legs if kind != "stock"] or [100]
    lo = lo if lo is not None else min(strikes) * 0.8
    hi = hi if hi is not None else max(strikes) * 1.2
    xs = [lo + (hi - lo) * i / 120 for i in range(121)]

    def pay(s):
        total = 0.0
        for kind, k, prem, qty in legs:
            if kind == "call":
                v = max(s - k, 0)
            elif kind == "put":
                v = max(k - s, 0)
            else:
                v = s - k
            total += qty * (v - prem)
        return total

    ys = [pay(s) for s in xs]
    lo_y, hi_y = min(ys + [0]), max(ys + [0])
    parts, y_of, _ = _axes(lo_y, hi_y, "P&L per share at expiry", lambda v: f"{v:+.1f}")
    plot_w = W - PAD_L - PAD_R

    def x_of(s):
        return PAD_L + (s - lo) / (hi - lo) * plot_w

    zero = y_of(0)
    parts.append(f"<line x1='{PAD_L}' y1='{zero:.1f}' x2='{W - PAD_R}' y2='{zero:.1f}' stroke='{MUTED}' stroke-dasharray='4 4'/>")
    pos = " ".join(f"{x_of(s):.1f},{y_of(max(y, 0)):.1f}" for s, y in zip(xs, ys))
    parts.append(f"<polyline points='{pos}' fill='none' stroke='{COLORS[0]}' stroke-width='2.5'/>")
    neg = " ".join(f"{x_of(s):.1f},{y_of(min(y, 0)):.1f}" for s, y in zip(xs, ys))
    parts.append(f"<polyline points='{neg}' fill='none' stroke='{COLORS[3]}' stroke-width='2.5'/>")
    for k in sorted(set(strikes)):
        parts.append(f"<line x1='{x_of(k):.1f}' y1='{PAD_T}' x2='{x_of(k):.1f}' y2='{H - PAD_B}' stroke='{GRID}'/>")
        parts.append(f"<text x='{x_of(k):.1f}' y='{H - PAD_B + 18}' fill='{MUTED}' text-anchor='middle'>K {_fmt(k)}</text>")
    for s in (lo, hi):
        parts.append(f"<text x='{x_of(s):.1f}' y='{H - PAD_B + 34}' fill='{MUTED}' text-anchor='middle' font-size='11'>{_fmt(s)}</text>")
    parts.append(f"<text x='{W - PAD_R}' y='{H - PAD_B + 34}' fill='{MUTED}' text-anchor='end' font-size='11'>underlying price at expiry</text>")
    parts += _legend([f"{label}: profit", "loss"], y=H - 12) if False else []
    parts.append(f"<text x='{PAD_L}' y='{H - 12}' fill='{TEXT}'>{escape(label)} — green above zero, red below</text>")
    Path(path).write_text(_svg(parts, title))


def flow_diagram(path, steps, title=None, notes=None):
    """steps: list of short labels drawn left-to-right as boxes with arrows;
    notes: optional list, one per step, drawn beneath."""
    n = len(steps)
    gap = 26
    box_w = (W - PAD_L - PAD_R - gap * (n - 1)) / n
    box_h = 64
    y = PAD_T + 40
    parts = []
    for i, s in enumerate(steps):
        x = PAD_L + i * (box_w + gap)
        parts.append(f"<rect x='{x:.1f}' y='{y}' width='{box_w:.1f}' height='{box_h}' rx='8' fill='#141a1f' stroke='{COLORS[0]}' stroke-width='1.5'/>")
        lines = _wrap(s, max(10, int(box_w / 7.2)))
        for j, ln in enumerate(lines[:3]):
            parts.append(f"<text x='{x + box_w / 2:.1f}' y='{y + 26 + j * 15 - (len(lines[:3]) - 1) * 7}' fill='{TEXT}' text-anchor='middle' font-size='12' font-weight='600'>{escape(ln)}</text>")
        if i < n - 1:
            ax = x + box_w
            parts.append(f"<line x1='{ax + 4:.1f}' y1='{y + box_h / 2}' x2='{ax + gap - 6:.1f}' y2='{y + box_h / 2}' stroke='{MUTED}' stroke-width='2'/>")
            parts.append(f"<polygon points='{ax + gap - 6:.1f},{y + box_h / 2 - 5} {ax + gap:.1f},{y + box_h / 2} {ax + gap - 6:.1f},{y + box_h / 2 + 5}' fill='{MUTED}'/>")
        if notes and i < len(notes) and notes[i]:
            for j, ln in enumerate(_wrap(notes[i], max(12, int(box_w / 6.3)))[:5]):
                parts.append(f"<text x='{x + box_w / 2:.1f}' y='{y + box_h + 22 + j * 15}' fill='{MUTED}' text-anchor='middle' font-size='11'>{escape(ln)}</text>")
    Path(path).write_text(_svg(parts, title))


def _wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


if __name__ == "__main__":  # smoke test: python3 scripts/svgfig.py /tmp/out
    import sys
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/svgfig-test"); out.mkdir(parents=True, exist_ok=True)
    line_chart(out / "line.svg", {"SPY": [400, 405, 398, 410, 415, 412, 420], "SMA": [None, None, 401, 404, 408, 412, 416]}, title="Line", y_label="$", x_labels=list("MTWTFMT"), annotations=[(3, "cross")], hlines=[(410, "prior high")])
    bar_chart(out / "bar.svg", ["2020", "2021", "2022", "2023"], [18.4, 28.7, -18.1, 26.3], title="Bars", y_label="%", y_fmt=lambda v: f"{v:+.1f}%")
    candle_chart(out / "candle.svg", [(100, 104, 99, 103), (103, 105, 101, 102), (102, 106, 102, 105), (105, 107, 103, 104)], title="Candles", overlays={"SMA": [None, 102.5, 103.3, 103.5]}, marks=[(2, "breakout")])
    payoff_chart(out / "payoff.svg", [("call", 100, 3.2, 1), ("call", 110, 1.1, -1)], title="Bull call spread", label="Long 100C / short 110C")
    flow_diagram(out / "flow.svg", ["Order sent", "Broker routes", "Venue matches", "NSCC clears", "DTC settles T+1"], title="Trade lifecycle", notes=["market or limit", "wholesaler or exchange", "NBBO protected", "netted per broker", "shares and cash move"])
    print("wrote", sorted(p.name for p in out.iterdir()))

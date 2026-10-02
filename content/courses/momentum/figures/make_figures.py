"""Figures for the Momentum & Swing Trading course.

Every series is read from data.json next to this file. That file holds numbers
computed from Yahoo Finance daily bars (chart API, pulled 2026-09-24); the
calculations are shown in each lesson's Worked example. Run:

    cd figures && python3 make_figures.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, "../../../scripts")
sys.path.insert(0, str(HERE.parents[3] / "scripts"))  # phantom-site-courses/scripts, regardless of cwd
from svgfig import bar_chart, candle_chart, line_chart  # noqa: E402

D = json.load(open(HERE / "data.json"))


def pct(v):
    return f"{v:+.0f}%"


def formation_vs_hold():
    f = D["formation"]
    bar_chart(HERE / "formation-vs-hold-2025.svg", f["labels"], f["hold_pct"],
              title="12-1 formation rank (left = strongest) vs next 6-month return, 20 stocks",
              y_label="6-month return after formation, %", y_fmt=pct)


def rs_ranking():
    r = D["rs"]
    bar_chart(HERE / "rs-ranking-2026-03-31.svg", r["labels"], r["rs_pct"],
              title=f"6-month relative strength, {r['d0']} to {r['d1']} (SPY {r['spy_pct']:+.1f}%)",
              y_label="price change, %", y_fmt=pct)


def atr_sizing_curve():
    # Position value as % of account = risk% / (stop multiple x ATR%), 1% risk, 2 x ATR stop.
    xs = [1.0 + 0.25 * i for i in range(21)]  # ATR% from 1.0 to 6.0
    pos = [1.0 / (2 * x / 100) for x in xs]   # % of account
    labels = [f"{x:.2f}".rstrip("0").rstrip(".") + "%" if i % 4 == 0 else "" for i, x in enumerate(xs)]
    pts = D["atr_points"]
    ann = []
    for name in ("JNJ", "AVGO"):
        a = pts[name]
        k = min(range(len(xs)), key=lambda i: abs(xs[i] - a))
        ann.append((k, f"{name} ATR {a:.2f}% -> {pos[k]:.0f}% of account"))
    line_chart(HERE / "atr-sizing-curve.svg", {"position value, % of account (1% risk, 2 x ATR stop)": pos},
               title="ATR sizing: how much of the account one position gets", y_label="% of account",
               x_labels=labels, y_fmt=lambda v: f"{v:.0f}%", annotations=ann, hlines=[(100, "100% = fully invested in one name")])


def momentum_crash():
    c = D["crash"]
    base = c["eq"][0]
    eq = [100 * e / base for e in c["eq"]]
    labels = [d if d.endswith(("-01", "-07")) else "" for d in c["dates"]]
    k = c["dates"].index("2009-04")
    line_chart(HERE / "sector-momentum-crash-2009.svg", {"12-1 sector momentum, long top 3 / short bottom 3, monthly": eq},
               title="Nine SPDR sector ETFs, 12-1 momentum long/short, Dec 2007 = 100",
               y_label="index", x_labels=labels, annotations=[(k, "Apr 2009: -16.7% in one month")])


def turn_of_month():
    t = D["tom"]
    labels = [f"{d:+d}" for d in t["days"]]
    bar_chart(HERE / "turn-of-month-spy.svg", labels, t["bps"],
              title=f"SPY average daily return by trading day around month end, {t['first']} to {t['last']}",
              y_label="basis points per day (all other days: %.1f bp)" % t["other_bps"], y_fmt=lambda v: f"{v:+.0f}")


def rule_drawdown():
    d = D["drawdown"]
    labels = [x[:7] if i % 12 == 0 else "" for i, x in enumerate(d["dates"])]
    line_chart(HERE / "swing-rule-drawdown.svg", {"drawdown from equity peak, 1% risk per trade": d["dd_pct"]},
               title="20-day breakout swing rule, 20 stocks, drawdown by trade exit date",
               y_label="%", x_labels=labels, y_fmt=lambda v: f"{v:.0f}%")


def nvda_breakout():
    n = D["nvda"]
    k = n["breakout_idx"]
    stop_line = [n["stop"]] * len(n["ohlc"])
    candle_chart(HERE / "nvda-breakout-2025-06.svg", n["ohlc"],
                 title="NVDA daily, 2025-05-27 to 2025-07-18: 20-day-high breakout with the stop marked",
                 y_label="$", x_labels=n["dates"],
                 overlays={"50-day SMA": n["sma50"], f"stop {n['stop']:.2f} (2 x ATR under entry, = prior 20-day high)": stop_line},
                 marks=[(k, "breakout close 154.31"), (k + 1, "entry 155.98")])


if __name__ == "__main__":
    for fn in (formation_vs_hold, rs_ranking, atr_sizing_curve, momentum_crash, turn_of_month, rule_drawdown, nvda_breakout):
        fn()
    print("wrote", sorted(p.name for p in HERE.glob("*.svg")))

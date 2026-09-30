import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *
"""Figures for the Mean Reversion & Pairs course.

Every series is read from data.json next to this file. Those numbers were
computed from Yahoo Finance daily bars (chart API, period1/period2 unix
timestamps, interval=1d, pulled 2026-09-24) and the calculations are shown in
each lesson's Worked example. Run:

    cd figures && python3 make_figures.py
"""
import json
import math

HERE = Path(__file__).resolve().parent
D = json.load(open(HERE / "data.json"))


def pct(v):
    return f"{v:+.1f}%"


def acf_bars():
    # Lesson 2: SPY daily-return autocorrelation, lags 1-10, 2015-01-02 to 2026-09-23.
    vals = [round(v, 3) for v in D["acf_lags"]]
    bar_chart(HERE / "spy-daily-autocorrelation-lags.svg", [f"lag {k}" for k in range(1, 11)], vals,
              title="SPY daily return autocorrelation by lag, 2015-01-02 to 2026-09-23 (n = 2,947)",
              y_label="autocorrelation (2 s.e. = 0.037)", y_fmt=lambda v: f"{v:+.3f}")


def rsi_window():
    # Lesson 4: RSI(2) on SPY, 2025-02-03 to 2025-06-30, with the 10 line and selected signals.
    w = D["rsi_window"]
    labels = [d[5:] for d in w["dates"]]
    show = {"2025-02-25", "2025-04-08", "2025-05-23"}
    ann = []
    for idx, text, above in w["signals"]:
        date = text.split(" ")[0]
        if date in show:
            fwd = text.split("-> 5d ")[1]
            ann.append((idx, f"{date[5:]} {'above' if above else 'BELOW'} 200d, next 5d {fwd}"))
    line_chart(HERE / "spy-rsi2-signals-2025.svg", {"RSI(2) of SPY close": w["rsi"]},
               title="SPY RSI(2), 2025-02-03 to 2025-06-30: below 10 is the entry zone",
               y_label="RSI(2)", x_labels=labels, hlines=[(10, "entry threshold 10"), (70, "exit threshold 70")],
               annotations=ann, y_fmt=lambda v: f"{v:.0f}")


def rule_equity():
    # Lesson 4: growth of 1 for the RSI(2) rule vs SPY buy-and-hold, monthly samples.
    e = D["equity"]
    labels = [d[:7] for d in e["dates"]]
    line_chart(HERE / "spy-rsi2-rule-equity.svg", {"RSI(2) rule: buy < 10 above 200-day, exit close > 5-day SMA": e["rule"], "SPY buy and hold": e["spy"]},
               title="RSI(2) reversion rule on SPY vs buy and hold, 2015-10-19 to 2026-09-23, start = 1.00",
               y_label="growth of 1", x_labels=labels, y_fmt=lambda v: f"{v:.1f}")


def pair_zscore_year():
    # Lesson 8: XLE/XOP spread z-score over 2025-09-23 to 2026-09-23 with bands and the trades taken.
    p = D["xop_year"]
    labels = [d[:7] for d in p["dates"]]
    ann = []
    for t in p["trades_static"]:
        ann.append((p["dates"].index(t["entry"]), f"enter long spread {t['entry']} z {t['z_in']:+.2f}"))
    zmin = min(p["z_static"]); imin = p["z_static"].index(zmin)
    ann.append((imin, f"{p['dates'][imin]} z {zmin:+.2f}, worst mark {p['trades_static'][0]['worst_mtm']:+,.0f} USD"))
    ann.append((len(p["dates"]) - 1, f"open at {p['dates'][-1][5:]}, z {p['z_static'][-1]:+.2f}"))
    line_chart(HERE / "xle-xop-zscore-2025-2026.svg",
               {"z vs formation-window mean and s.d.": p["z_static"], "z vs rolling 60-day mean and s.d.": p["z_rolling"]},
               title="XOP vs 1.27 x XLE log spread z-score, 2025-09-23 to 2026-09-23 (Yahoo Finance closes)",
               y_label="z", x_labels=labels, hlines=[(2, "+2 entry"), (0, "0 exit"), (-2, "-2 entry")],
               annotations=ann, y_fmt=lambda v: f"{v:+.0f}")


def half_life_fit():
    # Lesson 9: fitted exponential decay of |z| after a 2 s.d. entry vs the in-sample average path.
    h = D["halflife"]
    xom, xop = h["xom"], h["xop"]
    k = list(range(0, 41))
    labels = [str(v) for v in k]
    line_chart(HERE / "spread-half-life-fit.svg",
               {f"XLE/XOM fit, half-life {xom['hl']:.0f}d": xom["fit"],
                f"XLE/XOM observed ({xom['n']} crossings)": xom["emp"],
                f"XOP/XLE fit, half-life {xop['hl']:.0f}d (t {xop['b']/xop['se']:.1f})": xop["fit"]},
               title="How fast a 2 s.d. deviation decays: half-life fits, formation 2023-09-22 to 2025-09-22",
               y_label="|z| (trading days after crossing 2 on the x-axis)", x_labels=labels, hlines=[(1.0, "half of entry deviation")],
               y_fmt=lambda v: f"{v:.1f}")


def blowout_2020():
    # Lesson 10: XLE/XOP z-score through 2020 using 2018-2019 formation stats.
    y = D["y2020"]
    labels = [d[:7] for d in y["dates"]]
    t0 = y["trades"][0]; ts = y["trades_stop"][0]
    zmax = max(y["z"]); imax = y["z"].index(zmax)
    ann = [(y["dates"].index(t0["entry"]), f"short spread {t0['entry']} z {t0['z_in']:+.2f}"),
           (y["dates"].index(ts["exit"]), f"4 s.d. stop {ts['exit']} z {ts['z_out']:+.2f}, {ts['net']:+,.0f} USD"),
           (imax, f"{y['dates'][imax]} z {zmax:+.2f}; no-stop mark {t0['worst_mtm']:+,.0f} USD")]
    line_chart(HERE / "xle-xop-zscore-2020.svg", {"z vs 2018-2019 formation stats (beta 2.38)": y["z"]},
               title="XOP vs XLE spread z-score through 2020: the deviation went to 14 s.d.",
               y_label="z", x_labels=labels, hlines=[(2, "+2 entry"), (4, "+4 stop"), (0, "0 exit")], annotations=ann,
               y_fmt=lambda v: f"{v:+.0f}")


def walk_forward_flow():
    # Lesson 12: the walk-forward loop used to test the RSI(2) rule.
    wf = D["walk_forward"]
    flow_diagram(HERE / "walk-forward-process.svg",
                 ["Fix the rule family and grid", "Train: 3 prior years", "Pick the best combination", "Test: next 1 year, untouched", "Roll forward 1 year", "Stitch the test years"],
                 title="Walk-forward validation as run in this course (SPY RSI(2), test years 2019 to 2026)",
                 notes=["32 combinations: threshold, exit, 200-day filter", "e.g. 2016-2018 for the 2019 test", "highest net return, at least 10 trades", "record every trade; never re-pick", "2020 test trains on 2017-2019, and so on",
                        f"{wf['oos_n']} trades, {wf['oos_total']*100:+.1f}% vs {wf['default_total']*100:+.1f}% fixed rule"])


if __name__ == "__main__":
    acf_bars(); rsi_window(); rule_equity(); pair_zscore_year(); half_life_fit(); blowout_2020(); walk_forward_flow()
    print("wrote", sorted(p.name for p in HERE.glob("*.svg")))

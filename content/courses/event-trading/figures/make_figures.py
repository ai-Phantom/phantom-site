"""Figures for the Earnings & Event Trading course.

Every plotted number is either (a) a price pulled from Yahoo Finance's public
chart API (query1.finance.yahoo.com/v8/finance/chart/<ticker>, daily or
5-minute bars, verified row counts, quoted in the lessons), (b) an option
quote from Cboe's public delayed-quotes feed for NVDA captured 2026-09-23, or
(c) the clearly labelled representative chain used in lessons 2, 5 and 13
(a 7.0% ATM straddle and a 1.4% short strangle, NOT dated quotes).

Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *  # noqa: E402,F401

OUT = Path(__file__).resolve().parent
MUTED_BAR = "#8a948e"
GREEN = "#7eff5c"

# ---------------------------------------------------------------------------
# Lesson 2: representative implied move (7.0%, labelled) vs realised
# close-to-close move for NVDA's last four reports. Realised moves from Yahoo
# daily closes: 186.52->180.64, 195.56->184.89, 223.47->219.51, 209.66->227.98.
# ---------------------------------------------------------------------------
reports = ["Nov-25", "Feb-26", "May-26", "Aug-26"]
implied_rep = 7.0
realised_abs = [3.15, 5.46, 1.77, 8.74]
labels, values, colors = [], [], []
for name, real in zip(reports, realised_abs):
    labels += [f"{name} impl", f"{name} real"]
    values += [implied_rep, real]
    colors += [MUTED_BAR, GREEN]
bar_chart(OUT / "nvda-implied-vs-realised-four-reports.svg", labels, values,
          title="NVDA: representative implied move vs realised |move|, last four reports",
          y_label="% of prior close", y_fmt=lambda v: f"{v:.1f}%", colors=colors)

# ---------------------------------------------------------------------------
# Lesson 4: ATM implied volatility by expiration for NVDA, Cboe delayed quotes
# snapshot 2026-09-23 (spot 228.56). Each point is the mean of the ATM call and
# put IV at the strike nearest spot.
# ---------------------------------------------------------------------------
expiries = ["Sep 25", "Sep 30", "Oct 2", "Oct 9", "Oct 16", "Oct 23", "Oct 30",
            "Nov 20", "Dec 18", "Jan 15", "Feb 19"]
atm_iv = [31.5, 29.9, 31.3, 31.0, 31.3, 31.2, 31.8, 36.5, 36.3, 36.2, 36.3]
line_chart(OUT / "nvda-atm-iv-term-structure-2026-09-23.svg", {"ATM implied vol": atm_iv},
           title="NVDA ATM implied volatility by expiration, Cboe snapshot 2026-09-23",
           y_label="% annualised", x_labels=expiries, y_fmt=lambda v: f"{v:.0f}%",
           annotations=[(7, "Nov 20: first expiry after the Nov 17 report")])

# ---------------------------------------------------------------------------
# Lesson 5: payoff at expiry for the representative chain on NVDA into the
# 2026-08-26 report (prior close 209.66). Long 210 straddle costs 7.0% of spot
# = 14.68 (7.34 per leg); short 190P/230C strangle collects 1.4% = 2.94 (1.47
# per leg). Representative, not dated quotes.
# ---------------------------------------------------------------------------
payoff_chart(OUT / "long-straddle-payoff-nvda-aug-2026.svg",
             [("call", 210, 7.34, 1), ("put", 210, 7.34, 1)],
             title="Long 210 straddle, cost 14.68 (representative chain, NVDA 2026-08-26)",
             lo=180, hi=240, label="Long 210C + long 210P")
payoff_chart(OUT / "short-strangle-payoff-nvda-aug-2026.svg",
             [("put", 190, 1.47, -1), ("call", 230, 1.47, -1)],
             title="Short 190P / 230C strangle, credit 2.94 (representative chain)",
             lo=180, hi=240, label="Short 190P + short 230C")

# ---------------------------------------------------------------------------
# Lesson 6: SPY 5-minute closes on FOMC day 2026-09-16 (Yahoo, 78 regular-
# session bars 09:30-15:55 ET). Statement 14:00, press conference 14:30.
# Prior close 757.39 (2026-09-15).
# ---------------------------------------------------------------------------
spy_0916 = [759.21, 758.81, 758.8, 759.89, 760.24, 760.2, 759.68, 759.7, 759.55, 759.28,
            758.96, 758.96, 759.15, 759.37, 759.84, 759.62, 759.68, 760.21, 760.53, 760.91,
            760.74, 760.6, 760.54, 760.34, 760.13, 760.39, 760.57, 761.05, 760.79, 760.69,
            760.33, 760.48, 760.37, 760.33, 759.98, 760.14, 759.69, 759.89, 759.9, 760.1,
            759.89, 759.77, 759.41, 759.57, 759.73, 759.76, 759.64, 759.93, 759.79, 759.63,
            759.34, 759.57, 759.79, 760.28, 760.21, 760.67, 759.97, 759.94, 759.85, 759.68,
            757.65, 757.89, 759.0, 757.56, 755.14, 753.89, 754.76, 753.2, 751.31, 750.95,
            750.68, 751.26, 752.57, 752.42, 752.09, 753.46, 754.09, 754.07]
times = [f"{h:02d}:{m:02d}" for h in range(9, 16) for m in range(0, 60, 5) if (h, m) >= (9, 30)]
assert len(times) == len(spy_0916) == 78
line_chart(OUT / "spy-fomc-day-2026-09-16.svg", {"SPY 5-min close": spy_0916},
           title="SPY on FOMC day, 2026-09-16 (statement 14:00, press conference 14:30)",
           y_label="$", x_labels=times, annotations=[(54, "14:00 statement"), (60, "14:30 presser")],
           hlines=[(757.39, "prior close 757.39")])

# ---------------------------------------------------------------------------
# Lesson 10: NVDA daily candles 2026-08-12 to 2026-09-04 (Yahoo daily OHLC).
# Report after the close on 08-26; 08-27 opened 222.86 vs 209.66 close (+6.3%).
# ---------------------------------------------------------------------------
candles = [(221.04, 225.1, 220.2, 224.09), (225.06, 227.23, 223.71, 225.3), (226.77, 227.49, 224.5, 225.16),
           (225.98, 227.92, 224.86, 225.01), (220.45, 221.64, 218.69, 219.74), (221.67, 222.87, 216.76, 217.56),
           (218.36, 219.86, 215.66, 216.85), (218.42, 218.74, 214.5, 214.72), (215.53, 215.59, 207.25, 208.48),
           (211.03, 214.73, 210.11, 213.05), (212.64, 213.6, 209.23, 209.66), (222.86, 230.47, 220.9, 227.98),
           (227.36, 229.26, 216.81, 217.55), (218.87, 221.3, 216.21, 220.78), (216.75, 220.41, 215.1, 217.44),
           (218.79, 227.95, 218.48, 224.41), (226.02, 230.4, 224.75, 228.45), (231.09, 234.76, 229.63, 230.36)]
dates = ["08-12", "08-13", "08-14", "08-17", "08-18", "08-19", "08-20", "08-21", "08-24", "08-25", "08-26",
         "08-27", "08-28", "08-31", "09-01", "09-02", "09-03", "09-04"]
assert len(candles) == len(dates) == 18
candle_chart(OUT / "nvda-daily-candles-aug-2026-earnings.svg", candles,
             title="NVDA daily candles around the 2026-08-26 report (gap +6.3% at the 08-27 open)",
             y_label="$", x_labels=dates, marks=[(11, "08-27: gap open 222.86")])

# ---------------------------------------------------------------------------
# Lesson 10: the pre-event checklist as a flow.
# ---------------------------------------------------------------------------
flow_diagram(OUT / "pre-event-checklist-flow.svg",
             ["Confirm date and time", "Read the implied move", "Size for the gap", "Write the exit plan", "Open the journal row"],
             title="Pre-event checklist: five gates before any event position",
             notes=["company IR page or Fed/BLS calendar, not a screener",
                    "ATM straddle of the first expiry after the event",
                    "risk budget / (price x 2 x implied move)",
                    "what you do at the open, at 15 min, at the close",
                    "implied, expected, thesis, before the print"])

print("wrote", sorted(p.name for p in OUT.glob("*.svg")))

"""Figures for the Futures: ES/NQ, Margin & Contract Specs course.

Every number here is copied from a lesson's worked example, so the pictures
and the text agree exactly. Sources, as cited in the lessons:

  - Prices: Yahoo Finance chart API for ES=F / ESZ26.CME (daily, pulled
    2026-09-24 and 2026-09-30), CL contract months (2026-09-24 last trades),
    and ES=F 1-hour bars 2026-08-24 to 2026-09-24 for the session volumes.
  - Contract specs: CME Group E-mini S&P 500 contract specifications page
    ($50 multiplier, 0.25 tick = $12.50).
  - Margin: CME Group E-mini S&P 500 margins page; the figure used is the
    CME requirement for the Dec 2026 contract as republished on 2026-08-18
    (initial $27,526, maintenance $25,024).

Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *  # noqa: E402,F401,F403

MULTIPLIER = 50.0
REFERENCE_CLOSE = 7772.50          # ESZ26 close, 2026-09-23 (Yahoo Finance)
INITIAL_MARGIN = 27526.0           # CME, Dec 2026 ES, as republished 2026-08-18
MAINTENANCE_MARGIN = 25024.0
NOTIONAL = REFERENCE_CLOSE * MULTIPLIER          # 388,625
TWO_PCT_MOVE_DOLLARS = NOTIONAL * 0.02            # 7,772.50


def dollars(v):
    return f"${v:,.0f}"


# Lesson 3: what one ES contract controls versus what you post
bar_chart("leverage-vs-margin.svg",
          ["Notional value", "Initial margin", "Maintenance margin", "2% adverse move"],
          [NOTIONAL, INITIAL_MARGIN, MAINTENANCE_MARGIN, TWO_PCT_MOVE_DOLLARS],
          title="One ES contract at 7,772.50: notional vs performance bond",
          y_label="USD", y_fmt=dollars,
          colors=["#4d9fff", "#7eff5c", "#f5c842", "#ff4d6a"])

# Lesson 4: a $30,000 account long one ES from the 2026-06-01 close (7,613.25),
# marked to each daily close (Yahoo Finance ES=F) through 2026-06-10.
june_dates = ["06-01", "06-02", "06-03", "06-04", "06-05", "06-08", "06-09", "06-10"]
june_closes = [7613.25, 7623.75, 7571.75, 7601.00, 7400.50, 7416.00, 7392.75, 7278.50]
equity = [30000 + (c - june_closes[0]) * MULTIPLIER for c in june_closes]
line_chart("margin-call-path.svg", {"Account equity, long 1 ES": equity},
           title="Daily settlement of a $30,000 account, June 2026",
           y_label="USD", x_labels=june_dates, y_fmt=dollars,
           hlines=[(INITIAL_MARGIN, "initial $27,526"), (MAINTENANCE_MARGIN, "maintenance $25,024")],
           annotations=[(4, "06-05: -212.75 pts, equity $19,362.50")])

# Lesson 5: WTI crude term structure, last trades 2026-09-24 (Yahoo Finance CL contract months)
cl_months = ["Nov 26", "Dec 26", "Jan 27", "Feb 27", "Mar 27", "Jun 27", "Sep 27", "Dec 27"]
cl_prices = [92.41, 89.47, 86.90, 84.68, 82.78, 78.38, 75.32, 73.29]
line_chart("cl-term-structure.svg", {"CL last trade, 2026-09-24": cl_prices},
           title="WTI crude oil futures curve in backwardation",
           y_label="$ per barrel", x_labels=cl_months, y_fmt=lambda v: f"${v:.0f}")

# Lesson 6: the quarterly roll as a sequence of decisions
flow_diagram("quarterly-roll.svg",
             ["Expiring contract (ESZ26)", "Roll date: Thu before 3rd Fri", "Sell Dec / buy Mar as a spread", "Spread = carry + friction", "Continuous chart splices"],
             title="Rolling a long ES position across the Dec 2026 expiry",
             notes=["last trade 9:30 am ET Fri 2026-12-18, cash-settled to the SOQ",
                    "volume migrates to Mar on Thu 2026-12-10; most brokers auto-liquidate before expiry",
                    "one order, one fill on the calendar spread, spread tick 0.05 = $2.50",
                    "fair spread about 61 pts at r 4.14%, q 0.99%; friction is 2 commissions plus spread ticks",
                    "unadjusted charts show a gap at the splice; back-adjusted charts change past prices"])

# Lesson 7: share of ES volume by hour of day (ET), 1-hour bars 2026-08-24 to 2026-09-24, Yahoo Finance
hours = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a", "12p", "1p", "2p", "3p", "4p", "6p", "7p", "8p", "9p", "10p", "11p"]
share = [0.4, 0.6, 0.8, 1.2, 1.5, 1.2, 1.1, 1.6, 3.2, 12.3, 16.2, 12.5, 9.1, 7.5, 8.5, 16.2, 3.4, 0.1, 0.4, 0.8, 0.7, 0.5, 0.4]
bar_chart("es-volume-by-hour.svg", hours, share,
          title="ES volume by hour of day (ET), 2026-08-24 to 2026-09-24",
          y_label="% of monthly volume", y_fmt=lambda v: f"{v:.1f}%" if v < 10 else f"{v:.0f}%",
          colors=["#4d9fff"] * 9 + ["#7eff5c"] * 8 + ["#4d9fff"] * 6)

# Lesson 11 and capstone: dollar loss on a 2% adverse open (155.45 pts) at 7,772.50 by position size
two_pct_points = REFERENCE_CLOSE * 0.02           # 155.45
positions = ["1 MES", "2 MES", "5 MES", "1 ES", "2 ES"]
per_point = [5, 10, 25, 50, 100]
losses = [-two_pct_points * p for p in per_point]  # -777.25 ... -15,545
bar_chart("adverse-open-by-position.svg", positions, losses,
          title="Loss on a 2% adverse open (155.45 pts) by position, $25,000 account",
          y_label="USD", y_fmt=lambda v: f"-${abs(v):,.0f}" if v < 0 else f"${v:,.0f}")

print("wrote", sorted(p.name for p in Path(".").glob("*.svg")))

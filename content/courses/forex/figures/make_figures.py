"""Figures for the Forex course. Every number below is a literal copied from the
lesson that embeds the figure, so the SVGs regenerate with no network access:
  - BIS Triennial Central Bank Survey, April 2025 (turnover by layer)
  - tastyfx forex product details, read 2026-09-24 (minimum spreads, margins)
  - ECB euro foreign exchange reference rates, 2025-09-23 to 2026-09-23 (rates,
    daily volatility, 2008 and 2024 carry-crash spot moves)
  - OANDA TMS Brokers swap points table valid 2026-09-21 to 2026-09-27
  - Yahoo Finance chart API daily bars for USD/JPY and EUR/USD, pulled 2026-09-24
  - RBA, BoJ and Federal Reserve policy rates for the carry windows
Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *
import math

# --- Figure 1 (lesson 1): the path of a retail order ---
flow_diagram(
    "retail-order-path.svg",
    ["Your order", "Dealer is the counterparty", "Liquidity providers, ECNs", "Interbank platforms", "CLS settlement"],
    title="Path of a retail FX order (turnover: BIS Triennial Survey, April 2025)",
    notes=[
        "1 lot EUR/USD at 1.1411: $114,110 notional, bought at the ask",
        "NFA rule: FDM is counterparty to every trade; nets clients, hedges the rest",
        "banks, non-bank market makers; $4.8trn/day, 50% of turnover",
        "EBS, Refinitiv Matching; inter-dealer $4.4trn/day, 46%",
        "spot settles T+2 PvP; retail rolls at 17:00 New York",
    ],
)

# --- Figure 2 (lesson 3): minimum spread as % of a one-sigma daily move ---
PAIRS  = ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/MXN", "USD/ZAR", "USD/TRY"]
SPREAD = [0.8, 0.8, 1.0, 1.0, 50.0, 110.0, 50.0]            # pips, tastyfx minimums
RATE   = [1.1411, 157.92, 1.3276, 0.7067, 17.439, 16.347, 48.837]  # ECB fix 2026-09-23
ANNVOL = [5.4, 8.1, 6.1, 7.8, 7.4, 11.0, 1.5]                # % annualised, ECB daily rates, 1y
PIP    = [0.0001, 0.01, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001]
def sigma_pips(rate, vol, pip):
    return rate * (vol / 100) / math.sqrt(252) / pip
PCT = [round(s / sigma_pips(r, v, p) * 100, 1) for s, r, v, p in zip(SPREAD, RATE, ANNVOL, PIP)]
bar_chart(
    "spread-cost-vs-daily-sigma.svg", PAIRS, PCT,
    title="Minimum spread as % of a one-sigma daily move (tastyfx spreads, ECB vol to 2026-09-23)",
    y_label="% of one-sigma day", y_fmt=lambda v: f"{v:.1f}%",
)

# --- Figure 3 (lesson 4): leverage vs probability of a 50% drawdown in 60 days ---
SIGMA_DAY = 0.00339   # EUR/USD daily std dev of log returns, ECB rates 2025-09-23..2026-09-23
N_DAYS = 60
def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))
LEV = list(range(1, 51))
RUIN = [round(200 * phi(-(0.5 / L) / (SIGMA_DAY * math.sqrt(N_DAYS))), 2) for L in LEV]
line_chart(
    "leverage-vs-ruin-probability.svg",
    {"P(lose 50% within 60 days)": RUIN},
    title="Leverage vs probability of a 50% drawdown in 60 days, EUR/USD, sigma 0.339%/day",
    y_label="%", x_labels=[str(L) for L in LEV], y_fmt=lambda v: f"{v:.0f}%",
    annotations=[(29, f"ESMA 30:1 cap: {RUIN[29]:.0f}%"), (49, f"CFTC 50:1 cap: {RUIN[49]:.0f}%"), (9, f"10:1: {RUIN[9]:.0f}%")],
)

# --- Figure 4 (lesson 5): the 24-hour clock in UTC ---
flow_diagram(
    "session-clock-utc.svg",
    ["Sydney 22:00 to 07:00", "Tokyo 00:00 to 09:00", "London 08:00 to 17:00", "New York 13:00 to 22:00", "Rollover 22:00 UTC"],
    title="The FX trading day in UTC (winter time)",
    notes=[
        "week opens Sun 21:00 UTC; AUD, NZD pairs; RBA decisions",
        "with Singapore (11.8%) and Hong Kong; BoJ decisions ~03:00 UTC",
        "largest centre; ECB decisions 13:15; London fix 16:00",
        "13:00-17:00 overlap with London is deepest; NFP, CPI 13:30; FOMC 19:00",
        "17:00 ET: swap applied, spreads widen briefly; Fri 22:00 close",
    ],
)

# --- Figure 5 (lesson 7): carry earned vs spot move, % of notional ---
bar_chart(
    "carry-vs-spot-decomposition.svg",
    ["AUDJPY 08 carry", "AUDJPY 08 spot", "USDJPY 24 carry", "USDJPY 24 spot", "USDJPY 30d carry", "USDJPY 30d 1-sigma"],
    [1.8, -45.6, 0.5, -12.1, 0.15, -2.35],
    title="Carry collected vs spot move, % of notional: 2008, 2024 and a 30-day hold in 2026",
    y_label="% of notional", y_fmt=lambda v: f"{v:+.1f}%" if abs(v) >= 1 else f"{v:+.2f}%",
)

# --- Figure 6 (lesson 9): median daily range by session type, 2026 YTD ---
EV_LABELS = ["EUR other", "EUR NFP", "EUR CPI", "EUR FOMC", "EUR BoJ", "JPY other", "JPY NFP", "JPY CPI", "JPY FOMC", "JPY BoJ"]
EV_PIPS   = [47.7, 60.9, 48.0, 35.1, 48.5, 66.9, 127.6, 91.0, 67.8, 177.8]
bar_chart(
    "event-day-ranges-2026.svg", EV_LABELS, EV_PIPS,
    title="Median daily range by session type, 2026-01-01 to 2026-09-23 (Yahoo daily bars)",
    y_label="pips", y_fmt=lambda v: f"{v:.0f}",
    colors=[COLORS[1]] * 5 + [COLORS[0]] * 5,
)

# --- Figure 7 (lesson 10): USD/JPY daily candles, last 60 sessions, with event marks ---
DATES = ["2026-07-02", "2026-07-03", "2026-07-06", "2026-07-07", "2026-07-08", "2026-07-09", "2026-07-10", "2026-07-13", "2026-07-14", "2026-07-15", "2026-07-16", "2026-07-17", "2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23", "2026-07-24", "2026-07-27", "2026-07-28", "2026-07-29", "2026-07-30", "2026-07-31", "2026-08-03", "2026-08-04", "2026-08-05", "2026-08-06", "2026-08-07", "2026-08-10", "2026-08-11", "2026-08-12", "2026-08-13", "2026-08-14", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20", "2026-08-21", "2026-08-24", "2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28", "2026-08-31", "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-07", "2026-09-08", "2026-09-09", "2026-09-10", "2026-09-11", "2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-21", "2026-09-22", "2026-09-23"]
OHLC = [[162.542, 162.584, 160.688, 162.539], [161.404, 161.494, 160.62, 161.449], [161.487, 162.424, 161.465, 161.452], [162.095, 162.173, 161.688, 162.088], [162.362, 162.698, 162.08, 162.363], [162.51, 162.565, 162.247, 162.539], [162.335, 162.419, 161.292, 162.363], [161.886, 162.393, 161.886, 161.878], [162.413, 162.466, 161.695, 162.429], [162.187, 162.415, 161.967, 162.187], [162.084, 162.469, 161.98, 162.072], [162.381, 162.467, 162.147, 162.376], [162.525, 162.583, 162.271, 162.512], [162.48, 163.031, 162.44, 162.487], [163.168, 163.198, 162.85, 163.186], [163.068, 163.979, 162.994, 163.081], [163.876, 163.931, 163.645, 163.832], [163.588, 163.761, 163.326, 163.611], [163.792, 163.942, 163.644, 163.771], [163.858, 163.883, 163.293, 163.864], [163.253, 163.733, 157.994, 163.3], [160.179, 160.836, 158.668, 160.183], [157.698, 157.869, 155.256, 157.582], [157.539, 157.952, 157.231, 157.529], [157.735, 157.863, 157.302, 157.692], [157.664, 158.48, 157.599, 157.6], [158.448, 158.561, 156.831, 158.409], [157.9, 159.046, 157.849, 157.891], [159.154, 159.383, 159.004, 159.156], [159.282, 159.456, 158.719, 159.265], [159.318, 159.476, 159.027, 159.328], [159.427, 159.495, 158.637, 159.426], [159.225, 159.402, 158.856, 159.223], [159.329, 159.777, 159.32, 159.34], [159.529, 159.529, 158.052, 159.55], [158.255, 158.958, 158.176, 158.276], [158.906, 159.125, 158.381, 158.883], [158.865, 159.279, 158.715, 158.904], [159.135, 159.485, 159.102, 159.139], [159.225, 159.438, 158.88, 159.223], [159.251, 159.51, 159.116, 159.255], [159.307, 160.052, 159.297, 159.321], [160.099, 160.099, 159.477, 160.122], [159.772, 160.202, 159.639, 159.747], [160.203, 160.383, 158.36, 160.196], [158.9, 158.942, 155.345, 158.923], [155.639, 156.717, 155.323, 155.66], [156.209, 156.246, 154.064, 156.197], [153.847, 154.387, 152.897, 153.855], [153.424, 153.814, 152.985, 153.478], [153.559, 154.622, 153.309, 153.573], [154.46, 154.58, 153.306, 154.482], [153.438, 154.99, 153.378, 153.424], [154.422, 155.223, 154.414, 154.385], [155.287, 155.47, 154.901, 155.266], [156.029, 156.273, 155.34, 156.014], [156.159, 157.998, 156.12, 156.129], [157.009, 157.523, 156.592, 157.046], [157.361, 157.772, 156.827, 157.369], [157.474, 158.393, 157.44, 157.464]]
ENTRY, STOP = 157.92, round(157.92 - 1.15, 2)
def idx(d): return DATES.index(d)
candle_chart(
    "usdjpy-daily-2026-q3-events.svg", OHLC,
    title="USD/JPY daily bars, 2026-07-02 to 2026-09-23, September event days marked",
    y_label="JPY per USD", x_labels=[d[5:] for d in DATES],
    overlays={"ECB fix 157.92": [ENTRY] * len(OHLC), "115-pip stop 156.77": [STOP] * len(OHLC)},
    marks=[(idx("2026-09-04"), "NFP"), (idx("2026-09-11"), "CPI"), (idx("2026-09-16"), "FOMC +25bp"), (idx("2026-09-18"), "BoJ +25bp")],
)
print("wrote 7 figures; spread % =", dict(zip(PAIRS, PCT)), "; ruin % at 10/20/30/50 =", RUIN[9], RUIN[19], RUIN[29], RUIN[49])

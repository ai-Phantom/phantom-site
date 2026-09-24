"""Figures for the Market Structure & Order Flow course.

Every series is a literal below so the figures regenerate with no network access.
Real data: the SPY half-hour volume profile (Yahoo Finance chart API, 5-minute bars,
60 regular sessions 2026-06-30 to 2026-09-23, pulled 2026-09-24) and the 2025 venue
shares (Cboe, "2025 U.S. Equities Year in Review"). Everything else is a clearly
labelled representative dataset built for the lessons, not a real book or tape.
Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

GREEN, BLUE, YELLOW, RED = COLORS[0], COLORS[1], COLORS[2], COLORS[3]

# --- Lesson 1: representative limit order book, five levels each side --------------
# Bids (price: shares) and asks. Mid 187.11, spread $0.02. Representative, not real.
BOOK_LEVELS = ["187.06", "187.07", "187.08", "187.09", "187.10", "187.12", "187.13", "187.14", "187.15", "187.16"]
BOOK_SIZES = [6000, 4500, 3100, 2600, 1200, 900, 1800, 2400, 5200, 7000]
bar_chart(
    "order-book-depth-ladder.svg", BOOK_LEVELS, BOOK_SIZES,
    title="Representative order book: resting shares at each price (bids left, asks right)",
    y_label="shares resting", y_fmt=lambda v: f"{v:,.0f}",
    colors=[GREEN] * 5 + [RED] * 5,
)

# --- Lesson 2: SPY average volume per half-hour slot, 60 sessions (real) --------------
SLOTS = ["09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30"]
SPY_HALF_HOUR_M = [5.32, 3.12, 2.58, 2.53, 1.98, 1.92, 1.69, 1.78, 1.48, 1.88, 2.26, 2.71, 7.94]
bar_chart(
    "spy-volume-by-half-hour-with-auctions.svg", SLOTS, SPY_HALF_HOUR_M,
    title="SPY average volume per half hour, 60 sessions 2026-06-30 to 2026-09-23 (millions)",
    y_label="million shares", y_fmt=lambda v: f"{v:.1f}",
    colors=[YELLOW] + [BLUE] * 11 + [YELLOW],
)

# --- Lesson 3: where a retail order goes under Reg NMS ---------------------------------
flow_diagram(
    "retail-order-routing-path.svg",
    ["You send a market order", "Broker's router", "Wholesaler or exchange", "NBBO check (Rule 611)", "Print and report"],
    title="The path of a retail marketable order",
    notes=[
        "broker chooses the venue, not you (Rule 606 discloses where)",
        "more than 90% of retail marketable orders go to wholesalers (SEC, Dec 2022)",
        "wholesaler fills from inventory; exchange matches on its book",
        "no fill through a protected quote; fee cap $0.003/share (Rule 610)",
        "exchange trades print on the SIP; off-exchange trades via a FINRA TRF",
    ],
)

# --- Lesson 4: 2025 share of consolidated US equity volume by venue type (real) ----------
# Cboe 2025 review: TRF 50.6% of consolidated volume; of TRF, 18.7% ATS and 81.3% principal dealers.
OFF = 50.6
VENUE_LABELS = ["Exchanges 2025", "Off-exch. dealers 2025", "Off-exch. ATS 2025", "Off-exch. total Apr 2023", "Off-exch. total 2025"]
VENUE_SHARES = [round(100 - OFF, 1), round(OFF * 0.813, 1), round(OFF * 0.187, 1), 45.0, OFF]
bar_chart(
    "on-vs-off-exchange-share-2025.svg", VENUE_LABELS, VENUE_SHARES,
    title="Share of US consolidated equity volume, % (Cboe; FINRA TRF data)",
    y_label="% of consolidated volume", y_fmt=lambda v: f"{v:.1f}%",
    colors=[BLUE, RED, RED, YELLOW, YELLOW],
)

# --- Lesson 7: representative session REP-A, cumulative delta vs price by half hour -------
BUY_A = [1.31, 0.82, 0.61, 0.58, 0.44, 0.41, 0.37, 0.40, 0.33, 0.42, 0.49, 0.55, 1.62]
SELL_A = [1.02, 0.71, 0.66, 0.54, 0.47, 0.46, 0.42, 0.41, 0.36, 0.45, 0.58, 0.71, 1.88]
CLOSE_A = [187.42, 187.96, 188.11, 188.05, 188.20, 188.14, 188.09, 188.17, 188.12, 188.02, 187.88, 187.61, 187.24]
OPEN_A = 187.10
delta_a = [round(b - s, 2) for b, s in zip(BUY_A, SELL_A)]
cvd_a, run = [], 0.0
for d in delta_a:
    run = round(run + d, 2); cvd_a.append(run)
line_chart(
    "cumulative-delta-vs-price-rep-a.svg",
    {"CVD, 10k shares": [round(c * 100) for c in cvd_a],
     "price change from open, cents": [round((c - OPEN_A) * 100) for c in CLOSE_A]},
    title="Representative session REP-A: cumulative delta and price, by half hour",
    y_label="10k shares / cents", x_labels=SLOTS,
    annotations=[(11, "CVD turns negative, price still +51c")],
    hlines=[(0, "zero")],
)

# --- Lesson 10: square-root impact model, cost vs order size as % of ADV ---------------
# cost_bps = sigma_daily_bps * sqrt(Q / ADV); sigma 1.5% and 3.0%
SIZES = [0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
import math
line_chart(
    "market-impact-vs-order-size.svg",
    {"daily vol 1.5%": [round(150 * math.sqrt(q / 100), 1) for q in SIZES],
     "daily vol 3.0%": [round(300 * math.sqrt(q / 100), 1) for q in SIZES]},
    title="Square-root impact model: expected cost vs order size (% of average daily volume)",
    y_label="impact, basis points", x_labels=[f"{s}%" for s in SIZES],
    y_fmt=lambda v: f"{v:.0f}",
)

# --- Lesson 11: the spoofing cycle (Coscia pattern as described by the CFTC, 2013) --------
flow_diagram(
    "spoofing-cycle.svg",
    ["Rest a small genuine buy", "Layer large sells above the ask", "Book looks heavy; sellers hit the bid", "Small buy fills; cancel the layers", "Mirror it to sell out"],
    title="A spoofing cycle: what the book shows versus what the trader wants",
    notes=[
        "the order the trader wants filled",
        "several large orders, never meant to trade",
        "other participants react to displayed size",
        "cancellation within milliseconds of the fill",
        "repeat on the other side to exit at a profit",
    ],
)

print("wrote 7 figures")

"""Figures for the Crypto: Spot, Perpetuals & Funding course.

Every number below is a literal copied from the course's cited sources so the
figures regenerate with no network access:
  * BTC weekly candles: Yahoo Finance chart API, BTC-USD daily bars
    (https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=5y&interval=1d),
    aggregated Monday-to-Sunday, 2021-11-01 to 2022-11-28.
  * Funding: Deribit public API get_funding_rate_history, BTC-PERPETUAL, hourly rows
    2026-06-26 to 2026-09-24, averaged per UTC day (interest_8h field).
  * Realised volatility: computed from Yahoo daily closes (BTC-USD, SPY), see lesson 9.
  * Liquidation distances, cash-and-carry legs, AMM curve, capstone P&L: from the
    worked examples in lessons 7, 8, 10 and 13 (Deribit snapshot 2026-09-24 07:28 UTC,
    BitMEX XBTUSD margin parameters, Kraken fee schedule).
Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

# --- Figure 1 (lesson 12): BTC weekly candles, 2021-11-08 peak to 2022-11-21 trough ---
WEEK_START = ['2021-11-01', '2021-11-08', '2021-11-15', '2021-11-22', '2021-11-29', '2021-12-06', '2021-12-13', '2021-12-20', '2021-12-27', '2022-01-03', '2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07', '2022-02-14', '2022-02-21', '2022-02-28', '2022-03-07', '2022-03-14', '2022-03-21', '2022-03-28', '2022-04-04', '2022-04-11', '2022-04-18', '2022-04-25', '2022-05-02', '2022-05-09', '2022-05-16', '2022-05-23', '2022-05-30', '2022-06-06', '2022-06-13', '2022-06-20', '2022-06-27', '2022-07-04', '2022-07-11', '2022-07-18', '2022-07-25', '2022-08-01', '2022-08-08', '2022-08-15', '2022-08-22', '2022-08-29', '2022-09-05', '2022-09-12', '2022-09-19', '2022-09-26', '2022-10-03', '2022-10-10', '2022-10-17', '2022-10-24', '2022-10-31', '2022-11-07', '2022-11-14', '2022-11-21', '2022-11-28']
WEEK_OHLC = [(61320, 64243, 59695, 63327), (63344, 68790, 62334, 65467), (65521, 66282, 55705, 58730), (58707, 59368, 53570, 57248), (57292, 59113, 42875, 49369), (49413, 51935, 46942, 50098), (50115, 50205, 45598, 46707), (46707, 51814, 45580, 50810), (50803, 51956, 45820, 47345), (47344, 47511, 40672, 41912), (41910, 44278, 39797, 43114), (43118, 43413, 34349, 36277), (36276, 38825, 33184, 37918), (37920, 42501, 36376, 42412), (42407, 45661, 41748, 42198), (42157, 44667, 38113, 38431), (38423, 40005, 34459, 37710), (37706, 45078, 37518, 38420), (38429, 42466, 37260, 37850), (37846, 42317, 37681, 41248), (41246, 46828, 40668, 46820), (46822, 48087, 44403, 46454), (46445, 47106, 42021, 42208), (42201, 42425, 39373, 39717), (39721, 42894, 38696, 39469), (39473, 40714, 37586, 38469), (38472, 39903, 33879, 34059), (34060, 34222, 26350, 31305), (31304, 31305, 28709, 30324), (30309, 30591, 28262, 29446), (29443, 32250, 29304, 29907), (29910, 31693, 26763, 26763), (26738, 26796, 17709, 20553), (20553, 21784, 19689, 21027), (21028, 21478, 18730, 19297), (19297, 22315, 19063, 20860), (20856, 21601, 19000, 20779), (20782, 24197, 20782, 22609), (22607, 24573, 20777, 23337), (23337, 23579, 22486, 23176), (23180, 24975, 22772, 24319), (24318, 25136, 20857, 21534), (21531, 21805, 19617, 19617), (19615, 20543, 19601, 19987), (19989, 21771, 18644, 21769), (21770, 22674, 19387, 19420), (19419, 19675, 18290, 18802), (18804, 20338, 18553, 19044), (19044, 20408, 19025, 19446), (19446, 19889, 18320, 19268), (19269, 19667, 18771, 19567), (19568, 20988, 19206, 20636), (20634, 21447, 20086, 20926), (20925, 21053, 15683, 16353), (16352, 17109, 15873, 16292), (16291, 16771, 15599, 16445), (16440, 17197, 16055, 17130)]
candle_chart(
    "btc-2021-2022-drawdown-weekly.svg", WEEK_OHLC,
    title="BTC-USD weekly candles, Nov 2021 to Nov 2022: close-to-close drawdown of 76.6%",
    y_label="$", x_labels=[d[2:7] for d in WEEK_START],
    marks=[(1, "peak close 67,567 (2021-11-08)"), (55, "trough close 15,787 (2022-11-21)")],
)

# --- Figure 2 (lesson 6): Deribit BTC-PERPETUAL funding, daily average of the 8-hour rate, 90 days ---
FUND_DATES = ['2026-06-26', '2026-06-27', '2026-06-28', '2026-06-29', '2026-06-30', '2026-07-01', '2026-07-02', '2026-07-03', '2026-07-04', '2026-07-05', '2026-07-06', '2026-07-07', '2026-07-08', '2026-07-09', '2026-07-10', '2026-07-11', '2026-07-12', '2026-07-13', '2026-07-14', '2026-07-15', '2026-07-16', '2026-07-17', '2026-07-18', '2026-07-19', '2026-07-20', '2026-07-21', '2026-07-22', '2026-07-23', '2026-07-24', '2026-07-25', '2026-07-26', '2026-07-27', '2026-07-28', '2026-07-29', '2026-07-30', '2026-07-31', '2026-08-01', '2026-08-02', '2026-08-03', '2026-08-04', '2026-08-05', '2026-08-06', '2026-08-07', '2026-08-08', '2026-08-09', '2026-08-10', '2026-08-11', '2026-08-12', '2026-08-13', '2026-08-14', '2026-08-15', '2026-08-16', '2026-08-17', '2026-08-18', '2026-08-19', '2026-08-20', '2026-08-21', '2026-08-22', '2026-08-23', '2026-08-24', '2026-08-25', '2026-08-26', '2026-08-27', '2026-08-28', '2026-08-29', '2026-08-30', '2026-08-31', '2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04', '2026-09-05', '2026-09-06', '2026-09-07', '2026-09-08', '2026-09-09', '2026-09-10', '2026-09-11', '2026-09-12', '2026-09-13', '2026-09-14', '2026-09-15', '2026-09-16', '2026-09-17', '2026-09-18', '2026-09-19', '2026-09-20', '2026-09-21', '2026-09-22', '2026-09-23', '2026-09-24']
FUND_8H_PCT = [0.0044, 0.0028, 0.0005, 0.004, 0.0022, 0.0011, 0.0019, 0.0038, 0.0001, 0.0011, 0.009, 0.0053, 0.0034, 0.0046, 0.008, 0.0066, 0.0033, 0.0067, 0.0016, 0.0017, 0.0036, 0.0012, 0.0016, 0.0073, 0.0048, 0.0049, 0.0077, 0.001, 0.0016, 0.0008, 0.001, 0.0068, 0.002, 0.007, 0.011, 0.003, 0.0024, 0.002, 0.0052, 0.0035, 0.0015, 0.0014, 0.0005, 0.0001, 0.0, 0.0008, 0.0024, 0.0061, 0.0066, 0.0072, 0.0014, 0.0001, 0.0037, 0.001, 0.0032, 0.0101, 0.0057, 0.0091, 0.0067, 0.0059, 0.0021, 0.0035, 0.0056, 0.0007, 0.0016, 0.0016, 0.0087, 0.0068, 0.006, 0.0037, 0.0014, -0.0027, -0.0, 0.0002, 0.0018, 0.0061, 0.0008, 0.0013, 0.0, 0.0015, 0.0005, 0.002, 0.0056, 0.0066, 0.002, 0.0083, 0.0088, 0.0189, 0.0119, 0.0093, 0.0038]
line_chart(
    "deribit-btc-funding-90d.svg", {"8-hour funding rate, daily average (%)": FUND_8H_PCT},
    title="Deribit BTC-PERPETUAL funding, 2026-06-26 to 2026-09-24 (8h rate, daily mean)",
    y_label="% per 8 hours", x_labels=[d[5:] for d in FUND_DATES],
    y_fmt=lambda v: f"{v:.3f}%", hlines=[(0.0, "zero: longs and shorts pay nothing"), (0.01, "0.01% = the 'interest' floor many venues default to")],
    annotations=[(87, "2026-09-21: 0.0189% (20.7% annualised)")],
)

# --- Figure 3 (lesson 8): distance to liquidation vs leverage, maintenance margin 0.5% (BitMEX XBTUSD maintMargin) ---
LEV = [2, 3, 5, 10, 20, 25, 50, 100]
DIST = [round((1 / L - 0.005) * 100, 2) for L in LEV]      # 49.5 ... 0.5
line_chart(
    "liquidation-distance-vs-leverage.svg", {"adverse move that liquidates (%)": DIST},
    title="How far price must move against you before liquidation (isolated, 0.5% maintenance)",
    y_label="% move", x_labels=[f"{L}x" for L in LEV], y_fmt=lambda v: f"{v:.1f}%",
    hlines=[(2.45, "one daily standard deviation, BTC 2026 YTD (2.45%)")],
    annotations=[(7, "100x: 0.5%, one fifth of a normal day"), (1, "3x: 32.8%")],
)

# --- Figure 4 (lesson 7): the cash-and-carry legs ---
flow_diagram(
    "cash-and-carry-legs.svg",
    ["Buy 1 BTC spot", "Sell 1 BTC dated future (or perp)", "Hold to expiry", "Future settles at index", "Sell spot, compare to T-bill"],
    title="Cash-and-carry, Deribit snapshot 2026-09-24 07:28 UTC",
    notes=[
        "index 84,256.40; pay maker or taker fee on the spot venue",
        "BTC-30OCT26 mark 84,719.61: basis $463.21 = 0.55% for 36 days; the perp instead pays 8h funding",
        "price risk is hedged; you carry venue risk on both legs and margin risk on the short",
        "36 days later the future cash-settles to the index; basis is fully captured",
        "gross 5.57% annualised vs 4.03% 13-week T-bill; fees decide the rest",
    ],
)

# --- Figure 5 (lesson 9): realised volatility by calendar year, BTC vs SPY ---
YEARS = ["2022", "2023", "2024", "2025", "2026 YTD"]
BTC_VOL = [64.1, 43.3, 53.0, 41.9, 46.8]
SPY_VOL = [24.3, 13.2, 12.6, 19.3, 13.3]
labels, values, colors = [], [], []
for y, b, s in zip(YEARS, BTC_VOL, SPY_VOL):
    labels += [f"BTC {y}", f"SPY {y}"]; values += [b, s]; colors += [COLORS[2], COLORS[1]]
bar_chart(
    "realised-vol-btc-vs-spy.svg", labels, values,
    title="Annualised realised volatility of daily closes: BTC-USD (365d) vs SPY (252d), Yahoo Finance",
    y_label="% per year", y_fmt=lambda v: f"{v:.0f}%", colors=colors,
)

# --- Figure 6 (lesson 10): constant-product AMM price impact, pool of 1,000 BTC / 84,256,400 USDC, 0.30% fee ---
TRADE_USD = [10_000, 100_000, 500_000, 1_000_000, 2_000_000, 5_000_000, 10_000_000]
IMPACT = [0.313, 0.420, 0.894, 1.488, 2.675, 6.235, 12.169]
line_chart(
    "amm-price-impact.svg", {"average price paid vs pool price (%, incl. 0.30% fee)": IMPACT},
    title="Price impact of buying BTC from a 1,000 BTC / 84.26M USDC constant-product pool",
    y_label="% above 84,256.40", x_labels=["$10k", "$100k", "$500k", "$1M", "$2M", "$5M", "$10M"],
    y_fmt=lambda v: f"{v:.1f}%", annotations=[(3, "$1M buys 11.69 BTC at avg 85,510")],
)

# --- Figure 7 (capstone): P&L decomposition of the 1 BTC / BTC-30OCT26 carry, 36 days ---
bar_chart(
    "capstone-carry-pnl.svg",
    ["Basis captured", "Spot fees (0.15% x2)", "Future fee (0.035%)", "Net carry", "T-bill on $84,256, 36d"],
    [463.21, -252.77, -29.65, 180.79, 334.74],
    title="Capstone: 1 BTC cash-and-carry vs BTC-30OCT26, 2026-09-24 snapshot, dollars",
    y_label="$", y_fmt=lambda v: f"{v:+,.0f}",
    colors=[COLORS[0], COLORS[3], COLORS[3], COLORS[2], COLORS[1]],
)
print("wrote 7 figures")

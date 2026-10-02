import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

# Every number below is produced by the lessons' worked examples.
# Price data: Yahoo Finance chart API, SPY daily bars, period1=1104537600 (2005-01-01 UTC)
# period2=1790726400 (2026-09-30 UTC), interval=1d, dataGranularity verified "1d", 5,469 rows
# 2005-01-03 .. 2026-09-29; tests run on 2010-01-04 .. 2025-12-31 with dividend-adjusted OHLC.
# Second source for lesson 2: Cboe S&P 500 index daily history CSV (SPX_History.csv).
# Cash: Yahoo ^IRX (13-week T-bill discount yield). Fetched 2026-09-30.
HERE = Path(__file__).resolve().parent


def gate_stack():
    flow_diagram(HERE / "gate-stack.svg",
                 ["D0-D6 Data gates", "P Trade definition", "G1-G2 Geometry and cash", "G3 Random-entry null",
                  "G4-G6 Power, eras, holdout", "G7 Benchmark and replication", "Forward record"],
                 title="The gate stack: data first, inference after, a forward record last",
                 notes=["second source, adjustments, empty bars, seams",
                        "R denominator, overlap, timestamps",
                        "win rate vs breakeven, beats T-bills over the hold",
                        "percentile vs matched random entry",
                        "required n, edge repeats per era, holdout sign",
                        "buy-and-hold, fresh pre-registered universe",
                        "entry, exit fill, R, stop condition"])


def vendor_returns():
    # Lesson 2: SPY daily return in bps on three dates, Yahoo raw close vs Yahoo adjusted close vs Cboe SPX
    labels = ["raw 12-16-16", "adj 12-16-16", "SPX 12-16-16",
              "raw 12-20-24", "adj 12-20-24", "SPX 12-20-24",
              "raw 12-23-24", "adj 12-23-24", "SPX 12-23-24"]
    values = [-78.0, -19.6, -17.5, 86.2, 120.1, 108.7, 59.9, 59.9, 72.9]
    colors = [COLORS[2], COLORS[0], COLORS[1]] * 3
    bar_chart(HERE / "vendor-returns-ex-dividend.svg", labels, values,
              title="SPY daily return, bps: Yahoo raw close vs Yahoo adjusted close vs Cboe S&P 500 index",
              y_label="bps", y_fmt=lambda v: f"{v:+.0f}", colors=colors)


def collapsed_denominator():
    # Lesson 4: 3-bar pullback on SPY 2010-2025, stop = lowest low of the three bars, 10-bar time exit.
    # Top ten trades by R; label = stop distance as % of entry price.
    risk_pct = [0.025, 0.120, 0.290, 0.099, 0.355, 0.358, 0.289, 0.284, 0.334, 0.103]
    r = [152.6, 69.4, 32.2, 30.0, 20.4, 20.4, 14.6, 10.6, 10.2, 10.1]
    labels = [f"{p:.3f}%" for p in risk_pct]
    colors = [COLORS[3] if p < 0.1 else COLORS[0] for p in risk_pct]
    bar_chart(HERE / "collapsed-denominator-top-trades.svg", labels, r,
              title="Ten largest trades in R, labelled by stop distance as % of price (SPY 3-bar pullback, 2010-2025)",
              y_label="R multiple", y_fmt=lambda v: f"{v:.1f}", colors=colors)


def null_distribution():
    # Lesson 5: Donchian 20/10 long on SPY 2010-2025, 71 trades, mean +1.4251% per trade.
    # 2,000 random-entry draws matched on trade count and holding periods; histogram of the mean return per draw.
    edges = [-0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2]
    counts = [3, 8, 18, 36, 56, 115, 141, 190, 251, 288, 255, 222, 180, 108, 66, 39, 17, 4, 3]
    labels = [f"{e:.1f}" for e in edges]
    colors = [COLORS[3] if e == 1.4 else COLORS[1] for e in edges]
    bar_chart(HERE / "null-distribution-donchian.svg", labels, counts,
              title="Random-entry null, 2,000 draws: mean % per trade. Red bin holds the Donchian rule (+1.43%, 42nd pct)",
              y_label="draws", y_fmt=lambda v: f"{v:.0f}", colors=colors)


MONTHS = [f"{y}-{m:02d}" for y in range(2010, 2026) for m in range(1, 13)]
X = [m[:4] if m.endswith("-01") else "" for m in MONTHS]
STRAT = [1.0, 1.0001, 1.0002, 1.0021, 0.9981, 0.9399, 0.9781, 0.964, 0.9641, 0.9642, 0.964, 0.9642, 0.9643, 0.979, 1.0101, 0.9946, 1.0113, 0.9885, 0.9784, 0.9201, 0.9416, 0.9968, 0.9801, 0.9801, 0.9801, 0.9802, 1.0129, 1.004, 0.9679, 0.9963, 1.0395, 1.0485, 1.0701, 1.0813, 1.1001, 1.1183, 1.1465, 1.1466, 1.1466, 1.1467, 1.1467, 1.1881, 1.1881, 1.1887, 1.1809, 1.1885, 1.1886, 1.2006, 1.1947, 1.2313, 1.2466, 1.2373, 1.2374, 1.2535, 1.2284, 1.2323, 1.2255, 1.238, 1.238, 1.2582, 1.2625, 1.296, 1.2871, 1.2865, 1.3131, 1.3337, 1.3411, 1.309, 1.2998, 1.3025, 1.3054, 1.344, 1.2546, 1.283, 1.2833, 1.2829, 1.2957, 1.3643, 1.3646, 1.3824, 1.3888, 1.3885, 1.3984, 1.3983, 1.4171, 1.4177, 1.4279, 1.4262, 1.4481, 1.4479, 1.4491, 1.4652, 1.4663, 1.4677, 1.4757, 1.4772, 1.4789, 1.4278, 1.4148, 1.4026, 1.4133, 1.3923, 1.3967, 1.4121, 1.4172, 1.3565, 1.3718, 1.3213, 1.3239, 1.3263, 1.3375, 1.3401, 1.3303, 1.3688, 1.3706, 1.3447, 1.339, 1.3458, 1.3474, 1.3707, 1.3632, 1.2531, 1.1479, 1.148, 1.1892, 1.2318, 1.2319, 1.232, 1.2687, 1.2804, 1.3465, 1.3655, 1.3491, 1.3731, 1.3731, 1.3731, 1.406, 1.4323, 1.4446, 1.4698, 1.4934, 1.5127, 1.5008, 1.542, 1.5253, 1.5491, 1.5704, 1.5325, 1.5392, 1.4844, 1.4973, 1.4574, 1.4191, 1.4209, 1.4659, 1.4862, 1.5355, 1.5278, 1.5515, 1.5924, 1.6606, 1.6677, 1.6746, 1.6709, 1.6335, 1.6211, 1.6445, 1.6513, 1.707, 1.714, 1.7212, 1.7459, 1.7686, 1.7758, 1.7568, 1.8145, 1.8658, 1.8815, 1.9833, 2.0438, 2.081, 2.0648, 2.0845, 2.0374, 2.0582, 2.0651, 2.0718, 2.0685, 2.0752, 2.1033, 2.1349, 2.1878]
BH = [0.9476, 0.9771, 1.0366, 1.0527, 0.969, 0.9189, 0.9817, 0.9375, 1.0215, 1.0605, 1.0605, 1.1314, 1.1577, 1.198, 1.1981, 1.2328, 1.219, 1.1984, 1.1744, 1.1099, 1.0328, 1.1455, 1.1409, 1.1528, 1.2063, 1.2586, 1.2991, 1.2904, 1.2129, 1.2622, 1.2771, 1.3091, 1.3423, 1.3179, 1.3253, 1.3372, 1.4056, 1.4235, 1.4776, 1.506, 1.5415, 1.521, 1.5996, 1.5516, 1.6007, 1.6748, 1.7244, 1.7692, 1.7068, 1.7845, 1.7993, 1.8118, 1.8538, 1.8921, 1.8667, 1.9404, 1.9136, 1.9586, 2.0125, 2.0074, 1.9479, 2.0574, 2.025, 2.045, 2.0712, 2.0292, 2.075, 1.9485, 1.8988, 2.0603, 2.0679, 2.0321, 1.931, 1.9294, 2.0591, 2.0673, 2.1024, 2.1097, 2.1867, 2.1893, 2.1894, 2.1515, 2.2307, 2.2759, 2.3167, 2.4077, 2.4107, 2.4346, 2.469, 2.4847, 2.5358, 2.5432, 2.5944, 2.6556, 2.7368, 2.7699, 2.9261, 2.8197, 2.7424, 2.7565, 2.8236, 2.8398, 2.945, 3.039, 3.0571, 2.8458, 2.8986, 2.6434, 2.855, 2.9476, 3.0009, 3.1235, 2.9243, 3.1278, 3.1751, 3.122, 3.1827, 3.2531, 3.3708, 3.4687, 3.4673, 3.1929, 2.7942, 3.149, 3.299, 3.3575, 3.5552, 3.8034, 3.661, 3.5697, 3.958, 4.1046, 4.0628, 4.1758, 4.3653, 4.5963, 4.6265, 4.7303, 4.8457, 4.9899, 4.7574, 5.0912, 5.0503, 5.2838, 5.0052, 4.8574, 5.04, 4.5977, 4.608, 4.2281, 4.6174, 4.429, 4.0196, 4.3463, 4.5879, 4.3235, 4.5954, 4.4798, 4.6459, 4.7202, 4.7419, 5.0492, 5.2145, 5.1298, 4.8864, 4.7803, 5.217, 5.4552, 5.5421, 5.8313, 6.022, 5.7792, 6.0715, 6.2857, 6.3618, 6.5105, 6.6472, 6.5879, 6.9807, 6.8128, 6.9958, 6.9069, 6.5221, 6.4655, 6.8719, 7.225, 7.3914, 7.5431, 7.8118, 7.998, 8.0136, 8.02]
CASH = [1.0, 1.0001, 1.0002, 1.0004, 1.0005, 1.0006, 1.0007, 1.0008, 1.0009, 1.0011, 1.0012, 1.0013, 1.0014, 1.0015, 1.0016, 1.0016, 1.0016, 1.0017, 1.0017, 1.0017, 1.0017, 1.0017, 1.0017, 1.0017, 1.0017, 1.0018, 1.0019, 1.0019, 1.002, 1.0021, 1.0021, 1.0022, 1.0023, 1.0024, 1.0024, 1.0025, 1.0025, 1.0026, 1.0027, 1.0027, 1.0028, 1.0028, 1.0028, 1.0028, 1.0029, 1.0029, 1.0029, 1.003, 1.003, 1.003, 1.0031, 1.0031, 1.0031, 1.0031, 1.0031, 1.0032, 1.0032, 1.0032, 1.0032, 1.0032, 1.0032, 1.0032, 1.0032, 1.0033, 1.0033, 1.0033, 1.0033, 1.0033, 1.0033, 1.0034, 1.0034, 1.0036, 1.0038, 1.004, 1.0043, 1.0045, 1.0047, 1.0049, 1.0051, 1.0054, 1.0056, 1.0059, 1.0062, 1.0066, 1.007, 1.0074, 1.0081, 1.0087, 1.0095, 1.0103, 1.0112, 1.0121, 1.0129, 1.0139, 1.0149, 1.0159, 1.0171, 1.0183, 1.0197, 1.0212, 1.0229, 1.0245, 1.0261, 1.028, 1.0296, 1.0317, 1.0337, 1.0356, 1.0376, 1.0395, 1.0415, 1.0436, 1.0457, 1.0475, 1.0494, 1.0512, 1.0528, 1.0543, 1.0556, 1.0569, 1.0583, 1.0595, 1.0597, 1.0598, 1.0599, 1.06, 1.0601, 1.0602, 1.0603, 1.0604, 1.0604, 1.0605, 1.0606, 1.0606, 1.0606, 1.0606, 1.0606, 1.0606, 1.0607, 1.0607, 1.0607, 1.0608, 1.0608, 1.0609, 1.061, 1.0612, 1.0616, 1.0622, 1.0631, 1.0643, 1.0662, 1.0687, 1.0714, 1.0747, 1.0784, 1.0822, 1.086, 1.0898, 1.0945, 1.0985, 1.1034, 1.1081, 1.1127, 1.1181, 1.1228, 1.128, 1.133, 1.1377, 1.1427, 1.1474, 1.1522, 1.1574, 1.1628, 1.1674, 1.1727, 1.1778, 1.1822, 1.1871, 1.1913, 1.1955, 1.1995, 1.2033, 1.2075, 1.2117, 1.216, 1.2201, 1.2246, 1.2288, 1.2328, 1.2371, 1.2406, 1.2445]


def equity_vs_benchmarks():
    # Lesson 7: RSI(2)<10 / exit close>SMA5 on SPY, 5 bps per side, growth of $1 at month-ends 2010-2025
    line_chart(HERE / "rsi2-vs-buy-and-hold-and-cash.svg",
               {"RSI(2) rule, 5 bps/side": STRAT, "SPY buy-and-hold": BH, "13-week T-bill": CASH},
               title="Growth of $1, 2010-2025: RSI(2) rule (+119%) vs SPY buy-and-hold (+702%) vs T-bills (+24%)",
               y_label="growth of $1", x_labels=X)


def per_era():
    # Lesson 8: RSI(2) on SPY, percentile against a per-era random-entry null (2,000 draws each), plus pooled
    labels = ["2010-13", "2014-17", "2018-21", "2022-25", "pooled"]
    values = [72.9, 84.9, 34.8, 99.1, 95.0]
    colors = [COLORS[0] if v >= 95 else COLORS[3] for v in values]
    bar_chart(HERE / "per-era-percentiles.svg", labels, values,
              title="RSI(2) on SPY: percentile vs random entry, scored per era and pooled (bar = 95th)",
              y_label="percentile", y_fmt=lambda v: f"{v:.1f}", colors=colors)


def spread_by_year():
    # Lesson 11: one-cent round-trip spread on SPY as bps of the year's median close (Yahoo raw close)
    years = [str(y) for y in range(2010, 2026)]
    bps = [0.879, 0.779, 0.722, 0.605, 0.516, 0.481, 0.475, 0.411, 0.365, 0.343, 0.306, 0.233, 0.248, 0.233, 0.184, 0.161]
    bar_chart(HERE / "spread-in-bps-by-year.svg", years, bps,
              title="A one-cent round trip on SPY in bps of the year's median close, 2010-2025",
              y_label="bps", y_fmt=lambda v: f"{v:.2f}")


if __name__ == "__main__":
    gate_stack(); vendor_returns(); collapsed_denominator(); null_distribution()
    equity_vs_benchmarks(); per_era(); spread_by_year()
    print("wrote", sorted(p.name for p in HERE.glob("*.svg")))

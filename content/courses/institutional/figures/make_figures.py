import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

OUT = Path(__file__).resolve().parent

# Lesson 2 — the IPS process as a pipeline. Steps paraphrase the CFA Institute
# IPS elements (objectives, constraints, policy, implementation, review).
flow_diagram(
    OUT / "ips-process.svg",
    ["Liability and purpose", "Return objective", "Risk and constraints", "Policy allocation", "Implement and rebalance", "Measure and review"],
    title="The investment policy statement: what outranks any trade",
    notes=[
        "who is paid, when, how much",
        "spend + inflation (Harvard: 5% + 3% = 8%)",
        "drawdown, liquidity, horizon, tax, legal",
        "targets, ranges, benchmarks",
        "rules, not opinions",
        "vs benchmark; amend the IPS, not the mood",
    ],
)

# Lesson 4 — Yale's target allocation for fiscal 2021 (The Yale Endowment 2021,
# Yale Investments Office). Percent of endowment.
yale_labels = ["Absolute return", "Venture capital", "Buyouts", "Foreign equity", "Real estate", "Bonds & cash", "Natural res.", "US equity"]
yale_targets = [23.5, 23.5, 17.5, 11.75, 9.5, 7.5, 4.5, 2.25]
bar_chart(
    OUT / "yale-target-allocation.svg",
    yale_labels, yale_targets,
    title="Yale endowment target allocation, fiscal 2021 (% of endowment)",
    y_label="% of endowment", y_fmt=lambda v: f"{v:g}%",
    colors=["#4d9fff", "#7eff5c", "#7eff5c", "#f5c842", "#a78bfa", "#8a948e", "#ff9f43", "#f5c842"],
)

# Lesson 6 — growth of 100 in each Fama-French factor, annual data 2014-2025
# (Kenneth R. French Data Library, F-F_Research_Data_Factors and
# F-F_Momentum_Factor, annual rows). Values are compounded from the published
# annual factor returns in the lesson's table.
years = [str(y) for y in range(2013, 2026)]
factors = {
    "Mkt-RF": [100, 111.7, 112.0, 126.9, 154.2, 143.7, 184.5, 228.1, 282.5, 222.3, 270.6, 324.1, 367.2],
    "SMB (size)": [100, 92.3, 88.8, 94.6, 89.7, 86.9, 81.2, 92.2, 88.7, 82.5, 79.6, 70.6, 63.0],
    "HML (value)": [100, 98.2, 88.8, 109.1, 94.5, 85.4, 76.5, 40.6, 51.0, 64.1, 55.1, 50.5, 54.9],
    "MOM (momentum)": [100, 100.8, 121.2, 95.5, 100.1, 109.6, 107.3, 115.2, 112.5, 130.4, 98.7, 118.2, 115.5],
}
line_chart(
    OUT / "factor-cumulative-2014-2025.svg", factors,
    title="Fama-French factors, growth of 100, end-2013 to end-2025 (annual data)",
    y_label="growth of 100", x_labels=years,
    annotations=[(7, "HML 2020: -46.9%")],
    hlines=[(100, "start")],
)

# Lesson 7 — $500,000 compounding for 10 years at 8% gross under four fee
# regimes. Rates: index 0.05% expense; 2-and-20 with no hurdle nets
# (8% - 2%) x 0.8 = 4.8%; 2-and-20 with a 5% hurdle nets 6% - 0.2 x (6% - 5%) = 5.8%.
fee_years = [str(y) for y in range(0, 11)]
fee_paths = {
    "Gross 8%": [500000, 540000, 583200, 629856, 680244, 734664, 793437, 856912, 925465, 999502, 1079462],
    "Index fund 0.05%": [500000, 539750, 582660, 628982, 678986, 732965, 791236, 854139, 922043, 995345, 1074475],
    "2-and-20, 5% hurdle": [500000, 529000, 559682, 592144, 626488, 662824, 701268, 741942, 784974, 830503, 878672],
    "2-and-20, no hurdle": [500000, 524000, 549152, 575511, 603136, 632086, 662427, 694223, 727546, 762468, 799066],
}
line_chart(
    OUT / "fee-drag-2-and-20.svg", fee_paths,
    title="$500,000 at 8% gross for 10 years: what the fee structure keeps",
    y_label="$", x_labels=fee_years, y_fmt=lambda v: f"{v/1000:,.0f}k",
)

# Lesson 8 — 2022 total returns of six ETFs, computed from Yahoo Finance
# adjusted closes 2021-12-31 to 2022-12-30 (251 trading days each).
bar_chart(
    OUT / "asset-returns-2022.svg",
    ["SPY", "IWM", "EFA", "VNQ", "AGG", "TLT"],
    [-18.18, -20.48, -14.39, -26.25, -13.02, -31.23],
    title="2022 total returns: stocks, bonds and real estate fell together",
    y_label="% total return", y_fmt=lambda v: f"{v:+.1f}%",
)

# Lesson 9 — a 60/40 US large cap / US aggregate bond portfolio: dollar weight
# vs share of portfolio volatility, using J.P. Morgan 2025 LTCMA inputs
# (vol 16.26% and 4.52%, correlation 0.26). Portfolio vol 10.37%.
bar_chart(
    OUT / "risk-budget-vs-dollars.svg",
    ["Equity: $ weight", "Equity: risk share", "Bonds: $ weight", "Bonds: risk share"],
    [60, 92.7, 40, 7.3],
    title="60/40 in dollars is 93/7 in risk",
    y_label="%", y_fmt=lambda v: f"{v:g}%",
    colors=["#4d9fff", "#ff4d6a", "#4d9fff", "#ff4d6a"],
)

# Lesson 13 — the capstone reference allocation for the $500,000 account and
# each sleeve's share of portfolio volatility (computed in the capstone).
bar_chart(
    OUT / "capstone-allocation.svg",
    ["US LC wt", "US LC risk", "EAFE wt", "EAFE risk", "EM wt", "EM risk", "REIT wt", "REIT risk", "Agg wt", "Agg risk", "TIPS wt", "TIPS risk", "Cash wt", "Cash risk"],
    [40, 57.7, 15, 22.7, 5, 8.0, 5, 6.4, 25, 4.2, 5, 1.1, 5, 0.0],
    title="Capstone reference allocation: dollar weight vs share of volatility (%)",
    y_label="%", y_fmt=lambda v: f"{v:g}",
    colors=["#4d9fff", "#ff4d6a"] * 7,
)

print("wrote", sorted(p.name for p in OUT.glob("*.svg")))

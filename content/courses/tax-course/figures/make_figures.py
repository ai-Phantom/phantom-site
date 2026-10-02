"""Figures for the Tax Strategy for Traders course.

Every number below is a literal copied from the worked examples in the lessons,
so the figures regenerate with no network access:
  * Figure 1 (lesson 1): after-tax proceeds of a $10,000 gain by 2025 single-filer
    bracket, Rev. Proc. 2024-40 rate tables and section 1(h) thresholds; 3.8% NIIT
    (IRC section 1411) added for the 32%, 35% and 37% rows, where a single filer taking
    the 2025 standard deduction necessarily has MAGI above $200,000.
  * Figure 2 (lesson 3): the 61-day wash-sale window around the 2025-04-04 SPY sale,
    IRC section 1091(a); prices are Yahoo Finance daily closes.
  * Figure 3 (lesson 4): the harvesting decision flow built from Pub. 550, Wash Sales.
  * Figure 4 (lesson 5): ordinary bracket rate versus the 60/40 blended rate under
    IRC section 1256(a)(3), 2025 single-filer brackets, no NIIT.
  * Figure 5 (lesson 9): the Form 1040-ES (2026) required-annual-payment decision,
    IRC section 6654(d)(1).
  * Figure 6 (lesson 13): reported gain or loss per capstone trade after the
    wash-sale adjustment, tax year 2025, Yahoo Finance daily closes.
Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

# --- Figure 1 (lesson 1): after-tax proceeds of a $10,000 gain, short-term vs long-term, 2025 single ---
BRACKETS = ["10%", "12%", "22%", "24%", "32%", "35%", "37%"]
AFTER_TAX_ST = [9000, 8800, 7800, 7600, 6420, 6120, 5920]
AFTER_TAX_LT = [10000, 10000, 8500, 8500, 8120, 8120, 7620]
labels, values, colors = [], [], []
for b, st, lt in zip(BRACKETS, AFTER_TAX_ST, AFTER_TAX_LT):
    labels += [f"{b} ST", f"{b} LT"]; values += [st, lt]; colors += [COLORS[3], COLORS[0]]
bar_chart(
    "after-tax-10000-gain-by-bracket.svg", labels, values,
    title="What is left of a $10,000 gain after federal tax, by 2025 single-filer bracket",
    y_label="$ after tax (NIIT 3.8% included from the 32% bracket up)", colors=colors,
    y_fmt=lambda v: f"{v:,.0f}",
)

# --- Figure 2 (lesson 3): the 61-day wash-sale window around the 2025-04-04 SPY sale ---
flow_diagram(
    "wash-sale-61-day-window.svg",
    ["2025-03-05: window opens", "2025-04-04: sell 100 SPY at 505.28", "2025-04-24: buy 100 SPY at 546.69", "2025-05-04: window closes", "2025-12-01: sell replacement at 680.27"],
    title="IRC section 1091: 30 days before, the sale day, 30 days after (61 days)",
    notes=[
        "30 days before the sale; any purchase of substantially identical SPY from here counts",
        "loss of $10,765 on shares bought 2025-02-19 at 612.93; loss is disallowed, not lost",
        "inside the window: basis becomes 54,669 + 10,765 = 65,434; holding period tacks",
        "30 days after the sale; a purchase on 2025-05-05 would not trigger the rule",
        "gain 68,027 - 65,434 = 2,593; the deferred loss is recognised here",
    ],
)

# --- Figure 3 (lesson 4): harvesting decision flow ---
flow_diagram(
    "harvesting-decision-flow.svg",
    ["Position shows a loss", "Taxable account?", "Any identical purchase within 30 days either side?", "Sell and choose the replacement", "Record and reconcile"],
    title="Tax-loss harvesting: the questions in the order they are asked",
    notes=[
        "compare proceeds with adjusted basis per lot; a paper loss in one lot may hide a gain in another",
        "a loss inside an IRA or 401(k) is never deductible; only taxable accounts harvest",
        "all your accounts, your spouse, your IRA and options to buy; if yes, the loss is deferred",
        "cash for 31 days, a different-index fund, or a same-index fund from another sponsor (unsettled)",
        "date, lot, basis, disallowed amount; check the 1099-B box 1g in the following February",
    ],
)

# --- Figure 4 (lesson 5): ordinary rate vs 60/40 blended rate, 2025 single ---
ORD = [10.0, 12.0, 22.0, 24.0, 32.0, 35.0, 37.0]
BLEND = [4.0, 4.8, 17.8, 18.6, 21.8, 23.0, 26.8]
labels, values, colors = [], [], []
for b, o, bl in zip(BRACKETS, ORD, BLEND):
    labels += [f"{b} ord", f"{b} 60/40"]; values += [o, bl]; colors += [COLORS[3], COLORS[1]]
bar_chart(
    "sixty-forty-blended-vs-ordinary.svg", labels, values,
    title="Section 1256 contracts: ordinary bracket rate vs the 60/40 blended rate, 2025 single",
    y_label="% federal rate on the gain (no NIIT)", colors=colors, y_fmt=lambda v: f"{v:.1f}%",
)

# --- Figure 5 (lesson 9): estimated-tax safe-harbour decision ---
flow_diagram(
    "estimated-tax-safe-harbour-flow.svg",
    ["Will you owe $1,000 or more after withholding?", "Was 2025 AGI above $150,000?", "Required annual payment = the smaller", "Pay one quarter by each due date", "Income arrives late in the year?"],
    title="Form 1040-ES (2026): finding the required annual payment, IRC section 6654(d)",
    notes=[
        "no: no estimated payments are required; yes: continue",
        "yes: prior-year safe harbour is 110% of 2025 tax; no: 100% ($75,000 if married filing separately)",
        "of 90% of the 2026 tax or the prior-year figure; example: min(54,000, 41,800) = 41,800",
        "Apr 15, Jun 15, Sep 15 2026 and Jan 15 2027; 10,450 each in the example",
        "annualise on Form 2210 Schedule AI so early quarters are not penalised for later gains",
    ],
)

# --- Figure 6 (lesson 13): capstone reported gain or loss per trade after the wash-sale adjustment ---
CAP_LABELS = ["1 NVDA", "2 SPY (W)", "3 SPY repl", "4 TSLA", "5 QQQ", "6 AAPL", "7 IWM", "8 TSLA", "9 NVDA", "10 QQQ", "11 AAPL LT", "12 MES 1256"]
CAP_VALUES = [3369.00, 0.00, 1296.50, 5629.60, -3025.50, 4386.60, 7597.00, 1573.80, -617.00, 3266.10, 1696.50, 3350.00]
bar_chart(
    "capstone-gain-loss-by-trade.svg", CAP_LABELS, CAP_VALUES,
    title="Capstone, tax year 2025: reported gain or loss by trade (scenario A)",
    y_label="$ reported on Form 8949 / Form 6781", y_fmt=lambda v: f"{v:,.0f}",
)
print("wrote", sorted(p.name for p in Path(".").glob("*.svg")))

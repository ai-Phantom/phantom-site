"""Figures for the Options Trading Complete course.

Every number here comes from the course's representative chain (lessons 2-13):
XYZ at $100.00, 45 DTE, 28% implied volatility, 4% risk-free rate, no dividend.
Payoff legs use the chain mid prices quoted in the lessons; the theta and delta
curves are the same Black-Scholes model that produced those mids, so the
pictures and the worked examples agree to the cent.

Run:  cd figures && python3 make_figures.py
"""
import math
import sys
from pathlib import Path

# scripts/ lives at the repo root, four levels above figures/ (figures -> options -> courses -> content -> root)
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import bar_chart, line_chart, payoff_chart  # noqa: E402

SPOT = 100.0
RATE = 0.04
IV = 0.28


def cumulative_normal(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def call_price_and_delta(spot, strike, days, rate=RATE, sigma=IV):
    """Black-Scholes European call, no dividend. Returns (price, delta)."""
    t = days / 365
    d1 = (math.log(spot / strike) + (rate + sigma * sigma / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    price = spot * cumulative_normal(d1) - strike * math.exp(-rate * t) * cumulative_normal(d2)
    return price, cumulative_normal(d1)


# Lesson 9: single-leg payoffs at the chain mids
payoff_chart("long-call-payoff.svg", [("call", 100, 4.16, 1)], lo=85, hi=115,
             title="Long XYZ 100 call at 4.16 (45 DTE)", label="Max loss 4.16, break-even 104.16")
payoff_chart("long-put-payoff.svg", [("put", 100, 3.67, 1)], lo=85, hi=115,
             title="Long XYZ 100 put at 3.67 (45 DTE)", label="Max loss 3.67, break-even 96.33")

# Lesson 10: vertical spreads at the chain mids
payoff_chart("bull-call-spread.svg", [("call", 100, 4.16, 1), ("call", 105, 2.16, -1)], lo=90, hi=115,
             title="Bull call spread: long 100C 4.16 / short 105C 2.16", label="Debit 2.00, max gain 3.00, break-even 102.00")
payoff_chart("bear-put-spread.svg", [("put", 100, 3.67, 1), ("put", 95, 1.69, -1)], lo=85, hi=110,
             title="Bear put spread: long 100P 3.67 / short 95P 1.69", label="Debit 1.98, max gain 3.02, break-even 98.02")
payoff_chart("bull-put-credit-spread.svg", [("put", 95, 1.69, -1), ("put", 90, 0.61, 1)], lo=80, hi=105,
             title="Bull put credit spread: short 95P 1.69 / long 90P 0.61", label="Credit 1.08, max loss 3.92, break-even 93.92")

# Lesson 5: value of the ATM 100 call as days to expiration run from 90 to 0
dte_axis = list(range(90, 0, -1))
theta_curve = [round(call_price_and_delta(SPOT, 100, d)[0], 2) for d in dte_axis] + [0.0]
line_chart("theta-decay-curve.svg", {"XYZ 100 call, IV 28%": theta_curve},
           title="Time value of the ATM 100 call vs days to expiration",
           y_label="option value ($ per share)", x_labels=dte_axis + [0],
           annotations=[(45, "45 DTE: 4.16"), (69, "21 DTE: 2.79"), (83, "7 DTE: 1.58")])

# Lesson 4: delta of the 100 call across underlying prices at three DTEs
prices = list(range(80, 121))
delta_series = {
    f"{d} DTE": [round(call_price_and_delta(s, 100, d)[1], 3) for s in prices] for d in (45, 7, 1)
}
line_chart("delta-vs-price.svg", delta_series,
           title="Delta of the XYZ 100 call vs underlying price",
           y_label="delta", x_labels=prices, y_fmt=lambda v: f"{v:.1f}",
           hlines=[(0.5, "ATM: delta ~0.50")])

# Lesson 13: the 100/105 bull call spread priced four ways
bar_chart("capstone-pricing-comparison.svg",
          ["Chain mid", "Put-call parity", "Binomial, 1 step", "Binomial, 50 steps"],
          [2.00, 2.01, 2.49, 1.98],
          title="XYZ 100/105 bull call spread: price by method ($ per share)",
          y_label="$ per share", y_fmt=lambda v: f"{v:.2f}")

print("wrote 8 figures")

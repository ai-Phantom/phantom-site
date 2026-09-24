import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

"""Figures for Options Income: Spreads, the Wheel, Condors.

Every number is taken from the course's model chain and the lessons' worked
examples: XYZ at $100.00, November 6, 2026 expiration (45 DTE), 28% implied
volatility, 4% risk-free rate, no dividend. Chain mids: 85P 0.16, 90P 0.61,
95P 1.69, 100C 4.16, 105C 2.16, 110C 1.00, 115C 0.41. Premiums are passed as
positive numbers; the qty sign marks long (+) or short (-), as svgfig expects.

Run:  cd figures && python3 make_figures.py
"""

# Lesson 2: covered call, long 100 shares at 100.00 plus short 105 call at 2.16.
# Break-even 97.84, maximum gain 7.16 per share above 105.
payoff_chart("covered-call-payoff.svg",
             [("stock", 100, 0.0, 1), ("call", 105, 2.16, -1)],
             lo=85, hi=115,
             title="Covered call: long XYZ at 100.00, short Nov 105 call at 2.16",
             label="Break-even 97.84, max gain 7.16 at or above 105")

# Lesson 3: cash-secured put, short 95 put at 1.69. Break-even 93.31, max gain 1.69.
payoff_chart("cash-secured-put-payoff.svg",
             [("put", 95, 1.69, -1)],
             lo=80, hi=110,
             title="Cash-secured put: short Nov 95 put at 1.69",
             label="Break-even 93.31, max gain 1.69, loss grows below 93.31")

# Lesson 4: the wheel as a cycle, numbers from the lesson's worked example.
flow_diagram("wheel-cycle.svg",
             ["Sell 95 put", "Assigned at 95", "Sell 95 call", "Called away at 95", "Back to cash"],
             title="The wheel on the model chain: one 87-day cycle",
             notes=["Sep 22: credit 1.69, cash 9,500 reserved",
                    "Nov 6: XYZ 92.00, basis 95 - 1.69 = 93.31",
                    "Nov 6: Dec 95 call at 2.88, break-even 90.43",
                    "Dec 18: XYZ 96.50, cycle P&L 169 + 288 = $457",
                    "5.30% on 9,500 with interest; repeat or stop"])

# Lesson 5: bull put spread, short 95 put 1.69 / long 90 put 0.61.
# Credit 1.08, max loss 3.92, break-even 93.92.
payoff_chart("bull-put-spread-payoff.svg",
             [("put", 95, 1.69, -1), ("put", 90, 0.61, 1)],
             lo=80, hi=110,
             title="Bull put spread: short Nov 95 put 1.69 / long 90 put 0.61",
             label="Credit 1.08, max loss 3.92, break-even 93.92")

# Lesson 5: expected P&L per spread at half-spread market fills, from the lesson's
# integration under a lognormal with drift equal to the 4% rate.
# "no VRP": realised 28% = implied. "VRP 4 pts": realised 24%.
# POP: 100/95 58%, 95/90 74%, 90/85 87%.
bar_chart("pop-vs-expected-value.svg",
          ["100/95 no VRP", "100/95 VRP 4pt", "95/90 no VRP", "95/90 VRP 4pt", "90/85 no VRP", "90/85 VRP 4pt"],
          [-11.4, -0.5, -8.1, 11.5, -4.9, 11.1],
          title="Expected P&L per bull put spread at market fills ($): POP 58% / 74% / 87%",
          y_label="$ per spread", y_fmt=lambda v: f"{v:+.1f}")

# Lesson 6: iron condor, short 90 put 0.61 and 110 call 1.00, long 85 put 0.16 and 115 call 0.41.
# Credit 1.04, max loss 3.96, break-evens 88.96 and 111.04.
payoff_chart("iron-condor-payoff.svg",
             [("put", 90, 0.61, -1), ("put", 85, 0.16, 1), ("call", 110, 1.00, -1), ("call", 115, 0.41, 1)],
             lo=78, hi=122,
             title="Iron condor: short 90P 0.61 / 110C 1.00, long 85P 0.16 / 115C 0.41",
             label="Credit 1.04, max loss 3.96, break-evens 88.96 and 111.04")

# Lesson 13: capstone results on November 6 by path (dollars per position).
# Wheel: A and B put expired +169; C assigned, shares marked at 84.00 vs 93.31 basis = -931.
# Condor held: +104, +104, -396. Condor closed Oct 16 at checkpoint marks 0.54 / 0.41 / 1.41.
bar_chart("capstone-three-paths.svg",
          ["A wheel", "A IC held", "A IC 21d", "B wheel", "B IC held", "B IC 21d", "C wheel", "C IC held", "C IC 21d"],
          [169, 104, 50, 169, 104, 63, -931, -396, -37],
          title="Capstone: P&L on November 6 by price path ($ per position)",
          y_label="$", y_fmt=lambda v: f"{v:+,.0f}")

print("wrote 7 figures")

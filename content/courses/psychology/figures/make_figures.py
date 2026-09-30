"""Figures for the Trading Psychology & Process course.

Every number plotted here is either taken from a cited study (Odean 1998,
Tversky and Kahneman 1992) or computed by the same arithmetic the lesson's
worked example shows (binomial streak probability, expectancy, the capstone's
100-trade simulation). Nothing is fetched at run time.

Run:  cd figures && python3 make_figures.py
"""
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import *

# --- Figure 1 (lesson 2): the disposition effect, Odean (1998), Table I ---
# PGR = realized gains / (realized gains + paper gains) = 13,883 / (13,883 + 79,658)
# PLR = realized losses / (realized losses + paper losses) = 11,930 / (11,930 + 110,348)
PGR_YEAR = 13883 / (13883 + 79658)          # 0.148
PLR_YEAR = 11930 / (11930 + 110348)         # 0.098
PGR_DEC, PLR_DEC = 0.108, 0.128             # December only, Odean (1998) Table I
assert round(PGR_YEAR, 3) == 0.148 and round(PLR_YEAR, 3) == 0.098
bar_chart(
    "disposition-effect-odean-1998.svg",
    ["PGR, whole year", "PLR, whole year", "PGR, December", "PLR, December"],
    [PGR_YEAR, PLR_YEAR, PGR_DEC, PLR_DEC],
    title="Proportion of gains realized (PGR) vs losses realized (PLR), 10,000 accounts, 1987-1993",
    y_label="share of available positions sold", y_fmt=lambda v: f"{v:.3f}",
    colors=[COLORS[0], COLORS[3], COLORS[0], COLORS[3]],
)

# --- Figure 2 (lesson 3): the prospect-theory value function, Tversky & Kahneman (1992) ---
# v(x) = x^0.88 for gains, -2.25 * (-x)^0.88 for losses
def value(x, alpha=0.88, lam=2.25):
    return x ** alpha if x >= 0 else -lam * (-x) ** alpha

XS = list(range(-100, 101, 5))
line_chart(
    "prospect-theory-value-curve.svg",
    {"v(x): felt value of a gain or loss of x": [value(x) for x in XS]},
    title="Prospect-theory value function: a $100 loss feels like -129, a $100 gain like +58",
    y_label="felt value", x_labels=[f"{x:+d}" if x else "0" for x in XS],
    y_fmt=lambda v: f"{v:+.0f}", hlines=[(0, "zero")],
    annotations=[(0, "-100 -> -129.5"), (40, "+100 -> +57.5")],
)

# --- Figure 3 (lesson 9): expectancy for win-rate / payoff pairs, loss fixed at 1R ---
PAIRS = [(30, 3.0), (40, 2.0), (50, 1.0), (55, 1.0), (60, 0.8), (70, 0.5), (80, 0.2)]
def expectancy(win_rate_pct, avg_win_r, avg_loss_r=1.0):
    p = win_rate_pct / 100
    return p * avg_win_r - (1 - p) * avg_loss_r

bar_chart(
    "expectancy-by-win-rate-and-payoff.svg",
    [f"{p}% / {w:.1f}R" for p, w in PAIRS],
    [round(expectancy(p, w), 3) for p, w in PAIRS],
    title="Expectancy per trade (R) = win rate x avg win - loss rate x 1R",
    y_label="R per trade", y_fmt=lambda v: f"{v:+.2f}",
)

# --- Figure 4 (lesson 10): probability of at least one losing streak of k in 100 trades ---
def p_streak(n_trades, loss_prob, k):
    """Probability of at least one run of >= k consecutive losses in n independent trades."""
    state = [0.0] * k; state[0] = 1.0; hit = 0.0
    for _ in range(n_trades):
        nxt = [0.0] * k
        for run_len, pr in enumerate(state):
            if pr == 0.0:
                continue
            nxt[0] += pr * (1 - loss_prob)
            if run_len + 1 >= k:
                hit += pr * loss_prob
            else:
                nxt[run_len + 1] += pr * loss_prob
        state = nxt
    return hit

WIN_RATES = list(range(40, 71, 5))
# the lesson's worked example: 55% win rate, 100 trades, streak of 7 -> 17.9%
assert round(p_streak(100, 0.45, 7), 3) == 0.179
line_chart(
    "losing-streak-probability-100-trades.svg",
    {f"streak of {k} or more": [100 * p_streak(100, 1 - w / 100, k) for w in WIN_RATES] for k in (5, 7, 10)},
    title="Chance of at least one losing streak of k in 100 trades, by win rate",
    y_label="probability, %", x_labels=[f"{w}%" for w in WIN_RATES],
    y_fmt=lambda v: f"{v:.0f}%",
)

# --- Figure 5 (lesson 11): the daily routine ---
flow_diagram(
    "daily-routine.svg",
    ["Pre-market: read the plan", "Session: setups only", "Circuit breaker", "Post-market: journal", "Weekly: review, rest"],
    title="The daily routine: the plan is read before the open and graded after the close",
    notes=[
        "sleep logged; loss limit and max trades written down; orders pre-staged",
        "entry, stop and size fixed by rule; no trade outside the written setups",
        "daily loss limit or two rule breaks ends the session; platform closed",
        "every trade logged within 30 min: rule followed? R result, MAE",
        "expectancy and error bar recomputed; one change at most; screens off",
    ],
)

# --- Figure 6 (lesson 12): the stop rule ---
flow_diagram(
    "stop-rule.svg",
    ["Drawdown rule hit", "Stop live trading", "Fixed break", "Paper-trade N trades", "Return criteria met?"],
    title="The stop rule: written before the drawdown, executed without a vote",
    notes=[
        "peak-to-trough loss reaches the written limit, e.g. 12R or 6% of equity",
        "no live orders the same day; the limit is not renegotiated",
        "minimum 5 sessions away from the screen; sleep and exercise logged",
        "same plan, same size, 30 trades; expectancy and rule-adherence measured",
        "adherence 95%+, expectancy not negative by 2 SE: resume at half size",
    ],
)

# --- Figure 7 (capstone): the reference 100-trade simulation ---
# 55% win rate, average win +1.2R, average loss -1.0R, drawn with random.seed(2026).
OUTCOMES = [1.2, 1.2, 1.2, -1.0, 1.2, 1.2, -1.0, -1.0, -1.0, 1.2, -1.0, -1.0, -1.0, -1.0, 1.2, -1.0, 1.2, -1.0, 1.2, -1.0, -1.0, -1.0, 1.2, 1.2, -1.0, -1.0, -1.0, -1.0, 1.2, 1.2, 1.2, -1.0, 1.2, 1.2, -1.0, -1.0, -1.0, 1.2, -1.0, 1.2, 1.2, 1.2, -1.0, 1.2, 1.2, 1.2, -1.0, -1.0, 1.2, -1.0, 1.2, 1.2, -1.0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, -1.0, -1.0, 1.2, -1.0, 1.2, 1.2, 1.2, -1.0, -1.0, 1.2, 1.2, -1.0, -1.0, 1.2, -1.0, -1.0, 1.2, -1.0, 1.2, 1.2, -1.0, 1.2, 1.2, 1.2, 1.2, -1.0, -1.0, 1.2, 1.2, 1.2, -1.0, 1.2, 1.2, 1.2, -1.0, -1.0, -1.0, -1.0, -1.0, 1.2, -1.0]
assert len(OUTCOMES) == 100 and sum(1 for o in OUTCOMES if o > 0) == 53
EQUITY = [0.0]
for o in OUTCOMES:
    EQUITY.append(round(EQUITY[-1] + o, 2))
assert EQUITY[-1] == 16.6 and EQUITY[6] == 5.0 and EQUITY[28] == -3.8
line_chart(
    "capstone-equity-curve.svg",
    {"cumulative R, 100 trades": EQUITY},
    title="Reference simulation: 55% win rate, +1.2R / -1.0R, 100 trades, final +16.6R",
    y_label="R", x_labels=[str(i) if i % 10 == 0 else "" for i in range(101)],
    y_fmt=lambda v: f"{v:+.0f}", hlines=[(0, "start")],
    annotations=[(6, "peak +5.0R (trade 6)"), (28, "trough -3.8R (trade 28): 8.8R drawdown"), (98, "5-loss streak, trades 94-98")],
)
print("wrote 7 figures")

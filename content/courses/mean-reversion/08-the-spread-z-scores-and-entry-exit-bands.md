---
{
  "title": "The Spread, Z-Scores and Entry/Exit Bands",
  "duration": "19 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2026-01-05 XOP closed at 127.50 and XLE at 46.89. With α = 0.0970, β = 1.2717 and a formation standard deviation of 0.0510, the spread's z-score was about:", "opts": ["+2.8", "−2.8", "0", "−0.7"], "correct": 1, "explain": "s = ln(127.50) − 0.0970 − 1.2717 × ln(46.89) = 4.8481 − 0.0970 − 4.8933 = −0.1422; z = −0.1422 / 0.0510 = −2.79. Below −2, so the rule goes long the spread: long XOP, short 1.27 dollars of XLE per dollar of XOP."},
    {"q": "The static-z trade opened on 2026-01-05 was still open on 2026-09-23, 179 trading days later, with z at −2.85. Its net result on a $10,000 XOP leg was:", "opts": ["+$59, with a worst mark-to-market of −$579", "+$1,048", "−$579", "+$127 before costs, and costs were zero"], "correct": 0, "explain": "Gross +$127 (XOP +43.25% on $10,000 against XLE +33.01% on $12,717), less $22.72 in transaction costs and $45.16 of borrow on the short leg: +$59. The spread never returned to zero; the trade ended because the sample did."},
    {"q": "Switching from formation-window statistics to a rolling 60-day mean and standard deviation for the z-score changed the year's result to:", "opts": ["One trade, +$59", "Three trades netting −$119, including a −$498 trade in which z reached −5.23 before crossing zero", "Ten winning trades", "No trades"], "correct": 1, "explain": "The rolling version adapts and so trades more often, but its second trade (2025-12-18 to 2026-03-05) was marked at −$1,276 at the worst point. Adaptive bands do not remove the risk that the spread keeps going; they change which trades you take."},
    {"q": "Why is the XLE leg sized at $12,717 rather than $10,000?", "opts": ["Because XLE is more expensive per share", "Because the hedge ratio from the log-log regression is 1.2717, meaning a 1% move in XLE has historically gone with a 1.27% move in XOP; equal dollar legs would leave the position net long energy", "Because of margin rules", "Because XLE pays a dividend"], "correct": 1, "explain": "With log prices, the regression slope is an elasticity, and the dollar ratio that neutralises the common factor equals that slope. Dollar-neutral (1:1) is only correct when β = 1."},
    {"q": "The lesson's honest summary of the XLE/XOP year is:", "opts": ["The rule made money, so the pair works", "A pair that failed the cointegration test behaved like a pair that failed the cointegration test: the spread went to −3.82 and stayed outside the band for eight months; the small profit was luck in the sign of the drift, not reversion", "The rule should use 3 s.d. bands", "XOP is the better ETF"], "correct": 1, "explain": "Lesson 7's t-statistic of −1.23 predicted this. When there is no statistical pull toward the mean, an entry at −2 is a coin flip on which way the random walk continues."}
  ],
  "task": "Using the hedge ratio you estimated for your own pair, compute the spread and its z-score for the last 20 sessions and note whether it is inside or outside ±2."
}
---

Once you have a hedge ratio, the pair collapses to one number a day: the spread. Standardising it gives a z-score, and the rule is then just thresholds on z. This lesson builds the spread for XLE and XOP, sets the bands, and logs every trade the standard 2σ-entry, 0σ-exit rule would have taken over the twelve months to 2026-09-23, with costs. The pair failed the cointegration test in lesson 7. Watching what the rule does anyway is the point.

## Spread and z-score

With α and β from the formation regression:

s_t = ln(Y_t) − α − β·ln(X_t)

The spread is the residual of the fitted relation, evaluated on new data. Two ways to standardise it:

**Formation statistics** (Gatev, Goetzmann and Rouwenhorst, 2006): z_t = (s_t − μ_F) / σ_F, where μ_F and σ_F are the mean and standard deviation of s over the formation window. Because the residual of an OLS fit has mean zero, μ_F = 0. The bands are fixed for the whole trading period.

**Rolling statistics**: z_t = (s_t − mean of the last 60 values of s) / (s.d. of the last 60). The bands move with the recent level. This adapts to drift, which sounds like a benefit and is also a way of redefining "the mean" as wherever the spread went last quarter.

The course uses formation statistics as the base case, because the trade's premise is that the formation-window relation persists. If you have to keep moving the mean, the premise has failed.

## Bands and sides

- z > +2: the spread is high, Y is rich relative to X. **Short the spread**: short Y, long β dollars of X per dollar of Y.
- z < −2: **long the spread**: long Y, short β dollars of X.
- Exit when z crosses 0.
- No new entry while a position is open.

Position sizing for the log spread: for N dollars of Y, hold β·N dollars of X. The log-log slope is an elasticity, so the dollar ratio that neutralises the common move is β itself. Gross notional is N(1 + β). Costs in this lesson: 0.05% per side on every leg (a 1 to 2 cent quote on a $40 to $180 ETF plus slippage), and 0.5% per year borrow on the short leg, prorated by holding days. Lesson 11 examines both numbers.

## Worked example

Pair: Y = XOP, X = XLE. Formation 2023-09-22 to 2025-09-22: α = 0.0970, β = 1.2717, σ_F = 0.05101. Trading window 2025-09-23 to 2026-09-23, 251 sessions. Data: Yahoo Finance daily closes, `interval=1d`, pulled 2026-09-24. N = $10,000 on the XOP leg, so $12,717 on the XLE leg, gross $22,717.

**The z-score at the start.** 2025-09-23: z = −0.67. Inside the band. It stayed inside through the autumn (−0.53 on 10-01, −1.21 on 11-03, −0.99 on 12-01) and crossed −2 at the turn of the year.

**Entry, 2026-01-05.** XOP 127.50, XLE 46.89.

ln(127.50) = 4.8481; ln(46.89) = 3.8478; β × ln(XLE) = 1.2717 × 3.8478 = 4.8933
s = 4.8481 − 0.0970 − 4.8933 = **−0.1422**
z = −0.1422 / 0.05101 = **−2.79**

(The trade log, computed at full precision, records −2.78.) Below −2: long the spread. Buy $10,000 of XOP (78.4 shares at 127.50), short $12,717 of XLE (271.2 shares at 46.89).

**The path.** The spread kept falling. On 2026-02-12, XOP 144.63 and XLE 53.98: XOP was up 13.44% on the entry, XLE up 15.12%. Mark: 10,000 × 0.1344 − 12,717 × 0.1512 = 1,344 − 1,923 = **−$579**. That was the low: z = **−3.82**. It then oscillated between −3.3 and −2.0 for the rest of the year (−3.18 on 02-02, −3.27 on 03-02, −2.31 on 04-01, −2.05 on 05-01, −2.39 on 06-01) and never reached zero.

**End of sample, 2026-09-23.** XOP 182.65, XLE 62.37. XOP +43.25% on entry, XLE +33.01%.

Gross = 10,000 × 0.4325 − 12,717 × 0.3301 = 4,325 − 4,198 = **+$127**
Transaction cost = 2 sides × $22,717 × 0.0005 = **$22.72**
Borrow = $12,717 × 0.005 × 179/252 = **$45.16**
Net = 127 − 22.72 − 45.16 = **+$59**

One trade, 179 trading days, +0.26% on gross notional, with z still at −2.85 on the last day. Both ETFs rose more than a third; the profit is the small difference between two large moves, and it is positive because XOP happened to outpace 1.27 times XLE by a whisker. The formation mean was never revisited.

**Rolling-60 version.** Three trades, all long the spread:

- 2025-10-17 to 2025-11-25 (27 days): z −2.47 to +0.18; gross +$149, costs $29.53, net **+$120**.
- 2025-12-18 to 2026-03-05 (51 days): z −2.07 to +0.12; but z reached **−5.23** on 2026-01-05 and the mark bottomed at **−$1,276**; gross −$463, costs $35.58, net **−$498**. The exit at zero was a zero of the rolling mean, which had by then moved down to meet the spread.
- 2026-08-18 to 2026-08-27 (7 days): z −2.34 to +0.24; net **+$260**.

Total: gross −$29, costs $89.59, net **−$119**, two winners out of three.

## The trade log

| Rule (XOP vs 1.2717 × XLE, 2025-09-23 to 2026-09-23) | Entry | Exit | Days | z in | z out | Worst mark | Gross | Costs | Net |
|---|---|---|---|---|---|---|---|---|---|
| Formation z, ±2 / 0 | 2026-01-05 | open at 09-23 | 179 | −2.78 | −2.85 | −$579 | +$127 | $67.88 | +$59 |
| Rolling-60 z, ±2 / 0 | 2025-10-17 | 2025-11-25 | 27 | −2.47 | +0.18 | −$162 | +$149 | $29.53 | +$120 |
| Rolling-60 z, ±2 / 0 | 2025-12-18 | 2026-03-05 | 51 | −2.07 | +0.12 | −$1,276 | −$463 | $35.58 | −$498 |
| Rolling-60 z, ±2 / 0 | 2026-08-18 | 2026-08-27 | 7 | −2.34 | +0.24 | $0 | +$284 | $24.48 | +$260 |

$10,000 XOP leg, $12,717 XLE leg; 0.05% per side, 0.5% annual borrow on the short leg. Source: Yahoo Finance daily closes, computed by the course.

## Chart

![Z-score of the XOP versus 1.27 × XLE log spread from 2025-09-23 to 2026-09-23, standardised two ways: by the 2023-09-22 to 2025-09-22 formation mean and standard deviation, and by a rolling 60-day window. Bands at +2, 0 and −2. The formation-z entry on 2026-01-05, the −3.82 low on 2026-02-12 and the still-open position at the end are marked. Source: Yahoo Finance daily closes, computed by the course.](figures/xle-xop-zscore-2025-2026.svg)

## Reading the year

The formation-z line spends eight of twelve months below −2 and never touches zero. Lesson 7 said this pair had no detectable pull toward its formation mean (t = −1.23), and here is what that looks like in trading terms: the deviation does not close, it persists. The rolling line touches zero three times, because a rolling mean follows the spread down and then declares the spread "back at the mean" when the spread stops falling. Two of those three trades won, and the year still lost money, because the one loser was marked at −$1,276 on the way to being closed at −$498.

Neither result is a verdict on the rule; both are verdicts on applying the rule to a spread that failed its test. The formation version could as easily have ended −$1,000 had XLE outpaced XOP by the same whisker, and the rolling version's +$120 and +$260 are the kind of trades that a stationary spread produces routinely. What you should take is the shape of the failure: entry at −2.78, worst mark −$579 at −3.82, no exit for eight months. Lesson 9 asks how long a spread should take to come back, and lesson 10 asks what to do when it does not.

## Sources

- Gatev, E., Goetzmann, W. N. and Rouwenhorst, K. G. (2006). Pairs trading: performance of a relative-value arbitrage rule. *Review of Financial Studies*, 19(3), 797–827. https://doi.org/10.1093/rfs/hhj020
- Avellaneda, M. and Lee, J.-H. (2010). Statistical arbitrage in the US equities market. *Quantitative Finance*, 10(7), 761–782. https://doi.org/10.1080/14697680903124632
- Yahoo Finance historical data: XLE https://finance.yahoo.com/quote/XLE/history/ and XOP https://finance.yahoo.com/quote/XOP/history/

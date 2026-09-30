---
{
  "title": "Volatility: Realised, Implied, EWMA and Vol Targeting",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2026-09-23 SPY's 20-day realised volatility was 10.9%, its EWMA (λ = 0.94) estimate 11.3%, its one-year realised 13.0% and the VIX closed at 15.18. The most defensible reading is", "opts": ["The VIX is wrong", "Recent realised vol is below the year's average and below what options imply; the option market is charging a premium over realised, which is its usual state", "Volatility is about to spike", "The 20-day number should be ignored because it is the smallest"], "correct": 1, "explain": "Implied volatility usually sits above subsequently realised volatility, which is the variance risk premium. A VIX of 15 against a realised 11 is unremarkable. The numbers disagree because they measure different windows and different things."},
    {"q": "Over 5,716 SPY daily returns from 2004 to 2026, the lag-1 autocorrelation of returns was −0.10 while the lag-1 autocorrelation of squared returns was +0.26 and of absolute returns +0.31. What does that pair of facts establish?", "opts": ["Returns are predictable", "Volatility is constant", "Squared returns are a mistake", "Direction is close to unpredictable, but the size of moves is persistent: a big move today makes a big move tomorrow more likely, which is why a recent-weighted vol estimate is useful"], "correct": 3, "explain": "That is volatility clustering. The sign of tomorrow's return carries almost no memory; its magnitude does. EWMA and GARCH exist to exploit the second fact."},
    {"q": "The EWMA variance recursion with λ = 0.94 has a half-life of about", "opts": ["11 days", "2 days", "60 days", "252 days"], "correct": 0, "explain": "Half-life = ln(0.5) / ln(0.94) = 11.2 days. An observation from eleven trading days ago carries half the weight of today's. A 20-day simple window gives every day in it equal weight and then drops it to zero on day 21."},
    {"q": "Between 2020-02-19 and 2020-03-16, SPY's 20-day realised vol went from 13.4% to 77.0%, the 60-day from 9.7% to 46.4%, and the EWMA from 11.0% to 78.8%. Which estimator would have de-risked a vol-targeted book fastest?", "opts": ["The 60-day window", "None of them; only the VIX moved", "The 20-day or EWMA; both had caught most of the move by 03-16, while the 60-day was still diluting it with January's calm", "They are all equally fast"], "correct": 2, "explain": "A long equal-weighted window is slow by construction. On 2020-04-30 the 60-day estimate was still 60.4%, above the 20-day's 36.8%, because it was still carrying March. Slow in, slow out."},
    {"q": "A 12% vol target on SPY with EWMA scaling, capped at 1.5x, from 2008 to 2026 produced 9.3% a year at 12.4% vol and a −23.7% worst drawdown, versus 11.3% a year at 19.7% vol and −51.9% for buy-and-hold. What is the honest summary?", "opts": ["Vol targeting beat the market", "Vol targeting returned less in total but more per unit of risk and with less than half the drawdown; it is a risk control, and it is paid for in average return", "Vol targeting failed", "The drawdown improvement was luck"], "correct": 1, "explain": "The Sharpe ratio rose from 0.64 to 0.78 and the maximum drawdown halved, at the cost of two percentage points a year of return, most of which was forgone in the 2009 and 2020 rebounds when the scale was still low. That trade is the point; pretending it is free is not."}
  ],
  "task": "Compute your book's daily returns for the last year and its 20-day, 60-day and EWMA volatility today; note which is highest and why."
}
---

## Three numbers that are all called volatility

Volatility is the one risk quantity you can re-estimate every day from a short window and expect the estimate to carry forward. That makes it the backbone of daily control. But "the volatility" is a family of numbers, and the report has to say which member it means.

**Realised volatility** is the standard deviation of past daily returns over some window, annualised by √252. The window is the whole argument: a 20-day window reacts fast and is noisy; a one-year window is stable and slow.

**Implied volatility** is the volatility the options market is pricing, read off option prices through a model. The VIX is the 30-day implied volatility of S&P 500 index options. It is a forecast plus a risk premium, and it usually runs above what is subsequently realised.

**EWMA volatility** is a realised estimate that weights recent returns more than old ones: σ²ₜ = λ σ²ₜ₋₁ + (1 − λ) r²ₜ. With λ = 0.94, the value RiskMetrics popularised for daily data, an observation eleven trading days old has half the weight of today's. It reacts nearly as fast as a 20-day window and does not have the 20-day window's habit of dropping a large return off a cliff on day 21.

## Why volatility clusters

The whole case for daily re-estimation rests on one empirical fact: large moves cluster. Over 5,716 SPY daily returns from 2004-01-02 to 2026-09-23 (Yahoo adjusted closes), the lag-1 autocorrelation of returns is −0.10 and the lag-5 and lag-20 autocorrelations are −0.01 and +0.02: direction has essentially no memory. The lag-1 autocorrelation of squared returns is +0.26, lag-5 +0.29, lag-20 +0.14. For absolute returns, +0.31, +0.35, +0.23 at lags 1, 5 and 20, fading to +0.07 by lag 60.

So the size of a move persists for weeks, and its sign does not. A volatility estimate that leans on the last two or three weeks is using real information; a return forecast that does the same is not. This asymmetry is what Engle's ARCH work formalised, and it is the reason a risk desk updates vol daily but does not update its return expectation daily.

The corollary for a book: when today's realised vol jumps, tomorrow's is more likely to be high than to revert. A book sized for last month's calm is oversized this month, and the estimate that tells you so soonest is the one weighted to the last few days.

## Vol targeting

Vol targeting sizes the book so that its expected volatility equals a chosen target. Scale = target ÷ current estimate, applied to gross exposure, usually capped so calm periods cannot lever you into the next crash. With a 12% target and a 24% estimate you run at half size; with an 8% estimate you run at 1.5x if the cap allows.

Two things happen when you do this. Volatility of the book becomes roughly constant, so a daily VaR built on it stops swinging by a factor of five between regimes. And exposure is cut early in a crash, because realised vol rises before or with the first big down days, which shortens the left tail. The cost is that exposure is also low at the bottom, when returns are best, so long-run average return falls. Moreira and Muir (2017) document that the Sharpe ratio improvement survives across markets and factors; the lower total return is the price.

## Worked example

SPY, Yahoo Finance adjusted closes, as of the 2026-09-23 close.

**20-day realised.** The last twenty daily returns, 2026-08-26 through 2026-09-23, in percent: +0.02, +0.66, −0.23, −0.30, −0.69, +0.44, +1.05, −0.39, −0.55, −0.46, −0.60, +0.85, −0.45, −0.46, −0.44, +1.13, +0.13, +1.55, −0.02, −0.72. Sum = +1.39, so the mean is +0.0695%. Sum of squares = 0.0008917 (in decimal units). Sample variance = (0.0008917 − 20 × 0.000695²) ÷ 19 = (0.0008917 − 0.0000097) ÷ 19 = 0.0000464. Daily standard deviation = √0.0000464 = 0.00681, or 0.68%. Annualised: 0.68% × √252 = 0.68% × 15.87 = **10.9%** (10.87% unrounded).

**60-day realised**, same method on the last sixty returns: **11.3%** (11.25%).

**One-year realised**, 251 returns from 2025-09-24: **13.0%** (12.99%).

**EWMA, λ = 0.94.** The recursion was seeded with the variance of the first 250 returns in 2004 and run forward daily; after twenty-two years the seed is irrelevant. On 2026-09-22 the EWMA variance was 0.00005097 (annualised vol 11.33%). The 2026-09-23 return was −0.7202%, so r² = 0.00005187. New variance = 0.94 × 0.00005097 + 0.06 × 0.00005187 = 0.00004791 + 0.00000311 = 0.00005102. Annualised: √(0.00005102 × 252) = √0.012857 = 0.1134 = **11.3%**.

**Implied.** VIX close on 2026-09-23: **15.18**.

Four estimates, 10.9% to 15.2%, in the order you would expect in a calm month: short realised windows lowest, the year higher because it still contains a rougher spring, implied highest because it carries the variance premium.

**Vol target.** With a 12% target and the EWMA estimate: scale = 12 ÷ 11.34 = **1.06**, so the rule would run SPY at 106% of base size today. Applied daily from 2008-01-02 to 2026-09-23 with yesterday's EWMA and a 1.5x cap, the rule averaged a scale of 0.89 and bottomed at 0.14 on 2008-10-29. Results: 9.3% a year compounded at 12.4% realised vol, Sharpe 0.78, worst drawdown −23.7%. SPY unscaled over the same period: 11.3% a year at 19.7% vol, Sharpe 0.64, worst drawdown −51.9%.

**Speed in a crash.** On 2020-02-19, the pre-crash high, the 20-day, 60-day and EWMA estimates were 13.4%, 9.7% and 11.0%, VIX 14.4. On 02-28: 24.8%, 16.5%, 25.1%, VIX 40.1. On 03-16: 77.0%, 46.4%, 78.8%, VIX 82.7. On 03-23, the low: 82.1%, 49.6%, 74.7%, VIX 61.6. On 04-30: 36.8%, 60.4%, 49.5%, VIX 34.2. The 20-day peaked at 93.2% on 03-27 and the EWMA at 80.6% on 03-24, both after the low. The 60-day window was still rising into May. In April 2025 the same pattern repeated on a smaller scale: 20-day peak 54.5% on 04-25, VIX peak 52.3 on 04-08.

## Chart

![SPY 20-day realised volatility (annualised) and the VIX close, sampled every fifth trading day from 2019-09-23 to 2026-09-17, with the 12% vol target as a dashed line. Peaks of 92.5% on 2020-03-30 and 54.5% on 2025-04-25 are marked. Source: Yahoo Finance daily adjusted closes for SPY and ^VIX.](figures/spy-realised-vol-and-target.svg)

## How the book uses this

Each line in the exposure table from lesson 2 gets a one-year and an EWMA volatility next to it. The book's own volatility is computed from the position return series (lesson 4), and that number, not any single line's, is what the vol target scales.

Choose the estimator for its purpose. For sizing, EWMA or 20-day: fast is what you want. For the VaR window, one year: you want the sample to contain a bad month. For the stress test in lesson 5, the crisis window itself.

And the rule for reporting: when the fast estimate crosses above the slow one, say so in words. That crossover is the earliest signal a risk report gives that the regime has changed, and it arrives days before any drawdown rule fires.

## Sources

- Engle, R. F. (2003). "Risk and Volatility: Econometric Models and Financial Practice." Nobel Prize lecture. https://www.nobelprize.org/uploads/2018/06/engle-lecture.pdf
- Moreira, A. and Muir, T. (2017). "Volatility-Managed Portfolios." *Journal of Finance* 72(4). https://doi.org/10.1111/jofi.12513
- Cboe. "Cboe Volatility Index (VIX) Methodology." https://www.cboe.com/tradable_products/vix/
- Yahoo Finance historical data, SPY and ^VIX. https://finance.yahoo.com/quote/%5EVIX/history/

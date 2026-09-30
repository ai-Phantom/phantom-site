---
{
  "title": "What Mean Reversion Is and Where It Lives",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Over 2015-01-02 to 2026-09-23, the lag-1 autocorrelation of SPY's daily returns was −0.117 with a standard error of about 0.018. The right reading is:", "opts": ["Daily returns are unpredictable", "A down day is followed, on average, by a slightly up day and vice versa; the effect is small per day but far too large to be chance in this sample", "SPY trends strongly from day to day", "Yesterday's return explains most of today's"], "correct": 1, "explain": "A t-statistic of about −6.4 rules out chance, but −0.117 means yesterday explains barely 1.4% of today's variance. Small, real, and only tradeable when costs are near zero."},
    {"q": "After a SPY down day worse than −2% (100 cases in the sample), the average next-day return was:", "opts": ["+0.38%, up 60% of the time", "−0.46%, up 47% of the time", "+0.05%, the same as any day", "Exactly zero"], "correct": 0, "explain": "The next-day mean after a sub −2% day was +0.380% with 60.0% of next days positive, against +0.051% and 54.4% for all days. The mirror case, after a +2% day, averaged −0.464%."},
    {"q": "Which of these is the strongest and most reliable mean-reverting series in the lesson?", "opts": ["SPY's price level", "The 12-month return of a single stock", "The VIX index level", "The cross-section of six-month stock returns"], "correct": 2, "explain": "VIX cannot drift to zero or to infinity; after closes at or above 30 it averaged 9.6 points lower twenty trading days later. SPY's level is close to a random walk and six-month returns show continuation, not reversal."},
    {"q": "In the 20-stock cross-section, past one-week return versus next-week return had a mean correlation of −0.024, while past six-month return versus next-month return had +0.059. This illustrates:", "opts": ["Reversal at short horizons, continuation (momentum) at intermediate horizons", "Momentum at all horizons", "That correlation is meaningless", "That reversal grows with horizon"], "correct": 0, "explain": "The sign flips with horizon: short lookbacks revert, three-to-twelve-month lookbacks continue. Both effects are small in this 20-stock sample, and the momentum horizon is where a reversion rule should not be applied."},
    {"q": "Why is a large negative autocorrelation in daily index returns not automatically a profitable strategy?", "opts": ["Because autocorrelation only exists in simulations", "Because the average next-day edge (a few tenths of a percent after extreme days, hundredths of a percent on ordinary days) is comparable to round-trip trading costs and is unevenly distributed across time", "Because indexes cannot be traded", "Because it requires options"], "correct": 1, "explain": "The whole course is about the gap between a statistically real reversal and a net-of-cost profit. Lesson 3 measures that gap on individual stocks; lesson 11 builds the cost stack."}
  ],
  "task": "Pull SPY daily closes for the last three years from Yahoo Finance, compute the average next-day return after every down day and after every up day, and write both numbers down with the sample sizes."
}
---

Mean reversion is the tendency of a quantity to move back toward a central value after it has moved away. In markets it shows up in three places: in short-horizon returns of stocks and indexes, in the spread between two related assets, and in volatility. It does not show up everywhere, and a trader who assumes it does will be run over by the one thing that does not revert, which is price itself over months and years. This lesson measures each case on real data so you can see the size of the effect, not just the sign.

## Three things that revert and one that does not

**Short-horizon returns.** A stock that fell sharply this week tends, on average, to do slightly better than a stock that rose sharply this week. Narasimhan Jegadeesh documented this at the one-month horizon in 1990 and Bruce Lehmann at the one-week horizon the same year. The effect is small per period, it is largest in illiquid names, and it is fragile to costs. Lesson 3 tests it on twenty large stocks.

**Spreads.** Two assets that share a common driver, an oil producer ETF and an oil sector ETF, gold and gold miners, two soft-drink makers, tend to move together. When the ratio between them stretches, the stretch sometimes closes. Whether it closes reliably is a statistical question with a formal test, which is lesson 7, and the answer for the most popular pairs is less comfortable than most books admit.

**Volatility.** Implied volatility, measured by the VIX, is bounded below by zero and cannot rise forever. When it spikes, it decays. Of the three, this is the most dependable, and also the hardest to trade directly, because you cannot buy the VIX index itself; you buy futures or options whose prices already embed the expected decay.

**What does not revert.** The level of a broad index behaves close to a random walk with an upward drift. Over three to twelve months, stocks that have risen tend to keep rising relative to those that have fallen, which is momentum, the opposite of reversion. A reversion rule applied at the momentum horizon is a rule for buying what is about to keep falling.

## Worked example

All numbers here are computed from Yahoo Finance daily closes pulled on 2026-09-24 through the chart API with explicit `period1`/`period2` timestamps and `interval=1d`. The SPY file has 2,948 rows from 2015-01-02 to 2026-09-23, so 2,947 daily returns. VIX closes come from the same endpoint for `^VIX`.

**Daily autocorrelation.** The lag-1 autocorrelation of SPY daily returns is the correlation between today's return and yesterday's:

ρ₁ = Σ(r_t − r̄)(r_{t−1} − r̄) / Σ(r_t − r̄)² = **−0.117**

The standard error of an autocorrelation under the null of zero is roughly 1/√n = 1/√2947 = 0.018, so the t-statistic is −0.117 / 0.018 = **−6.35**. That is not chance. But the variance explained is ρ² = 0.014, or 1.4%. Yesterday tells you almost nothing about today; it just tells you that little with confidence.

**Conditional next-day returns.** Split every day by what happened the day before:

- All days (n = 2,942 with a five-day lookahead available): next-day mean **+0.051%**, positive 54.4% of the time; next five days **+0.253%**.
- After a day below −2% (n = 100): next day **+0.380%**, positive 60.0%; next five days **+0.591%**.
- After a day below −1% (n = 328): next day +0.152%, positive 55.2%; next five days +0.463%.
- After a day above +1% (n = 387): next day −0.083%; next five days +0.162%.
- After a day above +2% (n = 70): next day **−0.464%**, positive 47.1%; next five days −0.418%.

So a −2% day was followed by a next-day return seven times the unconditional average, and a +2% day by a negative one. That is the reversal. Note the sample sizes: 100 and 70 events in eleven and a half years, many of them clustered in 2018, 2020, 2022 and April 2025.

**Volatility.** Take every VIX close and look twenty trading days ahead:

- VIX below 15 (n = 1,042 days): average level 12.8, average twenty days later 14.5, change **+1.8**. SPY over the same twenty days: +0.48%.
- VIX 15 to 20 (n = 1,022): 17.2 to 17.8, change +0.6. SPY: +0.69%.
- VIX 20 to 30 (n = 706): 23.8 to 22.4, change −1.4. SPY: +1.32%.
- VIX at or above 30 (n = 158): 37.9 to 28.3, change **−9.6**. SPY: +5.17%.
- VIX at or above 40 (n = 40): 52.6 to 35.2, change **−17.4**. SPY: +7.97%.

The VIX sample mean over the period was 18.33, its median 16.64, and its maximum 82.69 on 2020-03-16. Low readings drift up, high readings fall hard: that is a series pulled toward a centre from both sides. An AR(1) fit to the VIX level gives a coefficient of 0.9616, which lesson 9 will turn into a half-life of about 18 trading days.

**The horizon where it stops.** Take the twenty large stocks used throughout this course (AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, JPM, V, UNH, LLY, XOM, COST, HD, PG, NFLX, CAT, WMT, JNJ). On each date, compute the correlation across the twenty names between a past return and a future return, then average those correlations over all dates:

- Past 1 week versus next 1 week: mean correlation **−0.024**, standard error 0.013, over 588 weeks (t = −1.84).
- Past 1 month versus next 1 month: −0.011, s.e. 0.029, 139 months (t = −0.39).
- Past 6 months (skipping the latest month) versus next month: **+0.059**, s.e. 0.031, 133 months (t = +1.90).
- Past 12 months (skipping the latest month) versus next month: +0.053, s.e. 0.033, 127 months (t = +1.64).

The sign flips as the lookback lengthens. Reversal at a week, continuation at six to twelve months, and neither effect is large in twenty mega-caps. For SPY itself, the lag-1 autocorrelation of non-overlapping 21-day returns is −0.156 on 140 observations (t = −1.85) and of 252-day returns is −0.434 on eleven observations, which is not a measurement, it is eleven numbers.

## Table

| Condition (SPY, 2015-01-02 to 2026-09-23) | n | Next-day mean | Next day positive | Next 5 days mean |
|---|---|---|---|---|
| All days | 2,942 | +0.051% | 54.4% | +0.253% |
| Previous day < −2% | 100 | +0.380% | 60.0% | +0.591% |
| Previous day < −1% | 328 | +0.152% | 55.2% | +0.463% |
| Previous day < 0 | 1,336 | +0.083% | 55.8% | +0.335% |
| Previous day > 0 | 1,600 | +0.024% | 53.2% | +0.185% |
| Previous day > +1% | 387 | −0.083% | 51.7% | +0.162% |
| Previous day > +2% | 70 | −0.464% | 47.1% | −0.418% |

Source: Yahoo Finance daily closes, computed by the course.

## What the numbers do and do not license

The table says that extreme days revert on average. It does not say that buying every −2% close is a business. A +0.38% average next-day return with a 60% hit rate is real, but the hundred events include 2020-03-12 (SPY −9.57%, then +8.55% the next day) and 2020-03-16 (−10.94%, then +5.40%): a handful of pandemic days carry a lot of the mean. Remove the 24 events from 2020 and the next-day average after a −2% day falls from +0.380% to +0.109% with a 56.6% hit rate, although the five-day average holds up at +0.718%. Add a round-trip cost and the ordinary-day version, +0.05%, disappears entirely.

The lesson to carry forward is the shape of the evidence. Reversion is strongest where there is a hard boundary (volatility cannot go below zero), next strongest at very short horizons after very large moves, weak and noisy in the ordinary cross-section, and absent or reversed at the horizons where momentum lives. Every rule in this course is built inside that shape, and the ones that ignore it, like shorting a strong stock because it is "overbought", are the ones the tests will show losing money.

## Sources

- Jegadeesh, N. (1990). Evidence of predictable behavior of security returns. *Journal of Finance*, 45(3), 881–898. https://doi.org/10.1111/j.1540-6261.1990.tb05110.x
- Lehmann, B. N. (1990). Fads, martingales, and market efficiency. *Quarterly Journal of Economics*, 105(1), 1–28. https://doi.org/10.2307/2937816
- Jegadeesh, N. and Titman, S. (1993). Returns to buying winners and selling losers: implications for stock market efficiency. *Journal of Finance*, 48(1), 65–91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/ and Cboe VIX index page: https://www.cboe.com/tradable_products/vix/

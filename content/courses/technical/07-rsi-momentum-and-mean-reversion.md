---
{
  "title": "RSI: Momentum, the 2-Period Variant, and Mean Reversion",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "RSI is computed from:", "opts": ["The ratio of volume on up days to volume on down days", "The ratio of the smoothed average gain to the smoothed average loss over n periods, rescaled to 0–100", "The distance from the 200-day moving average", "The number of up days in the last n days"], "correct": 1, "explain": "RS = average gain / average loss (Wilder smoothing), and RSI = 100 − 100 / (1 + RS)."},
    {"q": "On 12 October 2022, SPY's 2-period average gain was 0.1291 and average loss 2.3120. The RSI(2) was:", "opts": ["94.7", "34.6", "5.3", "50.0"], "correct": 2, "explain": "RS = 0.1291 / 2.3120 = 0.0558; RSI = 100 − 100 / 1.0558 = 5.29."},
    {"q": "In the ten-year SPY check, the average 5-day forward return after RSI(2) < 10 was +0.72% on 229 cases. What is the correct comparison to judge it?", "opts": ["Zero", "The unconditional 5-day forward return of +0.28%", "The 200-day SMA", "The RSI(14) value"], "correct": 1, "explain": "Every conditional return must be compared with the base rate. Here the conditional (+0.72%) is about 2.6 times the base rate (+0.28%), before costs."},
    {"q": "The conventional RSI(14) > 70 'overbought' condition, over the same ten years, was followed by a 5-day forward return of:", "opts": ["−0.07% on 246 cases, marginally below the base rate", "+3.0%", "−5.0%", "It never occurred"], "correct": 0, "explain": "Overbought on an index that trends up most of the time is a weak sell signal at best. Chong and Ng (2008) found RSI signals generated small or negative profits on the FT30 after costs."},
    {"q": "Which statement about RSI(2) and RSI(14) is accurate?", "opts": ["They measure different things", "They apply the same formula with different smoothing lengths; RSI(2) is dominated by the last two closes and swings between extremes constantly", "RSI(2) is for stocks and RSI(14) is for indexes", "RSI(14) cannot go below 30"], "correct": 1, "explain": "Same formula, different n. Shorter n means less smoothing and far more frequent extreme readings, which is why RSI(2) is used as a short-term mean-reversion trigger."}
  ],
  "task": "Compute RSI(2) and RSI(14) on your ticker in a spreadsheet, count the days below 10 and below 30 respectively over the past two years, and record the 5-day forward return after each against the base rate."
}
---

The Relative Strength Index measures the balance between recent gains and recent losses on a 0 to 100 scale. It was introduced by J. Welles Wilder in 1978 with a 14-period setting and "overbought above 70, oversold below 30" thresholds that have been repeated ever since. This lesson covers the formula, the difference between the 14-period and 2-period versions, and what ten years of SPY data say about each as a mean-reversion trigger.

## The formula

For each period, compute the change in close. Split it into a gain (the change if positive, else zero) and a loss (the absolute change if negative, else zero). Then smooth both series with Wilder's method, which is an exponential average with k = 1/n:

- Average gain today = Average gain yesterday + (1/n) × (Gain today − Average gain yesterday)
- Average loss today = Average loss yesterday + (1/n) × (Loss today − Average loss yesterday)

Then RS = Average gain / Average loss, and **RSI = 100 − 100 / (1 + RS)**.

If losses are zero, RSI is 100. If gains are zero, RSI is 0. If gains and losses are equal, RS = 1 and RSI = 50. The rescaling makes RSI bounded and comparable across instruments, which is its main advantage over raw momentum.

Two details matter in practice. First, Wilder's smoothing with k = 1/n is slower than the standard EMA with k = 2/(n+1); an RSI(14) behaves like a 27-period EMA. Second, because the smoothing is recursive, the value on any day depends on the entire history, so two calculators seeded on different start dates can differ slightly for the first hundred bars or so.

## RSI(14): the conventional reading

The standard interpretation is that RSI above 70 signals an overbought market likely to fall and below 30 an oversold market likely to rise. Two things are wrong with this on an equity index. First, an index that rises in most years spends far more time above 70 than below 30, so the sell signal fires constantly in uptrends. Second, RSI(14) is smooth enough that by the time it reaches 30, price has usually fallen for weeks and the fastest part of any rebound may already be over.

Chong and Ng (2008) tested RSI and MACD rules on the London FT30 index over 60 years and found RSI rules produced returns that were not significantly better than buy-and-hold once costs were included. That is representative of the academic record: the oscillator describes, it does not reliably forecast, and the thresholds are conventions rather than findings.

## RSI(2): the short-term variant

Set n = 2 and the same formula becomes almost entirely a function of the last two closes. It swings from below 10 to above 90 several times a month. Connors and Alvarez popularised RSI(2) in 2009 as a mean-reversion trigger: buy when RSI(2) is very low and price is above its 200-day moving average (so you are buying dips in an uptrend), and exit a few days later when price closes above a short moving average.

The logic connects to something you saw in Lesson 1: SPY daily returns have a lag-1 autocorrelation of about −0.13. Sharp short-term declines have, on average, been followed by partial rebounds. RSI(2) is a way of identifying "sharp short-term decline" objectively. Whether the rebound is large enough to trade is the question the worked example answers for one ticker and one decade.

## Worked example

SPY, daily closes from Yahoo Finance historical data, September 2016 to September 2026. First the arithmetic for one day, then the conditional statistics.

**12 October 2022** (the lowest close of the 2022 bear market). The closes: 6 October 373.20, 7 October 362.79, 10 October 360.02, 11 October 357.74, 12 October 356.56. The daily changes: −10.41, −2.77, −2.28, −1.18. Four consecutive losses, no gains.

For RSI(2), Wilder smoothing with k = 1/2. On 11 October the running values were: average gain 0.2582, average loss 3.4440. Update for 12 October (gain 0, loss 1.18):

- Average gain = 0.2582 + 0.5 × (0 − 0.2582) = **0.1291**
- Average loss = 3.4440 + 0.5 × (1.18 − 3.4440) = **2.3120**
- RS = 0.1291 / 2.3120 = **0.0558**
- RSI(2) = 100 − 100 / (1 + 0.0558) = 100 − 94.71 = **5.29**

For RSI(14) on the same day: average gain 1.6949, average loss 3.1970, RS = 0.5302, RSI(14) = 100 − 100 / 1.5302 = **34.65**. The 14-period reading was not even "oversold" by the conventional 30 threshold at the bear-market low. For comparison, on 8 April 2025, after a 7.90-point drop, RSI(2) was 1.67 and RSI(14) was 21.42.

**Conditional statistics.** For each day, the forward 1-day and 5-day returns (close to close). Base rates over 2,512 days: 1-day +0.057%, 5-day **+0.281%**, and 61.0% of 5-day forward returns were positive.

The conditional-statistics table under the Table heading below gives the figures. Read it against the base rate, row by row.

RSI(2) < 10 was followed by a 5-day return of +0.724%, which is 0.724 / 0.281 = **2.6 times** the base rate, on 229 cases. That is the mean-reversion tendency, and it is the clearest signal in the table. The 200-day filter, which is meant to improve it, made it worse in this sample: +0.474% on 136 cases. The filter removed the 93 signals that fired below the 200-day, and those were the best ones, because they included the October 2022 and April 2025 lows. Whether that is a property of the filter or of this particular decade is exactly the kind of question you cannot answer from one sample.

RSI(14) < 30 looks excellent at +2.124% and 82.5% winners, but it fired only **40 times in ten years**, and those 40 days cluster in a handful of episodes (December 2018, March 2020, 2022, April 2025). Effectively it is four or five events, not forty. Do not build on it.

The overbought rows are what the literature predicts: RSI(14) > 70 was followed by a slightly negative 5-day return (−0.066%) with 56.1% positive, marginally worse than the base rate. RSI(2) > 90 was indistinguishable from the base rate. Selling an index because it is "overbought" has, in this decade, been a way to sit out a rising market.

None of these figures include costs, slippage or the fact that you cannot buy at the close that generated the signal. Lesson 12 turns the RSI(2) row into a rule with an entry, an exit and a cost model, and shows how much of the +0.724% survives.

## Table

SPY, September 2016 to September 2026, forward close-to-close returns after each condition.

| Condition | Days | Avg 1-day fwd | Avg 5-day fwd | 5-day fwd > 0 |
|---|---|---|---|---|
| All days (base rate) | 2,512 | +0.057% | +0.281% | 61.0% |
| RSI(2) < 10 | 229 | +0.369% | +0.724% | 65.9% |
| RSI(2) < 10 and close > 200-day SMA | 136 | +0.181% | +0.474% | 64.0% |
| RSI(2) > 90 | 477 | +0.054% | +0.243% | 61.2% |
| RSI(14) < 30 | 40 | +1.323% | +2.124% | 82.5% |
| RSI(14) > 70 | 246 | +0.013% | −0.066% | 56.1% |

The two columns to carry forward are "Days" (a signal that fires 40 times in ten years is not a strategy) and the comparison of each "Avg 5-day fwd" with the base-rate row.

## Using RSI

Use RSI(2) as a **trigger** for short-term mean reversion, not as a forecast. It tells you that the last two days were sharply down, which on an index has tended to be followed by a small rebound. The rebound is small, so costs matter, and the exit rule matters more than the entry.

Use RSI(14) as a **descriptor**. Divergence between price and RSI(14) (a new price high with a lower RSI high) is a description of decelerating momentum; the evidence that it forecasts a reversal is anecdotal.

Do not use fixed thresholds without checking the base rate. "Below 30" on a stock that spends 20% of its time there means something different from "below 30" on an index that spends 1.6% of its time there.

## Sources

- Chong, T. T.-L., & Ng, W.-K. (2008). "Technical analysis and the London stock exchange: testing the MACD and RSI rules using the FT30." *Applied Economics Letters*, 15(14). https://doi.org/10.1080/13504850600993598
- Park, C.-H., & Irwin, S. H. (2007). "What Do We Know About the Profitability of Technical Analysis?" *Journal of Economic Surveys*, 21(4). https://doi.org/10.1111/j.1467-6419.2007.00519.x
- CFA Institute. "Technical Analysis" (Level I curriculum refresher reading; defines RSI and its conventional thresholds). https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/technical-analysis
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

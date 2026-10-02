---
{
  "title": "Volatility Regimes: VIX Levels, Term Structure, Realised vs Implied, and What SPY Did at VIX 30",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Since 1990 the VIX has closed above 30 on about 8% of sessions and below 15 on about 32%. Months whose average VIX exceeded 30 saw SPY return a mean of -1.12% with a standard deviation of 8.15%; months averaging below 15 returned +1.70% with a standard deviation of 2.24%. What does this establish?", "opts": ["High VIX predicts losses", "High VIX coincides with losses and, above all, with dispersion; the contemporaneous relationship says nothing about what follows", "Low VIX is dangerous", "The VIX is useless"], "correct": 1, "explain": "The month's average VIX is computed from the same days as the month's return. It describes the month; it cannot be used to trade it, because you only know the average at the end."},
    {"q": "Using the VIX at the prior month-end instead, months that began with the VIX above 30 returned a mean of +1.93% (median +4.76%, 72% positive) and months that began below 15 returned +0.75%. Which conclusion is honest?", "opts": ["Buy when the VIX is above 30; it is a reliable signal", "The VIX is contrarian and should be faded aggressively", "The two results contradict each other", "A high VIX at month-end has historically been followed by above-average returns on average, in only 32 months, with a standard deviation of 7.7%, and the worst of those months was -16.5%; the mean is not the trade"], "correct": 3, "explain": "Both results are true and they do not contradict: high VIX arrives with the losses and is followed, on average, by the rebound. But 32 observations with a 7.7% standard deviation give a standard error near 1.4%, and one of them was October 2008."},
    {"q": "The VIX exceeded trailing 21-day realised volatility on 86% of sessions since 1993, by a mean of 3.7 points. This gap is:", "opts": ["The volatility risk premium: option sellers are paid, on average, for bearing the risk that realised volatility jumps", "An error in the VIX", "Proof that the VIX is too high", "Zero on average"], "correct": 0, "explain": "The VIX also exceeded the NEXT 21 days' realised volatility on 83% of sessions by the same 3.7 points. Implied volatility is a forecast plus an insurance premium; the premium is the 3.7."},
    {"q": "Vol clustering in the data: the unconditional probability of a daily SPY move larger than 2% is 7.2%; conditional on the prior day also exceeding 2% it is 21.1%. Which trading implication follows?", "opts": ["Big moves are random", "You should always buy after a big down day", "A large move today triples the odds of a large move tomorrow, in either direction: position size should fall after a shock even if you have no view on direction", "The market trends after big moves"], "correct": 2, "explain": "The lag-1 autocorrelation of absolute returns is +0.28; of signed returns it is -0.08. Magnitude persists, direction barely does. That is the empirical basis for volatility-based sizing in lesson 10."},
    {"q": "VIX/VIX3M above 1 (backwardation) occurred on 10.9% of sessions from 2006 to 2026. SPY's mean return over the following 21 sessions was +1.77% after backwardation and +0.93% after contango, with standard deviations of 7.97% and 4.10%. What is the term structure telling you?", "opts": ["Backwardation is bullish", "Contango is bearish", "Backwardation marks acute stress: the following month has had a higher mean and nearly double the dispersion, which is the same shape as the high-VIX-month result", "The term structure is noise"], "correct": 2, "explain": "The near-term index above the 3-month index means the market is pricing the next 30 days as more dangerous than the next 90, which happens only in a shock. What follows a shock is wide in both directions."}
  ],
  "task": "Compute SPY's trailing 21-session realised volatility (annualised standard deviation of daily returns) for the latest session and write it next to the VIX close on the same day."
}
---

## Two volatilities

Realised volatility is what the market did: the standard deviation of daily returns over a window, annualised by multiplying by the square root of 252. Implied volatility is what option prices say the market will do. The VIX is the best-known implied measure: Cboe computes it from the prices of S&P 500 options across a strip of strikes, as the 30-day expected volatility under the risk-neutral measure, and publishes it in annualised percentage points. A VIX of 20 means the options market is pricing a one-standard-deviation move of about 20% / sqrt(12) = 5.8% over the next month.

The two are related but not equal, and the difference is where much of the information lives. Since 1993 the VIX has closed above the trailing 21-session realised volatility on 86% of sessions, by 3.7 points on average. It has also exceeded the following 21 sessions' realised volatility on 83% of sessions, by the same 3.7 points. That persistent gap is the volatility risk premium: option sellers are paid, on average, for bearing the risk that realised volatility jumps. It is also the reason "the VIX is high" is not the same as "the market will be volatile"; the VIX is a forecast plus an insurance premium.

## Levels

The VIX's long-run distribution is skewed, and the skew is the first thing to internalise: the index cannot go below zero, spends most of its life between 12 and 22, and makes its excursions upward, fast, in clusters. Over 9,284 sessions from 1990-01-02 to 2026-09-29 (FRED VIXCLS), the mean is 19.4, the median 17.6, the maximum 82.69 on 2020-03-16. It closed below 15 on 32% of sessions and above 30 on 8%. The course uses three levels as regime boundaries: 15, below which the market is calm; 25, above which it is stressed (the classifier's threshold in lesson 9); and 30, above which it is in an acute episode. There is nothing sacred about any of them; they are round numbers that sit near the 32nd, 85th and 92nd percentiles.

What SPY did at those levels is the worked example, and the answer depends entirely on whether you read the VIX before or after the month it describes.

## Term structure

Cboe also publishes a 3-month index, VIX3M. Normally VIX3M is above VIX (contango), because uncertainty accumulates with horizon and because the premium is larger for longer-dated protection. From 2006-07-17 to 2026-09-29 the ratio VIX/VIX3M averaged 0.907 and exceeded 1 on 10.9% of sessions. When it exceeds 1 (backwardation) the market is pricing the next 30 days as more dangerous than the next 90, which happens only during a shock. The five highest ratios in the sample were all in October 2008, peaking at 1.43 on 2008-10-24 with the VIX at 79.1 and VIX3M at 55.3.

Backwardation is a cleaner acute-stress flag than any single VIX level, because it is self-normalising: a VIX of 30 with VIX3M at 33 is a nervous market, a VIX of 30 with VIX3M at 26 is a market in the middle of something. It is also rarer than a VIX above 25 (10.9% of sessions since 2006, against 17.2% of sessions with the VIX above 25 in the FRED series since 1990), which makes it a stricter gate for the exposure caps in lesson 10.

## Clustering

Volatility clusters: large moves follow large moves. The measurement is simple. The unconditional probability that SPY moves more than 2% in a session (either direction) is 7.2% over 1993-2026. Conditional on the prior session having moved more than 2%, it is 21.1%, nearly three times higher. The lag-1 autocorrelation of absolute daily returns is +0.28; of signed returns it is -0.08. Magnitude persists strongly from one day to the next; direction barely does, and if anything reverses.

This is the single most robust fact in the course, and it is why volatility is the axis a trader cannot ignore. It says that the size of tomorrow's move is forecastable from today's even when its sign is not, which is exactly the information a sizing rule can use.

## Worked example

Data: `^VIX` daily closes from the Yahoo Finance chart API (9,256 rows, 1990-01-02 to 2026-09-30, last row dropped) for the monthly and daily tests aligned to SPY; FRED VIXCLS (9,284 observations, same span) for the level distribution; `^VIX3M` from Yahoo (5,084 rows from 2006-07-17); SPY adjusted closes as in lesson 1. All monthly tests use calendar months from 1993-02 to 2026-08, 403 complete months.

Monthly return: SPY's adjusted close on the last session of the month divided by the adjusted close on the last session of the prior month, minus one. Two ways to attach a VIX reading to a month.

Contemporaneous: the mean VIX close over the month's sessions. Months with mean VIX below 15 (128 months): mean return +1.70%, median +1.97%, standard deviation 2.24%, 80% positive, worst -3.5%. Mean VIX 15 to 20 (124): +1.23%, standard deviation 3.54%, 69% positive. Mean VIX 20 to 30 (119): +0.42%, standard deviation 4.86%, 50% positive. Mean VIX above 30 (32): -1.12%, median +0.21%, standard deviation 8.15%, 50% positive, worst -16.5% (October 2008), best +12.7% (April 2020).

Predictive: the VIX close on the last session of the prior month. Prior-end VIX below 15 (127 months): +0.75%, standard deviation 2.61%, 69% positive. 15 to 20 (124): +0.95%, 3.38%, 71% positive. 20 to 30 (120): +0.91%, 5.13%, 54% positive. Above 30 (32): +1.93%, median +4.76%, standard deviation 7.72%, 72% positive, worst -16.5% (October 2008, which began with the VIX at 39.4 after September), best +12.7% (April 2020, which began at 53.5).

The standard error of the above-30 predictive mean is 7.72% / sqrt(32) = 1.36%, so the +1.93% mean is about 1.4 standard errors above zero and about 0.9 standard errors above the +0.75% calm-month mean. It is suggestive, not established, and the 32 months are not independent: eight of them are October 2008 through May 2009, and four more are March through July 2020. Treat the predictive result as a reason not to sell into a VIX spike, not as a reason to buy one.

Realised versus implied: trailing 21-session realised volatility on day t is the sample standard deviation of the 21 daily returns ending on t, times sqrt(252), times 100. VIX minus trailing realised, over 8,453 sessions: mean +3.68 points, positive on 86% of sessions. VIX on day t minus realised over days t+1 to t+21: mean +3.68, positive on 83%, correlation between the two 0.72. Realised volatility's extremes: 94.5% annualised on 2008-10-28, 3.4% on 2017-10-11.

Term structure: after sessions with VIX/VIX3M above 1 (553 sessions), SPY's mean 21-session forward return was +1.77% with a standard deviation of 7.97%; after contango sessions (4,509), +0.93% with a standard deviation of 4.10%.

## Chart

![VIX close on the last session of each month, February 1993 to August 2026, from the Yahoo Finance ^VIX series, with the 15 (calm) and 30 (acute) regime lines and the October 2008 (59.9), August 2011, March 2020 (53.5) and September 2022 month-ends annotated.](figures/vix-regimes.svg)

The chart shows the shape that the monthly tables quantify. Sessions above 30 are rare and arrive in clusters: 1997-98, 2001-03, 2008-09, 2010-11, 2020, 2022 and April 2025, thirty-two months in all, most of them in three episodes. Between the clusters the index spends years under 20. That is the regime structure: long calm states, short violent ones, and the transitions are where the sizing decisions in lesson 10 earn or lose their keep.

## Sources

- Cboe, VIX Index methodology and white paper: https://www.cboe.com/tradable_products/vix/vix_index_methodology/
- Cboe, Cboe 3-Month Volatility Index (VIX3M): https://www.cboe.com/tradable_products/vix/vix3m/
- Federal Reserve Bank of St. Louis, FRED VIXCLS: https://fred.stlouisfed.org/series/VIXCLS
- Bollerslev, T. (1986), "Generalized Autoregressive Conditional Heteroskedasticity", Journal of Econometrics 31(3), https://doi.org/10.1016/0304-4076(86)90063-1

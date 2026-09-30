---
{
  "title": "Half-Life of Reversion, Holding Period and the Time Stop",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Regressing the daily change in a spread on its lagged level gives a slope of −0.03687. The half-life of a deviation is:", "opts": ["3.7 days", "36.9 days", "ln(2) / 0.03687 = 18.8 trading days", "0.5 days"], "correct": 2, "explain": "The slope is −λ, the fraction of the deviation that decays per day. Half-life = ln(2) / λ. For the XLE-on-XOM spread that is 18.8 trading days, about four weeks."},
    {"q": "For the XOP-on-XLE spread the same regression gave a slope of −0.00665 with a standard error of 0.00513 (t = −1.30) and a half-life of 104 days. The correct reading is:", "opts": ["The spread reverts in 104 days", "The point estimate is 104 days but the slope is not statistically different from zero, so the half-life is not distinguishable from infinite; there is no established reversion to set a holding period by", "The spread reverts faster than XLE/XOM", "104 days is a fast half-life"], "correct": 1, "explain": "A half-life is only meaningful when the slope it is computed from is significant. A t of −1.30 is the regression form of lesson 7's failed cointegration test."},
    {"q": "A common time-stop rule is to exit a reversion trade after two to three half-lives. For a spread with a 19-day half-life that is about:", "opts": ["2 to 3 days", "190 days", "One year", "40 to 60 trading days"], "correct": 3, "explain": "After two half-lives the expected remaining deviation is a quarter of the entry deviation, after three it is an eighth. If the spread has not come most of the way back by then, the fitted process is not the one you are in."},
    {"q": "The VIX level's regression slope was −0.0384 with t = −7.59, half-life 18 days. Compared with the XLE/XOM spread's 18.8-day half-life, the difference is:", "opts": ["No difference at all", "Similar speed, but the VIX estimate rests on 2,947 observations and a t of −7.59 while the spread's rests on 500 and a t of −3.06; the VIX number is far more reliable", "The VIX is slower", "The spread is more reliable because it is an ETF"], "correct": 1, "explain": "Two half-lives can be numerically equal and differ enormously in how much you should trust them. Sample size and the t-statistic on the slope are what tell you which."},
    {"q": "The empirical average |z| path after a 2 s.d. crossing for XLE/XOM was 2.29, 1.76, 1.32, 1.24, 0.55 at 0, 5, 10, 20 and 30 days, against a fitted 2.00, 1.66, 1.38, 0.96, 0.66. Why should you not read too much into how well they match?", "opts": ["Because the fit is wrong", "Because the empirical path averages only six crossings, all from the same window the slope was fitted on; it is in-sample and small", "Because the VIX is not included", "Because 30 days is too short"], "correct": 1, "explain": "Six events cannot validate a model; they can only fail to contradict it. The check is worth doing because a gross mismatch would be informative, not because a match is proof."}
  ],
  "task": "Fit the change-on-lagged-level regression to your own spread, compute the half-life, and write down whether the slope's t-statistic is beyond −3."
}
---

If a spread reverts, the next question is how fast. Speed decides everything practical: how long you expect to hold, when a trade has taken too long and should be abandoned, and whether the reversion is fast enough to beat the borrow cost of the short leg. The tool is the half-life of an autoregressive process. This lesson fits it to two spreads, one that passed near the cointegration threshold and one that did not, and shows why a half-life without a t-statistic is a number without meaning.

## The model

Treat the spread as a discrete Ornstein-Uhlenbeck process, which is the continuous-time version of the AR(1) from lesson 2:

Δs_t = a + b·s_{t−1} + ε_t

If b < 0, a fraction λ = −b of any deviation is expected to close each day. The deviation left after k days is (1 − λ)^k ≈ e^{−λk} of the starting deviation, and the half-life, the number of days for half of it to close, is:

half-life = ln(2) / λ

The regression is the same one the Dickey-Fuller test uses; the slope b is the γ of lesson 7. The test asks whether b is negative enough to believe; the half-life asks, if you believe it, how fast the process runs. Never compute the second without looking at the first.

## Worked example

Data: Yahoo Finance daily closes, `interval=1d`, pulled 2026-09-24. Both spreads are residuals from the lesson 7 regressions on 2023-09-22 to 2025-09-22 (501 days, 500 daily changes).

**XLE on XOM** (the pair that reached the 10% level). Regress Δs_t on s_{t−1}:

b = **−0.03687**, standard error 0.01205, t = **−3.06**
λ = 0.03687; half-life = ln(2) / 0.03687 = 0.6931 / 0.03687 = **18.8 trading days**

About four weeks. After 19 days, half of a deviation is expected to be gone; after 38 days, three quarters; after 56 days, seven eighths. The spread's standard deviation is 0.0245 and the daily change's standard deviation is 0.00665. A consistency check: a stationary AR(1) with φ = 1 − λ = 0.9631 and shock standard deviation 0.00665 has a long-run standard deviation of 0.00665 / √(1 − 0.9631²) = 0.00665 / 0.2692 = 0.0247, which matches the measured 0.0245. The fitted process is internally coherent.

**XOP on XLE** (the pair that failed). Same regression:

b = **−0.00665**, standard error 0.00513, t = **−1.30**
λ = 0.00665; half-life = 0.6931 / 0.00665 = **104 trading days**

Five months as a point estimate. But the t-statistic says the slope is 1.3 standard errors from zero; a slope of zero, half-life infinite, is comfortably inside the interval. The same consistency check gives 0.00585 / √(1 − 0.9934²) = 0.0509 against a measured 0.0510, so the numbers hang together, but they hang together around a process that may simply be a random walk. Lesson 8's trade sat for 179 days without reaching zero. With a 104-day half-life you would have expected about 70% of the entry deviation to close in that time; the deviation grew instead.

**Two reference points.** The VIX level over 2015-2026: b = −0.0384, t = **−7.59**, half-life **18.0 days**, on 2,947 observations. PEP on KO over 2015-2019: b = −0.01518, t = −3.22, half-life 45.7 days. The VIX and XLE/XOM half-lives are nearly equal; the VIX's rests on six times the data and a t-statistic two and a half times as large.

**Empirical decay.** Within the formation window, find every day on which |z| first crossed 2 and average |z| over the following 40 days. XLE/XOM, six crossings: |z| = 2.29 at day 0, 1.76 at day 5, 1.32 at day 10, 1.24 at day 20, 0.55 at day 30, 0.67 at day 40. The fitted curve 2·e^{−0.03687k}: 2.00, 1.66, 1.38, 0.96, 0.66, 0.46. XOP/XLE, seven crossings: 2.09, 1.79, 1.62, 1.29, 0.89, 0.86 against a fitted 2.00, 1.93, 1.87, 1.75, 1.64, 1.53. The failed pair's in-sample crossings actually reverted faster than its own fit, which is what a handful of lucky episodes inside a random walk looks like; the trading year in lesson 8 was the out-of-sample version.

## Chart

![Expected decay of a 2 standard-deviation spread deviation. Fitted exponential curves for XLE on XOM (half-life 18.8 days) and XOP on XLE (half-life 104 days, slope not significant), plus the in-sample average |z| path after six XLE/XOM crossings. Formation window 2023-09-22 to 2025-09-22. Source: Yahoo Finance daily closes, computed by the course.](figures/spread-half-life-fit.svg)

## From half-life to rules

**Expected holding period.** A trade entered at 2σ and exited at 0 does not, in the model, ever reach exactly zero in expectation; the deviation halves and halves. In practice the noise carries it across. Simulation and the Avellaneda-Lee results both put the typical round trip at one to two half-lives for a 2σ/0 rule. For XLE/XOM, expect three to eight weeks.

**Time stop.** If after two to three half-lives the spread has not closed most of the gap, the process you fitted is not the process you are in. For an 18.8-day half-life, that is 40 to 60 trading days. Lesson 10 uses 60. For the 104-day half-life it would be 200 to 300 days, which is the first sign that the pair is untradeable at retail scale: a year of capital and borrow tied up waiting for a reversion the test could not confirm.

**Borrow hurdle.** Borrow at 0.5% per year on the short leg costs 0.5% × (holding days / 252) of that leg. For a 40-day trade that is 0.08% of the short notional, small against a 2σ move of 2 × 0.0245 = 4.9% in the spread. For a 200-day trade it is 0.40%, against a 2σ move of 10.2%. The ratio of expected gain to carry gets worse as the half-life lengthens, and the slower pair also carries the risk that it is not reverting at all.

**Re-estimation interval.** The half-life also tells you how often to refit. A spread with a 19-day half-life produces roughly a dozen independent reversion episodes a year, enough to re-estimate the slope every six to twelve months and notice if it has drifted. A 104-day half-life produces two or three, so a refit on the same schedule is fitting to noise, and a change in the estimate tells you nothing until years have passed.

**Bands.** The half-life also argues against tightening the entry band to chase more trades. A 1σ entry on a 19-day half-life spread expects to capture 1σ of deviation over the same two to three half-lives as the 2σ entry, so it halves the expected gain per trade while leaving costs unchanged. Wider bands with fewer trades are the natural setting for a slow, expensive-to-hold instrument.

## The number that matters

Half-life is downstream of the test. Report the slope, its standard error and its t-statistic before the half-life, and if the t-statistic is not beyond about −3, do not quote a half-life at all. The XOP/XLE figure of 104 days is a true calculation and a false promise: it is the half-life of a process that, on the evidence, might not exist.

## Sources

- Uhlenbeck, G. E. and Ornstein, L. S. (1930). On the theory of the Brownian motion. *Physical Review*, 36(5), 823–841. https://doi.org/10.1103/PhysRev.36.823
- Avellaneda, M. and Lee, J.-H. (2010). Statistical arbitrage in the US equities market. *Quantitative Finance*, 10(7), 761–782. https://doi.org/10.1080/14697680903124632
- Engle, R. F. and Granger, C. W. J. (1987). Co-integration and error correction: representation, estimation, and testing. *Econometrica*, 55(2), 251–276. https://doi.org/10.2307/1913236
- Yahoo Finance historical data: XOM https://finance.yahoo.com/quote/XOM/history/ and XLE https://finance.yahoo.com/quote/XLE/history/

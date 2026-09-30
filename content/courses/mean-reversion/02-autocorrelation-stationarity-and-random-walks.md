---
{
  "title": "Autocorrelation, Stationarity and Random Walks",
  "duration": "18 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "A series is stationary, in the sense that matters for reversion trading, when:", "opts": ["It never changes", "Its mean and variance do not depend on time, so a deviation from the mean is expected to shrink", "It has positive drift", "Its daily changes are large"], "correct": 1, "explain": "A stationary series has a fixed centre and a fixed spread; the further it is from centre, the more it is expected to move back. A random walk has no centre, so 'far from the mean' has no meaning for it."},
    {"q": "The Dickey-Fuller regression on SPY's log price (2015-2026) gave a coefficient on the lagged level of about −0.00001 with t = −0.01, against a 5% critical value of −2.86. Conclusion:", "opts": ["SPY's price is stationary and reverts", "You cannot reject that SPY's log price is a random walk; there is no evidence its level pulls back toward any mean", "SPY has negative drift", "The test failed to run"], "correct": 1, "explain": "A unit-root test needs a t-statistic more negative than the critical value to reject the random walk. −0.01 is nowhere near −2.86. The level of a broad index is the canonical example of what not to trade for reversion."},
    {"q": "The variance ratio VR(20) for SPY daily log returns was 0.800. That means:", "opts": ["20-day returns have 80% of the variance a random walk would give them, consistent with negative autocorrelation in this sample", "20-day returns are 80% predictable", "Returns are trending", "Variance grows faster than linearly"], "correct": 0, "explain": "Under a random walk, variance scales with horizon and VR = 1. Below 1 means multi-day returns are smaller in magnitude than the sum of independent daily moves would be, which is what reversal does."},
    {"q": "The VIX level had an AR(1) coefficient of 0.9616 and an ADF t-statistic of −6.48. Compared with SPY's price:", "opts": ["VIX is the random walk and SPY is stationary", "Both are random walks", "VIX is clearly stationary (t far beyond −3.43, the 1% value) while SPY's level is not", "The two tests cannot be compared"], "correct": 2, "explain": "−6.48 rejects the unit root at any conventional level. The coefficient 0.9616 implies that about 3.8% of any deviation decays per day, a half-life near 18 trading days."},
    {"q": "The GDX-on-GLD regression residual over 2023-09-22 to 2025-09-22 had an ADF t of −1.01. Even though the two ETFs' daily returns are 0.80 correlated, the residual:", "opts": ["Is stationary because the correlation is high", "Cannot be distinguished from a random walk on this window, so there is no statistical basis for expecting the ratio to revert", "Reverts with a half-life of 5 days", "Was mis-specified"], "correct": 1, "explain": "Correlation of returns and stationarity of the spread are different properties. Two assets can move together day to day while their ratio wanders without limit. Lesson 7 makes this the centre of pairs selection."}
  ],
  "task": "Take any daily price series you follow, compute the autocorrelation of its daily returns at lags 1 through 5, and note whether any lag exceeds 2/√n in absolute value."
}
---

Lesson 1 showed you reversion by looking at averages. This lesson gives you the three tools that decide whether a series can be traded for reversion at all: autocorrelation, the variance ratio, and the unit-root test. Every one of them is applied to real data below, and the same code path is used later for pairs. If you understand the difference between a series that random-walks and one that is stationary, you will not make the most common mean-reversion mistake, which is fading something that has no mean.

## Random walk versus stationary

A random walk is p_t = p_{t−1} + ε_t. Each step is independent of the last, so the best forecast of tomorrow's level is today's level, and the uncertainty around that forecast grows with the square root of the horizon. There is no centre. If the walk is at 100 and drifts to 150, nothing about the process wants it back at 100. Buying at 150 "because it is above its mean" is buying at a number that has no special status.

A stationary AR(1) series is x_t = μ + φ(x_{t−1} − μ) + ε_t with |φ| < 1. The deviation from μ shrinks by a factor of φ each period on average. If φ = 0.96, four percent of any gap closes per day. The series has a fixed long-run mean and a fixed long-run variance, and the further it is from μ, the larger the expected move back. That expected move is the reversion trade.

Prices of individual assets are, to a first approximation, random walks with drift. Differences and ratios between related assets, and volatility, can be stationary. The whole craft is finding the second kind and not mistaking the first for it.

## The three measurements

**Autocorrelation** at lag k is the correlation between a series and itself shifted k periods. For returns, negative autocorrelation is reversal, positive is continuation. The standard error under the null of no autocorrelation is about 1/√n, so with 2,947 daily returns anything beyond ±0.037 is two standard errors away.

**Variance ratio.** Lo and MacKinlay (1988) proposed comparing the variance of q-period returns with q times the variance of one-period returns. Under a random walk, VR(q) = 1. Below 1 indicates negative autocorrelation (reversal), above 1 positive (momentum). It is more robust than any single lag because it aggregates all lags up to q.

**Unit-root test.** Dickey and Fuller (1979) proposed regressing the change in a series on its lagged level: Δy_t = a + γ·y_{t−1} + ε_t. If the series is a random walk, γ = 0. If it is stationary, γ < 0, and the more negative, the faster the reversion. The t-statistic on γ does not have the usual t distribution under the null, so it is compared with special critical values. MacKinnon (2010) tabulates them: for a series with a constant and no trend, −3.43 at 1%, −2.86 at 5%, −2.57 at 10%. Adding lagged changes to the regression (the "augmented" version) mops up short-run autocorrelation; the course uses one lag throughout.

The course's implementation of this test was checked on 2,000 simulated random walks of 500 days: the 5th percentile of the t-statistic came out at −2.85 against the tabulated −2.86, and 4.8% of the walks were wrongly rejected at that value. On 2,000 simulated AR(1) series with φ = 0.95 it rejected 96% of the time. The tool works; what matters is what you point it at.

## Worked example

Data: Yahoo Finance daily closes, `interval=1d`, pulled 2026-09-24. SPY 2015-01-02 to 2026-09-23 (2,948 closes), VIX over the same dates, GLD and GDX 2023-09-22 to 2025-09-22 (501 common dates).

**SPY log price, unit-root test.** Regress Δ(ln P_t) on ln P_{t−1} and one lagged change, n = 2,946:

γ = **−0.00001**, t = **−0.01**.

Against −2.86 at 5%, that is not close. The fitted AR(1) coefficient on the level is φ = 1 + γ = **0.99993**, with a standard error of 0.00052. One is inside the interval. There is no measurable pull of SPY's price toward any mean over this period, which is what you should expect of an index that went from 205.43 to 767.81.

**SPY daily log returns, unit-root test.** The same regression on the returns themselves gives t = **−38.46**. Returns are stationary; prices are not. Difference a random walk once and you get white noise.

**SPY variance ratios.** The daily log-return variance is 1.236 × 10⁻⁴ (standard deviation 1.112%). Sum returns over q days (overlapping windows) and compare:

- q = 2: variance 2.188 × 10⁻⁴; VR = 2.188 / (2 × 1.236) = **0.885**
- q = 5: variance 5.247 × 10⁻⁴; VR = 5.247 / (5 × 1.236) = **0.849**
- q = 10: **0.815**
- q = 20: variance 1.977 × 10⁻³; VR = 19.77 / (20 × 1.236) = **0.800**
- q = 60: **0.607**

Every ratio is below one. Multi-day SPY returns in this sample were smaller than independent daily moves would produce; the daily reversal you saw in lesson 1 compounds into a 20-day variance 20% below the random-walk benchmark. Be careful with the interpretation: this is one eleven-year sample containing 2018, 2020 and 2025, three episodes of violent drops followed by violent recoveries. Those episodes push VR down. Lo and MacKinlay's original finding on 1962–1985 weekly data was the opposite sign, VR above one, driven by small stocks. The direction of autocorrelation in index returns is not a constant of nature.

**VIX level.** AR(1) coefficient φ = **0.9616**; ADF(1) t = **−6.48** on 2,947 observations. The unit root is rejected at any level. A deviation decays at (1 − 0.9616) = 3.84% per day, a half-life of ln(2)/−ln(0.9616) = 17.7 trading days. This is what a stationary series looks like in the test.

**GDX on GLD.** Regress ln(GDX) on ln(GLD) over 2023-09-22 to 2025-09-22: intercept −3.0057, slope **1.2150** (standard error 0.0148). Daily-return correlation between the two ETFs is 0.803. Now test the residual, the part of GDX's log price not explained by GLD's:

ADF(1) t = **−1.01**.

The pairs critical value (lesson 7 explains why it differs) is −3.34 at 5%. The residual's AR(1) coefficient is 0.9881, which if taken at face value implies a half-life of 58 days, but the test says you cannot distinguish that from a random walk on 501 days. The variance ratios of the residual's changes, 0.935 at q = 2 down to 0.648 at q = 60, lean the right way, but leaning is not passing. Two ETFs whose returns are 80% correlated have a ratio that, on this window, wanders.

## Chart

![Autocorrelation of SPY daily returns at lags 1 to 10, computed from 2,947 Yahoo Finance daily closes from 2015-01-02 to 2026-09-23. Two standard errors is 0.037; lags 1, 2, 4, 6, 7, 8 and 9 exceed it and lag 5 just touches it. Source: Yahoo Finance, computed by the course.](figures/spy-daily-autocorrelation-lags.svg)

The bars show lag 1 at −0.117 as the dominant feature, then a scatter of smaller values with alternating signs. Lags 7 and 9 at +0.113 and +0.110 look interesting and are probably not: with ten lags tested, you expect one or two to cross two standard errors by chance, and there is no economic story for a seven-day cycle. The lag-1 value has a story (short-term liquidity provision, the subject of lesson 3) and a t-statistic of −6.35. Treat the rest as noise until someone shows you a reason.

## What to carry into the pairs lessons

Three rules fall out of this lesson. First, never fade a level without a unit-root test; if the test cannot reject a random walk, the "mean" you are reverting to is a number you made up. Second, high return correlation is not evidence of a stationary spread, as GDX/GLD just showed. Third, autocorrelation and variance ratios describe the sample you measured them on. SPY's VR(20) of 0.80 says daily reversal was strong from 2015 to 2026; it does not promise the same for 2027. That is why lesson 12 tests rules on data they were not fitted to.

## Sources

- Lo, A. W. and MacKinlay, A. C. (1988). Stock market prices do not follow random walks: evidence from a simple specification test. *Review of Financial Studies*, 1(1), 41–66. https://doi.org/10.1093/rfs/1.1.41
- Dickey, D. A. and Fuller, W. A. (1979). Distribution of the estimators for autoregressive time series with a unit root. *Journal of the American Statistical Association*, 74(366), 427–431. https://doi.org/10.1080/01621459.1979.10482531
- MacKinnon, J. G. (2010). Critical values for cointegration tests. Queen's Economics Department Working Paper 1227. https://www.econ.queensu.ca/sites/econ.queensu.ca/files/wpaper/qed_wp_1227.pdf
- Yahoo Finance historical data pages for SPY, GLD and GDX: https://finance.yahoo.com/quote/GDX/history/

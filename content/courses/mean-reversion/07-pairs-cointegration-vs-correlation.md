---
{
  "title": "Pairs Trading: Cointegration Versus Correlation",
  "duration": "19 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "XOP and XLE had a daily-return correlation of 0.945 over 2023-09-22 to 2025-09-22, yet the Engle-Granger test on their log prices gave t = −1.23 against a 5% critical value of −3.34. This means:", "opts": ["The pair is cointegrated because the correlation is high", "The two ETFs move together day to day, but the gap between them shows no statistically detectable tendency to close; on this window it is a random walk", "The test is broken", "XOP should be shorted"], "correct": 1, "explain": "Correlation is about daily co-movement; cointegration is about whether a fixed combination of the levels stays bounded. Two assets can have both high correlation and a drifting ratio, and that is what the most popular energy pair showed."},
    {"q": "The hedge ratio of XOP on XLE was 2.21 over 2015-2019, 2.38 over 2018-2019 and 1.27 over 2023-2025. The practical consequence is:", "opts": ["The 2015 ratio is the right one", "A pair position built on any of these ratios is only neutral to the common factor if the ratio holds during the trade; when it drifts, the 'spread' includes a directional bet you did not intend", "Hedge ratios do not matter", "XOP tracks XLE exactly"], "correct": 1, "explain": "The ratio nearly halved between windows. A spread hedged at 2.38 in 2020 was heavily over-hedged in XLE, which is part of why lesson 10's 2020 trade went to 14 standard deviations."},
    {"q": "Of the seven pairs tested on the two-year window, how many passed the cointegration test at the 5% level?", "opts": ["All seven", "Four", "One", "None"], "correct": 3, "explain": "None passed at 5%. XLE on XOM came closest (t = −3.13, past the 10% value of −3.04). The pairs that appear in every textbook did not pass on recent data, which is the honest starting point for lesson 8."},
    {"q": "Regressing PEP on KO over 2023-2025 gave a hedge ratio of −0.54. What does a negative hedge ratio tell you?", "opts": ["That PEP and KO are cointegrated", "That over that window PEP fell while KO rose, so the best straight-line fit slopes down; a 'pair' with a negative ratio is two longs or two shorts, not a spread, and should be discarded", "That you should buy both", "That the regression should be run the other way"], "correct": 1, "explain": "A spread needs a positive ratio so that one leg hedges the other. PEP dropped from 175.27 to 141.03 while KO rose from 57.60 to 66.21; there is no common factor to trade in that."},
    {"q": "The Engle-Granger critical values (−3.34 at 5%) are more negative than the ordinary Dickey-Fuller values (−2.86) because:", "opts": ["Pairs are more volatile", "The residual being tested was itself chosen by a regression to be as stationary-looking as possible, so the test must demand more before it believes it", "ETFs trade on different exchanges", "Engle and Granger used weekly data"], "correct": 1, "explain": "OLS picks the hedge ratio that minimises the residual variance. That fitting step makes a random residual look more mean-reverting than it is, and MacKinnon's critical values correct for it."}
  ],
  "task": "Pick two ETFs you believe move together, pull two years of daily closes, regress the log of one on the log of the other, and record the slope and the daily-return correlation."
}
---

Pairs trading is the purest form of mean reversion: buy one asset, short a related one, and wait for the gap between them to close. Its appeal is that the position is roughly immune to the market. Its danger is that "related" is usually established by looking at a chart, and a chart of two correlated series tells you nothing about whether the gap between them has a mean. This lesson sets out the statistical difference between correlation and cointegration, runs the formal test on seven popular pairs, and reports that none of the textbook pairs pass on recent data.

## Two properties that get confused

**Correlation** measures whether two series move together period by period. Compute the daily returns of XLE and XOP and correlate them: 0.945. On an up day for one, the other is up. That is a statement about changes.

**Cointegration** (Engle and Granger, 1987) is a statement about levels. Two non-stationary series are cointegrated if some fixed linear combination of them is stationary. In pairs language: if there exists a hedge ratio β such that ln(Y) − β·ln(X) has a constant mean and bounded variance, then the spread has a home to return to, and a deviation from that home is a trade.

The two properties are independent. Two random walks driven by the same shocks each day will be highly correlated and, if either has an extra independent component, will drift apart without limit. Gatev, Goetzmann and Rouwenhorst (2006), the standard academic pairs study, avoided the issue by choosing pairs on the distance between normalised price paths and found the strategy's returns fell by more than half from the 1990s to the 2000s. The distance rule finds pairs that were close; it does not test whether they are pulled together.

## The Engle-Granger procedure

1. Over a formation window, regress ln(Y_t) = α + β·ln(X_t) + ε_t by ordinary least squares. β is the hedge ratio: the dollars of X to hold against each dollar of Y.
2. Take the residuals ε_t, which are the spread. Run a Dickey-Fuller regression on them: Δε_t = a + γ·ε_{t−1} + b·Δε_{t−1} + u_t.
3. Compare the t-statistic on γ with MacKinnon's cointegration critical values. For two variables with a constant: −3.90 at 1%, **−3.34 at 5%**, −3.04 at 10%.

The critical values are more demanding than the plain unit-root values from lesson 2 because step 1 chose β to make the residual as small and as well-behaved as possible. A residual that has been fitted will look somewhat mean-reverting even when it is not; the test corrects for that.

Two cautions. The procedure is not symmetric: regressing Y on X and X on Y give different residuals and different t-statistics. And the hedge ratio is a property of the window it was estimated on, not of the pair.

## Worked example

Data: Yahoo Finance daily closes, `interval=1d`, pulled 2026-09-24. Formation window 2023-09-22 to 2025-09-22, 501 common trading days for each pair.

**XOP on XLE.** On 2023-09-22 XLE closed at 44.65 and XOP at 143.42; on 2025-09-22, 43.83 and 130.19. The regression of ln(XOP) on ln(XLE) over the 501 days gives:

α = **0.0970**, β = **1.2717** (standard error 0.0148)

So the fitted relation is ln(XOP) ≈ 0.097 + 1.272 × ln(XLE), and a dollar-neutral spread holds 1.27 dollars of XLE per dollar of XOP. On the last formation day the residual is ln(130.19) − 0.0970 − 1.2717 × ln(43.83) = 4.8690 − 0.0970 − 4.8076 = **−0.0356**, which is 0.70 standard deviations below zero given a residual standard deviation of 0.0510.

Dickey-Fuller on the residual with one lag: t = **−1.23**. Against −3.34, the residual is not distinguishable from a random walk. With zero lags the t-statistic is −1.30 and with four lags −1.22; the lag choice does not rescue it. Daily-return correlation: 0.945. This is the pair that every pairs-trading introduction uses, and on the two most recent years it is correlated and not cointegrated.

**GDX on GLD.** α = −3.0057, β = **1.2150**, residual standard deviation 0.0625, DF t = **−1.01**. Return correlation 0.803. The last formation day's residual is ln(74.33) + 3.0057 − 1.2150 × ln(345.05) = **+0.2141**, or **3.43** standard deviations above zero. The formation window ends with the spread already far outside any trading band, which is the situation the capstone asks you to think through.

**PEP on KO.** β = **−0.5433**. Over the window KO rose from 57.60 to 66.21 and PEP fell from 175.27 to 141.03, so the least-squares line slopes downward. A negative hedge ratio means the "spread" is long both or short both; there is nothing to trade. DF t = −1.89, which does not matter.

**QQQ on SPY.** β = 1.1060, return correlation 0.957, DF t = −2.61. **IWM on SPY.** β = 0.6977, DF t = −2.71. Both nearer the line than the commodity pairs, neither past −3.04.

**XLE on XOM.** β = 0.7251, return correlation 0.891, DF t = **−3.13**. Past the 10% value, short of 5%. Run the other way, XOM on XLE gives β = 1.0136 and t = −2.46. The one near-pass in the set is a sector ETF against its own largest holding, which is cointegration by construction more than by economics, and it only shows up in one of the two regression directions.

**The hedge ratio moves.** XOP on XLE: β = 2.2059 over 2015-01-02 to 2019-12-31 (t = −2.78), 2.3767 over 2018-2019 (t = −2.39), 1.2717 over 2023-2025. GDX on GLD: 2.2907 (2015-2019, t = −2.38), 1.7852 (2018-2019, t = **−3.01**), 0.9439 (2021-2025, t = −1.68), 1.6272 (2024-2025, t = −1.17), and 1.0884 over the full 2015-2026 sample (t = −3.19). PEP on KO passed nearest on 2015-2019 (β = 1.1421, t = **−3.32**, a hair short of −3.34) and over the full sample gives t = −0.18.

## Table

| Pair (Y on X), 2023-09-22 to 2025-09-22, n = 501 | Return correlation | Hedge ratio β | Residual s.d. | DF t (1 lag) | Cointegrated at 5%? |
|---|---|---|---|---|---|
| XOP on XLE | 0.945 | 1.2717 | 0.0510 | −1.23 | No |
| GDX on GLD | 0.803 | 1.2150 | 0.0625 | −1.01 | No |
| PEP on KO | 0.629 | −0.5433 | 0.0819 | −1.89 | No (negative ratio) |
| QQQ on SPY | 0.957 | 1.1060 | 0.0155 | −2.61 | No |
| IWM on SPY | 0.805 | 0.6977 | 0.0390 | −2.71 | No |
| XLE on XOM | 0.891 | 0.7251 | 0.0245 | −3.13 | No (10% only) |
| XOM on XLE | 0.891 | 1.0136 | 0.0289 | −2.46 | No |

Critical values (MacKinnon 2010, two variables, constant): −3.90 (1%), −3.34 (5%), −3.04 (10%). Source: Yahoo Finance daily closes, computed by the course.

## What to do with a table of failures

The honest reading is not that pairs trading is dead. It is that the pairs people name from memory are named because their charts look alike, and a chart cannot show you a unit root. Three practical rules follow.

Test before you trade, on a stated window, and write the t-statistic down. If it is not past −3.34, you are trading a correlated random walk, and lesson 8 shows what that looks like over a year.

Re-estimate the hedge ratio and re-run the test at a fixed interval, because a pair that passed on 2018-2019 (GDX on GLD, t = −3.01) can fail on 2023-2025 (t = −1.01). The ratio for XOP against XLE nearly halved between windows; a position hedged at the old ratio is a directional bet on the ETF you thought you were neutral to.

Prefer pairs with an economic reason for a fixed relation (two share classes, an ETF and its holdings, a futures contract and its underlying) over pairs with a thematic one (gold and gold miners, oil and oil producers). Miners have operating leverage, costs and balance sheets; producers have hedging programmes and capital discipline that change over years. The relation is real but it is not a constant, and cointegration is a test for a constant.

## Sources

- Engle, R. F. and Granger, C. W. J. (1987). Co-integration and error correction: representation, estimation, and testing. *Econometrica*, 55(2), 251–276. https://doi.org/10.2307/1913236
- Gatev, E., Goetzmann, W. N. and Rouwenhorst, K. G. (2006). Pairs trading: performance of a relative-value arbitrage rule. *Review of Financial Studies*, 19(3), 797–827. https://doi.org/10.1093/rfs/hhj020
- MacKinnon, J. G. (2010). Critical values for cointegration tests. Queen's Economics Department Working Paper 1227. https://www.econ.queensu.ca/sites/econ.queensu.ca/files/wpaper/qed_wp_1227.pdf
- Yahoo Finance historical data pages for XLE, XOP, GLD, GDX, KO, PEP, SPY, QQQ, IWM and XOM: https://finance.yahoo.com/quote/XOP/history/

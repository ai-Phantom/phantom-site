---
{
  "title": "The Gate Stack: What a Strategy Must Pass Before It Trades",
  "duration": "19 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A strategy shows +0.57% per trade over 72 trades in-sample (2008-2017) and +0.54% over 76 trades out-of-sample (2018-2026). Which gate does that comparison address?", "opts": ["Cost survival", "Out-of-sample replication: the edge measured on data the rule was not fitted to is of the same size, which is the strongest evidence available that it is not a fit", "Correlation to the book", "The cash benchmark"], "correct": 1, "explain": "Replication is the gate most strategies fail. An edge that halves out of sample was mostly fitted; one that holds within its own sampling error was mostly real. Here the two windows agree to within 0.03% per trade on standard errors of about 0.18%."},
    {"q": "Why is the sample-size gate written as a minimum number of trades and a minimum t-statistic rather than a minimum return?", "opts": ["Because a large return over few trades is indistinguishable from luck; the t-statistic (mean ÷ standard error) measures how many times the average clears its own noise, and it needs enough trades to mean anything", "Because returns are not important", "Because regulators require t-statistics", "Because trades are easier to count"], "correct": 0, "explain": "With 76 trades, a mean of 0.54% and a per-trade standard deviation of 1.49%, t = 0.54 ÷ (1.49 ÷ √76) = 3.2. With 12 trades the same mean would have t = 1.3, which is noise. Harvey, Liu and Zhu argue for a threshold of 3 once you account for how many strategies were tried."},
    {"q": "At a 10 basis point round-trip cost the RSI(2) strategy's average trade falls from +0.54% to +0.44%. At what cost would it break even, roughly?", "opts": ["About 10 bps", "About 25 bps", "About 54 bps", "It never breaks even"], "correct": 2, "explain": "Each trade is one round trip, so the cost per trade in percent equals the round-trip cost: 0.54% of edge is consumed by 54 bps of cost. A strategy with 0.54% per trade has a five-fold cushion over a 10 bps assumption for SPY and almost none if it were moved to a name that costs 40 bps to trade."},
    {"q": "The strategy's daily returns correlate 0.35 with SPY. The gate is 'below 0.5 to the existing book'. What is this gate protecting against?", "opts": ["Regulatory limits", "High turnover", "Low returns", "Adding a strategy that is a disguised copy of what the book already holds, which raises the book's variance without adding a new source of return; lesson 6's overlap problem at the strategy level"], "correct": 3, "explain": "A long-only mean-reversion strategy on SPY will always carry some SPY correlation. 0.35 says two-thirds of its variance is something else. A strategy at 0.9 to the book would pass every other gate and still be pointless."},
    {"q": "The strategy earned +49.4% over the 261 days it was in the market between 2018 and 2026-09-23. BIL returned +24.6% over the whole 8.7 years; SPY returned +228.6%. Which comparison is the cash gate?", "opts": ["Strategy plus idle cash in BIL versus BIL alone; the strategy adds about 49% on top of the cash return it earns on the 88% of days it is flat, and passes", "Strategy versus SPY, and it fails", "Strategy versus zero", "None; the strategy should be compared to nothing"], "correct": 0, "explain": "A strategy that is invested 12% of the time is not competing with buy-and-hold SPY; its capital sits in T-bills the rest of the time. The right null is the return of that cash. Beating SPY is a different question, about capital allocation, not about whether the strategy has an edge."}
  ],
  "task": "Write your gate list as five numbered pass/fail tests with thresholds, and run your most recent strategy idea through it before its next trade."
}
---

## Why the gates come before the trade

Everything in lessons 2 through 7 assumes the book is made of positions that have a reason to be there. The gate stack is where that reason gets tested. It is a written checklist that a strategy must pass, with numbers, before it is allowed to put on a position, and it is the single most effective risk control in this course because it works on the one thing no limit can fix: a strategy that has no edge.

The stack is deliberately mechanical. Each gate is a pass or fail against a threshold written down before the test is run. If the strategy fails one gate, it does not trade, and the failure is recorded rather than explained away. The gates address five ways a backtest lies.

## Gate 1: sample size

The lie: a spectacular result over a handful of trades. Twelve trades that averaged +2% is a story; it is not evidence.

The test: at least 60 completed trades, and a t-statistic on the per-trade mean of at least 2.5, where t = mean ÷ (standard deviation ÷ √n). Harvey, Liu and Zhu (2016), surveying the hundreds of published equity anomalies, argue that after accounting for how many ideas have been tried the bar should be nearer 3.0. Use 2.5 as the floor and 3.0 as the comfortable level, and remember that every idea you discarded before this one counts against the bar.

## Gate 2: out-of-sample replication

The lie: a rule tuned on the data it is then tested on. Any strategy with two or three free parameters can be made to look good on any ten-year window.

The test: split the data before fitting. Fit on the first window, freeze every parameter, then measure on the second. The out-of-sample mean per trade must be positive, must have its own t-statistic above 2, and must lie within one standard error of the in-sample mean. A halving of the edge out of sample is a fail even if the number is still positive: it says the rule was mostly fitted. Better still is a third window, a fresh universe or a later period, that the rule has never seen.

## Gate 3: cost survival

The lie: a backtest at zero cost. A strategy with 0.1% per trade of edge and 300 trades a year is a gift to your broker.

The test: apply a round-trip cost that is honest for the instrument, including spread, commission and the slippage of trading at the close of a bar you only knew was a signal at the close. For SPY, 5 to 10 basis points is conservative; for a mid-cap name, 30 to 50; for an option, lesson 9's territory, several percent. The strategy must retain at least half of its zero-cost edge at the honest cost, and remain positive at double that cost.

## Gate 4: uncorrelated to the existing book

The lie: a new strategy that is the old book in disguise. Three momentum systems on three universes are one momentum system.

The test: correlation of the strategy's daily returns with the existing book's daily returns below 0.5, and its marginal contribution to book variance (lesson 6) at its intended size below its share of gross. If the book is empty, correlate to its nearest benchmark.

## Gate 5: beats cash

The lie: a positive total return in a period when T-bills paid 5%. Beating zero is not an edge.

The test: over the out-of-sample window, the strategy's return on capital, including the cash return earned on days it is flat, must exceed the return of that cash alone, with a Sharpe ratio above the cash-adjusted Sharpe of the benchmark at matched exposure. The comparison is to the alternative use of the capital, which for a strategy that is in the market 12% of the time is mostly T-bills.

## Worked example

A well-known mean-reversion rule, run through the five gates on SPY. The rule is not a recommendation; it is a specimen that happens to pass, chosen because most specimens fail somewhere and it is instructive to see what passing looks like.

**Rule.** Buy SPY at the close when its 2-period RSI (Wilder smoothing on adjusted closes) is below 10 and the close is above the 200-day simple moving average. Sell at the close when RSI(2) is above 60. One position, full size, no stop. In-sample window 2008-01-01 to 2017-12-31; out-of-sample 2018-01-01 to 2026-09-23. Parameters (10, 60, 200) are the textbook ones and were not tuned on either window. Data: Yahoo Finance daily adjusted closes.

**Gate 1, sample size.** In-sample: 72 completed trades, mean +0.572% per trade, standard deviation 1.65%, t = 0.572 ÷ (1.65 ÷ √72) = 0.572 ÷ 0.194 = **2.95**. Out-of-sample: 76 trades, mean +0.541%, standard deviation 1.49%, t = 0.541 ÷ (1.49 ÷ √76) = 0.541 ÷ 0.171 = **3.16**. Combined 148 trades, t = 4.31. Pass on both windows against the 2.5 floor; the out-of-sample window alone clears 3.0.

**Gate 2, replication.** In-sample +0.572% per trade, 79.2% winners, worst trade −10.16% (October 2008). Out-of-sample +0.541%, 75.0% winners, worst trade −4.13%. The difference, 0.031%, is a sixth of the out-of-sample standard error. **Pass.** The edge did not shrink out of sample.

**Gate 3, cost survival.** At 5 bps round trip, out-of-sample mean +0.491%; at 10 bps, **+0.441%**, t = 2.58, total +38.6% versus +49.4% at zero cost. The edge retains 82% of itself at 10 bps and stays positive to about 54 bps. **Pass.** The same rule moved to a name costing 40 bps would keep only a quarter of its edge and would fail the "half retained" line.

**Gate 4, correlation.** Correlation of the strategy's daily return series (zero on flat days) with SPY's daily returns over 2018-2026: **0.35**. In-sample: 0.30. Against an empty book, SPY is the benchmark, and 0.35 is below 0.5. **Pass.** Against the course book, whose beta-adjusted net is 0.31, the correlation would be lower still.

**Gate 5, cash.** The strategy was in the market on 261 of 2,192 out-of-sample days, 11.9% of the time, and earned +49.4% on those days (zero cost). BIL, the 1-3 month T-bill ETF, returned +24.6% over the whole window. Capital in the strategy earns the strategy return when invested and the BIL return otherwise, so its return on capital is roughly 49.4% plus 88% of 24.6%, about +71%, against +24.6% for cash alone. Sharpe ratio of the strategy's daily series, 0.73 (0.61 at 10 bps). **Pass.** For the record, SPY buy-and-hold returned +228.6% over the same window; the strategy is not a substitute for equity exposure, it is a 12%-of-the-time overlay, and the cash gate is the one that describes what it competes with.

**Verdict.** Five of five. It may trade, at a size set by lesson 6's variance-contribution limit, with lesson 12's monitoring of whether the live per-trade mean stays inside the out-of-sample sampling band.

What the example does not show is the graveyard. The rule above is one of a family; variants with the exit at 50 or 70, the filter at 100 or 150 days, or the entry at 5 or 15, mostly pass too, which is reassuring, but the honest count of how many other families were looked at before this one is what sets the gate-1 bar, and that count is never zero.

## Chart

![The gate stack as a flow: sample size of 60 or more trades; out-of-sample replication; cost survival at 10 basis points; correlation to the book under 0.5; beats cash (BIL). Notes carry the RSI(2)-on-SPY results: 76 out-of-sample trades 2018-2026 against 72 in-sample 2008-2017; +0.54% per trade out-of-sample against +0.57% in-sample with t = 3.2; +0.44% after 10 bps; 0.35 correlation to SPY; +49.4% on 261 invested days against +24.6% for BIL over 8.7 years. Source: Yahoo Finance adjusted closes.](figures/gate-stack-flow.svg)

## The written gate list

As it should appear in the risk document, one page, dated, with the thresholds fixed before any test is run:

1. **Sample.** ≥ 60 completed trades; per-trade t ≥ 2.5 (≥ 3.0 preferred).
2. **Replication.** Out-of-sample per-trade mean > 0 with t ≥ 2.0, within one standard error of in-sample. Parameters frozen before the out-of-sample window is opened.
3. **Costs.** Retains ≥ 50% of edge at an honest round-trip cost; positive at double that cost.
4. **Overlap.** Daily-return correlation to the book < 0.5; variance contribution at intended size ≤ share of gross.
5. **Cash.** Return on capital (strategy plus idle cash) > cash alone over the out-of-sample window; Sharpe > 0.5.

A strategy that fails any gate is recorded with the failing number and shelved. A strategy that passes is sized, added to the exposure and VaR tables, and re-tested against gate 2 every quarter on live results: the live per-trade mean is the fourth window, and it is the only one that cannot be fitted.

## Sources

- Harvey, C. R., Liu, Y. and Zhu, H. (2016). "… and the Cross-Section of Expected Returns." *Review of Financial Studies* 29(1). https://doi.org/10.1093/rfs/hhv059
- Bailey, D. H. and López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality." *Journal of Portfolio Management* 40(5). https://doi.org/10.3905/jpm.2014.40.5.094
- Yahoo Finance historical data, SPY and BIL. https://finance.yahoo.com/quote/BIL/history/

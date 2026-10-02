---
{
  "title": "Capstone: Turn-of-Month on SPY Through the Whole Stack",
  "duration": "60 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On SPY 2010-2025, buying the close of the last trading day of each month and selling three sessions later at 5 bps per side gave 191 trades at +0.2108% net. A random-entry null with the same three-session hold and cost averaged +0.0723%. The percentile was 85.7. Which gate does it fail?", "opts": ["G2 cash", "D6 source", "G3 null, at the 85.7th against a 95th bar", "P3 overlap"], "correct": 2, "explain": "It beats cash per trade (0.2108% against 0.0162% of bills over the hold) and has no overlap, but 85.7 is below 95. With 5 of 5 eras positive in the notes' longer window, the honest label is underpowered, not absent."},
    {"q": "The edge over the null is 0.1385% and the per-trade standard deviation 1.829%. The required n at z = 1.645 is:", "opts": ["472", "191", "1,000", "47"], "correct": 0, "explain": "(1.645 x 1.829 / 0.1385)^2 = 21.72^2 = 472. The window holds 191, so G4 reports underpowered by a factor of about 2.5."},
    {"q": "Yahoo SPY adjusted daily returns against Cboe's S&P 500 index over 2010-2025 differ by a median 2.66 bps with 5 of 4,023 days beyond 50 bps, all in March 2020 and April 2025. On the 191 three-day trade windows the largest disagreement is 35.1 bps. The D6 verdict is:", "opts": ["Fail: five outliers", "Pass: median under 5 bps, 0.12% of days beyond 50 bps against a 1% bar, and no trade window beyond 50 bps; the outliers are crash days both sources report", "Skip: the index is not the ETF", "Fail: the levels drift 20%"], "correct": 1, "explain": "Returns, not levels. The ETF and the index are different instruments, which the returns test tolerates and the level test does not."},
    {"q": "Turn-of-month's equity curve over 2010-2025 ends at +74.7% against SPY's +702.0%, with a Sharpe against cash of 0.36 against 0.76. G7 reads:", "opts": ["Pass, because drawdown was only 12.5%", "Not applicable to calendar rules", "Pass, because it beats bills", "Fail at 0.47x of buy-and-hold's Sharpe against cash"], "correct": 3, "explain": "0.36 / 0.76 = 0.47. Its small drawdown comes from being in cash 81% of the time, which the Sharpe-against-cash comparison neutralises."},
    {"q": "The 2014-2017 era scores the 48.2nd percentile and 2022-2025 the 34.8th; 2010-2013 scores 92.6 and 2018-2021 84.1. Eras above 95:", "opts": ["Zero of four, so the era gate fails too", "Two", "One", "Four"], "correct": 0, "explain": "None reaches 95. Two eras are near-misses and two are at or below the median of random timing. The ledger records it as failing G3, G4 and the era gate on this window, with the notes' longer window as the reason it remains a lead rather than closed."}
  ],
  "task": "Submit your ledger entry for the rule with every number traced to a source and a formula, score it against the rubric, and only then compare it with the reference solution."
}
---

## The exercise

Take one stated rule through every gate in this course on a stated window, and write the ledger entry the run earns. You are graded on whether each number can be traced to a source and a formula and whether the verdict follows from the numbers, not on whether the rule passes. In the reference solution it does not pass on this window, and recognising which gates it fails, and why, is the grade.

The rule: turn-of-month on SPY. Buy at the close of the last trading day of each calendar month; sell at the close three sessions later. Always long, one position, no stop. The window: entries from 2010-01-01 to 2025-12-31 whose exits fall inside the window. The alternative, if you prefer, is RSI(2) below 10 with exit above the 5-day average, which Lessons 7 to 11 have already worked through; choosing it means your reference numbers are in those lessons and the work is in assembling them.

Write the rule down, with the window and the pass criteria, before you fetch any data. The criteria for this capstone are the stack's: D6 median return difference under 5 bps and under 1% of days beyond 50 bps; P2 and P3 as in Lessons 4 and 8; G2 positive excess over bills on the hold; G7 at least 1.0x of buy-and-hold's Sharpe against cash; G3 at or above the 95th percentile against a matched random-entry null; G4 n at or above the required n against the null; at least two of four eras above the 95th.

### Part 1: data

Fetch SPY daily bars from Yahoo Finance's chart endpoint with explicit period1 and period2 Unix timestamps; confirm `dataGranularity` reads `1d`; report the row count per year against the NYSE calendar, nulls, zero-volume rows, and the count of dividend-factor changes. Fetch a second source that did not produce the first (Cboe's S&P 500 daily history works; Stooq's CSV may refuse automated requests, in which case say so and use Cboe). Compare daily returns, not levels, on the adjusted series: report the median absolute difference in bps, the count and dates of days beyond 50 bps, and the same statistics restricted to your trade windows. State D6's verdict and its coverage.

### Part 2: the trade

State the unit. This rule has no stop, so R is undefined; say so and use percent of price, with Lesson 4's reasoning. Report P2 as not applicable with the reason, and P3: the greedy non-overlap count against the nominal count. State the lookahead check: the signal (last trading day of the month) is known from the calendar before the close.

### Part 3: inference

Compute gross and net per trade at 5 bps per side, win rate and the per-trade standard deviation. Build a random-entry null of 2,000 draws matched on trade count and the three-session hold, charged the same cost, with a stated seed. Report the null mean, its 5th and 95th percentiles and the rule's percentile. Compute the required n at z = 1.645 against the null mean. Split into four four-year eras, each with its own null, and report each era's percentile.

### Part 4: benchmarks and cost

Compute the growth of one dollar for the rule (in cash between trades), SPY buy-and-hold and 13-week bills; CAGR, maximum drawdown and Sharpe against cash for each. Compute G2 per trade and G7 as a ratio. Report net per trade at 0, 0.5, 5 and 10 bps per side and the one-cent spread on the window's median raw price.

### Part 5: the ledger entry

One row: rule, window, universe, verdict, the gates passed, the gate it died at, the deciding number, and the label (dead, underpowered, lead). Then three sentences on what the next test would be and why.

## Worked example

Reference solution, computed 2026-09-30 from Yahoo Finance SPY daily bars (period1 = 1104537600, period2 = 1790726400; 5,469 rows, 2005-01-03 to 2026-09-29), Cboe SPX_History.csv and Yahoo ^IRX.

Data. 2010-2025 holds 4,024 rows, 250 to 253 per year (2012: 250, Hurricane Sandy; 2020: 253), no nulls, no zero-volume rows. Cboe's index has the identical 4,024 dates. Adjusted SPY against the index: median absolute daily difference 2.66 bps; 5 of 4,023 days beyond 50 bps (0.12%), namely 2020-03-13, 03-16, 03-17, 2025-04-09 and 04-10, crash days both sources report. On the 191 three-day trade windows: median difference 1.71 bps, largest 35.1, none beyond 50. D6 passes with 100% coverage. The largest daily move in the window, −10.94% on 2020-03-16, is confirmed by the index, so D5 passes.

Trade. No stop, unit is percent. P2 not applicable. P3: one trade a month, three-session holds, inflation 1.00x. P0: the signal is a calendar date.

Inference. 191 trades, first entry 2010-01-29, last exit 2025-12-03 (the 2025-12-31 entry exits in 2026, outside the window). Gross +0.3110% per trade, net +0.2108% at 5 bps per side, 57.6% positive, standard deviation 1.829%. G1: the 110 winners average +1.3557% and the 81 losers −1.3441%, so the breakeven win rate is 1.3441 / (1.3557 + 1.3441) = 49.8%; with the five-point margin the bar is 54.8%, and 57.6% clears it. Null (seed 20260930): mean +0.0723%, 5th percentile −0.1462%, 95th +0.2758%. Percentile 85.7. G3 fails. Edge over the null 0.2108 − 0.0723 = 0.1385 points; required n = (1.645 × 1.829 / 0.1385)^2 = 472 against 191 held. G4 reports underpowered by 2.5 times. Eras: 2010-13, 48 trades, +0.4597% against +0.0913%, 92.6th; 2014-17, 48, +0.0370% against +0.0384%, 48.2nd; 2018-21, 48, +0.4007% against +0.1071%, 84.1st; 2022-25, 47, −0.0600% against +0.0508%, 34.8th. Zero of four above 95.

Benchmarks and cost. Growth of one dollar: rule 1.747 (+74.7%, CAGR 3.56%, max drawdown −12.5%, Sharpe against cash 0.36); SPY 8.020 (+702.0%, 13.93%, −33.7%, 0.76); bills 1.245 (+24.5%). G2: bills over a three-session hold averaged 0.0162%, so the rule clears cash by 0.195 points per trade; pass. G7: 0.36 / 0.76 = 0.47x; fail. Net per trade at 0, 0.5, 5 and 10 bps per side: +0.3110%, +0.3010%, +0.2108%, +0.1106%. The window's median raw close was $258.13, so a one-cent round trip is 0.387 bps; the 10 bps round-trip assumption is 26 times that, and the rule clears it.

Ledger entry: turn-of-month, SPY, 2010-2025, single instrument. Passed D0-D6, P0, P3, G1, G2. Died at G3, 85.7th (seven seeds not run; required before a final label). Also fails G7 at 0.47x and the era gate at 0 of 4. Deciding number: edge over null 0.1385 points against a required n of 472. Label: underpowered on this window. The research notes reached the 99th percentile on 395 trades from 1993 to 2026 with a larger pre-2008 effect; this window alone cannot see it. The next test is not another SPY backtest: it is the forward record, already running in the notes, and a fresh market with its own second source.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Data gates | Explicit timestamps and granularity check; per-year rows, nulls, zero volume, dividend events; a second independent source compared on returns with median, outlier count and dates, restricted to trade windows; D6 verdict with coverage | 20 |
| Trade definition | Unit stated and justified; P0, P2 and P3 each reported with a value or a stated reason for not applicable | 10 |
| Null, power and eras | Matched null with seed, draw count, cost and hold stated; percentile; required n against the null mean, not zero; four eras each scored against its own null | 25 |
| Benchmarks | Growth of one dollar, CAGR, drawdown and Sharpe against cash for rule, buy-and-hold and bills on the same window; G2 charged over the hold; G7 as a ratio | 20 |
| Costs | Net per trade at four cost levels; spread from raw prices on the window; turnover per year | 10 |
| Ledger entry | Verdict, first failing gate, deciding number and label consistent with the numbers; every figure traceable to a source and formula; next test named with a reason | 15 |

Total: 100. A submission scoring 80 or more with no criterion below half marks has run a strategy through the stack honestly. A submission that labels this rule a pass on 2010-2025 has an error somewhere in Part 3 and should find it before writing anything else.

## Sources

- Ariel, R. A. (1987). "A Monthly Effect in Stock Returns." Journal of Financial Economics 18(1). https://doi.org/10.1016/0304-405X(87)90066-3
- Lakonishok, J., Smidt, S. (1988). "Are Seasonal Anomalies Real? A Ninety-Year Perspective." Review of Financial Studies 1(4). https://doi.org/10.1093/rfs/1.4.403
- Cboe Global Markets, S&P 500 index daily price history: https://cdn.cboe.com/api/global/us_indices/daily_prices/SPX_History.csv
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

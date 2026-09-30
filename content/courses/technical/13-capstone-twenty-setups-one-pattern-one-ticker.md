---
{
  "title": "Capstone: Twenty Setups, One Pattern, One Ticker",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Before logging the first setup, you must have written down:", "opts": ["The expected win rate", "The pattern definition, entry rule, stop rule, target or time-stop rule, and the date range, all fixed and unchangeable", "Your favourite indicator", "The name of the pattern only"], "correct": 1, "explain": "Everything that determines an outcome is fixed before the first outcome is known. Changing a rule after seeing results converts the exercise into curve-fitting."},
    {"q": "A setup you would have skipped 'because it looked wrong' must be:", "opts": ["Omitted from the log", "Logged and counted, because the rules did not exclude it", "Counted as a win", "Counted twice"], "correct": 1, "explain": "Discretionary exclusion after the fact is selection on outcome. If a filter is needed, it goes into the rules for the next test, not into this one."},
    {"q": "With 20 setups, 11 winners averaging +1.8% and 9 losers averaging −1.1%, the expectancy is:", "opts": ["+0.70%", "+0.495%", "+1.8%", "−0.40%"], "correct": 1, "explain": "0.55 × 1.8 − 0.45 × 1.1 = 0.99 − 0.495 = +0.495% per trade."},
    {"q": "The standard error of a win rate of 55% measured on 20 trades is roughly:", "opts": ["1%", "5%", "11%", "25%"], "correct": 2, "explain": "√(0.55 × 0.45 / 20) = √0.0124 = 0.111. A 55% win rate on 20 trades is consistent with a true rate anywhere from about 33% to 77%."},
    {"q": "The final section of the write-up must state what the sample cannot tell you. Which of these belongs there?", "opts": ["Whether the pattern will work next year", "The entry price of trade 7", "The ticker symbol", "The number of trades"], "correct": 0, "explain": "The sample is one ticker, one period, twenty instances, no costs modelled unless you added them. Forward performance, other tickers and other regimes are all outside what it can support."}
  ],
  "task": "Submit your log, your statistics and your written assessment; then, if you continue, extend the same log to 50 setups without changing a single rule."
}
---

This capstone asks you to do, once, the thing every earlier lesson said was necessary and every chart-pattern book skips: take one precisely defined pattern on one ticker, find twenty historical instances without cherry-picking, simulate each trade to its exit, and compute what happened. Then write down what the result does and does not tell you. The write-up is graded by the rubric at the end; the numbers are not graded on whether they are good, only on whether they are correct and honestly interpreted.

## Step 1: Fix the rules

Write the following before you open a chart. Once written, nothing changes.

- **Ticker.** One liquid instrument with at least five years of daily history. Index ETFs and large-cap stocks are easiest because data is clean and splits are few.
- **Data source.** Name it (Yahoo Finance historical data, Nasdaq historical data, your broker's export). State whether prices are split-adjusted.
- **Pattern definition.** One condition or a small set of conditions computable from OHLCV. Examples used in this course: a daily close above the highest close of the prior 50 days (Lesson 10); RSI(2) below 10 with the close above the 200-day SMA (Lessons 7 and 12); a close below the lower Bollinger Band (Lesson 9); the first higher low after a sequence of lower lows using the 10-bar swing algorithm (Lesson 4). Pick one.
- **Entry.** The next day's open, or the close of the signal day. State which.
- **Stop.** A fixed rule in ATR units or at a structural level (the pattern's low, the range's opposite side). State it as a formula.
- **Target or time stop.** A fixed multiple of the stop distance, a moving-average exit, or a maximum holding period. State it.
- **Date range.** A start and end date. The first twenty instances inside that range are your sample. Not the best twenty; the first twenty.
- **Costs.** Either zero, stated as such, or a fixed round-trip percentage subtracted from every trade.

## Step 2: Find the setups

Go through the history from the start date forward. Every day the pattern condition is true and you are not already in a trade is a setup. Log it. Do not skip any, including the ones that look obviously bad. If two setups overlap (a second signal while the first trade is open), the rule "one position at a time" excludes the second; log that it was excluded and why.

Stop when you have twenty completed trades.

## Step 3: Simulate each trade

For each setup, walk forward bar by bar from the entry:

1. On each day, check the low against the stop and the high against the target (for a long). If both are touched on the same day, assume the stop was hit first, which is the conservative assumption.
2. If neither is touched, check the time stop or the moving-average exit at the close.
3. Record the exit date, exit price, exit reason (stop, target, time, rule), and the return as (exit / entry − 1) × 100, minus costs if you specified them.
4. Also record the maximum adverse excursion (the lowest low between entry and exit, as a percentage of entry) and the maximum favourable excursion (the highest high). These tell you how close each trade came to the stop and how much it left on the table.

## Example log rows

Three rows from the Rule B log in Lesson 12, so you can see the format. SPY, daily data from Yahoo Finance. Pattern: RSI(2) < 10 and close > 200-day SMA. Entry: next open. Stop: entry − 1 × ATR(14). Target: entry + 2 × ATR(14). Time stop: 10 days. Costs: none.

| # | Signal date | Entry date | Entry | ATR | Stop | Target | Exit date | Exit | Reason | Return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 Jan 2024 | 4 Jan 2024 | 468.30 | 3.93 | 464.37 | 476.16 | 10 Jan 2024 | 476.16 | Target | +1.68% |
| 2 | 17 Jan 2024 | 18 Jan 2024 | 474.01 | 4.16 | 469.85 | 482.33 | 19 Jan 2024 | 482.33 | Target | +1.76% |
| 3 | 4 Apr 2024 | 5 Apr 2024 | 514.46 | 4.64 | 509.82 | 523.74 | 12 Apr 2024 | 509.82 | Stop | −0.90% |

Check the arithmetic on row 1: stop = 468.30 − 3.93 = 464.37; target = 468.30 + 2 × 3.93 = 476.16; return = 476.16 / 468.30 − 1 = +1.68%. Every row in your log should be checkable the same way.

## Step 4: Compute the statistics

From the twenty rows:

- **Win rate** = winners / 20.
- **Average win**, **average loss**, **largest win**, **largest loss**.
- **Expectancy** = win rate × average win − loss rate × average loss.
- **Profit factor** = sum of wins / |sum of losses|.
- **Longest losing streak** in sequence.
- **Average holding period** in trading days, and total days in market.
- **Exit-reason counts** (how many stops, targets, time exits).
- **Standard error of the win rate** = √(p × (1 − p) / 20), where p is the win rate. Report the win rate ± two standard errors.
- **Standard error of the expectancy** = standard deviation of the twenty returns / √20. Report the expectancy ± two standard errors.

Then compute the **base rate**: the average return over the same holding period for every day in your date range, not just signal days. Your expectancy is only interesting relative to that number.

## Step 5: Write the assessment

Four to six paragraphs, plain language, covering:

1. **What the sample shows.** The numbers, with their standard errors, against the base rate.
2. **What drove the result.** Was it one or two trades? Which exit reason dominated? Did MAE show that stops were routinely nearly hit?
3. **What the sample cannot tell you.** Twenty trades on one ticker in one period, with the rules you chose from many possible rules, cannot establish that the pattern has an edge, that it will persist, or that it transfers to other instruments. Say this specifically, with reference to the standard errors you computed.
4. **What you would test next**, without changing this test: a different period, a different ticker, 50 more instances, a cost model.
5. **What you would have done differently in the rules**, kept strictly separate from item 4, so that any reader can see you did not tune them mid-test.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Rules fixed in advance | Ticker, data source, pattern, entry, stop, target/time stop, date range and cost assumption all stated as formulas before the log, and unchanged | 20 |
| Log completeness and honesty | Twenty consecutive instances from the start date with no omissions; excluded overlaps noted; every row has entry, stop, target, exit, reason, return, MAE, MFE | 25 |
| Arithmetic | Stops, targets, returns, win rate, expectancy, profit factor and standard errors all correct and reproducible from the rows | 20 |
| Base-rate comparison | The unconditional return over the same holding period is computed for the same date range and the expectancy is judged against it | 10 |
| Interpretation | The write-up separates what the sample shows from what it cannot show, cites the standard errors, identifies what drove the result, and does not claim an edge the numbers cannot support | 20 |
| Separation of next test from rule changes | Proposed follow-up tests keep the rules fixed; any proposed rule changes are listed separately and explicitly not applied to this sample | 5 |

A total of 70 or above is a pass. Note that a log showing a losing pattern, correctly computed and honestly interpreted, scores identically to a log showing a winning one.

## Sources

- Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2014). "Pseudo-Mathematics and Financial Charlatanism." *Notices of the American Mathematical Society*, 61(5). https://www.ams.org/notices/201405/rnoti-p458.pdf
- Lo, A. W., Mamaysky, H., & Wang, J. (2000). "Foundations of Technical Analysis." *Journal of Finance*, 55(4). https://www.nber.org/papers/w7613
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

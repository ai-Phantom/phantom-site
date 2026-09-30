---
{
  "title": "Building a Rules-Based Checklist and Testing It on History",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Expectancy per trade is:", "opts": ["Win rate alone", "(Win rate × average win) − (Loss rate × average loss)", "The largest winning trade", "Average win divided by average loss"], "correct": 1, "explain": "For Rule A in the worked example: 0.741 × 0.98% − 0.259 × 1.52% = +0.33% per trade."},
    {"q": "Rules A and B in the worked example used the same entry signal. Rule A won 74% of the time and Rule B won 39%. Which had the higher expectancy?", "opts": ["Rule B, because its winners were bigger", "Rule A, at +0.33% per trade versus +0.12%", "They were identical", "Neither had positive expectancy"], "correct": 1, "explain": "The exit rule, not the entry, determined the result. A 2-ATR target on a mean-reversion signal was hit only 30 times in 90 trades; the 1-ATR stop was hit 55 times."},
    {"q": "Why split the history into two periods and test the rule on each?", "opts": ["To double the number of trades", "To check whether the result holds in a period that was not used to design the rule; a rule that works only in one half is likely fitted to it", "Because spreadsheets have row limits", "To find the best parameters for each period"], "correct": 1, "explain": "Bailey et al. (2014) and Harvey, Liu and Zhu (2016) show how easily a rule fitted to one sample fails on the next. A hold-out period is the minimum defence."},
    {"q": "Rule A's summed return over ten years was +27.0% while buy-and-hold returned +214.7%. The most accurate reading is:", "opts": ["Rule A is worthless", "Rule A was in the market about 3.4 days per trade, 81 times, so it captured a small fraction of the index's rise while taking a small fraction of its exposure; it cannot be compared with buy-and-hold without adjusting for time in market", "Buy-and-hold is always better", "The rule should have used a bigger target"], "correct": 1, "explain": "Roughly 275 days in the market out of 2,500 is 11% exposure. Comparing raw returns across very different exposures is one of the commonest errors in strategy evaluation."},
    {"q": "Adding a 0.10% round-trip cost to Rule A reduced expectancy from +0.334% to:", "opts": ["+0.334%, costs do not matter", "+0.234%", "−0.10%", "+0.50%"], "correct": 1, "explain": "Costs subtract directly from a per-trade expectancy. On a rule with a 0.33% edge, a 0.10% cost removes 30% of it; on a rule with a 0.12% edge (Rule B), the same cost removes 80%."}
  ],
  "task": "Write your own checklist as numbered rules with no adjectives, apply it by hand to the past 12 months of your ticker without skipping any signal, and compute win rate, expectancy and the split-period results before the capstone."
}
---

You now have a set of measurements: structure, levels, volume, averages, oscillators, volatility, patterns and timeframes. None of them is a strategy. A strategy is a written list of conditions that, when all true, produce an entry with a stop, a target or time limit, and a size, applied without discretion to every instance. This lesson shows how to write one, how to test it on history, and how to read the result without fooling yourself. The worked example tests one real rule two ways and gets two very different answers from the same entry.

## The checklist

A usable checklist has five parts. Each must be answerable yes or no from the data, with no adjectives.

1. **Regime filter** (higher timeframe). Example: close above the 200-day SMA.
2. **Setup** (the condition that makes today a candidate). Example: RSI(2) below 10.
3. **Entry** (the exact price and time). Example: next day's open.
4. **Exit if wrong** and **exit if right**. Example: stop 1 ATR below entry; target 2 ATR above; time stop of 10 days. Or: exit on the first close above the 5-day SMA.
5. **Size**. Example: shares = (0.5% of account) / (entry − stop).

Write it down before you look at any outcomes. The order of operations is the discipline: rules first, data second, results third. If you look at results and then adjust a rule, you are fitting, and the number you get afterward is not an estimate of anything.

## Testing it

For every day in your history, apply rules 1 and 2. On every day they are both true and you are flat, apply rule 3 the next day and follow rule 4 forward until an exit. Record entry date, entry price, stop, target, exit date, exit price, and the reason for exit. That log is the entire output; everything else is arithmetic on it.

From the log, compute:

- **Number of trades** (n). Under 30 is anecdote; under 100 is suggestive.
- **Win rate** = winners / n.
- **Average win** and **average loss**, as percentages of entry.
- **Expectancy** = win rate × average win − loss rate × average loss. This is the average return per trade and the number that matters.
- **Worst trade** and **longest losing streak**, which tell you what living through it would have felt like.
- **Time in market**, so you can compare exposure with buy-and-hold.

Then split the history into two halves and compute everything again for each. If the rule only works in one half, you have learned something important.

Then subtract a cost per trade. For a liquid ETF, 0.05% round trip is optimistic and 0.10% is realistic; for a thinly traded stock, more. Watch what the cost does to the expectancy.

## Why testing is hard

Bailey, Borwein, López de Prado and Zhu (2014) showed that if you try enough variations of a rule on the same data, you will find one with an excellent backtest by chance alone, and the more variations you try the better the best one looks. They call this backtest overfitting and show that it is nearly guaranteed under normal research practice. Harvey, Liu and Zhu (2016) applied the same logic to the academic literature on return predictors and concluded that most published findings would not survive a proper multiple-testing correction. White (2000) and Sullivan, Timmermann and White (1999) built the formal tools for correcting a backtest for the number of rules tried.

The practical defences are simple to state and hard to follow: decide the rule before testing, test it once, hold out a period you did not look at, and count every variation you tried as a separate test when judging the winner.

## Worked example

SPY, daily data from Yahoo Finance, September 2016 to September 2026. The entry checklist, fixed in advance:

1. Regime: close above the 200-day SMA.
2. Setup: RSI(2) below 10 (Wilder smoothing).
3. Entry: next day's open. One position at a time.

That produced 136 qualifying signal days over the decade. Two exit rules were then tested on the same signals.

**Rule A**: exit at the close of the first day the close is above the 5-day SMA. **Rule B**: stop 1 ATR(14) below entry, target 2 ATR above, both checked against each day's low and high starting on the entry day, and a time stop at the close of the tenth day.

The results, with no costs, are in the table under the Table heading below.

The expectancy arithmetic for Rule A: 0.741 × 0.98 − 0.259 × 1.52 = 0.726 − 0.394 = **+0.33%** per trade. For Rule B: 0.389 × 2.03 − 0.611 × 1.09 = 0.790 − 0.666 = **+0.12%**.

Read the table.

The **entry is identical** in both rules. Rule A wins three trades in four; Rule B loses three in five. Every difference is the exit. A 2-ATR target on a short-term mean-reversion signal asks for a move the signal does not usually deliver: it was reached 30 times in 90. The 1-ATR stop sits inside the noise of the days right after a sharp decline and was hit 55 times. Rule A asks only for price to get back above a 5-day average, which after a two-day drop is a small distance, and it got it 74% of the time, at the cost of larger losses (−1.52% average, −4.58% worst) when it did not, because Rule A has no stop.

The **split periods** agree for Rule A (+0.31% and +0.36%) and disagree for Rule B (+0.02% then +0.22%). Rule B's whole result comes from the second half. That is the pattern that should make you suspicious, and it would be invisible in a single ten-year number.

**Costs.** At 0.05% round trip, Rule A's expectancy falls to +0.284%; at 0.10%, to +0.234%. The same 0.10% would leave Rule B at roughly +0.02%, which is zero.

**Exposure.** Rule A held SPY for about 81 × 3.4 = 275 trading days out of roughly 2,500, or 11% of the time, and summed to +27.0%. Buy-and-hold over the same span returned +214.7% with 100% exposure. The rule is not competing with buy-and-hold; it is a small, short-exposure overlay whose per-day-in-market return (27.0 / 275 = 0.098% per day) was higher than the index's (about 0.05% per day) but which was flat 89% of the time. Whether that is worth doing depends on what the capital does the other 89% of the time, which is not a technical-analysis question.

**What this test does not establish.** That the rule will work next year. That it works on any ticker other than SPY. That the +0.33% is distinguishable from luck: with 81 trades, an average of 0.334% and a standard deviation of trade returns of 1.38%, the standard error of the mean is 1.38 / √81 = 0.15%, so the expectancy is about 2.2 standard errors from zero. That is suggestive, not conclusive, and it is one rule from a family (RSI(2) thresholds, SMA exit lengths, 200-day filter) with dozens of members, most of which nobody reports when they fail.

## Table

SPY, September 2016 to September 2026. Same entry (close above 200-day SMA, RSI(2) below 10, buy next open), two exits, no costs.

| | Rule A (SMA-5 exit) | Rule B (1 ATR stop / 2 ATR target) |
|---|---|---|
| Trades | 81 | 90 |
| Win rate | 74.1% | 38.9% |
| Average win | +0.98% | +2.03% |
| Average loss | −1.52% | −1.09% |
| Expectancy per trade | +0.334% | +0.124% |
| Sum of returns | +27.0% | +11.2% |
| Worst trade | −4.58% | −1.79% |
| Average hold | 3.4 days | 3.7 days |
| 2016–2021: trades / win / expectancy | 37 / 73.0% / +0.308% | 42 / 35.7% / +0.017% |
| 2022–2026: trades / win / expectancy | 44 / 75.0% / +0.355% | 48 / 41.7% / +0.217% |
| Exit reasons | all SMA-5 | 55 stop, 30 target, 5 time |

If you take one row from it, take "Expectancy per trade" and its two split-period values; if you take one column, take Rule B, which shows how a positive-looking sum can be almost entirely luck of the period.

## Writing yours

Copy the five-part structure. Fill it with conditions you can compute from OHLCV. Keep the number of parameters small: each threshold you can tune is another dimension to overfit. Fix the exit before the entry, because the exit is where the result lives. Then run it by hand on at least 30 instances, ideally 100, and write the log. The capstone asks you to do exactly that for 20 setups, with the understanding that 20 is enough to learn the process and not enough to learn the answer.

## Sources

- Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2014). "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance." *Notices of the American Mathematical Society*, 61(5). https://www.ams.org/notices/201405/rnoti-p458.pdf
- Harvey, C. R., Liu, Y., & Zhu, H. (2016). "... and the Cross-Section of Expected Returns." *Review of Financial Studies*, 29(1). https://doi.org/10.1093/rfs/hhv059
- White, H. (2000). "A Reality Check for Data Snooping." *Econometrica*, 68(5). https://doi.org/10.1111/1468-0262.00152
- Sullivan, R., Timmermann, A., & White, H. (1999). "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." *Journal of Finance*, 54(5). https://doi.org/10.1111/0022-1082.00163

---
{
  "title": "Chart Patterns, Breakouts, and Why Most Fail",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Lo, Mamaysky and Wang (2000) found that classic chart patterns:", "opts": ["Reliably predict large profits", "Occur more often than in a random series and change the distribution of subsequent returns, without a demonstrated profitable trading rule", "Never occur in real data", "Only work on weekly charts"], "correct": 1, "explain": "Their result is about information content, not profitability. The patterns are real regularities; turning them into money is a separate, unproven step."},
    {"q": "In the ten-year SPY check, what share of 50-day-high closing breakouts closed back below the breakout level within 20 trading days?", "opts": ["About 10%", "About 25%", "About 74%", "100%"], "correct": 2, "explain": "163 of 219 breakouts (74.4%) printed at least one close below the level within 20 days. Most breakouts are retested; whether a retest counts as failure depends on your definition."},
    {"q": "AAPL broke above its prior 50-day closing high of 192.35 on 3 June 2024, closing at 194.03. Twenty trading days later it closed at 220.27. The gain was about:", "opts": ["+1.5%", "+6.7%", "+13.5%", "+25%"], "correct": 2, "explain": "220.27 / 194.03 − 1 = 13.5%. This breakout never closed below its level; it was one of the 36% on AAPL that held."},
    {"q": "Why is the 'volume confirms the breakout' rule hard to defend on SPY?", "opts": ["Because SPY has no volume data", "Because only 8 of 219 breakouts came on more than 1.5× normal volume, and those 8 averaged −1.24% over the next 20 days", "Because breakouts always fail", "Because volume is measured in dollars"], "correct": 1, "explain": "The sample of high-volume breakouts is tiny and its average return was negative. There is no evidence in this data that volume improves breakout follow-through on an index."},
    {"q": "The most important reason breakout statistics differ so much between sources is:", "opts": ["Different chart colours", "The definition of 'breakout' and of 'failure' (close vs intraday, level lookback, retest window) changes the count and the outcome", "The day of the week", "Whether a trend line was drawn"], "correct": 1, "explain": "Change the lookback from 50 to 20 days, or count intraday highs instead of closes, or use a 10-day rather than 20-day retest window, and every number in this lesson moves. Fix the definition before you count."}
  ],
  "task": "Define one breakout pattern precisely (level, lookback, close or intraday, failure window), then find and log every instance on your ticker over the past two years with its outcome."
}
---

Chart patterns are named shapes: head and shoulders, double top, triangle, flag, cup with handle. Each comes with a story about buyers and sellers and a claimed outcome. This lesson covers what the patterns have in common, what the one serious academic study of them found, and then does what most pattern books do not: counts every instance of one precisely defined breakout on two tickers and reports how many failed.

## Every pattern is a breakout

Strip the names away and almost every classic pattern reduces to a **consolidation** followed by a **break** of one of its boundaries. A triangle is a narrowing range; a flag is a short range after a sharp move; a head and shoulders is a range whose middle high is higher than the sides, with the "neckline" as its lower boundary; a cup with handle is a rounded range with a smaller range at its right edge. The trade in every case is the same: enter when price leaves the range, place the stop back inside it, target some multiple of the range's height.

That means the useful question is not "does a head and shoulders work?" but "what happens after price breaks out of a range?" That question can be defined precisely and counted.

## What the evidence says

Lo, Mamaysky and Wang (2000) is the reference study. They fitted a smoothing kernel to daily prices of US stocks from 1962 to 1996, defined ten patterns algorithmically (head and shoulders, inverse head and shoulders, broadening tops and bottoms, triangle tops and bottoms, rectangle tops and bottoms, double tops and bottoms), and tested whether the distribution of returns after each pattern differed from the unconditional distribution. For several patterns it did, especially on Nasdaq stocks. The authors were careful to say what they had not shown: that any pattern could be traded profitably after costs. Their finding is that patterns carry some information, not that they carry an edge.

Sullivan, Timmermann and White (1999) included range-breakout rules in their data-snooping study and found the same result as for moving averages: apparent profits in the early sample, nothing out of sample.

The retail literature reports pattern "success rates" that are often above 60% or 70%. Those numbers depend entirely on how success is defined, over what window, and whether the pattern was identified before or after the outcome was known. A pattern identified in hindsight is selected on its outcome.

## Base counts and why they matter

Some practitioners count the number of times a range has been tested or the number of consecutive consolidations in a trend (the "base count") and claim later bases are more likely to fail. The mechanism is plausible: each successful breakout attracts more participants, so later breakouts have more crowded positioning and less new buying available. There is no clean academic test of it. Treat it as a hypothesis worth counting on your own ticker, not as a rule.

## Worked example

Define the pattern precisely. **Breakout**: a daily close above the highest close of the prior 50 trading days, where the previous day was not already a breakout. **Level**: that prior 50-day high close. **Failure**: at least one close below the level within the next 20 trading days. **Forward return**: close 20 trading days after the breakout divided by the breakout close, minus 1. Source: Yahoo Finance historical daily data, September 2016 to September 2026, unadjusted for SPY and split-adjusted for AAPL.

**SPY.** 219 breakouts in ten years. 163 of them, **74.4%**, closed back below the level within 20 days. Average 20-day forward return after a breakout: +0.40%, with 67.1% positive. Base rate for all days: +1.13%, 68.3% positive. So buying SPY on the day it made a new 50-day closing high produced, over the next month, a return below the average of buying it on any random day.

Split by volume: only 8 of the 219 breakouts came on more than 1.5× the 50-day average volume, and those 8 averaged **−1.24%** over 20 days (4 of 8 positive). The other 211 averaged +0.46% (67.8% positive). The "volume confirms the breakout" rule has no support in this sample, and the sample is too small to say anything else.

**AAPL.** 172 breakouts. 110 of them, **64.0%**, closed back below the level within 20 days. Average 20-day forward return +1.98%, 62.2% positive, against a base rate of +2.27% and 64.1% positive. Again slightly below the base rate.

**One instance in detail.** AAPL, 3 June 2024. The highest close of the prior 50 trading days was 192.35. The 3 June close was 194.03, a breakout by (194.03 − 192.35) / 192.35 = **+0.87%**. Volume was 50.1 million shares against a 50-day average of 58.8 million, so relative volume was 0.85: a "low-volume breakout" that the textbook rule would have rejected. The next 20 closes ran 194.35, 195.87, 194.48, 196.89, 193.12, 207.15, 213.07, 214.24, 212.49, 216.67, 214.29, 209.68, 207.49, 208.14, 209.07, 213.25, 214.10, 210.62, 216.75, 220.27. The lowest of them was 193.12, which is above the level of 192.35, so this breakout **did not fail** by the definition. The 20-day return was 220.27 / 194.03 − 1 = **+13.5%**, driven by a 7.3% single-day rise on 11 June (193.12 to 207.15) after a product announcement.

Compare 9 May 2024: level 183.38, breakout close 184.57 (+0.65%). The very next close was 183.05, below the level: a **failure** by the definition on day one. The 20-day return was 196.89 / 184.57 − 1 = **+6.7%**. The breakout "failed" and the trade made money. Whether you were still in it depends entirely on where your stop was. A stop at the level would have been hit on 10 May; a stop 1 ATR (3.87) below the entry, at 180.70, would not have been, because the lowest low of the next 20 days was 182.13.

That is the point of counting. The failure rate tells you how often the level is retested. It does not tell you whether the trade wins, because that depends on the stop and the holding period you choose. The forward return tells you what happened to the price. It does not tell you what happened to a trader with a stop. To know the trade's outcome you have to simulate the trade, which is the capstone.

## Table

| | SPY | AAPL |
|---|---|---|
| Breakouts (50-day closing high, 10 years) | 219 | 172 |
| Closed back below level within 20 days | 163 (74.4%) | 110 (64.0%) |
| Average 20-day forward return | +0.40% | +1.98% |
| Share of 20-day returns positive | 67.1% | 62.2% |
| Base rate: average 20-day return, all days | +1.13% | +2.27% |
| Base rate: share positive, all days | 68.3% | 64.1% |
| Breakouts on > 1.5× volume | 8 (avg −1.24%) | not tested |

## Using patterns

Define before you count. Write the level rule, the confirmation rule (close or intraday), the failure window and the holding period, and do not change them after you see the results.

Expect the retest. Three in four SPY breakouts and two in three AAPL breakouts came back to the level within a month. A stop exactly at the level is a stop designed to be hit. Either place it outside the level by an ATR fraction, or plan to enter on the retest instead of the break.

Ignore volume confirmation on indexes until you have tested it on your instrument. Individual stocks around news are a different matter, and the AAPL example (a low-volume breakout followed by a 7% single-day move a week later) shows the participation you care about often arrives after the entry.

Ignore the names. A pattern name is a compression of a range and a break. Trade the range and the break, with numbers.

## Sources

- Lo, A. W., Mamaysky, H., & Wang, J. (2000). "Foundations of Technical Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation." *Journal of Finance*, 55(4). https://www.nber.org/papers/w7613
- Sullivan, R., Timmermann, A., & White, H. (1999). "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." *Journal of Finance*, 54(5). https://doi.org/10.1111/0022-1082.00163
- Yahoo Finance. AAPL historical prices (split-adjusted). https://finance.yahoo.com/quote/AAPL/history/
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

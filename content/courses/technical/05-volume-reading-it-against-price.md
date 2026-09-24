---
{
  "title": "Volume: How to Read It Against Price",
  "duration": "13 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Karpoff's 1987 survey of the price–volume literature found the strongest relationship between volume and:", "opts": ["The direction of the next day's move", "The absolute size of price changes (volatility)", "Dividend yield", "Company earnings"], "correct": 1, "explain": "Volume is robustly related to the magnitude of price changes, not their sign. That is why volume is a participation and volatility measure, not a directional one."},
    {"q": "In the worked example, SPY on 24 March 2020 rose 9.06% on 235.5 million shares while the 50-day average was 157.6 million. Relative volume was:", "opts": ["0.67×", "1.49×", "2.31×", "3.00×"], "correct": 1, "explain": "235.5 / 157.6 = 1.49. The biggest up day of the crash came on lower relative volume than the down days that preceded it."},
    {"q": "Why does relative volume fall during a long high-volume period even when daily volume stays high?", "opts": ["Because exchanges cap volume", "Because the moving-average denominator rises as high-volume days enter it", "Because traders lose interest", "Because volume is adjusted for splits"], "correct": 1, "explain": "The 50-day average rose from 123.9M to 157.6M between 13 and 24 March 2020, so equal absolute volume shows as lower relative volume."},
    {"q": "In the ten-year SPY check, the average 5-day forward return after an up day on more than 1.5× normal volume was:", "opts": ["+2.0%, strongly bullish", "−0.79% on 61 cases, below the +0.28% base rate", "Exactly the base rate", "Not measurable"], "correct": 1, "explain": "High-volume up days were followed on average by weakness, the opposite of the 'volume confirms the move' rule. The sample of 61 is small, but the sign is not what the textbook predicts."},
    {"q": "The most defensible use of volume for a rules-based trader is:", "opts": ["To predict direction", "To measure participation and to flag days where the range is likely to be large", "To identify insider trading", "To replace price"], "correct": 1, "explain": "Volume tells you how many shares changed hands and correlates with range. Direction has to come from price."}
  ],
  "task": "Add a relative-volume column (volume divided by its 50-day average) to your spreadsheet and list every day in the past year above 2.0×, with that day's return and the return over the next five days."
}
---

Volume is the number of shares that changed hands in a period. It is the only widely available piece of market data that is not a price, which makes it valuable, and it is the most over-interpreted number on a chart, which makes it dangerous. This lesson shows what volume actually correlates with, how to normalise it so that it means something, and what a ten-year check on SPY says about the most common volume rules.

## What volume measures

Every share bought is a share sold. Volume does not tell you whether "buyers" or "sellers" were in control; it tells you how many transactions occurred. What high volume does indicate is participation and disagreement: more people were willing to transact, and, typically, price had to travel further to find them.

Karpoff (1987) surveyed the empirical literature on price and volume and found one relationship that holds almost everywhere: volume is positively correlated with the **absolute** size of price changes. Big moves happen on big volume, in both directions. The correlation between volume and the **sign** of price changes is weaker and less consistent. Volume is a volatility measure wearing a directional costume.

Blume, Easley and O'Hara (1994) gave a theoretical reason why volume might still carry information beyond price: it can reveal the precision of the information behind a move. A move on heavy volume reflects more participants acting on it. That is a statement about how much you should trust the move's size, not about where price goes next.

Gervais, Kaniel and Mingelgrin (2001) documented a "high-volume return premium": individual stocks with unusually high volume over a day or a week tended to outperform over the following weeks, regardless of the direction of the price move on the high-volume day. Their explanation is visibility: high volume attracts attention and attention attracts buyers. Note two things. The effect is measured on individual stocks in a cross-section, not on an index, and it is independent of direction, which is not what "volume confirms the trend" predicts.

## Normalising volume

Raw volume is meaningless across tickers and across time. SPY trades tens of millions of shares a day; a small-cap might trade a few hundred thousand. Volume also trends: as an ETF grows or a stock splits, its normal level shifts.

Use **relative volume**: today's volume divided by the average volume over a trailing window, usually 20 or 50 days. A value of 1.0 is normal; 2.0 is double normal; 0.5 is half.

One trap: the denominator moves. During a sustained high-volume period the trailing average rises, so a day of identical absolute volume registers as lower relative volume than it did a week earlier. Read relative volume in the context of its own recent path.

## The textbook rules, and the check

Three rules appear in every technical analysis manual:

1. A move on rising volume is confirmed; a move on falling volume is suspect.
2. A climax (very high volume at the end of a trend) marks exhaustion.
3. Breakouts on high volume are more likely to follow through than breakouts on low volume.

Here is what ten years of SPY daily data say about rules 1 and 2. Source: Yahoo Finance historical daily data, September 2016 to September 2026, 2,507 days with a valid 5-day forward return. Relative volume uses a 50-day simple average. The base-rate 5-day forward return over the sample was **+0.28%**.

- After an **up day on more than 1.5× normal volume** (61 cases): average 5-day forward return **−0.79%**.
- After a **down day on more than 1.5× normal volume** (149 cases): average 5-day forward return **+0.35%**.
- After any day on **less than 0.7× normal volume** (434 cases): average 5-day forward return **+0.41%**.

Rule 1 predicts that high-volume up days should be followed by more strength. In this sample they were followed by weakness. Rule 2 (climax) is partly consistent with the down-day result, but the effect is small and the sample of 61 high-volume up days is too thin to build anything on. What the data are consistent with is Karpoff: high volume means high volatility, and after a high-volatility burst the next few days on an index tend to retrace some of it regardless of direction. Rule 3 is tested in Lesson 10, where it also fails to show up on SPY.

## Worked example

The March 2020 crash and reversal on SPY. Source: Yahoo Finance historical daily data. Relative volume (RV) is the day's volume divided by the trailing 50-day average, which is stated for each day because it moved a great deal.

The five days, with each day's relative volume, are laid out in the table below. Work through what the numbers say and do not say.

The arithmetic for 24 March: 235,494,500 / 157,555,432 = **1.49**. For 13 March: 329,566,100 / 123,913,466 = **2.66**. Between those two dates the 50-day average rose by (157.6 − 123.9) / 123.9 = **27%** as crash-volume days replaced normal February days in the window. That is the denominator trap: 20 March's 347.2 million shares was the highest absolute volume in the table, yet its relative volume (2.34×) was below 13 March's.

The close-to-close move from 23 March to 24 March was 243.15 / 222.95 − 1 = **+9.06%**, the largest up day in the sequence, on the lowest relative volume in the table. Under rule 1 this rally was "unconfirmed". SPY closed at 314.38 on 9 July 2020, 29% higher. The unconfirmed rally was the bottom.

Under rule 2, the 20 and 23 March sessions (absolute volume above 325 million, relative volume above 2.1×, closes at or near the low of the range) look like a climax in hindsight. But so did 16 March, a week earlier, and buying that "climax" cost 239.85 → 222.95 = −7.0% over the following five sessions before it worked.

The volume told you what was true on every one of those days: participation was two to three times normal and the range was enormous (16 March: 19.54 points, against a February typical range near 3). It did not tell you which day was the low.

## Table

SPY, March 2020. RV is the day's volume divided by the trailing 50-day average volume.

| Date | Close | Change | Volume | 50-day avg | RV |
|---|---|---|---|---|---|
| 13 Mar 2020 | 269.32 | +8.55% | 329.6M | 123.9M | 2.66× |
| 16 Mar 2020 | 239.85 | −10.94% | 297.2M | 128.7M | 2.31× |
| 20 Mar 2020 | 228.80 | −4.87% | 347.2M | 148.4M | 2.34× |
| 23 Mar 2020 | 222.95 | −2.56% | 326.0M | 153.9M | 2.12× |
| 24 Mar 2020 | 243.15 | +9.06% | 235.5M | 157.6M | 1.49× |

Read the RV column against the Change column: there is no relationship between the size of RV and the sign of the day's return, which is exactly what Karpoff's survey predicts.

## How to use volume honestly

**As a participation flag.** Relative volume above 2× tells you the day mattered to a lot of people. Look at why: an earnings report, an index rebalance, a macro release, an options expiry. The reason often explains the move better than the chart.

**As a range predictor.** High-volume days have larger ranges, and volatility clusters, so the days after a 2× day tend to have larger ranges too. Widen stops accordingly or stand aside.

**As an index-rebalance and expiry filter.** Quarterly "triple witching" Fridays and index reconstitution days routinely print 2× to 3× volume with no information content about direction. Know the calendar so you do not read a mechanical spike as conviction.

**Not as a directional signal.** The ten-year check above gave the textbook rule the wrong sign. If you want to use volume to confirm direction, test it on your ticker and your timeframe first, and expect to be disappointed.

## Sources

- Karpoff, J. M. (1987). "The Relation Between Price Changes and Trading Volume: A Survey." *Journal of Financial and Quantitative Analysis*, 22(1). https://doi.org/10.2307/2330874
- Blume, L., Easley, D., & O'Hara, M. (1994). "Market Statistics and Technical Analysis: The Role of Volume." *Journal of Finance*, 49(1). https://doi.org/10.1111/j.1540-6261.1994.tb04424.x
- Gervais, S., Kaniel, R., & Mingelgrin, D. H. (2001). "The High-Volume Return Premium." *Journal of Finance*, 56(3). https://doi.org/10.1111/0022-1082.00349
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

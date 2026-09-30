---
{
  "title": "MACD: What It Measures and What It Misses",
  "duration": "13 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The MACD line is:", "opts": ["The 12-period EMA minus the 26-period EMA of the close", "The 9-period EMA of the close", "Price minus the 200-day SMA", "The ratio of two moving averages"], "correct": 0, "explain": "MACD = EMA(12) − EMA(26). The signal line is the 9-period EMA of the MACD line, and the histogram is MACD minus signal."},
    {"q": "On 13 October 2022, SPY's EMA(12) was 366.273 and EMA(26) was 374.830. The MACD line was:", "opts": ["+8.557", "−8.557", "−0.286", "+0.286"], "correct": 1, "explain": "366.273 − 374.830 = −8.557. It was still deeply negative; what changed that day was the histogram turning positive."},
    {"q": "Over ten years of SPY, trading every bullish MACD signal-line cross long until the next bearish cross produced 110 trades with a win rate of about:", "opts": ["49%", "70%", "85%", "20%"], "correct": 0, "explain": "49.1% winners, average +0.70%, median −0.07%. The average is positive only because a few long trend-following trades were large."},
    {"q": "Why does MACD give more signals than a 50/200 SMA crossover?", "opts": ["Because it uses volume", "Because 12 and 26-period EMAs are much faster than 50 and 200-period SMAs, so they cross far more often", "Because it is measured in points", "Because it is an oscillator with fixed bounds"], "correct": 1, "explain": "111 bullish crosses in ten years versus 5 golden crosses: the same filter logic at a shorter length produces roughly twenty times the signals and proportionally more whipsaws."},
    {"q": "Between 5 and 13 October 2022, the MACD signal line crossed three times in six trading days. This is an example of:", "opts": ["A reliable reversal", "Whipsaw: rapid alternating signals in a volatile, sideways market", "A divergence", "A histogram squeeze"], "correct": 1, "explain": "Bullish 5 Oct, bearish 11 Oct, bullish 13 Oct. Any crossover system produces clusters of false signals when price chops around the point where the averages meet."}
  ],
  "task": "Compute MACD(12, 26, 9) on your ticker, count the signal-line crosses in the past two years, and note how many were reversed by an opposite cross within ten trading days."
}
---

MACD stands for Moving Average Convergence Divergence. It was developed by Gerald Appel in the late 1970s and it is, underneath the name, the difference between two exponential moving averages. If you understood Lesson 6 you already understand MACD; this lesson shows what the extra pieces add, and gives you a ten-year record of its crossover signals on SPY.

## The three lines

- **MACD line** = EMA(12) − EMA(26) of the close. When the fast average is above the slow one the line is positive; the further apart they are, the larger the value. It is measured in price units, so it is not comparable across tickers.
- **Signal line** = EMA(9) of the MACD line. A smoothed version of the MACD line.
- **Histogram** = MACD line − Signal line. Positive when the MACD line is above its own smoothed version, which means the gap between the two price EMAs is widening upward (or narrowing downward).

The smoothing constants are k = 2/13 = 0.1538 for the 12-period EMA, 2/27 = 0.0741 for the 26, and 2/10 = 0.2 for the 9.

Three signals are conventionally read from these lines:

1. **Signal-line crossover**: MACD crosses above the signal line (bullish) or below it (bearish). Equivalent to the histogram changing sign.
2. **Zero-line crossover**: MACD crosses above or below zero. Equivalent to the 12-EMA crossing the 26-EMA, which is just a fast moving-average crossover.
3. **Divergence**: price makes a new high but the MACD line makes a lower high (bearish divergence), or the reverse.

## What it measures

MACD is a second-derivative-style measure. The MACD line measures how far the fast average is from the slow one, which is a proxy for the rate of change of price over the last few weeks. The histogram measures whether that rate of change is increasing or decreasing. So a rising histogram in an uptrend says the trend is accelerating; a falling histogram while price still rises says it is decelerating.

That is useful as description. As a forecast, it inherits every problem of moving averages: it is a function of past closes, it lags, and it gives more signals the faster you set it.

## What the evidence says

Chong and Ng (2008) tested MACD(12, 26) and RSI rules on the London FT30 from 1935 to 1994 and found that the MACD rule generated returns that beat buy-and-hold in some sub-periods, but the result was sensitive to the period and the profits were small relative to costs. Park and Irwin (2007), surveying the broader literature, put oscillator rules in the same category as moving-average rules: early positive results, weaker after costs and data-snooping adjustment. There is no well-replicated academic result showing that MACD crossovers have out-of-sample predictive value on equity indexes.

## Worked example

SPY, daily closes from Yahoo Finance historical data, September 2016 to September 2026. First the computation on one day, then the full crossover record.

**13 October 2022**, the day of the failed breakdown you studied in Lesson 3. The prior day's values were: EMA(12) 366.329, EMA(26) 375.539, MACD −9.210, signal −8.914, histogram −0.296. SPY closed at 365.97 on 13 October. Update the EMAs:

- EMA(12) = 366.329 + 0.1538 × (365.97 − 366.329) = 366.329 − 0.055 = **366.273**
- EMA(26) = 375.539 + 0.0741 × (365.97 − 375.539) = 375.539 − 0.709 = **374.830**
- MACD = 366.273 − 374.830 = **−8.557**
- Signal = −8.914 + 0.2 × (−8.557 − (−8.914)) = −8.914 + 0.071 = **−8.842**
- Histogram = −8.557 − (−8.842) = **+0.286**

The histogram turned from −0.296 to +0.286: a bullish signal-line crossover on the day of the low. That looks impressive until you look at the six sessions before it: a bullish cross on 5 October (close 377.09), a bearish cross on 11 October (close 357.74), then this bullish cross on 13 October (close 365.97). A trader following every signal bought at 377.09, sold at 357.74 for −5.1%, and bought again at 365.97. The 13 October signal then held until a bearish cross on 6 December at 393.83, a gain of +7.6%. Net across the three signals: roughly +2.1%, having endured a 5% loss to get there.

**The full record.** Over the ten-year sample the signal line crossed **111 times bullish and 110 times bearish**, roughly one cross every 11 trading days. Forward returns after each type of cross, compared with the base rate:

- After a bullish cross: 10-day forward return +0.98% (67.6% positive), 20-day +1.41% (72.1% positive).
- After a bearish cross: 10-day +0.66% (67.3% positive), 20-day +0.90%.
- Base rate, all days: 10-day +0.56% (64.8% positive), 20-day +1.13% (68.3% positive).

Bullish crosses were followed by returns modestly above the base rate. Bearish crosses were followed by returns that were positive and only modestly below the base rate: the market went up after "sell" signals about two-thirds of the time, which is roughly how often it goes up after anything.

As a trading rule (long from bullish cross to next bearish cross, no costs): 110 completed trades, **49.1% winners**, average +0.70%, **median −0.07%**, sum of returns +77.0%. Buy-and-hold over the same span: +214.7%. The positive average comes from a small number of long trend-following trades; the typical trade lost a fraction of a percent. Add a round-trip cost of 0.05% per trade (about $0.35 on a $700 ETF, which is optimistic for slippage) and 110 trades cost 5.5% of the 77%.

## Chart

Described chart: a two-panel daily chart of SPY from 1 September to 31 December 2022. The top panel shows the close, with the 12-EMA and 26-EMA drawn as two lines; the 12 crosses above the 26 (the zero-line cross) on 28 October at a close of 389.02. The bottom panel shows the MACD line and the signal line, both negative throughout September and October, with the histogram as bars. Mark the three signal-line crosses of 5, 11 and 13 October as vertical dashed lines: the histogram flips sign three times inside a band of ±0.5 while the MACD line itself stays between −11.4 and +1.6 across September and October. From 13 October the histogram widens steadily to a peak of +3.58 on 28 October, then shrinks through November even as price rises to 400: that shrinking histogram is the "deceleration" reading, and it preceded the 6 December bearish cross.

## Using MACD

Use the **histogram** as a description of acceleration and deceleration in the trend, on the same timeframe as your trade. It answers "is this move still gaining speed?" with a number.

Treat **signal-line crosses** as noise unless they are filtered by something with independent information, such as the regime label from the 200-day average or a structural swing point from Lesson 4. Unfiltered, they lose about half the time and produce clusters of three signals in a week in exactly the conditions where you least want them.

Ignore the **zero-line cross**; it is a 12/26 EMA crossover and you already know from Lesson 6 what fast crossovers do.

## Sources

- Chong, T. T.-L., & Ng, W.-K. (2008). "Technical analysis and the London stock exchange: testing the MACD and RSI rules using the FT30." *Applied Economics Letters*, 15(14). https://doi.org/10.1080/13504850600993598
- Park, C.-H., & Irwin, S. H. (2007). "What Do We Know About the Profitability of Technical Analysis?" *Journal of Economic Surveys*, 21(4). https://doi.org/10.1111/j.1467-6419.2007.00519.x
- CFA Institute. "Technical Analysis" (Level I curriculum refresher reading). https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/technical-analysis
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

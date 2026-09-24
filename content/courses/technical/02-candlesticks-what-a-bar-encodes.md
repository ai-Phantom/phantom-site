---
{
  "title": "Candlesticks: What a Bar Actually Encodes",
  "duration": "13 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "A daily candlestick contains exactly which pieces of information?", "opts": ["Open, high, low, close, and the sequence in which they occurred", "Open, high, low and close, but not the order in which the high and low were made", "Every trade of the day", "The average price of the day"], "correct": 1, "explain": "A bar is four numbers. Whether the high came before the low is not recoverable from the bar alone; you need a lower timeframe to know."},
    {"q": "In the worked example, SPY on 16 March 2020 opened at 241.18, hit 256.90, fell to 237.36 and closed at 239.85. The upper wick was:", "opts": ["1.33", "2.49", "15.72", "19.54"], "correct": 2, "explain": "Upper wick = high minus the top of the body = 256.90 − 241.18 = 15.72."},
    {"q": "The 'close location value' (close − low) / (high − low) for that same bar was about:", "opts": ["0.13", "0.50", "0.87", "1.00"], "correct": 0, "explain": "(239.85 − 237.36) / (256.90 − 237.36) = 2.49 / 19.54 = 0.127. Price closed in the bottom 13% of its range."},
    {"q": "What did Marshall, Young and Rose (2006) find when they tested classic candlestick patterns on large US stocks?", "opts": ["Every pattern was highly profitable", "The patterns had no predictive value after a bootstrap test", "Candlesticks only work on Japanese stocks", "They did not test candlesticks"], "correct": 1, "explain": "Their bootstrap study of Dow stocks (1992–2002) found candlestick reversal patterns did not forecast returns better than chance."},
    {"q": "Why is a large-range bar on unusually high volume worth noting even if you do not trust pattern names?", "opts": ["Because it always marks a reversal", "Because range and volume are direct measures of disagreement and participation, which are the raw inputs to volatility", "Because it guarantees a gap the next day", "Because it means institutions were buying"], "correct": 1, "explain": "Range and volume are measurable facts. They tell you how much the market disagreed and how many shares changed hands, without any claim about direction."}
  ],
  "task": "Pick any five daily bars on a ticker you follow, and for each compute body, upper wick, lower wick, range and close location value by hand."
}
---

A candlestick is four numbers drawn as a picture. Learn to read the numbers and the picture becomes optional. This lesson strips a bar down to what it encodes, shows how to compute the handful of measurements that matter, and tells you what the evidence says about the named patterns you will see in every trading book.

## The four numbers

For any period (one minute, one day, one week) the exchange feed gives you:

- **Open**: the price of the first trade in the period.
- **High**: the highest traded price.
- **Low**: the lowest traded price.
- **Close**: the price of the last trade.

Daily bars for US stocks use the official opening and closing auction prices set by the primary listing exchange (NYSE or Nasdaq), which is why the daily close is the most-watched single number in the market: it is the price at which index funds, options settlements and margin calculations are computed.

The candle draws the open and close as a rectangle (the **body**) and the high and low as thin lines above and below it (the **wicks** or shadows). If the close is above the open the body is conventionally hollow or green; if below, filled or red.

That is everything. A bar does not tell you whether the high was made before the low, how many trades occurred at each price, or whether the range was built in one burst or across the whole session. To know any of that you have to go down a timeframe.

## Five measurements

Compute these for any bar and you have extracted all its information:

1. **Range** = High − Low. The total distance travelled. This is the raw material of volatility, which you will meet in the ATR lesson.
2. **Body** = |Close − Open|. The net movement from first trade to last.
3. **Upper wick** = High − max(Open, Close). How far price went above the body before being rejected.
4. **Lower wick** = min(Open, Close) − Low. How far it went below.
5. **Close location value (CLV)** = (Close − Low) / (High − Low). Where in the range the bar finished, from 0 (at the low) to 1 (at the high).

The CLV is the most useful of the five because it is scale-free. A close in the top 10% of the range on a large bar says the same thing on a $20 stock and a $700 ETF: the last buyers were paying up into the close.

## What patterns claim

Candlestick pattern names (hammer, shooting star, engulfing, doji, harami) are labels for particular combinations of body size, wick length and CLV, sometimes across two or three bars. A hammer, for example, is a small body near the top of the range with a lower wick at least twice the body's length, appearing after a decline. The story attached is that sellers pushed price down, buyers absorbed the selling, and the close near the high shows the buyers won.

The story is plausible as a description. Whether it predicts anything is an empirical question.

## What the evidence says

Marshall, Young and Rose (2006) tested 28 candlestick patterns on the 35 Dow Jones Industrial Average stocks from 1992 to 2002 using a bootstrap that generates artificial price series with the same statistical properties as the real ones. They found that the patterns had no predictive value: returns after a bullish reversal pattern were not distinguishable from returns after randomly chosen days. A follow-up on Japanese equities (Marshall, Young and Cahan, 2008) reached the same conclusion in the market where the technique originated.

Lo, Mamaysky and Wang (2000) worked with longer multi-bar patterns rather than candlesticks, but their finding is relevant: some patterns occur more often than a random series would produce, yet the authors explicitly declined to claim that trading them is profitable.

Take the practical lesson: the measurements are real, the names are decoration, and the forecasting claim attached to the names has failed when tested. You can still use candlesticks. Use them to describe, and to define where you were wrong.

## Worked example

SPY, 16 March 2020, one of the largest single-day declines in the ETF's history. Source: Yahoo Finance historical daily data for SPY (unadjusted). The numbers:

- Open: 241.18
- High: 256.90
- Low: 237.36
- Close: 239.85
- Volume: 297,240,000 shares
- Prior close (13 March 2020): 269.32

Now the five measurements:

- Range = 256.90 − 237.36 = **19.54**
- Body = |239.85 − 241.18| = **1.33** (close below open, so a down body)
- Upper wick = 256.90 − 241.18 = **15.72**
- Lower wick = 239.85 − 237.36 = **2.49**
- CLV = (239.85 − 237.36) / 19.54 = 2.49 / 19.54 = **0.127**

Some derived facts:

- Gap at the open: 241.18 − 269.32 = **−28.14**, or −10.4% from the prior close. The market opened at a level that triggered the exchange-wide Level 1 circuit breaker (a 7% decline in the S&P 500 halts trading for 15 minutes).
- Day's change close-to-close: 239.85 / 269.32 − 1 = **−10.9%**.
- The body was only 1.33 points, 6.8% of the range. Almost all the day's travel was in the wicks, which means the day was a violent round-trip: price went 15.72 points above the open at some point and finished near the low.
- The 50-day average volume on that date was 128.7 million shares, so the day's volume was 297.2 / 128.7 = **2.31 times** normal.

What does this bar tell you? Descriptively: a huge gap down, a large intraday rally that failed completely, a close in the bottom eighth of the range, on more than double normal participation. A pattern reader would call the long upper wick a "shooting star" and say it is bearish. Here is what actually followed: SPY closed at 222.95 on 23 March (a further −7.0%) and then at 243.15 on 24 March (+9.1% in one session). The bar described a market in disagreement. It did not forecast the direction of the next week, and neither would any other bar.

## Table

| Measurement | Formula | 16 Mar 2020 value | What it measures |
|---|---|---|---|
| Range | High − Low | 19.54 | Total disagreement in the session |
| Body | \|Close − Open\| | 1.33 | Net result of the session |
| Upper wick | High − max(O, C) | 15.72 | Rejected upside |
| Lower wick | min(O, C) − Low | 2.49 | Rejected downside |
| CLV | (C − L) / (H − L) | 0.127 | Where the session finished |
| Gap | Open − prior Close | −28.14 | Overnight repricing |
| Relative volume | Volume / 50-day avg | 2.31× | Participation vs normal |

## How to use bars without believing the names

**Use range to size risk.** If a stock's typical daily range is $3 and you put a stop $0.50 away, you are betting on noise. Lesson 9 formalises this with ATR.

**Use CLV to describe pressure.** A run of closes in the top third of the range says buyers are controlling the close. A run in the bottom third says the opposite. Neither predicts tomorrow, but both describe today accurately.

**Use the bar to define "wrong".** If you buy because a bar closed strongly off its low, the low of that bar is the one price that falsifies your reason. That gives you a stop with a reason behind it, which is more than most stop placements have.

**Ignore single-bar reversal calls.** The evidence is against them, they are subjective to identify, and the same bar can be given a bullish and a bearish name depending on what the author wants to see.

## Sources

- Marshall, B. R., Young, M. R., & Rose, L. C. (2006). "Candlestick technical trading strategies: Can they create value for investors?" *Journal of Banking & Finance*, 30(8). https://doi.org/10.1016/j.jbankfin.2005.08.001
- Lo, A. W., Mamaysky, H., & Wang, J. (2000). "Foundations of Technical Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation." *Journal of Finance*, 55(4). https://www.nber.org/papers/w7613
- NYSE. "Market-Wide Circuit Breakers." https://www.nyse.com/markets/hours-calendars
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

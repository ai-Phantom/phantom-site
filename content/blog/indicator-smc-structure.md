---
{"title": "Smart Money Concepts Structure: Break of Structure and Change of Character", "cat": "indicators", "tag": "Indicators", "emoji": "📈", "excerpt": "The part of LuxAlgo's Smart Money Concepts the bots actually use: swing and internal BOS and CHoCH, sizes 50 and 5. Worked on SPY, 2025.", "date": "2026-10-02", "read": "8 min", "status": "published"}
---

## What it measures

Market structure is the pattern of swing highs and swing lows. An uptrend makes higher highs and higher lows. A downtrend makes lower lows and lower highs.

LuxAlgo's Smart Money Concepts indicator marks two kinds of structure break.

- **Break of structure (BOS):** price closes beyond the last swing point in the direction of the current trend. The trend continues.
- **Change of character (CHoCH):** price closes beyond the last swing point against the current trend. The first sign the trend may be turning.

It does this at two scales. **Swing** structure uses big pivots. **Internal** structure uses small ones.

The full LuxAlgo indicator does much more. **The bots' port includes only BOS and CHoCH.** Order blocks, fair value gaps, equal highs and lows, premium and discount zones, and multi-timeframe levels are not part of the bots' port. If you see them on a chart, the bots are not scoring them.

The bots compute this on daily bars. Swing size is 50. Internal size is 5.

## How it is calculated

**Step 1: find the legs.** Each day, look back exactly `size` bars, 50 for swing structure.

- If that old bar's high is above every high since, including today, a down leg has started. That old high becomes the latest **swing high**.
- If that old bar's low is below every low since, an up leg has started. That old low becomes the latest **swing low**.
- Otherwise the leg continues.

So a swing high on day X only becomes official 50 bars later.

**Step 2: watch for breaks.** Each swing level can be broken once, on a close.

- Close crosses above the latest swing high: bullish break.
- Close crosses below the latest swing low: bearish break.

**Step 3: label the break.** The indicator remembers the direction of the last break, its bias.

- Bullish break with a bearish bias: **bullish CHoCH**. Otherwise **bullish BOS**.
- Bearish break with a bullish bias: **bearish CHoCH**. Otherwise **bearish BOS**.
- After any break, the bias becomes that break's direction.

Internal structure repeats steps 1 to 3 with size 5.

## When it fires in the bots

| Break | Points |
|---|---|
| Swing CHoCH | +20, CALL if bullish, PUT if bearish |
| Swing BOS | +15 |
| Internal CHoCH | +10 |
| Internal BOS | +8 |

Swing breaks are premium signals. A setup needs at least one premium signal before it can post. Structure breaks also qualify for the bots' 8-point trend bonus.

The points are multiplied by a learned weight before they count. For these signals the weight starts at 1.0. It changes only as the bots' own paper trades build a record.

## Worked example

SPY, January to August 2025. Daily bars from Yahoo Finance. The bots recompute structure from the bars they load each scan, so this example uses a trailing window of 250 bars, about a year.

**June 27, 2025: swing bullish CHoCH.** The window runs from June 28, 2024 to June 27, 2025. Replaying it from the start:

1. **October 15, 2024.** The August 5, 2024 low of $510.27 is confirmed as a swing low, 50 bars after it printed.
2. **April 4, 2025.** SPY closes at $505.28, after $536.70 the day before. That crosses below $510.27. There was no earlier break in the window, so the bias was neutral. This is a bearish BOS. The bias turns bearish.
3. **May 1, 2025.** The February 19 high of $613.23 is confirmed as a swing high.
4. **June 18, 2025.** The April 7 low of $481.80 is confirmed as a swing low. SPY was already at $597.44.
5. **June 27, 2025.** SPY closes at $614.91, after $611.87. That crosses above $613.23. The bias was bearish, so this is a **bullish CHoCH. +20 CALL.**

![SPY daily close, 2 Jan to 29 Aug 2025, with the swing levels used by the size-50 structure in a 250-bar window ending 27 Jun 2025: the 613.23 swing high, the 510.27 swing low from 2024 and the 481.80 swing low, and the 4 Apr bearish BOS and 27 Jun bullish CHoCH marked. Data: Yahoo Finance.](figures/indicator-smc-structure.svg)

Now the catch. That April 4 bearish BOS was only visible in hindsight.

A scan on April 4 itself loaded a window starting in April 2024. In that window the latest swing low was a different one: $493.86, from April 19, 2024. SPY's close of $505.28 was above it. So on April 4, no swing break fired at all. The break at $510.27 only appears when you replay the year from a later starting point.

And with history back to January 2022, the leg never turned down in late 2024. The August 2024 low never became a swing low. There is no bearish break in April, and June 27 reads as a bullish **BOS** worth 15 points, not a CHoCH worth 20.

Same price. Same day. The label depends on where the data starts.

The internal structure was busier. In the windows the bots would have seen on each day, an internal bearish BOS fired on April 3 (+8 PUT) and an internal bullish CHoCH on April 24 (+10 CALL).

Whether a setup posted on any of these days depended on every other signal and gate that day.

## How to read it yourself

The full LuxAlgo indicator is open source on TradingView. To match the bots, use the daily chart, set the swing length to 50, and turn off order blocks, fair value gaps, equal highs and lows, and the zones.

1. **Find the last swing high and swing low.** Those are the two levels that matter. A close beyond either one is the next break.
2. **Ask which way the last break went.** That tells you whether the next break will be a BOS or a CHoCH.
3. **Remember the 50-bar delay.** On the chart, a swing label sits on the bar where the pivot formed. That pivot was not known until 50 bars later. The chart makes it look as if the indicator knew sooner than it did.
4. **Use internal breaks for detail, swing breaks for direction.** Internal structure flips often. Swing structure flips rarely.

## Known weaknesses

**Heavy lag.** A size-50 swing point is confirmed 50 bars after it forms. In the example, the April 7 low was confirmed on June 18, after SPY had risen from $504.38 to $597.44.

**Labels depend on loaded history.** As the example shows, BOS versus CHoCH, and whether a break exists at all, can change with the start of the data. Your TradingView chart, with years of history, can disagree with the bots.

**Swing breaks are rare on daily index charts.** In our replication, the bots' swing structure on SPY broke only twice between January 2025 and September 2026: June 27, 2025 and April 15, 2026.

**Internal breaks are noisy.** Size 5 confirms pivots in a week. On a daily chart that produces many small breaks in both directions.

**Closes only.** A wick through a level does not count. A close one cent through it does.

**The bar may not be finished.** The bots scan during the session. A close-based break on a live bar can disappear by the actual close.

## Credit

Smart Money Concepts (SMC) is by **LuxAlgo**, published open source on TradingView under CC BY-NC-SA 4.0. The bots port only its BOS and CHoCH structure logic, at swing size 50 and internal size 5.

## Sources

- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/
- LuxAlgo, Smart Money Concepts (SMC): https://www.tradingview.com/script/CnB3fSph-Smart-Money-Concepts-SMC-LuxAlgo/
- Phantom Traders bot code (October 2026)

*Educational content, not financial advice. Signals are paper-traded.*

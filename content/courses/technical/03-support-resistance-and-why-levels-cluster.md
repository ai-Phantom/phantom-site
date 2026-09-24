---
{
  "title": "Support, Resistance, and Why Levels Cluster",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The best-supported mechanism for why support and resistance exist is:", "opts": ["Prices have memory built into them", "Resting orders (stops and limits) cluster at prior highs, prior lows and round numbers, so price reacts where the orders sit", "Market makers draw the lines", "It is a purely psychological illusion with no mechanism"], "correct": 1, "explain": "Osler (2000, 2003) used actual dealer order books to show that customer orders cluster at these levels, which is a mechanism rather than a belief."},
    {"q": "In the worked example, SPY's October 2022 low of 348.11 was below the June 2022 low of 362.17 by about:", "opts": ["1.0%", "3.9%", "8.5%", "12.0%"], "correct": 1, "explain": "(348.11 − 362.17) / 362.17 = −3.9%. The level 'broke' by that amount intraday and then closed back inside the zone the same day."},
    {"q": "Why should support be treated as a zone rather than a line?", "opts": ["Because charts are drawn imprecisely", "Because orders cluster around a level rather than exactly at it, and the low of a test can undercut a prior low before buyers respond", "Because zones look better on a chart", "Because lines are only for resistance"], "correct": 1, "explain": "Order clustering is approximate, and the October 2022 undercut of the June low is a concrete example of a test that went through the line and held the zone."},
    {"q": "A level that has been tested many times without breaking is:", "opts": ["Guaranteed to hold next time", "Likely to have fewer resting orders left, because each test fills some of them", "Irrelevant", "Always a reversal point"], "correct": 1, "explain": "Each test consumes orders at the level. Osler's data suggest levels weaken with repeated tests rather than strengthen, contrary to the popular claim."},
    {"q": "In the round-number check on ten years of SPY and AAPL daily data, what fraction of daily lows fell within $0.10 of a $10 multiple, versus the 2.0% expected by chance?", "opts": ["About 2.0–2.2%, barely above chance", "About 10%", "About 25%", "Zero"], "correct": 0, "explain": "SPY lows: 2.19%; AAPL lows: 2.03%. The round-number effect Osler found in FX order data is at best weak in these daily equity series."}
  ],
  "task": "On a ticker of your choice, mark the three most-tested price zones of the past year, write down the exact high and low of each zone, and note whether each test undercut or held the prior extreme."
}
---

Support is a price area where buying has previously stopped a decline. Resistance is a price area where selling has previously stopped an advance. Those are descriptions of the past. The interesting questions are why the same areas keep mattering, how much they matter, and how to use them without pretending they are walls.

## The mechanism: orders cluster

Price does not remember anything. Orders do. A stop-loss order placed by someone who bought at a prior low, a limit order placed by someone who wants to buy "if it gets back down there", a take-profit order set at a round number: these rest in brokers' systems and at the exchange, and they get triggered when price arrives.

Osler (2000) examined the order book of a large currency dealer and found that stop-loss orders cluster just beyond round numbers and take-profit orders cluster just at them. Osler (2003) showed that, because of this, exchange rates reverse more often at round numbers than chance would predict, and that once they do break through, they move faster, because the clustered stops become market orders. This is the single best piece of evidence for support and resistance as a real phenomenon, and it comes from looking at orders rather than at charts.

The implication for equities is straightforward. Prior swing highs and lows are where the most people bought or sold most recently, so they are where the most stops and limits will sit. Round numbers attract orders because people think in round numbers. Where orders cluster, price reacts.

## What that mechanism does and does not imply

It implies that levels are **zones**, not lines. Orders cluster around a price, not exactly at it. A test of a prior low can go through the low by a fraction of a percent, trigger some stops, and then find the limit buyers who were sitting slightly lower. The line was broken; the zone held.

It implies that levels **weaken with repeated tests**, not strengthen. Each test fills some of the resting orders. The popular claim that "the more times a level is tested, the stronger it gets" has the mechanism backwards. What repeated tests do show is that the level is being watched, which brings new orders in, so the net effect is ambiguous. Do not assume strength from repetition.

It implies that a **clean break** through a zone can accelerate, because clustered stops become market orders in the direction of the break. This is the basis for breakout trading. It is also why breakouts are so often false: the same clustered stops get triggered by a brief undercut that then reverses, as in the worked example below.

It does not imply any particular win rate. Osler's effect was strongest in currencies, intraday, at round numbers. Equity daily data are noisier and the round-number effect in particular is weak there (see the check at the end of the worked example).

## Finding levels

You do not need drawing tools. A level is a prior swing high or low. Lesson 4 gives you an algorithm for finding swings; for now, use this rule of thumb: a daily low that is lower than the ten bars before it and the ten bars after it is a swing low. The same for highs.

Then group swings that fall within roughly one average daily range of each other into a zone. Record the zone's top and bottom, the dates of each test, and whether each test undercut or held the previous extreme. That log is more useful than any line on a chart.

## Worked example

SPY in 2022. Source: Yahoo Finance historical daily data, unadjusted. The bear market of that year made a low in June, retested it in late September and October, and reversed. Here are the tests of the zone between 357 and 367 (numbers in dollars):

- **16 June 2022**: low 364.08, close 366.65. **17 June**: low 362.17, close 365.86. This pair set the June low.
- **23 to 29 September**: lows of 363.29, 363.03, 360.87, 362.60 and 359.70, all inside or slightly under the June lows. Closes ranged 362.79 to 370.53.
- **30 September**: low 357.04, close 357.18. First close below the June low of 362.17, by 4.99 points or 1.4%.
- **3 to 12 October**: lows 359.21, 366.57, 360.94, 357.67, 355.71, 356.30. Closes from 356.56 (the lowest close of the year, 12 October) to 377.97.
- **13 October**: open 349.21, low 348.11, high 367.51, close 365.97.

Now the arithmetic for the decisive day. The 13 October low undercut the June low by 348.11 − 362.17 = −14.06 points, or 14.06 / 362.17 = **−3.9%**. It undercut the prior day's close by 356.56 − 348.11 = 8.45 points. The day's range was 367.51 − 348.11 = 19.40 points, against a 14-day average true range of 8.96, so the day travelled 2.2 times its normal distance. It closed at 365.97, which is 365.97 − 348.11 = 17.86 points off the low, giving a close location value of 17.86 / 19.40 = **0.92**. Volume was 147.3 million shares against a 50-day average of 82.1 million, or 1.79 times normal.

Read it through the order-clustering mechanism. The June low at 362.17 had four months of stops sitting under it. The 30 September close at 357.18 triggered the first layer. The 13 October open at 349.21 (the morning of a hotter-than-expected inflation report) triggered the rest. Once those stops had become market sells and been absorbed, there was no one left to sell, and price closed back inside the zone. That is what a failed breakdown looks like in the data, and it is the pattern Osler's mechanism predicts: acceleration through the level, then a reversal once the clustered orders are consumed.

What the example does not tell you: that the zone would hold. On 12 October the year's lowest close printed and nobody knew the next day would reverse. A trader buying the zone on 30 September at 357.18 and holding through 13 October had to sit through an intraday loss of (348.11 − 357.18) / 357.18 = −2.5% before being right. The zone was a place to look for a trade and a place to define a stop. It was not a floor.

**Round-number check.** A quick test of the other half of Osler's claim on daily equity data: across 2,512 daily bars each of SPY and AAPL (September 2016 to September 2026), the share of daily lows falling within $0.10 of a multiple of $10 was 2.19% for SPY and 2.03% for AAPL, against 2.00% expected by chance if lows were uniformly distributed. Highs: 2.43% and 1.95%. Whatever round-number clustering exists in these series is too small to see at daily resolution. Do not carry a currency-market finding into equities without checking.

## Table

| Test date | Low | Close | Below June low (362.17)? | Outcome |
|---|---|---|---|---|
| 16–17 Jun 2022 | 362.17 | 365.86 | Sets the level | Rally to 431.73 by 16 Aug |
| 23–29 Sep 2022 | 359.70 | 362.79 | Yes, intraday only (−0.7%) | Continued lower |
| 30 Sep 2022 | 357.04 | 357.18 | Yes, on a close (−1.4%) | Bounce to 377.97 on 4 Oct |
| 10–12 Oct 2022 | 355.71 | 356.56 | Yes, on a close (−1.6%) | Lowest close of the year |
| 13 Oct 2022 | 348.11 | 365.97 | Yes, intraday (−3.9%), close back inside | Failed breakdown; rally to 410.49 by 13 Dec |

## Using levels without believing in them

Treat every zone as three numbers: the top, the bottom, and the amount beyond the bottom you are willing to be wrong by. The third number is your stop, and it should be outside the zone by at least a fraction of the average daily range, because the mechanism guarantees that the line itself will be probed.

Log each test. Write down whether it undercut, by how much, and what the close did. After twenty tests on one ticker you will know something about that ticker's habit: some instruments respect prior lows to the cent, others routinely undercut by 1 to 2% before turning. That habit is the only thing that makes a level tradeable, and you can only learn it by measuring.

## Sources

- Osler, C. L. (2000). "Support for Resistance: Technical Analysis and Intraday Exchange Rates." *Federal Reserve Bank of New York Economic Policy Review*, 6(2). https://www.newyorkfed.org/research/epr/00v06n2/0007osle.html
- Osler, C. L. (2003). "Currency Orders and Exchange Rate Dynamics: An Explanation for the Predominant Success of Technical Analysis." *Journal of Finance*, 58(5). https://doi.org/10.1111/1540-6261.00588
- Brock, W., Lakonishok, J., & LeBaron, B. (1992). "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns." *Journal of Finance*, 47(5). https://www.jstor.org/stable/2328994
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/

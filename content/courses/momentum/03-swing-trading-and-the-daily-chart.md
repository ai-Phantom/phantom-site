---
{
  "title": "Swing Trading Defined: Holding Periods and the Daily Chart",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A swing trade, as defined in this course, is held for:", "opts": ["Minutes", "Days to a few weeks, with decisions made on daily bars", "At least one year", "Until the stock doubles"], "correct": 1, "explain": "Swing trading sits between day trading and position trading. The holding period is set by the exit rule on the daily chart, and in the course's backtest it averaged about 21 trading days with a median of 15."},
    {"q": "On SPY daily data from 2024-09-24 to 2026-09-23, the mean one-day return was 0.065% with a standard deviation of 1.04%; the mean ten-day return was 0.63% with a standard deviation of 2.73%. The ratio of mean to standard deviation:", "opts": ["Fell from 0.23 to 0.06 as the horizon lengthened", "Rose from 0.06 to 0.23 as the horizon lengthened", "Was the same at both horizons", "Cannot be computed"], "correct": 1, "explain": "0.065 / 1.04 = 0.062 and 0.632 / 2.73 = 0.231. The drift compounds linearly with time while the noise grows roughly with the square root, so longer windows have a better signal-to-noise ratio."},
    {"q": "Why does the course use the daily close as its decision price?", "opts": ["It is the only price Yahoo reports", "It is the price at which the whole session's participants have settled, it is not subject to intraday noise, and it can be evaluated once a day without watching a screen", "It is always the high of the day", "Brokers require it"], "correct": 1, "explain": "The close is a consensus price. Evaluating rules on it removes the temptation to react to intraday moves and makes the system reproducible from free daily data."},
    {"q": "The FINRA pattern day trader rule applies to accounts that:", "opts": ["Hold any stock overnight", "Execute four or more day trades within five business days in a margin account, subject to the $25,000 minimum equity requirement", "Trade more than 100 shares", "Use stop orders"], "correct": 1, "explain": "A swing trader who holds overnight is not making day trades, so the rule does not bind. It is one practical reason the multi-day holding period suits smaller accounts."},
    {"q": "SPY closed at 496.48 on 2025-04-08 and 548.62 the next day, a one-day gain of 10.5%. Ten sessions after 2025-04-08 it closed at 535.42. What does this pair of figures illustrate?", "opts": ["Ten-day returns are always smaller than one-day returns", "A single daily bar can carry more movement than the following two weeks combined, which is why swing rules are evaluated on the close and sized for gaps", "The market only moves on Wednesdays", "Nothing; it is an outlier and should be ignored"], "correct": 1, "explain": "The one-day move was +10.5% and the ten-day move was +7.8%, so the nine sessions after the jump gave part of it back. Daily bars contain the shocks; the swing horizon contains the drift."}
  ],
  "task": "Open a daily chart of any stock on your list, mark the last three swings that lasted between five and twenty sessions, and note what ended each one."
}
---

Swing trading is holding a position for days to a few weeks, deciding on daily bars, and getting out when a rule on those bars says so. That is the whole definition. It sits between day trading, which closes everything before the bell, and position trading, which holds through quarters. The horizon is not arbitrary. It is the one where momentum's drift is large enough to matter and short enough that a stop still protects you, and this lesson shows that with numbers.

## Why the horizon matters

Every horizon has a signal and a noise. The signal is the average drift you expect to collect; the noise is the spread of outcomes around it. Over a single day, drift is tiny and noise is not, so one-day results are almost entirely luck. Over a year, the drift dominates but a stop placed to survive a year's worth of noise is so far away that it no longer limits anything. Somewhere in between, the ratio of drift to noise is good enough to trade and the stop is close enough to mean something.

There is a classical result underneath this. If daily returns were independent, the standard deviation of a ten-day return would be the daily standard deviation times the square root of ten, while the mean would be ten times the daily mean. Signal grows with time; noise grows with its square root. Lo and MacKinlay (1988) showed that weekly stock returns do not quite follow a random walk, and the worked example below finds the same thing on recent data: the ten-day noise is a little less than the square-root rule predicts, which is good for a swing trader.

## Worked example

Data: SPY daily closes from Yahoo Finance's chart API, `https://query1.finance.yahoo.com/v8/finance/chart/SPY?range=2y&interval=1d`, pulled 2026-09-24, covering 2024-09-24 to 2026-09-23, 501 sessions. Returns are close-to-close.

One-day returns: 500 observations, mean **+0.065%**, standard deviation **1.041%**. Share of positive days: **54.8%**.

Ten-day returns (each close divided by the close ten sessions earlier): 491 observations, mean **+0.632%**, standard deviation **2.732%**. Share of positive windows: **61.9%**.

Signal-to-noise at one day: 0.065 / 1.041 = **0.062**. At ten days: 0.632 / 2.732 = **0.231**. The ratio improved by a factor of 3.7 from lengthening the window. The square-root rule would have predicted a ten-day standard deviation of 1.041 × √10 = 3.29%; the observed 2.73% is lower, which means some of the daily moves in this sample were partly given back over the following days rather than compounding. That is a mild mean-reversion at the one-to-two-week horizon, layered on top of the longer momentum drift.

One dated instance makes the point concrete. SPY closed at 496.48 on 2025-04-08 and at 548.62 on 2025-04-09, a one-day return of 548.62 / 496.48 − 1 = **+10.5%**. Ten sessions after 2025-04-08, on 2025-04-23, it closed at 535.42, a ten-day return of 535.42 / 496.48 − 1 = **+7.8%**. One bar carried more than the entire two weeks. A day trader flat at the close of the 8th missed all of it; a swing trader long from the prior week collected it, and a stop placed inside the normal daily range would have been jumped by the gap the other way had the news gone the other way. Daily bars carry the shocks. The swing horizon carries the drift.

Here is what the horizon looks like from inside a system. Lesson 12 backtests a 20-day breakout rule with a trailing exit on the same twenty stocks used throughout this course, from December 2024 to August 2026. It produced 100 trades. Their holding periods, in trading days from entry to exit:

| Holding period | Trades | Share |
|---|---|---|
| 0 to 5 days | 23 | 23% |
| 6 to 20 days | 37 | 37% |
| 21 to 40 days | 27 | 27% |
| More than 40 days | 13 | 13% |
| Mean 21.5 days, median 15.5 days, longest 109 days | 100 | 100% |

Nobody chose those numbers. The entry rule and the exit rule produced them. Almost a quarter of trades ended inside a week, which is the stop doing its job on breakouts that failed at once; the winners ran for a month or two. A "swing trade" is therefore not a fixed duration; it is what falls out of a daily-bar rule, and the distribution is skewed, short losers and long winners. That skew is the shape of a working momentum system, and it will come up again in lesson 8.

## The daily chart as the unit of decision

This course evaluates every rule on the daily close. Three reasons.

The close is a consensus. Intraday prices are bids and offers meeting under time pressure; the close is where the session's participants settled. A breakout that holds into the close has been tested against the sellers who had all day to lean on it.

The close is once a day. A rule you evaluate at 4:05 p.m. cannot be triggered by a 10:15 wobble, cannot be overridden because you happened to be watching, and can be checked from free end-of-day data years later. That last property is what makes lesson 12 possible.

The close is what the academic evidence is built on. Every momentum study in this course uses daily or monthly closes. If you trade off intraday triggers, as lesson 5 allows in one specific case, you are extending the evidence, not applying it.

You can still look at intraday charts. Just do not decide on them unless the rule says so.

## Practical consequences of the horizon

**Overnight risk is the risk.** A swing trader is exposed to gaps by definition. Lesson 6 sizes for it and lesson 11 tells you when to step aside for scheduled events.

**The pattern day trader rule does not bind.** FINRA's rule flags accounts that make four or more day trades within five business days in a margin account and requires $25,000 in equity to continue. A trader who holds overnight is not day trading, which makes the swing horizon accessible to smaller accounts.

**Costs are amortised over days, not minutes.** A round trip that costs 0.10% of the position is trivial against a 6% swing and ruinous against a 0.3% scalp. Lesson 12 charges 0.10% per side and you will see it matters but does not dominate.

**You need the daily data, and only the daily data.** Twenty tickers, two years, one API call each. The whole course runs on that.

## Sources

- Lo, A. W. and MacKinlay, A. C. (1988). Stock market prices do not follow random walks: evidence from a simple specification test. *Review of Financial Studies*, 1(1), 41–66. https://doi.org/10.1093/rfs/1.1.41
- FINRA. Day trading: margin requirements for pattern day traders. https://www.finra.org/investors/investing/investment-products/stocks/day-trading
- Jegadeesh, N. and Titman, S. (1993). Returns to buying winners and selling losers. *Journal of Finance*, 48(1), 65–91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Yahoo Finance historical data, SPY: https://finance.yahoo.com/quote/SPY/history/

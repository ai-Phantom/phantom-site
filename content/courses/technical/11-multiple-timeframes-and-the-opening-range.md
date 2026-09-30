---
{
  "title": "Multiple Timeframes and the Opening Range",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The purpose of reading a higher timeframe before a lower one is:", "opts": ["To find more signals", "To classify the regime (trend, range, distance from key levels) so that lower-timeframe signals are taken only in the direction the higher timeframe permits", "To avoid the lag of moving averages", "Higher timeframes are always more accurate"], "correct": 1, "explain": "The higher timeframe is a filter. It reduces the number of trades you take, which is the point; whether it improves them has to be tested."},
    {"q": "In the week ending 14 October 2022, SPY closed at 357.63 with the 40-week SMA at 411.65 and the daily 200-day SMA at 415.72. Both timeframes agreed that:", "opts": ["SPY was in an uptrend", "SPY was well below its long-term averages (about 13–14% below), in a downtrend regime", "SPY was overbought", "The weekly and daily disagreed"], "correct": 1, "explain": "357.63 / 411.65 − 1 = −13.1% and 357.63 / 415.72 − 1 = −14.0%. Both timeframes gave the same regime label; the daily then gave the short-term reversal signal inside it."},
    {"q": "On 16 September 2026 the SPY 30-minute opening range was 758.72 to 760.43. The first 5-minute close above the range was 760.53 at 11:00. With the stop at the range low, the risk per share was:", "opts": ["0.10", "1.71", "1.81", "6.46"], "correct": 2, "explain": "760.53 − 758.72 = 1.81. The stop was hit at 14:30; the day closed at 754.07, so a trader without the stop lost 6.46."},
    {"q": "Over the 60 sessions from 30 June to 23 September 2026, the simple 30-minute opening-range breakout on SPY with a stop at the opposite side of the range produced:", "opts": ["A 75% win rate", "41.7% winners, 35% of days stopped out, and a net loss of about 18 points", "No breakouts at all", "A guaranteed profit"], "correct": 1, "explain": "Every day broke out of its range, most breakouts reversed at least partially, and the average day lost 0.30 points before costs. A 60-day sample is far too small to conclude anything durable, in either direction."},
    {"q": "Under FINRA Rule 4210, a 'pattern day trader' in a US margin account must maintain minimum equity of:", "opts": ["$2,000", "$5,000", "$25,000", "$100,000"], "correct": 2, "explain": "Four or more day trades in five business days in a margin account (above 6% of activity) triggers the designation, which requires $25,000 minimum equity."}
  ],
  "task": "For one week, write down the weekly and daily regime labels (trend direction, position relative to the 40-week and 200-day averages) for your ticker before the open, then record the 30-minute opening range and whether the first breakout of it held to the close."
}
---

A daily bar is 78 five-minute bars. A weekly bar is five daily bars. Every timeframe is a different level of compression of the same transactions, and each level hides what the others show. This lesson covers how to use a higher timeframe as a filter for a lower one, and then examines the most widely taught intraday setup, the opening range breakout, on real 5-minute data with a real result.

## Timeframes as a hierarchy of filters

A trader working on daily bars uses the weekly chart to answer one question: what is the regime? Is the weekly structure making higher highs and higher lows (Lesson 4)? Is price above or below its 40-week average (roughly the 200-day)? How far is it from the nearest weekly swing level? Those answers do not generate trades. They decide which daily signals are allowed.

The logic is the same at every level. A day trader on 5-minute bars uses the daily chart for regime and the 30-minute chart for structure, then looks for entries on the 5-minute. The higher timeframe is always the filter, the lower timeframe is always the trigger, and the stop and target are sized from the timeframe you entered on.

There is a cost: the higher timeframe updates slowly. When the weekly regime is "downtrend", the daily chart may have already turned up for weeks before the weekly confirms it. Different regime definitions also turn at different times. In Lesson 4 the daily swing structure of SPY confirmed a change to uptrend on 16 February 2023; the weekly 10-week average had crossed above the 40-week three weeks earlier, on 27 January 2023, and the daily 50/200 golden cross came on 2 February. Three reasonable definitions of the same regime change, spread across a month. Filters reduce trades; they also delay them, by an amount that depends on which filter you chose.

Here are the numbers for the October 2022 low, from Yahoo Finance daily and weekly data. The week ending 14 October 2022 closed at 357.63. The 40-week SMA was 411.65 and the 10-week SMA was 388.45, so the weekly close was 357.63 / 411.65 − 1 = **13.1% below** its long-term average and the weekly regime was unambiguously "downtrend". On the daily chart on 13 October the 200-day SMA was 415.72 and the 50-day was 393.63. Both timeframes agreed. A daily-timeframe signal that day (the RSI(2) reading of 5.3 from Lesson 7, or the failed breakdown from Lesson 3) was a **counter-trend** signal inside a confirmed downtrend on every higher timeframe. That does not make it wrong; it makes it a different kind of trade, with a smaller expected move and a tighter time limit, and a rule that only takes signals in the direction of the weekly regime would have skipped it.

## The opening range

The opening range (OR) is the high and low of the first n minutes of the regular session, usually 5, 15, 30 or 60 minutes after the 9:30 ET open. The opening range breakout (ORB) enters when price moves beyond the range, with the stop at the opposite side of the range and an exit at a target or at the close.

The argument for it is structural: the open is where overnight information is priced, the first half hour has the highest volume and widest spreads of the day, and the range it establishes is the day's first real support and resistance zone. The argument against it is that every intraday participant knows this, so the stops sitting just outside the range are the first thing to be run.

Zarattini and Aziz (2023) reported strong results for a 5-minute ORB on a basket of high-volume US stocks from 2016 to 2023, using a volatility-based stop and a large target; Zarattini, Aziz and Barbon (2024) reported similar results for an intraday momentum strategy on SPY that uses a "noise band" around the open rather than a fixed range. Both are working papers, both were published after the strategies were designed, and both use leverage and cost assumptions you should read before drawing conclusions. Marshall, Cahan and Cahan (2008), testing a large set of intraday technical rules on SPY at 5-minute intervals, found none that were profitable after adjusting for data snooping. The academic record on intraday technical trading is thin and mostly negative; the practitioner record is enthusiastic and mostly untested.

## Worked example

SPY, 5-minute bars, regular session only, 30 June to 23 September 2026 (60 sessions), from Yahoo Finance intraday data. The rule, defined before looking at the outcome:

- Opening range: high and low of the six 5-minute bars from 9:30 to 9:59 ET.
- Entry: the close of the first 5-minute bar (from 10:00 onward) that closes above the range high (long) or below the range low (short). One trade per day, first side to break.
- Stop: the opposite side of the range, checked against every subsequent bar's high or low.
- Exit: the stop, or the 16:00 close.
- No costs, no slippage, no target.

**16 September 2026.** The opening range: high 760.43 (set at 9:50), low 758.72 (set at 9:40), range 1.71 points. Price sat inside the range for an hour. The 11:00 bar closed at 760.53, 0.10 above the range high: long entry at 760.53, stop at 758.72, risk per share = 760.53 − 758.72 = **1.81**. The 11:05 bar reached 761.03, the high of the trade. Price then sank; the 14:30 bar traded through 758.72 and the stop was filled at −1.81. SPY went on to close at 754.07, with an intraday low of 749.60. Without the stop the loss would have been 754.07 − 760.53 = **−6.46**, 3.8 times the opening range.

**21 September 2026**, for contrast. Range 766.03 to 767.72 (1.69 points). The 10:10 bar closed at 767.79: long at 767.79, stop 766.03, risk 1.76. The stop was never touched; the close was 773.52, for +5.73, or 3.3 times the risk.

**The 60-session record.** Every one of the 60 sessions broke its range on a 5-minute close: 27 long, 33 short. Outcomes:

- Winners: 25 of 60, **41.7%**.
- Stopped out at the opposite side of the range: 21 of 60, **35.0%**. The remaining 14 losers ran to the close below entry without touching the stop.
- Average winner: +2.07 points. Average loser: −2.00 points.
- Expectancy per day: 0.417 × 2.07 − 0.583 × 2.00 = 0.863 − 1.166 = **−0.30 points**, before any costs. Sum over 60 days: **−18.22 points**.
- By month: July −17.21, August +1.44, September −4.41.
- Average opening range: 2.46 points, or 0.32% of a price near 765.

The July result dominates. Removing it would leave a small negative number. Nothing in this sample suggests the rule as defined has an edge on SPY, and nothing in a 60-day sample could establish one either way: with an average absolute daily outcome near 2 points and a standard deviation of a similar size, distinguishing an expectancy of +0.3 from −0.3 would need several hundred days.

Two things the example does show. First, the 1:1 stop at the opposite side of the range is hit on more than a third of days; the range is small relative to the day's movement, and price routinely traverses it in both directions. Second, the winners that do run (21 September at 3.3 R; 4 August at +7.41, the best of the sample) are the entire source of return; the average winner is only slightly larger than the average loser because most winners are small. An ORB rule lives or dies on its exit, not its entry, which is the same conclusion Lesson 12 reaches for a daily rule.

## Table

| Item | Value (SPY, 30 Jun – 23 Sep 2026, 60 sessions) |
|---|---|
| Opening range definition | High/low of 9:30–9:59 ET (six 5-minute bars) |
| Sessions with a breakout on a 5-minute close | 60 of 60 (27 long, 33 short) |
| Winning sessions | 25 (41.7%) |
| Sessions stopped at opposite side of range | 21 (35.0%) |
| Average winner / average loser | +2.07 / −2.00 points |
| Expectancy per session (no costs) | −0.30 points |
| Net over 60 sessions | −18.22 points |
| Average opening range | 2.46 points (0.32%) |
| Best session | 4 Aug 2026, +7.41 (held to the close) |
| Worst session | 31 Jul 2026, −5.98 (stopped; a wide range) |

## Regulatory and practical notes

Day trading in a US margin account is governed by FINRA Rule 4210. Four or more day trades within five business days, where those trades exceed 6% of total trading activity, makes you a "pattern day trader" and requires $25,000 of minimum equity in the account. The SEC and FINRA investor pages on day trading are blunt about the base rates: most people who attempt it lose money, and the costs (spread, commissions, data, time) are paid whether or not the strategy has an edge.

The regular session for US equities runs 9:30 to 16:00 ET; the first and last half hours carry the highest volume and the widest ranges. If you test an intraday rule, test it with the session boundaries and the volatility profile of the day built in, and use a data source that separates regular-session bars from pre-market and after-hours trades, or your opening range will be wrong.

## Sources

- Zarattini, C., & Aziz, A. (2023). "Can Day Trading Really Be Profitable? Evidence of Sustainable Long-term Profits from Opening Range Breakout Strategies." SSRN Working Paper 4416622. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622
- Marshall, B. R., Cahan, R. H., & Cahan, J. M. (2008). "Does intraday technical analysis in the U.S. equity market have value?" *Journal of Empirical Finance*, 15(2). https://doi.org/10.1016/j.jempfin.2007.07.001
- FINRA. Rule 4210, Margin Requirements (pattern day trader provisions). https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- NYSE. Trading hours and calendars. https://www.nyse.com/markets/hours-calendars

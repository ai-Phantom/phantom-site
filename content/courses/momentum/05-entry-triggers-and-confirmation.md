---
{
  "title": "Entry Triggers and Confirmation",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2025-06-25 NVDA closed at 154.31. What made that close a valid breakout trigger under this lesson's rule?", "opts": ["It was the highest close of the year", "It was above the prior 20-day high of 147.96, above a rising 50-day average, and on higher volume than the prior sessions", "The RSI crossed 70", "NVDA had reported earnings that morning"], "correct": 1, "explain": "The trigger is a close above a defined level with the trend and participation confirming it. The 20-day high was 147.96, the 50-day average was 127.76 and rising, and volume was 269 million shares against roughly 150 to 190 million on the preceding days."},
    {"q": "Why does this course trigger on the daily close rather than the first intraday tick through the level?", "opts": ["Closes are always higher than intraday prices", "Intraday pokes through a level that fail by the close are common, and the close is the price that most participants have agreed on for the day", "Brokers do not accept intraday orders", "Volume is only reported at the close"], "correct": 1, "explain": "A close above the level filters out failed intraday probes. You pay for that filter with a worse entry price, which is the trade-off the lesson describes."},
    {"q": "In the TSLA example on 2026-09-03, the 30-minute opening range was 365.91 to 378.23 and the range high was first exceeded at 10:20. The day closed at 376.37. Which statement is correct?", "opts": ["The opening-range trigger fired and the day closed above it", "The opening-range trigger fired, the day closed below the trigger but above the daily breakout level, and the next session fell through both", "No trigger fired that day", "The daily breakout level was never exceeded"], "correct": 1, "explain": "The trigger fired at 10:20 near 378.3, the close of 376.37 was under it but above the 368.92 twenty-day high, and on 2026-09-04 the stock traded down to 351.32."},
    {"q": "A pullback-to-a-rising-average entry differs from a breakout entry mainly in that:", "opts": ["It needs no stop", "It buys closer to the technical level, so the stop is tighter and the position can be larger for the same risk, at the cost of sometimes buying a pullback that keeps falling", "It only works in bear markets", "It requires options"], "correct": 1, "explain": "Buying near the average shortens the distance to the level that proves you wrong. The same dollar risk therefore buys more shares, but a pullback can become a reversal."},
    {"q": "Which of these is a confirmation, not a trigger?", "opts": ["A close above the 20-day high", "A 5-minute bar trading through the opening-range high", "A rising 50-day average on the day of the breakout", "A close back above the 20-day average after a touch"], "correct": 2, "explain": "Triggers are the events that tell you to act. Confirmations are conditions that must already be true for a trigger to count. A rising 50-day average is a condition, not an event."}
  ],
  "task": "From your ranked list, find one stock whose most recent close exceeded its prior 20-day high while the 50-day average was rising, and write down the level, the close, the volume and the 50-day average on that day."
}
---

A ranking tells you what to buy. A trigger tells you when. Most losses in swing trading that are blamed on "picking the wrong stock" are really a strong stock bought at the wrong moment: at the top of a spike, in the middle of a pullback, or on an intraday poke through a level that reversed by the close. This lesson gives you three triggers, the confirmations that must be true before any of them counts, and a real breakout worked bar by bar.

## The job of a trigger

A trigger is an event on the chart that converts a candidate into a position. It has three properties. It is defined before it happens, so you know the price and the day you are waiting for. It is observable from a bar you can see, so you never argue with yourself about whether it fired. And it implies a level whose violation proves the idea wrong, because that level is where the stop goes in the next lesson.

If you cannot state the trigger as a sentence with a number in it, you do not have one. "It looks ready" is not a trigger. "A daily close above 147.96" is.

## Trigger one: the breakout

The breakout trigger is a close above the highest high of the prior N sessions. Twenty sessions is the default in this course, roughly a month of trading. The academic cousin is the 52-week high: George and Hwang (2004) showed that a stock's distance from its 52-week high predicts future returns about as well as past-return momentum does, which is a formal way of saying that buying near new highs is not the mistake it feels like.

The reason a breakout works when it works is that a range represents a period of agreement about value. A close outside the range on volume means the agreement broke. Whoever sold inside the range is now wrong, and short sellers above it are being squeezed. None of that guarantees follow-through; it means the odds of follow-through are better than they are at a random moment.

The confirmations for a breakout are:

- **Trend.** The 50-day simple moving average is above its value ten sessions earlier. You are buying a pause inside an uptrend, not the first bounce off a low.
- **Participation.** Volume on the breakout day exceeds the typical volume of the prior sessions. The exact multiple matters less than the direction; a breakout on the lowest volume of the month is a warning.
- **No gap.** The open on the breakout day is within about 2% of the prior close. A larger gap usually means news, which lesson 11 treats separately, and it makes the stop distance awkward.
- **Ranking.** The stock is in the top half of your relative-strength list. A breakout in a bottom-ranked name is a different, weaker setup.

## Trigger two: the pullback to a rising average

Strong stocks do not go up in straight lines; they run, rest, and run again. The pullback trigger buys the rest. The rule is: the stock is above a rising 20-day average, it trades down to touch that average, and then it closes back above it. The touch is the setup; the close back above is the trigger.

Brock, Lakonishok and LeBaron (1992) tested simple moving-average rules on the Dow back to 1897 and found the buy signals were followed by higher average returns than the sell signals, which was surprising at the time and has since been argued over at length. You do not need the average to have magical properties. You need a repeatable place where buyers who missed the breakout tend to reappear, and a moving average is a reasonable proxy for that.

The pullback trigger's virtue is proximity: you buy close to the level that proves you wrong, so the stop is tight and the position can be larger for the same dollar risk. Its vice is that a pullback sometimes continues into a reversal, and the tight stop means you find out quickly. Both are acceptable. What is not acceptable is buying the touch without the close back above, because that is buying a falling price and calling it a plan.

## Trigger three: the opening range as an intraday trigger for a daily setup

You can use a daily setup and an intraday trigger. The opening range is the high and low of the first 15 or 30 minutes of the session. When a stock on your list has a daily breakout level nearby, a trade through the opening-range high is an earlier entry than waiting for the daily close, with the opening-range low as a natural stop. Zarattini, Barbon and Aziz (2023) documented an opening-range breakout on a leveraged index fund with a stop at the range's opposite side, and their work is a useful description of the mechanics even though their instrument and holding period differ from a stock swing.

The price of entering early is that you act before the day's verdict is in. The worked example shows exactly that.

## Worked example

All figures come from Yahoo Finance's chart API, pulled 2026-09-24: daily bars from `https://query1.finance.yahoo.com/v8/finance/chart/NVDA?range=2y&interval=1d` and 5-minute bars for TSLA on 2026-09-03 from the same endpoint with `interval=5m`. One note on the intraday feed: Yahoo appends a 16:00 stub bar whose close does not match the session close; the 15:55 bar does, so the stub is discarded.

**Breakout: NVDA, 2025-06-25.** The prior 20 sessions (2025-05-27 to 2025-06-24) had a highest high of 147.96, set on 2025-06-24. The lowest low of the last 15 of those sessions was 137.95 on 2025-06-03, so the consolidation spanned 147.96 − 137.95 = 10.01 points. The 14-day ATR was 4.02, so the range was 10.01 / 4.02 = 2.5 ATRs tall: tight for a stock that had gained 40% in two months.

On 2025-06-25 NVDA opened at 149.27, traded to 154.45 and closed at **154.31**. Checks:

- Close 154.31 above the 20-day high 147.96: trigger fired.
- 50-day average 127.76, versus 119.71 ten sessions earlier: rising.
- Volume 269.1 million shares, against 187.6 million the day before and 139 to 243 million over the prior two weeks: higher.
- Open 149.27 against the prior close 147.90: a gap of +0.9%, under the 2% limit.

One honesty note before the entry. A strictly mechanical version of the rule had already fired one day earlier: on 2025-06-24 NVDA closed at 147.90 against a prior 20-day high of 146.20 (the 2025-06-20 high), a margin of 1.2%, and a system would have bought the 2025-06-25 open at 149.27. The 2025-06-25 bar is the second, decisive breakout close, and it is the one a trader looking at the chart would call the breakout. Both are valid under the rule as written; the mechanical one got the better price, which is a recurring pattern and a point in favour of letting the rule, not the eye, decide.

For the rest of this lesson and the next, the trade is taken from the decisive bar. The entry is the next open, 2025-06-26, at **155.98**, which is 1.1% above the trigger close. That slippage is the cost of waiting for the close; a trader who bought the last minutes of the breakout session would have paid closer to 154.31. Lesson 6 places the stop and lesson 8 follows the exit, which came on 2025-08-20 at 175.17.

**Pullback: NVDA, 2025-08-19.** After the breakout the stock never closed below its 20-day average until 2025-08-19, when it closed at 175.64 against an average of 178.46, having traded as low as 175.49. That is the touch. The trigger, a close back above the average, had not fired by 2025-08-20 (close 175.40 against an average of 178.69). A trader running only the pullback rule was still waiting; a trader in the breakout position was being told, by the same bar, that the exit rule in lesson 8 was close.

**Opening range: TSLA, 2026-09-03.** The prior close was 357.01 and the prior 20-day high 368.92. The stock opened at 365.82, a gap of +2.5%. The 30-minute opening range, 9:30 to 9:59, was **365.91 to 378.23**. The first 5-minute bar to trade above 378.23 was 10:20, with a high of 379.49, so the intraday trigger fired at about 378.3. The session then closed at **376.37**: above the daily breakout level of 368.92, but below the intraday trigger. On 2026-09-04 TSLA traded down to 351.32 and closed at 354.08, through the opening-range low and through the 20-day high. The intraday trigger fired, the daily trigger fired, and both failed within one session. That is not a reason to abandon the triggers. It is the reason lesson 6 exists.

## Chart

![NVDA daily candles, 2025-05-27 to 2025-07-18, with the 50-day average. The 2025-06-25 close of 154.31 cleared the prior 20-day high of 147.96; entry was the next open at 155.98 and the stop at 147.94 is drawn as the flat line. Source: Yahoo Finance daily bars.](figures/nvda-breakout-2025-06.svg)

## Choosing between the three

Use the breakout when the stock has been consolidating and the range is tight relative to its ATR: the NVDA example, at 2.5 ATRs, is the shape you want. Use the pullback when the stock has already broken out, you missed it, and it has come back to a rising average without violating the breakout level. Use the opening-range trigger only when you can watch the first half hour and you accept that the day's verdict is not yet in.

Whichever you use, write the trigger down the night before with its number. A trigger you compute after the bar has printed is a rationalisation.

## Sources

- George, T. J. and Hwang, C.-Y. (2004). The 52-week high and momentum investing. *Journal of Finance*, 59(5), 2145–2176. https://doi.org/10.1111/j.1540-6261.2004.00695.x
- Brock, W., Lakonishok, J. and LeBaron, B. (1992). Simple technical trading rules and the stochastic properties of stock returns. *Journal of Finance*, 47(5), 1731–1764. https://doi.org/10.1111/j.1540-6261.1992.tb04681.x
- Zarattini, C., Barbon, A. and Aziz, A. (2023). Can day trading really be profitable? SSRN Working Paper 4416622. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622
- Yahoo Finance historical data, NVDA: https://finance.yahoo.com/quote/NVDA/history/

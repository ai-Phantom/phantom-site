---
{
  "title": "Exits: Trailing Stops, Time Stops and Targets",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The trailing exit used in this course is:", "opts": ["Sell when the stock is up 10%", "Sell at the next open after a close below the lowest low of the prior 10 sessions", "Sell after exactly 20 days", "Sell when the RSI exceeds 70"], "correct": 1, "explain": "The 10-day-low trail ratchets up as the stock makes new highs and only triggers on a close beneath the recent structure. It never tightens on a good day and never loosens."},
    {"q": "On the NVDA trade entered at 155.98 with 8.04 of risk, the 10-day-low trail exited at 175.17 for +2.39R, a fixed 2R target exited at 172.06 for +2.00R, and a 20-day time stop exited at 173.50 for +2.18R. What does this comparison show?", "opts": ["The target is always best", "On a trade that worked, the three exits landed within 0.4R of each other; the choice of exit mattered far less than the fact that the entry was right", "The time stop is broken", "Trailing stops lose money"], "correct": 1, "explain": "The entry put the trade in a position to win; the exits divided a win that already existed. The system-level table shows the same thing across 100 trades."},
    {"q": "Applied to random entries on the same 20 stocks over the same period, the trailing exit produced +0.16R per trade, the 2R target +0.15R and the 20-day time stop +0.03R. The breakout entry with the trailing exit produced +0.30R. The lesson's conclusion is:", "opts": ["Exits are irrelevant", "Exits moved random entries by about 0.13R at most, while the entry rule added about 0.14R on top of the best exit; exits shape a result but cannot create one", "Random entries are better than the rule", "The time stop should be used with random entries"], "correct": 1, "explain": "The random-entry result is positive only because the sample was a rising tape. The gap between random and rule-based entries is the entry's contribution, and no exit closed it."},
    {"q": "Odean's 1998 study of retail brokerage accounts found that investors:", "opts": ["Sold losers too quickly", "Were more likely to sell winners than losers, holding losing positions longer, and the losers they held went on to underperform the winners they sold", "Never used stop orders", "Traded only at month end"], "correct": 1, "explain": "The disposition effect is the behavioural reason exits need to be rules. Left to preference, people cut the trades that would have paid and keep the ones that will not."},
    {"q": "Why does the course's trailing rule exit at the next open rather than at the close that triggered it?", "opts": ["Opens are always higher", "Because the rule is evaluated on the close, the earliest a trader acting on it can actually sell is the next session, and the backtest must not assume a fill that was not available", "To collect an extra day of dividends", "Because stop orders only work at the open"], "correct": 1, "explain": "Assuming a fill at the triggering close is look-ahead. It flatters a backtest by exactly the amount of the overnight move, on every trade."}
  ],
  "task": "Take the last five trades you have made or paper-traded, and for each write down what the 10-day-low trail, a 2R target and a 20-day time stop would have done, using the actual bars."
}
---

An exit is a rule that turns an open position into a number. Most traders spend their attention on entries and improvise exits, which is backwards in one sense and correct in another. Backwards, because a position with no exit rule is not a trade, it is an opinion with a ticker on it. Correct, because as this lesson shows with data, the exit decides how a good entry pays but cannot rescue a bad one.

## Four kinds of exit

**The initial stop** is the exit for being wrong. Lesson 6 placed it. It does not move against you, ever.

**The trailing stop** is the exit for being right and then less right. The version used in this course is the 10-day low: once in a trade, if a close falls below the lowest low of the prior ten sessions, sell at the next open. As the stock rises the 10-day low rises with it, so the stop ratchets up and never down. It never tightens on a good day, which means it gives back part of every winner; that is the price of never being taken out of a trend by a one-day dip.

**The time stop** is the exit for nothing happening. If a breakout has not made progress after N sessions, the reason for the trade has weakened even if the stop has not been hit. Twenty sessions is the version tested below.

**The target** is the exit for reaching a predefined multiple of the initial risk. A 2R target on a trade with 8.04 of risk is a limit order 16.08 above the entry. Targets cap winners, which is why momentum traders distrust them, and they raise the win rate, which is why everyone else likes them.

The temptation is to combine all four and tune the parameters. Resist it until you have seen the numbers, because they say something specific about which choices matter.

## Why exits have to be rules

Terrance Odean (1998) examined ten thousand retail accounts and found that investors sold winning positions far more readily than losing ones, and that the losers they kept went on to underperform the winners they sold over the following year. This is the disposition effect and it is the exact opposite of what a momentum trade needs. Left to instinct, you will take the 1R gain in a stock that goes on to 4R and sit through the −1R stop until it is −3R. The rule exists to overrule you.

## Worked example

Two levels: one trade, then a hundred.

**One trade.** The NVDA breakout from lessons 5 and 6: entry 2025-06-26 at 155.98, stop 147.94, risk 8.04 per share. Data from Yahoo Finance daily bars, pulled 2026-09-24.

- *10-day-low trail.* On 2025-08-19 NVDA closed at 175.64, below the 10-day low of 175.90. Exit at the 2025-08-20 open, **175.17**. Gain 19.19, R = 19.19 / 8.04 = **+2.39R**. 38 sessions held.
- *2R target.* 155.98 + 2 × 8.04 = 172.06. The 2025-07-15 high was 172.40, so the limit filled at **172.06**: **+2.00R**. 13 sessions.
- *3R target.* 155.98 + 24.12 = 180.10. Filled 2025-07-31 (high 183.30): **+3.00R**. 25 sessions.
- *20-day time stop.* The twentieth session after entry was 2025-07-25, close **173.50**. R = (173.50 − 155.98) / 8.04 = **+2.18R**.

Four exits, results between +2.00R and +3.00R. The entry did the work; the exits divided it up. Now the harder question: was the entry the thing that did the work, or would any entry have looked this good in that tape?

**A hundred trades.** Lesson 12 describes the system in full. Briefly: twenty stocks, December 2024 to August 2026, enter at the next open after a close above the prior 20-day high with the 50-day average rising and the stock in the top half of the 6-month relative-strength rank; stop 2 ATRs below entry; trailing exit at the 10-day low; costs of 0.10% per side. That baseline is the first row. Each subsequent row changes one thing. The last three rows replace the entry rule with a coin flip: on each day, each stock has a 3% chance of being bought, with no ranking, and the same stops and exits are applied.

| Variant | Trades | Win rate | Avg win | Avg loss | Expectancy (R) |
|---|---|---|---|---|---|
| Baseline: breakout entry, 10-day-low trail | 100 | 44.0% | +1.95R | −1.00R | **+0.30** |
| Same entry, 2R target instead of trail | 138 | 41.3% | +1.57R | −0.94R | +0.10 |
| Same entry, 20-day time stop added | 137 | 40.9% | +1.80R | −1.01R | +0.14 |
| Same entry, stop at 3 ATRs | 94 | 47.9% | +1.34R | −0.75R | +0.25 |
| Random entry, 10-day-low trail | 168 | 33.9% | +2.02R | −0.80R | +0.16 |
| Random entry, 2R target | 190 | 37.4% | +1.66R | −0.75R | +0.15 |
| Random entry, 20-day time stop | 187 | 39.0% | +1.37R | −0.83R | +0.03 |

Expectancy is the average R per trade: win rate × average win + loss rate × average loss. For the baseline, 0.44 × 1.95 + 0.56 × (−1.00) = 0.858 − 0.560 = +0.30R, which matches the table.

Read it in two directions. Down the first four rows, the entry is held fixed and the exit changes: expectancy moves from +0.30 to +0.10. The trail beat the target by 0.20R per trade because the target capped the handful of trades that made the whole result; the top ten trades in the baseline contributed 44.4R of the 29.8R total, meaning the other ninety trades were net negative and the tail paid for everything. A 2R cap cannot collect a tail. Across the bottom three rows, the entry is a coin flip and the exit changes: expectancy moves from +0.16 to +0.03. The exits mattered there too.

Now compare across. Random entries with the best exit: +0.16R. The breakout entry with the same exit: +0.30R. The entry rule was worth 0.14R per trade, and no exit applied to random entries got within 0.14R of the baseline. That is the sense in which exits cannot fix a bad entry: they can only reshape what the entry delivered, and the reshaping range, here about 0.13R, was smaller than the entry's contribution.

One honesty note. Random long entries made money in this sample under two of three exits. That is not a property of the exits; it is a property of the period, during which the index rose. A trailing stop on random entries in a falling tape would have shown a negative number, and the entry rule's contribution would have been the difference between two losses rather than two gains. The regime lesson deals with that.

## Choosing the exit for a momentum system

The data favour the trail, and the reason generalises: momentum returns are skewed. A few trades run for months and the rest are small losses or small wins. Any exit that caps the long trades, a target or a short time stop, cuts off the skew that pays. A trailing stop that only tightens with new highs keeps you in the tail.

The 3-ATR stop is the interesting variant. It raised the win rate from 44% to 48% and cut the average loss from 1.00R to 0.75R, because fewer trades were stopped by noise and, with the wider stop, the R-unit is larger so each stop-out is a smaller multiple. Its expectancy was slightly lower, +0.25 versus +0.30, on fewer trades. That is a real trade-off, not a free lunch, and it is the kind of choice to make on temperament: a trader who cannot sit through a 44% win rate may do better with 48% and slightly less per trade than with a system they abandon.

Do not add a target to collect "guaranteed" profit. If you need the win rate, widen the stop.

## Running the exit

Evaluate the trail after every close. If it has triggered, sell at the next open; do not wait to see if the stock bounces. Keep the initial stop on the broker's server and replace it with the trailed level whenever the 10-day low rises above it, so that the exit executes without you. And record the exit reason on every trade, stop, trail, or time, because in lesson 12 the breakdown by reason is how you find out which part of the system is carrying it.

## Sources

- Odean, T. (1998). Are investors reluctant to realize their losses? *Journal of Finance*, 53(5), 1775–1798. https://doi.org/10.1111/0022-1082.00072
- Kaminski, K. M. and Lo, A. W. (2014). When do stop-loss rules stop losses? *Journal of Financial Markets*, 18, 234–254. https://doi.org/10.1016/j.finmar.2013.07.001
- U.S. Securities and Exchange Commission, Investor.gov glossary: Stop order. https://www.investor.gov/introduction-investing/investing-basics/glossary/stop-order
- Yahoo Finance historical data, NVDA: https://finance.yahoo.com/quote/NVDA/history/

---
{
  "title": "What a System Is, and What It Is Not",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Which of these is a system in the sense this course uses?", "opts": ["Buy SPY when it looks oversold and the news is bad", "Buy SPY at the next open when the close is at least 2% below its 5-day high; sell at the next open after the close exceeds the 5-day SMA", "Buy strong stocks on pullbacks, size by conviction", "Trade the plan, but skip days when the tape feels wrong"], "correct": 1, "explain": "Only the second one names the data, the threshold, the execution bar and the exit. Every other option contains a word (oversold, bad, strong, feels) that two people would code differently."},
    {"q": "The main thing systematising buys you is:", "opts": ["Higher returns", "A measurable record where every decision is reproducible", "Freedom from drawdowns", "The ability to trade more markets"], "correct": 1, "explain": "A system's return can be lower than a good discretionary trader's. What it guarantees is that every decision came from a written rule, so the record can be tested, attributed and audited."},
    {"q": "The main cost of systematising is:", "opts": ["Rigidity: the rule keeps trading its pattern after the world changes", "You need a computer", "Lower win rate", "Regulators require more paperwork"], "correct": 0, "explain": "A rule cannot notice that its premise has stopped holding. That is why the course spends later lessons on out-of-sample tests, walk-forward and kill switches."},
    {"q": "In 2024, SPY closed at least 2% below its 5-day high on 24 of 252 sessions. The mean 5-day forward return after those days was +1.43% against +0.49% for all days. What does this establish?", "opts": ["A tradeable edge", "A measured fact about one year that a hypothesis can now be built on", "That dips always recover", "Nothing, because 24 is too few observations to compute a mean"], "correct": 1, "explain": "A difference of means in one year with 24 observations is a fact, not an edge. It has no costs, no execution convention, no out-of-sample check and no significance test. Lesson 3 shows what has to happen next."},
    {"q": "A discretionary trader and a systematic trader both lose 8% in a month. Which statement is true?", "opts": ["The systematic trader can attribute the loss to specific rule firings and re-run the month with any rule change", "The discretionary trader has the better record because they can explain the loss", "Both records are equally testable", "Neither can learn from the month"], "correct": 0, "explain": "The systematic record is a set of signals and fills produced by code. It can be replayed under any alternative rule. The discretionary record is a set of decisions that cannot be re-generated."}
  ],
  "task": "Write one rule you currently trade in a single sentence that names the data, the threshold, the execution bar and the exit; if you cannot, write down which word stops you."
}
---

## The one-sentence test

A trading system is a rule that a computer can run without you in the room. That is the whole definition, and it is stricter than it sounds. The test is whether two people given the same sentence and the same data would produce the same list of trades. If any word in your rule needs judgement to apply (oversold, strong, extended, confirmed, quality), the sentence fails and what you have is a style, not a system.

Take "buy SPY on a dip". A dip relative to what? Measured on which bar? How far? For how long do you hold? Now take this: "At the close of each session, if SPY's close is at least 2% below the highest close of the last five sessions, buy at the next session's open; sell at the next open after the first close above the 5-day simple moving average." That sentence names the data (daily closes and opens), the threshold (2%, five sessions), the execution bar (the next open) and the exit (close above the 5-day SMA). It is a system. You may think it is a bad one, and you may be right, but it can be tested, which is what this course is about.

Notice what the sentence does not contain: any reference to why the rule should work, any claim about its returns, any adjective. Those belong in the hypothesis (lesson 3) and in the test results (lessons 4 through 9), not in the rule.

## Discretionary versus systematic

The distinction is not "human versus machine". Many discretionary traders use screens, indicators and code. Many systematic traders override their models. The distinction is where the decision lives. In a discretionary process the decision is made by a person at the moment of the trade, informed by whatever they are looking at. In a systematic process the decision was made once, in advance, when the rule was written, and every trade after that is the rule being applied.

That difference has three consequences you should feel before you commit to either side.

First, a systematic record is reproducible. Every trade in it came from a rule applied to data, so you can regenerate the record from scratch, and you can regenerate it under a different rule to see what would have changed. A discretionary record is a list of decisions that happened. You can study it, but you cannot re-run it.

Second, a systematic process is consistent by construction. It fires on the 200th signal exactly as it fired on the first, after a losing streak as after a winning one, at 3:59 pm on a Friday in a drawdown as on a quiet Tuesday. Consistency is not a virtue in itself; a consistently bad rule is still bad. But consistency is what makes measurement mean anything. If the process changes with your mood, a statistic over 100 trades describes 100 slightly different processes.

Third, a systematic process is rigid. It cannot notice that its premise has stopped holding. A trend rule keeps buying breakouts in a market that has started to chop; a mean-reversion rule keeps buying dips in a market that has started to fall through them. The rule has no way to know. A discretionary trader can (in principle) notice. In practice the evidence that they do notice, reliably and ahead of the damage, is thin, but the possibility is real and it is the honest argument for discretion.

## What you are buying and what it costs

You systematise to get measurability and consistency. Measurability means you can put a number on the rule's expectancy, its drawdown, its tail, its correlation to what you already run, and you can put error bars on those numbers. Consistency means the number you measured is the number you will get, up to sampling error and the cost of execution, because the thing that produced the measurement is the same thing that will trade.

You pay for it with rigidity, and you pay in two other ways people underestimate. You pay in research time: the rule has to be specified to the level a computer can run, which surfaces every ambiguity you were glossing over. And you pay in temptation: once the rule is code, changing a parameter costs nothing, and every change you make after seeing the results is a step toward fitting the past. Lessons 7 and 8 are about that temptation.

None of this makes systematic trading superior. A rule is a bet that a written pattern will keep paying. A discretionary trader is a bet that a person will keep reading the market well. Both bets can lose. The reason this course is about the first kind is that the first kind can be tested before money is at risk, and the second kind cannot.

## What a system is not

A system is not an indicator. RSI, moving averages and Bollinger Bands are transformations of price; they become a system only when paired with a threshold, an execution convention and an exit. A system is not a backtest result; the result is evidence about a system, and lessons 6 and 7 are about how that evidence gets corrupted. A system is not a piece of software; the software is a container. And a system is not automatic profit. Most rules that get written do not survive the tests in this course, and the course reports that honestly for its own running example.

A system is also not necessarily complicated. The running example in this course is two lines of logic on one ticker. Its simplicity is the point: a rule you can state in a sentence is a rule you can test, attribute and, when it fails, retire without arguing with yourself.

## Worked example

Here is the smallest possible measurement, done properly, so you see what "measurable" means before any strategy is on the table. The data is SPY daily bars from the Yahoo Finance chart API, requested with explicit Unix timestamps (`period1=1420070400`, 2015-01-01; `period2=1767139200`, 2025-12-31; `interval=1d`), which returned 2,765 rows from 2015-01-02 to 2025-12-30 with no missing values. Closes are dividend-adjusted using the ratio of Yahoo's adjusted close to its close (lesson 2 covers why).

The question: in 2024, how often did SPY close at least 2% below its 5-day high, and what happened over the next five sessions?

```python
import pandas as pd
px = pd.read_csv("spy_daily.csv", parse_dates=["date"], index_col="date")
close = px["adj_close"]
high5 = close.rolling(5).max()
dip = (close / high5 - 1) <= -0.02          # today's close 2%+ under the 5-day high
fwd5 = close.shift(-5) / close - 1          # return over the next five sessions
y = "2024"
print(dip.loc[y].sum(), len(dip.loc[y]))    # 24 252
print(fwd5.loc[y][dip.loc[y]].mean())      # 0.01433
print(fwd5.loc[y].mean())                   # 0.00491
```

The rule flagged 24 of the 252 sessions of 2024. The mean 5-day forward return after a flagged session was +1.433%. The mean 5-day forward return over every session in 2024 was +0.491%. The difference is +0.942 percentage points per event.

Now be precise about what that is. It is a fact: two averages over one year, computed by code you can re-run. It is not an edge. It has no execution convention (`fwd5` measures close-to-close, and you cannot trade at the close you just observed; lesson 4 fixes this), no costs (lesson 5), no significance test (24 observations from overlapping windows; lesson 3), and no out-of-sample check (lesson 8). The average is also carried by a few events: the 24 flagged sessions fall in runs (four in mid-April, four in late July, four in early August, four in early September, and the rest spread over late October to December), so they are roughly eight independent episodes, not 24.

What the measurement does give you is a starting point that a discretionary "buy the dip" never could: a number, a date range, a definition, and a piece of code that anyone can run to get the same 24 and the same +1.433%.

## Table

How the two approaches differ on the properties this course tests.

| Property | Discretionary | Systematic |
|---|---|---|
| Where the decision is made | At the moment of the trade | Once, when the rule is written |
| Can the record be regenerated? | No | Yes, from data plus rule |
| Can an alternative rule be replayed on the same history? | No | Yes |
| Consistency across trades | Varies with state, mood, attention | Identical by construction |
| Response to a changed market | Possible, unreliable | None until a human intervenes |
| Cost of a parameter change | High (habit) | Near zero (and therefore dangerous) |
| Testable before capital is risked | Only by paper-trading the person | Yes, with the caveats of lessons 6 and 7 |
| Failure mode | Inconsistency, hindsight narrative | Overfitting, rigidity, silent data faults |

## Where this course goes

Lesson 2 is about data, because every number in this course is only as good as the bars underneath it, and the bars have traps. Lesson 3 is the research loop: hypothesis, rule, test, decide, in that order, and why reversing the order is how most backtests go wrong. Lesson 4 writes the first backtest in pandas with next-bar execution. Lessons 5 through 9 are the ways a backtest lies to you (costs, leakage, overfitting, bad splits, misleading metrics) and the test for each. Lessons 10 and 11 move from a single rule to a book and from a backtest to a live paper record. Lesson 12 assembles everything into a written gate stack with thresholds. The capstone runs one rule, RSI(2) below 10 on SPY with an exit above the 5-day SMA, through the whole stack and asks you to write the verdict.

The running example does not pass every gate. You will see exactly where it fails and why, because a course that only showed you a winner would be teaching you the wrong thing.

## Sources

- Yahoo Finance, SPY historical data page: https://finance.yahoo.com/quote/SPY/history/
- pandas documentation, `Series.rolling` and window operations: https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html
- Bailey, D. H., Borwein, J., López de Prado, M., Zhu, Q. J. (2014). "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance." Notices of the AMS 61(5). https://doi.org/10.1090/noti1105

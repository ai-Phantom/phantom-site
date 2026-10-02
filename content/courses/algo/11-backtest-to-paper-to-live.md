---
{
  "title": "From Backtest to Paper to Live: Reconciliation, Fill Gaps and Kill Switches",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The paper book's signal series must match the backtest's signal-for-signal on every session. Why is matching the trade count or the monthly return not enough?", "opts": ["Because counts are hard to compute", "Because monthly returns include dividends", "Because two signal series can have the same count and similar returns while firing on different days; only a row-by-row comparison shows the live code is running the tested rule", "Because brokers report counts differently"], "correct": 2, "explain": "A live feed with a different adjustment, a different close time or a stale bar can produce a rule that looks like the backtest in aggregate and is a different rule in detail. The comparison is per session, per signal."},
    {"q": "On the 110 entry days, SPY moved on average -0.087% from the open to the close, with a standard deviation of 1.04%. What does that say about the cost of a one-session delay in placing the entry?", "opts": ["A delay is free", "A delay averages about 9 bps of slippage on this rule but with a spread of 1% either way; the average is small, the variance is what a live book will notice", "Delays always help mean-reversion rules", "The standard deviation is the cost"], "correct": 1, "explain": "The mean is inside the modelled 5 bps cost, so on average the delay is not ruinous; but a 1% daily dispersion means single fills will differ from the model by far more than any cost assumption, which is why fills are reconciled individually."},
    {"q": "Executing the rule one session late (position from the signal's second open instead of its first) raised the ten-year Sharpe from 0.27 to 0.48. This is:", "opts": ["A warning: the rule's edge does not depend on the timing the hypothesis claimed, so the thing being traded is not the thing that was tested", "Good news; trade it late", "Proof of a stronger edge", "An artefact of costs"], "correct": 0, "explain": "If the signal's timing carried information, delaying it should cost return. It gained. The mean reversion the rule captures happens over days two to six, which the hypothesis did not say, and a rule that works better when mis-executed is a rule whose mechanism is not understood."},
    {"q": "A kill switch set at a 20-session return of -10% would have tripped three times in 2016-2025, all between 2020-02-27 and 2020-04-07. After the first trip the next 20 sessions returned -7.4%. This shows:", "opts": ["Kill switches cost return", "The switch is set from the backtest's own tail, it fires only in the one episode the backtest already identified as the rule's failure mode, and on this history it would have avoided part of the loss; whether it helps in the next crash is not knowable from this one", "Kill switches should be set at -1%", "The switch would have fired 20 times"], "correct": 1, "explain": "One episode is one observation. The switch's job is to bound the loss when the rule's premise fails; that it would have helped in March 2020 is consistent with its design and proves nothing about the next event."},
    {"q": "The paper book earns nothing. Its purpose is:", "opts": ["To practise placing orders", "To satisfy the broker", "To calibrate position size", "To generate the only replication on data that did not exist when the rule was written, and to measure the fill gap between the model and the broker"], "correct": 3, "explain": "Every earlier gate ran on history the researcher could see. Sixty sessions of forward record on a frozen rule is the first evidence that could not have been fitted, and it comes with measured fills to compare against modelled ones."}
  ],
  "task": "Freeze your rule's code and parameters with a dated hash, and start a paper log with one row per session: signal, modelled fill, actual fill, cost, equity."
}
---

## Three books

A rule lives in three books, and the transitions between them are where most of the remaining risk hides. The backtest book is the daily return series you have been computing since lesson 4. The paper book is the same rule, frozen, run forward on live data with orders logged but not sent, or sent to a paper account. The live book is money. Each book should be reconcilable to the one before it, session by session, and the moment they cannot be reconciled is the moment to stop.

This lesson is about the two transitions: what the paper book has to record, how the modelled fill differs from the measured one, and the kill switch that has to exist before the live book opens.

## Freeze, then record

The paper book starts with a freeze. The rule's code, parameters, data source, adjustment method and execution convention are fixed, hashed and dated. From that date, every session produces one row: the bar the rule read, the signal it produced, the position it wants, the modelled fill (the next open, in this course), the fill it got (from the paper account, or the actual opening print if orders are only logged), the cost, and the equity. Nothing about the rule changes while the book runs. If something must change, the book restarts from a new freeze date.

The paper book's first job is not to earn; it is to prove the live code runs the tested rule. That is checked by comparing the signal series the live code produced with the signal series the backtest produces on the same sessions, row by row. Any session where they differ is a defect, whether in the live feed (a stale bar, an unadjusted price, a close captured before the auction), in the code, or in the environment. Aggregate matches are not enough: a live rule can fire the same number of times as the backtest in a month, on different days, for different reasons.

Sixty sessions is the minimum this course requires. It is about three months, enough for the running example to fire roughly three times and for every part of the pipeline (fetch, signal, order, fill, reconciliation) to run on a holiday week, an ex-dividend date and at least one large-move day.

## Modelled fills against measured fills

The backtest fills at the next open. The paper book records what the open actually was and, if orders were sent, what the fill actually was. The difference has three components, and each is measured, not assumed.

The auction gap. A market-on-open order fills at the opening auction print, which is the open in the bar. A limit order may not. The gap between the auction print and the bar's open is normally zero for SPY; it is not zero for a thin stock whose bar open is a single early trade.

Latency. If the order goes in late, the fill is not the open. The worked example measures what a full session of latency would have done to this rule.

Cost. The modelled 5 bps per side is compared against the measured cost: the difference between the fill and the mid-quote at the time, plus fees. For SPY it will be far under 5 bps; the measurement exists so that when the same pipeline trades something else, the number is known rather than assumed.

The reconciliation is a table with one row per fill: date, side, modelled price, measured price, gap in bps, explanation. Every row with a gap over the modelled cost needs an explanation. Rows that cannot be explained fail the paper gate.

## The kill switch

A kill switch is a rule that stops the rule. It is defined from the backtest's own tail before the paper book starts, and it is not a stop-loss on a trade; it is a stop on the strategy. The trigger is a measure of recent performance that, if breached, means the rule is doing something the backtest did not show, or is doing the one thing the backtest showed it does badly.

The threshold comes from the backtest's distribution of rolling returns. Set it inside the worst observed value, at a level that would have tripped only in the episodes the backtest identified as the failure mode. Set it too tight and it fires on noise; set it at the historical worst and it fires only after a loss as large as the worst one already seen, which is not protection.

When it trips, the rule goes flat and stays flat until a human has read the log, found the cause, and either re-frozen the rule or retired it. Automatic re-arming defeats the purpose.

## Worked example

The running example (RSI(2) below 10 on SPY, exit above SMA5, next-open, 5 bps per side, 2016-01-04 to 2025-12-30, adjusted bars from the Yahoo Finance chart API, 2,765 rows). Three measurements a paper book would make, computed here on history.

Latency. The modelled fill is the open. If the order were a full session late, the fill would be the next session's open, and the position would be one row further shifted. The cost of a same-session delay is approximated by the move from open to close on entry days:

```python
sig = rsi_signal(adj, 10, 5)
pos = sig.shift(1)
entries = (pos.diff() == 1).loc["2016":"2025"]
oc = (adj["close"] / adj["open"] - 1).loc["2016":"2025"][entries]
print(len(oc), oc.mean(), oc.median(), oc.std(), (oc > 0).mean())
# 110  -0.000873  0.000150  0.010421  0.518
```

Across the 110 entries, SPY moved -0.087% on average from the entry open to that day's close, median +0.015%, standard deviation 1.04%, positive on 51.8% of days. The worst was -3.51% on 2025-04-04. A delay of a session costs about 9 bps on average, which is under the modelled cost, but the dispersion is 1.04%: a single late fill will differ from the model by far more than any cost assumption. That is why fills are reconciled one at a time and not on average.

Now the full-session delay itself, run as a backtest: `pos = sig.shift(2)` instead of `shift(1)`, so the position starts at the second open after the signal.

```python
o2o = adj["open"].shift(-1) / adj["open"] - 1
late_pos = sig.shift(2).fillna(0)
late = (late_pos * o2o - late_pos.diff().abs().fillna(0) * 5 / 1e4).loc["2016":"2025"].dropna()
print(late.mean() / late.std() * 252 ** 0.5, (1 + late).prod() - 1)   # 0.48  +56.2%
```

The late rule scored a Sharpe of 0.48 and a total return of +56.2%, against 0.27 and +26.1% on time. That is not good news. A rule whose edge improves when it is executed a day late is a rule whose hypothesis (buy the close of the dip) was wrong about the timing: the mean reversion this rule captures is concentrated in days two to six after the signal, not day one. It also means the paper book's fill reconciliation cannot be judged by return, since a worse fill process produced a better return; it has to be judged by the gap in basis points, fill by fill.

Kill switch. The backtest's 20-session rolling return has 2,493 windows. The worst was -23.07%, ending 2020-03-20; the 1st percentile was -7.36%. A threshold of -10% sits between them.

```python
r = backtest(adj, sig, 5).loc["2016":"2025"]
roll20 = (1 + r).rolling(20).apply(np.prod, raw=True) - 1
hit = roll20 <= -0.10
print(hit.sum(), (hit & ~hit.shift(1, fill_value=False)).sum())   # 20 windows, 3 episodes
```

At -10% the switch would have tripped on 20 of 2,493 windows, in three episodes: 2020-02-27 (one session, -10.2%), 2020-03-11 to 2020-03-25 (minimum -23.1%) and 2020-03-27 to 2020-04-07 (minimum -13.6%). All three are the March 2020 failure lesson 9 traced trade by trade. After the first trip on 02-27 the rule's next 20 sessions returned -7.4% over 13 active days; a switch that went flat there would have avoided that. At -7.5% the switch trips in four episodes, at -5% in eleven, and the extra episodes are ordinary drawdowns the rule recovered from. The -10% level is the one this course would arm, with the note that it is calibrated on one crash and its behaviour in the next is unknown.

## Table

The paper book's row format and the reconciliation checks run on it, with the pass condition for each.

| Field or check | What is recorded | Pass condition for the G6 gate |
|---|---|---|
| Freeze record | Code hash, parameters, data source, adjustment method, execution convention, date | Unchanged for 60 sessions |
| Signal (live) vs signal (backtest re-run) | 0/1 per session, both sources | Identical on every session |
| Bar read by the live code | Open, high, low, close, adjusted factor, fetch timestamp | Fetch after the close; factor matches the stored one |
| Modelled fill | Next session's open from the bar | Present on every position change |
| Measured fill | Paper account fill, or opening auction print if orders were only logged | Within modelled cost (5 bps) of the modelled fill, or explained |
| Cost per side | Fill minus mid at the time, plus fees | Within 5 bps of the modelled cost on average |
| Equity | Cumulative, from measured fills | Tracks the backtest re-run on the same sessions within reconciled gaps |
| Kill switch | Threshold, rolling window, armed date, trip log | Defined and armed before session 1; if tripped, book stops until reviewed |
| Session count | Sessions completed since freeze | ≥ 60, including at least one ex-dividend date and one holiday week |

A paper book that passes every row is the first evidence about the rule that could not have been fitted. It is not proof of an edge; sixty sessions is three signals for this rule. It is proof that the pipeline trades the rule that was tested, with fills the model can account for, under a switch that will stop it. The live book opens on that evidence and nothing less.

## Sources

- Harvey, C. R., Liu, Y. (2015). "Backtesting." Journal of Portfolio Management 42(1). https://doi.org/10.3905/jpm.2015.42.1.013
- NYSE, opening and closing auctions (the print the modelled fill assumes): https://www.nyse.com/markets/nyse/trading-info
- 17 CFR 242.605, Disclosure of order execution information (how brokers report measured fills against the quote): https://www.ecfr.gov/current/title-17/section-242.605
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

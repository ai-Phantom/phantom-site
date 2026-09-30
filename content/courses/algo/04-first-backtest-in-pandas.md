---
{
  "title": "A First Backtest in pandas: Next-Bar Execution, No Look-Ahead",
  "duration": "20 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A signal is computed from Thursday's close. Under next-bar execution, which return does the position first earn?", "opts": ["Thursday's close-to-close return", "Friday's open to the following open", "Thursday's open to Thursday's close", "Friday's close to Monday's close"], "correct": 1, "explain": "You cannot act on a close until it has printed. The first fill you can get is Friday's open, and the first return you earn runs from that open to the next open, when you could next act."},
    {"q": "In the code, `pos = signal.shift(1)` does what?", "opts": ["Delays the signal by one row so today's position is yesterday's decision", "Advances the signal so it uses tomorrow's close", "Reverses the signal", "Removes the first row"], "correct": 0, "explain": "shift(1) moves each value one row later. The position on row t is the signal from row t-1, which is the only signal that was known when the position was opened."},
    {"q": "SPY closed at 270.51 on 2020-02-27, below its 200-day SMA of 274.97, so the signal turned off. The open-to-open return attributed to that row is -5.49%. Was the strategy exposed to it?", "opts": ["No, the signal was off", "Yes, because the position on 02-27 came from the 02-26 signal, which was on; the exit fills at the 02-28 open", "Only half", "It depends on the broker"], "correct": 1, "explain": "The row's return runs from the 02-27 open to the 02-28 open. The position during that stretch was set by the 02-26 close, when the signal was still on. The rule ate the whole drop, which is what a real trader following it would have done."},
    {"q": "The same trend rule scores a 0.93 Sharpe with next-open fills and 1.00 with fills at the signal bar's close. Why does the difference matter?", "opts": ["It does not; both are correct", "The close-fill number assumes you can trade a price you have not yet seen, unless you are placing MOC orders; the next-open number is the one a reader of the close can achieve", "Next-open fills always score higher", "The close-fill number includes dividends"], "correct": 1, "explain": "A close-to-close backtest with shift(1) assumes a fill at the close of the signal bar. That is achievable only with a market-on-close order placed before the close prints. Otherwise the honest convention is the next open."},
    {"q": "Over 2016-2025 the SMA200 rule returned 11.1% a year with a -19.8% max drawdown; SPY buy-and-hold returned 15.1% with -32.0%. What does this comparison NOT tell you?", "opts": ["That the rule was less exposed to the 2020 crash", "That the rule traded 26 times", "Whether the rule would beat buy-and-hold in the next decade", "That the rule's volatility was lower"], "correct": 2, "explain": "One ten-year sample with one crash in it is one observation of the rule's behaviour in a crash. It describes the past. Lessons 7 and 8 are about what it takes to say anything about the future."}
  ],
  "task": "Run the backtest in this lesson, then change the SMA length to 100 and 300 and record all three Sharpe ratios in your research log as three trials."
}
---

## The convention that makes a backtest honest

A backtest is a loop over bars that asks, at each one, what the rule would have done with the information available at that bar, and what the market then paid. The word that carries the weight is "then". A rule that computes a signal from today's close cannot have acted on it at today's close, because the close is the last print of the session. The earliest fill is tomorrow's open. Everything the rule earns is measured from that fill to the next point at which it could act again, which is the following open.

That is next-bar execution, and in pandas it is one call: `signal.shift(1)`. The position held on row t is the signal from row t-1. Every backtest in this course uses it. The alternative, letting the position on row t depend on the signal of row t, is the most common look-ahead there is; lesson 6 measures how much it inflates a result.

There is a second convention hiding inside the first: what return does the position earn on row t? With next-open fills the honest answer is the open-to-open return, `open[t+1] / open[t] - 1`, because the position was opened at `open[t]` and is next re-evaluated at `open[t+1]`. Many backtests use close-to-close returns with a one-row shift instead. That is the same as assuming a fill at the close of the signal bar, which is achievable with a market-on-close order for a liquid ETF but is not what "decide at the close, trade tomorrow" means. This lesson shows both and reports the gap.

## The rule

The first rule is a trend filter, chosen because it trades rarely and its logic is transparent: hold SPY when the adjusted close is above its 200-day simple moving average, hold cash otherwise. Signal at the close, fill at the next open, cash earns nothing (lesson 10 fixes that). The data is the adjusted SPY frame from lesson 2 (Yahoo Finance chart API, 2,765 rows, 2015-01-02 to 2025-12-30); 2015 is warm-up for the 200-day window and the test runs 2016-01-04 to 2025-12-30.

```python
import numpy as np, pandas as pd
adj = pd.read_csv("spy_adjusted.csv", parse_dates=["date"], index_col="date")

sma200 = adj["close"].rolling(200).mean()
signal = (adj["close"] > sma200).astype(int)          # known at the close of row t

o2o = adj["open"].shift(-1) / adj["open"] - 1        # return from open t to open t+1
pos = signal.shift(1).fillna(0)                        # position during row t = signal at t-1
strat = (pos * o2o).loc["2016-01-01":"2025-12-31"].dropna()
bh = o2o.loc["2016-01-01":"2025-12-31"].dropna()

def summary(r):
    eq = (1 + r).cumprod()
    return {"total": eq.iloc[-1] - 1,
            "cagr": eq.iloc[-1] ** (252 / len(r)) - 1,
            "vol": r.std() * np.sqrt(252),
            "sharpe": r.mean() / r.std() * np.sqrt(252),
            "max_dd": (eq / eq.cummax() - 1).min()}
print(summary(strat)); print(summary(bh))
```

Every line is doing one thing. `signal` is an integer series that is 1 when the rule wants to be long. `o2o` is the return of holding from one open to the next, so its row-t value is the return a position opened at row t's open earned. `pos` is the signal delayed one row. Their product is the strategy's daily return. The last row of `o2o` is `NaN` because there is no next open yet, and `dropna` removes it.

## What the numbers say

Over 2,512 sessions the trend rule turned $1 into $2.86 (+185.8%), a compound annual growth rate of 11.11%, with annualised volatility of 12.16%, a Sharpe ratio (daily mean over daily standard deviation, times the square root of 252, no risk-free subtraction; lesson 9 is about conventions) of 0.93, and a maximum drawdown of -19.85% reached on 2020-06-12. Buy-and-hold over the same 2,512 open-to-open returns turned $1 into $4.05 (+304.6%), a CAGR of 15.05%, volatility 17.26%, Sharpe 0.90, maximum drawdown -32.05% on 2020-03-20.

The rule was long 82.6% of the time. It traded 26 round trips, about 2.6 a year, with an average hold of 115 calendar days; 12 of the 26 (46.2%) were profitable, with an average winner of +12.83% and an average loser of -1.93%, for an expectancy of +4.88% per trade. The largest single-trade loss was -5.12% on a position opened at the 2018-12-03 open. The largest winner was +46.75%.

Read those numbers the way lesson 1 asked. The rule gave up four points of CAGR to cut the worst drawdown by twelve points and volatility by five. Its Sharpe is a hair above buy-and-hold's. That is one decade with one crash in it, and the rule's whole advantage is what it did in the first weeks of that crash, so it is one observation, not a distribution. Nothing here has been charged a cost, and nothing here says what a 100-day or 300-day SMA would have done; if you try those (the task asks you to), you have run three trials, and lesson 7 explains what that does to the meaning of the best one.

The same rule with close-to-close returns and the same `shift(1)`, which is a fill at the signal bar's close, scored a Sharpe of 1.00 and a CAGR of 11.82%. The seven basis points of Sharpe and seventy basis points of CAGR are the price of insisting on a fill you could actually get without an MOC order. It is small for a rule that trades 26 times; lesson 6 shows it is not small for a rule that trades 110 times.

## Worked example

The clearest way to see next-bar execution is to watch it across the week the signal flipped in early 2020. The table below is the frame the code builds, printed for 2020-02-24 to 2020-03-03, prices dividend-adjusted.

```python
frame = pd.DataFrame({"close": adj["close"], "sma200": sma200, "signal": signal,
                      "pos": signal.shift(1), "o2o": o2o})
print(frame.loc["2020-02-24":"2020-03-03"].round(4))
```

| Date | Adj close | SMA200 | Signal (at close) | Position (during row) | Open-to-next-open |
|---|---|---|---|---|---|
| 2020-02-24 | 293.16 | 274.61 | 1 | 1 | +0.25% |
| 2020-02-25 | 284.28 | 274.75 | 1 | 1 | -3.01% |
| 2020-02-26 | 283.23 | 274.87 | 1 | 1 | -2.78% |
| 2020-02-27 | 270.51 | 274.97 | 0 | 1 | -5.49% |
| 2020-02-28 | 269.38 | 275.04 | 0 | 0 | +3.29% |
| 2020-03-02 | 281.04 | 275.17 | 1 | 0 | +3.79% |
| 2020-03-03 | 273.00 | 275.25 | 0 | 1 | -1.09% |

Walk the rows. On 02-27 the close of 270.51 fell under the SMA of 274.97 and the signal turned off. But the position during 02-27 (from the 02-27 open to the 02-28 open) was set by the 02-26 signal, which was on, so the rule was exposed to the -5.49% open-to-open drop. It sold at the 02-28 open. During 02-28 it was flat and missed the +3.29% rebound into the 03-02 open. On 03-02 the close of 281.04 crossed back above and the signal turned on; the rule bought at the 03-03 open, was exposed to the -1.09% into 03-04, and the 03-03 close below the SMA turned it off again for a sale at the 03-04 open.

The rule's return over the seven rows is the product of (1 + pos × o2o): (1.0025)(0.9699)(0.9722)(0.9451)(1)(1)(0.9891) - 1 = -11.6%. Buy-and-hold over the same seven rows: (1.0025)(0.9699)(0.9722)(0.9451)(1.0329)(1.0379)(0.9891) - 1 = -5.3%. In this week the rule did worse than holding, because it sold after the drop and missed the bounce; its edge over the decade comes from the weeks after, when it stayed out through March. A backtest that let the position on 02-27 use the 02-27 signal would have sidestepped the -5.49% and shown the rule in a light no trader could have matched.

Do the arithmetic of the shift once by hand like this for every new rule. It takes five minutes and it is the cheapest look-ahead check there is.

## Table

The three execution conventions you will meet, what each assumes, and what the SMA200 rule scored under each over 2016-2025 (no costs).

| Convention | Position on row t | Return on row t | What it assumes | SMA200 Sharpe | SMA200 CAGR |
|---|---|---|---|---|---|
| Next open (this course) | `signal.shift(1)` | `open[t+1] / open[t] - 1` | Read the close, trade the next opening auction | 0.93 | 11.11% |
| Market-on-close | `signal.shift(1)` | `close[t] / close[t-1] - 1` | An MOC order placed before the close that fills at the close of the signal bar | 1.00 | 11.82% |
| Same-bar (look-ahead) | `signal` (no shift) | `close[t] / close[t-1] - 1` | You traded at yesterday's close on a signal you would only see at today's close | see lesson 6 | see lesson 6 |

The first two are legitimate and differ by what order type you actually use; state which one you used in every result. The third is a defect. Lesson 6 measures it on this rule and on the running example.

## Sources

- pandas documentation, `Series.shift`: https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html
- pandas documentation, `Series.rolling`: https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html
- NYSE, closing auction and MOC order rules: https://www.nyse.com/markets/nyse/trading-info
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

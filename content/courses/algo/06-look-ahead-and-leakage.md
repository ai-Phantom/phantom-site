---
{
  "title": "Look-Ahead and Leakage: Finding the Future in Your Backtest",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A rule buys SPY with a limit order 2% below yesterday's close and exits at the close. Filled at the limit price it earned +0.042% per fill; filled 'at the low' it earned +0.917% per fill. Where is the leak?", "opts": ["The limit price is wrong", "Filling at the low assumes you knew the day's minimum before the day ended; the low is only known at the close", "Exiting at the close is a leak", "There is no leak; both are valid"], "correct": 1, "explain": "Your order fills when price touches your limit, at your limit. The low of the day is whichever print was lowest, known only after the fact. Pricing the fill there is intrabar peeking, and it turns a 0.14 Sharpe into 2.69."},
    {"q": "The truncation-invariance test says:", "opts": ["A rule's signals up to date D must be identical whether it is run on data ending at D or on data ending later", "A rule must perform the same in every year", "A rule must be truncated to 100 trades", "Signals must not change when costs change"], "correct": 0, "explain": "If adding future rows changes past signals, something in the rule reads the future. A full-sample z-score rule changed 456 of 2,014 past signals when 2023-2025 was appended; the rolling version changed none."},
    {"q": "The SMA200 rule earned a 1.00 Sharpe with a one-row shift and 1.76 without it. The unshifted version:", "opts": ["Is the better strategy", "Uses the close of day t to hold a position through day t, which no trader could do", "Only differs by dividends", "Is what MOC orders achieve"], "correct": 1, "explain": "Without the shift, the position on the day the close crosses the SMA is already long for that day's move. The crossing day is by construction an up day, so the leak harvests it every time."},
    {"q": "Quarterly earnings dated 2024-12-31 were filed on 2025-02-14. A fundamental series indexed by fiscal period:", "opts": ["Is correct if you shift by one quarter", "Leaks about six weeks of the future on every row and must be indexed by the filing date", "Is only a problem for small caps", "Is fine because earnings are backward-looking"], "correct": 1, "explain": "The number was not knowable until it was filed. A rule that reads it on 2024-12-31 traded on information that arrived 45 days later."},
    {"q": "For the RSI(2) rule the same-bar defect produced a Sharpe of -2.44, worse than the honest 0.37. What does this show?", "opts": ["That the rule is robust to look-ahead", "That leakage always inflates results", "That leakage produces fiction in either direction; a mean-reversion entry that captures its own trigger day eats the drop that triggered it", "That RSI is a leading indicator"], "correct": 2, "explain": "The entry fires on a large down day. Without the shift the rule holds through that down day. The number is wrong, not merely optimistic. A leak is a defect whether it helps or hurts."}
  ],
  "task": "Run your lesson-4 backtest on data truncated at 2022-12-30 and on the full data, and assert that the signal series agree on every date up to the cut."
}
---

## What leakage is

Leakage is any path by which information from after a decision reaches the code that makes it. Look-ahead is the common case: the rule reads a price that had not printed yet. But leakage also enters through the data (a fundamental dated before it was public, a universe list built with survivors), through the fill model (a fill at a price you could not have known), and through the research process itself (a parameter chosen after seeing the result; lesson 7).

A leaked backtest is not optimistic. It is fiction. The number it reports describes a trader who knew something at the time that nobody knew, and there is no adjustment that recovers the honest number from it. The only remedy is to find the leak and re-run.

This lesson covers the four leaks that account for most of the fiction in retail backtests, shows the size of each on real SPY data, and gives you two tests that catch most of them mechanically.

## Leak 1: deciding at the close with the close

The signal is computed from today's close and the position earns today's close-to-close return. In pandas it is the missing `shift(1)`. Lesson 4 showed the correct version; here is the size of the defect.

On the SMA200 trend rule over 2016-2025, fills at the signal bar's close (the legitimate MOC convention) gave a Sharpe of 1.00, a CAGR of 11.82% and a maximum drawdown of -19.8%. Removing the shift, so the position on the crossing day already holds that day's return, gave a Sharpe of 1.76, a CAGR of 22.20% and a maximum drawdown of -10.1%. The leak nearly doubled the return and halved the drawdown. The mechanism is simple: the day the close crosses above the SMA is, by construction, an up day, and the day it crosses below is a down day, and the leaked version is long for the first and flat for the second, every time.

On the RSI(2) rule the same defect gave a Sharpe of -2.44 and a total return of -93%, against the honest 0.37 and +41%. Here the entry fires on a large down day, and the leaked version holds through it. Leakage cuts both ways; a number that is too bad is as much a defect as one that is too good.

## Leak 2: intrabar peeking

A daily bar tells you the high and low but not when they happened or whether you could have traded there. Any rule that fills at the high or low, or that uses the high or low to decide something and then fills at the open or close of the same bar, is reading the end of the day at the start of it.

The common form is the limit order. Buying with a limit 2% below yesterday's close is a real strategy: your order rests, and it fills at your limit price if the day's low touches it, or at the open if the market gaps through it. The leak is filling the order at the low itself. The worked example measures the gap.

## Leak 3: future-dated data

Fundamentals are the classic case. A company's fourth-quarter revenue is dated December 31 and filed in mid-February; a series indexed by fiscal period leaks six to eight weeks on every row. Economic data is revised: the payroll number your rule reads for March 2020 is the third revision, not the one released in April 2020. Index membership lists are the survivorship case from lesson 2. Even prices leak: an adjusted close is restated every quarter (lesson 2), so a signal computed on adjusted prices can shift slightly when a new dividend is paid, which is why signals should be computed on raw prices or with an adjustment that is frozen as of the signal date.

The rule for all of these is point-in-time: every value is stamped with the date it became known, and the rule reads only values stamped on or before the decision date.

## Leak 4: the researcher

Choosing the window after seeing the equity curve, dropping 2020 because it "was not representative", picking the SMA length that worked: these leak the future through you. Lesson 7 is about them.

## Two mechanical tests

Truncation invariance. Run the rule on the full data and on the data truncated at some date D, and compare the signal series up to D. They must be identical. Any rule that normalises with a full-sample mean, centres a window, fits a model on all rows, or fills forward from later data will fail. This test catches every leak that runs through the code, and it costs one line.

```python
cut = "2022-12-30"
full = rsi_signal(adj).loc[:cut]
trunc = rsi_signal(adj.loc[:cut])
assert (full != trunc).sum() == 0, "signal reads the future"
```

The fill-price bracket. For every fill, record the bar's open, high, low and close alongside the fill price, and assert that a buy fills at a price you could have known: the open, the close, or a limit price you set the day before. A fill at the low or at the high fails. This catches the intrabar leaks that truncation cannot see, because peeking at the low does not change with later data.

## Worked example

All numbers use the adjusted SPY bars from lesson 2 (Yahoo Finance chart API, 2,765 rows, 2015-01-02 to 2025-12-30), tested 2016-01-04 to 2025-12-30, no costs.

The intrabar leak. A limit order to buy at 0.98 times yesterday's adjusted close rests each day; if the day's low is at or below it, the order fills and the position is sold at that day's close. Two fill models: at the limit price (or the open, if the open gapped below the limit), and at the day's low.

```python
import numpy as np
lim = adj["close"].shift(1) * 0.98
filled = adj["low"] <= lim
fill_ok = np.where(adj["open"] <= lim, adj["open"], lim)        # what you could get
r_ok = pd.Series(np.where(filled, adj["close"] / fill_ok - 1, 0.0), index=adj.index)
r_low = pd.Series(np.where(filled, adj["close"] / adj["low"] - 1, 0.0), index=adj.index)
w = slice("2016-01-01", "2025-12-31")
print(filled.loc[w].sum())                                        # 167
print(r_ok.loc[w][filled].mean(), (1 + r_ok.loc[w]).prod() - 1)   # 0.000417  0.058
print(r_low.loc[w][filled].mean(), (1 + r_low.loc[w]).prod() - 1) # 0.009167  3.547
```

The order filled on 167 days. Priced honestly, the average fill earned +0.042% by the close and the ten-year total was +5.8%, an annualised Sharpe of 0.14: nothing. Priced at the low, the average fill earned +0.917%, the total was +354.7%, and the Sharpe was 2.69. The difference, 0.875 percentage points per fill, is the average distance from the day's low to the limit price on days that touched the limit; it is the size of the fiction, and it is 22 times the honest edge.

Truncation invariance, on three rules, with the cut at 2022-12-30 (2,014 rows from 2015-01-02 to the cut):

- A full-sample z-score rule, long when the close is more than half a standard deviation below the full-sample mean: 456 of the 2,014 signals up to the cut changed when 2023-2025 was appended, because the mean and standard deviation moved. This rule reads the future on every row.
- The same rule with a rolling 252-day mean and standard deviation: 0 changes.
- The RSI(2) rule: 0 changes. Wilder's smoothing is recursive and uses only past values.

The full-sample z-score is the version people write first, because `(close - close.mean()) / close.std()` is the natural line. It is a leak, and the test finds it in one assertion.

## Table

A catalogue of leaks, the symptom, and the check that finds each one.

| Leak | Typical code or data | Symptom | Check |
|---|---|---|---|
| Same-bar decision | Missing `shift(1)`; `pos = signal` | Trend rules look far too smooth; mean-reversion rules look absurd in either direction | Hand-walk five rows (lesson 4); compare Sharpe with and without shift |
| Intrabar fill | Fill at `low` or `high`; stop assumed to fill at the stop price on a gap | Per-fill edge far above the spread; Sharpe above 2 on a daily rule | Fill-price bracket: every fill equals open, close or a prior-day limit |
| Full-sample statistic | `close.mean()`, `close.std()`, `rolling(center=True)`, a model fit on all rows | Signals change when data is appended | Truncation invariance |
| Future-dated fundamentals | Series indexed by fiscal period | Rule "anticipates" earnings | Index by filing date; point-in-time database |
| Restated prices | Signals on adjusted closes that shift with each dividend | Signals drift between fetches | Compute signals on raw prices or freeze the factor at the signal date |
| Survivor universe | Today's index members applied to the past | Long-only stock rules with no blow-ups | Point-in-time membership (lesson 2) |
| Researcher | Window, parameters or exclusions chosen after seeing results | Every backtest passes | Pre-registered rule and thresholds (lesson 3); deflated Sharpe (lesson 7) |

Run the first three checks on every rule before reading a single performance number. They are cheap and they catch most of the fiction.

## Sources

- Bailey, D. H., Borwein, J., López de Prado, M., Zhu, Q. J. (2014). "Pseudo-Mathematics and Financial Charlatanism." Notices of the AMS 61(5). https://doi.org/10.1090/noti1105
- pandas documentation, `Series.rolling` (note the `center` parameter, which is a leak in any signal): https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html
- SEC EDGAR full-text search (filing dates are the point-in-time stamp for fundamentals): https://www.sec.gov/edgar/search/
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

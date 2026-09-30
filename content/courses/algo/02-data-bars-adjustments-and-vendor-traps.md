---
{
  "title": "Data: Bars, Adjustments, Survivorship and Vendor Traps",
  "duration": "18 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "SPY went ex-dividend on 2024-12-20. The raw close moved from 586.10 to 591.15 (+0.862%) while the adjusted close moved +1.201%. Which return did a holder actually earn?", "opts": ["+0.862%, the price return", "+1.201%, because the $1.966 dividend is theirs too", "Neither; dividends are paid later so the return is undefined", "+0.862% minus tax"], "correct": 1, "explain": "The holder received $1.966 per share on top of the price move. Adjusted prices fold that payment into the series so that close-to-close returns are total returns."},
    {"q": "Requesting Yahoo's chart endpoint with range=max and interval=1d returned 405 rows for SPY. What happened?", "opts": ["SPY has only traded for 405 days", "The endpoint silently returned monthly bars; dataGranularity in the response reads 1mo", "The request was rate-limited", "Rows were de-duplicated"], "correct": 1, "explain": "With range=max the endpoint downgrades the interval and says so only in the meta block. Explicit period1/period2 timestamps returned 2,765 daily rows for the same ticker."},
    {"q": "Survivorship bias means:", "opts": ["Your universe today omits the names that were delisted along the way, so any test on it overstates what a trader at the time could have earned", "Old prices are less accurate", "Only large caps have long histories", "Backtests favour rules that survive costs"], "correct": 0, "explain": "The names that went to zero are not in today's S&P 500 list. A rule tested on today's members never buys them, which no real trader in 2016 could have arranged."},
    {"q": "A vendor's daily file for a ticker that delisted in 2019 keeps returning bars through 2025 with an unchanged close and zero volume. What is the correct treatment?", "opts": ["Keep them; a flat price has zero return and does no harm", "Drop the padded rows; a flat series with zero volume is not tradeable and it hides the delisting event", "Average them with the index", "Fill the volume from a peer"], "correct": 1, "explain": "The padded rows make a dead name look like a name that stopped moving. A rule could hold it forever with no drawdown and no cost, which never happened. Detect it with a zero-volume run and cut the series at the last real print."},
    {"q": "Why does a point-in-time universe matter more for a 500-stock rule than for a single-ETF rule?", "opts": ["ETFs never delist", "Stocks have more dividends", "Point-in-time data is only sold for stocks", "The ETF has no membership, so there is no list that could have been built with hindsight; a stock universe chosen today is a list built with hindsight"], "correct": 3, "explain": "The look-ahead is in the list, not the prices. SPY's history is one series with no membership decisions to leak. A basket picked from today's constituents leaks the survivors."}
  ],
  "task": "Fetch SPY daily bars for 2015-01-01 to 2025-12-31 with explicit period1 and period2, print the row count per calendar year, and confirm dataGranularity reads 1d."
}
---

## What a bar is

A daily bar is four prices and a count: the first trade of the session (open), the highest and lowest trades (high, low), the last trade (close), and the number of shares that changed hands (volume). It is a summary, and everything a summary throws away is a place a backtest can cheat. You do not know the order in which the high and the low occurred. You do not know whether the open printed on one share or a million. You do not know that a price "traded" in any size you could have taken. Lesson 6 shows what happens when a rule pretends otherwise.

For a US ETF like SPY the close is the official closing auction price, which is the most reliable number in the bar: it is the print the MOC order book settles at and the one every index fund marks to. The open is the opening auction print and is also reliable. Highs and lows are single trades and can be odd lots or prints away from the NBBO. If a rule depends on the high or low, assume it is the most fragile thing in the row.

## Adjustments: splits and dividends

A price series is a record of what a share cost, not of what a holder earned. Two corporate actions break the link. A split multiplies the share count and divides the price; without adjustment, a 4-for-1 split looks like a 75% crash. A dividend moves cash out of the share and into the holder's account; on the ex-dividend date the price drops by roughly the dividend and the holder is no better or worse off, but a price series shows a loss.

Vendors handle this by publishing an adjusted close: the raw close multiplied by a cumulative factor that is less than one before each dividend and split. Yahoo's chart endpoint returns both `close` and `adjclose`. The factor for any row is `adjclose / close`, and it changes only on ex-dates. To adjust the open, high and low, multiply them by the same row's factor. Once every price column is adjusted, close-to-close returns are total returns and split days are flat.

Two things follow. First, the adjusted series is re-stated every time a new dividend is paid: the factor for 2016 shrinks a little each quarter, so an adjusted close you saved last year is not the one you will download this year. If you cache bars, store raw prices and the factor separately, and re-derive. Second, the difference is not small. SPY's price return from 2015-01-02 to 2025-12-30 was +234.4%; its total return over the same window was +302.7%. A backtest on raw closes gives the buy-and-hold benchmark 68 points less than it earned and makes any rule that sits in cash across ex-dates look relatively better.

## Survivorship and point-in-time universes

Single-ticker tests on SPY are immune to the next problem, which is why this course uses SPY. Multi-stock tests are not. If you test a rule on "the S&P 500" using the list of members as of today, you are testing on 500 companies that are known to have survived to today. The names that fell out (bankruptcies, acquisitions, the ones that dropped 90% and were replaced) are absent. Your rule never buys them, and no trader in 2016 could have arranged that.

The fix is a point-in-time universe: for every date in the test, the list of names that were members on that date, including the ones that were later removed. That data is not free. Without it, the honest choices are to test on an instrument with no membership (a broad ETF), or to build the universe from a rule that uses only information available at the time (for example, the 500 largest names by market cap on each rebalance date, computed from a full delisted-inclusive price database), and to state plainly that you did so.

The same look-ahead hides in fundamentals. A company's Q4 earnings are dated December 31 but were not public until February. A fundamental series indexed by fiscal period leaks about six weeks of the future on every row; it must be indexed by the date the number was filed. Lesson 6 has more.

## Vendor traps

Three faults recur across vendors and are worth checking on every fetch.

The padded delisted ticker. A name stops trading, and the vendor's daily file keeps emitting rows with the last close repeated and volume zero, sometimes for years. A rule that holds the name sees no return, no drawdown and no cost, forever. Detect it with a run of zero-volume rows or an unchanged close over more than a handful of sessions, and cut the series at the last real print.

The silent interval downgrade. Yahoo's chart endpoint with `range=max&interval=1d` returns SPY as 405 monthly bars; the response's `meta.dataGranularity` reads `1mo` and nothing else warns you. Explicit `period1` and `period2` Unix timestamps with `interval=1d` return daily bars. Always read the granularity field back and always count rows against the trading calendar.

The missing or duplicated row. Holidays, half days and vendor outages leave gaps; re-stated rows leave duplicates. A per-year row count against the exchange calendar (about 252) catches both, and an index uniqueness check catches the second.

## Worked example

The data used across this course is SPY daily bars from Yahoo Finance's chart API, requested on 2026-09-30 with explicit Unix timestamps. `period1=1420070400` is 2015-01-01 00:00 UTC and `period2=1767139200` is 2025-12-31 00:00 UTC.

```python
import json, datetime as dt, urllib.request
import pandas as pd

def unix(y, m, d):
    return int(dt.datetime(y, m, d, tzinfo=dt.timezone.utc).timestamp())

url = ("https://query1.finance.yahoo.com/v8/finance/chart/SPY"
       f"?period1={unix(2015,1,1)}&period2={unix(2025,12,31)}&interval=1d&events=div,split")
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
res = json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]
assert res["meta"]["dataGranularity"] == "1d"          # the interval trap
q = res["indicators"]["quote"][0]
px = pd.DataFrame({"open": q["open"], "high": q["high"], "low": q["low"], "close": q["close"],
                   "adj_close": res["indicators"]["adjclose"][0]["adjclose"], "volume": q["volume"]},
                  index=pd.to_datetime(res["timestamp"], unit="s", utc=True)
                          .tz_convert("America/New_York").normalize().tz_localize(None))
assert px.index.is_unique and px.isna().sum().sum() == 0
print(len(px), px.index[0].date(), px.index[-1].date())
print(px.groupby(px.index.year).size().to_dict())
```

The response held 2,765 rows from 2015-01-02 to 2025-12-30, no nulls, 44 dividend events and 0 splits. Row counts per year: 2015: 252, 2016: 252, 2017: 251, 2018: 251, 2019: 252, 2020: 253, 2021: 252, 2022: 251, 2023: 250, 2024: 252, 2025: 249. Every year matches the NYSE calendar (2025 is 249 because the window ends on 12-30; 2020 is 253 because 2020 had no weekday holidays lost to weekends). The same ticker requested with `range=max&interval=1d` returned 405 rows with `dataGranularity` equal to `1mo`.

Now the adjustment. SPY went ex-dividend on 2024-12-20. The previous close (2024-12-19) was 586.10; the ex-date close was 591.15.

Raw return: 591.15 / 586.10 - 1 = +0.862%.

The adjustment factors (`adj_close / close`) were 0.977443 on 12-19 and 0.980733 on 12-20. Adjusted return: (591.15 × 0.980733) / (586.10 × 0.977443) - 1 = +1.201%.

The implied dividend is the previous close times one minus the ratio of the factors: 586.10 × (1 - 0.977443 / 0.980733) = $1.966 per share, which matches the $1.966 distribution SPY paid for Q4 2024. A holder earned 1.201% that day; a raw-price backtest records 0.862%. The 0.339-point gap recurs every quarter, and across 44 dividends it compounds into the 68-point difference between price return and total return quoted above.

```python
factor = px["adj_close"] / px["close"]
adj = px[["open", "high", "low", "close"]].mul(factor, axis=0)   # adjust every price column
adj["volume"] = px["volume"]
adj.to_csv("spy_adjusted.csv")
```

The adjusted frame `adj` is what every later lesson reads.

## Table

The checks to run on every bar file before a single rule touches it, with what each one caught on this fetch.

| Check | How | This fetch |
|---|---|---|
| Interval is what you asked for | Read `meta.dataGranularity` | `1d` with explicit timestamps; `1mo` with `range=max` |
| Row count per year vs exchange calendar | `groupby(year).size()` | 249 to 253 per year, all consistent with NYSE |
| Unique, sorted index | `index.is_unique`, `index.is_monotonic_increasing` | Both true |
| No nulls in price columns | `isna().sum()` | 0 |
| Adjustment factor only changes on ex-dates | `(factor.diff().abs() > 1e-6).sum()` equals number of events (the raw diff is never exactly zero because `adjclose` is rounded) | 44 changes, 44 dividends, 0 splits |
| No padded tail | Zero-volume rows; longest run of unchanged closes | 0 zero-volume rows; 6 single sessions with an unchanged close, no run longer than 1 |
| Price sanity | `low <= min(open, close)`, `high >= max(open, close)` | Holds on all 2,765 rows |

Run this table as code, not as a habit. A single assertion that fails loudly is worth more than a careful glance.

## Sources

- Yahoo Finance, SPY historical prices (dividends and splits listed under the Historical Data tab): https://finance.yahoo.com/quote/SPY/history/
- NYSE holidays and trading hours (calendar used for the per-year row counts): https://www.nyse.com/markets/hours-calendars
- pandas documentation, `DataFrame.groupby` and `Index.is_unique`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
- Elton, E. J., Gruber, M. J., Blake, C. R. (1996). "Survivor Bias and Mutual Fund Performance." Review of Financial Studies 9(4). https://doi.org/10.1093/rfs/9.4.1097

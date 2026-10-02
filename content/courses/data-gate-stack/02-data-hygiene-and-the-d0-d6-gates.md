---
{
  "title": "Data Hygiene: Adjustments, Survivorship and the D0-D6 Gates",
  "duration": "20 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Two vendors' adjusted price levels for a high-yield stock differ by a steady 235 bps while their raw closes agree to the cent and their daily returns differ by less than 1 bp. What is wrong?", "opts": ["The high-yield vendor has a corrupt file", "The stock had a split one vendor missed", "Nothing about the prices; the two vendors amortise dividends differently, so a level comparison is a dividend-yield test in disguise", "The returns must be recomputed from the levels"], "correct": 2, "explain": "An adjusted level embeds every dividend since the start of the series under a convention the vendor chose. Two conventions diverge in proportion to yield. Returns, which is what every backtest consumes, are what to compare."},
    {"q": "On 2024-12-20 SPY's raw close moved from 586.10 to 591.15 while the Cboe S&P 500 index moved from 5,867.08 to 5,930.85. The raw SPY return is 22.5 bps below the index's. The most likely explanation is:", "opts": ["The ETF was mispriced at the close", "SPY went ex-dividend that day; its adjusted return of +120.1 bps is 13.4 bps above the index, within normal tracking", "The index vendor has a stale close", "A split"], "correct": 1, "explain": "Raw 591.15/586.10 - 1 = +0.862%; adjusted 579.7604/572.8795 - 1 = +1.201%; index 5930.85/5867.08 - 1 = +1.087%. The $1.966 distribution explains the raw shortfall, and the adjusted series lands on the far side of the index by an ordinary amount."},
    {"q": "A vendor keeps returning daily bars for a bank that failed in March 2023: close 0.006, volume 0, every day through 2026. Which universe rule keeps it out?", "opts": ["Require non-zero volume over a trailing window before a name enters the universe on a given date", "Require that the vendor returns a bar on the date", "Require a price above $1", "Ask the vendor's metadata endpoint whether the name is listed"], "correct": 0, "explain": "Presence is not liveness. The metadata endpoint returned all-None for that name. A price floor would have caught this one and missed a padded name at $30. Only an activity test generalises."},
    {"q": "A quality gate measures coverage against the requested window and rejects a 2010 IPO at 46% coverage of a 35-year request. Clamping the window start to the first bar the vendor returned would:", "opts": ["Fix it with no side effect", "Also make a vendor that silently truncates a 5-year request to 2 years read as 100% coverage", "Only affect ETFs", "Require a new vendor"], "correct": 1, "explain": "A young listing and a truncated response look identical from inside the data. The honest fix needs an explicit listing date per name, so that a missing 2009 bar for a 2010 IPO is expected and a missing 2022 bar for SPY is a defect."},
    {"q": "The D6 source-agreement gate was changed from comparing levels to comparing returns with two halves: a shifted median and a fraction of outlier days. Why both?", "opts": ["Two tests are always better than one", "The median finds a basis error and cannot see a split booked on the wrong day; the outlier fraction finds the mis-dated split and cannot see a basis error", "The median is for daily and the fraction for intraday", "Regulators require two"], "correct": 1, "explain": "One name passed a level comparison at 0.00 bps while 252 of 2,683 days disagreed by more than 50 bps on the return, because a split had been booked a day apart. A median over levels is blind to that; a count of outlier days is not."}
  ],
  "task": "Fetch one year of daily bars for a ticker of your choice from two different vendors, align them by date, and report the median absolute difference in daily returns in bps and the number of days that differ by more than 50 bps."
}
---

## What a price series is not

A price series is a record of what a share cost on each day. It is not a record of what a holder earned, it is not a record of which companies existed, and it is not a record of which rows are real. Each of those gaps has a name and a check, and the checks run before any rule is defined, because a rule cannot tell a real bar from a fake one.

## Splits and dividends

A split changes the share count and the price together. Without adjustment a 10-for-1 split reads as a 90% crash. A dividend moves cash out of the share and into the holder's account; the price drops by roughly the dividend on the ex-date, and a raw series records a loss the holder did not take. Vendors publish an adjusted series that multiplies earlier prices by a cumulative factor so that close-to-close returns become total returns.

Yahoo's chart endpoint returns two columns. `close` is already adjusted for splits: NVDA's 10-for-1 on 2024-06-10 shows as 120.89 on 06-07 and 121.79 on 06-10, no cliff. `adjclose` adds dividends. The ratio `adjclose / close` is the dividend factor, and for SPY between 2015 and 2025 it changes exactly 44 times, once per quarterly distribution. To adjust the open, high and low, multiply each by that same ratio. XLF's 1,231-for-1,000 event on 2016-09-19 is the reminder that not every "split" is a split: it was a special distribution of a real-estate spin-off, and Yahoo booked it into `close` as a split factor. The bar shows +0.64% both raw and adjusted, which is right, but a strategy reading `volume` per share across that date sees a discontinuity that is not a trade.

The trap is not the arithmetic. It is a stored series that keeps the adjustment state it had when it was fetched. The research notes (Phantom Traders, 2026, internal) record a table whose bars were upserted only for recent dates: after a 30-for-1 reverse split the rows before the split stayed at the old scale and the rows after arrived at the new one, so one day read as +2,309% against a real move of −19.7%. Nine of 42 watchlist names had a corporate action in the prior fifteen months. A ranking strategy loved the fake crashes: it manufactured +183% a year, and on re-fetched data the same test was −9.7 bps a day. The fix was to re-fetch the whole history once the action settled, never to derive factors by hand and make your own arithmetic the source of truth. Then a second seam appeared, because the vendor's plan capped daily history at about two years, so a re-fetch asking for more silently started at that boundary and left the older bars stale. Always check the date range a fetch returned, not the row count; "501 bars upserted" read as success.

## Survivorship and the padded dead

A universe built from today's constituents omits every name that failed on the way. That is survivorship bias in its textbook form and the point-in-time list is the fix. The notes add a more specific trap: delisted names behave three different ways in the same vendor's feed. One taken private in October 2022 ends cleanly on its last day. One bank that failed in May 2023 returns HTTP 404, a visible hole. A third, a bank that failed in March 2023, collapses correctly from $283 to $0.97 on real volume and then never stops: close 0.006, volume 0, every day through September 2026. The vendor's metadata endpoint answered all-None when asked whether it was listed.

The padded name is worse than the 404 because it is fiction shaped like data. A universe built on "has a bar on date X" holds a company that has not existed for three years. A low-price screen adores a six-tenths-of-a-cent stock. And a flat series has a daily return of exactly zero, which quietly deflates any volatility, Sharpe or correlation computed across the universe. Liveness has to be an activity test: non-zero volume over a trailing window before a name may enter on a given date.

The mirror-image trap is coverage. A quality gate that measures coverage against the requested window will reject a 2010 IPO asked for 35 years of history at 46.1% coverage, while the vendor delivered 99.7% of the days the stock has existed. The obvious fix, clamping the window to the first returned bar, disarms a working defence: a vendor that returns two years of a five-year request and calls it success would then read as 100% covered. From inside the data the two cases are identical. Separating them needs the listing date, recorded explicitly per name.

## Missing rows, holidays and the calendar

Count rows per year against the exchange calendar. SPY from Yahoo and the S&P 500 from Cboe both hold 2,766 rows for 2015-01-02 to 2025-12-31, with identical dates: 252, 252, 251, 251, 252, 253, 252, 251, 250, 252 and 250 per year. The date sets match exactly, so no holiday, half-day or outage is represented differently by the two vendors. A mismatch would name the missing or extra row directly. Also assert a unique, sorted index; re-stated rows arrive as duplicates.

## Vendor disagreement: the only test that finds an unknown

Every other check asks a question you already know how to ask. A second source finds what you did not know to ask about. The notes' first cross-sectional run of the source gate (28 tickers, 2026-09-14) also found two defects in the gate itself, and both are instructive.

The gate compared adjusted price levels and refused two names for disagreeing by 51 and 235 bps. Their raw closes agreed to 0.00 bps and their daily returns differed by about 1 bp. Each vendor amortises dividends under its own convention, so adjusted levels diverge in proportion to yield: 1.31 bps on SPY, 51 on a mid-yielder, 235 on the highest yielder in the set. A level comparison is a dividend-yield threshold in disguise. Meanwhile one name passed the level test at 0.00 bps and had 252 of 2,683 days disagreeing by more than 50 bps on the return, worst case 7,529 bps, because a split had been booked on different days by the two vendors. A median over levels cannot see that. The gate was rebuilt to test returns, which is what every downstream number uses, with two halves that catch different things: a shifted median for a basis error and an outlier-day fraction for a mis-dated event.

Two more rules from the same run. A dataset pulled from vendor X cannot be audited by vendor X; it passes by construction, which is a green check testing nothing and is worse than a skip. And a missing reference is a skip, reported by name, never a pass. Coverage of the audit is itself reported: a reference that reaches 32% of the trades is not the same evidence as one that reaches 100%.

## Worked example

Yahoo Finance SPY daily bars against Cboe's published S&P 500 index history, 2015-01-02 to 2025-12-31, both fetched 2026-09-30. Cboe is not Yahoo, so the test is real. The instrument is not identical either (an ETF holding the index, with dividends, against the index level without them), which is exactly the situation the returns-not-levels rule is for.

Levels first, to show why they fail. The ratio of SPY's raw close to the index is 0.09981 on 2015-01-02 and 0.09962 on 2025-12-31, a drift of −0.20% over eleven years. The ratio of SPY's dividend-adjusted close to the index drifts from 0.08224 to 0.09884, +20.19%, because the adjusted series folds eleven years of distributions into its early values. A level gate at 40 bps would refuse the adjusted series on day one, and the prices are fine.

Now returns, in bps, aligned on 2,765 common days.

Raw SPY close against the index: median absolute difference 2.61 bps; 20 days differ by more than 50 bps (0.72%). The largest are the crash days of March 2020 and April 2025 (an ETF's 4 p.m. auction print against an index computed from constituent closes can differ by 100 bps on a −11% day) and then a run of mid-December dates: 2016-12-16 (raw −78.0 vs index −17.5), 2015-12-18 (−236.3 vs −178.0), 2017-12-15 (+32.0 vs +89.7). Those are SPY ex-dividend dates.

Adjusted SPY close against the index: median absolute difference 2.56 bps; 5 days differ by more than 50 bps (0.18%). The December dates are gone (2016-12-16 adjusted: −19.6 vs −17.5). The five that remain are all in March 2020 and April 2025, and both vendors report them; they are real.

The single-day arithmetic for the 2024-12-20 ex-date: raw 591.15 / 586.10 − 1 = +0.862% (86.2 bps); adjusted 579.7604 / 572.8795 − 1 = +1.201% (120.1 bps); index 5,930.85 / 5,867.08 − 1 = +1.087% (108.7 bps). Raw sits 22.5 bps below the index and adjusted 13.4 bps above it. The implied distribution, 586.10 × (1 − 0.977443 / 0.980733) = $1.966 per share, matches the quarter's declared amount. On 2024-12-23, a day with no distribution, raw and adjusted both read +59.9 bps against the index's +72.9, ordinary tracking.

![Nine bars of SPY's daily return in bps on 2016-12-16, 2024-12-20 and 2024-12-23, each date shown three ways: Yahoo raw close, Yahoo dividend-adjusted close and the Cboe S&P 500 index. On the two ex-dividend dates the raw bar falls short of the index and the adjusted bar does not; on the control date all three agree.](figures/vendor-returns-ex-dividend.svg)

The gate's verdict: returns median 2.56 bps against a 5 bps bar, outlier fraction 0.18% against a 1% bar, PASS on the adjusted series, with the five outlier days listed by name so a reader can see they are crashes and not defects.

## Table

The seven data gates, in the order they run, and what each one caught in the research notes.

| Gate | Question | What it caught |
|---|---|---|
| D0 range | Did the response cover the dates requested? | An 18-year request answered with status OK and 502 rows |
| D1 grid | Are timestamps on the expected grid? | 44,961 snapshot rows at second resolution inside a 5-minute table |
| D2 shape | Do sessions hold the expected bar count? | 150-bar sessions where 78 was right; duplication shows as sessions that are too long |
| D3 empty | Any bars with zero volume and open = high = low = close? | 281,905 dead rows; 202 padded bars on a delisted name |
| D4 close | Does every intraday session end on a bar that traded? | The 16:00 stub. Intraday only: a daily bar is its own session |
| D5 continuity | Any jump over 45% on daily (25% intraday) unconfirmed by the reference? | A mixed adjusted/unadjusted seam faking +183% a year; real −30% days kept because the second source agreed |
| D6 source | Do daily returns agree with an independent vendor: median under 5 bps, under 1% of days beyond 50 bps? | A split booked a day apart (9.4% of days disagreeing); two false refusals when it still compared levels |

D5's threshold is stated with its cost: a 3-for-2 split (33%) sits inside the daily noise floor and D5 cannot see it. D6 is what catches those, and it needs a vendor that did not produce the file.

## Sources

- Elton, E. J., Gruber, M. J., Blake, C. R. (1996). "Survivor Bias and Mutual Fund Performance." Review of Financial Studies 9(4). https://doi.org/10.1093/rfs/9.4.1097
- Shumway, T. (1997). "The Delisting Bias in CRSP Data." Journal of Finance 52(1). https://doi.org/10.1111/j.1540-6261.1997.tb03818.x
- Cboe Global Markets, S&P 500 index daily price history (the second source used above): https://cdn.cboe.com/api/global/us_indices/daily_prices/SPX_History.csv
- Yahoo Finance, SPY historical data with dividends and splits: https://finance.yahoo.com/quote/SPY/history/

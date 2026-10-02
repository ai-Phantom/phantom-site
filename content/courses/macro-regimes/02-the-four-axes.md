---
{
  "title": "The Four Axes: Growth, Inflation, Rates and Liquidity, Volatility",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Which of the four axes is read from the fastest-updating data?", "opts": ["Growth, from GDP", "Inflation, from CPI", "Volatility, from the VIX close", "Rates and liquidity, from the Fed balance sheet"], "correct": 2, "explain": "GDP is quarterly and revised, CPI is monthly with a two-week lag, the balance sheet is weekly. The VIX prints every session. That is why the classifier in lesson 9 uses volatility rather than growth as one of its two inputs."},
    {"q": "On 2022-06-30, CPI inflation was 9.0% year on year, the 10-year real yield was +0.65% (up from -1.04% at the end of 2021), and the VIX closed at 28.71. Which axis had moved the most since December 2021?", "opts": ["Rates, as measured by the real yield", "Growth", "Inflation, as measured by CPI", "Volatility"], "correct": 0, "explain": "CPI rose from 7.2% to 9.0%, a large move. But the real yield moved from -1.04% to +0.65%, a 1.69-point swing in the price of money after inflation, which is what repriced both stocks and long bonds in 2022."},
    {"q": "Why does the course treat rates and liquidity as one axis rather than two?", "opts": ["Because they are the same number", "Because liquidity cannot be measured", "Because rates never change", "Because both are set by the same institution and move the same direction over a cycle: the Fed tightens by raising the funds rate and shrinking its balance sheet, and eases by doing the reverse"], "correct": 3, "explain": "They are different quantities (a price and a stock), but over a cycle they are steered together. Lesson 5 shows the one period where they diverged, 2019-2020, when the balance sheet grew while the funds rate was cut."},
    {"q": "The unemployment rate was 3.4% in April 2023 and 4.1% in August 2026 (BLS via FRED). As a growth reading this tells you:", "opts": ["A recession has started", "The labour market has loosened from a very tight level; on its own that is neither a recession signal nor a growth signal", "Nothing, because unemployment is a lagging indicator", "Growth has accelerated"], "correct": 1, "explain": "Unemployment lags the cycle and 4.1% is not high by the standards of the last forty years. The growth axis needs several readings, and none of them is decisive alone."},
    {"q": "Which of these is an observable-at-the-close reading of the inflation axis?", "opts": ["Next month's CPI print", "The Fed's stated 2% target", "The 10-year breakeven inflation rate from FRED (T10YIE)", "The average CPI of the last decade"], "correct": 2, "explain": "The breakeven is a market price, updated daily, that embeds the bond market's inflation expectation. The CPI print is known only after the month ends; the target and the long average do not change with the environment."}
  ],
  "task": "Open FRED and pull the latest value of one series from each axis (for example UNRATE, T10YIE, DFF, VIXCLS) and write the four numbers with their dates in one line."
}
---

## Four questions about the environment

Any trading environment can be described by answering four questions. Is the economy growing or shrinking? Are prices accelerating or decelerating? What does money cost and how much of it is the central bank adding or draining? How much is the market moving, and how much does it expect to move? Those are the growth, inflation, rates-and-liquidity and volatility axes. This lesson gives each one a definition, a data source, an update frequency and a reason a trader should care. Lessons 3 through 6 then take each in turn.

The axes are not independent. Inflation drives rates, rates drive liquidity, liquidity drives volatility, and volatility feeds back into growth through financial conditions. That is why a two-variable classifier can work at all: the axes are correlated enough that two well-chosen readings carry much of the information in four.

## Growth

Growth is what the whole cycle is nominally about and it is the hardest axis to read in real time. The canonical measure, real GDP, is quarterly, arrives a month after the quarter ends, and is revised for years. The monthly series are better: nonfarm payrolls (FRED PAYEMS), the unemployment rate (UNRATE), industrial production (INDPRO), and weekly initial jobless claims (ICSA). All come from the Bureau of Labor Statistics or the Federal Reserve and are free on FRED.

The trader's use of the growth axis is mostly defensive. A rule built for an expanding economy will meet a contraction eventually, and the contraction will arrive in the price data before it arrives in GDP. That is why this course reads growth largely through its market shadows: the yield curve (lesson 3), credit spreads (lesson 5) and the trend in the index itself (lesson 7).

## Inflation

Inflation has two readings: what has happened and what is expected. What has happened is the Consumer Price Index (BLS, FRED CPIAUCSL) and the personal consumption expenditures price index (BEA, FRED PCEPI), both monthly. The Fed targets PCE, the public discusses CPI, and the two usually differ by half a point or so; in June 2022 CPI was 9.0% year on year and PCE was 7.2%.

What is expected is priced in the Treasury market. The 10-year breakeven inflation rate (FRED T10YIE) is the nominal 10-year yield minus the 10-year inflation-indexed yield; it is the inflation rate at which a nominal bond and a TIPS return the same. The inflation-indexed yield itself (FRED DFII10) is the real yield, the price of money after inflation, and lesson 4 shows that it, not the CPI print, is the variable that moved stocks, bonds and gold in 2022.

## Rates and liquidity

The price of money is the federal funds rate, set by the Federal Open Market Committee at eight scheduled meetings a year and published daily as the effective rate (FRED DFF). The quantity of money the central bank is supplying is read from its balance sheet: total assets (FRED WALCL, weekly, Wednesday) grow when the Fed buys securities and shrink when it lets them mature. The overnight reverse repo facility (FRED RRPONTSYD, daily) is where excess cash parks when there is more of it than the banking system wants.

These are one axis because they are steered together. From March 2022 the Fed raised the funds rate from 0.08% to 5.33% and, from June 2022, shrank its balance sheet from a peak of $8.97 trillion (2022-04-13) to $6.75 trillion (2026-09-23). Both are tightening; both are read from FRED; lesson 5 gives the dates.

## Volatility

Volatility is the fastest axis and the one closest to your P&L. Realised volatility is what the market did: the annualised standard deviation of daily returns over some window. Implied volatility is what the market expects: the VIX is the 30-day expected volatility of the S&P 500 implied by option prices, computed by Cboe from a strip of puts and calls. Both are daily. Lesson 6 measures how they relate (the VIX has sat above trailing realised volatility on 86% of sessions since 1993) and what SPY did in months of high and low VIX.

Volatility is the axis you can least afford to ignore, because it determines the size of your losses directly. A 1% position in a 12%-volatility market and a 1% position in a 40%-volatility market are not the same risk, whatever the growth and inflation readings say.

## Reading all four at once

The table in the worked example puts the four axes side by side at five dates chosen because the environment was different at each. Read down the columns to see what each axis looked like in a calm expansion, a pandemic crash, an inflation shock, a soft landing and the present. Read across the rows to see which axes move together.

## Worked example

Every number below is from FRED (https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES) or the Yahoo Finance chart API, pulled 2026-09-30. The FRED series are UNRATE (monthly), CPIAUCSL (monthly, converted to year-on-year by dividing each month by the value twelve months earlier), T10YIE, DFII10 and DFF (daily), WALCL (weekly). The VIX is the `^VIX` close from Yahoo. Where a date falls on a day without a print, the last available value is used and its date is noted.

The five dates: 2019-12-31 (late expansion), 2020-03-23 (SPY's pandemic low), 2022-06-30 (CPI peak month), 2023-12-29 (soft-landing consensus), 2026-09-29 (latest full session).

Growth. UNRATE: 3.6% (Dec 2019), 4.4% (Mar 2020, the April print was 14.8%), 3.6% (Jun 2022), 3.8% (Dec 2023), 4.1% (Aug 2026, latest). The reading is nearly flat across four very different markets, which is the point: unemployment alone does not separate the regimes.

Inflation. CPI year on year, computed as CPIAUCSL(month) / CPIAUCSL(month minus 12) minus one: 2.3% (Dec 2019), 1.5% (Mar 2020), 9.0% (Jun 2022, the peak; PCE was 7.2%), 3.3% (Dec 2023), 3.4% (Aug 2026; note that FRED carries no October 2025 CPI print, so always divide by the observation dated twelve months earlier rather than the row twelve positions earlier). T10YIE breakeven: 1.77 (2019-12-31), 0.80 (2020-03-23), 2.33 (2022-06-30), 2.16 (2023-12-29), 2.35 (2026-09-29). The bond market never priced the 2022 spike as permanent; the breakeven peaked at 3.02 on 2022-04-21 while CPI was still rising.

Rates and liquidity. DFF: 1.55, 0.15 (the target range was cut to 0 to 0.25% on 2020-03-15), 1.58, 5.33, 3.88. DFII10 real 10-year yield: +0.15, -0.04, +0.65, +1.72, +2.91. WALCL, nearest Wednesday print: $4.17 trillion (2019-12-25), $4.67 trillion (2020-03-18), $8.91 trillion (2022-06-29), $7.71 trillion (2023-12-27), $6.75 trillion (2026-09-23). The real-yield row is the one to remember: it went from negative to +2.9% across the sample, a repricing of money that lesson 4 connects to the 2022 losses.

Volatility. VIX close: 13.78 (2019-12-31), 61.59 (2020-03-23), 28.71 (2022-06-30), 12.45 (2023-12-29), 16.04 (2026-09-29).

Two calculations to check for yourself. The CPI year-on-year for June 2022 is 294.957 / 270.654 minus 1 = 8.98%, which rounds to 9.0%; the index levels FRED serves today carry later seasonal revisions, so the figure differs slightly from the 9.1% published in July 2022, and you should always quote the vintage you computed from. The real-yield change from 2021-12-31 (-1.04) to 2022-06-30 (+0.65) is 1.69 percentage points in six months; the largest 126-session rise in the DFII10 series (which starts in January 2003) was 2.20 points, ending 2022-09-30.

## Table

| Axis | Series (source) | 2019-12-31 | 2020-03-23 | 2022-06-30 | 2023-12-29 | 2026-09-29 |
|---|---|---|---|---|---|---|
| Growth | Unemployment rate, % (BLS, UNRATE) | 3.6 | 4.4 | 3.6 | 3.8 | 4.1 (Aug) |
| Inflation | CPI YoY, % (BLS, CPIAUCSL) | 2.3 | 1.5 | 9.0 | 3.3 | 3.4 (Aug) |
| Inflation | 10y breakeven, % (FRED, T10YIE) | 1.77 | 0.80 | 2.33 | 2.16 | 2.35 |
| Rates | Fed funds effective, % (DFF) | 1.55 | 0.15 | 1.58 | 5.33 | 3.88 |
| Rates | 10y real yield, % (DFII10) | +0.15 | -0.04 | +0.65 | +1.72 | +2.91 |
| Liquidity | Fed total assets, $T (WALCL, nearest Wednesday) | 4.17 | 4.67 | 8.91 | 7.71 | 6.75 |
| Volatility | VIX close (Cboe via Yahoo) | 13.78 | 61.59 | 28.71 | 12.45 | 16.04 |

Reading across, the 2020-03-23 column shows what a growth shock looks like before the growth data catches up: unemployment had barely moved, inflation expectations collapsed, the funds rate was at the floor, and the VIX was at 61. The 2022-06-30 column is the opposite shape: growth data fine, inflation at a forty-year high, the real yield up 1.7 points in six months, and the VIX elevated but not extreme. Those two columns are the two very different bear markets that the case studies in lesson 12 take apart.

## Sources

- Federal Reserve Bank of St. Louis, FRED series pages: https://fred.stlouisfed.org/series/UNRATE, https://fred.stlouisfed.org/series/CPIAUCSL, https://fred.stlouisfed.org/series/T10YIE, https://fred.stlouisfed.org/series/DFII10, https://fred.stlouisfed.org/series/DFF, https://fred.stlouisfed.org/series/WALCL
- Bureau of Labor Statistics, Consumer Price Index: https://www.bls.gov/cpi/
- Board of Governors of the Federal Reserve System, Federal Open Market Committee: https://www.federalreserve.gov/monetarypolicy/fomc.htm
- Cboe, VIX Index methodology: https://www.cboe.com/tradable_products/vix/vix_index_methodology/

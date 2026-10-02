---
{
  "title": "Inflation Regimes: CPI, PCE, Breakevens, Real Yields and What 2021-2023 Did to Stocks, Bonds and Gold",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The 10-year breakeven inflation rate (FRED T10YIE) is:", "opts": ["The nominal 10-year Treasury yield minus the 10-year TIPS yield: the inflation rate at which the two bonds return the same", "Last year's CPI", "The Fed's inflation target", "The 10-year TIPS yield"], "correct": 0, "explain": "It is a market price, updated daily. Its peak in the 2021-2023 episode was 3.02% on 2022-04-21, while CPI inflation went on to 9.0%: the bond market priced the spike as temporary."},
    {"q": "Between 2021-12-31 and 2022-12-30 the 10-year real yield (DFII10) went from -1.04% to +1.58%. Over calendar 2022, SPY returned -18.2%, TLT -31.2% and GLD -0.8%. Which variable best explains the pattern across all three?", "opts": ["CPI, because it peaked in June", "The VIX, which never exceeded 37", "The yield curve", "The real yield: a 2.6-point rise in the after-inflation price of money repriced long bonds most, equities second, and gold, which competes with real yields for the store-of-value role, was roughly flat because demand for an inflation hedge offset much of the real-yield and dollar headwind"], "correct": 3, "explain": "The CPI print was known to be high all year; what changed was what the market demanded to hold a real claim. Long-duration assets fell in proportion to their duration."},
    {"q": "CPI year-on-year peaked at 9.0% in June 2022 (BLS, FRED CPIAUCSL as revised) and PCE at 7.2% the same month. Why do the two differ?", "opts": ["One is monthly and one quarterly", "PCE excludes food and energy", "Different baskets and weights: PCE covers a broader set of expenditures including those paid on consumers' behalf, updates its weights continuously, and gives housing a smaller share", "CPI is not seasonally adjusted"], "correct": 2, "explain": "Both are monthly and both have core versions. The structural difference is the basket and weighting; the Fed targets PCE, which has run about half a point below CPI in this period."},
    {"q": "The monthly correlation between GLD's return and the monthly change in the 10-year real yield from January 2005 to September 2026 was -0.46. In 2022 alone it was -0.45, the real yield rose 2.62 points, and yet GLD returned -0.8%, not a large loss. The most defensible reading is:", "opts": ["The correlation is spurious", "The correlation held in 2022 (it was -0.45), but a monthly correlation of -0.46 explains only about a fifth of gold's variance, so other drivers, including the dollar and the inflation hedge demand, can dominate the annual total", "Gold is uncorrelated with real yields", "Gold went up in 2022"], "correct": 1, "explain": "The square of -0.46 is 0.21. Real yields are the single most important driver of gold in this sample and still leave four fifths of the variance to everything else."},
    {"q": "From SPY's 2022 low (2022-10-12) to 2023-12-29, SPY returned +36.0%, GLD +22.6% and TLT +2.7%, while the real yield rose further to +1.72% and CPI fell from 7.8% to 3.3%. What regime transition does this describe?", "opts": ["A recession", "A return to the 2010s", "Stagflation", "From inflation shock to disinflation with growth intact: falling inflation, still-high real yields, equities and gold recovering, long bonds not"], "correct": 3, "explain": "Disinflation with positive growth is a distinct state from the 2022 shock. Bonds did not recover because the level of real yields stayed high; equities and gold recovered because the direction of inflation turned."}
  ],
  "task": "Compute CPI year-on-year for the latest month from CPIAUCSL by dividing by the observation dated twelve months earlier, and write down the same month's T10YIE and DFII10 next to it."
}
---

## Two measures of the past, two of the future

Inflation regimes are defined by the interaction of what prices did and what the market expects them to do. The past is measured by the Consumer Price Index (BLS, monthly, released about two weeks after the month ends, FRED CPIAUCSL) and the PCE price index (BEA, monthly, released about a month after, FRED PCEPI). Year-on-year inflation is the index divided by its value twelve months earlier, minus one. FRED's CPI series has no observation for October 2025, so compute the ratio on dates, not on row offsets, or a twelve-row lag will silently become thirteen months.

The two indexes differ in basket and weights. CPI is built from urban consumer out-of-pocket spending with a large shelter weight; PCE covers all personal consumption including spending on consumers' behalf (employer health insurance, for instance), re-weights continuously as spending shifts, and gives shelter a smaller share. The Fed's 2% target is on PCE. In June 2022 CPI inflation was 9.0% and PCE 7.2%; in August 2026 they were 3.4% and 3.4%.

The future is priced in the Treasury market. A 10-year nominal Treasury pays a fixed coupon; a 10-year TIPS pays a coupon on a principal that grows with CPI. The TIPS yield (FRED DFII10) is the real yield, the return over inflation an investor accepts to hold a riskless real claim. The nominal yield minus the real yield is the breakeven (FRED T10YIE), the inflation rate at which both bonds return the same. If you think inflation will exceed the breakeven, TIPS are the better buy; if not, nominals. The breakeven is therefore the market's expected inflation plus a risk premium, and its daily movement is the fastest reading of the inflation axis you can get.

## The four inflation states

Combine the direction of realised inflation with the direction of the real yield and you get four states worth naming. Rising inflation with falling or negative real yields (2020-2021) is the state in which everything with duration rallies: the real cost of money is falling even as prices rise. Rising inflation with rising real yields (2022) is the state in which everything with duration falls at once, and it is the one the stock-bond diversification of the previous twenty years was not built for. Falling inflation with high real yields (2023-2024) favours equities and gold over long bonds. Falling inflation with falling real yields (2019, 2024 second half) is the classic easing state, good for bonds and usually for equities.

The variable doing the work in each state is the real yield. CPI tells you the state you were in; the real yield tells you what the market is charging for it now.

## What 2021-2023 did

The episode in numbers. CPI year-on-year: 1.4% in January 2021, 4.1% in April, 7.2% in December, 9.0% at the June 2022 peak, 6.4% in December 2022, 3.1% in June 2023, 3.3% in December 2023. The breakeven ran ahead and then stopped: 1.99% at the end of 2020, 2.56% at the end of 2021, a peak of 3.02% on 2022-04-21 (two months before the CPI peak), 2.30% at the end of 2022. The market never priced the spike as permanent. What it did reprice was the real yield: -1.06% at the end of 2020, -1.19% at the low on 2021-08-03, -1.04% at the end of 2021, +0.65% on 2022-06-30, +1.58% on 2022-12-30, +2.49% at the 2023-10-19 high, +1.72% at the end of 2023.

The asset returns follow the real yield, not the CPI. In 2021, with CPI rising from 1.4% to 7.2% and the real yield essentially unchanged at -1.04%, SPY returned +28.7%, TLT -4.6%, GLD -4.1%. In 2022, with CPI peaking and the real yield rising 2.62 points, SPY returned -18.2%, TLT -31.2%, GLD -0.8%. In 2023, with CPI halving and the real yield still rising to +1.72%, SPY returned +26.2%, TLT +2.8%, GLD +12.7%. Over the three years together, from 2020-12-31 to 2023-12-29: SPY +32.9%, TLT -32.6%, GLD +7.2%.

TLT's drawdown from its 2020-08-04 peak to its 2023-10-19 trough was -48.4%, the largest in the fund's history, and it was inflicted by a 3.5-point rise in the real yield on a bond with roughly seventeen years of duration. Nothing about the CPI print, which was public and rising for eighteen months before TLT's worst stretch, would have told you the size of that loss. The real yield would have.

## Gold and real yields

Gold pays nothing, so the opportunity cost of holding it is the real yield on the riskless alternative. That gives a clean hypothesis: gold should fall when real yields rise. The worked example measures it: the correlation between GLD's monthly return and the monthly change in DFII10 from January 2005 to September 2026 (261 months) is -0.46, and in 2022 alone it is -0.45. The relationship held in 2022 exactly as it held before. What it did not do is determine the year: with real yields up 2.62 points, GLD finished 2022 down only 0.8%, because the dollar's 8.2% rise and the demand for an inflation hedge pulled in opposite directions and a -0.46 correlation leaves most of the variance to other things. Correlations describe distributions, not years.

## Worked example

Data: FRED CPIAUCSL, PCEPI, T10YIE, DFII10, DGS10, pulled 2026-09-30. Yahoo Finance chart API daily bars for SPY, TLT, GLD, USO and DX-Y.NYB, adjusted close for the three funds, close for the dollar index (an index, no dividends), last full session 2026-09-29. Calendar-year return is the adjusted close on the last session of the year divided by the adjusted close on the last session of the previous year, minus one. Window returns use the nearest prior session to each date.

CPI year-on-year at the June 2022 peak: CPIAUCSL(2022-06) / CPIAUCSL(2021-06) - 1 = 294.957 / 270.654 - 1 = 8.98%, reported as 9.0%. (The July 2022 press release said 9.1%; FRED's current vintage reflects later seasonal-factor revisions. Quote the vintage you used.) PCE: PCEPI(2022-06) / PCEPI(2021-06) - 1 = 7.22%.

Real-yield change over 2022: DFII10 on 2022-12-30 minus DFII10 on 2021-12-31 = 1.58 - (-1.04) = +2.62 percentage points. The largest 126-session rise in the series was 2.20 points, ending 2022-09-30.

Calendar-year returns (SPY, TLT, GLD, USO, DXY): 2020: +18.3%, +18.2%, +24.8%, -67.8%, -6.7%. 2021: +28.7%, -4.6%, -4.1%, +64.7%, +6.4%. 2022: -18.2%, -31.2%, -0.8%, +29.0%, +8.2%. 2023: +26.2%, +2.8%, +12.7%, -4.9%, -2.1%. 2024: +24.9%, -8.1%, +26.7%, +13.4%, +7.1%. 2025: +17.7%, +4.2%, +63.7%, -8.5%, -9.4%.

Window returns: 2020-12-31 to 2022-06-30 (the CPI run-up): SPY +3.0%, TLT -25.5%, GLD -5.6%, USO +143.4%, DXY +16.4%. 2021-12-31 to 2022-10-12 (SPY's peak-to-trough year): SPY -24.1%, TLT -31.2%, GLD -8.8%, USO +30.5%, DXY +18.4%. 2022-10-12 to 2023-12-29 (disinflation): SPY +36.0%, TLT +2.7%, GLD +22.6%, USO -6.0%, DXY -10.6%.

Gold versus real yields: for each month from 2005-01 to 2026-09, take GLD's last adjusted close and DFII10's last observation; compute GLD's monthly return and the monthly change in DFII10 (261 pairs); the Pearson correlation is -0.46. Restricting to the twelve months of 2022 gives -0.45. The square of -0.46 is 0.21: about a fifth of GLD's monthly variance is associated with real-yield changes in this sample.

## Table

| Date | CPI YoY | PCE YoY | 10y nominal | 10y breakeven | 10y real | SPY calendar-year TR | TLT | GLD |
|---|---|---|---|---|---|---|---|---|
| 2020-12-31 | 1.3% | 1.3% | 0.93 | 1.99 | -1.06 | 2020: +18.3% | +18.2% | +24.8% |
| 2021-12-31 | 7.2% | 6.0% | 1.52 | 2.56 | -1.04 | 2021: +28.7% | -4.6% | -4.1% |
| 2022-06-30 | 9.0% | 7.2% | 2.98 | 2.33 | +0.65 | (H1 2022 window: SPY +3.0% from 2020-12-31) | | |
| 2022-12-30 | 6.4% | 5.6% | 3.88 | 2.30 | +1.58 | 2022: -18.2% | -31.2% | -0.8% |
| 2023-12-29 | 3.3% | 2.9% | 3.88 | 2.16 | +1.72 | 2023: +26.2% | +2.8% | +12.7% |
| 2024-12-31 | 2.9% | 2.6% | 4.58 | 2.34 | +2.24 | 2024: +24.9% | -8.1% | +26.7% |
| 2026-09-29 | 3.4% (Aug) | 3.4% (Aug) | 5.26 | 2.35 | +2.91 | 2026 YTD: +12.9% | -7.5% | -3.4% |

CPI and PCE year-on-year are for the month containing the date (December for year-ends). Yields are FRED daily values on the date. Returns are Yahoo adjusted-close total returns for the calendar year ending on the date.

Read the real-yield column against the TLT column: TLT's two losing years in the table are the two in which the real yield rose (2022, +2.62 points, TLT -31.2%; 2024, +0.52 points from an already high base, TLT -8.1%), and the size of the loss scales with the size of the rise. Read it against GLD: the relationship is looser, and 2024-2025, with real yields above 2% and GLD up 26.7% then 63.7%, is a reminder that the real-yield model of gold is a partial one.

## Sources

- Bureau of Labor Statistics, Consumer Price Index: https://www.bls.gov/cpi/ ; Bureau of Economic Analysis, Personal Consumption Expenditures Price Index: https://www.bea.gov/data/personal-consumption-expenditures-price-index
- FRED: https://fred.stlouisfed.org/series/CPIAUCSL, https://fred.stlouisfed.org/series/PCEPI, https://fred.stlouisfed.org/series/T10YIE, https://fred.stlouisfed.org/series/DFII10
- U.S. Department of the Treasury, Treasury Inflation-Protected Securities (TIPS): https://www.treasurydirect.gov/marketable-securities/tips/
- Erb, C. B. and Harvey, C. R. (2013), "The Golden Dilemma", Financial Analysts Journal 69(4), https://doi.org/10.2469/faj.v69.n4.1

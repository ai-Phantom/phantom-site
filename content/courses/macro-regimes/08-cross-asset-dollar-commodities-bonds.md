---
{
  "title": "Cross-Asset: The Dollar, Commodities and the 2022 Stock-Bond Correlation Flip",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The correlation of SPY and TLT daily returns was -0.40 from 2002-07-31 to 2021-12-31 and +0.11 from 2022-01-01 to 2026-09-29. The 36-month correlation of monthly returns went from -0.33 at the end of 2021 to +0.60 at the end of 2023. What changed?", "opts": ["The dominant shock changed from growth to inflation: when growth is the fear, bonds rally as stocks fall; when inflation is the fear, both fall together because the real yield is rising", "Nothing; the numbers are noise", "TLT changed its holdings", "Stocks became bonds"], "correct": 0, "explain": "The sign of the stock-bond correlation is a regime variable in itself. It was negative for two decades of low and stable inflation and turned positive when inflation became the thing the market feared."},
    {"q": "A daily-rebalanced 60% SPY / 40% TLT portfolio returned -22.8% in 2022, worse than SPY alone (-18.2%). Why?", "opts": ["TLT is riskier than SPY", "Rebalancing is bad", "TLT fell 31.2% in 2022 while its correlation with SPY turned positive, so the bond allocation added to the loss instead of offsetting it", "The portfolio was leveraged"], "correct": 2, "explain": "Diversification is a property of the correlation, not of the asset. When the correlation flips, the hedge becomes a second exposure to the same shock."},
    {"q": "The dollar index rose from 90.0 on 2021-05-28 to 114.1 on 2022-09-27. Over 2006-2026 the monthly correlation of DXY with GLD was -0.45 and with SPY -0.45. What does the dollar's rise in 2022 tell you about the regime?", "opts": ["The dollar always rises in bear markets", "A rising dollar with rising real yields and falling stocks and bonds is the signature of US-led tightening: capital moves to the highest real rate; gold, priced in dollars, is squeezed from both sides", "The dollar is uncorrelated with everything", "Gold should have risen"], "correct": 1, "explain": "GLD fell only 0.8% in 2022 despite that squeeze, which is why the lesson calls the dollar a partial explanation. The correlation is -0.45, not -1."},
    {"q": "USO (crude oil) returned +64.7% in 2021, +29.0% in 2022 and -4.9% in 2023. Its monthly correlation with SPY over 2006-2026 was +0.33. Which role does crude play on the axes?", "opts": ["A pure inflation hedge", "A bond substitute", "A dollar proxy", "A growth asset with an inflation kicker: positively correlated with equities most of the time, but it led the 2021-2022 inflation regime and peaked (2022-06-08) in the month CPI did"], "correct": 3, "explain": "Oil is an input cost and a demand indicator at once. In 2022 the inflation side dominated; in 2020, when it fell 67.8%, the growth side did."},
    {"q": "The 60-day rolling correlation of SPY and TLT was -0.65 in October 2002 and +0.50 in September 2026. Why does the lesson use a rolling window rather than a single number?", "opts": ["Because rolling windows are always better", "Because daily data is noisy", "Because the correlation is itself a regime variable that has changed sign; a single number over 24 years (-0.30) describes neither the 2010s nor the 2020s", "Because TLT is illiquid"], "correct": 2, "explain": "The full-sample correlation of -0.30 is a weighted average of two very different states. The rolling series lets you see which state you are in now."}
  ],
  "task": "Compute the 60-session rolling correlation of SPY and TLT daily returns for the latest session and note whether it is positive or negative."
}
---

## Why cross-asset matters for a single-market trader

Even if you only ever trade SPY, the other assets tell you which regime the index is in. The dollar tells you where global capital is moving. Commodities tell you whether the inflation axis is being driven by demand or by supply. The bond market's co-movement with equities tells you whether the shock the market fears is a growth shock or an inflation shock. None of these is a trading signal for SPY; all of them are regime evidence.

## The dollar

The US dollar index (DXY, Yahoo `DX-Y.NYB`) measures the dollar against a basket of six currencies dominated by the euro. It rises when US real rates rise relative to the rest of the world and when investors seek the safety of dollar assets; it fell 8.4% in 2007 and rose 6.0% in 2008, fell 6.7% in 2020 and rose 8.2% in 2022, rose 7.1% in 2024 and fell 9.4% in 2025.

Over May 2006 to September 2026 (245 months), the monthly-return correlation of DXY with SPY was -0.45, with GLD -0.45, with USO -0.28 and with TLT -0.10. A rising dollar is, on average, bad for equities and bad for gold, and the 2022 rise from 90.0 (2021-05-28) to 114.1 (2022-09-27) is the reason gold went nowhere in an inflation year: gold is priced in dollars, and a dollar up 27% is a gold price down in every other currency. The dollar's fall from 110.0 (2025-01-13) to 101.4 (2026-09-29) is part of the explanation of gold's +63.7% in 2025.

## Commodities

Crude oil (USO, Yahoo, from 2006-04-10) is the commodity most tightly linked to the inflation axis and, at the same time, to growth. Its monthly correlation with SPY over the same 245 months was +0.33, the highest of any cross-asset pair in the lesson's table: oil is a growth asset most of the time. But it led the inflation regime. USO returned +64.7% in 2021, when CPI went from 1.4% to 7.2%, and +29.0% in 2022, peaking on 2022-06-08 in the same month CPI peaked. In 2020 the growth side dominated: USO fell 67.8% for the year, with a low on 2020-04-28.

Gold is not a commodity in the same sense; its supply is a stock, not a flow, and lesson 4 showed its main driver is the real yield (-0.46 monthly correlation with the change in DFII10). Its correlation with SPY over the 245 months was +0.08, effectively zero, which is what makes it a diversifier in a way oil is not.

## The stock-bond correlation

For most of the twenty years before 2022, US Treasuries were the hedge for US equities. The daily-return correlation of SPY and TLT was -0.32 in 2003, -0.48 in 2008, -0.71 in 2011, -0.46 in 2019, -0.48 in 2020. When stocks fell, bonds rallied, because the thing stocks were falling on was a growth scare, and a growth scare means lower rates.

In 2022 the sign flipped: +0.08 for the year in daily returns, +0.51 in monthly returns, and it stayed positive: +0.13 (2023), +0.06 (2024), +0.10 (2025), +0.36 (2026 to date). The 36-month correlation of monthly returns, which smooths the daily noise, went from -0.33 at the end of 2021 to +0.15 at the end of 2022, +0.60 at the end of 2023, +0.68 at the end of 2024, +0.66 at the end of 2025 and +0.49 in September 2026. The 60-day rolling daily correlation, which is what the chart plots, reached +0.16 in September 2022 and +0.23 in April 2024 after sitting below zero for essentially all of 2002-2021.

The mechanism is the inflation axis. When the market's fear is inflation, the shock that hurts equities (a higher real yield) hurts bonds at the same time and by more, because bonds have more duration. The correlation flips sign not because either asset changed but because the dominant shock did. And the consequence for a diversified portfolio is arithmetic: a daily-rebalanced 60/40 of SPY and TLT returned -22.8% in 2022, worse than SPY alone at -18.2%, because TLT's -31.2% arrived in the same direction.

The correlation is a regime variable in its own right, and a slow one. It changed sign once in the sample and has stayed flipped for four years. It tells you whether your bond allocation is a hedge or a second exposure, and it tells you which axis the market is currently trading on.

## Worked example

Data: Yahoo Finance chart API daily bars, current session dropped: SPY and TLT (aligned from 2002-07-31, TLT's first session, 6,081 common return days to 2026-09-29), GLD (from 2004-11-18), USO (from 2006-04-10), `DX-Y.NYB` (close, no dividends). Adjusted closes for the funds.

Daily correlation by calendar year is the Pearson correlation of the two funds' daily returns within the year. Full sample 2002-07-31 to 2026-09-29: -0.30. Pre-2022: -0.40. From 2022-01-01: +0.11. By year: 2003 -0.32, 2004 -0.04, 2005 +0.01, 2006 +0.05, 2007 -0.40, 2008 -0.48, 2009 -0.32, 2010 -0.55, 2011 -0.71, 2012 -0.65, 2013 -0.21, 2014 -0.46, 2015 -0.37, 2016 -0.37, 2017 -0.33, 2018 -0.28, 2019 -0.46, 2020 -0.48, 2021 -0.14, 2022 +0.08, 2023 +0.13, 2024 +0.06, 2025 +0.10, 2026 +0.36.

Monthly-return correlation by year (12 observations each, so noisy): 2021 +0.18, 2022 +0.51, 2023 +0.87, 2024 +0.74, 2025 +0.03. The 36-month trailing correlation of monthly returns at each year-end: 2007 -0.33, 2012 -0.78, 2019 -0.34, 2021 -0.33, 2022 +0.15, 2023 +0.60, 2024 +0.68, 2025 +0.66, 2026-09 +0.49.

The 60-session rolling correlation is the Pearson correlation of the 60 daily returns ending on each session; the chart samples it on the last session of each month, 288 points from 2002-10 to 2026-09. First point -0.65; 2008-11 -0.52; 2013-06 -0.24; 2022-01 -0.33; 2022-09 +0.16; 2024-04 +0.23; last point +0.50.

The 60/40 calculation: for each session in 2022, the portfolio return is 0.6 times SPY's daily return plus 0.4 times TLT's, compounded over the 251 sessions of the year (daily rebalancing, no costs): -22.8%. SPY alone: -18.2%; TLT alone: -31.2%. Maximum drawdown within 2022: SPY -24.5% (2022-01-03 to 2022-10-12), TLT -34.9%.

Dollar and commodity correlations: monthly returns from 2006-05 to 2026-09, 245 months. DXY-GLD -0.45, DXY-USO -0.28, DXY-SPY -0.45, DXY-TLT -0.10, GLD-SPY +0.08, USO-SPY +0.33. DXY levels: 90.03 (2021-05-28), 114.11 (2022-09-27, the 2022 high), 103.52 (2022-12-30), 109.96 (2025-01-13), 101.37 (2026-09-29). USO: 2022 high on 2022-06-08; 2020 low on 2020-04-28.

## Chart

![60-session rolling correlation of SPY and TLT daily total returns, sampled at month-ends from October 2002 to September 2026, Yahoo Finance data; the zero line is drawn and November 2008, the 2013 taper tantrum, the September 2022 flip and April 2024 are annotated.](figures/stock-bond-correlation.svg)

Two things to read off the chart. First, the pre-2022 series spends almost all of its time below zero and dips deepest in the crises (2008, 2011, 2020): the hedge worked best when it was needed most, which is the property a hedge is supposed to have. Second, the post-2022 series oscillates around and above zero with no return to the old state. If you are running a stock-bond portfolio, the chart is telling you which regime your diversification assumption belongs to.

## Sources

- Yahoo Finance historical data: https://finance.yahoo.com/quote/TLT/history/, https://finance.yahoo.com/quote/GLD/history/, https://finance.yahoo.com/quote/USO/history/, https://finance.yahoo.com/quote/DX-Y.NYB/history/
- Federal Reserve Board, "Nominal/Real Indexes: Trade-Weighted Dollar": https://www.federalreserve.gov/releases/h10/summary/
- Campbell, J. Y., Pflueger, C. and Viceira, L. M. (2020), "Macroeconomic Drivers of Bond and Equity Risks", Journal of Political Economy 128(8), https://doi.org/10.1086/707766
- Ilmanen, A. (2003), "Stock-Bond Correlations", Journal of Fixed Income 13(2), https://doi.org/10.3905/jfi.2003.319353

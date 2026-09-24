---
{
  "title": "Volatility and Correlation: BTC and ETH Against Equities",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In 2022 the annualised realised volatility of daily closes was 64.1% for BTC and 24.3% for SPY. A one-standard-deviation day was therefore", "opts": ["3.4% for BTC and 1.5% for SPY", "6.4% and 2.4%", "1.7% and 1.0%", "The same for both"], "correct": 0, "explain": "64.1 over the square root of 365 is 3.36%; 24.3 over the square root of 252 is 1.53%. BTC trades every day, so it is scaled by 365."},
    {"q": "The correlation of BTC and QQQ daily returns in 2022 was 0.58. In 2023 it was 0.18. What does that pair of numbers tell you?", "opts": ["BTC is always a tech stock", "BTC is never correlated with stocks", "Correlation is regime-dependent: high in the 2022 rate-driven sell-off, low in the year after", "The data is wrong"], "correct": 2, "explain": "Correlation is not a constant of the asset. In 2022 both fell on the same macro driver; in 2023 they did not share one."},
    {"q": "The correlation between BTC and ETH daily returns has been", "opts": ["Near zero", "Between 0.80 and 0.91 every year from 2022 to 2026", "Negative", "Exactly 1"], "correct": 1, "explain": "Holding both is one bet on the crypto factor with two tickers. Diversification inside crypto is close to nil."},
    {"q": "Why does scaling BTC's daily volatility by the square root of 365 rather than 252 matter?", "opts": ["It does not", "BTC has 365 return observations a year, so using 252 would understate annual volatility by about 17%", "252 is only for bonds", "365 overstates volatility"], "correct": 1, "explain": "The square root of 252 over 365 is 0.83. The convention must match the number of trading days the series actually has."},
    {"q": "A portfolio adds BTC as a 'diversifier' in early 2022. The numbers say that during that year's equity drawdown it", "opts": ["Rose while stocks fell", "Fell 65% with a 0.58 correlation to the Nasdaq-100 ETF, amplifying the loss", "Was flat", "Was uncorrelated"], "correct": 1, "explain": "BTC's 2022 calendar return was minus 65.3% against QQQ's roughly minus 33%; it was a levered version of the same trade."}
  ],
  "task": "Compute the 30-day realised volatility of BTC from daily closes and write down the resulting one-day standard deviation in dollars at today's price."
}
---

## What volatility is, and the convention that changes it

Realised volatility is the standard deviation of daily log returns, annualised by multiplying by the square root of the number of return observations in a year. Equities have about 252. Crypto trades every calendar day, so its series has 365, and the annualisation factor is √365 = 19.1 rather than √252 = 15.9. Scaling a crypto series by 252 understates its annual volatility by 17%, and comparing a 252-scaled crypto number to a 252-scaled equity number is not comparing like with like. Every number in this lesson uses 365 for BTC and ETH and 252 for SPY and QQQ, all computed from Yahoo Finance daily closes pulled on 2026-09-24.

## Chart

![Annualised realised volatility of daily log returns by calendar year, BTC-USD scaled by the square root of 365 and SPY by the square root of 252, computed from Yahoo Finance daily closes pulled 2026-09-24. BTC: 64.1%, 43.3%, 53.0%, 41.9%, 46.8% for 2022 to 2026 year to date; SPY: 24.3%, 13.2%, 12.6%, 19.3%, 13.3%.](figures/realised-vol-btc-vs-spy.svg)

The ratio is what to remember. BTC's realised volatility has run between 2.2 and 4.2 times the S&P 500 ETF's every year in the sample, and ETH's higher still: 87.1% in 2022, 74.7% in 2025, 63.0% in 2026 year to date. "Crypto is volatile" is not a slogan; it is a multiplier of about three on every risk number you have learned to use for equities.

## Worked example

Compute 2022, the year that answered the question of whether crypto diversifies an equity portfolio.

**Step 1: realised volatility.** Take the 365 daily BTC-USD closes for 2022 from Yahoo's chart endpoint, giving 364 log returns r_t = ln(P_t ÷ P_{t−1}). Their population standard deviation is 0.03355. Annualise: 0.03355 × √365 = 0.03355 × 19.105 = 0.641, or 64.1%. One daily standard deviation was 3.36%, which at the year's opening price of about $46,300 was $1,550 a day, and at the November low near $16,000 was $540.

SPY's 250 log returns in 2022 have a standard deviation of 0.01531; × √252 = 0.01531 × 15.875 = 0.243, or 24.3%. Daily sigma 1.53%. BTC was 2.6 times as volatile as the index and 2.2 times as volatile as the Nasdaq-100 ETF (QQQ, 32.1%).

**Step 2: the drawdown.** BTC's peak close was $67,566.83 on 2021-11-08 and its trough close $15,787.28 on 2022-11-21: 15,787.28 ÷ 67,566.83 − 1 = −76.6%. Over the same cycle QQQ fell from a $403.99 close on 2021-11-19 to $260.10 on 2022-12-28, −35.6%, and SPY from $477.71 (2022-01-03) to $356.56 (2022-10-12), −25.4%. The 2022 calendar-year return was −65.3% for BTC; its worst single day was −17.4%.

**Step 3: correlation.** Align BTC and QQQ on the 250 dates in 2022 when both have a close (BTC's weekend bars are dropped, which slightly understates BTC's total variance but is the only way to pair the series). The Pearson correlation of the paired daily log returns is 0.58. Against SPY it is 0.56. The first half of the year gives 0.60 and the second half 0.56, so the relationship was stable across the year, not a product of one week.

What that means in portfolio terms: a position with 0.58 correlation and 2.2 times the volatility of QQQ behaves, in the part of its variance shared with QQQ, like about 1.3 units of QQQ (beta ≈ ρ × σ_BTC ÷ σ_QQQ = 0.58 × 64.1 ÷ 32.1 = 1.16, before adjusting for the weekend bars). Adding it to a Nasdaq-heavy portfolio in January 2022 added leverage to the existing bet, plus a large idiosyncratic component that also went down.

**Step 4: the years after.** The same computation for 2023 gives BTC–QQQ correlation of 0.18; 2024, 0.33; 2025, 0.46; 2026 year to date, 0.42. Against SPY: 0.15, 0.38, 0.42, 0.45. The 2022 reading was the highest in the sample and it coincided with the one year in which a single macro driver, the rate-hiking cycle, moved both assets. Since then the number has drifted in the 0.3 to 0.5 range: not zero, not one, and not stable enough to build an allocation on.

**Step 5: inside crypto.** BTC–ETH daily correlation: 0.90 in 2022, 0.83 in 2023, 0.80 in 2024, 0.82 in 2025, 0.91 in 2026 year to date. Holding both is one position.

## Reading these numbers as a trader

Volatility sets the size of everything else. A stop 2% away on an equity is 1.3 daily sigmas; the same 2% on BTC is 0.6 sigmas and will be hit by noise most weeks. Leverage is a distance (lesson 8), and the distance must be measured in the asset's own sigma, which for BTC has not been below 2.2% a day in any year of the sample.

Correlation sets what a hedge is worth. BTC and ETH hedge each other almost perfectly, so a long-BTC short-ETH position is a small residual, not a directional trade. BTC and equities correlate enough in a macro sell-off that an equity trader who adds crypto for diversification should assume it will fall with the Nasdaq when the Nasdaq falls for macro reasons, and then fall further on its own. Regulators reached the same conclusion from the same data; the IMF's January 2022 working paper on crypto-equity spillovers documents the rise in co-movement from the pre-2020 near-zero levels, and the Federal Reserve's November 2022 Financial Stability Report discusses the 2022 crypto drawdown alongside the broader tightening.

## A caution about the estimates

Every number here is a realised statistic over a stated window. Correlation over 250 daily observations has a standard error of roughly 0.05 to 0.06, so 0.58 and 0.56 are not distinguishable, and 0.18 and 0.33 barely are. Realised volatility over 30 days is noisier still: BTC's 30-day figure on 2026-09-24 was 41.8%, against 46.8% year to date, and it will read differently next month. Use the numbers to set the scale of your stops and sizes; do not use the third decimal place of any of them.

## From volatility to a position size

The number you will use most often is the one-day dollar standard deviation of a position, because it is what a stop, a margin buffer and a risk budget are all measured in. Compute it as position value × daily sigma. On 2026-09-24, with BTC at $84,242 and the year-to-date daily sigma of 2.45%, 1 BTC has a one-day standard deviation of 84,242 × 0.0245 = $2,064. Ten BTC is $20,640 a day. If your rule is that a one-sigma day may cost at most 1% of a $250,000 account, or $2,500, the position size is 2,500 ÷ 2,064 = 1.2 BTC, about $102,000, with no leverage at all. The same rule on SPY, with a daily sigma of 13.3% ÷ √252 = 0.84%, allows 2,500 ÷ 0.0084 = $298,000 of exposure, three times as much. That ratio, roughly three to one, is the practical content of every volatility comparison in this lesson: whatever size you would hold in an index ETF, hold a third of it in BTC for the same daily risk, and less than that if the position is levered or the window includes a 2022.

Correlation enters when there is more than one position. Two positions of equal daily sigma with correlation 0.9, BTC and ETH, have a combined sigma of √(1 + 1 + 2 × 0.9) = 1.95 times one position's, almost the full sum; the same pair at correlation 0.3 would be 1.61 times. Diversifying BTC with ETH reduces risk by about 2%; diversifying it with an asset at 0.3 reduces it by 20%. Treat the two coins as one line in the risk budget.

## Sources

- Yahoo Finance chart API, BTC-USD daily bars, 5-year range: https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=5y&interval=1d
- Yahoo Finance chart API, QQQ and SPY daily bars, 5-year range: https://query1.finance.yahoo.com/v8/finance/chart/QQQ?range=5y&interval=1d
- Tara Iyer, "Cryptic Connections: Spillovers between Crypto and Equity Markets", IMF Working Paper 2022/001, January 2022: https://www.imf.org/en/Publications/WP/Issues/2022/01/11/Cryptic-Connections-Spillovers-between-Crypto-and-Equity-Markets-511776
- Board of Governors of the Federal Reserve System, Financial Stability Report, November 2022: https://www.federalreserve.gov/publications/files/financial-stability-report-20221104.pdf

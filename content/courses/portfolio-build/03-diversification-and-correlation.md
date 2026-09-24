---
{
  "title": "Diversification and Correlation",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Five stocks each have 35% volatility. If their average pairwise correlation is 0.6, the equal-weight portfolio's volatility is closest to", "opts": ["7%", "21%", "29%", "35%"], "correct": 2, "explain": "Portfolio variance = (1/5)(0.35²) + (4/5)(0.6)(0.35²) = 0.0245 + 0.0588 = 0.0833, so volatility is √0.0833 ≈ 28.9%. Five tech stocks remove only about six points of volatility."},
    {"q": "As the number of equally weighted holdings grows very large, portfolio volatility approaches", "opts": ["Zero", "The average stock's volatility", "√(average correlation) × average stock volatility", "The volatility of the largest holding"], "correct": 2, "explain": "The 1/n term vanishes and what remains is ρ × σ², so the floor is σ × √ρ. With ρ = 0.6 and σ = 35% the floor is about 27%; with ρ = 0.2 it is about 15.7%. Correlation, not count, sets the floor."},
    {"q": "Which statement about correlation in market crises is supported by the research cited in this lesson?", "opts": ["Correlations between stocks fall sharply in crashes, helping diversification", "Correlations between equity markets rise in large down moves, so diversification across stocks helps least when needed most", "Correlation is constant over time", "Only crypto correlations change"], "correct": 1, "explain": "Longin and Solnik (2001) and Ang and Chen (2002) both document that correlations rise in large negative moves. Diversification across stocks reduces ordinary volatility but does not protect against a broad crash; only assets with genuinely different drivers do that."},
    {"q": "Between 2010 and 2020 the correlation of SPY and TLT daily returns was roughly negative. In 2022 it turned positive. What does this tell you?", "opts": ["Bonds are useless", "Correlation is an estimate from a window of data and can change when the driver of returns changes, so a plan must not depend on a single historical value", "TLT was mispriced", "The 60/40 portfolio can never lose money"], "correct": 1, "explain": "In 2022 both stocks and long bonds fell because rising rates hit both at once. A diversifier's value depends on the regime; you should assume correlations can move against you and size accordingly."},
    {"q": "Statman (1987) and Campbell, Lettau, Malkiel and Xu (2001) suggest roughly how many stocks are needed to remove most diversifiable risk?", "opts": ["3 to 5", "10", "30 to 50", "500"], "correct": 2, "explain": "Statman put the figure at 30 to 40 for a well-diversified portfolio; Campbell and co-authors found that rising idiosyncratic volatility had pushed the number to around 50 by the late 1990s. A ten-stock portfolio still carries meaningful single-name risk unless the core is a broad fund."}
  ],
  "task": "Compute the correlation of monthly returns between your two largest holdings using at least 36 months of data."
}
---

## Why diversification is arithmetic, not opinion

Harry Markowitz's 1952 paper made one observation that still runs every serious portfolio: the risk of a portfolio is not the average risk of its holdings. It depends on how the holdings move together. Two assets that each swing 20% can combine into something that swings 20%, 14%, or almost nothing, depending on one number: their correlation.

Correlation runs from −1 to +1. At +1 two assets move in lockstep and combining them changes nothing. At 0 their moves are unrelated and some cancel. At −1 they move exactly opposite and the right mix cancels everything. Real assets sit mostly between 0 and +0.9, and the interesting work of building a portfolio happens in that range.

This lesson gives you the formula, works it with real tickers, and then explains the two ways correlation will disappoint you if you trust a single historical number.

## The formula

For two assets with weights w₁ and w₂, volatilities σ₁ and σ₂, and correlation ρ:

Portfolio variance = w₁²σ₁² + w₂²σ₂² + 2 w₁ w₂ ρ σ₁ σ₂

Portfolio volatility is the square root of that.

For n assets held in equal weights, each with volatility σ and average pairwise correlation ρ, the formula collapses to:

Portfolio variance = (1 ÷ n) σ² + (1 − 1 ÷ n) ρ σ²

Look at what happens as n grows. The first term shrinks toward zero; that is the diversifiable part. The second term approaches ρσ². So no matter how many holdings you add, volatility never falls below σ√ρ. The count of holdings removes the first term. Only low correlation lowers the floor.

## Worked example

Take five large technology stocks: AAPL, MSFT, GOOGL, AMZN and NVDA. Using daily returns over 2019 to 2023 and rounding, their annualised volatilities ran from roughly 30% (MSFT, AAPL) to 50% (NVDA), and their average pairwise correlation was about 0.6. To keep the arithmetic clean, use 35% volatility for each and ρ = 0.6. Your own figures will differ with the window; the shape of the result will not.

**Equal-weight portfolio of the five:**

- First term: (1 ÷ 5) × 0.35² = 0.2 × 0.1225 = 0.0245
- Second term: (1 − 0.2) × 0.6 × 0.1225 = 0.8 × 0.0735 = 0.0588
- Variance: 0.0245 + 0.0588 = 0.0833
- Volatility: √0.0833 = 28.9%

Five stocks at 35% each produced a portfolio at 28.9%. You removed about six points of volatility, and the floor for this group is 0.35 × √0.6 = 27.1%. Adding a sixth, tenth or fiftieth tech stock would take you from 28.9% toward 27.1% and no further. That is what "five tech stocks are not diversified" means in numbers: they share a driver, so they share most of their risk.

**Same five volatilities, but stocks from five different sectors with ρ = 0.2:**

- First term: 0.0245 (unchanged)
- Second term: 0.8 × 0.2 × 0.1225 = 0.0196
- Variance: 0.0441
- Volatility: √0.0441 = 21.0%

Same count, same individual volatilities, eight points less portfolio volatility, and the floor is now 0.35 × √0.2 = 15.7%. The difference between 28.9% and 21.0% came entirely from correlation.

**Add a bond fund.** Now take a two-asset mix: 80% in the five-sector stock basket (21.0% volatility) and 20% in BND, the Vanguard Total Bond Market ETF, with roughly 5% volatility and correlation to stocks of about 0.1 over 2010 to 2021.

- w₁²σ₁² = 0.64 × 0.0441 = 0.02822
- w₂²σ₂² = 0.04 × 0.0025 = 0.00010
- Cross term: 2 × 0.8 × 0.2 × 0.1 × 0.21 × 0.05 = 0.000336
- Variance: 0.02866
- Volatility: √0.02866 = 16.9%

A 20% bond allocation took the portfolio from 21.0% to 16.9%. Lesson 2 showed that volatility drag is half the variance, so this also lifts the compounded return relative to the arithmetic return by about (0.0441 − 0.0287) ÷ 2 = 0.77 points a year, partially offsetting the lower expected return of bonds.

## Table

Approximate correlations of daily returns, 2019 to 2023, rounded to one decimal. Compute your own before relying on any of them.

| | AAPL | MSFT | GOOGL | AMZN | NVDA | SPY | BND |
|---|---|---|---|---|---|---|---|
| AAPL | 1.0 | 0.7 | 0.6 | 0.6 | 0.6 | 0.8 | 0.1 |
| MSFT | 0.7 | 1.0 | 0.7 | 0.6 | 0.6 | 0.8 | 0.1 |
| GOOGL | 0.6 | 0.7 | 1.0 | 0.6 | 0.5 | 0.7 | 0.1 |
| AMZN | 0.6 | 0.6 | 0.6 | 1.0 | 0.5 | 0.7 | 0.1 |
| NVDA | 0.6 | 0.6 | 0.5 | 0.5 | 1.0 | 0.7 | 0.0 |
| SPY | 0.8 | 0.8 | 0.7 | 0.7 | 0.7 | 1.0 | 0.1 |
| BND | 0.1 | 0.1 | 0.1 | 0.1 | 0.0 | 0.1 | 1.0 |

Two things to read off the table. First, each of the five stocks correlates more strongly with SPY than with the others, because the index is what they have in common; a holder of all five has largely bought the index with extra single-name noise. Second, BND sits near zero against everything, which is the property that made the bond calculation above work.

## How many stocks is enough

Evans and Archer, in 1968, found that most of the diversifiable variance was gone by about 10 randomly chosen stocks. Meir Statman revisited the question in 1987 with a cost-benefit framing and put the figure at 30 to 40. Campbell, Lettau, Malkiel and Xu showed in 2001 that individual-stock volatility had roughly doubled between the 1960s and the 1990s while market volatility had not, so the number of stocks required to reach a given level of diversification had risen to around 50.

The practical reading for a first portfolio: a handful of individual stocks does not diversify you, and even ten do not fully. That is not an argument against holding single names. It is the argument for putting a broad fund at the core, which gives you the 500 or 3,500 names at once, and treating individual stocks as bounded additions on top. Lesson 6 is built on that split.

## Two ways correlation will let you down

**Correlations rise when markets fall.** François Longin and Bruno Solnik, using 38 years of monthly data across international equity markets, showed that correlation increases in large negative moves and not in large positive ones. Andrew Ang and Joseph Chen found the same asymmetry within US stocks. In October 2008, almost every equity market, most commodities and most credit fell together; the 0.6 in the table above was closer to 0.9 that month. Diversification across stocks reduces ordinary, day-to-day volatility. It offers much less protection against the event you most want protection from. Only assets with a genuinely different driver, such as Treasury bonds and cash, kept their value that year.

**Correlations change regime.** The SPY–TLT correlation, roughly −0.3 over 2010 to 2020, turned positive in 2022, when the S&P 500 lost 18.1% and TLT lost over 30% because both were repriced by the same rise in interest rates. Anyone who had sized their bond allocation on the assumption that bonds always rise when stocks fall was surprised twice. A correlation estimate is a description of a window of history, and the regime that produced it can end.

The defence against both is the same: do not build a portfolio whose survival depends on a correlation staying where it was. Size positions so that if everything falls together, the total fall is still inside your risk budget from lesson 1. Treat the diversification benefit as a bonus in normal times, not as the load-bearing wall.

## What to do with this

Before you add any holding, ask what it correlates with. If the answer is "the things I already own," you are adding size, not diversification. If you cannot answer, compute it: three years of monthly returns and a spreadsheet correlation function take five minutes.

Then remember that the number you computed is a snapshot. Assume it will be higher in a crash, and check that the portfolio still fits your budget when it is.

## Sources

- Harry Markowitz, "Portfolio Selection", Journal of Finance 7(1), 1952: https://www.jstor.org/stable/2975974
- Meir Statman, "How Many Stocks Make a Diversified Portfolio?", Journal of Financial and Quantitative Analysis 22(3), 1987: https://www.jstor.org/stable/2330969
- John Y. Campbell, Martin Lettau, Burton G. Malkiel and Yexiao Xu, "Have Individual Stocks Become More Volatile?", Journal of Finance 56(1), 2001: https://doi.org/10.1111/0022-1082.00318
- François Longin and Bruno Solnik, "Extreme Correlation of International Equity Markets", Journal of Finance 56(2), 2001: https://doi.org/10.1111/0022-1082.00340

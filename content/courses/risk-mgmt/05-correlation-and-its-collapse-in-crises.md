---
{
  "title": "Correlation and Its Collapse in Crises",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The average pairwise correlation of the nine S&P sector ETFs was 0.31 in calendar 2017 and 0.88 between 2020-02-20 and 2020-04-30. What does that do to a diversified long book?", "opts": ["Nothing; sector weights are unchanged", "It only affects short books", "It makes the book safer because everything moves together", "It removes most of the diversification: with correlations near 0.9 the book behaves like one large position, so its volatility jumps even before individual vols rise"], "correct": 3, "explain": "Portfolio variance is wᵀΣw. When the off-diagonal terms go from 0.3 to 0.9, the sum grows even with the diagonal unchanged. Add the vol spike and the two effects multiply."},
    {"q": "In the book's stress test, replacing the last year's correlation matrix with the March 2020 matrix while keeping current volatilities raised 95% VaR from $9,972 to $16,841. Replacing both correlations and volatilities with March 2020 values raised it to $42,357. Which statement is right?", "opts": ["Correlation alone did most of the damage", "Correlation alone raised VaR by 69%; volatility did the rest, and the two together multiplied to a fourfold increase, which is what a crisis looks like", "Volatility does not matter", "The $42,357 figure is impossible"], "correct": 1, "explain": "Correlation shock: ×1.69. Both shocks: ×4.25. Neither number is a forecast; both are answers to the question 'what would this book have done in that regime', which is what a stress test is for."},
    {"q": "SPY–TLT correlation was −0.33 in 2017, −0.50 in the 2008 and 2020 crisis windows, and +0.27 over the year to 2026-09-23. What does that imply for a book counting on Treasuries as its equity hedge?", "opts": ["The hedge worked in the two deflationary crashes and has not worked in the recent regime; a hedge that depends on a sign that flips must be stress-tested under the flipped sign", "Treasuries always hedge equities", "TLT should be shorted", "Correlation with TLT is irrelevant"], "correct": 0, "explain": "The 2022 bear market, when both fell together, is the case the positive correlation describes. A stress test that assumes −0.5 for TLT is assuming the crash will be the kind that suits your hedge."},
    {"q": "The book's eight long positions had an average pairwise correlation of 0.05 over the last year and 0.59 in February to April 2020. Its two shorts correlated 0.57 and 0.62 with the long basket last year, and 0.92 and 0.90 in 2020. What happened to the short hedge in 2020?", "opts": ["It stopped working", "It doubled the loss", "It worked better: the shorts moved almost one-for-one with the longs, so they offset more of the fall; the replay shows the book lost 14.4% while SPY lost 33.7%", "It made no difference"], "correct": 2, "explain": "Rising correlation hurts a long-only book and helps a hedged one, because the shorts start tracking the longs. That is the argument for holding a short leg against a factor rather than relying on low correlation among longs, which disappears exactly when you need it."},
    {"q": "Why does the course prefer a stress test that replays a historical correlation matrix over one that sets every pair to 0.8?", "opts": ["Because 0.8 is too low", "Because the historical matrix keeps the structure that actually occurred, for example gold at 0.13 to 0.28 against everything while equities went to 0.7 to 0.9; a flat 0.8 destroys real diversifiers along with fake ones", "Because it is easier to compute", "Because regulators require it"], "correct": 1, "explain": "The flat shock gave $19,645 against $16,841 for the replay. The difference is almost entirely GLD, which the flat shock forces to 0.8 with every equity. Use both, but understand that the flat shock is a bound and the replay is a history."}
  ],
  "task": "Compute your book's correlation matrix over the last year and over 2020-02-20 to 2020-04-30, and recompute portfolio volatility with the crisis matrix and current vols."
}
---

## Diversification is a correlation bet

Every diversified book is implicitly betting that the correlations that made it look diversified will still be there when it matters. They usually are not. The evidence is old, consistent, and worth restating with current numbers because the 2025-26 regime has been unusually low-correlation, which makes books look safer than they are.

Longin and Solnik (2001) showed that international equity correlations rise in bear markets and not in bull markets; the asymmetry is in the left tail specifically. Ang and Chen (2002) found the same within US equities: correlations conditional on down moves are much higher than conditional on up moves, and the effect is strongest for the largest down moves. The mechanism is not mysterious. In a crisis, the marginal seller is selling everything to raise cash or cut gross, and the marginal buyer has stepped away. Prices are then set by the same flow, and the same flow produces the same sign.

## The evidence, measured

Daily-return correlations from Yahoo adjusted closes, four windows: calendar 2017 (251 days, a calm year); 2008-09-15 to 2008-12-31 (76 days, from the Lehman filing); 2020-02-20 to 2020-04-30 (50 days); and the year to 2026-09-23 (251 days).

Average pairwise correlation among the nine original S&P sector ETFs (XLK, XLF, XLE, XLV, XLY, XLP, XLU, XLI, XLB): **0.31 in 2017, 0.82 in late 2008, 0.88 in spring 2020, 0.21 in the last year.**

Selected pairs, 2017 / 2008 / 2020 / last year:

- XLK–XLF: 0.37 / 0.84 / 0.92 / 0.22
- XLE–XLU: −0.03 / 0.87 / 0.66 / 0.06
- XLV–XLY: 0.39 / 0.74 / 0.89 / 0.29
- SPY–EFA: 0.69 / 0.97 / 0.96 / 0.79
- SPY–EEM: 0.62 / 0.93 / 0.93 / 0.77
- SPY–HYG: 0.68 / 0.61 / 0.84 / 0.77
- SPY–TLT: −0.33 / −0.50 / −0.50 / +0.27
- SPY–GLD: −0.25 / +0.08 / +0.22 / +0.33

Energy and utilities, which in 2017 were uncorrelated, moved together at 0.87 in late 2008. Foreign and emerging equities, which in a calm year retain some independence from US stocks, become the same trade at 0.93 to 0.97. Treasuries kept their negative correlation in both deflationary crashes; gold did not, drifting to zero or slightly positive.

Two warnings in the table. SPY–TLT is +0.27 over the last year, so the Treasury hedge that worked in 2008 and 2020 is currently not a hedge at all, as it was not in 2022. And the last-year sector average, 0.21, is lower than even 2017; a book built on 2025-26 correlations is being flattered by the calmest cross-sectional regime in the sample.

## What it does to a portfolio

Portfolio variance is wᵀΣw, where Σ has variances on the diagonal and covariances off it. For a long-only book of n equal positions with common vol σ and common correlation ρ, portfolio variance is σ²[1/n + ρ(1 − 1/n)]. With ρ = 0.3 and n = 10, the bracket is 0.37; with ρ = 0.9 it is 0.91. Correlation going from 0.3 to 0.9 raises portfolio volatility by √(0.91/0.37) = 1.57 times before any single position's vol has changed. Then the vols double or triple, and the effects multiply.

For a long-short book the sign is different. A short that was 0.6 correlated with the longs offsets some of the move; at 0.9 it offsets more. The replay below shows this: the book lost less than half of what SPY lost in March 2020, because the two shorts went to 0.9 correlation with the long basket and did their job.

## Worked example

The course book, current weights, three stress calculations. In each, portfolio daily σ = √(wᵀΣw) where Σ is built as Dᵀ C D from a correlation matrix C and a diagonal of daily vols D; 95% VaR = 1.645 × σ × $1,000,000.

**Base.** Last-year correlations and vols (2025-09-24 to 2026-09-23). Average pairwise correlation among the eight longs: 0.05. IWM and ARKK correlate 0.57 and 0.62 with the weighted long basket. σ = 0.6062%, VaR = **$9,972**. (This reproduces lesson 4.)

**Shock 1: March 2020 correlations, current vols.** C from 2020-02-20 to 2020-04-30, 50 days. In that matrix NVDA–MSFT is 0.92, JPM–IWM 0.91, IWM–ARKK 0.93; the average among the eight longs is 0.59; GLD sits at 0.13 to 0.28 against everything. The shorts correlate 0.92 (IWM) and 0.90 (ARKK) with the long basket. σ = 1.024%, VaR = **$16,841**, 1.69 times base.

**Shock 2: flat 0.8 correlations, current vols.** Every off-diagonal entry set to 0.8, including GLD. σ = 1.194%, VaR = **$19,645**, 1.97 times base. The extra $2,800 over shock 1 is almost entirely GLD being forced to move with equities.

**Shock 3: March 2020 correlations and March 2020 vols.** Annualised vols in that window: NVDA 101%, MSFT 81%, AMZN 54%, JPM 99%, XOM 84%, UNH 93%, COST 56%, GLD 30%, IWM 74%, ARKK 83%. σ = 2.575%, VaR = **$42,357**, 4.25 times base.

**Vols doubled, current correlations** (for comparison): VaR = $19,944, 2.0 times base. So doubling every vol and shocking every correlation to March 2020 each roughly double the VaR on their own, and together they quadruple it, because the effects compound in the quadratic form.

**Replay.** Hold the current weights through 2020-02-19 to 2020-03-23 and mark daily. Position returns over the window: NVDA −32.4%, MSFT −27.4%, AMZN −12.3%, JPM −42.5%, XOM −47.9%, UNH −35.9%, COST −11.6%, GLD −3.6%, IWM −40.7%, ARKK −36.5%. Book return = Σ wᵢ rᵢ = 0.15(−32.4) + 0.12(−27.4) + 0.11(−12.3) + 0.12(−42.5) + 0.10(−47.9) + 0.09(−35.9) + 0.09(−11.6) + 0.12(−3.6) − 0.15(−40.7) − 0.10(−36.5) = **−14.35%**, against −33.7% for SPY. The shorts contributed +6.1% + 3.7% = +9.8%; without them the long book alone lost 24.1%.

## Chart

![Daily-return correlations for eight pairs in calendar 2017 (blue, 251 days) and in the crisis window 2020-02-20 to 2020-04-30 (red, 50 days): XLK–XLF, XLE–XLU, XLV–XLY, SPY–EFA, SPY–EEM, SPY–HYG, SPY–TLT, SPY–GLD. Every equity pair rises toward 0.9; TLT stays negative; gold goes from −0.25 to +0.22. Source: Yahoo Finance adjusted closes.](figures/sector-correlations-calm-vs-crisis.svg)

## What to do with the stress number

The stress VaR is not a forecast and it does not replace the base VaR. It is the answer to "if the regime changes to the worst one in the sample, what is tomorrow's loss threshold?" and its job in the report is to size the gap between the everyday number and the crisis number.

For this book the gap is 4.25x. That ratio, more than either level, tells you how much of the book's apparent safety is borrowed from the current correlation regime. A book whose stress VaR is twice its base VaR is robust; one whose stress VaR is six times base is a calm-weather construction. The action rule in lesson 12 keys off this ratio: when the fast vol estimate from lesson 3 starts rising, the book is assumed to be moving toward the stress number, not the base, and gross comes down before the correlations confirm it.

Two closing cautions. Historical matrices contain only the crises that happened; the next one will correlate differently, and the flat-shock bound exists to cover that. And a short hedge that worked in the replay worked because the shorts were index-like and high-beta; a single-name short can go the other way in a squeeze, which is a correlation shock with the wrong sign.

## Sources

- Longin, F. and Solnik, B. (2001). "Extreme Correlation of International Equity Markets." *Journal of Finance* 56(2). https://doi.org/10.1111/0022-1082.00340
- Ang, A. and Chen, J. (2002). "Asymmetric correlations of equity portfolios." *Journal of Financial Economics* 63(3). https://doi.org/10.1016/S0304-405X(02)00068-5
- Forbes, K. J. and Rigobon, R. (2002). "No Contagion, Only Interdependence: Measuring Stock Market Comovements." *Journal of Finance* 57(5). https://doi.org/10.1111/0022-1082.00494
- Yahoo Finance historical data, sector ETFs, SPY, EFA, EEM, HYG, TLT, GLD. https://finance.yahoo.com/quote/XLK/history/

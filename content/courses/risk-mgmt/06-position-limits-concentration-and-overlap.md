---
{
  "title": "Position Limits, Concentration and the Overlap Problem",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "NVDA is 15.0% of the book by weight but contributes 30.0% of its variance. Why can a position contribute twice its weight in risk?", "opts": ["Because its share count is high", "Because it is a technology stock", "Because risk contribution is weight × covariance with the book ÷ portfolio variance: a high-vol position that also correlates with the rest of the book carries more of the total than its dollar size", "Because the book is short IWM"], "correct": 2, "explain": "NVDA has the second-highest vol in the book (37.8%) and positive correlation with MSFT, AMZN and the two shorts' underlying factor. Both raise its covariance with the portfolio, and that, not its weight alone, sets its share of the variance."},
    {"q": "The 'effective number of positions' from the Herfindahl index of gross weights is 9.69 for a ten-line book. The risk-weighted picture says the top three lines hold 71% of the variance. Which number should drive the concentration check?", "opts": ["The risk-weighted one; the Herfindahl index counts dollars, and dollars are not what lose money at the same time", "The Herfindahl number, because it is closer to ten", "Neither; concentration is not measurable", "The average of the two"], "correct": 0, "explain": "Ten equal weights give an effective N of ten however correlated they are. A concentration check on weights alone would pass this book. The variance decomposition shows three names doing most of the work."},
    {"q": "Where does a hard 20% single-name cap come from in fund practice?", "opts": ["The Investment Company Act of 1940 sets it", "No statute sets 20%; it is the size at which a 50% single-name gap costs 10% of NAV, roughly one month's tolerable loss for a concentrated fund. The statutory anchors are 5% per issuer for the diversified 75% of a 1940 Act fund and 25% per issuer under the tax rules for the rest", "FINRA Rule 4210", "The Basel Committee"], "correct": 1, "explain": "Section 5(b)(1) of the 1940 Act defines a diversified fund by the 75-5-10 test; IRC §851(b)(3) allows up to 25% in one issuer for the other half. Managers who run concentrated books choose 20% as the largest single position whose plausible worst day is survivable."},
    {"q": "Over the last year NVDA, MSFT and AMZN were pairwise correlated at only 0.25 to 0.39. In February to April 2020 NVDA–MSFT was 0.92. What is the overlap problem?", "opts": ["The three stocks are the same company", "There is no overlap if the sectors differ", "Correlation is always 0.92 in tech", "Three positions taken on three separate signals can still be one factor bet, and the factor shows itself in the regime when it matters; calm-regime correlation understates the overlap"], "correct": 3, "explain": "The signal that picked each stock may be independent; the return driver is not. Concentration limits on names do not catch a book that is 38% one factor, which is why the limit is set on factor exposure as well."},
    {"q": "The book's diversification ratio, the weighted average of position vols divided by portfolio vol, is 3.50. What does a falling diversification ratio tell you?", "opts": ["Positions are getting cheaper", "The book has fewer positions", "Correlations are rising and the book is converging toward a single bet; in a crisis the ratio collapses toward one", "Volatility is falling"], "correct": 2, "explain": "The ratio measures how much vol the book is 'saving' through imperfect correlation. If every pair went to 1.0 the ratio would be 1.0. Tracking it daily is a cheap early warning that lesson 5's stress case is arriving."}
  ],
  "task": "Decompose your book's variance into per-position contributions and compare the top three contributors to the top three weights."
}
---

## Limits are the rules that do not need a forecast

Volatility, VaR and correlation all try to predict something. Position limits do not. A cap on the largest position is a statement that whatever happens to one name, the book survives it, and that statement holds whether or not your model of the name is right. That is why limits sit at the top of the framework: they are the part that works when everything else is wrong.

A limit framework has three layers. A cap on any single position. A cap on any group of positions that share a driver. And a way of measuring the second thing, because the group is not always visible from the labels.

## Single-name caps and where the numbers come from

There is no statute that says 20%. The numbers that regulators actually wrote down are these. Section 5(b)(1) of the Investment Company Act of 1940 defines a "diversified" fund as one where at least 75% of assets are invested such that no single issuer exceeds 5% of assets or 10% of the issuer's voting stock, the "75-5-10" test. The tax code's diversification test for regulated investment companies, IRC §851(b)(3), requires 50% of assets to meet a similar 5% rule and caps any single issuer at 25% of assets. UCITS funds in Europe live under the "5/10/40" rule of Directive 2009/65/EC: 5% per issuer normally, up to 10% if the issuers above 5% sum to no more than 40%.

The 20% you see in hedge-fund offering documents and prop-firm rulebooks comes from arithmetic rather than law. A single stock can gap 50% on an earnings miss, a fraud, or a failed trial. At 20% of NAV that costs 10% of NAV, which is about the largest monthly loss a concentrated fund can take without triggering investor redemptions or a firm's drawdown rule. At 30% the same gap costs 15%, which usually triggers something. So 20% is where "survivable single-name catastrophe" meets "meaningful position." Managers who run more names, or more leverage, set it lower; the course book, at 15% max, is at the conservative end of concentrated.

Write your own cap as a loss, not a weight: "no single position may cost more than X% of NAV on a 50% gap." Then the weight follows.

## Concentration in dollars versus in risk

The Herfindahl index of gross weights, H = Σ (|wᵢ| / Σ|wⱼ|)², gives an "effective number of positions" 1/H. Ten equal weights give 10; one 50% position and ten 5% positions give about 3.6. It is a fast check and it is nearly useless on its own, because it treats every dollar as equally risky and equally independent.

The better decomposition is by variance. Portfolio variance σ²ₚ = wᵀΣw can be written as Σᵢ wᵢ (Σw)ᵢ, so each position's contribution is wᵢ (Σw)ᵢ / σ²ₚ, and the contributions sum to 100%. (Σw)ᵢ is the covariance of position i with the whole book, so a position's risk share is its weight times how much it moves with everything else. A large, volatile, correlated position dominates; a small uncorrelated one, or a short that offsets, contributes little or negative.

A related number is the diversification ratio: Σ|wᵢ|σᵢ divided by σₚ. It is the vol the book would have if every pair were perfectly correlated, divided by the vol it actually has. Higher is more diversified; in a crisis it collapses toward one.

## The overlap problem

Suppose three separate signals fire: a momentum screen picks NVDA, a quality screen picks MSFT, a mean-reversion setup picks AMZN. Three positions, three strategies, three sectors if you squint. In a calm year they correlate at 0.25 to 0.39 with each other and the book looks diversified. Then the growth factor sells off and all three fall together at 0.8 to 0.9 correlation, because what the signals shared was not the setup but the factor.

Overlap is concentration that the name-level limit cannot see. It is caught two ways. First, by a factor exposure cap, from lesson 2: net growth-factor exposure (beta to QQQ times weight, summed) under some limit, regardless of how many names supply it. Second, by running the variance decomposition on the crisis correlation matrix from lesson 5 rather than the calm one, which shows the concentration the calm matrix hides.

## Worked example

The course book, last-year daily vols and correlations (2025-09-24 to 2026-09-23), σₚ = 0.6062% per day.

**Herfindahl.** Gross weights sum to 114.9%. Normalised gross weights: NVDA 0.131, MSFT 0.105, AMZN 0.096, JPM 0.105, XOM 0.087, UNH 0.078, COST 0.078, GLD 0.104, IWM 0.131, ARKK 0.087. H = Σ w² = 0.103. Effective N = **9.69**. Verdict by dollars: nearly perfectly diversified.

**Variance decomposition.** Contribution of each position to σ²ₚ, in percent of total:

NVDA **30.0%** · MSFT **22.1%** · AMZN **18.7%** · GLD 13.6% · UNH 10.9% · JPM 8.7% · XOM 4.2% · COST 2.8% · IWM −4.1% · ARKK −6.9%. Sum 100.0%.

NVDA, MSFT and AMZN are 38% of NAV and **70.8%** of the variance. The two shorts, 25% of gross, contribute −11%: they reduce risk, which is what shorts against a long book should do. XOM and COST, 19% of NAV, contribute 7% between them, because their correlations with the rest of the book are near zero or negative over this window.

In vol terms: NVDA's share is 0.300 × 0.6062% = 0.182% of the book's 0.606% daily σ. If NVDA were cut to 10% of NAV, its contribution would fall roughly in proportion to weight squared for its own variance and linearly for its covariances, so the book's σ would fall by around 0.06% a day, about 10%.

**Diversification ratio.** Σ|wᵢ|σᵢ (annualised): 0.150 × 37.8 + 0.120 × 32.5 + 0.110 × 34.4 + 0.120 × 22.4 + 0.100 × 26.2 + 0.090 × 34.5 + 0.090 × 19.9 + 0.120 × 29.4 + 0.150 × 18.7 + 0.100 × 38.0 = 5.67 + 3.90 + 3.78 + 2.69 + 2.62 + 3.11 + 1.79 + 3.53 + 2.81 + 3.80 = 33.7%. Portfolio σ annualised = 0.6062% × √252 = 9.62%. Ratio = 33.7 ÷ 9.62 = **3.50**. Under the March 2020 correlations with current vols (lesson 5), σₚ = 1.024% daily = 16.3% annualised, and the ratio falls to 33.7 ÷ 16.3 = 2.07.

**Single-name gap.** Largest position NVDA at 15.0%. A 30% overnight gap costs 4.5% of NAV; a 50% gap costs 7.5%. Against a 10%-of-NAV monthly loss limit, the cap holds with room. The same 50% gap at a 20% weight would cost 10.0%, using the whole month's budget on one name.

**Overlap.** Last-year correlations: NVDA–MSFT 0.25, NVDA–AMZN 0.27, MSFT–AMZN 0.39. ARKK (short) against the three: 0.51, 0.35, 0.40. NVDA–QQQ 0.69. In February to April 2020: NVDA–MSFT 0.92, NVDA–AMZN 0.79, MSFT–AMZN 0.84. The three longs are one bet in the regime that matters, and the ARKK short is a partial hedge on the same bet: net growth-factor exposure from lesson 2 was about 0.10 after the shorts, against 0.35 gross. A factor cap of, say, 0.25 net would pass this book; a name cap of 15% passes it too; only the two together describe it.

## Table

| Position | Weight | Ann. vol | Share of variance | Rank by weight | Rank by risk |
|---|---|---|---|---|---|
| NVDA | 15.0% | 37.8% | 30.0% | 1= | 1 |
| MSFT | 12.0% | 32.5% | 22.1% | 3= | 2 |
| AMZN | 11.0% | 34.4% | 18.7% | 6 | 3 |
| GLD | 12.0% | 29.4% | 13.6% | 3= | 4 |
| UNH | 9.0% | 34.5% | 10.9% | 8= | 5 |
| JPM | 12.0% | 22.4% | 8.7% | 3= | 6 |
| XOM | 10.0% | 26.2% | 4.2% | 7 | 7 |
| COST | 9.0% | 19.9% | 2.8% | 8= | 8 |
| IWM (short) | −15.0% | 18.7% | −4.1% | 1= | 9 |
| ARKK (short) | −10.0% | 38.0% | −6.9% | 7 | 10 |

Source: Yahoo Finance adjusted closes, 2025-09-24 to 2026-09-23; weights at the 2026-09-23 close.

## The limit list

For a book like this one, written as a page in the risk document:

1. No single name above 15% of NAV; no single name whose 50% gap costs more than 7.5% of NAV.
2. No single position above 35% of the book's variance on the last-year matrix, or above 45% on the crisis matrix.
3. No factor (growth, small-cap, energy, duration, gold) above 0.25 net beta-weighted exposure.
4. Diversification ratio below 2.0 on the last-year matrix triggers a review of what has become correlated.
5. Every limit is checked from marks, not targets, every day.

The first rule is the one that works without a model. The other four are the ones that catch what the first rule cannot see.

## Sources

- Investment Company Act of 1940, §5(b)(1), 15 U.S.C. §80a-5. https://www.law.cornell.edu/uscode/text/15/80a-5
- Internal Revenue Code §851(b)(3), 26 U.S.C. §851. https://www.law.cornell.edu/uscode/text/26/851
- Directive 2009/65/EC (UCITS), Article 52. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0065
- Goetzmann, W. N. and Kumar, A. (2008). "Equity Portfolio Diversification." *Review of Finance* 12(3). https://doi.org/10.1093/rof/rfn005

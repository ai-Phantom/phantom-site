---
{
  "title": "Position Sizing and Portfolio-Level Tests: Correlation, Cash and Capacity",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The RSI(2) rule and the SMA200 rule have daily-return correlation 0.31, annualised volatilities of 10.76% and 12.16%, and Sharpe ratios of 0.27 and 0.93. A 50/50 blend scored 0.77. Why is the blend below the trend rule alone?", "opts": ["Because the blend halves the trend rule's return while adding a rule whose return is close to zero; low correlation cannot rescue a component with no edge", "Because correlation should be negative", "Because 50/50 is the wrong weight", "Because pandas averages Sharpe ratios"], "correct": 0, "explain": "Diversification reduces volatility (9.27% for the blend against 12.16%) but the blend's mean return is the average of the two means, and one of them is small. A low-correlation rule helps a book only if it has an edge of its own."},
    {"q": "The rule returned +26.1% over 2016-2025; 3-month T-bills returned +25.1%. Its Sharpe in excess of T-bills was 0.06. What does the cash benchmark say?", "opts": ["The rule passes because 26.1 is greater than 25.1", "The rule added one point over ten years relative to doing nothing; that is inside the noise and it fails a benchmark that sits at zero risk", "T-bills are not a fair benchmark for an equity rule", "The rule should be levered"], "correct": 1, "explain": "Cash is what the capital earns when the rule is flat, which is 85% of the time, and it is what the capital would earn with the rule switched off. A rule must beat that by more than sampling error to justify existing."},
    {"q": "Under the square-root impact model with SPY's 2025 ADV of $44.76 billion and daily volatility 1.13%, the order size at which impact alone reaches 5 bps is about:", "opts": ["$1 million", "$448 million", "$88 million", "$4.5 billion"], "correct": 2, "explain": "Set 1.13% × sqrt(Q / 44.76e9) = 0.05%: sqrt(Q / ADV) = 0.0442, so Q / ADV = 0.00196 and Q is about $87.6 million per order. The 1%-of-ADV rule of thumb ($448 million) would cost about 11 bps."},
    {"q": "Volatility targeting scales a rule's position so its realised volatility matches a target. For a 10% target and a rule with 10.76% realised volatility, the scale factor is:", "opts": ["1.076", "0.93", "0.10", "10.76"], "correct": 1, "explain": "Scale = target / realised = 0.10 / 0.1076 = 0.93. The rule is already near the target; a rule at 20% volatility would be run at half size, and one at 5% would need 2x leverage, which is a separate decision with a separate cost."},
    {"q": "The rule's correlation with SPY buy-and-hold is 0.62. If your existing book is mostly long SPY, what does this imply for the rule's contribution?", "opts": ["It is a hedge", "It is mostly more of the same exposure, concentrated on the days SPY is falling, and adds little diversification to that book", "Correlation does not matter for single-ticker rules", "It should be sized at 100%"], "correct": 1, "explain": "A rule that buys SPY on down days is long SPY on the days SPY is most volatile. Against a long-SPY book it adds beta at the worst moments and a small, uncertain edge on top."}
  ],
  "task": "Compute the daily-return correlation between your rule and every position you currently hold, and between your rule and T-bills; write down which one you would fund it from."
}
---

## A rule is not a portfolio

Everything up to this lesson evaluated one rule in isolation, funded from nothing, sized at 100% of capital. None of those assumptions hold when the rule joins a book. The capital it uses was earning something before; the exposure it adds overlaps with exposures already there; and the size it can run is limited by what the market will absorb. Three tests, each with a number: the cash benchmark, correlation with what you already run, and capacity. Then sizing, which is what you do with the three numbers.

## The cash benchmark

The simplest question is the one most reports skip: what did the capital earn compared with doing nothing? "Nothing" is not zero. It is the risk-free rate, which over 2016-2025 was the 3-month T-bill yield (FRED series DGS3MO), averaging 2.25% a year and compounding to +25.11% over the decade.

The running example (RSI(2) below 10, exit above SMA5, 5 bps per side, next-open) returned +26.09% over the same days. It beat cash by 0.98 percentage points in ten years. Its Sharpe in excess of the daily T-bill rate was 0.06. With a standard error near 0.32 for a ten-year Sharpe, 0.06 is indistinguishable from zero.

The benchmark bites harder than it looks because the rule is flat 85% of the time. In a real account the flat days earn the T-bill rate on the idle cash, so the rule's contribution is only what it earns on its 385 active days in excess of what those days would have earned in bills. That is the excess Sharpe, and it is 0.06.

Any rule that spends most of its time in cash must clear this gate first. It is also the reason lesson 12 puts "beats cash" ahead of "beats the index": a rule that beats the index but not cash is a rule that was short something that fell.

## Correlation with what you already run

A rule's value to a book is not its Sharpe; it is what it does to the book's Sharpe. That depends on the rule's correlation with what is already there. The standard formula for a two-asset blend with weights w₁, w₂, volatilities σ₁, σ₂ and correlation ρ:

σ² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂

The mean return of the blend is just the weighted mean of the two means. Volatility falls with correlation; return does not. A low-correlation rule with no return of its own lowers the book's volatility and its return by similar proportions, which leaves the book's Sharpe about where it was or lower.

The worked example computes this for the two rules in the course.

## Capacity

Lesson 5's square-root impact model gives the cost of an order as a function of its size: impact ≈ σ_daily × √(Q / ADV). Turn it round and it gives the largest order whose impact stays within the cost budget the rule can afford. If the rule survives at 5 bps per side and is dead at 20, impact must stay well under 5 bps, so:

√(Q / ADV) ≤ 0.0005 / 0.0113 = 0.0442, so Q / ADV ≤ 0.00196.

With SPY's 2025 average daily dollar volume of $44.76 billion, that is about $87.6 million per order. The common 1%-of-ADV rule of thumb ($447.6 million) would cost 1.13% × √0.01 = 11.3 bps and kill the rule. For a rule on a stock trading $50 million a day, the same budget is $98,000 per order. Capacity is not a concern for a retail account trading SPY; it is the first concern for the same rule on anything else.

## Worked example

Daily return series, 2016-01-04 to 2025-12-30, from the adjusted SPY bars of lesson 2 (Yahoo Finance chart API, 2,765 rows), next-open execution, no costs on the trend rule and 5 bps on the RSI rule as in earlier lessons. T-bills from FRED DGS3MO.

```python
rsi2 = backtest(adj, rsi_signal(adj, 10, 5), 5).loc["2016":"2025"]
trend = backtest(adj, (adj["close"] > adj["close"].rolling(200).mean()).astype(int)).loc["2016":"2025"]
spy = (adj["open"].shift(-1) / adj["open"] - 1).loc["2016":"2025"].dropna()
book = pd.DataFrame({"rsi2": rsi2, "trend": trend, "spy": spy}).dropna()
print(book.corr().round(3))
blend = 0.5 * book["rsi2"] + 0.5 * book["trend"]
ann = lambda x: (x.mean() / x.std() * 252 ** 0.5, x.std() * 252 ** 0.5)
print(ann(book["rsi2"]), ann(book["trend"]), ann(blend))
```

Correlations of daily returns: RSI rule to trend rule 0.307; RSI rule to SPY 0.622; trend rule to SPY 0.704. The RSI rule is long SPY on 15% of days, and those are the days after sharp falls, so its correlation to SPY is high relative to its exposure. The two rules are only modestly correlated with each other because they are long at different times.

The blend, 50% in each rule. Volatilities: σ₁ = 10.76% (RSI rule), σ₂ = 12.16% (trend rule), ρ = 0.307.

σ² = 0.25 × 0.1076² + 0.25 × 0.1216² + 2 × 0.25 × 0.307 × 0.1076 × 0.1216 = 0.002894 + 0.003697 + 0.002008 = 0.008599; σ = 9.27%.

Mean daily returns: the RSI rule's is 0.27 × 0.1076 / √252 = 0.000183; the trend rule's is 0.93 × 0.1216 / √252 = 0.000712; the blend's is 0.000448. Blend Sharpe = 0.000448 / (0.0927 / √252) = 0.77. Measured directly: Sharpe 0.77, CAGR 6.89%, volatility 9.27%, maximum drawdown -20.7%.

Adding the RSI rule at 50% to the trend rule took the Sharpe from 0.93 to 0.77, the CAGR from 11.11% to 6.89%, and the volatility from 12.16% to 9.27%. The low correlation cut the volatility by a quarter; the RSI rule's near-zero excess return cut the mean by more. This is the whole lesson in one row: correlation tells you what a rule does to risk, and it can only improve a book if the rule also brings return.

Vol targeting the RSI rule to 10% annualised: scale = 0.10 / 0.1076 = 0.93. Sizing is not the problem here; the rule already runs near target and a 7% haircut changes nothing. Vol targeting matters when rules of different volatility share a book, so that each contributes risk in proportion to its weight rather than its native volatility, and it matters when a rule's realised volatility drifts: the running example's realised volatility was 2.0% annualised in 2017 (7 entries, +3.5%) and 11.4% in 2018 (14 entries, -11.3%), a five-fold change that a fixed position size ignores and a rolling target would have caught only as it happened.

## Table

The three portfolio tests applied to the running example, with the thresholds lesson 12 uses.

| Test | Threshold | RSI(2) rule, 5 bps | Result |
|---|---|---|---|
| Beats cash: excess Sharpe over T-bills | ≥ 0.30 | 0.06 (+26.1% vs +25.1% over 2016-2025) | Fail |
| Correlation with existing rules | < 0.50 | 0.31 with the SMA200 rule | Pass |
| Correlation with the book's main exposure | < 0.50 | 0.62 with long SPY | Fail if the book is long SPY |
| Blend improves the book's Sharpe | Blend Sharpe > book Sharpe | 0.77 blended vs 0.93 for the trend rule alone | Fail |
| Capacity at the cost budget (impact ≤ 5 bps) | Intended size ≤ capacity | $87.6M per order on SPY | Pass for any retail size |
| Volatility target | Scale between 0.5 and 2.0 without leverage | 0.93 | Pass |

Four passes and two fails on paper, but the two fails are the ones that matter: the rule does not beat cash, and it does not improve a book that already holds the trend rule. A rule that fails the cash gate has nothing to size.

## Sources

- Markowitz, H. (1952). "Portfolio Selection." Journal of Finance 7(1). https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
- Tóth, B., Lempérière, Y., Deremble, C., de Lataillade, J., Kockelkoren, J., Bouchaud, J.-P. (2011). "Anomalous Price Impact and the Critical Nature of Liquidity in Financial Markets." Physical Review X 1(2), 021006 (the square-root impact law). https://doi.org/10.1103/PhysRevX.1.021006
- FRED, 3-Month Treasury Bill Secondary Market Rate (DGS3MO): https://fred.stlouisfed.org/series/DGS3MO
- pandas documentation, `DataFrame.corr`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

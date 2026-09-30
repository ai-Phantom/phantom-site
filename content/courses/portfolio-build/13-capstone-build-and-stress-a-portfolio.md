---
{
  "title": "Capstone: Build and Stress a Five-Position Portfolio",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In the capstone, the simple portfolio risk number is the weighted average of the holdings' volatilities. This number", "opts": ["Understates true volatility because it ignores bonds", "Is an upper bound on true volatility, because it assumes all holdings are perfectly correlated", "Equals the Sharpe ratio", "Cannot be computed without options data"], "correct": 1, "explain": "The weighted average is the correlation-1.0 case. Real correlations are lower, so true portfolio volatility is below it. It is used because it is quick, conservative and shows every step."},
    {"q": "A portfolio has a weighted beta of 0.885 to the broad market. A −20% market shock is expected to move it by about", "opts": ["−20%", "−17.7%", "−8.9%", "−10%"], "correct": 1, "explain": "0.885 × (−20%) = −17.7%. Beta scales the market move; a portfolio with bonds and low-beta holdings has a beta below 1 and falls less than the market."},
    {"q": "A 12.5% position falls 50% while everything else is unchanged. The portfolio falls by", "opts": ["50%", "12.5%", "6.25%", "3.1%"], "correct": 2, "explain": "12.5% × 50% = 6.25%. The position's weight afterward is 6.25 ÷ 93.75 = 6.7%, which tells you whether a rebalancing band or a stop has been hit."},
    {"q": "After the single-name shock, the correct written response is", "opts": ["Buy more of the fallen stock to average down", "Whatever the plan's stop and thesis-review rules say for that position, applied without reference to the loss", "Sell everything", "Wait for it to get back to the purchase price"], "correct": 1, "explain": "The capstone tests whether your plan produces an answer without judgement. Averaging down is the disposition effect; waiting for cost basis is anchoring; both were named in lesson 10."},
    {"q": "Why does the capstone require at least one broad fund among the five positions?", "opts": ["Funds are cheaper to trade", "Because five individual stocks cannot be diversified (lesson 3), so a broad fund is the only way for five positions to hold a real core", "It is a regulatory requirement", "Funds never fall"], "correct": 1, "explain": "With only five lines, single stocks alone would leave the portfolio at the correlation floor with heavy single-name risk. A broad fund gives the core its thousands of holdings in one line."}
  ],
  "task": "Submit your five-position portfolio with all six sections completed and score it against the rubric before reading the sample solution."
}
---

## The exercise

You will build a five-position portfolio on paper, size it, compute its weights and a simple risk number, then hit it with two shocks and write down what your plan says to do. The point is not to produce the best portfolio. It is to produce one where every number can be traced to a rule you wrote, and where the shocks produce an answer without your having to think at the moment of stress.

Work in a spreadsheet or on paper. Show every calculation. Use a nominal $10,000 unless you prefer your own figure.

### Part 1: Choose five positions with reasons

Constraints:

- At least one broad index fund (a total-market stock fund, or a stock fund plus a bond fund).
- No more than three individual stocks.
- If you hold three individual stocks, they must be in three different sectors.
- Each position gets a one-line reason in the form "Role: … Thesis: …". For a core fund the thesis is simply "deliver the allocation." For a stock it must be checkable within a year.

### Part 2: Size the positions

- State your risk budget: maximum tolerable fall in percent and dollars.
- State the allocation the five positions implement (stocks / bonds / cash).
- Give each position a weight and a dollar amount.
- For each individual stock, give the stop price and show that (weight × distance to stop) is inside your per-position risk rule, and that the weight is inside your per-position cap.

### Part 3: Compute the weights and a risk number

- Confirm the weights sum to 100%.
- For each position, state an approximate annualised volatility and a beta to the broad US market. Use round figures from any reputable data source and say where they came from. For the purpose of this exercise, these are acceptable: broad US stock fund 17% and beta 1.0; international stock fund 17% and beta 0.9; total bond fund 5% and beta 0.0; T-bill fund 0.5% and beta 0.0; large-cap stocks 20% to 50% depending on the name, beta 0.6 to 1.8.
- Compute the weighted average volatility (the simple risk number) and the weighted beta.
- Optionally, compute a diversified volatility using the two-asset formula from lesson 3 for the stock and bond sleeves.

### Part 4: Apply a −20% market shock

- Assume the broad market falls 20%. Move each position by its beta times −20%.
- Compute the new dollar value of every position, the portfolio total, and the portfolio return.
- Compute the new weights.
- Identify which rebalancing bands, if any, are breached.
- Write what your plan says to do, and the specific trades in dollars.

### Part 5: Apply a single-name −50% shock

- Choose the individual stock with the largest weight. Assume it falls 50% while everything else is unchanged.
- Compute the portfolio return and the position's new weight.
- State whether the stop was hit (it was, unless the stop was more than 50% away, which itself would fail Part 2).
- Write what the plan says to do, and the specific trade.

### Part 6: Reflection

In no more than 200 words: which of the two shocks was worse for this portfolio, what one change to the construction would have reduced it, and what that change would cost in expected return or in the goal's required return.

## Worked example

A sample submission, abbreviated. Yours should show the same steps for your own positions.

**Part 1.** $10,000. Risk budget: 25%, $2,500.

- VTI, 40%: Role core US equity. Thesis: deliver the allocation.
- VXUS, 15%: Role core international equity. Thesis: deliver the allocation.
- BND, 20%: Role drawdown control. Thesis: deliver the allocation.
- JPM, 12.5%: Role satellite, financials. Thesis: return on equity stays above 15% through the next annual report.
- NVDA, 12.5%: Role satellite, technology. Thesis: data-centre revenue grows over 30% year on year in the next two quarterly reports.

**Part 2.** Allocation 80% stocks / 20% bonds. Per-position risk rule 2% ($200). Per-position cap 12.5%.

- JPM at $250, stop $210 (16% below). Risk: 12.5% × 16% = 2.0%. At the limit; passes.
- NVDA at $180, stop $150 (16.7% below). Risk: 12.5% × 16.7% = 2.1%. Marginally over. Fix: reduce NVDA to 12% and move 0.5% to BND, or tighten the stop to $151. The sample keeps 12.5% and tightens the stop to $151 (16.1% below, risk 2.0%). Prices are round figures for the exercise; use live quotes.

**Part 3.** Volatilities and betas, rounded from 2020 to 2024 data: VTI 17% / 1.0; VXUS 17% / 0.9; BND 5% / 0.0; JPM 28% / 1.1; NVDA 50% / 1.7.

Weighted volatility = 0.40 × 17 + 0.15 × 17 + 0.20 × 5 + 0.125 × 28 + 0.125 × 50
= 6.80 + 2.55 + 1.00 + 3.50 + 6.25 = 20.1%

Weighted beta = 0.40 × 1.0 + 0.15 × 0.9 + 0.20 × 0.0 + 0.125 × 1.1 + 0.125 × 1.7
= 0.400 + 0.135 + 0 + 0.1375 + 0.2125 = 0.885

**Part 4, market −20%.** Each position moves by beta × −20%:

- VTI: 4,000 × (1 − 0.20) = $3,200
- VXUS: 1,500 × (1 − 0.18) = $1,230
- BND: 2,000 × (1 − 0) = $2,000
- JPM: 1,250 × (1 − 0.22) = $975
- NVDA: 1,250 × (1 − 0.34) = $825
- Total: $8,230. Return: −17.7%, matching 0.885 × −20%.

New weights: VTI 38.9%, VXUS 14.9%, BND 24.3%, JPM 11.8%, NVDA 10.0%. Stocks are 75.7% versus an 80% target; bonds 24.3% versus 20%. With a ±5-point band on the stock/bond split, the drift of 4.3 points is inside the band, so the rebalancing rule alone says: no trade until the next check date; direct new contributions to the equity funds. The −17.7% fall is inside the 25% budget.

Now check the stops against the beta-scaled prices, which is the step most submissions miss. JPM at 250 × 0.78 = $195 is below its $210 stop. NVDA at 180 × 0.66 = $118.80 is below its $151 stop. Both satellites were stopped out on the way down. The plan says: sell each at its stop the next trading day, hold the proceeds in BND until the next check date, record both losses. With the stops honoured the actual damage is smaller than the beta arithmetic suggests: JPM loses 16% of 12.5% = 2.0 points, NVDA loses 16.1% of 12.5% = 2.0 points, VTI loses 8.0 points, VXUS 2.7 points, BND nothing. Portfolio: −14.7%, not −17.7%, and the ending balance is about $8,530 with $2,098 of it parked in BND from the two sales. The interaction between a market shock and per-position stops is exactly the kind of thing the exercise exists to surface.

**Part 5, NVDA −50%.** NVDA: 1,250 × 0.5 = $625. Everything else unchanged. Total: $9,375. Return: −6.25%. NVDA's new weight: 625 ÷ 9,375 = 6.7%. The stop at $151 was hit on the way down at −16%, long before −50%. Plan says: sold at the stop for a loss of about $200 (2% of portfolio); the remaining −4.25% of the shock never reached the portfolio. Trade: sell 6.94 shares at $151 for roughly $1,048; proceeds to BND pending the next check date.

**Part 6.** The market shock was worse in size (−14.7% with stops honoured, versus −2% for the single-name shock after its stop). The single change that would have reduced it most is 10 points from VTI to BND, taking the beta to 0.785 and the shock to −15.7%, at a cost of roughly 0.4 to 0.5 points of expected annual return using long-run stock and bond averages. For a goal requiring under 5%, that cost is affordable.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Position rationale | Five positions, at least one broad fund, no more than three stocks in distinct sectors; each with a role and a checkable one-line thesis | 20 |
| Sizing and weights | Risk budget stated in % and $; allocation stated; weights sum to 100%; every stock has a stop; (weight × stop distance) shown to be inside the risk rule; weights inside the cap; any breach fixed and the fix shown | 20 |
| Risk number | Volatilities and betas stated with a source; weighted volatility and weighted beta computed with every step visible; correctly described as an upper bound | 15 |
| Market shock | Beta-scaled moves per position; new values, total, return and weights all computed; band breaches identified; stops checked against the scaled fall; the plan's response written as specific trades | 15 |
| Single-name shock | Correct position chosen; portfolio return and new weight computed; stop hit identified and the actual loss under the stop computed; response written as a specific trade with proceeds destination | 15 |
| Reflection and consistency | Names the worse shock with numbers; proposes one construction change and quantifies both its risk reduction and its cost; every action in Parts 4 and 5 traceable to a written rule rather than to judgement | 15 |

Total: 100. A submission that scores 80 or above with no criterion below 10 has produced a portfolio that can be run. A submission that scores well on Parts 1 to 3 but fails the shocks has produced a pile with good intentions, and should be revised before real money follows it.

## Sources

- U.S. Securities and Exchange Commission, Investor.gov, "Asset Allocation": https://www.investor.gov/introduction-investing/getting-started/asset-allocation
- Harry Markowitz, "Portfolio Selection", Journal of Finance 7(1), 1952: https://www.jstor.org/stable/2975974
- Vanguard Research (Jaconetti, Kinniry, Zilbering), "Best practices for portfolio rebalancing", 2010: https://www.vanguard.com/pdf/icrpr.pdf
- FINRA, "Asset Allocation and Diversification": https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification

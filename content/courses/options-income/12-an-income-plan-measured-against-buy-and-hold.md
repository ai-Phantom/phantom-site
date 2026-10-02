---
{
  "title": "An Income Plan, Measured Honestly Against Buy-and-Hold",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The chain's cash-secured 95 put collected $169. On November 6 XYZ is 92.00 and you are assigned. What does an honest ledger show for the cycle?", "opts": ["-$131 marked to market on the shares (basis 93.31 against 92.00), plus $46.85 of collateral interest", "+$169 of income", "+$169 income and a separate stock position at 95.00", "$0 until the shares are sold"], "correct": 0, "explain": "The premium is not income; it is inside the basis. Marking the shares at 92.00 against a 93.31 basis is -$131. Counting the $169 as income while carrying shares at 95.00 double-counts it."},
    {"q": "Which denominator is correct for the wheel's return?", "opts": ["The premium received", "The broker's buying-power reduction", "The full cash committed to the strike ($9,500), because that is the capital that could not be used elsewhere and that bears the loss", "The maximum loss"], "correct": 2, "explain": "The PUT index is measured this way: puts over a Treasury bill account equal to the strike. Using buying power as the denominator flatters the return and hides the capital at risk."},
    {"q": "Cycle returns on a short-premium strategy have a standard deviation of about 4% per 45-day cycle. Roughly how many cycles are needed before an average edge of 0.5% per cycle is two standard errors from zero?", "opts": ["8", "32", "256", "1,000"], "correct": 2, "explain": "Standard error of the mean = 4% / sqrt(n). Two standard errors equal 0.5% when sqrt(n) = 16, so n = 256 cycles, about 32 years of 45-day cycles. A one-year record of 8 cycles has a standard error of 1.4%, three times the edge."},
    {"q": "The fair benchmark for a wheel on XYZ is:", "opts": ["Cash", "The S&P 500", "The premium collected", "100 shares of XYZ bought on the plan's start date and held, with dividends, plus a mechanical put-write on the same name for the volatility component"], "correct": 3, "explain": "The wheel is XYZ exposure with a volatility overlay. Buy-and-hold XYZ isolates what the overlay added or cost; a mechanical put-write (the PUT index construction applied to XYZ) isolates what your management added over a rule."},
    {"q": "Over the Lesson 4 cycle the wheel returned 5.30% in 87 days and buy-and-hold XYZ returned -3.5%. Compounding 5.30% to a year gives 24.2%. Which is the honest statement for the plan?", "opts": ["The plan targets 24% a year", "The wheel earned 5.30% over 87 days on one path; annualising one cycle is not a forecast and the plan's target should be stated as a comparison to the benchmark, not a number", "The wheel beats buy-and-hold by 8.8% per cycle", "Nothing can be said from one cycle"], "correct": 1, "explain": "One path is a data point, not an expectation. The plan should state the benchmark it aims to beat on a risk-adjusted basis and the number of cycles after which it will be judged."}
  ],
  "task": "Write a one-page income plan using the template in this lesson: objective, benchmark, gate, structures, sizing, management rules, ledger columns, and the review date at which you will compare it to buy-and-hold."
}
---

## What a plan is for

Everything in Lessons 1 to 11 is a component. A plan is the document that fixes, before the first trade, which components you use, when you use them, how big, and how you will know whether it worked. The reason to write it down is the one Lesson 5 gave: high-probability strategies produce long runs of wins that feel like proof and are not. Without a written standard, the seven-month winning streak sets the size and the eighth month sets the loss.

The plan has two halves. The rules half is short. The measurement half is where most income traders fail, because the natural way to count, premium collected, is wrong.

## The rules half

**Objective.** State what the strategy is supposed to do relative to a benchmark, not an absolute number. "Earn the variance risk premium on XYZ-type names with lower volatility and drawdown than holding the shares, and at least equal total return over a full cycle of the market" is a testable objective. "Generate 2% a month" is a wish.

**Universe and gate.** Names you would own at the put strike (Lesson 3). Lesson 8's gate: IV percentile at or above 50, implied volatility above 20-day realised, no event inside the expiration unless deliberately priced.

**Structures and defaults.** Cash-secured puts at 25 to 30 delta, 30 to 60 days; covered calls at or above basis after assignment; iron condors on index products at 15 to 20 delta shorts with 5-delta wings; credit spreads when defined risk is required by the budget. Calendars only when the gate fails for low IV and both expirations' implied volatilities are visible.

**Sizing.** Lesson 10: 1% max-loss budget per defined-risk position, shock-loss budget of 2% for cash-secured puts with the full strike in cash, 8% portfolio ceiling on the sum of all short-premium max losses.

**Management.** Profit: close defined-risk trades at 50% of credit. Time: manage every position at 21 days. Loss: close defined-risk trades at two times the credit; for puts on names you want, take assignment; every roll must pass Lesson 9's fresh-trade test in writing.

**Tax hygiene.** Calls with more than 30 days, at or above the lowest qualified benchmark; 31-day wait before re-writing puts on a name sold at a loss; index products where the 60/40 treatment matters.

## The measurement half

**Count total return, not premium.** The premium is inside the basis (Lesson 11) and inside the loss (Lesson 3). A cycle that collects $169 and ends assigned at 92.00 is -$131, not +$169. Mark every position to market at each cycle end; realised and unrealised together.

**Use the right denominator.** For cash-secured puts and covered calls the capital is the strike or the share cost, the full $9,500, because that is the money that could not be elsewhere and that bears the loss. For defined-risk trades it is the max loss, but only if you also report the portfolio ceiling, because a 26% return on $396 is $104. The PUT index does this correctly: puts over a Treasury bill account equal to the strike, with the bill interest counted.

**Include the interest and the costs.** Collateral interest ($46.85 on the chain's put for 45 days at 4%) is part of the return; commissions, bid/ask tolls and assignment fees are part of the cost. Lesson 11's numbers go into the ledger at your rates.

**Benchmark against buy-and-hold on the same names.** The wheel on XYZ is XYZ exposure plus a volatility overlay. The right comparison is 100 XYZ bought on the plan's start date and held, dividends included, over the same dates. The BXM and PUT factsheets do exactly this against the S&P 500 total return index, and the result over 1986 to 2026 was lower return, lower volatility and smaller drawdown. Expect the same shape and measure whether the trade-off was worth it: return per unit of volatility, and maximum drawdown.

**Benchmark against a rule.** A mechanical version of your own strategy, puts sold at a fixed delta and held to expiration, separates the premium from your management. If you cannot beat the rule, the rule is the plan.

**Know how little a year proves.** Suppose your cycle returns have a standard deviation of 4%. After eight 45-day cycles the standard error of your average is 4 / sqrt(8) = 1.41%. To show a 0.5% per-cycle edge at two standard errors you need sqrt(n) = 2 x 4 / 0.5 = 16, so 256 cycles, about 32 years. You will never have that record. What you can have, sooner, is a record that rules out large losses: a drawdown history, a count of budget breaches, a count of rolls that failed the fresh-trade test. Judge the process on those; judge the return only against the benchmark and only with the standard error written beside it.

## Worked example

The Lesson 4 wheel cycle scored under this plan's measurement rules. September 22 to December 18, 87 days, one contract, commissions excluded except the bid/ask toll.

Capital committed: $9,500 (the 95 strike). Collateral interest, leg 1: $46.85.

Ledger, marked at each event:

- Sep 22: sell 95 put, fill 1.64 (toll 0.05). Cash 9,500 + 164 = 9,664; short put marked at its 1.69 mid. Equity 9,664 - 169 = 9,495. Cycle-to-date -0.05%; the toll is the first loss.
- Nov 6, before assignment: XYZ 92.00, put marked at 3.00 intrinsic (-300); collateral interest +46.85. Equity 9,664 + 46.85 - 300 = 9,410.85. Cycle-to-date -0.94%.
- Nov 6, after assignment and call sale: 100 shares at 92.00 = 9,200; cash 9,664 + 46.85 - 9,500 + 283 (call fill 2.83, toll 0.05) = 493.85; short call marked at 2.88 (-288). Equity 9,200 + 493.85 - 288 = 9,405.85. Cycle-to-date -0.99%.
- Dec 18, XYZ 96.50, called at 95.00: cash 493.85 + 9,500 = 9,993.85; no positions. Equity 9,993.85. Cycle return (9,993.85 - 9,500) / 9,500 = 5.20% over 87 days (5.30% before the two tolls). Check: 164 + 283 + 46.85 = 493.85.

Buy-and-hold, 100 XYZ at 100.00 on Sep 22, marked Dec 18 at 96.50: -3.50%. Maximum drawdown along the path: Nov 6 at 92.00, -8.0%. Wheel maximum drawdown along the same path: -0.99% on Nov 6.

Difference on this path: +8.70 percentage points, wheel. Standard error of that difference from one observation: undefined. Record it, do not conclude from it.

Annualised: (1.052)^(365/87) - 1 = 23.7%. Do not put it in the plan. The plan says: after 8 cycles, report the average cycle return, its standard error (4% / sqrt(8) = 1.41% if the dispersion is typical), the maximum drawdown, the number of budget breaches (target zero), and the same figures for buy-and-hold on the same names over the same dates.

## Table

Plan template with the chain's defaults filled in. Replace every number with your own before trading.

| Section | Rule | Chain value |
|---|---|---|
| Objective | Beat buy-and-hold on the same names on return per unit of volatility and maximum drawdown over a full market cycle | Benchmark: 100 XYZ held from Sep 22 |
| Gate | IV percentile >= 50; IV > 20-day realised; no event in expiration | 95th percentile, 28% vs 21% realised, no event: pass |
| Put entry | 25 to 30 delta, 30 to 60 DTE, strike at a price you would pay | Nov 95 put, delta -0.27, 45 DTE, 1.69 |
| Call after assignment | At or above basis, > 30 DTE (qualified) | Dec 95 call, 2.88, basis 93.31 |
| Condor | 15 to 20 delta shorts, 5-delta wings, 30 to 60 DTE | 90/85 + 110/115, credit 1.04 |
| Sizing | 1% defined risk, 2% shock loss on puts, 8% portfolio ceiling | $50k: 1 condor ($396), 1 put (shock $847), total 2.5% |
| Profit management | Close at 50% of credit | Condor at 0.52 |
| Time management | Act at 21 DTE | Oct 16 |
| Loss management | Defined risk: close at 2x credit; puts: assignment or fresh-trade roll test | Condor at 2.08; put: Lesson 9 table |
| Ledger | Mark to market every event; total capital denominator; interest and tolls included | Dec 18: 5.20% on $9,500 |
| Review | After 8 cycles: average, standard error, drawdown, breaches, versus benchmark | 4% / sqrt(8) = 1.41% SE |

## Sources

- Cboe Global Indices, PUT index methodology (the collateral-and-interest accounting used as the measurement standard): https://www.cboe.com/us/indices/dashboard/put/
- Cboe Global Indices, BXM index factsheet (benchmark comparison against the S&P 500 total return index): https://www.cboe.com/us/indices/dashboard/bxm/
- Israelov, R. and Nielsen, L. N. (2014), "Covered Call Strategies: One Fact and Eight Myths", *Financial Analysts Journal* 70(6), on decomposing an income strategy's return into equity, volatility and timing components: https://doi.org/10.2469/faj.v70.n6.3

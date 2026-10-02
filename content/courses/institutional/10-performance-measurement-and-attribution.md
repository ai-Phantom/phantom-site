---
{
  "title": "Performance Measurement, GIPS and Attribution",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {
      "q": "An investor put $100,000 into SPY on December 31, 2021, added $100,000 on June 30, 2022, and held to December 30, 2022. SPY's time-weighted return for 2022 was −18.18%. The investor's money-weighted return was about −10.5%. Why do they differ?",
      "opts": [
        "The time-weighted return includes dividends and the money-weighted does not",
        "The second $100,000 only experienced the second half (+2.26%), so the investor's dollars were mostly exposed to the milder period; TWR strips out the timing of cash flows, MWR keeps it",
        "The money-weighted return is always higher",
        "The investor paid lower fees on the second deposit"
      ],
      "correct": 1,
      "explain": "TWR chains sub-period returns (−19.98% then +2.26%) with equal weight; MWR is the IRR of the actual cash flows, which were larger during the better half."
    },
    {
      "q": "Under the GIPS 2020 standards, which return must a firm present for most composites, and why?",
      "opts": [
        "Money-weighted, because it reflects the client's experience",
        "Gross-of-fee only",
        "Arithmetic average annual return",
        "Time-weighted, because it removes the effect of client-directed cash flows the manager does not control"
      ],
      "correct": 3,
      "explain": "GIPS requires time-weighted returns for composites unless the firm controls the cash flows (for example closed-end private funds), where money-weighted returns are permitted."
    },
    {
      "q": "In the Brinson framework, the allocation effect for a sleeve is:",
      "opts": [
        "(portfolio weight − benchmark weight) x (benchmark sleeve return − total benchmark return)",
        "benchmark weight x (portfolio sleeve return − benchmark sleeve return)",
        "portfolio weight x portfolio sleeve return",
        "(portfolio return − benchmark return) / tracking error"
      ],
      "correct": 0,
      "explain": "Allocation measures the value of over- or under-weighting a sleeve relative to policy, evaluated at benchmark returns; selection measures the value of beating the sleeve benchmark at policy weights."
    },
    {
      "q": "A manager's 2022 active return of +3.87 points came almost entirely from an equal-weight equity sleeve beating the cap-weighted index. Before calling it alpha, what should the allocator check?",
      "opts": [
        "Whether the manager's office is in New York",
        "Whether the manager uses GIPS",
        "Whether the outperformance is explained by factor exposures (size and value both had strong years: HML +25.70% in 2022) that could be bought as an index",
        "Whether the benchmark was rebalanced monthly"
      ],
      "correct": 2,
      "explain": "Alpha is return unexplained by exposures you could have bought cheaply. Equal weighting is a size and value tilt; in 2022 those factors did the work."
    },
    {
      "q": "Dichev (2007) compared dollar-weighted and buy-and-hold returns for major stock markets and found that:",
      "opts": [
        "Investors' dollar-weighted returns were higher, because they timed the market well",
        "Investors' dollar-weighted returns were substantially lower than buy-and-hold, because capital flowed in after rises and out after falls",
        "The two were identical",
        "The study covered only mutual funds"
      ],
      "correct": 1,
      "explain": "Across the NYSE/AMEX, Nasdaq and international markets, dollar-weighted returns trailed geometric buy-and-hold returns by more than a percentage point a year, evidence of poor timing in aggregate."
    }
  ],
  "task": "Compute both your time-weighted and money-weighted return for the last calendar year; if they differ by more than a point, write down which of your cash flows caused it."
}
---

## Three questions, three numbers

"How did we do?" is three questions at an institution, and each has its own number.

*How did the portfolio do?* The time-weighted return (TWR): the return of a dollar left in the portfolio for the whole period, with cash flows stripped out. This is what a manager is judged on, because the manager does not control when the client adds or withdraws money.

*How did the investor do?* The money-weighted return (MWR), the internal rate of return of the actual cash flows. This is what the beneficiary experienced, and it can differ from the TWR by a lot when flows are large and badly timed.

*Why did we get that result?* Attribution: decomposing the difference between the portfolio and its policy benchmark into the decisions that produced it.

Institutions publish all three, in the formats the CFA Institute's Global Investment Performance Standards (GIPS) prescribe, and they insist on net-of-fee figures. Yale's 5.7% for fiscal 2024 and 9.5% for the decade are net of fees and time-weighted; CalPERS's 9.3% is net; Norway's 13.1% is before management costs of 0.04% but its relative return of −0.45 points is reported separately.

## Time-weighted versus money-weighted

TWR is computed by breaking the period at every cash flow, calculating the return of each sub-period, and chaining them: (1 + r₁)(1 + r₂)... − 1. Every sub-period counts equally regardless of how much money was in the portfolio.

MWR solves for the rate r such that the present value of all cash flows, discounted at r, equals the ending value. Money in the portfolio during good sub-periods pulls the MWR up; money in during bad ones pulls it down.

The difference is not academic. Dichev (2007) compared dollar-weighted returns (the MWR of the market as a whole, using aggregate capital flows) with buy-and-hold returns for the US and 19 other markets and found the dollar-weighted returns were substantially lower, on the order of 1.3 percentage points a year for the NYSE/AMEX and more for Nasdaq, because money arrived after rises and left after falls. The gap is the aggregate cost of timing.

GIPS 2020 requires TWR for composites, with MWR permitted only where the firm controls the timing of cash flows (closed-end private funds, for example), and requires that returns be presented net of fees or with a clear fee schedule, that all fee-paying discretionary portfolios be included in a composite so that bad accounts cannot be dropped, and that the firm's claim of compliance be verifiable. The standards exist because the alternative, cherry-picked accounts and gross returns, was the norm.

## Attribution: Brinson

Brinson, Hood and Beebower's method compares the portfolio to its policy benchmark sleeve by sleeve. With policy weights w_b,i, portfolio weights w_p,i, sleeve benchmark returns R_b,i, sleeve portfolio returns R_p,i, and total benchmark return R_b:

- Allocation effect = Σ (w_p,i − w_b,i) × (R_b,i − R_b)
- Selection effect = Σ w_b,i × (R_p,i − R_b,i)
- Interaction = Σ (w_p,i − w_b,i) × (R_p,i − R_b,i)

The three sum to the active return. Allocation asks whether over- or under-weighting a sleeve paid off, evaluated at index returns; selection asks whether the sleeve's manager beat its index at policy weights; interaction is the cross term. Many institutions fold interaction into selection.

## Worked example

**Part A: TWR versus MWR with real prices.** SPY adjusted closes (Yahoo Finance): $445.79 on December 31, 2021; $356.72 on June 30, 2022; $364.77 on December 30, 2022.

Sub-period returns: first half 356.72 / 445.79 − 1 = −19.98%; second half 364.77 / 356.72 − 1 = +2.26%.

TWR = (1 − 0.1998) × (1 + 0.0226) − 1 = 0.8002 × 1.0226 − 1 = −18.18%. This matches SPY's published 2022 total return, as it must.

Investor's path: $100,000 on December 31, 2021 → $80,019 on June 30, 2022. Adds $100,000 → $180,019. Grows 2.26% → $184,082 on December 30, 2022. Total invested $200,000; ending $184,082; dollar loss $15,918.

MWR: solve 100,000 × (1 + r) + 100,000 × (1 + r)^0.5 = 184,082. Try r = −10%: 90,000 + 94,868 = 184,868, slightly high. r = −10.5%: 89,500 + 94,604 = 184,104, close. r = −10.51%: 89,490 + 94,599 = 184,089. So MWR ≈ −10.5%.

The investor lost 10.5% on a money-weighted basis in a year when the fund lost 18.2%, because half the money was only exposed to the +2.26% half. Reverse the flows (add in June and withdraw in December) and the MWR would be worse than the TWR. Neither number is "wrong"; they answer different questions. The manager delivered −18.18%; the investor's timing added 7.7 points.

**Part B: Brinson attribution on a real year.** Policy: 60% US equity (benchmark SPY) and 40% US bonds (benchmark AGG). 2022 sleeve benchmark returns: SPY −18.18%, AGG −13.02%. Policy benchmark return: 0.6 × −18.18 + 0.4 × −13.02 = −16.12%.

The manager ran 55% equity and 45% bonds all year, held the equal-weight S&P 500 ETF (RSP, 2022 return −11.62%) in the equity sleeve, and AGG itself in bonds.

Portfolio return: 0.55 × −11.62 + 0.45 × −13.02 = −6.39 − 5.86 = −12.25%. Active return: −12.25 − (−16.12) = +3.87 points.

Allocation: equity (0.55 − 0.60) × (−18.18 − (−16.12)) = (−0.05) × (−2.06) = +0.10; bonds (0.45 − 0.40) × (−13.02 − (−16.12)) = 0.05 × 3.10 = +0.16. Total allocation +0.26.

Selection: equity 0.60 × (−11.62 − (−18.18)) = 0.60 × 6.56 = +3.94; bonds 0.40 × 0 = 0. Total selection +3.94.

Interaction: equity (−0.05) × 6.56 = −0.33; bonds 0.05 × 0 = 0. Total −0.33.

Sum: 0.26 + 3.94 − 0.33 = +3.87. It reconciles.

**Part C: is it alpha?** The +3.94 of selection came from holding the equal-weight index instead of the cap-weight index. Equal weighting is a small-cap and value tilt, and in 2022 the Fama-French value factor returned +25.70% while the market factor returned −21.32%. The "selection" was a factor exposure the allocator could have bought as an equal-weight index fund for about 0.20%. If the manager charged 0.80%, the net active return is 3.07 points, and the true alpha, after removing what a factor index would have delivered, is close to zero. That is what "alpha after fees" means at an institution: active return, minus fees, minus the part explained by exposures that were available cheaply. Jensen (1968) framed alpha this way for mutual funds and found the average was negative after costs; the definition has not changed, only the list of exposures.

## Table

| Measure | Question it answers | Who it judges | GIPS treatment | Trap |
|---|---|---|---|---|
| Time-weighted return | What did the portfolio earn per dollar continuously invested? | The manager | Required for composites | Ignores that the client's money was not there the whole time |
| Money-weighted return (IRR) | What did the investor's dollars earn? | The investor's timing | Permitted where the firm controls flows | Flattered or punished by flow timing (Dichev's 1.3-point gap) |
| Active return | Did we beat the policy benchmark? | Everyone | Presented alongside benchmark | Meaningless if the benchmark is wrong (Lesson 3) |
| Brinson attribution | Which decision produced the active return? | Board (allocation) vs staff (selection) | Not prescribed; standard practice | Interaction term is often hidden in selection |
| Alpha after fees and factors | Was there skill? | The manager | Net-of-fee presentation required | Most "alpha" is beta or factor exposure |

## What scales down

Compute your TWR from your broker's statements (most report it) and your MWR from your own cash flows once a year. The gap is your timing score, and over a decade it is the most honest measure of whether your decisions about *when* to invest have helped. Then run a two-sleeve Brinson attribution against your policy blend. If most of your active return is "selection" from a fund with a known factor tilt, you now know what you are paying for.

## Sources

- CFA Institute, Global Investment Performance Standards (GIPS) 2020: https://www.gipsstandards.org/standards/
- Brinson, G. P., Hood, L. R., and Beebower, G. L. (1986), "Determinants of Portfolio Performance," *Financial Analysts Journal* 42(4): https://doi.org/10.2469/faj.v42.n4.39
- Dichev, I. D. (2007), "What Are Stock Investors' Actual Historical Returns? Evidence from Dollar-Weighted Returns," *American Economic Review* 97(1): https://doi.org/10.1257/aer.97.1.386
- Jensen, M. C. (1968), "The Performance of Mutual Funds in the Period 1945–1964," *Journal of Finance* 23(2): https://doi.org/10.1111/j.1540-6261.1968.tb00815.x

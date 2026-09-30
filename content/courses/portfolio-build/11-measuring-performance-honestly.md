---
{
  "title": "Measuring Performance Honestly",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A portfolio returns +10% in the first half of a year and −10% in the second. Its time-weighted return for the year is", "opts": ["0%", "−1%", "+1%", "−10%"], "correct": 1, "explain": "Time-weighted return chains the sub-period returns: 1.10 × 0.90 = 0.99, so −1%. It is independent of any deposits or withdrawals."},
    {"q": "Same portfolio, but you deposited $10,000 at mid-year on top of the initial $10,000. Your money-weighted return is about", "opts": ["−1%", "−7.3%", "+4.5%", "−10%"], "correct": 1, "explain": "Solving 10,000(1 + r) + 10,000(1 + r)^0.5 = 18,900 gives r ≈ −7.3%. More of your money was exposed to the bad half than the good half, and money-weighted return captures that."},
    {"q": "Which return should you use to judge the portfolio's construction, as opposed to your own timing?", "opts": ["Money-weighted", "Time-weighted", "Whichever is higher", "Total dollars gained"], "correct": 1, "explain": "Time-weighted return removes the effect of cash flows, so it measures the holdings. Money-weighted return includes your deposits and withdrawals, so it measures the combined result of the holdings and your timing."},
    {"q": "The right benchmark for a 70/30 stock/bond portfolio is", "opts": ["The S&P 500", "A 70/30 blend of a broad stock index and a broad bond index, rebalanced the same way", "Cash", "Whatever index did best last year"], "correct": 1, "explain": "A benchmark should have the same risk as the portfolio. Comparing a 70/30 portfolio with an all-stock index makes it look bad in up years and good in down years for reasons that have nothing to do with skill."},
    {"q": "A portfolio returned 12% with 16% volatility when the risk-free rate was 4%. Its Sharpe ratio is", "opts": ["0.75", "0.50", "3.0", "0.25"], "correct": 1, "explain": "(12 − 4) ÷ 16 = 0.50. Sharpe ratio measures excess return per unit of volatility, so two portfolios with the same return can have very different Sharpe ratios."}
  ],
  "task": "Compute your portfolio's time-weighted return for the last 12 months and compare it with a blended benchmark matching your allocation."
}
---

## Two ways to measure the same year

Most people measure performance by looking at the account balance and remembering roughly what they put in. That number is real, but it is not a return, and it cannot be compared with anything. Two portfolios with identical holdings can show very different results depending on when the money arrived. To measure honestly you need to separate two questions: how did the holdings do, and how did I do?

**Time-weighted return (TWR)** answers the first. It splits the year into sub-periods at each deposit or withdrawal, computes the return of each sub-period from the holdings alone, and chains them together. Cash flows cannot affect it. This is the return that fund fact sheets report and that the CFA Institute's GIPS standards require for comparing managers, because it measures the portfolio rather than the investor's timing.

**Money-weighted return (MWR)**, also called the internal rate of return, answers the second. It finds the single rate that, applied to every cash flow at its actual date, produces the ending balance. If you put most of your money in just before a fall, MWR is worse than TWR. If you added just before a rise, it is better.

Neither is more correct. They answer different questions, and an honest measurement reports both.

## Worked example

You start the year with $10,000. Over the first six months the portfolio rises 10% to $11,000. At the end of June you deposit another $10,000, taking the balance to $21,000. Over the second six months the portfolio falls 10% to $18,900.

**Time-weighted return.** Two sub-periods: +10% and −10%.

TWR = (1.10 × 0.90) − 1 = 0.99 − 1 = −1.0%

The holdings lost 1% for the year. That is the number to compare with a benchmark.

**Money-weighted return.** Find r such that the two deposits, grown at r for their respective time in the portfolio, equal $18,900. The first $10,000 was in for a full year; the second for half a year.

10,000 × (1 + r) + 10,000 × (1 + r)^0.5 = 18,900

Let x = (1 + r)^0.5. Then 10,000x² + 10,000x − 18,900 = 0, or x² + x − 1.89 = 0.

x = [−1 + √(1 + 4 × 1.89)] ÷ 2 = [−1 + √8.56] ÷ 2 = [−1 + 2.926] ÷ 2 = 0.963

1 + r = x² = 0.927, so r = −7.3%.

**Cross-check with the Modified Dietz method**, a standard approximation that weights each cash flow by the fraction of the period it was invested:

MWR ≈ (End − Start − Flows) ÷ (Start + Flows × weight)
= (18,900 − 10,000 − 10,000) ÷ (10,000 + 10,000 × 0.5)
= −1,100 ÷ 15,000
= −7.3%

**Reading the two numbers together.** The holdings returned −1%. You earned −7.3%. The 6.3-point difference is entirely the timing of the second deposit, which arrived just before the bad half. If you were judging the portfolio's construction you would use −1%. If you were judging whether to keep making lump-sum deposits at moments of your choosing, you would use −7.3%, and the answer would be that your timing cost you.

**Dollar amounts, for completeness.** Total deposited $20,000, ending balance $18,900, dollar loss $1,100. This is the number the account statement shows. It is neither return, and comparing it with a benchmark is meaningless without the cash-flow dates.

## Choosing the benchmark

A benchmark is a passive portfolio you could have held instead. For it to be fair, it has to carry the same risk. The S&P 500 is the wrong benchmark for a 70/30 portfolio: in an up year the portfolio will trail it because of the bonds, and in a down year it will beat it for the same reason, and neither says anything about whether the construction was good.

Build a blend that matches the allocation: for a 70/30 portfolio, 70% of a total-market stock index and 30% of a total bond index, rebalanced on the same schedule you use. The cheapest way to track it is to note the returns of VTI and BND (or their indices) and compute the weighted average.

Then compare TWR with the blend. A portfolio of the lesson 7 kind, with 65% in index funds, will track the blend closely, and the difference is the contribution of the satellites. That is what you want to isolate: it tells you, over time, whether the satellite sleeve is earning its place. Lesson 6 suggested raising the sleeve only after a year in which it beat the core it replaced; this is the measurement that decides.

## Risk-adjusted return

Two portfolios that both returned 12% did not do equally well if one had 16% volatility and the other 8%. The Sharpe ratio, from William Sharpe's 1994 paper, divides excess return over the risk-free rate by volatility:

Sharpe = (Portfolio return − Risk-free rate) ÷ Portfolio volatility

At a 4% risk-free rate: (12 − 4) ÷ 16 = 0.50 for the first, (12 − 4) ÷ 8 = 1.00 for the second. The second delivered the same return with half the range of outcomes. Long-run Sharpe ratios for broad stock indices sit around 0.3 to 0.5; a first portfolio measured over a single year will bounce far outside that range, so treat the number as a comparison between your portfolio and its benchmark over the same period, not as an absolute grade.

Alongside Sharpe, record the maximum drawdown for the year. Lesson 9 showed why it is the number that decides whether you keep following the plan.

## Table

| | Time-weighted return | Money-weighted return |
|---|---|---|
| Question answered | How did the holdings perform? | How did my money perform, including my timing? |
| Effect of deposits and withdrawals | None | Fully included |
| Used by | Fund fact sheets, GIPS-compliant managers, benchmarks | Personal accounts, IRR calculations, Morningstar investor-return studies |
| Computation | Chain sub-period returns between cash flows | Solve for the rate that discounts all cash flows to the ending value |
| Worked example result | −1.0% | −7.3% |
| Compare with | A blended benchmark of the same allocation | Your own TWR; the gap is the cost or benefit of timing |
| Weakness | Hides whether your contributions were well timed | Cannot be compared across portfolios with different cash flows |

## The ways measurement lies

**Start-date selection.** A return "since I started" is only comparable if the benchmark is measured from the same date. Any return quoted from a market bottom looks heroic.

**Ignoring cash.** A portfolio that is 20% cash and reports the return of its invested 80% is overstating by a fifth. The cash is part of the portfolio and its return, near the T-bill rate, is in the TWR.

**Ignoring costs.** Spreads, commissions and fund expenses come out of the return. If you compute TWR from statement balances they are already included; if you compute it from index returns of the funds you hold, they are not.

**Survivorship.** If you sold two satellites at their stops and now report the return of the three that remain, you have reported the return of a portfolio you did not hold. The sold positions' returns, up to the day of sale, belong in the record.

**Reporting the better number.** After a year like the worked example, the temptation is to quote −1%. Quote both, and write down why they differ.

## The annual record

Once a year, on the plan review date from lesson 12, record: TWR, MWR, the blended benchmark's return, the difference, the portfolio's volatility and Sharpe ratio, its maximum drawdown, and the same figures for the satellite sleeve on its own. Seven numbers, one line per year. After three years that line is the most useful thing you own, because it will tell you, without flattery, whether the parts of the portfolio you chose are helping.

## Sources

- CFA Institute, Global Investment Performance Standards (GIPS): https://www.gipsstandards.org/
- William F. Sharpe, "The Sharpe Ratio", Journal of Portfolio Management 21(1), 1994: https://doi.org/10.3905/jpm.1994.409501
- Morningstar, "Mind the Gap 2024: A Report on Investor Returns in the U.S.": https://www.morningstar.com/lp/mind-the-gap
- U.S. Securities and Exchange Commission, "Mutual Funds and ETFs: A Guide for Investors": https://www.sec.gov/investor/pubs/sec-guide-to-mutual-funds.pdf

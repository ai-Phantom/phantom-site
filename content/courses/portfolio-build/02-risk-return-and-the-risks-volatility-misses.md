---
{
  "title": "Risk, Return, and the Risks Volatility Misses",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Portfolio A returns exactly 8% every year. Portfolio B alternates +38% and −22%, which also averages 8%. After ten years, which is worth more?", "opts": ["They are equal because the average is the same", "B, because it has bigger up years", "A, because the geometric return of B is only about 3.75% a year", "It depends on which year B starts with"], "correct": 2, "explain": "What compounds is the geometric return, not the arithmetic average. B's two-year growth factor is 1.38 × 0.78 = 1.0764, which is about 3.75% a year. Over ten years A grows to 2.16x and B to only 1.45x."},
    {"q": "Roughly how much does volatility reduce the compounded return relative to the arithmetic average?", "opts": ["By about the standard deviation", "By about half the variance (σ² ÷ 2)", "It does not reduce it", "By exactly 1% per year"], "correct": 1, "explain": "Geometric return is approximately arithmetic return minus half the variance. With a 30% standard deviation the drag is about 0.09 ÷ 2 = 4.5 percentage points a year."},
    {"q": "Which of these risks is NOT captured by the standard deviation of returns?", "opts": ["Day-to-day price fluctuation", "The chance that a single company goes to zero and never recovers", "The width of the range of annual outcomes", "How much the portfolio bounced last month"], "correct": 1, "explain": "Standard deviation measures dispersion around an average and treats up and down moves alike. Permanent loss, liquidity, sequence risk and concentration are different things and need to be tracked separately."},
    {"q": "Bessembinder (2018) found that over 1926 to 2016, net wealth creation in the US stock market above Treasury bills came from roughly what share of listed stocks?", "opts": ["Nearly all of them", "About half", "About 4%", "Exactly one company"], "correct": 2, "explain": "About 4% of stocks accounted for all of the net gain above T-bills; the majority of individual stocks earned less than T-bills over their lifetimes. Diversification is what captures the winners you cannot pick in advance."},
    {"q": "If a stock's daily return standard deviation is 2%, its approximate annualised volatility is", "opts": ["2%", "24%", "32%", "50%"], "correct": 2, "explain": "Annualise by multiplying by the square root of the number of trading days: 2% × √252 ≈ 2% × 15.9 ≈ 32%."}
  ],
  "task": "Compute the geometric return of any holding you own from its last five calendar-year returns and compare it to the simple average."
}
---

## Two returns, one that matters

When someone says a fund "averaged 8%," ask which average. There are two, and the gap between them is where a lot of disappointment lives.

The **arithmetic mean** adds up the yearly returns and divides by the number of years. It is what you get from a calculator and what marketing tends to quote.

The **geometric mean** is the constant annual rate that would have turned the starting balance into the ending balance. It is what your account actually experienced. It is always less than or equal to the arithmetic mean, and the gap grows with volatility.

For a set of yearly returns r₁, r₂ … rₙ:

- Arithmetic: (r₁ + r₂ + … + rₙ) ÷ n
- Geometric: [(1 + r₁)(1 + r₂)…(1 + rₙ)]^(1/n) − 1

A useful approximation links them: geometric ≈ arithmetic − σ² ÷ 2, where σ is the standard deviation of the yearly returns. This term, half the variance, is called volatility drag. It is not a rounding error; for volatile assets it is several percentage points a year.

## Worked example

Two portfolios, each starting at $10,000.

Portfolio A returns 8% every single year.

Portfolio B alternates: +38% in odd years, −22% in even years. Its arithmetic average is (38 − 22) ÷ 2 = 8%, the same as A.

**Geometric return of B.** Every two years B is multiplied by 1.38 × 0.78 = 1.0764. The annual rate is √1.0764 = 1.0375, so B compounds at 3.75% a year, not 8%.

**Check with the approximation.** B's returns are 38% and −22% around a mean of 8%, so each is 30 points from the mean. Standard deviation is 30%, variance is 0.09, and half the variance is 0.045. Arithmetic 8% minus 4.5% gives 3.5%, close to the exact 3.75%.

**Ten-year balances.**

- A: 10,000 × 1.08^10 = 10,000 × 2.1589 = $21,589
- B: 10,000 × 1.0764^5 = 10,000 × 1.4453 = $14,453

Same "average return," a $7,100 gap. Nothing about B was hidden; the arithmetic average simply describes a number that never compounds.

**One more step: what if B's bad year were −30% instead of −22%?** The arithmetic average is still respectable at (38 − 30) ÷ 2 = 4%. But 1.38 × 0.70 = 0.966 per two years, so B now loses 1.7% a year and ends ten years at $8,415. A small increase in the size of the bad years turns a positive average into a shrinking account. This is the arithmetic of why capping losses matters more than chasing gains, and it comes back in lesson 9.

## What standard deviation measures, and what it does not

Standard deviation, usually called volatility, measures how widely returns scatter around their average. For a portfolio with an 8% mean and 15% standard deviation, roughly two years in three land between −7% and +23%, and about one year in twenty lands outside −22% to +38%, if returns were normally distributed. They are not quite, and the tails are fatter than the bell curve implies, but the shape is a serviceable first picture.

To convert daily volatility to annual, multiply by the square root of the number of trading days, about 252. A stock with 2% daily standard deviation has 2% × √252 ≈ 32% annual volatility. Monthly figures multiply by √12.

Volatility is a genuinely useful number. It is the input to the diversification arithmetic in the next lesson, it drives the drag term above, and it scales roughly with how bad a bad year can be. But it has blind spots, and a beginner who tracks only volatility will be surprised by every one of them.

**It treats up and down alike.** A stock that jumps 20% on good news adds as much to volatility as one that falls 20%. You care about the second.

**It says nothing about permanence.** A broad index fund that falls 30% and a single company that falls 30% have the same volatility that month. The index has always recovered eventually; the company may be on its way to zero. Hendrik Bessembinder's 2018 study of every US-listed stock from 1926 to 2016 found that the majority of individual stocks earned less than one-month Treasury bills over their lifetimes, and that all of the net wealth creation above bills came from about 4% of them. Volatility does not distinguish the 4% from the rest.

**It ignores the order of returns.** Two sequences with identical volatility and identical geometric return can produce very different outcomes for someone who is adding or withdrawing money along the way. This is sequence risk, and it is the reason the horizon in lesson 1 matters.

**It ignores whether you can sell.** A private investment, a thinly traded small-cap or a crypto token on an exchange that halts withdrawals can show low volatility right up until the moment you need the cash and there is no bid.

**It ignores leverage.** A position bought on margin has the same volatility as one bought with cash, but a fall that a cash holder can wait out can force a margin holder to sell at the bottom.

## Table

| Risk | What it is | How you see it | How you limit it |
|---|---|---|---|
| Volatility | Width of the range of outcomes | Standard deviation of returns | Diversification, bond allocation |
| Drawdown | Peak-to-trough fall, however long it takes | Max drawdown, time to recover | Allocation sized to the risk budget |
| Permanent loss | A holding that never comes back | Single-name bankruptcies, delistings | Position limits, broad funds in the core |
| Concentration | Too much riding on one name, sector or theme | Largest position as % of total | Hard cap per position, look-through check |
| Sequence | Bad years landing when money is added or withdrawn | Outcome depends on order of returns | Shorter-horizon money in lower-risk buckets |
| Liquidity | Unable to sell at a fair price when needed | Wide spreads, halted trading | Prefer listed, high-volume holdings for money you may need |
| Inflation | Purchasing power falls while nominal value holds | Real return below zero | Do not hold long-horizon money entirely in cash |
| Leverage | Losses can exceed what you can wait out | Margin calls, forced sales | No margin in a first portfolio |

Each row is a separate thing to check. A portfolio can have low volatility and high concentration risk (one stable-looking stock), or high volatility and low permanent-loss risk (a broad small-cap index). You want a view of all of them, not one number.

## Return has to be judged against risk taken

Two portfolios that both returned 10% last year did not necessarily do equally well. If one had 8% volatility and the other 25%, the first delivered the same result with a much narrower range of things that could have gone wrong. The standard way to express this is the Sharpe ratio: excess return over the risk-free rate, divided by volatility. A 10% return with a 4% risk-free rate and 8% volatility gives (10 − 4) ÷ 8 = 0.75. The same return with 25% volatility gives 0.24. Lesson 11 comes back to this in detail; for now, the habit to build is never to look at a return without asking what risk bought it.

The same logic runs the other way. A portfolio that fell 12% in a year when the broad market fell 25% did its job if the job was to lose less. Judging it as a failure because the sign was negative is the mistake that pushes people into more risk right at the wrong moment.

## What this means for construction

Three practical consequences follow from the arithmetic in this lesson.

First, expected return is not the only thing you are buying. Every unit of volatility costs you about half its square in compounded return, so a portfolio that gives up a little average return to cut volatility substantially can end up ahead in dollars. This is the mathematical case for diversification, and the next lesson puts numbers on it.

Second, the big losses dominate. The −22% versus −30% comparison above showed how a modest change in the depth of bad years flips the sign of the compounded result. Rules that cap losses, such as position sizing and rebalancing, are not conservatism for its own sake; they protect the compounding.

Third, track more than one risk. Before you buy anything, be able to say what its volatility is, how far it has fallen from a peak before, whether it can go to zero, how much of your total it would be, and whether you could sell it on a bad day. If you cannot answer those five questions, you do not yet know what you are buying.

## Sources

- Hendrik Bessembinder, "Do Stocks Outperform Treasury Bills?", Journal of Financial Economics 129(3), 2018: https://doi.org/10.1016/j.jfineco.2018.06.004
- William F. Sharpe, "The Sharpe Ratio", Journal of Portfolio Management 21(1), 1994: https://doi.org/10.3905/jpm.1994.409501
- U.S. Securities and Exchange Commission, Investor.gov, "What Is Risk?": https://www.investor.gov/introduction-investing/investing-basics/what-risk
- FINRA, "Asset Allocation and Diversification": https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification

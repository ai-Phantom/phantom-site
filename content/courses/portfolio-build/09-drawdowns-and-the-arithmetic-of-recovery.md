---
{
  "title": "Drawdowns and the Arithmetic of Recovery",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A portfolio falls 40%. The gain required to get back to the previous peak is", "opts": ["40%", "50%", "66.7%", "80%"], "correct": 2, "explain": "Required gain = L ÷ (1 − L) = 0.40 ÷ 0.60 = 66.7%. Losses and gains are not symmetric because the gain is computed on the smaller base."},
    {"q": "The S&P 500 fell 56.8% from October 2007 to March 2009. The gain needed to recover was", "opts": ["56.8%", "100%", "131%", "200%"], "correct": 2, "explain": "0.568 ÷ 0.432 = 1.315, so a 131.5% gain. The index regained its price high in March 2013, about five and a half years after the peak."},
    {"q": "At a steady 7% a year, roughly how long does it take to recover from a 50% drawdown?", "opts": ["About 5 years", "About 7 years", "About 10 years", "About 14 years"], "correct": 2, "explain": "n = ln(1 ÷ 0.5) ÷ ln(1.07) = 0.693 ÷ 0.0677 = 10.2 years. Real recoveries have been faster because post-crash returns exceed the long-run average, but the arithmetic shows how expensive deep drawdowns are."},
    {"q": "In 2008 a 60/40 portfolio of the S&P 500 and the US Aggregate bond index lost about 20%, versus 37% for stocks alone. Its required recovery gain was", "opts": ["20%", "25%", "37%", "59%"], "correct": 1, "explain": "0.20 ÷ 0.80 = 25%, versus 0.37 ÷ 0.63 = 58.7% for the all-stock portfolio. Halving the drawdown more than halves the required recovery."},
    {"q": "Which of these is the correct reason to limit drawdown, given the material in this lesson?", "opts": ["Drawdowns are always permanent", "The recovery gain grows faster than the loss, and a drawdown beyond your tolerance ends the plan because you sell", "Bonds always rise in a crash", "The market never recovers"], "correct": 1, "explain": "Both halves matter. Mathematically, deep losses require disproportionate gains. Behaviourally, a drawdown larger than the stated budget is the point at which most investors abandon the plan, converting a temporary loss into a permanent one."}
  ],
  "task": "Compute the required recovery gain for the drawdown you wrote in lesson 1 and check that you could hold through it."
}
---

## The asymmetry

Lose 10% and you need 11.1% to get back. Lose 50% and you need 100%. Lose 80% and you need 400%. The percentage required to recover a loss grows faster than the loss itself, because the recovery has to be earned on the smaller base.

The formula: if a portfolio falls by a fraction L, the gain required to return to the previous peak is

Required gain = L ÷ (1 − L)

This is the single most important piece of arithmetic in portfolio construction, because it is the reason everything else in this course leans toward limiting losses rather than maximising gains. Lesson 2 showed volatility drag; this is the same effect seen from the bottom of the hole.

## What a drawdown is

A drawdown is the fall from a peak to a subsequent trough, measured as a percentage of the peak. Maximum drawdown is the largest such fall over a period. It has two dimensions: depth, which the formula above prices, and duration, which is the time from the peak until the portfolio makes a new high.

Duration is the part people under-estimate. A drawdown is not over when prices stop falling; it is over when you are back to where you were. For the S&P 500, the four largest drawdowns since 2000, on a price basis:

- March 2000 to October 2002: −49.1%. New high in May 2007. Duration about 7 years and 2 months.
- October 2007 to March 2009: −56.8%. New high in March 2013. Duration about 5 years and 6 months.
- February to March 2020: −33.9%. New high in August 2020. Duration about 6 months.
- January to October 2022: −25.4%. New high in January 2024. Duration about 2 years.

With dividends reinvested the durations are somewhat shorter, roughly four years for the 2007 episode. Either way, two of the four required the investor to sit with a loss for years while the news stayed bad. A plan that assumes recoveries take months has not been tested against the record.

## Worked example

**The 2007 to 2009 drawdown, all-stock portfolio.** The S&P 500 closed at 1,565 on 9 October 2007 and at 677 on 9 March 2009.

- Drawdown: (677 − 1,565) ÷ 1,565 = −56.8%
- Required gain: 0.568 ÷ (1 − 0.568) = 0.568 ÷ 0.432 = 131.5%

At a steady 7% a year, the time to earn 131.5% is:

n = ln(1 + 1.315) ÷ ln(1.07) = ln(2.315) ÷ 0.0677 = 0.839 ÷ 0.0677 = 12.4 years

The actual recovery took about 5.5 years, because the years after March 2009 returned far more than 7%. That is normal: post-crash returns are high because the crash pushed prices below fair value. But it was not knowable in March 2009, and the arithmetic says that if the recovery had been average, it would have taken until 2021.

**Same year, a 60/40 portfolio.** Calendar 2008: S&P 500 −37.0%, Bloomberg US Aggregate +5.2%.

- Portfolio return: 0.6 × (−37.0) + 0.4 × 5.2 = −22.2 + 2.1 = −20.1%
- Required gain: 0.201 ÷ 0.799 = 25.2%
- Time at 7%: ln(1.252) ÷ ln(1.07) = 0.2247 ÷ 0.0677 = 3.3 years

The all-stock investor needed 131% and, at average returns, over twelve years. The 60/40 investor needed 25% and about three years. The bond sleeve did not merely reduce the loss by 17 points; it reduced the recovery required by over 100 points, because the required gain is convex in the loss.

**And in dollars.** On a $100,000 portfolio, the all-stock investor was at $43,200 at the trough and needed $56,800 of gains. The 60/40 investor was at $79,900 and needed $20,100. If both were making $500 monthly contributions, the 60/40 investor's contributions alone would have restored about a third of the loss over three years; the all-stock investor's would have restored about a tenth.

## Table

| Drawdown | Gain to recover | Years to recover at 5% | Years at 7% | Years at 10% |
|---|---|---|---|---|
| 10% | 11.1% | 2.2 | 1.6 | 1.1 |
| 20% | 25.0% | 4.6 | 3.3 | 2.3 |
| 25% | 33.3% | 5.9 | 4.3 | 3.0 |
| 30% | 42.9% | 7.3 | 5.3 | 3.7 |
| 40% | 66.7% | 10.5 | 7.5 | 5.4 |
| 50% | 100.0% | 14.2 | 10.2 | 7.3 |
| 60% | 150.0% | 18.8 | 13.5 | 9.6 |
| 75% | 300.0% | 28.4 | 20.5 | 14.5 |
| 90% | 900.0% | 47.2 | 34.0 | 24.2 |

Years computed as ln(1 ÷ (1 − L)) ÷ ln(1 + r), assuming a constant return and no contributions. Real recoveries vary widely around these figures; the table shows the shape, which is that every step down the left column costs more than the step before.

## The behavioural half

The arithmetic above is only half of why drawdowns matter. The other half is that a drawdown larger than your tolerance is the moment you stop following the plan.

The plan says rebalance into stocks after a fall. At −20% most people can do it. At −35%, with the news uniformly bad and the account showing a five-figure loss, a large fraction of investors sell instead, and the temporary loss becomes permanent. Morningstar's "Mind the Gap" studies, which compare fund returns with the returns investors in those funds actually earned, put the cost of this kind of behaviour at about one percentage point a year over the decade to 2023. Most of that gap is concentrated in the months around drawdowns.

This is why lesson 1 asked for the risk budget in dollars, set as if you were already in the drawdown. The correct allocation is not the one with the highest expected return; it is the one with the highest expected return among those whose worst plausible year you would hold through. An 80/20 allocation that you abandon at −30% has a worse expected outcome than a 60/40 you hold through −20%, because abandoning it locks in the loss and usually misses the recovery.

## Measuring your own drawdown

Track it the same way the index figures above were computed: record the portfolio's highest month-end value to date, and each month express the current value as a percentage below that peak. The largest such figure over the year is your maximum drawdown, and it goes into the annual record from lesson 11 next to the return. A portfolio that returned 9% with a 6% maximum drawdown and one that returned 9% after a 28% maximum drawdown are not the same portfolio, and only the second number tells you which one you can hold.

## Two rules that follow

**Size the portfolio to the drawdown you can hold, not the return you want.** Use the 2008 stress test from lessons 6 and 7. If the number exceeds the budget, add bonds until it does not.

**Decide the drawdown response before the drawdown.** Write down, now, what you will do at −15%, −25% and −35%: probably "rebalance per the rule" at each, and "nothing else." Lesson 10 covers why the written version is the only one that works, and lesson 12 puts it into the plan.

## What recovery looks like from inside

One last point about duration. A recovery is not a return to the previous peak in a straight line. The 2009 to 2013 recovery included a 16% fall in 2010 and a 19% fall in 2011. Each felt, at the time, like the start of the next crash. An investor waiting for things to "feel safe" before returning to the plan would have waited past most of the recovery. The rebalancing rule does not feel; that is its value.

## Sources

- Aswath Damodaran, NYU Stern, "Historical Returns on Stocks, Bonds and Bills: 1928–2023": https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
- Morningstar, "Mind the Gap 2024: A Report on Investor Returns in the U.S.": https://www.morningstar.com/lp/mind-the-gap
- Vanguard Research, "Vanguard's Principles for Investing Success": https://corporate.vanguard.com/content/dam/corp/research/pdf/Principles-for-investing-success.pdf
- U.S. Securities and Exchange Commission, Investor.gov, "Market Indices": https://www.investor.gov/introduction-investing/investing-basics/glossary/market-indices

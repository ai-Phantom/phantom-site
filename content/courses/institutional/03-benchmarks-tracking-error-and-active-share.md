---
{
  "title": "Benchmarks, Tracking Error and Active Share",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {
      "q": "A fund reports annualized tracking error of 5.3% and an active return of +6.6% over the same year. Its realized information ratio is approximately:",
      "opts": [
        "0.8",
        "1.2",
        "5.3",
        "12"
      ],
      "correct": 1,
      "explain": "Information ratio = active return / tracking error = 6.6 / 5.34 ≈ 1.24. This is one year of data, so it is a description of what happened, not evidence of skill."
    },
    {
      "q": "Active share measures:",
      "opts": [
        "The fraction of the year a manager is trading",
        "The standard deviation of returns relative to the benchmark",
        "The manager's share of the fee",
        "The share of portfolio weights that differ from the benchmark's weights"
      ],
      "correct": 3,
      "explain": "Active share = one-half the sum of absolute weight differences between portfolio and benchmark. A pure index fund scores 0%; a portfolio with no benchmark holdings scores 100%."
    },
    {
      "q": "Petajisto's definition of a closet indexer is a fund with active share:",
      "opts": [
        "Between 20% and 60%",
        "Below 20%",
        "Above 80%",
        "Equal to its tracking error"
      ],
      "correct": 0,
      "explain": "In Cremers and Petajisto (2009) and Petajisto (2013), funds with active share under 60% but above the pure-index range are 'closet indexers': they charge active fees for a portfolio that mostly is the benchmark."
    },
    {
      "q": "Which benchmark property is violated by comparing a small-cap value manager to the S&P 500?",
      "opts": [
        "Investable",
        "Specified in advance",
        "Appropriate to the mandate",
        "Measurable"
      ],
      "correct": 2,
      "explain": "A valid benchmark must reflect the manager's actual investment universe and style. The S&P 500 is investable and measurable but not appropriate for a small-cap value mandate, so the comparison mostly measures the size and value factors, not skill."
    },
    {
      "q": "Why can two managers with identical tracking error have very different active share?",
      "opts": [
        "Tracking error is measured after fees and active share before",
        "Tracking error captures factor bets, active share captures stock-level differences; a sector-tilted index-hugger and a stock picker can produce the same return dispersion",
        "Active share is only defined for hedge funds",
        "They cannot; the two measures are mathematically identical"
      ],
      "correct": 1,
      "explain": "A fund that holds the index but overweights one sector has low active share and meaningful tracking error; a diversified stock picker can have high active share and modest tracking error. The two measures describe different kinds of activeness."
    }
  ],
  "task": "Pick the benchmark for your total portfolio (a blend of two or three indexes with fixed weights) and write down why it satisfies the seven criteria in this lesson."
}
---

## Relative to what?

An institution never asks "did we make money?" It asks "did we do what we said, and did it beat the alternative we could have bought for nothing?" The benchmark is that alternative. It is chosen before the period starts, written into the IPS, and used for three separate jobs: it defines the market exposure the allocation is supposed to deliver, it measures the manager's contribution on top of that exposure, and it tells the committee how much deviation from the plan is tolerable.

Norway's fund is the clearest case. Its owner, the Ministry of Finance, sets a benchmark index (roughly 70% global equities, 30% bonds) and a limit on expected deviation from it. In 2024 the fund returned 13.1% and reported that this was 0.45 percentage points below the benchmark; since 1998 it has beaten the benchmark by 0.25 percentage points a year. Those two numbers, and the fact that they are reported at all, are what a benchmark is for.

## What makes a valid benchmark

The CFA Institute's benchmark criteria, adopted in almost every institutional IPS, say a benchmark must be:

1. **Specified in advance.** Chosen before the period, not after you know what did well.
2. **Appropriate.** Consistent with the mandate's universe and style. A small-cap value manager is not benchmarked to the S&P 500.
3. **Measurable.** Its return can be calculated frequently and reliably.
4. **Unambiguous.** The constituents and weights are known.
5. **Reflective of current investment opinions.** The manager knows the securities in it.
6. **Accountable.** The manager accepts it as the standard.
7. **Investable.** You could actually hold it. This is the one that disqualifies most "peer group" and "absolute return" benchmarks: you cannot buy the median endowment or "cash plus 5%".

For a total portfolio, institutions use a *policy benchmark*: the strategic weights from the IPS applied to the sleeve benchmarks. If the policy is 60% US equity and 40% US bonds, the policy benchmark is 60% of the S&P 500 (or a total-market index) plus 40% of the Bloomberg US Aggregate, rebalanced on the same schedule as the policy. Everything the portfolio does differently from that blend is, by construction, an active decision someone should be able to name.

## Tracking error: how far you wander

Tracking error is the standard deviation of the difference between portfolio and benchmark returns, usually annualized. It measures how much the portfolio's path diverges from the benchmark's path, regardless of direction. An index fund has tracking error near zero; a concentrated stock picker might run 6–10%; an endowment with half its assets in private partnerships can have tracking error against a public benchmark in the double digits simply because private marks lag.

The **information ratio** is active return divided by tracking error: how much excess return you got per unit of deviation. It is the relative-return cousin of the Sharpe ratio, and like the Sharpe ratio it is only meaningful over long periods and with a benchmark that fits the mandate.

Institutions budget tracking error explicitly. A pension might allow its public equity sleeve 2% of tracking error, its total fund 1%, and its index mandates 0.1%. This is the risk budget in relative terms (Lesson 9 handles the absolute version).

## Active share: how different you are

Tracking error tells you the *outcome* of deviating; active share tells you the *amount* of deviation in the holdings. Cremers and Petajisto (2009) defined it as one-half the sum of the absolute differences between each security's weight in the portfolio and in the benchmark:

Active share = ½ Σ |w_portfolio,i − w_benchmark,i|

It ranges from 0% (you hold the index) to 100% (you hold nothing in the index). The two measures are different because tracking error is driven mostly by factor and sector bets, while active share is driven by stock-level differences. A fund that holds the index but doubles its technology weight has low active share and real tracking error. A fund that owns 60 stocks equal-weighted from across the index has high active share and can have modest tracking error.

## The evidence on closet indexing

The reason the measure matters is what Petajisto found when he applied it to US equity mutual funds from 1980 to 2009. Funds with active share below 60%, but too high to be explicit index funds, were "closet indexers": portfolios that mostly replicated the benchmark while charging active fees. Their share of fund assets grew to roughly a third by 2009. On average they underperformed their benchmarks after fees by about 0.9% a year, essentially the fee itself, because a portfolio that is 70% the index cannot generate enough active return on the other 30% to pay for the whole thing. The most active stock pickers, with active share above 80%, outperformed after fees by about 1.3% a year on average, though with wide dispersion. Funds that were active mainly through factor timing did worst.

The institutional lesson is not "buy high active share funds". It is that fees should be proportional to active share. If you pay 0.80% for a fund with 40% active share, you are paying 2.0% on the part of the portfolio that is actually active, and the other 60% could have been indexed for 0.05%. Large allocators now compute exactly this "fee per unit of active share" during manager due diligence (Lesson 7).

## Worked example

Two real, dated calculations: one for tracking error and information ratio, one for active share.

**Part A: tracking error of an equal-weight S&P 500 fund against the cap-weighted index in 2022.** The Invesco S&P 500 Equal Weight ETF (RSP) holds the same 500 stocks as SPY but at equal weights, so it is a clean example of a portfolio with modest stock-level activeness and large factor differences (it is smaller-cap and value-tilted). Using Yahoo Finance adjusted closes from December 31, 2021 to December 30, 2022 (251 trading days for each fund):

- SPY 2022 total return: −18.18%
- RSP 2022 total return: −11.62%
- Active return: −11.62 − (−18.18) = +6.56 percentage points

Daily active return (RSP minus SPY) had a mean of +0.029% and a standard deviation of 0.337%. Annualized tracking error = 0.337% × √252 = 5.34%.

Information ratio for the year = 6.56 / 5.34 = 1.23.

Now the interpretation. A tracking error of 5.3% is a lot for a fund holding exactly the benchmark's stocks: it comes entirely from the weights, i.e. from the size and value factors that equal-weighting introduces. And an information ratio above 1 for a single year is unremarkable; it says 2022 was a year when the equal-weight tilt worked, not that it will next year. Institutions insist on at least a full market cycle before an information ratio means anything, and even then they ask whether the same result could have been bought as a factor index for a few basis points.

**Part B: active share of a concentrated portfolio.** Suppose a manager holds 50 S&P 500 stocks at 2.0% each, and those 50 stocks together make up 40% of the index (an average index weight of 0.8% each). The other 450 index stocks, 60% of the index, are not held.

For the 50 held stocks, each contributes |2.0% − 0.8%| = 1.2%, total 50 × 1.2% = 60%.
For the 450 unheld stocks, each contributes |0% − w_i|, total 60%.
Sum = 120%; active share = ½ × 120% = 60%.

Sixty percent is exactly Petajisto's boundary between closet indexing and genuine activity. If the same manager instead held 30 stocks at 3.33% that summed to 25% of the index, the calculation gives 30 × |3.33% − 0.83%| = 75% plus 75% unheld = 150%, so active share = 75%. Concentration raises active share; overlap with the largest index names lowers it, which is why a fund that owns the ten largest S&P 500 companies at index-like weights can never be very active no matter how it trades the rest.

## Table

| Measure | Formula | Units | What drives it | Institutional use |
|---|---|---|---|---|
| Active return | R_p − R_b | % per period | Everything the portfolio does differently | Numerator of the information ratio |
| Tracking error | σ(R_p − R_b), annualized | % | Factor and sector bets, cash drag, private-asset lag | Risk budget in relative terms; mandate limits (Norway sets an expected TE limit) |
| Information ratio | Active return / tracking error | ratio | Skill and luck, over long samples | Manager evaluation over a full cycle |
| Active share | ½ Σ \|w_p − w_b\| | % | Stock-level weight differences | Fee-per-unit-of-activeness screening; closet-index detection (< 60%) |
| Policy benchmark | Σ (policy weight × sleeve index) | % return | The IPS itself | Separates allocation effects from selection (Lesson 10) |

## Scaling it down

Pick a two- or three-index blend that matches your policy weights, rebalance it on paper on the same schedule as your portfolio, and compute your active return against it every quarter. Then compute your active share once: for most individuals who own a few broad ETFs plus some single stocks, it is 10–30%, which means most of the portfolio is the benchmark and the fee and time spent on the active part should be judged accordingly.

## Sources

- Cremers, K. J. M., and Petajisto, A. (2009), "How Active Is Your Fund Manager? A New Measure That Predicts Performance," *Review of Financial Studies* 22(9): https://doi.org/10.1093/rfs/hhp057
- Petajisto, A. (2013), "Active Share and Mutual Fund Performance," *Financial Analysts Journal* 69(4): https://doi.org/10.2469/faj.v69.n4.7
- Norges Bank Investment Management, Government Pension Fund Global Annual Report 2024 (relative return and benchmark): https://www.nbim.no/en/news-and-insights/reports/2024/annual-report-2024/
- CFA Institute, Global Investment Performance Standards (GIPS) 2020, benchmark provisions: https://www.gipsstandards.org/standards/

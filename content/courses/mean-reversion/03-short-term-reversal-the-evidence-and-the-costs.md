---
{
  "title": "Short-Term Reversal in Stocks: The Evidence and the Costs",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Jegadeesh (1990) and Lehmann (1990) documented that stocks with the worst returns over the past month or week tended to:", "opts": ["Keep falling for a year", "Outperform the past winners over the following month or week, before costs", "Match the market exactly", "Be delisted"], "correct": 1, "explain": "Both papers found a statistically strong contrarian effect at one-month and one-week horizons on CRSP data. Both also noted that the strategy turns over its entire portfolio every period, which is where the costs come from."},
    {"q": "In the course's 20-stock test (611 weeks, 2015 to 2026), buying the five worst prior-week names and shorting the five best earned a gross spread of:", "opts": ["+0.094% per week with a t-statistic of 0.72, not distinguishable from zero", "+2% per week", "−1% per week", "+0.094% per week with t = 6"], "correct": 0, "explain": "The long leg made +0.616% per week and the short leg +0.521%, a spread of +0.094% with a weekly standard deviation of 3.24%. In mega-caps over this period the reversal is barely there before costs."},
    {"q": "The reversal portfolio replaces all ten positions every week. With a cost of c per side, the weekly cost drag on the long-short spread is about:", "opts": ["c", "2c", "4c", "10c"], "correct": 2, "explain": "Each leg is opened and closed every week (two sides), and there are two legs, so 4c. At 5 basis points per side that is 20 bp per week, roughly 10% per year, against a gross spread of 5% per year."},
    {"q": "Avramov, Chordia and Goyal (2006) found that short-term reversal profits are concentrated in:", "opts": ["The largest, most liquid stocks", "Illiquid, high-turnover stocks, where the costs of trading are highest", "Stocks with no news", "Stocks listed after 2000"], "correct": 1, "explain": "The reversal is largest exactly where it is most expensive to capture. That is consistent with Nagel's (2012) reading of reversal returns as compensation for providing liquidity, not a free lunch."},
    {"q": "In the worked example week (formation 2026-09-04 to 09-11, holding to 09-18), the losers averaged +0.804% and the winners +0.178% the following week. The correct lesson is:", "opts": ["The strategy always works", "One week is one observation of a noisy variable with a weekly standard deviation of 3.2%; the 611-week average is what to size by, and that average is close to zero after costs", "Mega-caps revert strongly", "The winners should have been bought"], "correct": 1, "explain": "A single +0.63% week is well inside one standard deviation of the weekly spread. The lesson is in the long-run average and its t-statistic, not in any one week."}
  ],
  "task": "Pick ten liquid stocks, rank them on last week's return, and record this week's return of the three worst and three best; repeat for four weeks and compute the average spread."
}
---

The academic case for short-term reversal is one of the oldest in the anomalies literature and one of the most consistently replicated. It is also the clearest example of a real statistical effect that a retail trader mostly cannot collect, because the effect is small per period and the strategy trades constantly. This lesson gives you the papers, then tests the rule on twenty large stocks and puts a cost on it, so you can see exactly where the money goes.

## The papers

Jegadeesh (1990) sorted NYSE and AMEX stocks each month on their prior-month return and found that the decile of biggest losers beat the decile of biggest winners over the next month by roughly 2% per month over 1934 to 1987, a striking number that persists after controlling for size and beta. Lehmann (1990) did the same at the weekly horizon: a portfolio that bought last week's losers and sold last week's winners, weighted by how far each had moved, was profitable in most weeks of 1962 to 1986, with the profits concentrated in the first week after formation.

Both papers were careful to say the effect might not be capturable. Lehmann's strategy turned over its entire portfolio every week; Jegadeesh's every month. Later work made this the central issue. Avramov, Chordia and Goyal (2006) showed the reversal is concentrated in illiquid stocks with high turnover. Nagel (2012) interpreted the return to reversal as the price of liquidity provision: when you buy last week's losers you are absorbing the inventory that other traders needed to dump, and you get paid more for that when volatility is high and market-makers are stretched. Novy-Marx and Velikov (2016) put reversal in a table with fifty other anomalies ranked by turnover and estimated that its net-of-cost return is negative for the standard construction, because it trades more than any other strategy they considered.

So the literature's summary is: the effect exists, it is largest where it is most expensive, and the naive version does not survive costs. What survives is a very selective version, run by people with very low costs.

## Worked example

The universe is the twenty large U.S. stocks used throughout this course: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, JPM, V, UNH, LLY, XOM, COST, HD, PG, NFLX, CAT, WMT, JNJ. Daily bars come from Yahoo Finance's chart API (`interval=1d`, explicit `period1`/`period2`), pulled 2026-09-24. Dividend-adjusted closes are used because the strategy holds across ex-dividend dates. Weeks end on the last trading day of each ISO week, which gives 613 week-ends from 2015-01-02 to 2026-09-23 and 611 pairs of a formation week followed by a holding week.

**The rule.** At each week-end, rank the twenty stocks on that week's return. Buy the five lowest, sell short the five highest, equal-weighted within each leg, one dollar long against one dollar short. Hold one week. Repeat.

**One week in full.** Formation week 2026-09-04 to 2026-09-11, holding week to 2026-09-18. The five losers and what they did next:

- NVDA: formation −5.13% (adjusted close 230.10 to 218.29); holding **+1.82%** (to 222.27)
- UNH: −4.55%; holding +0.03%
- HD: −3.83%; holding −2.84%
- JNJ: −3.51%; holding +1.66%
- LLY: −2.93%; holding +3.34%

Long leg average: (1.82 + 0.03 − 2.84 + 1.66 + 3.34) / 5 = **+0.804%**.

The five winners:

- AVGO: formation +1.14%; holding −1.21%
- TSLA: +3.21%; holding −0.32%
- AAPL: +3.84%; holding +1.16%
- XOM: +4.09%; holding −1.48%
- META: +5.07%; holding +2.73%

Short leg average: (−1.21 − 0.32 + 1.16 − 1.48 + 2.73) / 5 = **+0.178%**. Because you are short, that leg cost you 0.178%.

Spread for the week: 0.804 − 0.178 = **+0.626%** gross. Now the cost. Ten positions opened at the start of the week and ten closed at the end is twenty executions on two legs. Per unit of capital on each leg, that is two sides per leg per week, so 4 × c on the spread. At c = 5 basis points (a reasonable all-in figure for a mega-cap: a 1 to 2 bp half-spread plus slippage), the drag is 20 bp: 0.626 − 0.200 = **+0.426%** net. A good week.

**All 611 weeks.** Long leg mean **+0.616%** per week. Short leg mean **+0.521%** per week. Spread mean **+0.094%** per week, standard deviation 3.24%, positive in 52.5% of weeks. The t-statistic is 0.094 / 3.24 × √611 = **0.72**. Annualised (×52) the gross spread is +4.9%.

Net of 5 bp per side: 0.094 − 0.200 = **−0.106%** per week, about −5.5% per year. Net of 10 bp per side: **−0.306%** per week, −15.9% per year, t = −2.33. For comparison the equal-weighted average of all twenty stocks returned +0.485% per week; both legs are mostly just long or short the market, and the difference between them is small and noisy.

Notice that the short leg's average return was positive. Over eleven years in which these twenty names roughly quadrupled, you were short five of them at all times. Even the losers-minus-winners construction, which is market-neutral on paper, is long a small, unstable reversal effect and short a large, steady drift.

## Table

| Year | Weeks | Mean spread per week | Cumulative spread, gross |
|---|---|---|---|
| 2015 | 51 | −0.106% | −7.3% |
| 2016 | 52 | +0.241% | +11.8% |
| 2017 | 52 | +0.034% | +0.6% |
| 2018 | 52 | +0.940% | +59.1% |
| 2019 | 52 | +0.049% | +0.8% |
| 2020 | 53 | +0.186% | +4.4% |
| 2021 | 52 | −0.335% | −18.0% |
| 2022 | 52 | −0.092% | −7.2% |
| 2023 | 52 | −0.447% | −23.7% |
| 2024 | 52 | +0.137% | +3.7% |
| 2025 | 52 | −0.100% | −7.7% |
| 2026 (to 09-23) | 39 | +0.795% | +33.3% |

Twenty large stocks, five losers long against five winners short, weekly rebalance, before costs. Source: Yahoo Finance adjusted closes, computed by the course.

## Reading the table

Two years, 2018 and the first nine months of 2026, carry the whole result. Both were years with sharp, short sell-offs followed by fast recoveries in individual mega-caps, the environment in which last week's loser is next week's bounce. 2021 and 2023, years when leadership was persistent, were the worst: the losers kept losing and the winners kept winning, which is momentum eating reversal. The by-year sign is not something you could have forecast.

This is what the literature predicted for large, liquid stocks: a weak effect with a weekly standard deviation thirty times its mean. The strong version lives in small illiquid names, and there the round-trip cost is not 10 bp but 50 to 200. Nagel's framing tells you who does collect it: firms that are already providing liquidity, whose cost per side is close to zero and who are being paid to hold inventory. If that is not you, the cross-sectional reversal strategy is a thing to understand, not a thing to run. The rest of this course turns to the versions of reversion where the trade count is low enough that costs do not dominate: rare extreme readings on a single index, and spreads between two instruments.

## Sources

- Jegadeesh, N. (1990). Evidence of predictable behavior of security returns. *Journal of Finance*, 45(3), 881–898. https://doi.org/10.1111/j.1540-6261.1990.tb05110.x
- Lehmann, B. N. (1990). Fads, martingales, and market efficiency. *Quarterly Journal of Economics*, 105(1), 1–28. https://doi.org/10.2307/2937816
- Avramov, D., Chordia, T. and Goyal, A. (2006). Liquidity and autocorrelations in individual stock returns. *Journal of Finance*, 61(5), 2365–2394. https://doi.org/10.1111/j.1540-6261.2006.01060.x
- Novy-Marx, R. and Velikov, M. (2016). A taxonomy of anomalies and their trading costs. *Review of Financial Studies*, 29(1), 104–147. https://doi.org/10.1093/rfs/hhv063

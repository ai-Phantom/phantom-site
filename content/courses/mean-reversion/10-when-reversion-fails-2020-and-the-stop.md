---
{
  "title": "When Reversion Fails: Regime Change, 2020 and the Stop That Must Exist",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Using 2018-2019 formation statistics (β = 2.38), the XOP-on-XLE z-score in 2020 peaked at:", "opts": ["+3.5", "+4.7", "+14.25 on 2020-03-23", "+2.3"], "correct": 2, "explain": "A '2 standard deviation' entry on 2020-02-27 was followed by a move to 14.25 standard deviations. Standard deviations estimated in a calm regime say nothing about the size of moves in a different one."},
    {"q": "The short-spread trade entered 2020-02-27 with no stop, held to year-end, lost $3,825 net on a $10,000 XOP leg. Its worst mark-to-market during the year was:", "opts": ["−$3,825", "−$6,488", "−$1,851", "−$579"], "correct": 1, "explain": "On 2020-03-23 the position was marked at −$6,488, 19% of the $33,767 gross notional, before recovering about half. A trader sized for a 2 s.d. move would have been forced out near the bottom."},
    {"q": "With a stop at 4 standard deviations, the same trade exited on 2020-03-10 for −$1,851 and, because the rule does not re-enter until |z| falls back inside 2, took no further 2020 trades. That is:", "opts": ["Worse than no stop, because the no-stop trade recovered", "Half the year-end loss and 29% of the worst mark, at the price of never participating in the partial recovery; the stop bought a known loss in place of an unknown one", "A profit", "Irrelevant, because stops do not work in pairs"], "correct": 1, "explain": "The stop's value is not that it always improves the outcome; it is that it caps the distribution. The GDX/GLD case in the same year shows a stop that cost money, and the point is you cannot tell the two cases apart in advance."},
    {"q": "In the same year, the GDX-on-GLD spread hit −11.66 on 2020-03-13 and then fully reverted; the no-stop long-spread trade made +$1,081 after a −$2,759 mark. What should you conclude?", "opts": ["Stops are unnecessary for gold pairs", "That the same stopless approach that lost $3,825 on energy made $1,081 on gold, in the same month, for reasons that were not knowable in advance; a rule that survives both cases needs the stop", "That GDX is safer than XOP", "That 2020 was a good year for pairs"], "correct": 1, "explain": "One pair's spread was driven by a permanent shift (oil producers with negative crude), the other's by a liquidation that reversed in weeks. Ex ante they looked identical: a 2 s.d. deviation that kept growing."},
    {"q": "Haddad, Moreira and Muir (2021) and He, Nagel and Song (2022) document March 2020 spread blowouts in:", "opts": ["Only equity pairs", "Investment-grade bond ETFs trading at discounts to net asset value, and the Treasury cash-futures basis, both of which were 'riskless' arbitrages until the arbitrageurs' funding disappeared", "Cryptocurrencies", "Gold only"], "correct": 1, "explain": "Reversion trades are short liquidity. When every liquidity provider needs to reduce risk at once, every spread widens together, which is exactly when a stop that depends on the spread reverting will not be hit."}
  ],
  "task": "For your own pair, compute the z-score through February and March 2020 using 2018-2019 formation statistics, and note the maximum absolute value it reached."
}
---

Every reversion rule in this course has, so far, been allowed to hold until the reversion arrives. That is how the rules are usually described and it is how they blow up. This lesson replays 2020 on two pairs with the formation statistics a trader would actually have had, shows a 2 standard-deviation entry turning into a 14 standard-deviation loss, and sets out the stop that has to exist before the first trade is placed. Along the way it visits the other spreads that broke in March 2020, because the mechanism was the same everywhere.

## Why reversion trades fail together

A reversion trade sells what has just been bought in a hurry and buys what has just been sold in a hurry. It is a liquidity-provision trade, and its return, per Nagel (2012), is the fee for holding inventory that someone else needed to be rid of. In ordinary times that fee is paid reliably. When the whole market needs to reduce risk at once, three things happen: the inventory keeps coming, the price of providing liquidity spikes, and the liquidity providers themselves are forced to sell. Spreads that had reverted for years widen together, and the traders holding them are the ones being liquidated.

March 2020 was that in its purest form. Haddad, Moreira and Muir (2021) document investment-grade bond ETFs trading at discounts of 5% and more to their net asset values, an arbitrage that authorised participants normally close within a day, persisting for weeks until the Federal Reserve announced it would buy the ETFs. He, Nagel and Song (2022) show the Treasury cash-futures basis, one of the most crowded relative-value trades in the world, blowing out as levered funds were forced to unwind. Neither spread had a fundamental reason to change; both changed because the capital that kept them closed disappeared.

Equity pairs are not exempt, and some of them had a fundamental reason on top of the liquidity one.

## Worked example

Data: Yahoo Finance daily closes, `interval=1d`, pulled 2026-09-24. Formation window 2018-01-02 to 2019-12-31 (503 days), the window a trader would have used entering 2020. Rule: formation-statistics z-score, enter at ±2, exit at 0. Variants add a stop at |z| = 4 (or 3) and a 60-day time stop, and re-arm the entry only after |z| has come back inside 2. $10,000 on the Y leg, 0.05% per side, 0.5% annual borrow.

**XOP on XLE.** Formation β = **2.3767**, residual s.d. 0.0734, DF t = −2.39 (not cointegrated even then). The position per $10,000 of XOP is $23,767 of XLE, gross $33,767.

Entry 2020-02-27: XOP 59.32, XLE 22.66, z = **+2.30**. Short the spread: short $10,000 XOP, long $23,767 XLE.

What crude oil did next needs no retelling. Between 2020-02-19 and 2020-03-18, XLE fell from 27.42 to 11.99 (−56.3%) and XOP from 76.52 to 31.08 (−59.4%). Similar percentage falls, but the position held 2.38 dollars of XLE for every dollar of XOP, so it was net long $13,767 of energy into the collapse. The z-score:

- 2020-03-09: +3.50
- 2020-03-10: +4.69
- 2020-03-18: +14.10
- 2020-03-23: **+14.25**, the peak
- 2020-04-20: +8.29 (the day WTI settled below zero)
- 2020-06-30: +6.38
- 2020-12-31: +7.89

No stop, held to year-end: XOP 58.50 (−1.38% on entry), XLE 18.95 (−16.37%). Gross = −10,000 × (−0.0138) + 23,767 × (−0.1637) = +138 − 3,891 = **−$3,753**; with $33.77 transaction cost and $42.46 borrow, net **−$3,825**. The worst mark, on 03-23, was **−$6,488**. The spread ended the year at 7.89 standard deviations; it never came back, because the 2018-2019 relation between an equal-weighted producer basket and a cap-weighted integrated-oil basket was not the relation that held after producers were re-priced for negative crude.

Stop at 4σ: exit 2020-03-10 at z = 4.69. XOP 39.72 (−33.04%), XLE 17.77 (−21.58%). Gross = +3,304 − 5,129 = **−$1,825**; net **−$1,851** after $33.77 costs and $1.59 borrow. Then nothing: |z| never fell back inside 2 in 2020, so the re-arm condition kept the rule out for the rest of the year. Stop at 3σ: exit 2020-03-09 at z = 3.50, net **−$1,495**.

**GDX on GLD.** Formation β = 1.7852, residual s.d. 0.0359, DF t = **−3.01**, the closest to passing of any window in the course. Entry 2020-01-28 at z = −2.05, long the spread: long GDX, short $17,852 GLD.

Between 02-19 and 03-18 GLD fell 7.3% and GDX 33.8%: gold held, miners were liquidated. z reached **−11.66** on 2020-03-13. The no-stop trade was marked at **−$2,759** at its worst. Then it reverted: GDX went from 19.68 on 03-18 to 36.02 by year-end (+83%) against GLD +27%, z crossed zero on 2020-05-19, and the trade closed at gross +$1,137, net **+$1,081**. Two further no-stop trades in 2020 made +$856 and lost −$889 (the last still open at year-end at z = −4.73), for a year's net of +$1,048.

With the 4σ stop: the first trade stopped on 2020-02-27 at −4.29 for **−$858**, the rule re-armed on 04-30, and five trades over the year netted **+$305**. With a 3σ stop, six trades netted **+$11**. On this pair, in this year, the stop cost money.

## Outcomes under each rule

| Pair, 2020, 2018-2019 formation stats | Rule | Trades | First exit | Worst mark | Net for the year |
|---|---|---|---|---|---|
| XOP on XLE (β 2.38) | No stop, exit at 0 | 1 (open at year-end, z +7.89) | — | −$6,488 | −$3,825 |
| XOP on XLE | Stop 4σ, time 60 d, re-arm | 1 | 2020-03-10 at z +4.69 | −$1,815 | −$1,851 |
| XOP on XLE | Stop 3σ, time 60 d, re-arm | 1 | 2020-03-09 at z +3.50 | −$1,460 | −$1,495 |
| GDX on GLD (β 1.79) | No stop, exit at 0 | 3 (last open, z −4.73) | 2020-05-19 at z +0.27 | −$2,759 | +$1,048 |
| GDX on GLD | Stop 4σ, time 60 d, re-arm | 5 | 2020-02-27 at z −4.29 | −$823 | +$305 |
| GDX on GLD | Stop 3σ, time 60 d, re-arm | 6 | 2020-02-27 at z −4.29 | −$823 | +$11 |

$10,000 on the Y leg, β × $10,000 on the X leg; 0.05% per side, 0.5% annual borrow. Source: Yahoo Finance daily closes, computed by the course.

## Chart

![Z-score of the XOP versus 2.38 × XLE log spread through 2020, standardised by 2018-01-02 to 2019-12-31 formation statistics, with the +2 entry, +4 stop and 0 exit bands. The 2020-02-27 entry, the 2020-03-10 stop-out and the 2020-03-23 peak of +14.25 are marked with the corresponding marks on a $10,000 XOP leg. Source: Yahoo Finance daily closes, computed by the course.](figures/xle-xop-zscore-2020.svg)

## The stop that must exist

The table shows the stop losing money on one pair and saving it on the other, and that is the argument for it, not against. Before 2020-02-27 the two situations were indistinguishable: a 2σ deviation in a pair that had co-moved for years. One turned out to be a permanent re-pricing and one a six-week liquidation. You do not get to know which. What you get to choose is the shape of the distribution: with no stop, outcomes from −$6,488 to +$1,081; with a 4σ stop, from −$1,851 to +$305. The stop converts an unbounded loss into a bounded one and pays for it with a share of the recoveries.

Three components, all set before entry:

**A z-stop** at 3 to 4 standard deviations. Its logic is statistical: if the formation window is representative, |z| beyond 4 is an event of vanishing probability, so reaching it is evidence that the formation window is not representative. You are not stopping because the trade is losing; you are stopping because the model is wrong.

**A time stop** at two to three half-lives (lesson 9), for the trade that neither reverts nor blows out. The GDX/GLD trade entered 2020-07-30 sat 60 days going nowhere and was closed at −$227; the no-stop version of the same trade was open at year-end at −$889.

**A re-arm condition**: after a stop, no new entry until |z| is back inside the entry band. Without it, the rule re-enters the next day at 4.7σ, is stopped again, and turns a single loss into a sequence. In 2020 the re-arm kept the XOP/XLE rule flat from March onward, which was the correct trade.

None of this makes the pair safe. The XOP/XLE 4σ stop still cost 5.5% of gross notional in eight trading days, on a "market-neutral" position. It made the loss survivable, and survivable is the only thing a stop can promise.

## Sources

- Haddad, V., Moreira, A. and Muir, T. (2021). When selling becomes viral: disruptions in debt markets in the COVID-19 crisis and the Fed's response. *Review of Financial Studies*, 34(11), 5309–5351. https://doi.org/10.1093/rfs/hhab022
- He, Z., Nagel, S. and Song, Z. (2022). Treasury inconvenience yields during the COVID-19 crisis. *Journal of Financial Economics*, 143(1), 57–79. https://doi.org/10.1016/j.jfineco.2021.05.044
- Nagel, S. (2012). Evaporating liquidity. *Review of Financial Studies*, 25(7), 2005–2039. https://doi.org/10.1093/rfs/hhs066
- Yahoo Finance historical data: XOP https://finance.yahoo.com/quote/XOP/history/ and GDX https://finance.yahoo.com/quote/GDX/history/

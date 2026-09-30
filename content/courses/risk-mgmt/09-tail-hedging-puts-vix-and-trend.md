---
{
  "title": "Tail Hedging: Puts, VIX Products and Trend Followers",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The Cambria Tail Risk ETF (TAIL), which holds Treasuries plus a ladder of out-of-the-money S&P puts, returned +28.4% between 2020-02-19 and 2020-03-23 while SPY fell 33.7%. Its calendar-year returns 2019 to 2024 were −14.3%, +6.9%, −12.8%, −13.1%, −13.3%, −9.6%. What is the cost of the hedge?", "opts": ["Nothing; it made money in 2020", "The management fee", "Only the 2019 loss", "Roughly 10 to 14% a year in every calm year, which over the fund's life from 2017-04-06 to 2026-09-23 summed to −52.9% while SPY made +278%"], "correct": 3, "explain": "A put ladder bleeds premium in every year that does not contain a crash. The 2020 payoff was real and the bleed around it was larger. Israelov's finding is that this is the normal state of protective puts: the insurance is priced above its actuarial value."},
    {"q": "A 95/5 SPY/TAIL blend rebalanced monthly from 2017-05-01 to 2026-09-23 returned 14.05% a year with a −31.0% worst drawdown, versus 15.1% and −33.7% for SPY alone. What did 5% in puts buy?", "opts": ["A large reduction in drawdown", "A higher return", "About 2.7 points off the worst drawdown and 1.6 points of vol, for 1.05 points a year of return; a small, expensive improvement", "Nothing measurable"], "correct": 2, "explain": "The hedge helped in the crash and cost every other month. Netted over nine years, a 5% allocation to OTM puts bought a modest drawdown improvement at a price of about one point of annual return. Whether that is worth it depends on the funding constraint, not on the average."},
    {"q": "VIXY, a short-term VIX futures ETF, returned +278% from 2020-02-19 to 2020-03-23 and +404.9% to its 2020-03-18 peak. Since 2011-01-04 it has lost essentially 100% of its value. What explains both facts?", "opts": ["Bad management", "VIX futures are usually in contango, so a long position pays roll yield every month; the product is the purest crash payoff available and the most expensive to hold, losing 25% to 73% in each calm year", "The VIX index fell", "Leverage"], "correct": 1, "explain": "Calendar-year returns of −67.8% (2019), −72.4% (2021), −72.7% (2023) are the roll cost. A hedge that halves or worse in a calm year has to be sized so small that its crash payoff, even at 4x, barely moves the book."},
    {"q": "DBMF, a managed-futures trend ETF, lost 6.6% in the 2020 crash window but returned +21.6% in 2022 while SPY lost 18.2% and TLT lost 31.2%. What does that say about trend following as a tail hedge?", "opts": ["It pays in slow bears where a trend has time to form, and not in fast crashes where the signal has not turned yet; it is the complement of a put, not a substitute", "It is useless", "It only works in bond markets", "It always pays in crashes"], "correct": 0, "explain": "Hurst, Ooi and Pedersen document positive trend-following returns in most large equity drawdowns over a century, but the mechanism is that the drawdown lasts long enough for positions to flip. March 2020 was too fast; 2022 was ideal."},
    {"q": "An 80/20 SPY/DBMF blend from 2019-06-01 to 2026-09-23 returned 15.8% a year with a −28.5% worst drawdown against 16.84% and −33.7% for SPY. Compared with the 95/5 put blend, the trend blend", "opts": ["cost more and protected less", "was identical", "cost about the same in return (one point a year) but the hedge asset itself made money over the period (+98%), so the cost was diversification drag rather than premium bleed, and the drawdown reduction was larger", "cannot be compared"], "correct": 2, "explain": "Puts are a negative-carry asset by construction; a trend program is a positive-expected-return asset with crisis-convex behaviour. Over a long calm period the second is far cheaper to own, at the price of not reliably paying in the first three weeks of a crash."}
  ],
  "task": "For each of the three hedge types, write down what it would have paid your book in March 2020 and in 2022, and what it would have cost in 2023 and 2024."
}
---

## What a tail hedge is for

Lessons 3 through 7 manage risk by adjusting exposure: vol targeting, VaR limits, drawdown rules. All of them share a weakness: they act after the move has started, and a gap can put the move in front of them. A tail hedge is a position that pays when the book loses, held in advance, so that the first day of a crash is covered without anyone doing anything.

The three instruments that do this are out-of-the-money index puts, long volatility products, and trend-following programs. They differ in what they cost in calm years, how fast they pay in a crash, and whether they pay at all in a slow bear. The evidence on all three is unusually good, because each has a liquid ETF proxy with a track record that includes two very different crises.

## Puts

A put ladder on the index, typically 10% to 30% out of the money, one to three months out, rolled continuously. It pays as a function of the index level, so it pays on day one of a crash, with no dependence on a signal.

The cost is the premium. Israelov (2019) computed the return of protective puts on the S&P 500 and found that a continuously held put position reduced the portfolio's returns by more than it reduced its drawdowns, because index puts are priced above their actuarial value: the same variance risk premium that shows up as VIX above realised vol in lesson 3 shows up here as put-buyers overpaying. Ilmanen (2012) surveyed the evidence across asset classes and found that buying insurance, whether as index puts or as long volatility, has had negative long-run returns, and selling it positive returns, in essentially every market examined.

The proxy: TAIL, the Cambria Tail Risk ETF, launched 2017-04-06, holds intermediate Treasuries and spends a few percent a year on a ladder of OTM S&P puts.

## VIX products

Long positions in VIX futures, through an ETF such as VIXY (short-term VIX futures, since 2011). They pay when implied volatility spikes, which happens in the first days of any crash, so they are the fastest hedge and the most convex: VIXY quadrupled in four weeks in 2020.

The cost is the roll. VIX futures are in contango most of the time, which means the next month's contract costs more than the one expiring. A long position sells low and buys high every month, and the drag runs to 50% or more a year in calm markets. Over its life since 2011 VIXY has lost effectively all of its value, against a 697% gain for SPY.

## Trend followers

A managed-futures program that goes long or short a broad set of futures by their recent trend. It pays in crises because crises are trends: equities down, bonds up or down, dollar up, commodities moving. Hurst, Ooi and Pedersen (2017) document positive trend-following returns in the large majority of the worst equity drawdowns since 1880, including 1929-32, 1973-74, 2000-02 and 2008.

The cost is different in kind. A trend program has a positive expected return of its own, so it does not bleed premium; the drag on a blended book is the diversification into an asset that, in a strong equity bull market, returns less than equities. The weakness is speed: it takes weeks for trend signals to flip, so a three-week crash from an all-time high catches the program long equities.

The proxies: DBMF (since 2019-05-08) and KMLM (since 2020-12-02).

## Worked example

Yahoo Finance adjusted closes, total returns including distributions. All blends are rebalanced monthly to target weights.

**Calendar years, 2018 to 2026 year-to-date (through 09-23):**

SPY: −4.6, +31.2, +18.3, +28.7, −18.2, +26.2, +24.9, +17.7, +13.5.
TAIL: +2.9, −14.3, +6.9, −12.8, −13.1, −13.3, −9.6, +5.5, −12.5.
VIXY: +66.8, −67.8, +10.5, −72.4, −25.0, −72.7, −27.4, −43.0, −34.5.
DBMF: n/a, +10.7 (from May), +1.8, +11.5, +21.6, −8.9, +7.2, +13.8, +16.7.
KMLM: n/a, n/a, +5.4 (from Dec), +7.0, +24.2, −5.7, −1.7, −3.0, +19.7.
TLT: −1.6, +14.1, +18.2, −4.6, −31.2, +2.8, −8.1, +4.2, −4.9.
BIL: +1.7, +2.0, +0.4, −0.1, +1.4, +4.9, +5.2, +4.1, +2.6.

**Crash windows:**

2020-02-19 to 2020-03-23 (SPY −33.7%): TAIL **+28.4%** (peak +28.5% on 04-02). VIXY **+278.3%** (peak +404.9% on 03-18). DBMF **−6.6%**. TLT +14.2%. GLD −3.6%.

2022-01-03 to 2022-10-12 (SPY −24.5%): TAIL **−3.9%**. VIXY **+19.6%**. DBMF **+31.5%**. KMLM **+47.7%**. TLT −29.3%. GLD −7.3%.

2025-02-19 to 2025-04-08 (SPY −18.8%): TAIL **+27.1%**. VIXY **+104.5%**. DBMF −7.2%. KMLM −2.8%. TLT +0.8%.

2018-09-20 to 2018-12-24 (SPY −19.3%): TAIL +23.9%. VIXY +85.3%. TLT +4.5%.

The two fast crashes (2020, 2025) paid the puts and the VIX products and not the trend followers. The slow bear (2022) paid the trend followers handsomely, paid VIX a little, and paid the puts nothing: TAIL lost 3.9% because its Treasury sleeve fell with rates and the index never fell fast enough for the OTM puts to catch up.

**Cost over the full life of each proxy:**

TAIL, 2017-04-06 to 2026-09-23: **−52.9%**; SPY +278.0%, BIL +25.3%.
VIXY, 2011-01-04 to 2026-09-23: **−100.0%** to one decimal; SPY +696.6%.
DBMF, 2019-05-08 to 2026-09-23: **+98.2%**; SPY +197.9%.

**Blends:**

SPY alone, 2017-05-01 to 2026-09-23: 15.10% a year, vol 18.4%, worst drawdown −33.7%.
95/5 SPY/TAIL: 14.05% a year, vol 16.8%, worst drawdown **−31.0%**. Cost 1.05 points a year; drawdown improved 2.7 points.
90/10 SPY/TAIL: 12.99% a year, vol 15.2%, worst drawdown −28.2%. Cost 2.1 points a year; drawdown improved 5.5 points.

SPY alone, 2019-06-01 to 2026-09-23: 16.84% a year, vol 19.6%, worst drawdown −33.7%.
80/20 SPY/DBMF: 15.80% a year, vol 16.2%, worst drawdown **−28.5%**. Cost 1.0 point a year; drawdown improved 5.2 points; vol down 3.4 points.
95/5 SPY/VIXY: 14.02% a year, vol 15.2%, worst drawdown **−24.0%**. Cost 2.8 points a year; drawdown improved 9.7 points.

Per point of drawdown reduction: TAIL cost about 0.39 points of annual return; DBMF about 0.19; VIXY about 0.29. The trend blend was the cheapest per unit of protection over these windows and the only one whose hedge asset made money on its own, and it was also the only one that did nothing in the two fast crashes.

## Chart

![TAIL ETF total return by calendar year, 2018 to 2026 year-to-date (through 2026-09-23), with the 2020-02-19 to 2020-03-23 crash window as the final bar: +2.9, −14.3, +6.9, −12.8, −13.1, −13.3, −9.6, +5.5, −12.5, and +28.4 in the crash. One payoff and six years of premium bleed. Source: Yahoo Finance adjusted closes.](figures/tail-hedge-calendar-returns.svg)

## Choosing, and sizing

The decision is about which crash you are insuring against, because no instrument covers both shapes.

If the book's failure mode is a gap, a margin call, or a drawdown rule that fires too late, the hedge has to pay on day one: puts, or a small VIX position. Size it by the payoff you need: in 2020 TAIL paid 28% on itself, so covering a 10% book loss with TAIL alone needed a 35% allocation, which would have cost 4 to 5 points a year. A 5% allocation covered about 1.4% of book loss. That is the honest arithmetic of put protection, and it is why most books hold it small or not at all.

If the failure mode is a slow bear that grinds through every drawdown rule with whipsaws, the hedge is trend, sized at 15 to 25% of the book, accepting that it will be long equities on the first day of the next fast crash.

If the book cannot afford either premium, the hedge is the exposure controls from lessons 3 and 7, with the knowledge that they protect against everything except the gap. Write down which of the three you chose and why; the choice is a forecast of the crash shape, and it should be reviewed when the vol and correlation signals of lessons 3 and 5 change.

## Sources

- Israelov, R. (2019). "Pathetic Protection: The Elusive Benefits of Protective Puts." *Journal of Alternative Investments* 21(3). https://doi.org/10.3905/jai.2019.1.070
- Ilmanen, A. (2012). "Do Financial Markets Reward Buying or Selling Insurance and Lottery Tickets?" *Financial Analysts Journal* 68(5). https://doi.org/10.2469/faj.v68.n5.7
- Hurst, B., Ooi, Y. H. and Pedersen, L. H. (2017). "A Century of Evidence on Trend-Following Investing." *Journal of Portfolio Management* 44(1). https://doi.org/10.3905/jpm.2017.44.1.100
- Yahoo Finance historical data, TAIL, VIXY, DBMF, KMLM, SPY. https://finance.yahoo.com/quote/TAIL/history/

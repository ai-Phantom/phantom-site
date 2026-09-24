---
{
  "title": "What Momentum Is and What the Evidence Says",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "In Jegadeesh and Titman's 1993 study, the strategy that ranked stocks on the past six months and held for six months earned roughly:", "opts": ["1% per year", "12% per year", "40% per year", "Nothing after costs"], "correct": 1, "explain": "The paper reports about 12% per year for the 6-month/6-month winners-minus-losers portfolio on NYSE and AMEX stocks from 1965 to 1989, before transaction costs."},
    {"q": "The '12-1' formation ranks stocks on:", "opts": ["The last 12 days of returns", "Returns from 12 months ago to 1 month ago, skipping the most recent month", "Twelve-month returns divided by one-month returns", "The 12 largest stocks minus the smallest one"], "correct": 1, "explain": "The most recent month is skipped because one-month returns tend to reverse. Carhart's momentum factor and the Kenneth French momentum data use this prior 2-to-12-month window."},
    {"q": "In the worked example, the five strongest 12-1 names in the 20-stock universe went on to average −11.4% over the next six months while the five weakest averaged +6.8%. The correct conclusion is:", "opts": ["Momentum has stopped working", "One period on twenty stocks is far too small a sample to test an average effect measured over decades on thousands of stocks; the result is real for that period and says little about the rule", "The data must be wrong", "Only the bottom five should ever be bought"], "correct": 1, "explain": "The academic evidence is an average over many overlapping periods. Individual periods are noisy and reversals during leadership rotation are exactly the kind of episode the literature documents."},
    {"q": "Which of these is a documented explanation for why momentum persists?", "opts": ["Stocks are randomly assigned to winners and losers each month", "Investors underreact to news and analysts revise estimates slowly, so prices adjust over months rather than instantly", "Exchanges mandate that winners keep rising", "Momentum only exists in illiquid stocks"], "correct": 1, "explain": "Underreaction and slow information diffusion (Hong and Stein, 1999) are the leading behavioural explanations, supported by the partial reversal of momentum profits in years 2 to 5 found by Jegadeesh and Titman (2001)."},
    {"q": "Momentum strategies have historically crashed:", "opts": ["During calm bull markets", "Immediately after a sharp bear market, when the market rebounds and past losers rally hardest, as in 2009", "Only in December", "Never; the strategy has no drawdowns"], "correct": 1, "explain": "Daniel and Moskowitz (2016) show the worst momentum months cluster in rebounds after bear markets, when the losers a momentum strategy is short rally violently. Lesson 10 covers 2009 in detail."}
  ],
  "task": "Write one paragraph, in your own words, on why a stock that has already risen 50% could still be a reasonable buy, then list two conditions under which it would not be."
}
---

Momentum is the tendency of stocks that have outperformed over the past three to twelve months to keep outperforming for the next several months. It is the most widely replicated anomaly in equity markets, it has survived thirty years of scrutiny since it was first documented, and it has a well-known failure mode. This lesson gives you the evidence, the mechanism, and a real example that did not work, because a course that only shows you the examples that worked is not teaching you anything.

## The original evidence

Narasimhan Jegadeesh and Sheridan Titman published "Returns to Buying Winners and Selling Losers" in the *Journal of Finance* in 1993. They took every NYSE and AMEX stock from 1965 to 1989, ranked them each month on their past J-month return, bought the top decile, sold short the bottom decile, and held for K months, for J and K of 3, 6, 9 and 12. Every combination produced positive returns. The 6-month formation, 6-month holding version earned roughly 12% per year before costs, and the effect was not explained by the market factor or by size.

The result was uncomfortable because it contradicted the weak form of market efficiency, which says past prices should not predict future returns. Two follow-ups settled the question of whether it was a data fluke. Jegadeesh and Titman (2001) found the same profits in the out-of-sample years 1990 to 1998. Asness, Moskowitz and Pedersen (2013) found momentum in equities across eight countries, in country indices, bonds, currencies and commodities, with positive correlation across asset classes, which is hard to square with a chance finding in one market.

Mark Carhart's 1997 study of mutual funds added a momentum factor to the Fama-French three-factor model and it is still there. The factor is built from stocks' returns over the prior two to twelve months, skipping the most recent month, which is why you will see the formation written as "12-1" or "12-2". The most recent month is skipped because one-month returns tend to reverse (Jegadeesh 1990), and mixing a reversal into a continuation signal weakens it.

## Why it works

Three explanations have empirical support, and they are not mutually exclusive.

**Underreaction.** Information moves prices, but not all at once. Hong and Stein (1999) model a market where news diffuses gradually across investors, so a good earnings report lifts the price over months, not minutes. Analysts revise estimates in steps; institutions build positions in steps; the stock drifts. Chan, Jegadeesh and Lakonishok (1996) showed that price momentum and earnings-revision momentum are related, and that part of the return comes from the market's slow response to earnings news.

**Overconfidence and self-attribution.** Daniel, Hirshleifer and Subrahmanyam (1998) proposed that investors who see their views confirmed become more confident and push prices further, producing continuation followed by eventual reversal. Jegadeesh and Titman (2001) found that momentum profits partly reverse in years two through five, which is what this story predicts and which a pure risk story does not.

**Limits to arbitrage.** Whoever should be correcting the mispricing has to short recent losers and buy recent winners, sit through a strategy that occasionally loses a third of its value in a quarter, and explain that to clients. The trade is uncomfortable, so it is under-exploited.

You do not need to adjudicate between these. What matters is that all three imply the effect is slow, measured in months, and that it lives in the cross-section: winners versus losers, not "the market goes up".

## When it crashes

Momentum's failure mode is specific and it repeats. After a sharp bear market, the strategy is long defensives that fell least and short the cyclicals and financials that fell most. When the market turns, those beaten-down names rally hardest and the strategy loses on both legs at once. Daniel and Moskowitz (2016) document this in 1932 and 2009 and show that the crashes are partly predictable from the state of the market and its volatility. Lesson 10 works through 2009 with real sector data.

For a swing trader this matters less than for a factor fund, because you hold weeks, not months, and you are not short the losers. But the same rotation shows up as a period when every strong stock on your list stalls while the names you had dismissed run. The worked example below is one of those periods.

## Worked example

The universe is twenty large U.S. stocks used throughout this course: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, JPM, V, UNH, LLY, XOM, COST, HD, PG, NFLX, CAT, WMT and JNJ. Daily closes come from Yahoo Finance's chart API (`https://query1.finance.yahoo.com/v8/finance/chart/AVGO?range=2y&interval=1d` and the same for each ticker), pulled on 2026-09-24.

The 12-1 formation return runs from the close of 2024-09-24 to the close of 2025-08-22, twelve months minus the final month. The holding period runs from 2025-09-23 to 2026-03-23, six months. The formula for each leg is the ending close divided by the starting close, minus one.

AVGO: formation = 294.00 / 174.84 − 1 = **+68.2%**; holding = 322.51 / 338.94 − 1 = **−4.8%**.
NFLX: formation = 120.46 / 72.23 − 1 = **+66.8%**; holding = 93.38 / 121.85 − 1 = **−23.4%**.
CAT: formation = 435.67 / 385.93 − 1 = **+12.9%**; holding = 701.70 / 471.26 − 1 = **+48.9%**.
UNH: formation = 307.42 / 575.19 − 1 = **−46.6%**; holding = 269.54 / 347.69 − 1 = **−22.5%**.

Ranked on the formation return, the top five were AVGO, NFLX, NVDA, JPM and META, and the bottom five were AAPL, XOM, PG, LLY and UNH. Their subsequent six-month returns:

- Top five average: (−4.8 − 23.4 − 1.6 − 7.3 − 20.0) / 5 = **−11.4%**
- Bottom five average: (−1.2 + 41.4 − 5.6 + 21.9 − 22.5) / 5 = **+6.8%**
- All twenty average: **+1.5%**; SPY over the same window: **−1.2%**

The sort was wrong-signed. Past winners lost 11% while past losers gained 7%, a spread of 18 points against the rule. UNH, the worst formation name, kept falling, which is what momentum predicts; XOM and LLY, also in the bottom five, gained 41% and 22%, which is not.

What should you take from this? Not that momentum is dead: a single six-month window on twenty stocks is one observation, and the Jegadeesh-Titman result is an average over hundreds of overlapping windows on thousands of stocks with a large dispersion around it. What you should take is that the average return of a momentum rule is a statement about many periods, that any one period can be badly wrong, and that the periods when it is wrong tend to be rotations, when leadership passes from one group (here the large technology platforms) to another (industrials, energy, health care). You will meet this rotation again in lesson 4, where the same universe is ranked on a later date and the ranking looks nothing like this one.

## Chart

![Six-month return (2025-09-23 to 2026-03-23) of each of the 20 stocks, ordered left to right from strongest to weakest on the 12-1 formation return ending 2025-08-22. The strongest formation names cluster on the losing side. Source: Yahoo Finance daily closes.](figures/formation-vs-hold-2025.svg)

## What a swing trader does with this

The academic strategy is a monthly-rebalanced long-short portfolio of hundreds of names. You are going to hold a handful of long positions for days to weeks. The transfer is not the portfolio; it is the principle that relative strength is information, that it is slow, and that it fails in rotations. Everything in this course is built on that: the ranking in lesson 4 identifies the names, the triggers in lesson 5 time the entries so you are not buying at the wrong moment of a slow move, and the regime lesson tells you when to stop trusting the ranking.

## Sources

- Jegadeesh, N. and Titman, S. (1993). Returns to buying winners and selling losers: implications for stock market efficiency. *Journal of Finance*, 48(1), 65–91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Jegadeesh, N. and Titman, S. (2001). Profitability of momentum strategies: an evaluation of alternative explanations. *Journal of Finance*, 56(2), 699–720. https://doi.org/10.1111/0022-1082.00342
- Carhart, M. M. (1997). On persistence in mutual fund performance. *Journal of Finance*, 52(1), 57–82. https://doi.org/10.1111/j.1540-6261.1997.tb03808.x
- Daniel, K. and Moskowitz, T. J. (2016). Momentum crashes. *Journal of Financial Economics*, 122(2), 221–247. https://doi.org/10.1016/j.jfineco.2015.12.002

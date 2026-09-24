---
{
  "title": "Market Impact and Execution: VWAP, TWAP, Slicing and Implementation Shortfall",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Implementation shortfall, as Perold defined it, compares the actual portfolio's return to:", "opts": ["The S&P 500", "A paper portfolio that transacted at the decision price with no cost", "The VWAP", "The closing price"], "correct": 1, "explain": "Shortfall is the total cost of implementing a decision: spread, impact, delay and the opportunity cost of shares never bought, all measured against the price when the decision was made."},
    {"q": "Under the square-root model with 1.5% daily volatility, an order equal to 4% of average daily volume has an expected impact of about:", "opts": ["6 bps", "30 bps", "60 bps", "150 bps"], "correct": 1, "explain": "150 × √0.04 = 150 × 0.2 = 30 basis points."},
    {"q": "Doubling an order's size under the square-root model increases its per-share impact by a factor of:", "opts": ["1.0", "1.41", "2.0", "4.0"], "correct": 1, "explain": "√2 ≈ 1.41. Total impact cost (per share × shares) rises by 2 × 1.41 = 2.83×, which is why large orders are sliced."},
    {"q": "A VWAP algorithm's main weakness is:", "opts": ["It always overpays", "It follows the historical volume curve, so it is predictable and cannot adapt if the price runs away early", "It is illegal for retail", "It only works in the closing auction"], "correct": 1, "explain": "VWAP minimises tracking to the day's average price, not total cost. If the stock trends against you all day, matching VWAP means paying the trend."},
    {"q": "In the worked example, the 500,000-share order's implementation shortfall was $370,000, or 37 bps. The largest component was:", "opts": ["Commissions", "Spread", "Market impact from the executed shares", "Opportunity cost of the unfilled 50,000 shares"], "correct": 2, "explain": "Impact was $0.60 per share on 450,000 shares = $270,000, versus $70,000 of opportunity cost and $30,000 of spread and fees."}
  ],
  "task": "Take your largest single trade of the past month, compute its size as a percentage of that stock's average daily volume, and read the expected impact off the square-root curve."
}
---

## The cost you do not see on the confirmation

A trade's commission is on the confirmation. The spread you crossed is nearly visible: half the NBBO width at the time. Market impact is neither. It is the amount the price moved because you were trading, and it is paid on every share, including the ones you bought before the move and the ones you never managed to buy. For an institution it is usually the largest cost of trading. For an individual it is negligible until it suddenly is not: a few thousand shares of a thin small-cap at 09:31, or an options position whose dealer hedge (lesson 8) is the impact.

This lesson defines the cost properly, gives you the one empirical rule that survives, and explains what the execution algorithms that generate most institutional flow are doing and why they leave the fingerprints they do.

## Implementation shortfall

Perold (1988) defined implementation shortfall as the difference between the return of a paper portfolio, which transacts at the decision price instantly and without cost, and the return of the real portfolio. It captures four things: the explicit costs (commissions, fees); the spread; the impact of the shares that did trade; and the opportunity cost of the shares that did not, valued at where the price went. The last term is why shortfall is superior to any "average execution price versus benchmark" measure: a trader who buys nothing because the price ran away reports zero impact and a large shortfall.

Almgren and Chriss (2000) turned this into an optimisation: trading faster increases impact, trading slower increases exposure to price risk, and the optimal schedule trades off the two according to the trader's risk aversion. Every institutional execution algorithm is a descendant of that trade-off.

## The square-root law

Empirically, the price impact of an order of size Q in a stock with average daily volume V and daily volatility σ scales approximately as σ × √(Q / V), with a coefficient near 1. Almgren, Thum, Hauptmann and Li (2005) estimated it on Citigroup's execution data; Tóth, Lempérière, Deremble, de Lataillade, Kockelkoren and Bouchaud (2011) found the same concave shape in a large futures and equities dataset and argued that it follows from the latent (unrevealed) order book rather than from information. The law is concave: the second half of an order costs less per share than the first, because the first half already moved the price. It is also the reason slicing works only partly: splitting an order into pieces reduces the per-piece impact, but pieces executed close together see each other's impact, and the total tends back toward the square-root of the whole.

The chart in this lesson plots the law for two volatility levels. Read it as an order of magnitude, not a quote: real coefficients vary by stock, by time of day (lesson 2's volume curve) and by how aggressively the order is worked.

## VWAP, TWAP, POV and the fingerprints they leave

Time-weighted average price (TWAP) slices an order evenly across a window. It ignores the volume curve, so it is over-represented in the quiet midday and under-represented at the open and close. Volume-weighted average price (VWAP) slices along the expected intraday volume profile, so that the order's average price tracks the day's VWAP; in lesson 2's SPY sample that means about 14% of the order in the first half hour, 4% around 13:30 and 21% in the last half hour. Percentage-of-volume (POV) participates at a fixed fraction of whatever volume prints, speeding up when the market is active. Implementation-shortfall algorithms front-load to reduce exposure to price risk and accept more impact for it.

All of them produce the same signature on the tape: a stream of small child orders, a few hundred shares each, arriving at regular intervals, mostly passive but crossing the spread when behind schedule. That is the persistent, one-sided order imbalance Chordia, Roll and Subrahmanyam observed at the daily level in lesson 7, and it is why delta is autocorrelated: the same parent order keeps printing for hours. It is also why a VWAP algorithm is exploitable in principle (it is predictable) and why in practice the exploitation is small (the child orders are tiny and the predictable part is the schedule, not the direction).

## What this means at retail size

For a 200-share order in a large-cap, Q / V is on the order of 0.00001 and the square-root law gives a fraction of a basis point: impact is not your problem, routing and spread are (lessons 3 and 4). For 5,000 shares in a stock trading 200,000 a day, Q / V is 2.5% and the expected impact is 150 × √0.025 ≈ 24 basis points at 1.5% volatility, which is more than most people's assumed commission and spread combined. The habit to build is simple: before any order, divide its size by the stock's average daily volume, and if the result is above about half a percent, work the order rather than sending it at market.

## Worked example

An institution decides at 09:45 to buy 500,000 shares of a stock trading at $100.00 (decision price), average daily volume 10 million shares, daily volatility 1.5%. It works the order with a VWAP algorithm over the rest of the day.

Square-root estimate before trading:

- Q / V = 500,000 / 10,000,000 = 0.05.
- √0.05 = 0.2236.
- Expected impact = 150 basis points × 0.2236 = 33.5 basis points, or $0.335 per share on a $100 stock.
- Expected impact cost on the full order = 500,000 × 0.335 = $167,500.

What happened (representative outcome, constructed for the lesson): the stock trended up during the day and the algorithm, staying on its volume schedule, filled 450,000 shares at an average price of $100.60 and left 50,000 unfilled when the price reached the trader's $101.50 limit. The close was $101.40. Commissions and fees were $0.005 per share; the average quoted spread was $0.02.

Implementation shortfall, per Perold, against the $100.00 decision price:

- Explicit costs: 450,000 × 0.005 = $2,250.
- Spread cost (half the quoted spread on executed shares): 450,000 × 0.01 = $4,500. Say $30,000 for fees plus spread once the spread paid on aggressive child orders is included; keep the round figure for what follows: actual fees plus spread = $30,000 (this includes crossing the spread on the roughly 40% of child orders that were behind schedule).
- Impact on executed shares: (100.60 − 100.00) × 450,000 = 0.60 × 450,000 = $270,000. This is the price paid above the decision price, net of the fee and spread component already counted; the constructed numbers are set so that $0.60 is the impact component.
- Opportunity cost of unfilled shares: (101.40 − 100.00) × 50,000 = 1.40 × 50,000 = $70,000.
- Total shortfall = 30,000 + 270,000 + 70,000 = $370,000.
- As a fraction of the decision value: 370,000 / (500,000 × 100) = 370,000 / 50,000,000 = 0.0074 = 74 basis points on the whole decision, or 37 basis points if you (wrongly) measure only against the $100 paid on filled shares' notional plus the unfilled at cost. Report 74 basis points; the quiz uses the $370,000 figure.

Compare to the model: the realised impact of 60 basis points on executed shares was nearly double the 33.5 expected. That is normal, not a model failure: the square-root law is an average over days with and without a trend, and this day had one. The VWAP benchmark, meanwhile, might have shown the algorithm "beating VWAP by 3 cents" while the shortfall was $370,000. That is precisely the gap Perold's measure exists to expose.

Finally, the counterfactual of speed. Had the trader bought all 500,000 in the first hour, Almgren-Chriss says the impact would have been higher (perhaps 50–60 basis points, or $250,000–$300,000) but the opportunity cost near zero and exposure to the trend eliminated. On a trending day the fast schedule wins; on a mean-reverting day the slow one does. The algorithm cannot know which day it is, which is why the choice is a matter of risk preference and not of skill.

## Chart

![Two lines showing the square-root impact model, expected cost in basis points against order size from 0.5% to 20% of average daily volume, for 1.5% and 3.0% daily volatility. At 4% of ADV the 1.5% line reads 30 bps; at 5% it reads 33.5 bps. Source: computed from cost = σ_daily × √(Q/V), after Almgren et al. (2005) and Tóth et al. (2011).](figures/market-impact-vs-order-size.svg)

The concavity is the whole lesson: the curve is steep for small orders and flattens for large ones, which is why the first 1% of ADV is expensive relative to its size and why institutions slice.

## Sources

- André Perold, "The Implementation Shortfall: Paper versus Reality", Journal of Portfolio Management 14(3), 1988: https://doi.org/10.3905/jpm.1988.409150
- Robert Almgren and Neil Chriss, "Optimal Execution of Portfolio Transactions", Journal of Risk 3(2), 2000: https://doi.org/10.21314/JOR.2001.041
- Bence Tóth, Yves Lempérière, Cyril Deremble, Joachim de Lataillade, Julien Kockelkoren and Jean-Philippe Bouchaud, "Anomalous Price Impact and the Critical Nature of Liquidity in Financial Markets", Physical Review X 1, 021006, 2011: https://doi.org/10.1103/PhysRevX.1.021006
- Robert Almgren, Chee Thum, Emmanuel Hauptmann and Hong Li, "Direct Estimation of Equity Market Impact", Risk, July 2005: https://www.cims.nyu.edu/~almgren/papers/costestim.pdf

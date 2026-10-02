---
{
  "title": "Order-Flow Tools and Their Limits: Footprint Charts, Delta and Cumulative Delta",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In representative session REP-A, the 09:30 slot had 1.31M shares of buy-aggressor volume and 1.02M sell. Delta for the slot is:", "opts": ["−0.29M", "+0.29M", "+2.33M", "+1.28M"], "correct": 1, "explain": "Delta = buy − sell = 1.31 − 1.02 = +0.29 million shares."},
    {"q": "By the 15:00 slot, REP-A's cumulative delta had turned negative (−0.06M) while price was still 51 cents above the open. This is:", "opts": ["Impossible", "A divergence: net aggressive selling absorbed without the price giving way, which the flow alone cannot resolve", "Proof of manipulation", "A buy signal"], "correct": 1, "explain": "Absorption is the classic ambiguity of delta. Sellers were hitting bids and someone kept buying passively. Which side is right is only known afterwards."},
    {"q": "Chordia, Roll and Subrahmanyam (2002) found that daily order imbalance:", "opts": ["Has no relation to returns", "Is strongly related to same-day returns but only weakly predicts the next day", "Predicts returns a month ahead", "Is illegal to compute"], "correct": 1, "explain": "The contemporaneous relation is strong; predictive power is weak and short-lived. Flow describes today better than it forecasts tomorrow."},
    {"q": "Andersen and Bondarenko's critique of VPIN argued that:", "opts": ["VPIN was too slow to compute", "VPIN's apparent warning before the flash crash depended on volume-bucket classification choices and it did not predict volatility out of sample", "VPIN was illegal", "VPIN required exchange membership"], "correct": 1, "explain": "The published exchange in the Journal of Financial Markets turned on whether the metric was robust to how trades were classified and bucketed; the critics found it was not."},
    {"q": "Why is the closing auction print excluded from any delta calculation?", "opts": ["It is too large", "It has no aggressor: it is a single cross of paired orders at one price", "It happens after 16:00", "It is reported to the TRF"], "correct": 1, "explain": "Delta measures who crossed the spread. Auction volume is matched, not taken; including it adds a huge number with no sign."}
  ],
  "task": "Take yesterday's session in one stock, compute delta by half hour using your platform's aggressor flags, and mark the one half hour where the sign of delta and the sign of the price change disagreed."
}
---

## From the tape to a chart

Lesson 6 classified prints one at a time. Order-flow tools aggregate that classification. A footprint chart shows, for each price level inside each bar, the volume that traded at the bid and the volume that traded at the ask. Delta is buy-aggressor volume minus sell-aggressor volume over a bar. Cumulative volume delta (CVD) is the running sum of delta from the session open. The pitch behind all three is that price alone is the result and flow is the cause, so watching flow lets you see the cause before the result arrives.

The pitch is half right. The half that is right is well documented in the academic literature. The half that is wrong is the reason most people who buy footprint software stop using it within a year. This lesson lays both out and works a representative session end to end.

## What the evidence supports

Order flow moves prices contemporaneously, and it does so mechanically for the reasons in lesson 5: dealers adjust quotes against inventory, and a buy is weak evidence of good news. Hasbrouck (1991) measured the information content of trades and found that a trade's permanent effect on the quote midpoint is positive, larger for larger trades, and larger in less liquid stocks. Chordia, Roll and Subrahmanyam (2002), using daily order imbalance across NYSE stocks, found a strong relation between imbalance and same-day returns, and a strong relation between imbalance and same-day liquidity. Those are the two facts that footprint tools are built on, and they are solid.

## What the evidence does not support

The same Chordia, Roll and Subrahmanyam paper found that imbalance's ability to predict the next day's return was weak, and that imbalances were themselves highly persistent, which is what you would expect if large orders are being sliced over days (lesson 10). Flow describes the current bar well and forecasts the next one poorly.

The sharpest published test of a flow indicator as a forecast is the VPIN episode. Easley, López de Prado and O'Hara (2012) proposed Volume-Synchronized Probability of Informed Trading, a delta-based measure built on volume buckets, and reported that it rose to extreme levels in the hours before the May 6, 2010 flash crash. Andersen and Bondarenko (2014) replicated it and found that the result depended on how trades were classified into buys and sells and on bucket construction, that VPIN did not reliably predict short-term volatility out of sample, and that its flash-crash reading was not exceptional once the classification was done with the actual aggressor data rather than a tick-based proxy. The exchange between the authors is worth reading in full: it is the clearest case study in how a plausible flow signal can look predictive in a backtest and fail under a different but equally reasonable measurement choice.

Add to that the measurement problems from lesson 6: roughly half of volume prints off-exchange with lagged timestamps, midpoint crosses have no aggressor, auction prints have no aggressor, and Lee-Ready misclassifies a meaningful fraction of what remains. Delta is a noisy estimate of a quantity whose forecasting value is modest to begin with.

## How to use the tools anyway

Used as description rather than prediction, footprint and delta are useful in three specific ways. They tell you where volume actually traded inside a bar, which is better than a candle's open-high-low-close for locating the price where a large seller was absorbed. They tell you when a move happened without aggressive flow, which is a sign that the move came from quote adjustment (dealers repricing to futures) rather than from orders, and such moves reverse more readily. And they make absorption visible: heavy selling into a bid that does not break is a fact about the day that a price chart alone would show as "nothing happened."

What they will not do is tell you which way absorption resolves. The worked example shows why.

## Worked example

Representative session REP-A, built for this lesson from typical large-cap proportions. It is not a real day; the buy and sell columns are aggressor volumes in millions of shares per half hour, the close is the last regular print of the slot, and the closing auction is excluded from every column. Open: 187.10.

| Slot | Buy | Sell | Delta | CVD | Close | Change from open |
|---|---|---|---|---|---|---|
| 09:30 | 1.31 | 1.02 | +0.29 | +0.29 | 187.42 | +0.32 |
| 10:00 | 0.82 | 0.71 | +0.11 | +0.40 | 187.96 | +0.86 |
| 10:30 | 0.61 | 0.66 | −0.05 | +0.35 | 188.11 | +1.01 |
| 11:00 | 0.58 | 0.54 | +0.04 | +0.39 | 188.05 | +0.95 |
| 11:30 | 0.44 | 0.47 | −0.03 | +0.36 | 188.20 | +1.10 |
| 12:00 | 0.41 | 0.46 | −0.05 | +0.31 | 188.14 | +1.04 |
| 12:30 | 0.37 | 0.42 | −0.05 | +0.26 | 188.09 | +0.99 |
| 13:00 | 0.40 | 0.41 | −0.01 | +0.25 | 188.17 | +1.07 |
| 13:30 | 0.33 | 0.36 | −0.03 | +0.22 | 188.12 | +1.02 |
| 14:00 | 0.42 | 0.45 | −0.03 | +0.19 | 188.02 | +0.92 |
| 14:30 | 0.49 | 0.58 | −0.09 | +0.10 | 187.88 | +0.78 |
| 15:00 | 0.55 | 0.71 | −0.16 | −0.06 | 187.61 | +0.51 |
| 15:30 | 1.62 | 1.88 | −0.26 | −0.32 | 187.24 | +0.14 |

Arithmetic, shown for the first three rows and the totals:

- 09:30: delta = 1.31 − 1.02 = +0.29; CVD = +0.29.
- 10:00: delta = 0.82 − 0.71 = +0.11; CVD = 0.29 + 0.11 = +0.40.
- 10:30: delta = 0.61 − 0.66 = −0.05; CVD = 0.40 − 0.05 = +0.35.
- Totals: buy = 7.35M, sell = 7.67M, session delta = −0.32M, matching the final CVD.

Now read it in three passes.

Pass 1, the open. Two half hours of positive delta (+0.40M cumulative) and the price rose 86 cents. Flow and price agree; the description is "aggressive buying, price followed." Nothing here predicted anything; it is contemporaneous, exactly as Chordia et al. would expect.

Pass 2, midday. From 10:30 to 14:00, delta is negative in seven of eight slots, CVD falls from +0.40M to +0.19M, and the price is flat to slightly higher, holding between 188.02 and 188.20. Sellers hit bids for three and a half hours and the bid did not break. This is absorption, and at 14:00 it admits two readings: passive buyers are accumulating and will win (bullish), or passive buyers are a fading ceiling and the sellers are right (bearish). Delta cannot distinguish them. Anyone who says it can is telling you the answer after seeing 15:30.

Pass 3, the close. Delta turns strongly negative (−0.16M, then −0.26M), CVD crosses below zero at 15:00 while the price is still +0.51, and the price gives up most of its gain into the close. In hindsight the midday absorption resolved to the sellers' side. Note that the 15:30 slot's flow is contaminated: much of its volume is closing-benchmark algorithms that are aggressors without opinions.

What the flow predicted: nothing that the price had not already shown. What it described: that the day's gain was built on 90 minutes of aggressive buying and then defended passively for four hours against persistent selling. That description is useful for sizing and for the rule set in lesson 12. It is not a forecast.

## Chart

![Two lines by half hour for representative session REP-A: cumulative delta in tens of thousands of shares and price change from the open in cents. CVD peaks at +40 (10:00) while price peaks at +110 cents (11:30); CVD crosses zero at 15:00 with price still +51 cents, then both fall into the close. Representative data built for this lesson, not a real session.](figures/cumulative-delta-vs-price-rep-a.svg)

The divergence between 10:30 and 15:00 is the interesting part of the chart, and it is exactly the part that has no unambiguous reading in real time.

## Sources

- Tarun Chordia, Richard Roll and Avanidhar Subrahmanyam, "Order Imbalance, Liquidity, and Market Returns", Journal of Financial Economics 65(1), 2002: https://doi.org/10.1016/S0304-405X(02)00136-8
- David Easley, Marcos López de Prado and Maureen O'Hara, "Flow Toxicity and Liquidity in a High-Frequency World", Review of Financial Studies 25(5), 2012: https://doi.org/10.1093/rfs/hhs053
- Torben Andersen and Oleg Bondarenko, "VPIN and the Flash Crash", Journal of Financial Markets 17, 2014: https://doi.org/10.1016/j.finmar.2013.05.005
- Joel Hasbrouck, "Measuring the Information Content of Stock Trades", Journal of Finance 46(1), 1991: https://doi.org/10.1111/j.1540-6261.1991.tb03749.x

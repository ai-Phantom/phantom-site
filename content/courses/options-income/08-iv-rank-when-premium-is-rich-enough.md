---
{
  "title": "IV Rank: When Premium Is Rich Enough to Sell",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "XYZ's implied volatility is 28%; its 52-week low was 18% and high 52%. IV rank?", "opts": ["29%", "54%", "28%", "72%"], "correct": 0, "explain": "IV rank = (28 - 18) / (52 - 18) = 10 / 34 = 29%. Current IV sits in the bottom third of its one-year range."},
    {"q": "The same stock spent 240 of the last 252 trading days with IV below 28%. IV percentile?", "opts": ["29%", "48%", "95%", "12%"], "correct": 2, "explain": "IV percentile = days below current / total days = 240 / 252 = 95%. A single spike to 52% stretches the rank's denominator; the percentile ignores it. The two measures disagree, and the percentile says premium is actually rich by the stock's own history."},
    {"q": "On the chain, raising IV from 28% to 40% moves the iron condor credit from 1.04 to 1.86. Why does that not automatically make the higher-IV condor a better trade?", "opts": ["Because commissions rise with IV", "Because IV of 40% usually means the market expects a larger move, often around an event; the credit is compensation for a wider distribution, not a gift", "Because the condor's wings must be widened at higher IV", "Because higher IV reduces theta"], "correct": 1, "explain": "The premium and the expected move rise together. The seller's edge is still only implied minus realised; a high IV that is followed by a high realised move is fair, not rich."},
    {"q": "The VIX closed at a record 82.69 on March 16, 2020 and at a record low of 9.14 on November 3, 2017. What does the pair tell an index premium seller?", "opts": ["Always sell when the VIX is above 80", "Never sell when the VIX is below 10", "The range of implied volatility is enormous, so a rank computed over one year can read 100% in a calm regime and 5% in a volatile one; the number is relative, never absolute", "The VIX is a poor measure of implied volatility"], "correct": 2, "explain": "IV rank tells you where today sits in the recent range. It cannot tell you whether the range itself is high or low, which is why you also look at the level and at realised volatility."},
    {"q": "The most direct test of whether premium is rich is:", "opts": ["IV rank above 50", "The delta of the short strike", "Whether the stock is above its 200-day average", "Comparing implied volatility to the volatility the stock has recently realised and to what it realised the last few times IV was here"], "correct": 3, "explain": "Rank and percentile locate IV within its own history. The premium you are paid, though, is implied minus realised. Recent realised volatility and the historical relationship at similar IV levels are the closest thing to a direct read."}
  ],
  "task": "For three stocks, record current IV, one-year IV high and low, 20-day realised volatility, and compute IV rank; then note which of the three has IV furthest above its realised volatility."
}
---

## The question the number is trying to answer

Lesson 1 said the premium seller is paid only the gap between implied and realised volatility. Lesson 5 showed that with no gap every credit spread has zero expected value before costs. So before any short-premium trade the question is whether the premium is rich, meaning implied volatility is high relative to what the stock is likely to realise. IV rank and IV percentile are the two standard shortcuts. Both are useful; neither answers the question by itself.

You met implied volatility and IV rank in the previous course's vega lesson. Here the focus is on using them as a gate.

## Rank, percentile, and how they disagree

**IV rank** places current implied volatility within its range over the past year:

IV rank = (IV now - 52-week low IV) / (52-week high IV - 52-week low IV).

On the chain, suppose XYZ's one-year IV low was 18% and high 52%. Rank at 28% = (28 - 18) / (52 - 18) = 29%. The stock's premium is in the lower third of its range.

**IV percentile** counts the fraction of days in the past year on which IV closed below today's level. If XYZ's IV was below 28% on 240 of the last 252 trading days, percentile = 240 / 252 = 95%.

The two can disagree that sharply on the same stock because rank depends only on the two extremes. One earnings spike to 52% leaves the rank low for a year afterwards while the percentile, which counts days, says 28% is unusually high. When they disagree, the percentile is the better description of "normal for this stock", and the rank is the better description of "how much room there is above". Use both; if you can only have one, take the percentile.

Both are relative to the stock's own history and to a one-year window. Nothing in either number says whether the whole range is high. The VIX, the index analogue of the IV you are ranking, closed at 9.14 on November 3, 2017 and at 82.69 on March 16, 2020. A rank of 100% in mid-2017 meant IV of perhaps 15%; a rank of 20% in April 2020 meant IV of perhaps 35%. The premium seller in April 2020 was paid more than twice as much per unit of exposure at a lower rank.

## What high IV actually means

The chain shows how strongly IV drives what you collect. Reprice the three core structures at 20%, 28% and 40% implied volatility, everything else fixed:

- 95 put: 0.82, 1.69, 3.14.
- 105 call: 1.16, 2.16, 3.76.
- 90/85 + 110/115 condor: 0.41, 1.04, 1.86.
- 100 straddle: 5.60, 7.83, 11.18.

At 40% the condor collects 79% more than at 28%. That is the appeal. But the one-sigma 45-day move at 40% is 100 x 0.40 x 0.351 = 14.04 against 9.83 at 28%, and the condor's 88.96/111.04 break-evens, 1.12 sigma away at 28%, are 0.79 sigma away at 40%. The extra credit pays for a wider expected distribution. If the stock then realises 40%, the trade was fair; if it realises 30%, the ten-point gap is the edge, and it is a much larger edge in dollars than four points at 28%.

High IV comes in two kinds and the distinction matters. **Event IV** is elevated because a known date, earnings, a ruling, a drug trial, sits inside the expiration. The distribution is not wide, it is bimodal: a jump one way or the other, then a collapse in IV. Selling into it is a bet on the jump size, and the historical jump size is the number to check, not the rank. **Regime IV** is elevated because the market as a whole is moving, as in March 2020. The distribution is genuinely wide and the premium is compensation for a wider range that may keep widening. Carr and Wu (2009) found the variance risk premium on the S&P 500 was larger in absolute terms when implied variance was high, which is the case for selling in high-IV regimes, and their data also show the premium's realised payoff was most negative for the seller in exactly the episodes when variance jumped further.

## A practical gate

A gate is a rule that stops you trading; it does not find trades. A reasonable one for the structures in this course has three parts.

First, IV percentile at or above 50, or rank at or above 30 with percentile above 50. Below that, the credit is thin relative to the bid/ask toll (Lesson 5) and the calendar from Lesson 7 is the better use of the chain.

Second, implied volatility above recent realised volatility. Compute 20-day realised volatility as the annualised standard deviation of daily log returns; if XYZ has been realising 31% and implies 28%, the premium is cheap whatever the rank says. If it has been realising 20% and implies 28%, the eight-point gap is the reason to sell.

Third, no known event inside the expiration unless the trade is explicitly an event trade with the jump priced. The chain's November 6 expiration is clean by assumption; a real chain is not.

None of this is a forecast. Realised volatility over the next 45 days is unknown, and a stock that has realised 20% can realise 45%. The gate improves the odds that the premium you sell contains a premium, which is the only thing you are ever paid for.

## Worked example

XYZ at 100, chain IV 28%. One-year IV range 18% to 52%; IV below 28% on 240 of 252 days; 20-day realised volatility 21%.

IV rank: (28 - 18) / (52 - 18) = 10 / 34 = 29.4%.
IV percentile: 240 / 252 = 95.2%.
Implied minus realised: 28 - 21 = 7 points.

Gate: percentile 95 passes; rank 29 fails on its own but passes with the percentile; IV above realised by 7 points passes; no event. Sell.

What the 7 points are worth, on the iron condor from Lesson 6: repricing the condor at 21% gives a credit of 0.48 (a straight-line interpolation between the 0.41 at 20% and 1.04 at 28% would say 0.41 + (1/8) x 0.63 = 0.49; the model's 0.48 is lower because out-of-the-money premium is convex in volatility). Selling at 1.04 something worth 0.48 if the stock realises 21% is an expected edge of roughly 0.56 per share, $56 per condor, against a $396 maximum loss.

Same stock, same 28% IV, but the range was 18% to 32% and IV was below 28% on 170 of 252 days, realised 30%. Rank: (28 - 18) / (32 - 18) = 71%. Percentile: 67%. Implied minus realised: -2 points. Gate: rank and percentile pass, the realised comparison fails. Do not sell; the stock is moving more than the market is charging for.

One-sigma move check at three IV levels, 45 days: 20%: 100 x 0.20 x 0.351 = 7.02. 28%: 9.83. 40%: 14.04.

## Table

The model chain repriced at three implied volatilities, 45 days, XYZ 100, 4% rate. Credits per share; one-sigma move in dollars; condor break-evens in standard deviations.

| Implied volatility | 95 put | 105 call | Iron condor credit | 100 straddle | One-sigma 45-day move | Condor break-evens (sigma) |
|---|---|---|---|---|---|---|
| 20% | 0.82 | 1.16 | 0.41 | 5.60 | 7.02 | 1.57 |
| 28% (chain) | 1.69 | 2.16 | 1.04 | 7.83 | 9.83 | 1.12 |
| 40% | 3.14 | 3.76 | 1.86 | 11.18 | 14.04 | 0.79 |

Read across a row and the credit rises with IV. Read down the last column and the room for the stock to move falls. The premium is bigger because the distribution is wider; it is rich only if the distribution turns out narrower than priced.

## Sources

- Cboe Global Markets, Cboe Volatility Index (VIX) methodology: https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf
- Cboe Global Markets, VIX index dashboard and historical data: https://www.cboe.com/tradable_products/vix/
- Carr, P. and Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* 22(3): https://doi.org/10.1093/rfs/hhn038
- Bakshi, G. and Kapadia, N. (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium", *Review of Financial Studies* 16(2): https://doi.org/10.1093/rfs/hhg002

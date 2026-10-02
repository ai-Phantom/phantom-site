---
{
  "title": "Gamma and Why Short-Dated Options Move Violently",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Gamma measures:", "opts": ["The change in option price per day", "The change in delta per one-point move in the underlying", "The change in option price per point of IV", "The probability of assignment"], "correct": 1, "explain": "Gamma is the second derivative of price with respect to the stock: how fast delta itself changes as the stock moves."},
    {"q": "The ATM XYZ 100 call has gamma 0.040 at 45 DTE. At 1 DTE, with the stock still at 100, its gamma is about:", "opts": ["0.040", "0.010", "0.27", "1.00"], "correct": 2, "explain": "ATM gamma rises sharply as expiration nears: 0.040 at 45 DTE, 0.059 at 21, 0.103 at 7 and 0.272 at 1 DTE in the course's model chain."},
    {"q": "A 1 DTE ATM call is worth 0.59 with delta 0.51. The stock rises 2.00. The call is now worth about:", "opts": ["1.61 (delta times move)", "2.07, because delta rose toward 1 during the move", "0.59, gamma has no effect", "4.16"], "correct": 1, "explain": "Delta alone predicts +1.02, but gamma pushes delta from 0.51 to 0.91 as the stock rises, so the option gains about 1.48 and ends near 2.07, mostly intrinsic value."},
    {"q": "Which position is short gamma?", "opts": ["Short put", "Long put", "Long call", "Long straddle"], "correct": 0, "explain": "Every long option is long gamma; every short option is short gamma. A short put's delta moves against the writer as the stock moves in either direction."},
    {"q": "Why do 0DTE options move so violently relative to their premium?", "opts": ["Because exchanges relax price limits on expiration day", "Because with hours left, gamma is extreme: delta jumps from near 0 to near 1 across a small price range, so tiny stock moves are large percentage swings in an option that is almost all time value", "Because IV is always highest on expiration day", "Because the 100 multiplier doubles"], "correct": 1, "explain": "At 0 to 1 DTE, the ATM option's price is a small amount of pure time value and its delta changes fastest of any contract, so a move of one percent can multiply or erase the premium."}
  ],
  "task": "On a real chain, record the gamma of the ATM call in the nearest weekly expiration and in the expiration about 45 days out, and compute the ratio."
}
---


## Delta's rate of change

Lesson 4 said delta is a local estimate: it changes as the stock moves. Gamma is the amount by which delta changes for a one-point move in the stock. If the XYZ 100 call has delta 0.54 and gamma 0.040, then after XYZ rises one dollar the call's delta is about 0.58; after a one-dollar fall it is about 0.50.

Gamma is positive for every long option, call or put. A long call's delta rises as the stock rises and falls as it falls, so a long option holder is always accumulating exposure in the direction of the move and shedding it against the move. That is a desirable property, and it is what theta pays for. A short option holder has negative gamma: their delta moves against them in both directions, which is what the theta they collect compensates.

Gamma is quoted per share per one-point move. Multiply by 100 for the contract.

## Where gamma lives

Gamma is largest at the money and shrinks toward zero both deep ITM and far OTM, because delta is already near 1 or near 0 in those regions and has nowhere to go. On the XYZ 45 DTE chain the gammas are 0.009 (85 strike), 0.020 (90), 0.034 (95), 0.040 (100), 0.038 (105), 0.028 (110), 0.017 (115).

The far more important pattern is across time. ATM gamma rises as expiration approaches, and it rises fast. The 100 call's gamma is 0.028 at 90 DTE, 0.040 at 45 DTE, 0.059 at 21 DTE, 0.103 at 7 DTE and 0.272 at 1 DTE. Between 45 DTE and 1 DTE it grows nearly sevenfold. A 0DTE option in its final hours has gamma higher still.

Why? Think about what delta is: roughly, the probability of finishing ITM. With 45 days left, whether XYZ finishes above 100 is genuinely uncertain across a wide band of current prices, so delta changes gradually. With one day left, XYZ at 101 is very likely to finish above 100 (delta 0.76) and XYZ at 99 very unlikely (delta 0.25). The whole transition from "almost certainly OTM" to "almost certainly ITM" is compressed into a few dollars of stock price, and gamma is the slope of that transition.

## Gamma, theta and the market maker

A market maker who sells you the 100 call hedges by buying 54 shares. If XYZ rises one dollar, the call's delta becomes 0.58 and the hedge is now four shares short; the market maker buys four more at the higher price. If XYZ falls back, delta returns to 0.54 and they sell those four shares at the lower price. Every oscillation costs the hedger money; that cost is gamma, and the theta they collect is the payment for it. When realised volatility exceeds what was implied, the option buyer's gamma gains exceed the theta paid; when it falls short, the seller wins. Vega prices the expectation; gamma and theta settle the reality day by day.

This hedging activity is also why gamma matters to people who do not trade options. When dealers are net short gamma in a large expiration, their hedging buys strength and sells weakness, amplifying moves; when they are net long gamma, their hedging dampens moves. It is a real effect around large expirations and large 0DTE positions; it is not a reliable directional signal.

## Why short-dated options move violently

Put the pieces together. As expiration approaches, an ATM option becomes cheap (time value has decayed), its gamma becomes extreme, and its price is nearly all time value with no intrinsic cushion. A one-percent move in the stock therefore produces a huge percentage move in the option, in either direction.

At 45 DTE, XYZ moving from 100 to 102 takes the 100 call from 4.16 to 5.32, up 28%. At 7 DTE the same move takes it from 1.58 to 2.81, up 78%. At 1 DTE it goes from 0.59 to 2.07, up 251%. The reverse two-dollar move at 1 DTE takes it from 0.59 to 0.06, down 90%. Same stock, same strike, same two-dollar move; the outcomes differ by an order of magnitude because of where the contract sits on the time axis.

This is the appeal and the danger of **0DTE** trading. A 0DTE contract offers enormous leverage on the next few hours, at the price of theta that consumes the entire premium by the close and gamma so high that a normal intraday wiggle is the difference between doubling and zero. The Phantom Traders 0DTE signal cards carry the same fields as every other card, delta, DTE, spread cost, ATM or OTM, and every one of those fields should be read with this lesson in mind: a 0DTE delta is a snapshot that will be wrong within minutes.

## Gamma in spreads

One reason to trade verticals (Lesson 10) is that a spread's gamma is the difference of its legs' gammas. Long the 100 call (gamma 0.040) and short the 105 call (gamma 0.038) leaves net gamma of about 0.002 at entry; the position's delta barely moves for small stock moves, its theta is correspondingly small, and its behaviour is far more predictable than a naked call's. As expiration approaches and the stock sits between the strikes, gamma reappears and the spread's value becomes highly sensitive to whether the stock ends above or below each strike, which is pin risk, the subject of Lesson 11.

## Worked example

XYZ at 100.00, representative chain, 28% IV, 4% rate. Compare the 100 call at three expirations, stock moving from 100 to 102 and from 100 to 98.

**45 DTE (Nov 6). Price 4.16, delta 0.54, gamma 0.040.**
- Delta-only estimate for +2.00: 4.16 + 0.54 x 2 = 5.24.
- Gamma correction: 0.5 x 0.040 x 2^2 = 0.08. Estimate 5.32. Full model: **5.32**. Gain +28%.
- For -2.00: 4.16 - 1.08 + 0.08 = 3.16. Full model: **3.16**. Loss -24%.
- New delta after +2.00: 0.54 + 0.040 x 2 = 0.62 (model 0.62).

**7 DTE (Oct 30). Price 1.58, delta 0.52, gamma 0.103.**
- Delta-only for +2.00: 1.58 + 1.04 = 2.62. Gamma correction 0.5 x 0.103 x 4 = 0.21. Estimate 2.83. Full model: **2.81**. Gain +78%.
- For -2.00: 1.58 - 1.04 + 0.21 = 0.75. Full model: **0.76**. Loss -52%.
- New delta after +2.00: 0.52 + 0.206 = 0.73 (model 0.71).

**1 DTE (Nov 5). Price 0.59, delta 0.51, gamma 0.272.**
- Delta-only for +2.00: 0.59 + 1.02 = 1.61. Gamma correction 0.5 x 0.272 x 4 = 0.54. Estimate 2.15. Full model: **2.07**. Gain +251%.
- For -2.00: delta-only 0.59 - 1.02 = negative, which is impossible; the linear estimate has broken down. Full model: **0.06**. Loss -90%.
- New delta after +2.00: model 0.91. The estimate 0.51 + 0.544 = 1.05 exceeds 1, another sign that at this DTE gamma itself changes too fast for a one-step approximation.

The last block is the lesson. At 1 DTE, the Greeks on your screen describe the next few cents of stock movement, not the next two dollars. Any position sizing based on "delta 0.51" for a 1 DTE or 0DTE option is sizing for a contract that will have delta 0.91 or 0.09 an hour later.

## Table

The 100 call across expirations, stock at 100, IV 28%. Percent changes are for a 2.00 move in XYZ.

| DTE | Price | Delta | Gamma | Theta/day | Theta as % of price | Value at 102 | Value at 98 | Move for +2.00 | Move for -2.00 |
|---|---|---|---|---|---|---|---|---|---|
| 45 | 4.16 | 0.54 | 0.040 | -0.049 | 1.2% | 5.32 | 3.16 | +28% | -24% |
| 21 | 2.79 | 0.53 | 0.059 | -0.069 | 2.5% | 3.96 | 1.86 | +42% | -33% |
| 7 | 1.58 | 0.52 | 0.103 | -0.116 | 7.3% | 2.81 | 0.76 | +78% | -52% |
| 1 | 0.59 | 0.51 | 0.272 | -0.298 | 50.5% | 2.07 | 0.06 | +251% | -90% |

Every column moves the same direction down the table: less premium, more gamma, more theta as a share of what you paid, and wilder outcomes. That is the whole story of short-dated options in one grid.

## What to do with gamma

For long-option trades, gamma is the reason to hold through a move rather than scale out too early when the thesis is working: your exposure grows with the trend. It is also the reason to respect exit rules on the losing side, because your exposure shrinks as the stock moves against you, and the "it can't fall much further" instinct is measuring an option whose delta has already collapsed. For short-option trades, gamma is the risk you are paid for, and the last two weeks before expiration, where gamma is highest, are where most of that risk concentrates. Lesson 9 sets DTE rules for buyers; Lesson 10 sets them for spread sellers; Lesson 12 sizes both.

## Sources

- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy* 81(3): https://www.jstor.org/stable/1831029
- Cboe Global Markets, Options Institute, gamma and the Greeks: https://www.cboe.com/education/
- Cboe Global Markets, research on SPX 0DTE option trading and market impact: https://www.cboe.com/insights/
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document

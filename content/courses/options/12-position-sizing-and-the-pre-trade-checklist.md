---
{
  "title": "Position Sizing and the Pre-Trade Checklist",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Your account is $25,000 and your rule is to risk at most 1% per trade. A bull call spread has max loss $200. How many spreads?", "opts": ["5", "2", "1", "12"], "correct": 2, "explain": "1% of 25,000 is $250. 250 / 200 = 1.25, rounded down to 1 spread. Never round up."},
    {"q": "Same account and rule. A long 100 call costs $424. How many contracts?", "opts": ["0; the max loss exceeds the risk budget, so change the structure or the rule", "1, rounding up", "2", "As many as buying power allows"], "correct": 0, "explain": "424 > 250, so one contract already breaks the 1% rule. The choices are a cheaper defined-risk structure (a spread), a smaller account fraction of a higher-delta option, or a deliberate, written exception to 2%, not silent rounding up."},
    {"q": "For a credit spread, the number to size against is:", "opts": ["The credit received", "The width minus the credit, which is the max loss and the margin held", "The delta", "The notional value of the shares"], "correct": 1, "explain": "A 95/90 put spread sold for 1.08 risks 5.00 - 1.08 = 3.92 per share, $392 per spread. Sizing to the $108 credit understates the risk by more than three times."},
    {"q": "What is the model's expected value of a fairly priced option position at expiration, before costs?", "opts": ["Strongly positive for buyers", "Strongly positive for sellers", "Approximately zero, so any edge must come from a view that differs from what is priced", "Equal to the premium"], "correct": 2, "explain": "A price set by no-arbitrage replication has roughly zero expected value under the model's own probabilities. After the 4% to 14% cost hurdle it is slightly negative. Edge is a disagreement with the market, and it must be stated."},
    {"q": "Which item does NOT belong on a pre-trade checklist?", "opts": ["The next earnings date and whether it falls inside the expiration", "The bid-ask spread as a percent of mid", "Whether a friend is also in the trade", "The DTE at which you will exit regardless of price"], "correct": 2, "explain": "A checklist holds items that change the decision: event risk, cost, time stop. Social confirmation is not a risk control."}
  ],
  "task": "Fill in all 22 checklist items for one hypothetical trade using a real chain, and note which items you could not answer from your platform in under a minute."
}
---

## Size is the only Greek you fully control

Every earlier lesson described a risk you can measure but not eliminate: delta, theta, vega, gamma, cost, assignment. Sizing is the one decision that scales all of them at once, and the one that determines whether a run of ordinary losses is a bad month or the end of the account. It is also the part of options trading that is most often skipped, because a $200 spread feels small and buying five of them feels like a rounding error. This lesson makes the arithmetic explicit and then hands you a checklist that forces every earlier lesson to be applied before an order is placed.

## Fixed-fraction risk

The workhorse rule is a fixed fraction of the account at risk per trade, sized against the position's **maximum loss**, not its premium, its margin, or its delta. For defined-risk positions the maximum loss is known exactly: the debit for debit spreads and long options; width minus credit for credit spreads. For undefined-risk positions (naked short options) the maximum loss is either the strike times 100 (short puts) or unbounded (short calls), and the rule does not produce a number, which is the rule's way of telling you those positions need a different framework and a different approval level.

One percent per trade is a conservative baseline for a new options trader; two percent is a common ceiling. The count of contracts is the risk budget divided by the max loss per contract, **rounded down**. If the result is zero, the position does not fit and the answer is to change the structure (a narrower spread, a higher-delta option with a defined stop), not to buy one anyway.

Two portfolio-level limits complete the rule. Total premium at risk across all open long options and debit spreads should stay under a cap (5% of the account is a common figure), because long options can all go to zero in the same week. And total margin posted for credit spreads should stay under a cap (10% to 20%), because they can all move to max loss together in a fast sell-off, when correlations converge.

## Why the model says your edge is zero

A fairly priced option has, under the model's own probabilities, an expected value at expiration equal to its price grown at the risk-free rate. The 100/105 bull call spread at 2.00 has a model expected payoff of about 2.00 x 1.0049 = 2.01. Subtract the 2.00 you paid and the 0.16 to 0.29 in round-trip costs and the expected value is between -0.15 and -0.28 per share. That is not a reason not to trade; it is a statement of where the profit has to come from. It has to come from a view that the stock's distribution differs from the one priced, or that IV is mispriced relative to what will be realised, and that view must be written down as the first line of the plan, because it is the only thing in the plan that can make the expected value positive.

This is why the Phantom Traders cards list the mechanics of a contract (delta, DTE, spread cost, moneyness) and not a promise. The mechanics tell you what you are buying. The thesis is yours.

## The 22-point pre-trade checklist

Group A, the thesis:
1. Underlying and direction in one sentence, with the price level you expect and the date by which you expect it.
2. Why the market disagrees with you: what is priced (from the straddle's implied move, Lesson 8) versus what you expect.
3. What would prove you wrong, as a price level or an event.
4. Any scheduled event inside the expiration: earnings, dividend ex-date, index rebalance, macro release.

Group B, the contract:
5. Expiration and DTE at entry; DTE at planned exit.
6. Strike(s) and their delta(s); moneyness (ITM, ATM, OTM) of each leg.
7. Bid, ask and mid of each leg, and the net for the structure.
8. Spread as a percent of mid for the structure (the card's spread cost).
9. Open interest and today's volume at each strike relative to your size.
10. Deliverable: exactly 100 ordinary shares, or an adjusted contract?

Group C, the cost:
11. Round-trip cost in dollars and as a percent of net premium, including commissions.
12. Daily theta as a percent of net premium.
13. Cost hurdle plus expected theta over the planned hold, as the minimum move in the option and in the stock.

Group D, volatility and Greeks:
14. IV of the ATM strike, IV rank and IV percentile.
15. Term structure: does the expiration you chose carry an event premium?
16. Net delta, gamma, theta and vega of the structure per contract.
17. P&L of the structure if IV moves 5 points against you overnight.

Group E, risk and exits:
18. Maximum loss per contract, in dollars, defined or undefined.
19. Number of contracts = risk budget / max loss, rounded down; the risk budget as a percent of account.
20. Profit target in premium and in stock price.
21. Loss stop in premium and in stock price.
22. Time stop in DTE, and the expiration-day rule (close before the bell, or cash-settled).

If any of the 22 is blank, the order does not go in. It sounds slow. After a dozen trades it takes four minutes, and it eliminates the trades that fail because of something you knew and did not look at.

## Worked example

Account: $25,000. Rule: 1% risk per trade ($250), 5% cap on long premium ($1,250), 15% cap on credit-spread margin ($3,750). XYZ at 100.00, representative chain, 45 DTE.

**Candidate 1: long 100 call at 4.24.** Max loss $424.65 with commission. 250 / 424.65 = 0.59, rounded down to **0 contracts**. Does not fit at 1%. At a written 2% exception ($500): 500 / 424.65 = 1.18, **1 contract**. Long premium after the trade: $425 of the $1,250 cap.

**Candidate 2: 100/105 bull call spread at 2.13 (market fills).** Max loss 213 + 1.30 = $214.30. 250 / 214.30 = 1.17, **1 spread**. Delta +19 per spread, so the stock-equivalent exposure is about $1,900. Cost hurdle: about 0.29 / 2.13 = 13.6% at market, so the plan must use limit orders at or near the 2.00 mid, which drops the hurdle to about 8%.

**Candidate 3: 95/90 bull put credit spread at 1.00 (market) or 1.05 (limit).** Max loss = 5.00 - 1.05 = 3.95, $395 plus 1.30 commissions = $396.30. 250 / 396.30 = 0.63, **0 spreads** at 1%; at 2%, 500 / 396.30 = 1.26, **1 spread**. Margin posted: $395 of the $3,750 cap. Note the trap: sizing to the $105 credit would have suggested two spreads at 1%; sizing to the $395 max loss says one at 2%.

**The vega line (item 17).** Bull call spread net vega about +0.010: a 5-point IV drop costs 0.05, $5 per spread. Long 100 call vega 0.139: a 5-point drop costs 0.70, $70 per contract, 16% of the premium. The spread passes item 17 without comment; the long call needs the IV rank checked (item 14) before it does.

**The thesis lines (items 1 to 3).** Thesis: XYZ to 106 by 16 October. Priced: the 45 DTE straddle at 7.83 implies a one-sigma move of about 9.80 by 6 November, so a 6.00 move in three weeks is inside one standard deviation: the market does not consider it unusual, and the spread's 2.00 price gives it roughly a 42% chance of finishing above 102. Your edge, if any, is a reason to think the probability is higher than that, and it goes on line 2. Invalidation: a close below 97, line 3.

**Resulting plan.** One 100/105 bull call spread, limit 2.05, target 3.00 (about 60% of max gain; hold for more only if XYZ is above 105 at the time stop), stop 1.00, time stop 16 October, close before the bell on 6 November in all cases. Risk $205, 0.8% of the account.

## Table

Sizing three candidates on a $25,000 account against a 1% and a 2% per-trade risk budget. Max loss includes $0.65 per contract per side.

| Structure | Entry | Max loss per unit | Units at 1% ($250) | Units at 2% ($500) | Delta per unit | Vega per unit | Hurdle at market |
|---|---|---|---|---|---|---|---|
| Long 100 call | 4.24 | $424.65 | 0 | 1 | +54 | +13.9 | 4.2% |
| 100/105 bull call spread | 2.13 | $214.30 | 1 | 2 | +19 | +1.0 | 13.6% |
| 95/90 bull put spread | 1.05 credit | $396.30 | 0 | 1 | +15 | -4.5 | 17% |

Delta and vega are per unit in dollars per one-point move; the credit spread's delta is the net of the short 95 put (-0.27) and long 90 put (-0.12) with the sign flipped for the short.

## The habit

Size last, after every other line is filled in, because the max loss you size against depends on the structure, the fills and the exits you have already chosen. Then write the order exactly as the plan states it, with the limit price, and do not change the count because the fill looked good. The next lesson, the capstone, has you produce this entire document for one spread, priced three ways, and grade it against a rubric.

## Sources

- FINRA, Investor Insights, managing risk with options and understanding margin: https://www.finra.org/investors/investing/investment-products/options
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*, risk disclosure chapter: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- U.S. Securities and Exchange Commission, Investor.gov, options and risk: https://www.investor.gov/introduction-investing/investing-basics/glossary/options
- Cboe Global Markets, Options Institute, position sizing and risk management: https://www.cboe.com/education/

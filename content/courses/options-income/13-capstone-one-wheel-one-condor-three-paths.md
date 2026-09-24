---
{
  "title": "Capstone: One Wheel, One Condor, Three Price Paths",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On path C (XYZ 84 on November 6) the wheel's put is assigned. Marked at 84.00 against the 93.31 basis, the wheel's P&L on November 6 is:", "opts": ["-$931", "-$762", "-$1,100", "-$1,600"], "correct": 0, "explain": "(84.00 - 93.31) x 100 = -$931. The 1.69 credit is already inside the 93.31 basis; adding it again would double-count. Buy-and-hold from 100 is -$1,600 on the same path."},
    {"q": "On path A (XYZ 103 at the October 16 checkpoint) the condor marks at 0.54. Closing there earns:", "opts": ["$54", "$104", "$50, 48% of the credit", "$63"], "correct": 2, "explain": "1.04 - 0.54 = 0.50 per share, $50 per condor, 48% of the maximum. The 50% rule would have it close at 0.52, so this is a hold-or-close judgment call the rubric asks you to defend."},
    {"q": "The condor's buying-power reduction on both Reg T and portfolio margin is $396. Under a 1% budget on $50,000, the number of condors is:", "opts": ["2", "1", "5", "0"], "correct": 1, "explain": "$500 / $396 = 1.26, rounded down to 1."},
    {"q": "On path C the 21-DTE checkpoint shows XYZ 92, IV 34%, and the short 95 put marked at 4.63. The fresh-trade test for rolling to the December 95 put at 7.06 asks:", "opts": ["Whether the roll can be done for a credit", "Whether you would sell a December 95 put at 7.06, 3 points in the money with delta about -0.57, as a new position today", "Whether the December put has more than 30 days", "Whether IV rank is above 50"], "correct": 1, "explain": "A roll is a close plus an open. If the open is not a trade you would place on its own, the roll is a way of not booking the $294 loss."},
    {"q": "After completing the capstone, the honest annualised return figure to put in your plan for the wheel is:", "opts": ["The path A return compounded to a year", "The average of the three paths compounded to a year", "None; three model paths give a P&L table and a comparison to buy-and-hold, not a return expectation", "The best path's return, since you would have managed the others"], "correct": 2, "explain": "The paths are chosen to exercise the arithmetic, not to represent a distribution. Lesson 12's standard-error rule applies: one cycle, or three, proves nothing about the mean."}
  ],
  "task": "Complete the capstone as a single document, score it with the rubric, and file it with your income plan as the worked standard every future trade is checked against."
}
---

## The assignment

You will run two positions from the model chain, from entry through a 21-DTE checkpoint to expiration, along three stated price paths, and produce every number a plan requires: credits, buying power, maximum loss, checkpoint marks and decisions, realised P&L, a buy-and-hold comparison, a tax line, and a sizing line. Everything is on the chain you have used since Lesson 1, and every input you need is stated below. Show every calculation; a correct number without its arithmetic earns half marks.

**Model chain.** XYZ 100.00 on September 22, 2026. November 6, 2026 expiration, 45 days. IV 28%, rate 4%, no dividend. Mids: 85 put 0.16, 90 put 0.61, 95 put 1.69, 100 put 3.67; 100 call 4.16, 105 call 2.16, 110 call 1.00, 115 call 0.41. Bid/ask: 95 put 1.64 / 1.74; 90 put 0.58 / 0.64; 85 put 0.14 / 0.18; 110 call 0.96 / 1.04; 115 call 0.38 / 0.44.

**Position 1, the wheel.** Sell one November 95 put, cash-secured with $9,500. If assigned, sell one December 18, 2026 call (42 days) on the second-leg chain given under path C. Account: $50,000.

**Position 2, the iron condor.** Sell the November 90 put and 110 call, buy the 85 put and 115 call. One condor.

**Checkpoint.** October 16, 2026, 21 days to expiration.

**Path A, rally.** October 16: XYZ 103.00, IV 28%. November 6: XYZ 106.00.
**Path B, drift.** October 16: XYZ 97.00, IV 28%. November 6: XYZ 97.00.
**Path C, break.** October 16: XYZ 92.00, IV 34%. November 6: XYZ 84.00, IV 40%. Second-leg chain for the wheel, November 6, December 18 expiration, XYZ 84.00, IV 40%: 85 call 4.26, 90 call 2.42, 95 call 1.27. December 18: XYZ 88.00.

**Checkpoint marks, from the model.** October 16 values per share:

| Path | 95 put | 90 put | 85 put | 110 call | 115 call |
|---|---|---|---|---|---|
| A (103, 28%) | 0.34 | 0.05 | 0.00 | 0.66 | 0.17 |
| B (97, 28%) | 1.61 | 0.39 | 0.05 | 0.09 | 0.01 |
| C (92, 34%) | 4.63 | 1.98 | 0.60 | 0.04 | 0.01 |

Roll candidates for the put on path C, October 16, XYZ 92, IV 34%: December 95 put 7.06, December 90 put 4.31, January 15 90 put 5.19.

## What to produce

**Part 1, entry.** For each position: credit at mids and at half-spread fills; buying-power reduction under Reg T and under portfolio margin (state the -15% stress price and the position's value there; the 95 put at XYZ 85 is worth 10.16, the condor 3.06); maximum loss; break-evens; probability of profit from the model (95 put: 76%; condor: 74%); return on capital if expired worthless; contracts allowed under a 1% max-loss budget for the condor and a 2% shock-loss budget for the put.

**Part 2, checkpoint.** For each path and each position: the mark on October 16 from the table above, the open P&L, the fraction of maximum profit earned, and a decision, hold, close, or roll, with one sentence of justification. On path C, price every roll candidate as a close plus an open (net, total credits, break-even, new delta, days added) and apply the fresh-trade test in writing.

**Part 3, expiration.** For each path, the position's P&L on November 6 if held (condor) or the wheel's status: expired with premium kept, or assigned with shares marked at the November 6 price against basis. For path C, continue the wheel: choose the December call, justify the strike against basis, and compute the December 18 result at 88.00.

**Part 4, comparison and reporting.** For each path, buy-and-hold of 100 XYZ from 100.00 on September 22, marked November 6 (and December 18 on path C). The wheel's return on $9,500 including $46.85 of collateral interest. A tax line for each outcome under Publication 550 (expiry, assignment basis, qualified covered call check on the December call). A closing paragraph on what the three paths do and do not tell you.

## Worked example

Path B in full, as the standard for the other two.

Entry, September 22. Wheel: sell 95 put at 1.69 mid ($169); at the 1.64 bid, $164. Cash $9,500. Basis if assigned 93.31. Max loss $9,331. Reg T uncovered requirement max(169 + 2,000 - 500, 169 + 950) = $1,669; portfolio margin at XYZ 85: (10.16 - 1.69) x 100 = $847. Shock-loss budget 2% of 50,000 = $1,000; 1,000 / 847 = 1 contract. Probability the put expires worthless: 1 - 0.24 = 76%. Return on cash if expired: (169 + 46.85) / 9,500 = 2.27%.

Condor: credit (0.61 - 0.16) + (1.00 - 0.41) = 1.04 ($104); at half-spread fills 1.04 - 0.12 = 0.92. Max loss 5.00 - 1.04 = 3.96 ($396); buying power $396 on Reg T and, with broker minimums, on portfolio margin (stress value 3.06 at XYZ 85 implies a $202 loss before minimums). Break-evens 88.96 and 111.04. POP 74%. Return on capital 104 / 396 = 26.3%. Budget 1% = $500; 500 / 396 = 1 condor.

Checkpoint, October 16, XYZ 97.00. Put marks 1.61: open P&L 1.69 - 1.61 = +0.08 ($8), 5% of maximum. Decision: hold; the put is 2 out of the money with 21 days, and closing at 1.61 gives up nearly the whole premium; assignment at 93.31 remains acceptable. Condor marks 0.39 - 0.05 + 0.09 - 0.01 = 0.42: open P&L 1.04 - 0.42 = +0.62 ($62), 60% of maximum. Decision: close; both the 50% rule (0.52) and the 21-DTE rule say so, and the remaining 0.42 is not worth three weeks of gamma with the stock 7 points from the put strike.

Expiration, November 6, XYZ 97.00. Put expires; keep $169 plus $46.85 interest; return 2.27% on $9,500 for 45 days. Condor, if held: all legs expire, +$104; as closed on October 16: +$62, 15.7% on $396.

Comparison. Buy-and-hold 100 XYZ from 100.00 to 97.00: -$300. Wheel: +$215.85. Condor: +$62 closed, +$104 held.

Tax. Put expiring November 6: $169 short-term capital gain dated November 6. Condor closed October 16: $62 short-term gain dated October 16 (four option lines). No shares, no qualified-covered-call question.

Paths A and C follow the same template. For reference, the checkpoint condor marks are 0.54 on A (open P&L +$50, 48%) and 1.41 on C (open P&L -$37); held to expiration the condor finishes +$104 on A and -$396 on C. The wheel on A expires (+$169); on C it is assigned, and marked at 84.00 the shares stand at (84.00 - 93.31) x 100 = -$931 on November 6, against -$1,600 for buy-and-hold. The December 95 call at 1.27 is the strike at or above basis; at 88.00 on December 18 it expires, and the cycle stands at (88.00 - 93.31) x 100 + 127 = -$404 marked, against -$1,200 for buy-and-hold.

## Chart

![Capstone results on November 6 for the three paths: wheel (put expired +169 on A and B; assigned and marked at 84.00 for -931 on C), iron condor held to expiration (+104, +104, -396), and iron condor closed at the October 16 checkpoint (+50, +63, -37). Source: the capstone's worked example and checkpoint table.](figures/capstone-three-paths.svg)

The two green pairs are what most cycles look like. The right-hand group is one cycle in four, and it is the one the sizing rules were written for.

## Rubric

Score out of 100. A pass is 70 with no criterion below half marks.

| Criterion | What earns full marks | Points |
|---|---|---|
| Wheel arithmetic | Credit at mid and fill, cash reserved, basis, max loss, Reg T and portfolio-margin requirements, POP, return on cash with interest, and on path C the second-leg call chosen at or above basis with the December 18 result and the -$931 / -$404 marks derived, not asserted | 25 |
| Condor arithmetic | Credit at mid and fill, max loss, buying power with the one-side reasoning stated, break-evens, POP, return on capital, all three checkpoint marks built leg by leg from the table, and expiration results on all three paths | 25 |
| Sizing and budget | Contracts under the 1% and 2% budgets computed and rounded down, the portfolio ceiling checked, and the distinction between buying power, shock loss and theoretical max loss stated for both positions | 15 |
| Checkpoint decisions and the roll test | A hold/close/roll decision on every path for both positions with one-sentence justifications that cite the 50% rule, the 21-DTE rule, or the ownership test; on path C every roll candidate priced as close-plus-open and the fresh-trade test answered in writing | 15 |
| Comparison, tax and honesty | Buy-and-hold on each path over the same dates; the wheel's return on the full $9,500 with interest; correct Publication 550 treatment of each outcome including the qualified-covered-call check; and a closing paragraph that draws no return expectation from three paths and states what would be needed to (Lesson 12) | 20 |

## What passing means

If you can produce this document in an afternoon, you can take any short-premium idea, price it, size it, decide in advance what you will do at 21 days and at a loss, account for it the way the PUT index is accounted for, and compare it to simply owning the shares. That is the entire discipline of selling premium. The structures will vary; the ledger, the budget and the benchmark do not.

## Sources

- Cboe Global Indices, PUT and CNDR index methodologies (the mechanical benchmarks for the two positions): https://www.cboe.com/us/indices/dashboard/put/ and https://cdn.cboe.com/api/global/us_indices/governance/CNDR_Methodology.pdf
- FINRA Rule 4210, Margin Requirements: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- Internal Revenue Service, Publication 550 (2025), "Writers of puts and calls" and "Qualified covered call options and optioned stock": https://www.irs.gov/publications/p550
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document

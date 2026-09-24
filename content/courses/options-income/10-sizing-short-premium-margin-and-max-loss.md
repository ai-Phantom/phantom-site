---
{
  "title": "Sizing Short Premium: Buying Power, Margin and the Max-Loss Budget",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under Reg T (FINRA Rule 4210), the requirement for the chain's uncovered November 95 put is:", "opts": ["$9,500", "$1,119", "$1,669", "$392"], "correct": 2, "explain": "Greater of 20% x 10,000 - 500 OTM + 169 = $1,669 and 10% x 9,500 + 169 = $1,119. So $1,669."},
    {"q": "Portfolio margin under FINRA Rule 4210(g) sets the requirement for an equity position by:", "opts": ["A fixed 20% of underlying value", "Stress-testing the position's theoretical value across a range of underlying prices, plus or minus 15% for individual equities, and charging the worst loss", "The premium received times ten", "The same width-minus-credit formula as Reg T"], "correct": 1, "explain": "Portfolio margin uses the OCC's TIMS model: the position is repriced at price points across a specified range (+/-15% for single stocks, narrower for broad indexes) and the largest loss is the requirement, with minimums."},
    {"q": "Using the 1% max-loss budget on a $50,000 account, how many November 90/85 + 110/115 iron condors (max loss $396) may you hold?", "opts": ["5", "2", "1", "12"], "correct": 2, "explain": "Budget 1% x 50,000 = $500. 500 / 396 = 1.26, rounded down to 1. Two condors would put $792 at risk, above the budget."},
    {"q": "Why should the cash-secured put be sized by a shock loss (for example the -15% portfolio-margin stress) rather than by its theoretical maximum loss of $9,331?", "opts": ["Because the theoretical maximum makes the trade unsizeable under any budget, while the shock loss ($847 at -15%) is the number that recurs; budget to the shock, hold cash for the strike", "Because $9,331 cannot actually be lost", "Because brokers only charge for the shock", "Because puts are always assigned before the stock reaches zero"], "correct": 0, "explain": "A stock going to zero in 45 days is possible but not the planning case. Budgeting to a repeatable shock while keeping full cash reserved keeps both the budget and the true capital-at-risk honest."},
    {"q": "Your broker shows the condor's buying-power reduction as $396 while the covered call shows $4,784 on Reg T and $1,290 on portfolio margin. What is the correct reading of 'buying power'?", "opts": ["It is the maximum loss for every position", "It is always half the capital at risk", "It is the premium received", "It is the broker's collateral demand, which equals maximum loss only for defined-risk spreads; for stock and naked options it is smaller than what you can lose"], "correct": 3, "explain": "The condor's collateral equals its max loss. The covered call's collateral is a fraction of the $9,784 it can lose. Size to the loss, not to the collateral."}
  ],
  "task": "Write down your account size, your max-loss budget per position as a percentage, and for each structure in this course the number of contracts that budget allows using the shock-loss figures in this lesson."
}
---

## Two different numbers

Every short-premium position has a buying-power reduction, the collateral your broker locks, and a maximum loss, the most you can actually lose. For a credit spread or an iron condor they are the same number: width minus credit. For everything else they are not, and confusing them is how accounts with a defined-risk mindset blow up on undefined-risk trades.

On the chain: the November 95/90 bull put spread has buying power $392 and maximum loss $392. The uncovered 95 put has Reg T buying power $1,669 and maximum loss $9,331. The covered call (100 shares plus short 105 call) has Reg T buying power of about $4,784 and can lose $9,784. Position sizing has to start from the second column.

## Reg T and FINRA Rule 4210

Reg T is the Federal Reserve's initial margin rule; FINRA Rule 4210 sets the maintenance and the specific formulas brokers apply. For short options the rule you need is 4210(f)(2).

**Uncovered equity put or call.** The greater of: 100% of the premium plus 20% of the underlying's value minus any out-of-the-money amount; or 100% of the premium plus 10% of the strike (puts) or 10% of the underlying (calls). Chain 95 put: max(169 + 2,000 - 500, 169 + 950) = $1,669. Chain 110 call, uncovered: max(100 + 2,000 - 1,000, 100 + 1,000) = $1,100. The requirement is recomputed every day and rises as the option moves toward and into the money, which means margin calls arrive on the days the position is losing.

**Spreads with the long expiring no earlier than the short.** The difference in strikes minus the credit, or in practice the difference in strikes, with the credit applied. Chain 95/90 put spread: $500 - $108 = $392. Chain condor: $500 - $104 = $396, charged on one side only because the two sides cannot both lose.

**Covered call.** The stock is margined as stock, 50% initially under Reg T, and the call is covered so it carries no separate requirement; the premium received may be applied. Chain: 50% x $10,000 - $216 = $4,784.

**Cash-secured put** is not a margin concept. It is a choice to hold the full strike in cash, $9,500, so that assignment can never produce a margin call. Brokers allow puts to be sold in cash accounts on that basis.

## Portfolio margin

FINRA Rule 4210(g) permits qualifying accounts to be margined by risk rather than by formula. Positions are repriced under the OCC's TIMS model across a range of underlying prices, plus or minus 15% for individual stocks and narrow indexes, a tighter band for high-capitalisation broad indexes, and the requirement is the largest theoretical loss across the scenarios, subject to minimums. Brokers require approval and, under the rule, a minimum account equity that most set at $100,000 or more.

On the chain, the -15% scenario puts XYZ at 85. The 95 put repriced at 85 with 45 days and 28% IV is worth 10.16; the loss from the 1.69 sale is 8.47 per share, so the requirement is about $847 against Reg T's $1,669. The covered call at 85: shares lose $1,500, the 105 call falls from 2.16 to 0.06 and gains $210; net $1,290 against Reg T's $4,784. The condor at 85: worth 3.06, loss 2.02, about $202, though brokers apply a minimum per contract that typically brings a five-wide condor back near its $396 maximum loss. The credit spread is unchanged at $392.

Portfolio margin roughly halves the collateral on the naked put and cuts it by three-quarters on the covered call. That is its purpose and its hazard. The maximum loss on the put is still $9,331; only the collateral changed. An account that sizes to buying power will hold twice as many puts under portfolio margin as under Reg T and lose twice as much in a crash that exceeds the 15% stress band. March 2020 exceeded it.

## The max-loss budget

The rule that keeps a short-premium book alive is a cap on the loss any one position can inflict, expressed as a fraction of the account. One percent is the conventional figure for defined-risk trades; some use two. The mechanics:

Budget per position = account x budget percentage. Contracts = budget / loss per contract, rounded down. Zero is a valid answer.

The loss per contract is the maximum loss for defined-risk trades. For undefined-risk trades it is a planning loss, and the choice is the whole difficulty. Use the theoretical maximum ($9,331 on the put) and no budget under 10% will let you sell a single put on a $50,000 account. Use the credit and you will size to twenty puts. The defensible middle is a shock loss: the loss at a specified adverse move you are prepared to see, such as the -15% portfolio-margin scenario or a two-standard-deviation move (19.66 on the chain, XYZ to 80, where the 95 put is worth about 15 and the loss is about $1,330). Budget to the shock, keep full cash against the strike, and accept in writing that the true tail exceeds the budget.

Then the portfolio rule: every short-premium position in the book is short the same variance factor, so the budget applies to the sum. Five condors on five stocks at 1% each are 5% of the account at risk in one crash, and they will all lose in the same week. A total short-premium max loss of 5 to 10% of the account is a common ceiling; the BXM's -35.8% and PUT's -32.7% drawdowns are what an uncapped book on the index looked like.

## Worked example

Account $50,000. Max-loss budget 1% per position = $500. Portfolio short-premium ceiling 8% = $4,000. Chain positions, per contract.

Iron condor 90/85 + 110/115: credit $104, max loss $396, buying power $396 (Reg T and PM). Contracts = 500 / 396 = 1.26, so 1. Risk $396.

Bull put spread 95/90: credit $108, max loss $392. Contracts = 500 / 392 = 1.27, so 1. Risk $392.

Cash-secured 95 put: credit $169, theoretical max loss $9,331, cash held $9,500. Reg T uncovered requirement max(169 + 2,000 - 500, 169 + 950) = $1,669. PM requirement at -15%: 95 put at XYZ 85 = 10.16, loss (10.16 - 1.69) x 100 = $847. Shock loss at -15%: $847. Contracts by shock = 500 / 847 = 0.59, so 0 under a 1% budget; under 2% ($1,000): 1. Two-sigma shock (XYZ 80): loss about $1,330, 0 contracts under 2%.

Covered call, 100 shares at 100 plus short 105 call at 2.16: outlay $9,784, max loss $9,784. Reg T buying power 0.5 x 10,000 - 216 = $4,784. PM at -15%: -1,500 + (2.16 - 0.06) x 100 = -1,500 + 210 = -$1,290. Shock loss $1,290. Contracts by shock under 2%: 1,000 / 1,290 = 0, under 3%: 1.

Portfolio check with 1 condor, 1 spread and, under a 2% budget, 1 cash-secured put: defined-risk max loss 396 + 392 = $788; put shock $847; total $1,635 = 3.3% of the account, inside the $4,000 ceiling. Tail beyond the shock: the put's remaining $8,484 of theoretical exposure is the number you have agreed to carry, and the $9,500 in cash is what makes carrying it survivable.

## Table

Collateral versus loss for the chain's four structures, per contract. Shock loss is the loss at XYZ 85 (-15%), 45 days, 28% IV, from the model.

| Position | Credit | Reg T buying power | Portfolio margin (approx.) | Shock loss at -15% | Theoretical max loss | Contracts under 1% of $50k |
|---|---|---|---|---|---|---|
| Iron condor 90/85 + 110/115 | $104 | $396 | $396 (minimums apply) | $202 | $396 | 1 |
| Bull put spread 95/90 | $108 | $392 | $392 | $392 | $392 | 1 |
| Uncovered 95 put | $169 | $1,669 | $847 | $847 | $9,331 | 0 (1 at 2%) |
| Covered call 105 | $216 | $4,784 | $1,290 | $1,290 | $9,784 | 0 (1 at 3%) |

## Sources

- FINRA Rule 4210, Margin Requirements, paragraphs (f)(2) options and (g) portfolio margin: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- Cboe Global Markets, Margin Manual: https://www.cboe.com/us/options/strategy_based_margin/
- Options Clearing Corporation, portfolio margin and TIMS: https://www.theocc.com/risk-management/customer-portfolio-margin
- Federal Reserve Board, Regulation T (12 CFR Part 220): https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-220

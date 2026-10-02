---
{
  "title": "Expected Value: Why Win Rate Misleads, the Cost Stack, and Sizing",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The RSI(2) rule from lesson 4 won 75.5% of 94 trades with an average winner of +1.15% and an average loser of −1.40%. Its expected value per trade is:", "opts": ["+1.15%", "0.755 × 1.15 − 0.245 × 1.40 = +0.525%", "75.5%", "−0.25%"], "correct": 1, "explain": "Expected value is win rate times average win minus loss rate times average loss. +0.525% matches the measured +0.527% average trade to rounding. Costs were already inside the trade returns."},
    {"q": "A reversion rule wins 90% of the time with an average winner of +0.5% and an average loser of −6%. Its expected value is:", "opts": ["+0.45%", "+0.5%", "−0.15%", "+6%"], "correct": 2, "explain": "0.90 × 0.5 − 0.10 × 6 = 0.45 − 0.60 = −0.15%. A rule can win nine times in ten and lose money, and reversion rules without stops are the classic way to build one."},
    {"q": "In the lesson 8 XLE/XOP trade, costs were $22.72 of transaction cost and $45.16 of borrow. The borrow was the larger item because:", "opts": ["XLE is hard to borrow", "The position was held 179 trading days; borrow accrues daily on the short leg while the bid-ask cost is paid once, so on a slow spread carry dominates", "Yahoo Finance charges for data", "Transaction costs were zero"], "correct": 1, "explain": "0.5% per year on $12,717 for 179/252 of a year is $45.16, twice the round-trip spread cost. The longer the half-life, the larger the share of the edge that carry consumes."},
    {"q": "With a 2σ entry, a 4σ stop and a formation standard deviation of 0.0510 in the log spread, the risk on a $10,000 Y leg is roughly:", "opts": ["$100", "2 × 0.0510 = 10.2% of the leg, about $1,020, plus costs", "$5,100", "4% of the leg"], "correct": 1, "explain": "The distance from entry to stop is 2 standard deviations of the log spread, 0.102, which is about 10.2% of the Y leg's notional (10.7% compounded). To risk 1% of a $50,000 account you would size the Y leg at about $4,900."},
    {"q": "D'Avolio (2002) found that in the U.S. stock lending market:", "opts": ["Every stock costs 10% per year to borrow", "About 91% of stocks by value were 'general collateral', borrowable at under 1% per year, while a small minority were expensive or unavailable; the expensive ones are often exactly the names a reversion short wants", "Borrowing is free", "ETFs cannot be borrowed"], "correct": 1, "explain": "The 0.5% assumption used in this course is reasonable for liquid ETFs and large-caps. It is not reasonable for a heavily-shorted single stock, where the fee can exceed the entire expected edge."}
  ],
  "task": "Take any set of at least twenty trades you have made or simulated, compute win rate, average win, average loss and the expected value per trade, and compare it with the simple average."
}
---

Reversion rules win often. That is the property that sells them and the property that hides their risk, because a high win rate says nothing about expected value until you know the size of the losers, and reversion losers are large by construction: the trade is a bet against a move that has just happened, and the one time in five it keeps going, it keeps going. This lesson puts the trades from earlier lessons into the expected-value equation, itemises the costs a reversion trader actually pays, and derives position size from the stop rather than from the win rate.

## The equation

Expected value per trade = p × W − (1 − p) × L − C

where p is the win rate, W the average winner, L the average loser (as a positive number) and C the round-trip cost if it is not already inside W and L. Everything about a rule's economics is in this one line, and the win rate is only one of its four terms.

**RSI(2) rule, lesson 4.** p = 0.755, W = 1.15%, L = 1.40%, costs already inside the returns: EV = 0.755 × 1.15 − 0.245 × 1.40 = 0.868 − 0.343 = **+0.525%** per trade. The measured average trade was +0.527%. The losers are larger than the winners; the rule is profitable because it wins three times as often as it loses, and only because of that.

**RSI(2), exit at RSI above 70 (variant B).** p = 0.820, W = 1.21%, L = 2.29%: EV = 0.992 − 0.412 = **+0.580%**. Higher win rate, larger losers, slightly higher EV. This is the direction every reversion exit pushes as it gets more patient: p rises, L rises faster.

**Bollinger, exit at the upper band (lesson 5).** p = 0.761, W = 3.71%, L = 4.87%, worst trade −22.25%. EV = 2.823 − 1.164 = +1.66%. A fine number that was produced by a −22% event you would have had to sit through with no stop.

**XLE/XOP pair with 4σ stop and 60-day time stop, lesson 8 year.** Three trades: +$400, −$40, −$459. p = 0.33, W = $400, L = $250: EV = 133 − 167 = **−$33** per trade, or −0.15% of the $22,717 gross notional. A losing rule on a spread that failed its test, which is the result the test predicted.

**The trap.** Consider a rule with p = 0.90, W = +0.5% and L = −6%: EV = 0.45 − 0.60 = −0.15%. Nine winners, one loser, and the loser takes back more than the nine gave. Any reversion rule without a stop can be tuned into this shape by widening the exit: the win rate climbs toward 100% as you wait longer for the reversion, and L climbs toward the size of the worst move in the sample. The no-stop XOP trade of lesson 10, −$3,825 on a $10,000 leg, is what L looks like when there is no cap on it.

## Worked example

The full cost stack for the lesson 8 pair trade, entered 2026-01-05, $10,000 XOP long against $12,717 XLE short, 179 trading days. Data: Yahoo Finance daily closes; cost assumptions stated.

**Bid-ask spread.** XOP at 127.50 was quoted roughly two cents wide, XLE at 46.89 one cent. Half the spread is paid on each side: XOP 0.01 / 127.50 = 0.8 bp, XLE 0.005 / 46.89 = 1.1 bp. The course uses 5 bp per side to include slippage and the occasional wider quote: 2 sides × $22,717 × 0.0005 = **$22.72** for the round trip. On SPY, one cent wide on a $580 to $770 price, the half-spread is 0.07 to 0.09 bp, which is why lesson 4 could use 1 bp per side.

**Borrow.** The short XLE leg is borrowed. General-collateral ETFs lend at a small spread under the risk-free rate; the course uses 0.5% per year on the short notional: $12,717 × 0.005 × 179 / 252 = **$45.16**. Two thirds of the total cost of the trade, and it accrued because the spread took 179 days not to revert. D'Avolio (2002) measured the U.S. lending market and found roughly 91% of stocks by value borrowable at under 1% per year; the remainder, small, heavily-shorted or event-driven names, can cost 10% to 100% per year or be unavailable. A single-stock reversion short must check the fee before the signal.

**Margin.** Regulation T requires 50% initial margin on the long and on the short; FINRA maintenance is 25% on the long and 30% on the short. The pair therefore ties up about $5,000 + $6,359 = $11,359 of buying power for $22,717 of gross exposure, before any broker house requirements. That capital's opportunity cost is not in the trade log but is real.

**Slippage at the open.** Not applicable here: every entry and exit in this course is at the close. Lesson 6 showed that moving the same rule to the opening print adds 5 to 10 bp per side, enough to flip the sign of a gap fade.

**Fees and commissions.** Zero commission at most U.S. brokers on ETFs; SEC and FINRA transaction fees on sales are a fraction of a basis point and are ignored.

Total: $22.72 + $45.16 = **$67.88**, or 0.30% of gross notional, against a gross profit of $127. Costs took 53% of the gross. On the rolling-60 version of the same year, costs were $89.59 against a gross of −$29.

## Table

| Cost item, lesson 8 pair trade | Basis | Amount | Share of gross P&L (+$127) |
|---|---|---|---|
| Bid-ask and slippage, 4 executions | 5 bp per side × $22,717 × 2 | $22.72 | 18% |
| Borrow on $12,717 XLE short | 0.5% per year × 179/252 | $45.16 | 36% |
| Margin capital tied up (not a cash cost) | Reg T 50% each leg | $11,359 | — |
| Commissions, SEC/FINRA fees | ~0 for ETFs | ~$0 | 0% |
| Total cash cost | | **$67.88** | **53%** |

Source: trade from lesson 8 (Yahoo Finance closes); cost rates as stated; FINRA margin rules.

## Sizing from the stop

Size comes from the stop distance, not from the win rate or the expected value. The question is: if this trade goes to its stop, how much of the account is lost, and is that acceptable?

**Pair.** Entry at 2σ, stop at 4σ: the log spread moves 2 × 0.0510 = 0.102 against you, about 10.2% of the Y-leg notional (e^0.102 − 1 = 10.7% if you prefer the compounded figure). On a $10,000 leg that is roughly $1,020 plus costs. For a $50,000 account risking 1% per trade, $500 / 0.102 = **$4,900** on the XOP leg and $6,231 on the XLE leg. The 2020 trade of lesson 10 stopped at 4.69σ rather than 4.0 because z jumped through the level overnight: budget for that by treating the stop as 1.2 times its nominal distance.

**Single-instrument rule with no z-stop.** The RSI(2) rule's worst trade was −4.15% with the 200-day filter and −11.35% without it. If you accept the unfiltered version and want a worst case of 1% of the account, the position is 1% / 11.35% = 8.8% of the account, and the rule's +0.527% per trade becomes +0.046% of the account per trade, about 0.4% per year at nine trades a year. This is why lesson 4 said the filter trades return for survivability: the filtered rule's −4.15% worst trade allows a 24% position and 1.1% per year at the same risk budget.

**Never size from the win rate.** A 75% win rate feels like a reason to size up. It is not; the size of the loser is. The two numbers move together in the wrong direction as you loosen the exit, and the only quantity that stays fixed is the distance to a stop you set in advance.

## Sources

- D'Avolio, G. (2002). The market for borrowing stock. *Journal of Financial Economics*, 66(2–3), 271–306. https://doi.org/10.1016/S0304-405X(02)00206-4
- FINRA, Margin Accounts (Regulation T and maintenance requirements): https://www.finra.org/rules-guidance/key-topics/margin-accounts
- U.S. Securities and Exchange Commission, Key Points About Regulation SHO (short sale locate and borrow rules): https://www.sec.gov/investor/pubs/regsho.htm
- Frazzini, A., Israel, R. and Moskowitz, T. J. (2018). Trading costs. SSRN Working Paper 3229719. https://doi.org/10.2139/ssrn.3229719

---
{
  "title": "Managing Losers: The Arithmetic of Rolling",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On October 16 XYZ is 91.00, IV 34%, and your short November 95 put (sold at 1.69) marks at 5.28. You buy it back and sell the December 95 put at 7.06. Net for the roll, and total credits collected on the strike?", "opts": ["Net credit 1.78; total credits 3.47", "Net debit 1.78; total credits 1.69", "Net credit 7.06; total credits 8.75", "Net credit 1.78; total credits 5.28"], "correct": 0, "explain": "7.06 received minus 5.28 paid = 1.78 net credit. Together with the original 1.69 you have collected 3.47 against a 95 strike, so the new break-even is 91.53."},
    {"q": "Where did the 1.78 credit in the previous question come from?", "opts": ["From the decline in the stock", "From the extra 63 days of time value in the December put; the 4.00 of intrinsic value was paid out and bought back, not erased", "From a fall in implied volatility", "From the broker's roll rebate"], "correct": 1, "explain": "Both puts carry 4.00 of intrinsic value with XYZ at 91. The roll swaps 1.28 of remaining November time value for 3.06 of December time value; the difference is the credit, and the intrinsic loss is unchanged."},
    {"q": "Rolling down and out to the December 90 put at 4.31 instead costs a net 0.97 debit. What does it buy?", "opts": ["A higher break-even", "Nothing; debits are never worth paying", "A strike 5 points lower, so the position is at the money instead of 4 points in the money, with break-even at 89.28 against 91.53 for the same-strike roll", "A shorter time to expiration"], "correct": 2, "explain": "Total credits after the debit: 1.69 - 0.97 = 0.72; break-even 90 - 0.72 = 89.28. You pay 0.97 to move the strike 5.00 lower, and the trade is no longer a bet that the stock recovers to 91.53."},
    {"q": "The single best test of whether a roll is a decision or a denial:", "opts": ["Whether it can be done for a credit", "Whether the new position is one you would open fresh today, at today's price, with today's IV, as a new trade", "Whether the strike is unchanged", "Whether the expiration is within 60 days"], "correct": 1, "explain": "A roll is a close plus an open. If the open leg (short December 95 put at 91 with delta -0.57) is not a trade you would place on its own, the roll is a way of avoiding a realised loss, not a plan."},
    {"q": "Which structure has the weakest case for rolling a losing position?", "opts": ["A cash-secured put on a stock you want to own", "A covered call on shares you intend to keep", "A defined-risk credit spread or condor whose maximum loss is already the buying power committed", "A calendar spread"], "correct": 2, "explain": "On a defined-risk trade the loss is capped and the capital is already posted; rolling adds new risk to recover an old, bounded loss. The usual rule is to close at a predefined multiple of the credit and re-enter only if the fresh trade passes the gate."}
  ],
  "task": "Take any short-premium position you hold or have held, write the roll you would be tempted to make, price it as a close plus a fresh open, and answer in writing whether you would place the open leg on its own."
}
---

## The moment this lesson is about

It is October 16, 2026, 21 days before the November expiration. XYZ has fallen from 100 to 91.00 and implied volatility has risen from 28% to 34%. The November 95 put you sold on September 22 for 1.69 is 4.00 in the money and marks at 5.28. You are down 3.59 per share, $359, on a trade that collected $169. Every short-premium trader meets this moment, and what they do next decides whether the plan survives.

There are three honest choices: take assignment or its equivalent (close and buy the stock, or hold to expiry and be assigned), close at a loss, or roll. This lesson prices the roll, because it is the one that is most often done badly.

## What a roll is

A roll is two trades: close the existing option and open a new one, in a later expiration, at the same or a different strike. Brokers let you enter it as one ticket for a net credit or debit, which is convenient and is also the source of the confusion. The net number hides the fact that you are realising the loss on the first leg, today, in full. Rolling never makes a loss disappear; it moves the intrinsic value from an old contract into a new one and adds new time value on top.

Break the 5.28 mark into its parts. Intrinsic value: 95 - 91 = 4.00. Time value: 5.28 - 4.00 = 1.28. A December 95 put (63 days) at 34% IV is worth 7.06: intrinsic 4.00, time value 3.06. The roll to December at the same strike pays you 7.06 - 5.28 = 1.78 net, and 1.78 is exactly 3.06 - 1.28, the difference in time value. The 4.00 of intrinsic was bought back and sold again. It is still there, still against you, and will still be there at 91 on December 18.

## Rolling for a credit, and what it costs

Same strike, out in time, for a credit, is the roll that feels free. It is not.

You now hold a short December 95 put with XYZ at 91: delta -0.57, so the position moves 57 cents per dollar of stock, versus 27 cents when you opened. Total credits collected are 1.69 + 1.78 = 3.47; break-even 95 - 3.47 = 91.53; the stock has to hold 91.53 by December 18 for you to break even, and you have 63 more days of exposure to a stock that just fell 9% while its volatility rose. Roll again to January 15 (91 days) if it falls further and the arithmetic repeats: the January 95 put at 34% is 7.91, so a second roll from the December put would collect 0.85 more (7.91 - 7.06), for a total of 4.32 against a strike now perhaps 8 points in the money. Each roll collects a shrinking credit for an extended stay in a position with a growing delta.

The realistic alternative is to take the loss at 5.28 and open whatever trade the chain currently justifies. If that trade is the December 95 put, roll. If it is not, do not.

## Rolling down and out

The second roll moves the strike as well as the date. Buy back the November 95 at 5.28; sell the December 90 put at 4.31 (34% IV, 63 days, delta -0.42). Net debit 0.97. Total credits 1.69 - 0.97 = 0.72; break-even 90 - 0.72 = 89.28. You have paid 0.97 to lower the strike by 5.00, which is the cost of taking 4.00 of intrinsic value off the table (you were 4 in the money at 95 and are 1 out of the money at 90) less the extra time value.

Compare the two Decembers side by side with XYZ at 91. Same strike: break-even 91.53, delta -0.57, in the money. Down 5: break-even 89.28, delta -0.42, out of the money. The down-and-out roll is a materially different position, closer to the trade you originally meant to have, and it costs 0.97 today. Go further, to the January 90 put at 5.19 (net debit 0.09, break-even 89.91), and you have bought the strike reduction almost entirely with time. Or to the January 92 put at 6.20 (net credit 0.92, break-even 92 - 2.61 = 89.39): a small credit, a strike 3 lower, and 91 days of exposure. There is no roll that improves the break-even for free; the break-even only improves in exchange for time, strike, or cash.

## When rolling is denial

Apply one test to every roll: is the leg you are opening a trade you would place fresh, today, at this price, on this chain? Would you, on October 16 with XYZ at 91 and IV at 34%, sell a December 95 put at 7.06 as a new position? It is 4 points in the money with a 57 delta. Almost nobody would, and if you would not, the same-strike roll is a way of not booking a $359 loss. Would you sell the December 90 put at 4.31? Possibly; it is at the money on a stock that has just fallen, with IV elevated, which is a defensible premium sale, and if you would, the down-and-out roll is a real decision that happens to also close a loser.

Three further signs of denial. Rolling a defined-risk trade: the condor's maximum loss is $396 and the capital is already posted; rolling it adds new risk to recover a bounded, budgeted loss, and the usual rule is instead to close at a fixed multiple of the credit (two times is common) and re-enter only if the fresh trade passes Lesson 8's gate. Rolling to keep a call from being assigned on shares you agreed to sell: you are paying a debit to un-sell stock at a price you chose. Rolling more than once on the same underlying: the second roll is evidence the first was wrong.

The cash-secured put on a stock you want to own is the one case where rolling is nearly always sound, because the alternative, assignment at 93.31, was the plan. Rolling there is a choice between owning the shares now and being paid to wait; either is fine and the arithmetic above tells you the price of waiting.

## Worked example

October 16, 2026. XYZ 91.00, IV 34%. Short November 95 put, sold September 22 at 1.69. Per share.

Current mark: 5.28. Intrinsic 95 - 91 = 4.00; time value 1.28. Unrealised: 1.69 - 5.28 = -3.59 ($359).

Roll A, same strike out: buy November 95 at 5.28, sell December 18 95 put at 7.06 (intrinsic 4.00, time 3.06). Net credit 7.06 - 5.28 = +1.78. Total credits 1.69 + 1.78 = 3.47. Break-even 95 - 3.47 = 91.53. New delta -0.57. Days added: 63.

Roll B, down and out: buy November 95 at 5.28, sell December 90 put at 4.31. Net 4.31 - 5.28 = -0.97 debit. Total credits 1.69 - 0.97 = 0.72. Break-even 90 - 0.72 = 89.28. New delta -0.42. Days added: 63.

Roll C, down and further out: sell January 15 90 put at 5.19. Net 5.19 - 5.28 = -0.09. Total credits 1.60. Break-even 88.40. Delta -0.42. Days added: 91.

Roll D, down 3 and further out: sell January 92 put at 6.20. Net +0.92. Total credits 2.61. Break-even 89.39. Delta -0.47. Days added: 91.

Close and take assignment equivalent: buy November 95 at 5.28, buy 100 shares at 91.00. Realised -$359; shares at 91.00 with no short call. Or hold to November 6 and be assigned at 95, basis 93.31.

Denial test on Roll A: a fresh short December 95 put at 7.06 with XYZ 91, 4.00 in the money, delta -0.57. Not a trade you would open. Roll A fails.
Denial test on Roll B: a fresh short December 90 put at 4.31, at the money, IV 34%, delta -0.42. Defensible if XYZ still passes the ownership test at 90 - 4.31 = 85.69. Roll B is a decision.

## Table

Roll candidates on October 16 with XYZ 91.00 and IV 34%, per share. "Total credits" includes the original 1.69; break-even is strike minus total credits.

| Action | Close Nov 95 at | Open | Open price | Net | Total credits | Break-even | New delta | Days added |
|---|---|---|---|---|---|---|---|---|
| Hold to expiry | -- | -- | -- | 0.00 | 1.69 | 93.31 | -0.57 | 0 |
| Close only | 5.28 | -- | -- | -5.28 | realised -3.59 | -- | 0 | 0 |
| A: same strike, Dec | 5.28 | Dec 95 put | 7.06 | +1.78 | 3.47 | 91.53 | -0.57 | 63 |
| B: down 5, Dec | 5.28 | Dec 90 put | 4.31 | -0.97 | 0.72 | 89.28 | -0.42 | 63 |
| C: down 5, Jan | 5.28 | Jan 90 put | 5.19 | -0.09 | 1.60 | 88.40 | -0.42 | 91 |
| D: down 3, Jan | 5.28 | Jan 92 put | 6.20 | +0.92 | 2.61 | 89.39 | -0.47 | 91 |

## Sources

- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*, closing transactions and assignment: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- Cboe Global Markets, Options Institute, rolling and adjustment reference: https://www.cboe.com/education/
- FINRA Rule 4210, Margin Requirements (requirement changes as a short put moves in the money): https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210

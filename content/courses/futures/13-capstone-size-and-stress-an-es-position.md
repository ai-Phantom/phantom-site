---
{
  "title": "Capstone: Size and Stress an ES/MES Position for a $25,000 Account",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "With CME initial margin at $27,526 for ES and $2,753 for MES, what is the largest ES position a $25,000 account may hold overnight?", "opts": ["1 ES", "2 ES", "0 ES", "It depends on the day-trading margin"], "correct": 2, "explain": "Initial margin for one ES exceeds the account. Day-trading margin is intraday only and does not permit holding past the close."},
    {"q": "Four MES bought at 7,772.50 in a $25,000 account; maintenance $2,502 each. At what price does equity first fall below maintenance?", "opts": ["7,772.50 - 150.00 = 7,622.50", "7,772.50 - 749.60 = 7,022.90", "7,772.50 - 61.05 = 7,711.45", "7,772.50 - 388.63 = 7,383.87"], "correct": 1, "explain": "Maintenance on four MES is $10,008; cushion $25,000 - $10,008 = $14,992; at $20 per point that is 749.6 points, a 9.6% decline. Whether you would want to be there is a different question, answered by the loss limit."},
    {"q": "The 5% adverse open on four MES costs:", "opts": ["$1,943.13", "$3,886.25", "$7,772.50", "$19,431.25"], "correct": 2, "explain": "388.625 points x $20 per point = $7,772.50, 31.1% of the account, before any stop can act."},
    {"q": "Rolling four MES from Dec 2026 to Mar 2027 via the calendar spread at a fair 61.05 points with $2.50 commission per side: what is the friction (not the carry)?", "opts": ["$5.00", "$20.00 commission plus $1.00 spread tick = $21.00", "$1,221.00", "$3,052.50"], "correct": 1, "explain": "Four contracts x two sides x $2.50 = $20.00 commission, plus one 0.05-point spread tick on four MES: 0.05 x $5 x 4 = $1.00; total $21.00. The carry of 61.05 x $20 = $1,221 is separate and is returned through convergence."},
    {"q": "Which single change most reduces the capstone account's overnight risk without changing the trade idea?", "opts": ["Switching from MES to ES", "Widening the stop", "Cutting the contract count so a 2% adverse open costs no more than the daily loss limit", "Adding a stop-limit"], "correct": 2, "explain": "The adverse-open loss is contracts x points x $5 and no order can reduce it; only size can. Setting size so that 155.45 x $5 x n is at most the overnight limit is the rule the capstone asks you to derive."}
  ],
  "task": "Submit the completed worksheet with every calculation shown, then repeat it using the live CME margin figures and the current ESZ26 settlement on the day you submit."
}
---

## The brief

You manage a $25,000 futures account. You want long S&P 500 exposure held for about four months, through the December 2026 expiry into the March 2027 contract. Using only the E-mini S&P 500 (ES) and the Micro E-mini S&P 500 (MES), you will size the position, stress it against two adverse opens, find the margin call point, and price the roll across the quarterly expiry. Every number must be shown with its arithmetic and its source. The rubric at the end is how the worksheet is graded.

## Inputs you must use

Fixed for this exercise so that answers are comparable. On the day you submit you will repeat the exercise with live values (see the task).

- Reference price: ESZ26 close 7,772.50 on 2026-09-23 (Yahoo Finance daily bar, ESZ26.CME).
- Multipliers: ES $50 per index point, MES $5 per index point; tick 0.25 (CME contract specifications).
- CME margin table for the December 2026 contracts, figures republished 2026-08-18 from the CME margins pages:

| Contract | Initial margin | Maintenance margin | Initial / maintenance |
|---|---|---|---|
| ES (ESZ26) | $27,526 | $25,024 | 1.10 |
| MES (MESZ26) | $2,753 | $2,502 | 1.10 |

- Adverse opens: 2% (155.45 points) and 5% (388.625 points) below 7,772.50, occurring at the 6:00 p.m. ET reopen before any resting order can execute.
- Roll: December expires Friday 2026-12-18 at 9:30 a.m. ET; March expires 2027-03-19; 91 days apart. Fair calendar spread 61.05 points (Lesson 5: 7,772.50 x (0.0414 - 0.0099) x 91/365, rounded to the 0.05 tick). Commission assumed $2.50 per contract per side.
- Risk policy: 2% of equity ($500) of stop-defined risk for a position held for months, daily loss limit 2% ($500), and an overnight rule that no position may lose more than 5% of equity ($1,250) on a 2% adverse open.

## Part 1: what the exchange permits

State the maximum number of ES and of MES the account may hold overnight under the initial margin. Show the division and the rounding. State how much free equity remains at the maximum MES count and how many index points against you that free equity represents.

## Part 2: what the risk policy permits

Choose a stop distance in points for a position held for four months through the daily marks; justify it in one sentence with reference to the year's worst daily moves from Lesson 3 (-184.00 points on 2025-10-10, -200.50 on 2026-06-05) and worst opening gap (-84.63 on 2026-03-23). Then compute the contract count from contracts = $500 / (stop points x $ per point) for ES and for MES, rounding down.

Apply the overnight rule: the largest n such that 155.45 x $5 x n is at most $1,250. Show the inequality. Your position size is the smallest of the three constraints (margin, per-trade risk, overnight rule). State it, and state which constraint bound.

## Part 3: the adverse-open stress

For your chosen position, and separately for one ES (for comparison), compute the dollar loss and the percentage of the $25,000 account on the 2% and the 5% adverse opens. Then compute, for each, the account equity after the open and whether it is above or below the maintenance requirement for the position. Present the four results in a table with the arithmetic beneath it.

## Part 4: the margin call point

For your chosen position: compute total maintenance margin, the cushion of equity above it, and the number of index points of decline that consumes the cushion. Convert to a price and to a percentage decline from 7,772.50. Then compute the margin call amount if the settlement lands exactly 20 points beyond that price (the call restores initial, not maintenance). Repeat the calculation for one ES as if the account could hold it, and comment in two sentences on why the ES margin call point is undefined for this account.

## Part 5: the roll across the December expiry

You roll on Thursday 2026-12-10 by selling the ESZ26-ESH27 (or MESZ26-MESH27) calendar spread at 61.05 points. Compute:

1. The carry component in dollars: 61.05 x $ per point x contracts.
2. The friction: commissions on every contract-side, plus one spread tick (0.05 points x $ per point x contracts).
3. The financing check from Lesson 6: interest earned on the notional at 4.14% for 91/365 of a year, minus dividends forgone at 0.99%, minus the carry paid; show that it nets to approximately zero and say in one sentence what that means about the roll being a "cost."
4. The mistiming penalty if instead you legged out with two market orders on expiry morning and lost one outright tick per leg.

State the total out-of-pocket friction for holding the position through one roll, and the annualised friction for four rolls.

## Part 6: the plan rows

Fill the six rows of the Lesson 12 plan table that this exercise determined: products, exchange margin (with date), overnight capacity, risk per trade, daily loss limit, roll date and broker liquidation date (look up your broker's).

## Worked example

To calibrate your answers, here is Part 1 and the first line of Part 3 done for you; the rest is yours.

Part 1. ES: $25,000 / $27,526 = 0.908, rounds down to 0 contracts; the account cannot hold ES overnight. MES: $25,000 / $2,753 = 9.08, rounds down to 9; initial on 9 MES = 9 x $2,753 = $24,777; free equity = $25,000 - $24,777 = $223; at $45 per point for 9 MES that is $223 / $45 = 4.96 index points of decline before the account is under initial. Maintenance on 9 MES = 9 x $2,502 = $22,518; cushion above maintenance = $2,482 = 55.2 points.

Part 3, first line, for one ES as the comparison case. 2% adverse open: 155.45 x $50 = $7,772.50, 31.1% of the account; equity after = $17,227.50, below the $25,024 maintenance by $7,796.50, and below initial by $10,298.50, so an immediate call of $10,298.50 would be issued, which is 41% of the original account, on a position the account was never permitted to hold overnight in the first place. 5% adverse open: 388.625 x $50 = $19,431.25, 77.7%; equity after = $5,568.75.

Every other line follows the same pattern. Show the multiplication, the subtraction, and the comparison to the requirement, in that order.

## Table

| Part | Deliverable | Must show |
|---|---|---|
| 1 | Max ES and MES overnight; free equity at max MES in $ and points | Division, rounding, $223, 4.96 pts |
| 2 | Stop distance with justification; contracts by risk for ES and MES; overnight-rule n; chosen size and binding constraint | Three inequalities, one chosen n |
| 3 | 2% and 5% loss and % for chosen size and for 1 ES; equity after; above/below maintenance | Four rows of arithmetic |
| 4 | Maintenance, cushion, points, price, % decline; call amount 20 pts beyond | Restore-to-initial calculation |
| 5 | Carry $, friction $, financing check, mistiming penalty, annual friction | Netting to about zero |
| 6 | Six plan rows with dates | Dated margin figures, broker's liquidation date |

## Rubric

| Criterion | Points | What earns full marks |
|---|---|---|
| Margin capacity (Part 1) | 15 | Correct ES (0) and MES (9) counts with the division shown; free equity $223 and 4.96 points; maintenance cushion 55.2 points |
| Sizing and binding constraint (Part 2) | 20 | Stop justified against the year's real moves; three constraints computed; the overnight rule (n at most 1) or the risk rule identified as binding, with the resulting choice defended, including the option of no overnight position if the chosen stop cannot fit one MES |
| Adverse-open stress (Part 3) | 20 | 2% and 5% losses correct to the cent for both positions; equity after each; correct comparison to maintenance; percentages of the account |
| Margin call point (Part 4) | 15 | Cushion, points, price and percentage correct; call amount computed to initial, not maintenance; ES case explained as undefined for this account |
| Roll cost (Part 5) | 20 | Carry and friction separated; financing check nets to about zero with the three components; mistiming penalty; annualised friction |
| Plan rows and sourcing (Part 6, throughout) | 10 | Every figure carries its source and date; the live repeat is submitted with the CME page URLs and the settlement date |

Total 100. A worksheet that reaches the right size by the wrong arithmetic scores the sizing criterion at zero; the arithmetic is the deliverable.

## Sources

- CME Group, E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.margins.html
- CME Group, Micro E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.margins.html
- CME Group, E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- U.S. Department of the Treasury, Daily Treasury Bill Rates — https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates&field_tdr_date_value_month=202609

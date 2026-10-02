---
{
  "title": "Margin Is a Performance Bond, Not a Down Payment",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "With ESZ26 at 7,772.50 and an initial margin of $27,526, what leverage does one ES contract carry?", "opts": ["About 2x", "About 7x", "About 14x", "About 50x"], "correct": 2, "explain": "Notional $388,625 / initial margin $27,526 = 14.1x. Equivalently, margin is 7.1% of notional."},
    {"q": "What does futures margin represent?", "opts": ["A partial payment toward owning the underlying", "A loan from the broker at interest", "A good-faith deposit guaranteeing you can meet daily settlement losses", "A fee paid to the exchange"], "correct": 2, "explain": "Futures margin is a performance bond. You are not buying anything on credit; you are posting collateral against the daily cash flows of a contract you already fully own or owe."},
    {"q": "Initial margin is $27,526 and maintenance margin is $25,024. When must you add funds?", "opts": ["As soon as equity falls below $27,526", "Only when equity falls below $25,024", "Only at expiration", "Never; the broker liquidates instead"], "correct": 1, "explain": "The maintenance level is the trigger. Falling below initial is fine; falling below maintenance produces a margin call, and the call is to restore the initial level."},
    {"q": "Which of these is NOT an input to CME's SPAN calculation of the performance bond?", "opts": ["Price scan range", "Volatility scan range", "Your broker's commission schedule", "Inter-month spread charge"], "correct": 2, "explain": "SPAN measures the worst plausible one-day loss of a portfolio across price and volatility scenarios and adds spread charges. Commissions are outside it."},
    {"q": "A 2% adverse move in ES costs $7,772.50 per contract. As a share of the $27,526 initial margin that is:", "opts": ["About 2%", "About 14%", "About 28%", "About 50%"], "correct": 2, "explain": "$7,772.50 / $27,526 = 0.282, or 28.2%. The move that is 2% of notional is 28% of the collateral you posted; that ratio is the leverage."}
  ],
  "task": "Log in to your futures broker, find the current initial and maintenance margin it charges for ES and MES, and write them next to the CME figures from this lesson with the date you looked."
}
---

## The word "margin" means something different here

In a stock account, margin is a loan. You put up half, the broker lends the rest, you pay interest, and you own the shares. In a futures account the word describes something else entirely. CME calls it a **performance bond**, and the CFTC glossary defines margin as money or collateral deposited "by a customer with his broker, by a broker with a clearing member, or by a clearing member with a clearing organization, also called Performance Bond."

The distinction matters because a futures contract has no purchase price. When you buy one ES you do not pay $388,625 and you do not borrow it either. You have taken on an obligation whose value starts at zero and then moves with the index. The performance bond is the deposit that guarantees you can pay the losses as they arrive each day. No interest is charged on it because nothing has been lent. Most brokers pay nothing on it either, and some allow T-bills to be posted instead of cash.

The consequence is that the bond is small relative to the exposure. That is leverage, and it is the whole reason retail traders are drawn to futures and the whole reason the CFTC warns that they "can be required to pay more than they invested initially."

## Initial and maintenance

Two numbers govern the bond. **Initial margin** is the amount you must have in the account to open a position and the level to which you must restore it after a margin call. **Maintenance margin** is the lower level below which your account equity may not fall while the position is open. CME sets the maintenance requirement per contract and, for speculative (non-hedge) accounts, sets initial at 110% of maintenance.

CME's published figure for the December 2026 ES contract, as republished with a 2026-08-18 date because the CME margins page could not be fetched at the time of writing, was $25,024 maintenance and $27,526 initial. The ratio is $27,526 / $25,024 = 1.100, which is the 110% rule exactly. Micro contracts are set at one-tenth: about $2,502 maintenance and $2,753 initial for MES.

These figures change, sometimes weekly. CME's clearing house issues a "Performance Bond Requirements" advisory whenever it revises them; nine such notices covering various product groups were issued between January and September 2026, including one for equity products effective 2026-08-14. Volatility rises, margins rise, and they rise after the move that caused them, not before. Your broker may require more than CME's minimum and never less for overnight positions. Intraday, many brokers offer a reduced "day-trading margin" that can be a small fraction of the exchange figure; that is a broker credit decision and can be withdrawn at any time, and it does not reduce your risk by one cent.

## How CME sets the number: SPAN

CME computes performance bonds with SPAN (Standard Portfolio Analysis of Risk), now being succeeded by SPAN 2 for equity and energy products. The method is not a percentage of notional. It estimates the largest loss a portfolio would plausibly suffer over one day by revaluing it across a grid of scenarios: the price moved up or down by fractions of a **price scan range**, combined with implied volatility moved by a **volatility scan range**, plus extreme-move scenarios weighted at a fraction of their loss. The worst of those sixteen scenario losses is the scan risk. SPAN then adds an **inter-month spread charge** for calendar spreads, subtracts **inter-commodity spread credits** for offsetting positions in related products (long ES, short NQ, for example), and applies a **short option minimum**.

For a single outright ES contract the result is close to the price scan range times the multiplier. Working backwards from $25,024 / $50 = 500.5 index points, or 6.4% of 7,772.50, CME was treating a move of roughly 500 points as the one-day loss it needs covered. That is your first clue about what the exchange thinks the tail looks like.

## The arithmetic of leverage

Leverage is notional divided by the bond. Two equivalent ways to state it:

- Leverage = notional / initial margin
- Margin as a percentage of notional = initial margin / notional

The second is the more useful because it converts directly into the percentage move that consumes your collateral. If margin is 7% of notional, a 7% adverse move wipes out the entire bond, and a 2% move consumes 2/7 of it, about 28%. Neither figure depends on your account size; they are properties of the contract. What your account size determines is how many such moves you can absorb before the broker acts, which is Lesson 4.

The point most new traders miss is that the exchange's margin is calibrated to a one-day move, not to how much you can afford to lose. It is the clearinghouse protecting itself, not you. Your own risk limit (Lesson 11) must be far smaller than the margin.

## Worked example

All figures dated. ESZ26 closed at 7,772.50 on 2026-09-23 (Yahoo Finance). The CME multiplier is $50 per index point (CME spec page). CME's initial margin for ESZ26 was $27,526 and maintenance $25,024 (CME margins page, figure republished 2026-08-18).

Step 1, notional:

7,772.50 x $50 = $388,625.00

Step 2, leverage:

$388,625.00 / $27,526 = 14.12x

Step 3, margin as a share of notional:

$27,526 / $388,625.00 = 0.0708 = 7.08%

Step 4, the 2% adverse move:

2% of 7,772.50 = 155.45 index points
155.45 x $50 = $7,772.50 per contract
$7,772.50 / $27,526 = 28.2% of initial margin

Step 5, the 5% adverse move:

5% of 7,772.50 = 388.63 index points (388.625 rounded to the nearest tick is 388.50 or 388.75; use 388.625 for arithmetic)
388.625 x $50 = $19,431.25 per contract
$19,431.25 / $27,526 = 70.6% of initial margin

Step 6, the move that consumes the whole bond:

$27,526 / $50 = 550.52 index points = 7.08% of 7,772.50

Step 7, the same exercise on the micro. MES initial margin about $2,753 (one-tenth), notional $38,862.50, leverage $38,862.50 / $2,753 = 14.12x, identical. A 2% move costs $777.25 per MES, still 28.2% of its bond. The micro reduces dollars at risk by ten; it does not reduce leverage at all.

Compare these with what the market actually did over the year to 2026-09-24. The worst single daily close-to-close change in the ES=F continuous series was -2.71% on 2025-10-10 (6,779.25 to 6,595.25, a 184.00-point drop worth $9,200 per contract). The second worst was -2.64% on 2026-06-05 (7,601.00 to 7,400.50, 200.50 points, $10,025 per contract). Both exceed the "2% adverse open" scenario, and both consumed more than a third of the initial margin in one session.

![Bar chart of one ES contract at 7,772.50: notional value $388,625, initial margin $27,526, maintenance margin $25,024, and the $7,773 cost of a 2% adverse move. Price from Yahoo Finance ESZ26.CME close 2026-09-23; margin from the CME Group E-mini S&P 500 margins page as republished 2026-08-18.](figures/leverage-vs-margin.svg)

## Table

| Quantity | ES | MES | How computed |
|---|---|---|---|
| Close, 2026-09-23 | 7,772.50 | 7,772.50 | Yahoo Finance ESZ26 / MESZ26 |
| Multiplier | $50 | $5 | CME spec page |
| Notional | $388,625.00 | $38,862.50 | close x multiplier |
| Maintenance margin | $25,024 | $2,502 | CME margins page (2026-08-18 figure); micro = 1/10 |
| Initial margin | $27,526 | $2,753 | maintenance x 1.10 |
| Leverage | 14.1x | 14.1x | notional / initial |
| Margin as % of notional | 7.08% | 7.08% | initial / notional |
| 2% adverse move | -$7,772.50 (28.2% of initial) | -$777.25 (28.2%) | 0.02 x notional |
| 5% adverse move | -$19,431.25 (70.6%) | -$1,943.13 (70.6%) | 0.05 x notional |
| Move that exhausts initial | 550.5 pts (7.08%) | 550.5 pts (7.08%) | initial / multiplier |

## Sources

- CME Group, E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.margins.html
- CME Group, Performance Bonds/Margins FAQ — https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/faq-performance-bonds-margins.html
- CME Group, SPAN methodology overview — https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/span-methodology-overview.html
- CFTC Glossary, "Margin" — https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_m.html

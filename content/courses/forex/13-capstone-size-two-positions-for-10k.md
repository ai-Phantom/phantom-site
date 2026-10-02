---
{
  "title": "Capstone: Size a EUR/USD and a USD/JPY Position for a $10,000 Account",
  "duration": "25 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "For the EUR/USD leg (entry 1.1411, stop 40 pips, risk $100), what position size does the formula give?", "opts": ["0.10 lots", "0.25 lots", "0.40 lots", "1.00 lot"], "correct": 1, "explain": "$100 / 40 pips = $2.50 per pip; $2.50 / $10 per pip per lot = 0.25 lots."},
    {"q": "For the USD/JPY leg (entry 157.92, stop 80 pips, risk $100), what is the pip value of one standard lot in dollars?", "opts": ["$10.00", "$6.33", "$1.58", "$0.63"], "correct": 1, "explain": "0.01 × 100,000 = 1,000 yen; 1,000 / 157.92 = $6.33."},
    {"q": "What is the 30-day swap on 0.25 lots of long EUR/USD at −2.36% per year, on a notional of $28,527.50?", "opts": ["+$55.34", "−$55.34", "−$673", "−$5.53"], "correct": 1, "explain": "$28,527.50 × 0.0236 × 30/365 = $55.34, debited because long EUR/USD pays the differential."},
    {"q": "A submission uses 5% margin for EUR/USD 'because that is what my broker charges'. How should it be graded?", "opts": ["Wrong; only 2% is acceptable", "Correct if the broker's published margin table is cited with a date; the rubric requires the actual requirement, with the CFTC minimum noted", "Wrong; margin is not part of the capstone", "Correct without any citation"], "correct": 1, "explain": "Brokers may require more than the CFTC minimum. The rubric asks for the real requirement, sourced, alongside the regulatory floor."},
    {"q": "Why does the rubric require the P&L under a 100-pip move to include the swap over the hold?", "opts": ["It does not", "Because the position's result after 30 days is the spot P&L plus the accumulated financing, and omitting the swap misstates the outcome by 20% or more of the risk budget on the EUR/USD leg", "Because swap is larger than spot P&L", "To make the arithmetic harder"], "correct": 1, "explain": "On the EUR/USD leg the 30-day swap is $55.34 against a $250 spot move: 22% of it. Lesson 7 exists for this reason."}
  ],
  "task": "Submit the two-position worksheet with every input sourced and dated, every formula shown, and a one-paragraph note on which of the two positions you would actually take and why."
}
---

## The exercise

You have a $10,000 US-dollar account at a US retail forex dealer. Size, margin, finance and stress-test two positions using the procedure from lessons 2, 4, 7 and 11. Every input must come from a published source with a date; every calculation must be shown. This page states the inputs to use for the reference solution, works one leg in full, gives the answer key for both, and shows the rubric.

You may substitute your own broker's current rates, spreads, margins and swaps, in which case you must cite the page and the date, and your numbers will differ from the key; the grader checks the method and the sourcing, then the arithmetic.

## Inputs for the reference solution

- Account: $10,000 USD. Risk per position R = 1% = $100.
- Rates: ECB euro foreign exchange reference rates, 2026-09-23 fix. EUR/USD 1.1411. USD/JPY derived as EUR/JPY 180.20 ÷ EUR/USD 1.1411 = 157.92.
- Stops: EUR/USD 40 pips; USD/JPY 80 pips. Both positions long.
- Spreads and margins: tastyfx forex product details, read 2026-09-24. EUR/USD minimum spread 0.8 pips, margin 2%. USD/JPY minimum spread 0.8 pips, margin 5%. Regulatory floor: CFTC Regulation 5.9, 2% for major currencies.
- Swaps: OANDA TMS Brokers S.A. swap points table valid 2026-09-21 to 2026-09-27, in per cent per year. EUR/USD long −2.36%. USD/JPY long +1.81%.
- Hold: 30 calendar days. Ignore the Wednesday triple-swap convention and compounding; use 30/365 of the annual rate.
- Stress: spot moves 100 pips in your favour and 100 pips against, at the end of the 30 days.
- Broker step: 0.01 lots, round down.

## Worked example

The USD/JPY leg, in full. Repeat the same steps for EUR/USD.

**Step 1: pip value per lot.** Pip size 0.01 × contract 100,000 = ¥1,000 per pip per lot. In dollars at 157.92: 1,000 ÷ 157.92 = **$6.332** per pip per lot.

**Step 2: size.** Dollars per pip affordable = R ÷ stop = $100 ÷ 80 = $1.25. Lots = 1.25 ÷ 6.332 = 0.1974; round down to **0.19 lots** (19,000 dollars of notional). Position pip value = 0.19 × 6.332 = **$1.203** per pip. Risk at stop = 80 × 1.203 = **$96.25**, which is 0.96% of equity, inside the budget.

**Step 3: notional and margin.** Notional = 0.19 × 100,000 = **$19,000** (the base currency is the dollar, so no conversion). Margin at the broker's published 5% = **$950**, 9.5% of equity. At the CFTC 2% floor it would be $380; the broker's table governs. Leverage used = 19,000 ÷ 10,000 = 1.9:1.

**Step 4: swap over 30 days.** $19,000 × 0.0181 × 30 ÷ 365 = **+$28.27**, a credit, because the position is long the higher-rate currency. Per day: $0.94. In pips: 28.27 ÷ 1.203 = 23.5 pips over the month.

**Step 5: spread.** 0.8 pips × $1.203 = **$0.96** round trip.

**Step 6: P&L under the stress moves, after 30 days.**
- +100 pips (USD/JPY to 158.92): spot P&L = 100 × 1.203 = +$120.31. Plus swap +$28.27, minus spread $0.96. Net **+$147.62**, 1.48% of equity.
- −100 pips (to 156.92): the stop at 80 pips would have been hit first at −$96.25. If, for the exercise, the position is held to −100 pips: spot −$120.31 + $28.27 − $0.96 = **−$93.00**, 0.93% of equity. Note that the swap credit covered 23.5 of the 100 adverse pips.

**Step 7: the check line.** Lots × pip value × stop ≤ R: 0.19 × 6.332 × 80 = 96.25 ≤ 100. Margin ≤ 20% of equity: 9.5%. Both pass.

## Answer key

| Item | EUR/USD long | USD/JPY long |
| --- | --- | --- |
| Entry (ECB fix 2026-09-23) | 1.1411 | 157.92 |
| Stop | 40 pips | 80 pips |
| Pip value, 1 lot | $10.00 | $6.332 |
| Lots (rounded down) | 0.25 | 0.19 |
| Position pip value | $2.50 | $1.203 |
| Risk at stop | $100.00 | $96.25 |
| Notional | 25,000 × 1.1411 = $28,527.50 | $19,000 |
| Margin (broker table) | 2% = $570.55 | 5% = $950.00 |
| Margin (CFTC floor) | 2% = $570.55 | 2% = $380.00 |
| Swap, 30 days | $28,527.50 × −0.0236 × 30/365 = −$55.34 | $19,000 × 0.0181 × 30/365 = +$28.27 |
| Swap in pips | −22.1 pips | +23.5 pips |
| Spread | 0.8 × $2.50 = $2.00 | 0.8 × $1.203 = $0.96 |
| +100 pips, net of swap and spread | +$250.00 − $55.34 − $2.00 = +$192.66 | +$120.31 + $28.27 − $0.96 = +$147.62 |
| −100 pips, net (held past stop) | −$250.00 − $55.34 − $2.00 = −$307.34 | −$120.31 + $28.27 − $0.96 = −$93.00 |
| Both open: risk at stops | $196.25 (1.96% of equity) | |
| Both open: margin in use | $1,520.55 (15.2% of equity) | |
| Combined one-sigma risk (ρ = −0.58, lesson 8) | √(100² + 96.25² + 2 × −0.58 × 100 × 96.25) ≈ $90 | |

The asymmetry is the lesson. The two positions are the same size in risk terms, but over 30 days the euro leg pays $55 to exist and the yen leg is paid $28. On the euro leg the 100-pip favourable case is cut by 23% by financing and the adverse case is worsened by 22%; on the yen leg the credit cushions the adverse case by a quarter. A trader who sized both legs identically "by pips" would have missed that one of them needs a materially better win rate to break even, which lesson 11 computed at 60.2% versus 45.6% for a ten-day hold at 1:1.

## Extension (optional, not graded)

Repeat the key for both positions short. EUR/USD short receives +0.40%, USD/JPY short pays −3.71% per year. Compute the 30-day swap for each and the net P&L under the same ±100-pip moves. Then state which of the four positions has the best net result under an adverse 100-pip move, and why that is not the same as the best trade.

## Rubric

Scored out of 100. A submission below 70 is returned with the failing criteria marked; resubmit after fixing them. Where the submission uses its own broker's inputs, the grader recomputes the key from those inputs.

| Criterion | Points | Full marks require | Zero marks if |
| --- | --- | --- | --- |
| Inputs sourced and dated | 20 | Rates, spreads, margins and swaps each carry the publisher, page and date; the CFTC floor is cited alongside the broker's margin | Any input without a source, or a rate with no date |
| Pip value and position size | 25 | Pip value per lot derived for both pairs with the conversion shown for USD/JPY; lots computed from R and the stop and rounded down; the check line shown | Size derived from margin or leverage rather than the stop; rounding up; pip value asserted rather than derived |
| Margin and leverage | 15 | Notional, margin at the broker's rate, margin at the regulatory floor, and margin in use as a share of equity for the combined book | Margin computed on the wrong notional or omitted for either leg |
| Swap over the hold | 20 | Sign correct for both legs, 30/365 of the annual rate on the correct notional, expressed in dollars and pips | Wrong sign, wrong notional, or swap omitted |
| P&L under ±100 pips | 20 | Both scenarios for both legs, net of swap and spread, with the stop's earlier trigger noted on the adverse case, and one paragraph on what the asymmetry means | Spot-only P&L, or scenarios for one leg only |

## Sources

- European Central Bank, euro foreign exchange reference rates, 2026-09-23: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
- tastyfx, forex product details (spreads, margins, contract size): https://www.tastyfx.com/help-and-support/product-details/what-are-tastyfxs-forex-product-details/
- OANDA TMS Brokers S.A., swap points table valid 2026-09-21 to 2026-09-27: https://www.oanda.com/eu-en/document/91
- Commodity Futures Trading Commission, 17 CFR 5.9, security deposits for retail forex transactions: https://www.ecfr.gov/current/title-17/chapter-I/part-5/section-5.9

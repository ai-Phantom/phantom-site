---
{
  "title": "Building an FX Plan and a Trade Journal",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which item must be written in the plan before the first trade, according to this lesson?", "opts": ["A price target for the year", "The vendor and cut time of the daily bar you will use, so that every later measurement is comparable", "A list of indicators", "The broker's marketing claims"], "correct": 1, "explain": "Lesson 10 showed that the same day looks different on different cuts. A plan that does not name its data cannot be tested against its own journal."},
    {"q": "What does the journal record for the correlation assumption?", "opts": ["Nothing; correlation is not recorded", "The correlation you assumed between open positions when you sized the book, so it can be compared with the realised correlation later", "Only the correlation with the S&P 500", "The broker's correlation matrix"], "correct": 1, "explain": "Lesson 8's worked example: a book that assumed independence and got 0.88 was running a third more risk than planned. The journal makes that visible."},
    {"q": "Why does the journal record the spread at entry and the swap actually charged, rather than the broker's published minimums?", "opts": ["Because published minimums are illegal", "Because published minimums are the best case; the realised cost is what the strategy paid, and only realised cost can be compared with the strategy's average win", "Because swaps are always zero", "Because the spread does not matter"], "correct": 1, "explain": "Lesson 3 and lesson 7 priced costs from published tables; the journal measures whether those tables described your fills."},
    {"q": "The plan in the worked example caps total open risk at 2% of equity. With two positions each risking 1% and a correlation of +0.88 between them, what does the plan require?", "opts": ["Nothing; each is within 1%", "Reduce one or both, because the combined one-sigma risk is $194 on a $10,000 account and the plan's cap is on combined risk, not on the sum of labels", "Add a third position", "Close the account"], "correct": 1, "explain": "The cap is meaningful only if it is applied to the combined risk; two near-identical positions are one position at double size."},
    {"q": "What is the purpose of the 'what would prove me wrong' line in the plan?", "opts": ["Decoration", "To name, before entry, the price or event that invalidates the thesis, so that the stop is a decision made in advance rather than a reaction", "To satisfy the broker", "To pick a target"], "correct": 1, "explain": "A stop that is set after the position moves against you is set by the loss, not by the thesis."}
  ],
  "task": "Write your plan using the template in this lesson, fill in every numeric field from your own broker's published tables with the date you read them, and journal your next ten trades in the format shown before attempting the capstone."
}
---

## A plan is a set of numbers with dates

Everything in this course reduces to numbers you can look up and numbers you can compute from them. A trading plan is the document that lists both, with the date and source of each, so that the person reading it in six months, who is you, can see what you knew and check whether it was still true. A journal is the same document filled in per trade, plus the outcome.

This lesson gives the template, fills it in with the numbers from the earlier lessons, and explains what each field is for. The capstone in lesson 13 is graded on the same fields.

## The plan template

**1. Account and data.** Account currency and size. Broker, regulator, and the counterparty sentence from the customer agreement (lesson 1). The broker's margin close-out level and whether the account has negative balance protection (lesson 4). The data vendor and the cut time of its daily bar (lesson 10). The date you read each.

**2. Instruments.** The pairs you will trade, with for each: pip value per lot in your account currency at the current rate; published minimum spread; margin requirement; long and short swap; median daily range over the last year; the session you will trade it in; its central bank and next decision date (lessons 2, 3, 5, 7, 9).

**3. Risk rules.** R as a percentage of equity. Maximum combined open risk, applied to correlated positions using the formula of lesson 8, not to the sum of labels. Maximum margin in use as a share of equity. The stop rule as a multiple of measured daily range. The event rule: which releases you will not hold a tight stop through.

**4. Setup.** The condition that triggers a trade, written so that another person could apply it. The thesis in one sentence. The line "what would prove me wrong", as a price or an event, which becomes the stop.

**5. Costs at the planned holding period.** Spread plus swap for the intended hold, as a share of R, and the resulting break-even win rate for the planned reward-to-risk (lesson 11).

**6. Review.** A fixed date to compare the journal against the plan: realised spread versus published, realised swap versus published, realised correlation versus assumed, realised win rate versus break-even.

## Worked example

Fill the template for the two trades of lesson 11, with sources and dates.

**Account:** $10,000 USD. US retail forex dealer; NFA's guide confirms the dealer is the counterparty (read 2026-09-24). Margin close-out assumed at 50% of required margin; no negative balance protection. Daily bars: Yahoo Finance chart API, whose daily bar closes before 14:00 ET (established 2026-09-24 from the 16-17 September EUR/USD gap).

**Instruments (rates: ECB fix 2026-09-23; spreads and margins: tastyfx product details, read 2026-09-24; swaps: OANDA TMS Brokers table valid 2026-09-21 to 2026-09-27; ranges: Yahoo daily bars, year to 2026-09-24).**

- EUR/USD 1.1411. Pip value $10 per lot. Min spread 0.8 pips. Margin 2%. Swap long −2.36%, short +0.40% per year. Median daily range 47.7 pips. Session: London-New York overlap. Central banks: ECB (next decision after 10 September 2026 per the ECB calendar) and FOMC (27-28 October 2026).
- USD/JPY 157.92. Pip value $6.33 per lot. Min spread 0.8 pips. Margin 5%. Swap long +1.81%, short −3.71%. Median daily range 76.5 pips. Session: Tokyo for BoJ days, otherwise London-New York overlap. Central banks: BoJ (next statement after 18 September 2026) and FOMC.

**Risk rules.** R = 1% = $100. Combined open risk ≤ 2% by the correlation formula. Margin in use ≤ 20% of equity. Stop ≥ 0.8 × median daily range for trades held under a day, ≥ 1.5 × for multi-day trades. No stop tighter than the event's median range through NFP, CPI, FOMC in either pair or BoJ in USD/JPY (lesson 9 medians: USD/JPY NFP 127.6, CPI 91.0, BoJ 177.8 pips).

**Setup A: long EUR/USD.** Trigger: daily close above the prior week's high, entered in the following London session. Thesis: ECB tightening (deposit rate to 2.50% on 16 September 2026) narrowing the differential against the dollar. Proof of being wrong: a daily close back below the prior week's low, expected 40 pips away at entry. Size: 0.25 lots. Hold: up to 10 days. Costs: spread $2.00 + swap −$18.44 = $20.44 = 20% of R; break-even win rate at 1:1 = 60.2%. That is a high hurdle; the plan notes that this setup needs at least a 1.5:1 reward to be worth taking, which lowers the break-even to 120.44 ÷ (120.44 + 129.56) = 48.2%.

**Setup B: long USD/JPY.** Trigger: a BoJ day's range fully reversed (as on 18 September 2026) with the close back at the open, entered the next session. Thesis: the market rejected a stronger yen despite the hike. Proof of being wrong: a close below the BoJ day's low, 80 pips away. Size: 0.19 lots. Hold: up to 10 days. Costs: spread $0.96 + swap +$9.42 = net −$8.46 (a credit); break-even at 1:1 = 45.6%.

**Book check.** Both long: combined one-sigma risk ≈ $90 at a correlation of −0.58; within the 2% cap. Margin in use $1,520.55 = 15.2%; within the 20% cap.

**Review date:** 2026-10-24, after the October FOMC.

## Table

The journal has one row per trade with these columns. Fill the first ten at entry and the rest at exit.

| Column | Filled at | What it is for |
| --- | --- | --- |
| Date, time (UTC) and session | Entry | Ties the trade to lesson 5's clock and lesson 9's calendar |
| Pair, direction, entry price | Entry | The trade |
| Stop in pips and as a multiple of median daily range | Entry | Lesson 10: is the stop outside the noise |
| Lots, pip value, dollar risk at stop, R% | Entry | Lesson 2 and 11: the sizing formula's output, checkable |
| Margin posted and margin in use as % of equity | Entry | Lesson 4: distance from close-out |
| Spread at entry (measured, in pips and dollars) | Entry | Lesson 3: realised cost versus the published minimum |
| Published swap and intended hold; expected swap in dollars | Entry | Lesson 7: carry priced in advance |
| Correlation assumed with other open positions; combined risk | Entry | Lesson 8: the book, not the trade |
| Next scheduled event in the pair before the intended exit | Entry | Lesson 9: known spike risk |
| Thesis and the "wrong if" line | Entry | The reason, and the exit that follows from it |
| Exit date, price, reason (stop, target, time, event, discretion) | Exit | Was the exit the planned one |
| Realised P&L in pips and dollars; realised swap; realised spread on exit | Exit | Cost accounting against the plan's estimate |
| Maximum adverse and favourable excursion in pips | Exit | Whether the stop and target were placed where the trade actually went |
| Notes: what the calendar did, what you did that was not in the plan | Exit | The only column that improves the plan |

## Running the review

At the review date, the plan's estimates are compared with the journal's realised columns. Four comparisons matter most. Realised spread against the published 0.8 pips: if your average is 1.4, your entries are in the wrong session or around events. Realised swap against the table: if the debit is larger than the table implied, the broker's markup or the Wednesday triple is costing more than planned. Realised correlation against assumed: compute it from the journal's daily P&L by pair; if two "different" setups moved together, they are one setup. Realised win rate against the break-even for the realised reward-to-risk: this is the only line that says whether there is an edge, and it needs dozens of trades before it says anything.

Nothing in the review asks whether the market was kind. It asks whether the numbers you wrote down were true and whether you followed them. That is what a plan is for.

## Sources

- National Futures Association, "Forex Transactions: A Regulatory Guide" (counterparty and disclosure requirements): https://www.nfa.futures.org/members/member-resources/files/forex-regulatory-guide.html
- Commodity Futures Trading Commission, Customer Advisory: "Eight Things You Should Know Before Trading Forex": https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- OANDA TMS Brokers S.A., swap points table valid 2026-09-21 to 2026-09-27: https://www.oanda.com/eu-en/document/91
- tastyfx, forex product details (spreads, margins, contract sizes): https://www.tastyfx.com/help-and-support/product-details/what-are-tastyfxs-forex-product-details/

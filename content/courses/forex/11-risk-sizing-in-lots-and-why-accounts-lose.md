---
{
  "title": "Risk: Position Sizing in Lots From a Stop in Pips, and Why Most Retail FX Accounts Lose",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "What is the sizing formula this course uses?", "opts": ["Lots = account × leverage ÷ price", "Lots = (dollar risk ÷ stop in pips) ÷ pip value per lot, rounded down", "Lots = margin ÷ 2%", "Lots = 1 per $10,000"], "correct": 1, "explain": "Fix the dollar risk, fix the stop in pips, divide to get dollars per pip, divide by the pip value of one lot, round down to the broker's step."},
    {"q": "OANDA's US regulatory disclosure reported 39,992 non-discretionary accounts in Q2 2026, of which 34.04% were profitable. What is the rule that requires that disclosure?", "opts": ["ESMA's product intervention", "CFTC Regulation 5.5, which requires FCMs and RFEDs to disclose quarterly the number of non-discretionary retail forex accounts and the percentage profitable", "The Dodd-Frank Act's Volcker rule", "No rule; it is voluntary"], "correct": 1, "explain": "The CFTC's 2010 retail forex rule requires the disclosure for each of the four most recent quarters."},
    {"q": "Which broker in the lesson's table reported the highest share of profitable accounts in Q2 2026, and roughly what was it?", "opts": ["tastyfx, about 35%", "OANDA, about 34%", "Interactive Brokers, about 46%", "IG UK, about 69%"], "correct": 2, "explain": "Interactive Brokers reported 45.53% of 23,358 non-discretionary accounts profitable. IG's 69% is the share that lose, not win."},
    {"q": "Ten consecutive losses at 1% risk per trade cost what share of the account, versus at 5%?", "opts": ["10% versus 50%", "9.6% versus 40.1%", "1% versus 5%", "20% versus 100%"], "correct": 1, "explain": "1 − 0.99^10 = 9.6%; 1 − 0.95^10 = 40.1%. Losses compound on a shrinking base, which is why the fraction matters more than the count."},
    {"q": "Why is a quarterly profitability figure of 34% not the same as a 34% chance that a given account is profitable over a year?", "opts": ["It is the same", "Quarterly figures count accounts that were up over one quarter; the same account must be up in successive quarters to be profitable over a year, and costs accumulate, so the annual share is lower", "Because brokers round up", "Because the figure excludes losses"], "correct": 1, "explain": "The disclosures are snapshots per quarter. A trader who is up one quarter and down the next is counted as profitable once and unprofitable once."}
  ],
  "task": "Pull the last four quarters of your own broker's CFTC 5.5 or ESMA risk-warning disclosure and write the numbers at the top of your trading plan."
}
---

## The one formula

Every earlier lesson has built toward a single procedure, and this lesson states it once, in full, and then puts it next to the industry's own scoreboard.

1. Decide the dollar amount you will lose if the trade is wrong. Call it R. One per cent of the account is the conventional starting point; nothing in this course argues for more.
2. Decide where the trade is wrong, in price, and express that distance from entry in pips. Call it S. Lesson 10 sets S from measured range, not from what feels small.
3. Dollars per pip you can afford = R ÷ S.
4. Pip value of one standard lot in your account currency = pip size × 100,000, converted at the current rate if the quote currency is not your account currency (lesson 2).
5. Lots = (R ÷ S) ÷ (pip value per lot). Round down to the broker's minimum step, usually 0.01.
6. Check: lots × pip value × S ≤ R. Then check the margin (lesson 4) is a small fraction of equity and the swap (lesson 7) over the intended hold is known.

The size is the output. Leverage is whatever it turns out to be. Margin is whatever the broker requires. Neither is an input.

## Worked example

Account $10,000, R = $100, rates from the ECB fix of 2026-09-23 (EUR/USD 1.1411, USD/JPY 157.92, GBP/USD 1.3276), spreads and margins from tastyfx's product details, swaps from OANDA TMS Brokers' table for 2026-09-21 to 2026-09-27.

**Trade A: long EUR/USD, stop 40 pips.** $100 ÷ 40 = $2.50 per pip. Pip value per lot $10. Lots = 0.25. Notional = 25,000 × 1.1411 = $28,527.50. Margin at 2% = $570.55 (5.7% of equity). Spread 0.8 pips × $2.50 = $2.00. Swap for a 10-day hold at −2.36% per year: $28,527.50 × 0.0236 × 10/365 = −$18.44. Total known cost of a 10-day trade: $20.44, which is 20% of R. A 40-pip stop that is hit costs $100 + $20.44 = $120.44; a 40-pip target that is hit earns $100 − $20.44 = $79.56. The break-even win rate on this 1:1 trade is 120.44 ÷ (120.44 + 79.56) = **60.2%**, not 50%. Carry against you for ten days moved the hurdle by ten points.

**Trade B: long USD/JPY, stop 80 pips.** $100 ÷ 80 = $1.25 per pip. Pip value per lot = ¥1,000 ÷ 157.92 = $6.332. Lots = 1.25 ÷ 6.332 = 0.197, round down to 0.19. Pip value of the position = 0.19 × 6.332 = $1.203; risk at stop = 80 × 1.203 = $96.25. Notional $19,000. Margin at tastyfx's 5% = $950 (9.5% of equity; the CFTC minimum for a major currency would be 2%, $380). Spread 0.8 × $1.203 = $0.96. Swap for 10 days at +1.81%: $19,000 × 0.0181 × 10/365 = +$9.42. Net cost: −$8.46, a small credit. Break-even win rate on 1:1: (96.25 − 8.46) ÷ ((96.25 − 8.46) + (96.25 + 8.46)) = 87.79 ÷ 192.50 = **45.6%**. The same 1:1 geometry, but carry in your favour moved the hurdle four points the other way.

**Both trades open.** Total risk at stops = $196.25, 1.96% of equity. Total margin = $1,520.55, 15.2% of equity. Correlation of EUR/USD with USD/JPY over the year was −0.58 (lesson 8), and you are long both, so the two positions partially offset: combined one-sigma risk ≈ √(100² + 96² + 2 × (−0.58) × 100 × 96) = √(19,216 − 11,136) = $90, less than either alone. That is a diversified book, which the correlation table told you before you checked.

**Streaks.** With R at 1%, ten straight losses leave 0.99^10 = 90.4% of the account, a 9.6% drawdown. At 5%, 0.95^10 = 59.9%, a 40.1% drawdown that needs a 67% gain to recover. At 10%, 34.9% remains. For a strategy with a 50% win rate, the longest expected losing streak in N trades is about log₂(N): eight in 250 trades, nine in 500. Plan for ten.

## Why most retail FX accounts lose

US retail forex dealers must disclose, under CFTC Regulation 5.5, the number of non-discretionary retail accounts they hold and the percentage that were profitable in each of the last four quarters. EU and UK brokers must state, under ESMA's measures and the FCA's equivalent, the percentage of retail accounts that lose money. These are the industry's own audited figures, and they are consistent across firms, years and jurisdictions.

## Table

| Firm and jurisdiction | Period | Non-discretionary accounts | Profitable | Unprofitable | Source |
| --- | --- | --- | --- | --- | --- |
| tastyfx (US, CFTC 5.5) | Q3 2025 | 8,438 | 40.84% | 59.16% | Public and risk disclosures |
| tastyfx (US) | Q4 2025 | 8,856 | 37.93% | 62.07% | same |
| tastyfx (US) | Q1 2026 | 9,290 | 35.19% | 64.81% | same |
| tastyfx (US) | Q2 2026 | 8,801 | 34.50% | 65.50% | same |
| OANDA Corporation (US, CFTC 5.5) | Q3 2025 | 45,313 | 34.66% | 65.34% | Regulatory public disclosures |
| OANDA Corporation (US) | Q4 2025 | not stated in summary | 32.78% | 67.22% | same |
| OANDA Corporation (US) | Q1 2026 | not stated in summary | 31.74% | 68.26% | same |
| OANDA Corporation (US) | Q2 2026 | 39,992 | 34.04% | 65.96% | same |
| Interactive Brokers LLC (US, CFTC 5.5) | Q2 2026 | 23,358 | 45.53% | 54.47% | Performance of retail client forex accounts |
| IG (UK, FCA/ESMA-style warning) | Current warning, accessed 2026-09-24 | not stated | 31% | 69% | EUR/USD market page |
| EU CFD providers (ESMA analysis, 2018) | Various | not stated | 11% to 26% | 74% to 89% | ESMA press release, 27 March 2018 |

Two readings of the table are correct at once. Between a third and 45% of accounts are profitable in any given quarter, so the market is not unwinnable. And the figures are quarterly snapshots: an account counted as profitable in Q3 can be counted as unprofitable in Q4, so the share of accounts that are profitable over a full year is lower than any single quarter's number, and the share that stay profitable for years is lower again. Interactive Brokers' higher figure is consistent with a client base that is, on average, larger, less leveraged and trading FX as a hedge alongside other assets rather than as a leveraged product; that is an inference, not a disclosed fact.

The reasons are the ones this course has measured, and they compound:

- **Leverage.** Lesson 4's calculation: seven in ten fully leveraged 50:1 positions halve the account in a quarter on a coin flip. ESMA named leverage as the feature behind the 74% to 89% loss rates when it imposed the 30:1 cap.
- **Cost relative to holding period.** Lesson 3: the spread is a small share of a day, but a trade that targets 10 pips pays 8% of its target in EUR/USD and far more in an exotic. Lesson 7: carry against you accumulates daily. Trade A above needs a 60% win rate to break even on 1:1.
- **Stops inside the noise.** Lesson 10: a stop narrower than the instrument's ordinary range converts random movement into realised losses.
- **Events.** Lesson 9: a 188-pip round trip in USD/JPY on the BoJ's decision day, through every stop in both directions.
- **The counterparty.** Lesson 1: the dealer is on the other side and prices its risk. That is disclosed, legal, and constant; it is not why accounts lose, but it is why costs never go to zero.

## What the profitable third does differently

Nothing in the disclosures says. What this course can say is that every item on the list above is a number you can measure and control before the trade: the fraction risked, the stop as a multiple of range, the cost as a share of the target, the swap over the hold, the calendar. A trader who fixes those five numbers has removed the reasons the industry's own data gives for the loss rate. Whether they then have an edge is a separate question, and lesson 12's journal is how they find out.

## Sources

- tastyfx, "FDM public disclosures and risk warning" (CFTC Regulation 5.5 quarterly figures): https://www.tastyfx.com/public-and-risk-disclosures/
- OANDA Corporation, regulatory public disclosures (CFTC Regulation 5.5 quarterly figures): https://www.oanda.com/us-en/legal/regulatory-public-disclosures/
- Interactive Brokers LLC, "Performance of Interactive Brokers Retail Client Forex Accounts": https://www.interactivebrokers.com/en/general/about/performanceCustomerForex.php
- European Securities and Markets Authority, press release of 27 March 2018 (74% to 89% of retail CFD accounts lose money): https://www.esma.europa.eu/press-news/esma-news/esma-agrees-prohibit-binary-options-and-restrict-cfds-protect-retail-investors

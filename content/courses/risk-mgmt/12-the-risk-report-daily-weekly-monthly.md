---
{
  "title": "The Risk Report: Daily, Weekly, Monthly, and the Numbers That Trigger Action",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which numbers belong on the daily report rather than the weekly or monthly one?", "opts": ["Factor exposures and the gate-stack review", "Gross, net, beta-adjusted net, one-day VaR and ES, the day's P&L against VaR, the largest position and its risk share, fast versus slow vol, drawdown from peak, cash and margin excess, and a clean reconciliation", "The correlation matrix and the stress replay", "Strategy-level out-of-sample statistics"], "correct": 1, "explain": "The daily page holds what can change overnight and what the action rules key on. Correlations and stress tests move slowly and go weekly; strategy statistics need a month of trades to mean anything."},
    {"q": "The book's stress VaR is 4.25 times its base VaR. The weekly report tracks that ratio. What is the action rule attached to it?", "opts": ["Nothing; it is informational", "Double the position sizes", "When fast vol crosses above slow vol, the book is assumed to be moving toward the stress number, and gross is cut so that the stress VaR, not the base VaR, fits inside the daily loss budget", "Switch to historical VaR"], "correct": 2, "explain": "The ratio measures how much of the book's calm is borrowed from the regime. The vol crossover from lesson 3 is the earliest signal the regime is changing, and it arrives before the correlations confirm it."},
    {"q": "A 95% one-day VaR is expected to be breached about once a month. The monthly report counts breaches. What count triggers a model review?", "opts": ["More than four in a rolling quarter, or two in one week: either the window is stale or the regime has moved, and the vol input switches to EWMA and the window shortens until the count normalises", "Any breach", "Ten in a year", "Breaches never trigger anything"], "correct": 0, "explain": "Twelve or thirteen breaches a year is calibration; four in a quarter is 33% over the rate, which is within noise for a quarter but a warning. Two in a week is a regime signal, since the breaches cluster when vol clusters."},
    {"q": "Why does the report state each trigger as a number and an action in the same line, written before the day it fires?", "opts": ["For regulatory filing", "Because numbers are easier to read than words", "Because it looks professional", "Because a trigger without a pre-committed action becomes a discussion on the day, and the day is the one time the discussion cannot be trusted; the report's job is to have already decided"], "correct": 3, "explain": "Every rule in this course, from the drawdown ladder to the kill switch, exists to remove a decision from the moment of stress. The report is the document that holds those decisions where you will see them at 6 a.m."},
    {"q": "On 2026-09-23 the book's largest position (NVDA) is 15.0% of NAV and 30.0% of variance, the cap is 15% and 35%. The action is", "opts": ["Sell immediately", "Buy more to reach the risk cap", "None today: both inside their caps; but the position is at the weight cap, so any rally that pushes it over is trimmed at the next close, and that instruction is on the report already", "Hedge with ARKK"], "correct": 2, "explain": "The report does not only flag breaches. It flags where the book is against each limit, so that the trim that will be needed on a 2% NVDA rally is a written instruction rather than a decision. A book at its limits with no pending instructions is a book that will be surprised."}
  ],
  "task": "Produce tonight's daily page for your own book in the format of the worked example, every number computed, every limit stated next to its value."
}
---

## The report is the framework

Everything in lessons 1 through 11 is a number or a rule. The risk report is where they live, and it is the only artefact of the framework that exists on the day it is needed. A framework that is in your head is a framework that will be revised, under stress, by the person least able to revise it. A framework that is on a page, with today's numbers next to yesterday's and each limit next to its value, is one that can be followed by reading.

Three cadences, because the numbers move at three speeds. Daily: what can change overnight. Weekly: what changes with the regime. Monthly: what needs a sample to be judged.

## The daily page

Produced after the close, read before the open. Ten lines, all from lesson 2's shares-times-price table and lesson 4's VaR.

1. **Exposure**: gross, net, beta-adjusted net (two windows), against their limits.
2. **P&L**: today's, against yesterday's VaR; month-to-date; drawdown from the 252-day peak.
3. **VaR and ES**: one-day 95%, historical primary, parametric check; breaches this month.
4. **Concentration**: largest position by weight and by variance share; factor exposures against caps.
5. **Volatility**: book EWMA versus one-year; SPY 20-day versus one-year; the crossover flag.
6. **Funding**: cash at broker, margin excess under the applicable regime, stress VaR × 3 against cash.
7. **Reconciliation**: clean, or the break and its status.
8. **Pending instructions**: what will be done tomorrow if a stated number prints.

Each line has its value, its limit and its distance to the limit. A line at its limit carries an instruction.

## The weekly page

Produced Friday, read Monday. The slower quantities.

- Correlation matrix of the book, last 60 days, against the last year; average pairwise correlation among longs; correlation of each short to the long basket.
- Diversification ratio, current, against the last-year figure.
- Stress VaR (crisis correlations, current vols) and the stress-to-base ratio.
- The 2020 and 2008 replays at current weights.
- Position liquidity: shares held against 30-day ADV.
- Drawdown rule status: where the book is against each threshold; days since the last transition.
- Hedge inventory: what tail protection is on, what it cost this week, what it would pay at −10% and −20%.

## The monthly page

Produced on the first trading day, covering the prior month. The things that need a sample.

- VaR calibration: breaches this month and rolling quarter, against the expected 1.05 per month; historical versus parametric agreement.
- Per-strategy live statistics against out-of-sample: trades this month, mean per trade, running t-statistic; any strategy whose live mean has fallen outside the out-of-sample sampling band is flagged for gate-2 re-test.
- Realised vol of the book against the target; average scale applied.
- Cost analysis: realised round-trip cost against the gate-3 assumption.
- Operational: kill-switch test performed; key rotation date; broker cash confirmation; reconciliation breaks and their causes.
- Limit review: any limit that was touched this month, and whether it should move.

## Worked example

The daily page for the course book, 2026-09-23 close, NAV $1,000,000. Every value is from the lessons' calculations; every limit is from lesson 6, 10 and 11.

**Exposure.** Gross 114.9% (limit 200%; distance 85.1). Net 64.9% (limit 80%; distance 15.1). Beta-adjusted net 0.31 on one-year betas, 0.42 on three-year (limit 0.60; distance 0.29 / 0.18).

**P&L.** Today: SPY −0.72%; book P&L for the session is in the reconciliation. Month-to-date and drawdown from the 252-day peak are computed from the equity series; the drawdown-rule thresholds are −10% (gross × 0.5) and −20% (gross × 0). No transition pending.

**VaR.** Historical one-day 95%: $9,044. Parametric: $9,972. ES: $11,924. Breaches in the last 21 sessions: 1 (2026-09-09 was the fifth-worst day of the last quarter). Calibration: 9 in-sample breaches of the parametric cut over 251 days versus 12.6 expected; conservative, no action.

**Concentration.** Largest by weight: NVDA 15.0% (cap 15%; distance 0.0). Largest by variance share: NVDA 30.0% (cap 35%; distance 5.0). Growth-factor net beta-weighted 0.10 (cap 0.25). **Instruction: NVDA is at the weight cap; trim to 14.5% at the next close if it prints above 15.0% by weight.**

**Volatility.** Book one-year realised 9.6%; EWMA of the book not computed in the course, use SPY as the proxy: SPY EWMA 11.3%, 20-day 10.9%, one-year 13.0%, VIX 15.18. Fast below slow: no crossover flag. Vol-target scale on SPY 1.06.

**Funding.** Long $899,403, short $249,985. Reg T maintenance $299,846; portfolio-margin requirement $97,413. Cash $350,582. Stress VaR (Mar-2020 correlations and vols) $42,357; × 3 = $127,071; cash exceeds it by $223,511. Distance to the 4x-gross scenario that produces a call: not applicable at 1.15x.

**Reconciliation.** Positions: 10 lines matched to the share. Cash: matched within $50. Equity: $1,000,000 matched. Clean.

**Pending instructions.** (1) NVDA trim as above. (2) If SPY's 20-day vol prints above 13.0% (its one-year figure), cut gross to 100% at that close and re-run the stress replay. (3) If the book's daily loss exceeds $19,944, the kill switch halts new orders; at $29,916 it flattens; both are automatic.

**Weekly addendum, same date.** Average pairwise correlation among longs, last year: 0.05 (March 2020: 0.59). Shorts to long basket: IWM 0.57, ARKK 0.62 (2020: 0.92, 0.90). Diversification ratio 3.50 (review trigger 2.0). Stress-to-base VaR ratio 4.25. 2020 replay at current weights: −14.35%. Liquidity: every line under 0.03% of ADV. Drawdown rule: no transitions. Hedges: none held; a 5% TAIL sleeve would have covered about 1.4 points of the 14.35% replay loss at a cost of about 0.6 points a year on this book.

**Monthly addendum, September 2026.** VaR breaches, rolling quarter: within expectation. Live strategy statistics: not applicable, the book is a static specimen. Cost assumption 10 bps, realised not measured. Kill switch: tested with a 1-share order on the first of the month. Keys rotated on schedule. Limits touched: NVDA weight cap, from the rally; no change to the cap.

## Table

| Line | Value, 2026-09-23 | Limit or trigger | Distance | Action if crossed |
|---|---|---|---|---|
| Gross | 114.9% | 200% | 85.1 pts | Reduce to limit at next close |
| Net | 64.9% | 80% | 15.1 pts | Add index short |
| Beta-adjusted net (1y / 3y) | 0.31 / 0.42 | 0.60 | 0.29 / 0.18 | Add index short |
| One-day 95% VaR (hist / param) | $9,044 / $9,972 | $15,000 | $5,956 | Cut gross pro rata |
| Expected shortfall | $11,924 | $20,000 | $8,076 | Cut gross pro rata |
| Largest position, weight | NVDA 15.0% | 15% | 0.0 | Trim to 14.5% |
| Largest position, variance share | NVDA 30.0% | 35% | 5.0 pts | Trim |
| Growth factor, net beta-weighted | 0.10 | 0.25 | 0.15 | Add growth short |
| SPY 20-day vol vs 1-year | 10.9% vs 13.0% | Crossover | 2.1 pts | Gross to 100%; re-run stress |
| Drawdown from 252-day peak | at peak | −10% / −20% | 10 / 20 pts | Gross × 0.5 / × 0 |
| Cash vs 3 × stress VaR | $350,582 vs $127,071 | Cash ≥ 3× | $223,511 | Raise cash |
| Daily loss (kill switch) | — | −$19,944 / −$29,916 | — | Halt / flatten, automatic |
| Reconciliation | Clean | 1 share / $50 | — | Investigate before open |

Values from lessons 2, 4, 5, 6, 10 and 11; limits are the course's illustrative settings for a $1,000,000 book at 1.15x gross.

## The three questions, answered

Lesson 1 asked what a framework has to answer every day. The page above answers them for this book on this date.

How much can it lose? $9,000 to $10,000 on an ordinary bad day, $12,000 on average when it is worse than that, $42,000 if the regime becomes March 2020 overnight, and 14% over five weeks if the whole of March 2020 replays at these weights.

How fast? The one-day numbers are one day; the five-week number arrived over 23 sessions in 2020, and the drawdown rule would have cut gross by half at −10% and to zero at −20% along the way, at the cost lesson 7 measured.

Will it still be here? Cash covers three stress days with $223,000 to spare; the margin excess under either regime is a multiple of any one-day loss in the sample; the kill switch is tested; the reconciliation is clean. Yes, on this date, with this gross. The page exists so that the answer is re-derived tomorrow rather than remembered.

## Sources

- Basel Committee on Banking Supervision (2013). "Principles for effective risk data aggregation and risk reporting." BCBS 239. https://www.bis.org/publ/bcbs239.htm
- Litterman, R. (1996). "Hot Spots and Hedges." *Journal of Portfolio Management* 23 (special issue). https://doi.org/10.3905/jpm.1996.052
- Basel Committee on Banking Supervision (2019). "Minimum capital requirements for market risk." BCBS d457. https://www.bis.org/bcbs/publ/d457.htm

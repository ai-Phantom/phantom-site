---
{
  "title": "The Forward Record, the Run Ledger and What Passed Means",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A forward test recorded each entry price and stop, and a pre-registered stop condition said to halt if cumulative R fell below -20. The exit alerts carried no price and the stored broker payload was the submit acknowledgement with no fill. A reporter written the obvious way scores each missing exit as 0 R. The bias is:", "opts": ["Downward, so the stop fires too early", "Upward for any trade that actually lost, so the record looks better than the truth and the stop condition may never fire", "Zero on average", "Only a display issue"], "correct": 1, "explain": "The denominator was recorded and the numerator never was. A partial total gets acted on; one unpriced exit must make the whole cumulative figure undefined until fills are reconciled."},
    {"q": "Turn-of-month on SPY 2010-2025 had an edge over its null of 0.1385% per trade with a standard deviation of 1.829%. At 12 trades a year, how long does a forward record take to confirm that edge at z = 1.645?", "opts": ["About one year", "About four years", "It cannot be computed", "About 39 years, because (1.645 x 1.829 / 0.1385)^2 = 472 trades"], "correct": 3, "explain": "A forward record cannot confirm a small edge on a monthly rule in any useful time. Its jobs are to prove the process runs, to catch a break, and to accumulate the only out-of-sample observations that exist."},
    {"q": "The host running a forward record was offline for 69 hours over a holiday weekend that included a month-end evening. The rule says an entry may be written late provided the exit has not yet printed. What happens to that month's row?", "opts": ["It is written late with a late-by field if the exit bar has not printed when the host returns; if it has, the row is refused forever and reported as lost", "It is backfilled from the vendor's history", "It is skipped silently", "It is estimated from the prior month"], "correct": 0, "explain": "The thing to protect is that the writer could not know the result, not that the writer was punctual. Blind to the outcome, not on time."},
    {"q": "A forward-record job does nothing on 19 runs out of 20. What should its summary line lead with?", "opts": ["OK", "The number of runs today", "Any month-end that has no row, because a completion notice makes a stopped schedule look identical to a working one", "The cumulative return"], "correct": 2, "explain": "Liveness is counted in the units the experiment produces, month-ends, not in runs or days. 'ok' is what a dead schedule also prints if nothing checks what it should have produced."},
    {"q": "Turn-of-month passed every gate on 1993-2026 SPY at the 99th percentile and replicated across seven markets. In this course, its ledger status is:", "opts": ["A finding; size it", "Refuted", "Underpowered and closed", "A lead: worth two to three independent observations, with a forward record running and nothing traded on the backtest alone"], "correct": 3, "explain": "A pass earns a forward record and a label, LEAD. The seven markets were 1.4 looks, and 45% of the trades had been in data no second vendor had seen until an errand fixed that. Nothing is traded on the backtest alone."}
  ],
  "task": "Write the ledger row your current rule has earned, with its verdict, the gate it died at or the gates it passed, and the one number that decided it, before you change anything about the rule."
}
---

## The last gate never ends

Every gate before this one runs on history. History has been seen, by you or by the people whose papers you read, and every rule tested on it has been selected in part by the fact that it looked good there. The forward record is the only test whose data did not exist when the rule was written. It is also the slowest test in the stack and the easiest to get wrong without noticing, because it produces almost nothing on almost every day.

## What to log

The research notes (Phantom Traders, 2026, internal) record a forward test on SPY that was wired to run to 100 trades against a pre-registered stop condition, halt if cumulative R fell below −20, that nothing in the recorded data could evaluate. Three independent confirmations on 2026-09-30: the alert script attached a price and a stop to the entry alert only, and the target, trail and end-of-day exit alerts carried no price at all; the live trade rows agreed, with every end-of-day row priced as None; and the broker payload stored with each row was the submit acknowledgement, with no fill time, a filled quantity of zero and no average price. The bridge never polled for the fill. The R denominator had been recorded and the numerator never was.

A reporter written the obvious way treats a missing exit as a flat trade and scores it 0.0 R. That biases the total upward for every trade that in fact lost, so the forward record looks better than the truth and the stop condition never fires. The fix was to make one unpriced exit set cumulative R to undefined for the whole report and the stop condition to undefined with it. A partial total is worse than no total, because a partial total gets acted on. Then the real fill was fetched by order id after the acknowledgement, and two traps surfaced: a test regex that could not tell an order id from a client order id passed only because the real id happened to come first in the payload (order the fixture so the decoy comes first), and the bridge wrote order ids in two formats, so matching only one left half the record unreconciled in a bucket that was not an error.

Log, on one row per trade: the signal bar's timestamp and the time the row was written (Lesson 3); the entry price from the broker's fill, not the alert; the stop or the unit of risk (Lesson 4); the exit price from the broker's fill and its timestamp; the realised R or percent; and a field for lateness. Entry and exit on the same row, because the commonest ledger defect is signals that never resolve. Count rows by reading them back, not by counting writes. Keep the file under version control so a row cannot be altered later without the change showing.

## Blind to the outcome, not punctual

The notes' turn-of-month forward record ran on a scheduler whose host was dark 10.9% of the time, measured over 84,238 runs: four outages, two over 60 hours, one of them covering a Monday month-end evening entirely. A rule that entries may only be written for today could not survive that. The rule that replaced it protects the right thing: an entry may be written late, however late, provided the exit bar has not yet printed; once it has, the row is refused forever and reported as lost. Late rows carry how late they were. Trading days are counted on the vendor's calendar.

Three more design rules from the same build. Schedule daily and let the script decide whether today is a month-end, because a scheduler cannot express "last trading day of the month" and a second copy of that rule would drift from the detector. Repeat within the window, because a record cannot backfill and one failed run is a permanently lost observation. Make the summary line the liveness verdict: a job that does nothing on 19 runs in 20 must lead its output with any month-end that has no row, because a completion notice makes a stopped schedule look identical to a working one. An absent vendor bar is refused, never replaced: on 2026-08-31 the UK index had no bar because of the Summer Bank Holiday, and the record said so.

## The stop condition and what a record can confirm

Write the stop condition before the first row, in the units the record produces, and make it computable from the record alone. Then compute how long the record needs to confirm anything, because the answer is usually discouraging and it changes what the record is for. A record of a monthly rule cannot confirm a small edge in a useful time. Its jobs are to prove the process runs, to catch a break (a stretch far outside what the backtest's distribution allows), and to accumulate the only out-of-sample observations that exist.

## The run ledger and what passed means

The ledger is one row per study, written when the study ends: the rule, the window, the universe, the verdict, the gate it died at or the gates it passed, and the one number that decided it. It includes the failures, because the count of studies is the denominator in Lesson 10. The notes' ledger held seventeen studies by mid-September 2026 with one pass, and the order of the gates was fixed so that a study halts at its first failure and says which kind of failure it was:

D0-D6 data → P0 lookahead → P1 eras available → P2 denominator → P3 overlap → G1 geometry → G2 cash → G7 benchmark → G3 null → G4 power → G6 holdout, then replication and the forward record.

A skip is recorded by name and never counts as a pass. A failed gate carries its diagnosis forward: underpowered is not absent. And PASSED means a lead, nothing more. The one pass, turn-of-month on 1993-2026 SPY at the 99th percentile over 395 month-ends, was labelled a lead because 45% of its trades were in data no second vendor had seen, and it was given two errands before belief. A second vendor reaching back to 1993 agreed on returns at a median of 0.002 bps. Seven foreign markets replicated it, three above the 95th, median 94th, all seven positive over their nulls; at a correlation of 0.650 that was 1.4 looks. Its forward record went live with no route to a broker, and its first entry was due on 2026-09-30.

## Worked example

What a forward ledger for turn-of-month on SPY should contain, illustrated on the nine month-ends from 2025-12-31 to 2026-08-31. The prices are from Yahoo Finance daily bars fetched 2026-09-30, so this table was assembled after the fact and is not a forward record; it shows the row format and the arithmetic a real one would carry. Rule: buy the close of the last trading day of the month, sell the close three sessions later. No distribution fell inside any of these windows, so raw and adjusted returns agree.

| entry date | entry close | exit date | exit close | return |
|---|---|---|---|---|
| 2025-12-31 | 681.92 | 2026-01-06 | 691.81 | +1.450% |
| 2026-01-30 | 691.97 | 2026-02-04 | 686.19 | −0.835% |
| 2026-02-27 | 685.99 | 2026-03-04 | 685.13 | −0.125% |
| 2026-03-31 | 650.34 | 2026-04-06 | 658.93 | +1.321% |
| 2026-04-30 | 718.66 | 2026-05-05 | 723.77 | +0.711% |
| 2026-05-29 | 756.48 | 2026-06-03 | 754.24 | −0.296% |
| 2026-06-30 | 746.77 | 2026-07-06 | 751.28 | +0.604% |
| 2026-07-31 | 747.03 | 2026-08-05 | 769.79 | +3.047% |
| 2026-08-31 | 767.05 | 2026-09-03 | 773.17 | +0.798% |

Each return is exit over entry minus one: 691.81 / 681.92 − 1 = +1.450%; 686.19 / 691.97 − 1 = −0.835%, and so on. The sum is +6.675% over nine trades, a mean of +0.742%, six of nine positive. The 2026-09-30 entry has no exit yet (the last bar fetched is 2026-09-29); it is an open row, reported as open, not scored.

Now the missing-exit bias. Suppose the three losing rows had been written without an exit price and a reporter scored them 0. The sum would read 6.675 + 0.835 + 0.125 + 0.296 = +7.931%, an overstatement of 1.256 points on nine trades. The correct report with any exit missing is undefined.

Now the time to confirm. From the capstone's 2010-2025 measurement, the rule's edge over its random-entry null is 0.1385% per trade with a per-trade standard deviation of 1.829%. Required n at z = 1.645 is (1.645 × 1.829 / 0.1385)^2 = (21.72)^2 = 472 trades. At twelve a year that is 472 / 12 = 39.3 years. Nine excellent months, mean +0.742%, are 9 / 472 = 1.9% of the way there, and their mean sits about 0.742 / (1.829 / √9) = 1.2 standard errors above zero. A forward record of this rule is a liveness check and a break detector for decades before it is evidence.

## Table

The forward ledger's fields and the failure each one prevents.

| Field | Source | Failure it prevents |
|---|---|---|
| signal bar time, row written time | detector clock, database clock | stale stamp graded forward (Lesson 3) |
| entry price | broker fill, not alert | modelled P&L presented as measured |
| risk unit (stop or percent) | rule, at entry | collapsed or missing denominator (Lesson 4) |
| exit price and time | broker fill by order id | unpriced exit scored 0; stop condition uncomputable |
| return in R or percent | computed from the two fills | partial totals acted on |
| late-by days | writer vs signal date | outcome-aware late entries |
| lost month-ends | reconciliation against calendar | stopped schedule reading as healthy |

## Sources

- Wald, A. (1945). "Sequential Tests of Statistical Hypotheses." Annals of Mathematical Statistics 16(2). https://doi.org/10.1214/aoms/1177731118
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., Mellor, D. T. (2018). "The preregistration revolution." Proceedings of the National Academy of Sciences 115(11). https://doi.org/10.1073/pnas.1708274114
- Lakonishok, J., Smidt, S. (1988). "Are Seasonal Anomalies Real? A Ninety-Year Perspective." Review of Financial Studies 1(4). https://doi.org/10.1093/rfs/1.4.403
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

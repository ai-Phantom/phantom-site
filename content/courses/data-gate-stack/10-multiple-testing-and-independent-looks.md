---
{
  "title": "Multiple Testing: De-Duping, the Noise Floor and Independent Looks",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Eight of eighteen pairs cleared a measured noise floor of 2 (maximum 5). One ticker appeared in five of the eight passing cells, and three of its four partners were semiconductors. Excluding that ticker leaves:", "opts": ["7 passes, still clear", "8 passes, since the ticker is legitimate", "3 passes against a noise maximum of 5, inside noise; the verdict rested on one name", "0 passes"], "correct": 2, "explain": "The floor was computed assuming the passes are independent draws. Eight passes sharing one name are closer to one observation. De-duplicate by ticker, pair and sector before comparing any count to a floor."},
    {"q": "A turn-of-month rule replicated in seven foreign markets: three above the 95th percentile, median 94th, all seven positive over their nulls. The mean pairwise correlation of their returns was 0.650. How many independent looks are the seven worth?", "opts": ["About 1.4, from 7 / (1 + 6 x 0.650)", "7", "3", "0"], "correct": 0, "explain": "Seven correlated markets on the same calendar rule are not seven draws. The errand added about one independent observation, not seven."},
    {"q": "Nine parameter cells were tested and the best scored the 98th percentile. What percentile should the best of nine independent tests reach by chance alone?", "opts": ["The 50th", "The 98th exactly", "The 95th", "About the 90th, from 9 / 10; a 98th is above that but the family bar to keep a 5% error rate over nine cells is 99.4"], "correct": 3, "explain": "The expected maximum of n uniform draws is n / (n + 1). The Bonferroni bar for nine cells is 1 - 0.05 / 9 = 99.44%. The 98th cleared the single-cell bar and not the family bar, and later failed its confirmatory run."},
    {"q": "Eighteen names on one calendar rule are all net positive, median 83rd percentile, and one is at the 98th. The family bar was fixed at 99.8 in advance. Is the 98th a lead?", "opts": ["Yes, it is the best of the set", "No; the expected maximum of eighteen draws is the 94.7th, the bar is 99.8, and the names are one bet with one to three effective looks", "Yes, because all eighteen are positive", "Only if it repeats next year"], "correct": 1, "explain": "The metals lead had looked exactly like this before its confirmatory test refuted it. A best-of-set result inside the expected maximum is what a family of correlated tests produces on its own."},
    {"q": "Seven ETFs in this course have a mean pairwise daily-return correlation of 0.346, giving 2.28 effective looks. A per-test bar for a 5% family error rate over 2.28 looks is about the 97.8th percentile; over 6 fully independent looks it is the 99.15th. What does the difference change?", "opts": ["Which of the two replication passes clears: at 99.15 only XLF (99.7) does; at 97.8 both QQQ (98.2) and XLF do, and they are close to one look", "Nothing; use 95", "Only the null", "The number of trades"], "correct": 0, "explain": "The correction depends on how many independent questions were asked, and correlated instruments ask fewer than they appear to. Both readings belong in the ledger with the correlation that produced them."}
  ],
  "task": "For your last multi-name or multi-cell result, list every distinct ticker in the passing set with its count, compute the mean pairwise correlation of the instruments, and restate the pass count as effective looks."
}
---

## A count is only as independent as the names in it

Every gate so far scores one rule on one instrument. The moment a rule is tried on many instruments, or many parameter cells, or many markets, a new question arises that none of those gates can answer: how many things were tried, and how many of them were the same thing?

The research notes (Phantom Traders, 2026, internal) reached it through a pairs study that looked, for a day, like the first thing to clear every gate. Eight of eighteen judged pairs beat their own matched null against a measured noise floor of 2.0 (maximum 5 in the noise runs), and cost was not carrying the result. Then the concentration check. One ticker appeared in five of the eight passing cells. The eight cells were only seven distinct pairs, and three of that ticker's four partners were semiconductors. Excluding it left 3 passes against a noise maximum of 5, inside noise. The whole verdict rested on one name.

The rule: before comparing any pass count to a noise floor, de-duplicate by ticker, by pair and by sector. The floor was computed assuming the passes are independent draws; eight passes sharing one name are closer to one observation. Report the count with the concentration next to it.

## The noise floor

The noise floor is the number of passes the identical pipeline produces on a signal with no information. It is measured, not assumed: run the same detector, the same gates and the same thresholds on random entry dates, many times, and record the distribution of pass counts. The notes guessed about 2.5% once and measured 1.3 passes in 41 names. A count above the floor's maximum is a candidate; a count inside its range is nothing. The pairs study's 8 was above the maximum of 5 until it was de-duplicated to 3.

Two broken tests preceded the real one in that study, and each would have been filed as a negative. The first was not finishable: a rolling z-score recomputed its mean and standard deviation over a 120-bar window at every bar, several hundred million operations per pair. The second aligned all 108 tickers on a global common-date intersection, which collapsed 4,697 bars to 1,514 and moved the end date back fifteen months because exactly two tickers set the edges, one acquired in 2025 whose history legitimately ends, and one listed in 2019. One delisting and one late listing destroyed eleven years for every other pair. Align per pair on its own overlap and print how many were skipped.

## How many looks

A family of tests that share an underlying exposure asks fewer independent questions than its size. The standard reduction for n tests with mean pairwise correlation rho is n / (1 + (n − 1) rho), the number of uncorrelated tests with the same variance of the mean.

The turn-of-month rule in the notes replicated in seven foreign index markets: three of seven above the 95th percentile, median 94th, all seven positive over their nulls. The criterion had been written as if these were seven draws. The measured mean correlation was 0.650, so 7 / (1 + 6 × 0.650) = 7 / 4.9 = 1.43 effective looks. The errand was worth about one extra independent observation, not seven. The same rule's 25-name US cross-section had a lower correlation, 0.363, giving 25 / (1 + 24 × 0.363) = 2.57 looks, and that alone had defeated it: eighteen of eighteen names that reached the null were net positive at a median 83rd percentile, one name at the 98th, and the notes call the 98th not a lead, because the expected maximum of eighteen uniform draws is 18 / 19 = the 94.7th percentile and the family bar had been fixed at 99.8 in advance. The metals lead had looked exactly like this before its confirmatory test refuted it.

## Family bars

When several cells are tested, the bar for the best cell has to rise. The Bonferroni bar for a 5% family error rate over k cells is 1 − 0.05 / k; the Šidák version is 1 − 0.95^(1/k) and is nearly identical for small k. Nine breakout cells got a family bar of 1 − 0.05 / 9 = 99.44%. The best cell scored the 98th, which clears a single-cell 95 and not the family 99.4, and Lesson 1 records what its confirmatory run did to it. Eight time-exit widths on one rule scored a maximum of the 87th against an expected maximum of 8 / 9 = 88.9; nothing there was even above chance's best. Six trailing widths produced one 100th, which Lesson 8 traced to overlap.

The harder half of the correction is deciding what k is. Nine parameter cells on one instrument are highly correlated tests; seven markets at 0.650 are 1.4 tests; six ETFs at 0.346 are 2.3. Use the effective count, and say which one you used.

## Worked example

The seven instruments used in this course (SPY plus the six replication ETFs), daily returns from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted. The full pairwise correlation matrix has 21 off-diagonal entries; the ones that matter:

| | SPY | QQQ | IWM | EFA | TLT | GLD | XLF |
|---|---|---|---|---|---|---|---|
| SPY | 1.00 | 0.93 | 0.88 | 0.86 | −0.30 | 0.05 | 0.87 |
| TLT | −0.30 | −0.23 | −0.27 | −0.29 | 1.00 | 0.22 | −0.38 |
| GLD | 0.05 | 0.05 | 0.06 | 0.14 | 0.22 | 1.00 | −0.03 |

Mean of the 21 pairwise correlations: 0.346. Effective looks: 7 / (1 + 6 × 0.346) = 7 / 3.076 = 2.28. Among the five equity funds alone (SPY, QQQ, IWM, EFA, XLF) the mean pairwise correlation is 0.824, and 5 / (1 + 4 × 0.824) = 5 / 4.296 = 1.16 looks.

Now apply that to Lesson 9's replication. Six ETFs were tested, of which QQQ scored the 98.2nd percentile and XLF the 99.7th. Three ways to set the bar:

Single-instrument bar, 95th: both pass. This is the criterion as pre-registered, and it is the right criterion for the question "does the rule pass on this instrument", asked six times. The chance of two or more passes at that bar was 3.3%, computed in Lesson 9.

Family bar over six independent looks, Šidák: 1 − 0.95^(1/6) = 1 − 0.99149 = 99.15th (Bonferroni 1 − 0.05 / 6 = 99.17th). XLF passes, QQQ does not.

Family bar over 2.28 effective looks: 1 − 0.95^(1/2.28) = 1 − 0.97775 = 97.78th. Both pass. Over the 1.16 looks the equity funds represent, the bar is 1 − 0.95^(1/1.16) = 95.7th, and both pass, but they are then one confirmation, not two.

The expected maximum percentile of six independent tests with no information is 6 / 7 = 85.7th; of 2.28 tests, 2.28 / 3.28 = 69.5th. XLF's 99.7th is well above either. The point of the exercise is not that the correction changes the sign of the verdict here; it is that the number of confirmations the replication provides is between one and two and not six, and the ledger has to say so with the correlation that produced it.

The last computation is the one to carry. Six passes on six instruments correlated at 0.9 would look like overwhelming replication and would be one observation. Six passes on TLT, GLD and four things like them would be six.

## Table

The corrections in this lesson, the number each one asks for, and where it came from in the notes.

| Check | Compute | Value in the notes | Value in this course |
|---|---|---|---|
| De-duplicate the passing set | Distinct tickers, pairs, sectors among passes | 8 cells, 7 pairs, one ticker in 5; 3 without it against a floor max of 5 | 2 passes, both US equity, r = 0.93 and 0.87 to SPY |
| Measured noise floor | Same pipeline on random signals, distribution of pass counts | 1.3 of 41 measured against a 2.5% guess; max 5 of 18 pairs | 0.3 of 6 expected; P(2 or more) = 3.3% |
| Effective looks | n / (1 + (n − 1) rho) | 7 markets at 0.650: 1.43; 25 names at 0.363: 2.57 | 7 funds at 0.346: 2.28; 5 equity funds at 0.824: 1.16 |
| Expected maximum | n / (n + 1) | 18 names: 94.7th; 8 widths: 88.9th | 6 funds: 85.7th |
| Family bar | 1 − 0.05 / k or 1 − 0.95^(1/k) | 9 cells: 99.44; 18 names: fixed at 99.8 in advance | 6 looks: 99.15; 2.28 looks: 97.78 |

None of these numbers is hard to compute. All of them are easy to skip when a table of passes is on the screen, and every case in this lesson is a table of passes that did not survive them.

## Sources

- Harvey, C. R., Liu, Y., Zhu, H. (2016). "... and the Cross-Section of Expected Returns." Review of Financial Studies 29(1). https://doi.org/10.1093/rfs/hhv059
- White, H. (2000). "A Reality Check for Data Snooping." Econometrica 68(5). https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H., López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality." Journal of Portfolio Management 40(5). https://doi.org/10.3905/jpm.2014.40.5.094
- Yahoo Finance, SPY historical data (the seven instruments' daily returns): https://finance.yahoo.com/quote/SPY/history/

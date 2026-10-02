---
{
  "title": "Walk-Forward Validation and Scoring Per Era",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The RSI(2) rule on SPY scores the 95th percentile against random entry when the 2010-2025 window is pooled. Scored per four-year era it reads 73rd, 85th, 35th and 99th. What does the pooled figure hide?", "opts": ["Nothing; 95 is the average of the four", "That the null was mis-seeded", "That the rule is short-biased", "That the pass is carried by 2022-2025; the 2018-2021 era sits below the median of random entry and only one era clears the bar"], "correct": 3, "explain": "A pooled percentile can be carried by one exceptional stretch. The per-era view is the discriminator; the gate asks for at least two eras above the bar."},
    {"q": "A swing rule's parameters were frozen on data through 2016 and applied to 2017-2026: 99.4th percentile, profit factor 2.66. The walk-forward on data through 2016 had rejected it at the 82nd percentile. Both tests were rerun with frozen parameters through the same folds: 89.6th on the hard era, and frozen beat re-optimised in every fold. What follows?", "opts": ["The holdout is right and the walk-forward is wrong", "The inner optimisation never helped and hurt on the era where it mattered; the edge is not stationary, decisive after 2016 and marginal before, and 89.6 still misses the bar", "Use the average of 99.4 and 82", "More trades are needed"], "correct": 1, "explain": "When a holdout and a walk-forward disagree, test the mechanism. Two explanations were tested (search noise, sample size) and both died; what remained was that the effect lived in one era."},
    {"q": "A 3% trailing exit passed every gate at the 100th percentile. Of 389 trades, 41 were in 2017 and averaged +13.06%; the other 348 averaged +0.53%. The top five entries were from four days in April 2017, each held about 200 bars for about +20%. Applying the same greedy non-overlap rule to both the real trades and the null:", "opts": ["Cut the real count from 389 to 119 and the percentile from the 100th to the 38th; one move had been counted five times", "Changed nothing; the trades were already independent", "Improved the percentile", "Only affected the null"], "correct": 0, "explain": "Nominal trade count is not effective sample size. The overlap gate P3 now fails any study past 2.0x inflation, and both sides must run the same thinning rule."},
    {"q": "The in-sample ranking of nine strategies over ten years and over two years agreed at Spearman +0.933. Against a holdout, the ten-year ranking correlated -0.10. What does the +0.933 show?", "opts": ["That the in-sample ranking is reliable enough to trade", "That the holdout is corrupt", "That the in-sample measurement is reproducible and still predicts nothing out of sample; reproducibility is not validity", "That two years is enough"], "correct": 2, "explain": "A stable number can be stably wrong about the thing you care about. The best strategy on a 59-session holdout was the second worst over ten years; a small holdout ranks nothing."},
    {"q": "A study restricted its real trades to the post-2008 subset and scored them against a null drawn from the full 1993-2026 window. Why is that wrong?", "opts": ["It is not wrong; the null should always use all data", "The post-2008 subset is too small", "Nulls cannot be subset", "Each subset must draw its own null from its own pool; the full-window null had a different drift, and the pre-2008 null mean was in fact negative"], "correct": 3, "explain": "Restricting one side and not the other is the same error as the direction-keeping null in Lesson 5: an unmatched control. Fixed, the pre-2008 half read the 99th percentile and the post-2008 half the 89.5th."}
  ],
  "task": "Split your rule's window into at least four eras, score each against its own random-entry null, and count how many eras clear the 95th; if it is fewer than two, the pooled percentile is not a result."
}
---

## An edge must repeat

A pooled statistic over sixteen years can be carried by two of them. The rule that produces it will look identical, in every summary number, to a rule that earned the same total a little every year. The difference is the whole question, because a trader gets the years one at a time.

The research notes (Phantom Traders, 2026, internal) reached this the hard way. A swing-momentum rule was scored per walk-forward fold on five instruments, and the per-fold percentiles against random entry disagreed with the pooled figure in both directions:

| instrument | fold 1 | fold 2 | fold 3 | fold 4 | folds above 95 | pooled |
|---|---|---|---|---|---|---|
| QQQ | 36 | 76 | 46 | 24 | 0 of 4 | 51.1 |
| SPY | 65 | n/a | 91 | n/a | 0 of 2 | 88.1 |
| NVDA | 91 | 24 | 27 | 7 | 0 of 4 | 16.6 |
| TSLA | 79 | 83 | n/a | 17 | 0 of 3 | 52.3 |
| AAPL | 64 | 96 | 90 | 99 | 2 of 4 | 99.5 |

NVDA opens at the 91st and collapses to the 7th. SPY pools to a respectable 88th from a single good era. AAPL is the only instrument whose edge appears in more than one fold, and even there it is absent before 2016. The gate built from this asks for at least two eras above the bar, where the eras are the walk-forward folds already computed (no extra backtests), and an era with fewer than fifteen trades is scored as not-available and counts toward neither side. The threshold was anchored on an existing two-fold convention rather than fitted; at three, nothing promotes, AAPL included.

## When the holdout and the walk-forward disagree

The AAPL case is worth following to the end because it shows the discipline the notes apply when two valid tests disagree. Parameters frozen on data through 2016 and applied to 2017-2026 (first trade May 2017, no contamination from the search era) scored the 99.4th percentile against random entry, a profit factor of 2.66, a deployed Sharpe of 2.23. A clean pass. But the walk-forward on data through 2016 had rejected the same rule at the 81.8th percentile.

Two explanations were proposed and both tested. The first: the parameter search adds noise. Partly true, and it does not rescue the rule. Frozen parameters run through the same fold windows beat the re-optimised search on the hard era (profit factor 1.74 against 1.64, Sharpe 0.91 against 0.74, 89.6th percentile against 81.8th) and tie on the full history. The inner optimisation never helps, and on the era where parameter choice matters it hurts. But 89.6 still misses 95. The second: sample size. Dead; the frozen version has more trades (136 against 122), not fewer. What is left is that the edge is not stationary: decisive after 2016, marginal to absent across 1991-2016. Do not pick the reading you prefer. Test the mechanism.

## The overlap defect

Per-era scoring finds an edge that lived in one era. It does not find an edge that was one trade counted many times, and the notes record the only pass their stack ever produced being exactly that. A 3.00% trailing exit on an inside-day rule on SPY cleared every gate at the 100th percentile. Of 389 trades, 41 fell in 2017 and averaged +13.06%; the other 348 averaged +0.53%. 2017 was the lowest-volatility year in the sample, which produced a glut of inside days, and a 3% trail went about 200 bars untouched. The top five trades were entries from 4, 7, 12, 18 and 21 April 2017, held 198 to 210 bars, all about +20%. One move, counted five times.

Nothing in the stack saw it. The denominator gate measures concentration by magnitude, and the top five were 7.0% of gross, unremarkable, because each duplicate was an ordinary-sized trade. The power gate used nominal n. The null drew the same nominal count, but uniformly chosen dates do not cluster the way a regime-driven detector does, so the real side took one correlated bet against a null diversified over eighteen years.

The fix is an overlap gate, P3, that computes effective n as the greedy non-overlapping count and fails a study past 2.0x inflation, with the same greedy rule applied to both sides. At the 3% width the real count fell from 389 to 119 and the percentile from the 100th to the 38th. At 1%, where overlap was mild, 389 became 278 and the 42nd became the 48th. Measured cases bracket the threshold rather than derive it: 1.40x harmless, 2.21x not owed its pass, 3.27x fatal. The same gate later caught a pooled twelve-name book at 3.96x (2,575 nominal trades, 650 effective), and a 25-name cross-section on one calendar date at 24.15x: 25 correlated names entered on the same day are one observation.

## Two nulls for two subsets

One more mismatch belongs here because it is an era error. A turn-of-month study extended from 2008-2026 to 1993-2026 and produced a drop-one-era table. The table restricted the real trades to a subset while the null kept drawing from all 8,463 bars, and the pre-registered criterion scored the post-2008 half against the full-sample null. Each subset must draw from its own pool. Fixed: the pre-2008 half, 176 trades, +0.2699% against its own null of −0.0345% (that window holds the 2000-2002 decline, so a random three-day hold lost), edge +0.3044 points, 99.0th percentile; the post-2008 half, 219 trades, +0.2999% against +0.1360%, edge +0.1639, 89.5th. The effect was larger in the older era and the drift smaller, which is what a per-era view exists to show.

## Reproducible is not valid

Nine intraday strategies were ranked over ten years and over two years of the same instrument. The two in-sample league tables agreed at a Spearman correlation of +0.933. Against a holdout, the ten-year ranking correlated at −0.10 and the two-year at −0.02. The in-sample measurement is not noisy; it is highly reproducible and carries no information about out-of-sample order. A stable number can be stably wrong about the thing you care about. The best strategy on a 59-session holdout was the second worst over ten years, which settles what a small holdout is worth: it ranks nothing and is not a tiebreaker.

## Worked example

The RSI(2) rule from Lesson 7 (enter at the close when RSI(2) is below 10, exit at the first close above the 5-day moving average, 5 bps per side) on SPY daily bars from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted. The pooled result: 173 trades, +0.3456% net per trade, 95.0th percentile against 2,000 random-entry draws matched on holds and charged the same cost.

Now the same trades split into four four-year eras, each scored against its own null: 2,000 draws of random entries confined to that era, matched to that era's trade count and holding periods, seed 20260930.

2010-2013: 40 trades, +0.3042% per trade net; era null +0.1273%; 72.9th percentile. SPY rose 76.9% over the era.

2014-2017: 39 trades, +0.2801%; null +0.0632%; 84.9th. SPY +59.2%.

2018-2021: 41 trades, +0.0291%; null +0.1525%; 34.8th. SPY +89.4%. The rule earned less than a random day in the era that included the fastest rally in the sample.

2022-2025: 53 trades, +0.6700%; null +0.0547%; 99.1st. SPY +50.9%.

Eras above the 95th: one of four. The gate requires two. The pooled 95.0 is arithmetic on a distribution whose mass sits in the last era: 53 of 173 trades and +0.6700% against the other three eras' weighted mean of (40 × 0.3042 + 39 × 0.2801 + 41 × 0.0291) / 120 = +0.2024%. Remove 2022-2025 and the remaining 120 trades average +0.2024% against era nulls averaging about +0.114%, a gap that in Lesson 5's terms is inside the noise of a 120-trade sample.

The verdict line for this rule now reads: 95th pooled, 1 of 4 eras, fails the era gate. Combined with Lesson 7's 0.49x against buy-and-hold, it fails twice, for two different reasons, and the reasons are both more informative than the pooled percentile that had it on the bar.

![Bar chart of the RSI(2) rule's percentile against a random-entry null on SPY for four eras, 2010-13 at 72.9, 2014-17 at 84.9, 2018-21 at 34.8, 2022-25 at 99.1, and the pooled window at 95.0; bars at or above 95 are green and the rest red. Source: Yahoo Finance SPY daily data, 2,000 draws per era, fetched 2026-09-30.](figures/per-era-percentiles.svg)

## Table

The gates this lesson adds, in the order the stack runs them, with the case that forced each.

| Gate | Question | Threshold and its origin | Case that forced it |
|---|---|---|---|
| P3 overlap | Effective n from greedy non-overlap; same rule on both sides | Fail past 2.0x inflation; 1.40x, 2.21x and 3.27x measured | 3% trail: 100th to 38th; one April 2017 move counted five times |
| G4 power | Is n large enough to resolve the edge over the null mean, not over zero? | Required n from (sd / edge)^2 at z = 1.645; runs after G3 so the null mean exists | Turn-of-month: 159 required against zero, 456 against the null |
| G5 eras | Does the edge repeat? | At least two folds above the 95th; folds under 15 trades not counted | AAPL 2 of 4 promotes; NVDA 0 of 4 with a 91st opening fold rejects |
| G6 holdout | Frozen parameters on an untouched era, sign and magnitude | Disjoint window asserted in code; median of seven seeds | Breakout: 98th in discovery, 85th on 8.3 unseen years |

A failed power gate must say which kind of failure it is. A rule at the 86th percentile with five of five eras positive and n = 219 against a required 456 is underpowered, not absent; the notes carry that verdict forward past the halt so it cannot be read as a dead setup.

## Sources

- Bailey, D. H., Borwein, J. M., López de Prado, M., Zhu, Q. J. (2017). "The Probability of Backtest Overfitting." Journal of Computational Finance 20(4). https://doi.org/10.21314/JCF.2016.322
- Arnott, R., Harvey, C. R., Markowitz, H. (2019). "A Backtesting Protocol in the Era of Machine Learning." Journal of Financial Data Science 1(1). https://doi.org/10.3905/jfds.2019.1.064
- McLean, R. D., Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" Journal of Finance 71(1). https://doi.org/10.1111/jofi.12365
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

---
{
  "title": "The Random-Entry Null: Timing Against Random Timing",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A Donchian breakout on SPY 2010-2025 averaged +1.43% per trade over 71 trades with a mean hold of 30.8 sessions. Two thousand random-entry draws with the same 71 holding periods averaged +1.52%. The rule's percentile is 42. What did the breakout signal contribute?", "opts": ["About 1.4% per trade of timing skill", "A negative contribution large enough to reject the rule", "Cannot say without costs", "Nothing measurable; a random day with the same hold earned as much, and SPY's 0.0455% daily drift times 30.8 sessions is 1.40% on its own"], "correct": 3, "explain": "The positive return was drift plus holding period. The signal's timing sits in the middle of the random distribution, which means it added no information about when to be long."},
    {"q": "Why must the null match the holding period of each real trade rather than use a fixed hold?", "opts": ["Because in a drifting asset the return scales with time in the market, so a null with shorter holds would be beaten by any rule that simply holds longer", "Fixed holds are harder to code", "Because the exchange requires it", "It does not matter for daily data"], "correct": 0, "explain": "Holding longer collects more drift. A rule whose only property is a long hold beats a short-hold null without any timing information. Matching holds removes the exposure difference and leaves the timing."},
    {"q": "An intraday breakout rule chooses long or short from the direction of the break. A null that keeps each real trade's direction and randomises only the entry time scored the real rule at the 0th percentile; a null that coin-flips direction scored it at the 98th. Which null is right?", "opts": ["The direction-keeping null, because it is more closely matched", "Average them", "The coin-flip null, because the direction was chosen by the signal; a null that knows which way the day broke is leaking the outcome", "Neither; use a fixed hold"], "correct": 2, "explain": "When the signal picks the direction, keeping it hands the null the signal's information and it merely enters sooner. Daily rules that are always long can keep direction; rules that choose it cannot."},
    {"q": "A rule only fires when the close is above its 200-day average. Its null drew entry dates uniformly, including the 2008 and 2020 lows. Correcting the null to draw only from eligible dates moved a ten-day-hold cell from the 5th to the 16th percentile. Which direction was the original error?", "opts": ["It flattered the rule", "It punished the rule, because the null was allowed to buy crashes the rule could never buy", "No effect on verdicts", "It depends on the seed"], "correct": 1, "explain": "The unmatched null measured random timing plus the right to enter below the filter, where the best forward returns in the sample sit. The error scales with how little the exit truncates; a 2R bracket caps those windows and the correction moved that cell only five points."},
    {"q": "A cell scored the 99th percentile on one seed. Across seven seeds it scored 93.5, 98.0 and 99.0, and zero of seven cleared the 99.4 family bar. What is the rule for cells near the bar?", "opts": ["Take the best seed", "Take the first seed", "Re-run the null across several seeds and report the median; 200 draws is a sample and seed noise is decisive at the 99th even though it is irrelevant at the 40th", "Increase the hold"], "correct": 2, "explain": "A bootstrap percentile is itself an estimate. Near the pass line its sampling error is the whole question."}
  ],
  "task": "Take any long rule you have tested on a rising asset and score it against a random-entry null matched on trade count and holding periods; write down the percentile before you look at the equity curve again."
}
---

## A positive backtest is the null hypothesis

SPY rose about five-fold between 2008 and 2026, and about six-fold between 2010 and 2025. On an asset like that, almost any rule that is long some of the time and flat the rest will show a profit. The profit is not evidence of anything the rule did; it is the asset's drift, collected in proportion to the time the rule spent holding it. The question a backtest has to answer is not whether the rule made money but whether it made more than an equally exposed rule that entered on random days.

That is the random-entry null. Generate many pseudo-strategies that enter at random dates, hold for the same lengths as the real trades, use the same exit geometry and the same direction rules, and record what each one earned. The real rule's percentile against that distribution measures timing against random timing. Drift is controlled for, not measured; a rule at the 50th percentile has timing worth exactly nothing, however large its total return.

## The breakout that random entry beat

The research notes (Phantom Traders, 2026, internal) record the study that made this gate the one that outranks the others. A Donchian channel breakout on SPY, 2008 to 2026, in four cells (20- or 55-day entry channel, 10- or 20-day exit channel), read as the cleanest win of its batch: all four cells positive over the full sample, all four positive out of sample, best holdout +0.225 R. Against a null matched on trade count, direction mix, holding period and bracket geometry:

| cell | real, R per trade | null mean | percentile |
|---|---|---|---|
| 20 / 10 | +0.059 | +0.201 | 2nd |
| 20 / 20 | +0.034 | +0.251 | 0th |
| 55 / 10 | +0.118 | +0.255 | 7th |
| 55 / 20 | +0.092 | +0.312 | 1st |

Entering on a random day beat the breakout signal in every cell. The positive R was drift plus the shape of a trailing exit, and the signal actively subtracted value: it bought after the move it was trying to catch. Every other gate had passed it.

## What the null must match

A null is only as good as its matching, and each mismatch in the notes was found by getting it wrong first.

Count and holding period. Holding longer collects more drift, and the null must collect the same amount. The notes record a time-exit surface where mean return climbed monotonically with the hold, from +0.058% at one day to +1.007% at twenty, while the percentile did not climb at all. The drift went up; the timing stayed where it was.

Direction. A daily rule that is always long can keep its direction in the null. A rule whose direction is chosen by the signal cannot: an intraday breakout that goes long on an upside break, scored against a null that kept each trade's direction and randomised only the entry time, landed at the 0th percentile; against a null that coin-flipped direction it landed at the 98th. A 98-point swing from the null's construction alone. The direction-keeping null knew which way the day broke and merely entered sooner, which is the signal's entire information leaked into the control. Coin-flip whenever the signal chooses.

The setup's own filter. Every daily setup in the notes required the close to be above its 200-day average. The first null drew dates uniformly, so it could enter below the filter, including at the 2008 and 2020 lows whose forward returns are the best in the sample. It measured random timing plus the right to buy crashes the rule could not buy. Correcting the null to draw only from eligible dates moved a ten-day-hold cell from the 5th percentile to the 16th, and a one-day hold from the 48th to the 63rd. The error scales with how little the exit truncates; under a 2R bracket the same correction moved one cell only five points, which is how five prior studies carried it invisibly. It biased toward false negatives, the safe direction, and flipped no recorded verdict. The eligible pool is now printed with every run so an unmatched null can never read as matched.

Time of day, for intraday rules. The real entries' median offset was four bars from the open; a uniform draw's was forty. That gap is volatility and time left to resolve, and a null that ignores it is comparing different trades.

The same procedure on both sides. When the real trades were thinned to a non-overlapping set, the first null was thinned by rejection sampling. A long trade overlaps more and gets rejected more, so the null silently selected short trades, and a short trade under a trailing stop is a loser; its mean fell to −0.39% on construction alone and every real cell looked better. Both sides must run the same greedy rule, not merely both be non-overlapping.

Seeds. Two hundred draws is a sample. A cell near the pass line scored the 99th percentile on one seed and 93.5, 98.0 and 99.0 across seven; zero of seven cleared the family bar. Seed noise is irrelevant at the 40th percentile and decisive at the 99th. Re-run across seeds for any cell near the bar and report the median.

## What a percentile is and is not

A percentile against random entry answers one question: did the rule choose its days better than chance? It does not say the rule is profitable, which is Lesson 6. It does not say it beats holding the asset, which is Lesson 7. And a very high or very low percentile is a prompt to check the measurement before writing an explanation. The notes record two 0th-percentile results, both bugs (a short's target built above its entry, and an overlap artefact), and the author had written an explanation for one of them before checking the number. A 0th percentile is as implausible as a 100th.

## Worked example

Donchian 20/10 on SPY daily bars from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted closes, no costs (costs are the subject of Lessons 6 and 11). Entry: the close exceeds the highest high of the prior 20 sessions. Exit: the close falls below the lowest low of the prior 10 sessions. One position at a time, always long.

The rule produced 71 trades. Mean return per trade +1.4251%; median hold 27 sessions, mean hold 30.8; 47.9% of trades positive; the sum of per-trade returns +101.18%; time in the market 54.4% of sessions.

The null: for each of 2,000 draws, choose 71 random entry sessions uniformly from the window, hold each for the corresponding real trade's hold length (so the multiset of holding periods is identical to the real rule's), and record the mean return per trade for that draw. Seed 20260930.

The null's mean of means was +1.5190%; its 5th percentile +0.5553% and its 95th +2.4499%. The real rule's +1.4251% falls at the 42.2nd percentile: 844 of the 2,000 random-entry draws did better than the breakout.

Check the null against the drift directly. SPY's average daily growth over the window was 0.0455% (the ratio of the last close to the close on 2010-02-02, after the 20-session warm-up, is 6.178, and 6.178 raised to 1/3,999 sessions minus one is 0.000455). Multiply by the mean hold: 0.0455% × 30.8 = 1.40%, within a tenth of a point of the null's 1.52%. The null is, to a first approximation, the drift times the time held, and so was the rule.

Buy-and-hold over the same window, for the standing bar the stack prints alongside: +517.8%. The rule's sum of returns, +101.18%, is what 54% exposure to a rising asset pays, and the null says that a rule which chose its 54% at random would have been paid the same.

![Histogram of the random-entry null for the Donchian 20/10 rule on SPY 2010-2025: 2,000 draws, each matched on 71 trades and their holding periods, binned by mean return per trade in 0.2-point bins from -0.4% to 3.4%. The bin from 1.4% to 1.6%, drawn in red, holds the real rule's +1.43%, at the 42nd percentile.](figures/null-distribution-donchian.svg)

## Table

The four matching failures from the notes, each with the size of the swing it produced.

| Mismatch | What the null measured | Swing when fixed |
|---|---|---|
| Direction kept when the signal chose it | The signal's information, entered earlier | 0th to 98th percentile |
| Entry pool ignored the rule's own filter | Random timing plus crashes the rule could not buy | 5th to 16th (10-day hold); 48th to 63rd (1-day) |
| Non-overlap by rejection sampling on the null only | A short-biased null under a trailing stop | 1% trail: 42nd to 99th, spurious |
| One seed, 200 draws, cell near the bar | Sampling error of the percentile itself | 99th on one seed; 93.5 to 99.0 across seven |

Each row is a null that was methodologically defensible on paper and wrong in a way that only a second construction exposed. Print what the null drew from, every run.

## Sources

- Brock, W., Lakonishok, J., LeBaron, B. (1992). "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns." Journal of Finance 47(5). https://doi.org/10.1111/j.1540-6261.1992.tb04681.x
- Sullivan, R., Timmermann, A., White, H. (1999). "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." Journal of Finance 54(5). https://doi.org/10.1111/0022-1082.00163
- Efron, B. (1979). "Bootstrap Methods: Another Look at the Jackknife." Annals of Statistics 7(1). https://doi.org/10.1214/aos/1176344552
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

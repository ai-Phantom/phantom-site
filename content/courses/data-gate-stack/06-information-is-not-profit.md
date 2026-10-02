---
{
  "title": "Information Is Not Profit: Beating the Null While Losing",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A narrow-range breakout tested on 15 fresh large-cap names beat its matched null at the 100th percentile on 14 of them. Their nulls averaged -0.17 R to -0.39 R per trade; the rule averaged -0.08 R. What has been shown?", "opts": ["The rule is an edge on 14 of 15 names", "The null is broken", "The rule loses less than random entry loses with the same bracket; the signal carries information and the trade loses money", "Costs were omitted"], "correct": 2, "explain": "A strongly negative null means the bracket itself loses by construction. Beating it says only that the signal is less bad than chance. The gate is two-sided: beat the null AND be positive after measured cost."},
    {"q": "A short rule on SPY 2010-2025 averaged -0.2144% net per trade against a null of -0.2757% and sits at the 73rd percentile. Over 341 trades it lost 73% cumulatively. Which statement is correct?", "opts": ["It lost less than most random short entries, which is information about timing and no reason to trade; the null is negative because shorting a rising asset loses by construction", "It beat 73% of random short entries and should be traded small", "The percentile proves it is profitable in some years", "The null should have been long"], "correct": 0, "explain": "Report the percentile and the net expectancy side by side, always. A percentile on a page of negative numbers is not a result."},
    {"q": "An RSI(2) entry with a 0.25% stop and a 2R target on SPY paid 10 bps per round trip. In R, that cost is:", "opts": ["0.10 R", "0.025 R", "Cost does not convert to R", "0.40 R, because 10 bps divided by a 25 bp stop is 0.4"], "correct": 3, "explain": "Cost in R is cost divided by stop distance. The same 10 bps is 0.10 R at a 1% stop and 0.05 R at 2%. Tight stops make cost the dominant term."},
    {"q": "A gap-fill rule with a tight stop read +0.274 R and scored the 0th percentile on all eight tickers against nulls of +0.476 to +0.775 R. Why was the null so high?", "opts": ["The tickers were rising", "Tightening a stop inflates every R multiple, and the null was computed with the same tight stop, so it inflated too; the rule's R was ordinary once the null was matched", "The null had no stop", "A seed error"], "correct": 1, "explain": "Always compute the null with the same stop. A rule cannot beat a null it is not matched to, and the tight-stop illusion is a cousin of the collapsed denominator."},
    {"q": "Across a 42-cell tuning surface, every change that raised hit rate lowered reward-to-risk by a matching amount and every cell sat below its own breakeven. What does that pattern mean?", "opts": ["The rule is on the accuracy/payoff frontier; tuning moves along the frontier and cannot cross breakeven", "The rule is close and needs a finer grid", "The exit is wrong", "Costs are too high"], "correct": 0, "explain": "If a change moves hit rate and payoff in opposite directions by matching amounts, there is no free parameter left. If a change moves one without costing the other, an error is present and worth fixing."}
  ],
  "task": "Add two columns to your results table, net expectancy after measured cost and the null's mean, and refuse to read the percentile column without them."
}
---

## Half a gate

Lesson 5 established the random-entry null as the gate that outranks the others, because it was the only one a drifting breakout failed. The next round of studies showed that it was half a gate. The research notes (Phantom Traders, 2026, internal) tested a narrow-range breakout on fifteen large-cap technology names that had never been pulled before. Fourteen of fifteen beat their matched null at the 100th percentile. Fourteen of fifteen lost money. Their nulls sat at −0.17 R to −0.39 R per trade; the rule returned −0.08 R. The percentile column looked triumphant on a page of negative numbers.

Beating the null means the signal has information about timing. It does not mean the trade is profitable. The gate is two-sided from here on: beats its matched null, and is positive after measured cost. Report both, always adjacent, because each one alone can be read as the other.

## Why a null can be negative

A random-entry null inherits three things from the real rule: the asset's drift over the hold, the direction, and the bracket. Any one of them can make the null negative. Shorting an asset that rises loses on drift. A bracket that pays 1 R on a win and charges 1 R plus cost on a loss loses on cost. A tight stop that gets hit by ordinary noise before an ordinary move can pay loses on geometry. When the null is strongly negative, it is telling you that the trade structure loses by construction, and a rule that beats it is a rule that loses less by construction. That is information about the signal and a warning about the trade.

## Cost lives in the denominator

Cost is quoted in basis points of price and paid in R. Ten basis points round trip is 0.10 R against a 1% stop, 0.05 R against a 2% stop and 0.40 R against a 0.25% stop. The tighter the stop, the more of every trade's outcome is friction. The notes record two ends of the range in one line: a gap-fill rule where friction was 0.1 of a 0.4 percentage-point shortfall, nearly irrelevant because the risk unit was a full gap width, and a dead options book where friction was 59% of the loss on zero-to-two-day premium. Same measurement, opposite conclusion, and the difference was the stop distance.

Cost also decides which gate a rule dies at. The null pays the same date-dependent cost as the real rule, so friction cancels in the difference between them and the percentile barely moves. The turn-of-month study in the notes sat at the 99.5th percentile from a one-tick cost floor through four times the modelled cost, while its tradeable return fell from +0.3283% to +0.0383% per trade. Cost decides the geometry gate G1 and the cash gate G2, not the null gate G3. A rule can hold its percentile all the way to being untradeable.

## The tight-stop illusion

Tightening a stop inflates every R multiple, and the null inflates with it. A gap-fill rule with a tight stop read +0.274 R and scored the 0th percentile on all eight tickers against nulls of +0.476 to +0.775 R. Nothing was wrong with the rule's arithmetic; the null had been computed with the same tight stop and so was inflated by the same factor, and once matched, the rule's R was ordinary. Always compute the null with the same stop. This is the cousin of Lesson 4's collapsed denominator: there the denominator collapsed by accident on some trades, here it is small by design on all of them, and in both cases R stops meaning what it says.

## The frontier test

One more diagnostic from the same round. A VWAP rule was tuned across 42 cells spanning hit rates from 28% to 60% and reward-to-risk ratios from 0.51 to 1.84. Every cell sat below its own breakeven. Every change that raised the hit rate lowered the payoff by a matching amount; the shortfall narrowed to −0.9 percentage points and never crossed zero. That is the accuracy/payoff frontier, and tuning along it cannot help. The contrast case was an opening-range rule whose stop sat inside the range it had just broken: fixing that moved the hit rate without costing payoff, because it was an error rather than a trade-off. If a change moves hit rate and payoff in opposite directions by matching amounts, you are on the frontier. If a change moves one without costing the other, you have found an error worth fixing.

## Worked example

Two computations on SPY daily bars from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted, with 5 bps per side (10 bps round trip) charged on every trade and on every null trade.

First, a rule whose null is negative because the direction loses. Short SPY at the close after three consecutive higher closes; cover at the close three sessions later; no overlap. This produced 341 trades. Gross mean per trade −0.1144%; net of cost −0.2144%; 35.5% of trades profitable; cumulative net −73.1%. The matched null, 2,000 draws of 341 random short entries with the same three-session hold and the same cost, has a mean of −0.2757%, with a 5th percentile of −0.4378% and a 95th of −0.1137%. The rule's −0.2144% sits at the 72.9th percentile.

Read the two numbers together. The rule lost less than 73% of random short entries did: the signal (three up closes) carries a little information about a subsequent pause. And it lost 0.21% per trade, 73% over sixteen years, because shorting an asset that returned 702% over the window loses on drift whatever the timing. The percentile is not wrong. It is the answer to a different question from the one a trader is asking.

Second, the same 10 bps under three stop widths. Enter long when RSI(2) is below 10 at the close; stop a fixed fraction below entry; target at 2 R; exit at the stop, the target, or the tenth bar's close. Null: 500 draws of random entries with the identical bracket.

| stop | trades | real R | cost in R | null R | percentile | real R net of cost |
|---|---|---|---|---|---|---|
| 0.25% | 252 | −0.012 | 0.40 | +0.053 | 21st | −0.412 |
| 1.00% | 233 | +0.273 | 0.10 | +0.213 | 73rd | +0.173 |
| 2.00% | 188 | +0.207 | 0.05 | +0.188 | 61st | +0.157 |

The cost column is 0.0010 divided by the stop fraction: 0.0010 / 0.0025 = 0.40 R, 0.0010 / 0.01 = 0.10 R, 0.0010 / 0.02 = 0.05 R. At the tight stop the null is positive (a 2R target on a rising asset with a stop that noise hits often is still, on average, slightly positive before cost), the rule is below it, and cost is four-tenths of an R on every trade; the net −0.412 R per trade is dominated by friction. At 1% the rule edges the null (73rd percentile, not a pass at a 95th bar) and keeps +0.173 R after cost. Neither cell passes the two-sided gate, and the point is which side each one fails on: the tight stop fails on cost, the wide stop fails on timing.

## Table

The two-sided verdict on the cases from this lesson, written the way the stack prints it: percentile and net expectancy side by side.

| Rule | Percentile vs matched null | Net per trade after cost | Verdict |
|---|---|---|---|
| Narrow-range breakout, 15 fresh names (notes) | 100th on 14 of 15 | −0.08 R (nulls −0.17 to −0.39 R) | information, not profit |
| Short after three up closes, SPY 2010-25 | 73rd | −0.2144% | information, not profit |
| RSI(2) long, 0.25% stop, 2R | 21st | −0.412 R | fails both sides |
| RSI(2) long, 1.00% stop, 2R | 73rd | +0.173 R | positive, no timing evidence |
| Gap fill, tight stop, 8 tickers (notes) | 0th (null inflated by the same stop) | +0.274 R | mis-matched null; rerun |
| Turn-of-month, SPY 1993-2026 (notes) | 99.5th at every cost level | +0.3283% at one tick, +0.0383% at 4x model | percentile survives cost; tradeability does not |

The last row is the one to keep. The null gate cannot see cost, because both sides pay it. A rule's percentile is a statement about its signal; its net expectancy is a statement about its trade; a strategy needs both, and the second one is what a broker settles.

## Sources

- Novy-Marx, R., Velikov, M. (2016). "A Taxonomy of Anomalies and Their Trading Costs." Review of Financial Studies 29(1). https://doi.org/10.1093/rfs/hhv063
- Frazzini, A., Israel, R., Moskowitz, T. J. (2018). "Trading Costs." SSRN Working Paper 3229719. https://doi.org/10.2139/ssrn.3229719
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/

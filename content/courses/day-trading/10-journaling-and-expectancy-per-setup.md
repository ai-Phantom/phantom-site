---
{
  "title": "Journaling and Measuring Expectancy per Setup",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Expectancy per trade is:", "opts": ["Win rate minus loss rate", "(Win rate × average win) − (Loss rate × average loss)", "Total profit divided by winning trades", "Average win divided by average loss"], "correct": 1, "explain": "It is the probability-weighted average outcome, in dollars per share or in R."},
    {"q": "In the 30-session capstone window the rule earned +0.005R per trade but −$0.21 per share per trade. How can both be true?", "opts": ["A rounding error", "The losing trades had larger R (wider ranges) than the winning trades, so equal outcomes in R were unequal in dollars", "Costs were excluded from the R figure", "The R figure is computed on winners only"], "correct": 1, "explain": "Average R on losers was $2.12 versus $1.63 on winners. Sizing from the stop would have equalised dollars per R; a fixed share count did not."},
    {"q": "Thursdays in the 60-session sample won 16.7% and lost $19.77 per share on 12 trades. The correct response is:", "opts": ["Stop trading Thursdays", "Note it as a hypothesis to test on new data; with 12 trades and five weekday buckets, one bucket looking this bad is roughly what chance produces", "Trade Thursdays short only", "Double size on Tuesdays, which won 84.6%"], "correct": 1, "explain": "Splitting 60 trades into five groups guarantees that some group looks extreme. It is not evidence until it repeats out of sample."},
    {"q": "Which field is most often missing from a retail trading journal and most necessary for the capstone?", "opts": ["The entry price", "The cost per trade (spread, slippage, commissions), recorded per fill", "The ticker", "The date"], "correct": 1, "explain": "Without costs per trade, the journal computes gross expectancy, which is the number every losing day trader thinks they have."},
    {"q": "The standard error of the mean R over 30 trades with a standard deviation of 0.92R is about:", "opts": ["0.03R", "0.17R", "0.92R", "1.68R"], "correct": 1, "explain": "0.92 / sqrt(30) = 0.92 / 5.48 = 0.168R. Any mean expectancy smaller than about twice that is indistinguishable from zero."}
  ],
  "task": "Set up your journal with the fourteen fields in this lesson's table and back-fill it with the last five paper trades you took."
}
---

## Why the journal is the product

The setups in this course are hypotheses. The journal is the experiment. Without it you have a feeling about how you are doing, and the studies in lesson 1 are a catalogue of what happens to people who trade on that feeling. With it you have a number, an error bar and a decision rule.

The number is expectancy: the average outcome per trade, after costs, in R and in dollars. The error bar is its standard error. The decision rule is that a setup with an expectancy you cannot distinguish from zero is not yet a setup, no matter how it feels.

## Expectancy, defined and computed

Expectancy per trade = (win rate × average win) − (loss rate × average loss), where wins and losses are net of costs. Equivalently, it is the total net P&L divided by the number of trades. Compute it in R (dollars divided by the dollars risked on that trade) so that trades of different size are comparable, and in dollars per share so that you can see what the cost model is doing.

Its standard error is the standard deviation of per-trade outcomes divided by the square root of the number of trades. An expectancy less than about two standard errors from zero is not evidence of anything. That threshold is why the capstone asks for 30 sessions and why lesson 1 said even 60 was not enough for the reference rule.

## Worked example

The 30 capstone-window sessions, 2026-08-12 to 2026-09-23, reference opening-range rule (15-minute range, opposite-edge stop, 1R target, 15:55 exit, $0.02 cost). From the trade log in lesson 13:

16 winners, average net +$1.2444 per share. 14 losers, average net −$1.8743 per share.

Win rate = 16 / 30 = 0.5333. Loss rate = 0.4667.

Expectancy in dollars = 0.5333 × 1.2444 − 0.4667 × 1.8743 = 0.6637 − 0.8747 = −$0.211 per share per trade. Check against the total: net over 30 trades was −$6.33; −6.33 / 30 = −$0.211.

Expectancy in R: sum of R outcomes = +0.15R; 0.15 / 30 = +0.005R per trade.

The two signs disagree. The dollar figure is negative because the losing trades were, on average, larger trades: the average R (range width plus breakout distance) on the 14 losers was $2.12 per share, on the 16 winners $1.63. Each stop cost about 1.01R and each target paid about 0.99R, so in R terms the rule scratched; in dollars per share, with an implicit fixed share count, the wide-range losses outweighed the narrow-range wins. A trader sizing from the stop (lesson 7) would have experienced the R figure, roughly zero. A trader buying 100 shares every day would have experienced the dollar figure, −$633.

Standard error: the standard deviation of per-trade R was 0.921; 0.921 / sqrt(30) = 0.168R. Mean +0.005R is 0.03 standard errors from zero. This window says nothing about the rule's sign, and it is your reference answer for the capstone: an honest 30-session log will usually say exactly that.

Gross versus net: gross P&L was −$5.73; costs were 30 × $0.02 = $0.60; net −$6.33. Costs were 0.9% of the average R. If you had journaled gross only, you would have been wrong by $0.60 over 30 trades, which is nothing for this rule and everything for a scalp (lesson 5).

## The splitting trap

A journal with 60 rows invites you to slice it. Here is what slicing the 60-session reference log produces:

- By weekday: Monday 72.7% wins, +$12.10; Tuesday 84.6%, +$12.51; Wednesday 69.2%, +$11.46; Thursday 16.7%, −$19.77; Friday 45.5%, −$1.30.
- By entry time: by 10:00, 62.9% and +$13.17 on 35 trades; 10:05 to 10:30, 57.9% and +$2.97 on 19; after 10:30, 33.3% and −$1.14 on 6.
- By range width: narrowest third, 68.4%; middle third, 57.1%; widest third, 50.0%.
- By side: longs 60.0% on 25, shorts 57.1% on 35.

The Thursday result looks like a discovery: nine stops out of twelve trades. It is almost certainly not. Split 60 coin flips into five buckets of twelve and the worst bucket will often show two or three wins; the probability of 2 or fewer successes in 12 trials at p = 0.583 is about 0.5%, but you looked at five buckets and at least a dozen other ways of splitting, and the sample's first half was one long favourable stretch, so any bucket over-weighted in August and September looks bad. The right journal entry is "Thursday: hypothesis, 12 trades, revisit at 60 Thursdays," not a filter.

The entry-time split is different in kind, because lesson 2 predicted it before the data were cut: range and volume fade after the first hour, so late breakouts should do worse. A split that a prior mechanism predicts is worth more than one found by looking. It is still six trades.

## Table

The fourteen fields every row needs. The first nine are facts, recorded at the time; the last five are computed.

| Field | Example (2026-09-17) | Why it is there |
|---|---|---|
| Date | 2026-09-17 | |
| Setup name | OR15 breakout | Expectancy is per setup; mixed setups in one column measure nothing |
| Side | Short | Long/short splits |
| Range high / low | 763.41 / 760.40 | Reconstructs R and the target |
| Signal time and entry time | 10:05 close / 10:10 open | Entry-time splits; slippage |
| Entry, stop, target | 760.22 / 763.41 / 757.03 | |
| Shares (from the stop) | 47 at 0.5% of $30,000 | Confirms sizing was done from the stop |
| Exit time and price, outcome type | 15:50, 763.41, stop | Time-in-trade, exit-type statistics |
| Cost per share (spread, slippage, commission) | 0.02 | Net, not gross |
| Gross and net $/share | −3.19 / −3.21 | |
| Result in R | −1.01R | The unit everything else is measured in |
| MAE and MFE in R | 1.01R / 0.04R | Lesson 9's stop and target diagnostics |
| Rule followed? (yes/no, what deviated) | Yes | Separates the rule's statistics from yours |
| Running expectancy and standard error | after 26 trades: … | Tells you when you know something |

## Discipline fields

The "rule followed" column is the one that makes the rest honest. Odean's disposition-effect finding, that individuals sell winners too early and hold losers too long, shows up in a journal as time exits that should have been stops and targets taken at 0.6R. If you deviated, the row still counts for your account statistics but not for the setup's; keep both totals. Barber and Odean's "Trading Is Hazardous to Your Wealth" found that the households that traded most earned the least, and the mechanism was not bad setups, it was turnover. A journal that shows you took nine trades on a day the rule allowed one has found the same mechanism in you.

## When to act on the journal

After 30 trades: compute expectancy and standard error. If the mean is more than two standard errors below zero, stop the setup. If it is within two standard errors of zero, which is what the reference window produced, extend to 60. If it is more than two standard errors above zero, keep going and do not change the rule; changing a working rule resets the sample.

After 60: compare the two halves (lesson 12). A rule whose second 30 disagrees with its first 30 has told you something about itself that the total conceals.

At any point: if the "rule followed" column has more than three "no" entries in a month, stop counting the trades as evidence about the rule.

## Sources

- Terrance Odean, "Are Investors Reluctant to Realize Their Losses?" Journal of Finance 53(5), 1998: https://doi.org/10.1111/0022-1082.00072
- Brad Barber and Terrance Odean, "Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors," Journal of Finance 55(2), 2000: https://doi.org/10.1111/0022-1082.00226
- Yahoo Finance chart API, SPY 5-minute bars, 2026-06-30 to 2026-09-23, pulled 2026-09-24: https://finance.yahoo.com/quote/SPY/history/

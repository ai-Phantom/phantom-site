---
{
  "title": "Stops, Targets and Time Stops Intraday",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Among the reference rule's 30 winning trades, the median maximum adverse excursion before the target was hit was:", "opts": ["0.13R", "0.50R", "0.75R", "0.99R"], "correct": 0, "explain": "Winners rarely went far against the entry: median 0.13R, 75th percentile 0.25R, and 87% stayed under 0.5R."},
    {"q": "Moving the stop from the opposite edge of the range to its midpoint changed the 60-session net from +$15.00 to:", "opts": ["+$19.58", "+$7.33", "−$1.06", "+$15.00"], "correct": 1, "explain": "The tighter stop turned six extra trades into losses and cut the net roughly in half, with the longest losing streak rising from 4 to 6."},
    {"q": "Forcing an exit at 12:00 on any open trade changed the net from +$15.00 to:", "opts": ["+$5.68", "+$7.86", "+$12.11", "+$13.68"], "correct": 1, "explain": "Every earlier time stop reduced the sample's profit; the 15:55 exit was the best of those tested, though the differences are within noise."},
    {"q": "Why did the 2R target variant lose money while the 1R variant made money, using the same entries and stops?", "opts": ["Costs doubled", "Only 10 of 60 trades reached 2R, and 23 were still open at 15:55; the win rate fell to 45%, and 0.45 × 2.28 − 0.55 × 1.90 is negative", "The 2R variant had more stops", "Shorts were excluded"], "correct": 1, "explain": "A further target is hit less often; on this sample the fall in win rate outweighed the larger wins."},
    {"q": "On 2026-09-17 the short at 760.22 was stopped at 763.41 at 15:50 for −3.21. With a 12:00 time stop it would have exited at 762.34 for:", "opts": ["+2.12", "−2.14", "−3.21", "−1.06"], "correct": 1, "explain": "760.22 − 762.34 = −2.12 gross, −2.14 after the $0.02 cost: a smaller loss, but still a loss."}
  ],
  "task": "For your next five paper trades, record the maximum adverse and maximum favourable excursion in R alongside the outcome."
}
---

## Three exits, one trade

Every intraday trade ends one of three ways: the stop is hit, the target is hit, or time runs out. A rule that specifies only the entry is not a rule. This lesson uses the same 60-session SPY dataset (2026-06-30 to 2026-09-23, 5-minute bars, Yahoo Finance) to show what each exit choice did to the reference opening-range rule, and, more usefully, to show how to measure what your own exits are doing.

The reference exits: stop at the opposite edge of the 15-minute range, target one R from entry, exit at the 15:55 close if neither is touched. Over 60 sessions that produced 30 targets, 21 stops and 9 time exits, net +$15.00 per share after costs.

## Stops: where, and what the data says about tightening them

The stop's job is to define R, and R's job is to size the position (lesson 7). Where you put the stop therefore decides how many shares you hold, which is why "tighter is safer" is only half true: a tighter stop means more shares, so a stop that is hit by noise costs the same dollars as a wider one that is hit by being wrong.

Maximum adverse excursion (MAE) is the tool for looking at this. For each trade, measure how far price went against the entry before the trade resolved, in R. In the reference rule's 30 target-hitting trades, the median MAE was 0.13R, the 75th percentile 0.25R, and 87% of winners never went more than 0.5R against the entry. The largest was 0.99R, a winner that came within a cent of the stop. On the losing side, the 21 stopped trades had a median maximum favourable excursion (MFE) of 0.23R, and only 14% of them ever got as far as 0.5R in the trade's favour.

Read together, those numbers say the winners mostly went straight to work and the losers mostly went straight to the stop. That is what you would expect from a breakout: it either continues or it fails. It also says that a stop at half the range would have been hit by about 13% of the eventual winners, while saving nothing on the 86% of losers that never reached 0.5R of profit anyway. The empirical version confirms it: the midpoint-stop variant won 53.3% instead of 58.3%, netted +$7.33 instead of +$15.00, and its longest losing streak was 6 instead of 4.

That is one sample of one setup, and the lesson is the method, not the conclusion. Record MAE and MFE on every trade. If your winners routinely go 0.6R against you before working, your stop is too tight for your entry. If your losers routinely reach 0.7R of profit before reversing, a partial target or a break-even stop is worth testing.

## Targets: nearer and more often, or further and less often

The target sets the win rate. A target at 1R was hit on 30 of 60 trades; at 2R, on 10 of 60. Expectancy is the product of how often and how much, and the two move in opposite directions, so the only way to know which wins is to compute it.

## Worked example

Reference rule, 1R target, 60 trades: 35 winners (30 targets and 5 positive time exits) averaging +$1.83 net, 25 losers averaging −$1.96 net.

Expectancy = 0.583 × 1.83 + 0.417 × (−1.96) = 1.067 − 0.817 = +$0.25 per share per trade.

Same entries and stops, 2R target: 27 winners averaging +$2.28, 33 losers averaging −$1.90. Win rate 0.45.

Expectancy = 0.45 × 2.28 + 0.55 × (−1.90) = 1.026 − 1.045 = −$0.02 per share per trade.

The 2R variant's average win was 25% larger, but its win rate fell by 13 points, and 23 of its 60 trades were still open at 15:55, most of them having been at 1R profit at some point during the day and given it back. On this sample, the nearer target was worth $16 per share more over 60 sessions. That is not a law; the OR15 midpoint-stop variant did better with 2R than with 1R (+$19.58 versus +$7.33). It is a demonstration that target distance is a parameter that can flip the sign of a rule, and that you cannot choose it by intuition.

Now the time stop on a single trade. 2026-09-17: the short signal came on the 10:05 bar's close at 760.25, below the range low of 760.40; entry at the 10:10 open, 760.22; stop at the range high, 763.41; R = 3.19; target 757.03. Price never got within $2 of the target. It crossed back above VWAP by 10:20, drifted up through the afternoon, and the 15:50 bar's high of 763.57 took out the stop. Result: 760.22 − 763.41 = −3.19 gross, −3.21 net, the worst loss in the 60.

With a 12:00 time stop: the 12:00 bar closed at 762.34. Exit there: 760.22 − 762.34 = −2.12 gross, −2.14 net. The time stop saved $1.07 per share on that trade. Across all 60 trades, the same 12:00 rule reduced the net from +$15.00 to +$7.86, because on other days (2026-07-06, for instance, a long entered at 10:25 that reached its target at 14:55) it cut winners short. The single trade argues for the time stop; the sample argues against it; neither argument is statistically strong.

## Table

The reference rule's 60-session net under different forced-exit times. Each row exits any trade still open at that bar's close; stop and target are unchanged.

| Forced exit at | Net $/share | Win rate | Comment |
|---|---|---|---|
| 11:00 | +5.68 | 55.0% | Cuts most trades before they resolve |
| 12:00 | +7.86 | 56.7% | Saves 2026-09-17, loses 2026-07-06 |
| 13:00 | +12.11 | 55.0% | |
| 14:00 | +13.68 | 58.3% | |
| 15:55 (reference) | +15.00 | 58.3% | Best of the five on this sample |

Every earlier exit reduced the profit in this sample. The spread between rows is $9.32 per share over 60 trades, or about $0.16 per trade, which is smaller than the $0.27 standard error of the per-trade mean. The correct statement is "the data do not show a benefit from an intraday time stop for this rule," not "time stops hurt."

## Why time stops exist anyway

Lesson 2 showed that the session changes character around 11:30. A breakout trade is a bet on directional continuation while the first hour's volume carries it; by early afternoon it is a bet on something else. A time stop is the honest acknowledgement that the trade's premise has a shelf life. Its cost, as the table shows, is the occasional slow winner. Its benefit is not visible in P&L on a 60-session sample; it is visible in the tail. The 2026-09-17 trade tied up capital and attention for five and a half hours and then delivered the largest loss in the log. A trader who has watched that happen once tends to prefer a smaller loss at noon, and the sample gives no strong reason to argue with them.

There is a second reason. Odean's work on the disposition effect documents that individual investors hold losers longer than winners. An intraday time stop takes the holding decision away from the part of you that is hoping.

## Stops that are not price levels

Three more exits belong in a written rule, each of them tested the same way:

A break-even stop after the trade reaches some fraction of the target. On this sample, winners' MAE was small, so moving the stop to entry at 0.5R of profit would rarely have been triggered on eventual winners; it would have converted a few of the nine time exits from small losses into scratches. Untested here; test it.

A volatility stop, at some multiple of the recent bar range rather than at a chart level. It has the advantage of scaling with the day and the disadvantage of ignoring the range structure the setup is built on.

A rule stop: exit if you find you have moved any other stop. That one needs no backtest.

## What to carry into the capstone

Log the outcome type (target, stop, time), the MAE and MFE in R, and the time in trade for every session. With 30 rows you will be able to compute your own version of the table above and see whether your stops are being hit by noise, whether your targets are leaving money on the table, and whether your afternoons are paying for themselves. Those three questions are the ones that decide whether the exits need changing; the entry usually does not.

## Sources

- Terrance Odean, "Are Investors Reluctant to Realize Their Losses?" Journal of Finance 53(5), 1998: https://doi.org/10.1111/0022-1082.00072
- Kathryn Kaminski and Andrew Lo, "When Do Stop-Loss Rules Stop Losses?" Journal of Financial Markets 18, 2014: https://doi.org/10.1016/j.finmar.2013.07.001
- Yahoo Finance chart API, SPY 5-minute bars, 2026-06-30 to 2026-09-23, pulled 2026-09-24: https://finance.yahoo.com/quote/SPY/history/

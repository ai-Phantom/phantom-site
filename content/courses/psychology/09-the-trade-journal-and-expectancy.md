---
{
  "title": "The Trade Journal: What to Log, How to Review, and Expectancy as the Score",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Expectancy per trade, in R, is:", "opts": ["Win rate minus loss rate", "Total profit divided by winning trades", "Win rate x average win minus loss rate x average loss, equivalently total R divided by number of trades", "Average win divided by average loss"], "correct": 2, "explain": "It is the probability-weighted mean outcome. Both forms give the same number, which is a useful check on the arithmetic."},
    {"q": "A journal shows 40 trades: 22 wins averaging +1.1R and 18 losses averaging -1.0R. Expectancy and its standard error are about:", "opts": ["+0.155R and 0.167R", "+0.55R and 0.05R", "+0.10R and 0.01R", "-0.05R and 0.2R"], "correct": 0, "explain": "0.55 x 1.1 - 0.45 x 1.0 = 0.155R. The standard deviation of per-trade R is 1.058, so the standard error is 1.058 / sqrt(40) = 0.167R. The mean is under one standard error from zero."},
    {"q": "Seru, Shumway and Stoffman (2010) studied Finnish investors and found that:", "opts": ["Everyone improves with experience", "Some investors learn about their ability and stop trading, and the ones who continue improve only modestly; most of the 'learning' in the population is people quitting", "Nobody ever stops trading", "Experience makes everyone worse"], "correct": 1, "explain": "Learning by trading is mostly selection: people discover they are bad and leave. A journal is how you discover it in 100 trades rather than in your account balance."},
    {"q": "Which field is most often missing from a retail journal and most necessary for expectancy to be honest?", "opts": ["The ticker", "The date", "Whether the rule was followed, and the per-trade cost", "The entry price"], "correct": 2, "explain": "Without the adherence flag the journal measures a mixture of the plan and the doer's deviations; without cost it measures gross expectancy, which is the number every losing trader believes they have."},
    {"q": "A setup wins 80% of the time with average win 0.2R and average loss 1R. Its expectancy is:", "opts": ["+0.60R", "+0.16R", "0", "-0.04R"], "correct": 3, "explain": "0.8 x 0.2 - 0.2 x 1.0 = 0.16 - 0.20 = -0.04R. High win rates with small wins can be negative; the win rate alone is not the score."}
  ],
  "task": "Set up the fifteen-field journal from this lesson's table and back-fill it with your last ten trades, including the adherence flag and the cost for each."
}
---

## Why the journal is the only instrument

The studies in lesson 1 have a common feature: the traders in them did not know how they were doing. Barber and Odean's households believed they were beating the market and were 1.5 points behind it. The Brazilian day traders persisted for 300 days through losses that grew with time. The feeling of doing well and the fact of doing well are produced by different systems, and only one of them keeps records.

Seru, Shumway and Stoffman (2010) measured what happens when the records are the account balance itself. Using every trade by Finnish investors over seven years, they found that investors do learn, but mostly by discovering that they are bad and stopping; the ones who kept trading improved only slightly, and a large share of the "learning" visible in the population was this selection. The account balance is a slow, expensive and noisy journal. A written one with the right fields tells you the same thing in 100 trades instead of a career.

The journal has one output that matters, expectancy, and one qualifier, its standard error. Everything else in it exists to make those two numbers honest.

## Expectancy, defined

Expectancy per trade is the probability-weighted average outcome: win rate times average win minus loss rate times average loss, with wins and losses measured in R (dollars divided by the dollars risked on that trade) and net of costs. Equivalently it is the sum of all R outcomes divided by the number of trades. Compute it both ways; if they disagree, the arithmetic is wrong somewhere.

R is the unit for a reason lesson 3 gave: it makes trades of different size comparable and it makes the average-loss-to-average-win ratio visible. A journal kept in dollars alone will hide a disposition effect behind a few large winners. A journal in R shows it as an average loss above 1.0.

The standard error of expectancy is the standard deviation of the per-trade R outcomes divided by the square root of the number of trades. An expectancy less than two standard errors above zero is not yet evidence that the setup makes money; it is a number that a zero-edge setup produces a fair fraction of the time. Lesson 4 gave the same threshold for win rates. It is deliberately hard to meet, and the plan (lesson 7) should say that no size increase happens until it is met.

## What to log

Fifteen fields, nine recorded at the time and six computed. The table below lists them. Three deserve comment because they are the ones most journals omit.

Rule followed. Yes or no, and if no, which rule and how. This single field splits the journal into two records: the plan's performance and the doer's deviations. Without it, a plan with +0.20R expectancy traded by someone who widens one stop in five will show +0.05R and the trader will conclude the plan is weak. With it, you can compute expectancy on the rule-followed rows alone and on the deviations alone, and the deviations will almost always be the negative subset. That is the finding of lessons 2 through 6 in your own data.

Cost per trade. Spread, slippage against the intended price, commissions, and exchange or regulatory fees, recorded per fill. Lesson 1 showed cost is the variable that separated Barber and Odean's quintiles. A journal that records gross R computes a number that has never been the trader's actual result.

Maximum adverse excursion. The worst the trade went against you before it closed, in R. Across 50 trades this tells you whether your stop is at the right distance: if winners rarely see MAE above 0.5R, the stop can tighten and size can rise for the same dollar risk; if many winners see MAE near 1.0R, the stop is where it should be and any tightening would convert winners into stop-outs.

## Worked example

Forty trades from lesson 7's plan, all rule-followed, costs included.

Twenty-two winners, average net +1.1R (targets at 1.0R plus some positive time exits, less cost). Eighteen losers, average net -1.0R.

Win rate = 22 / 40 = 0.55. Loss rate = 0.45.

Expectancy = 0.55 x 1.1 - 0.45 x 1.0 = 0.605 - 0.450 = +0.155R per trade.

Check by the other route: total R = 22 x 1.1 - 18 x 1.0 = 24.2 - 18.0 = +6.2R; 6.2 / 40 = +0.155R. The two agree.

Standard error. Mean 0.155. Squared deviations: winners (1.1 - 0.155)^2 = 0.893 each, 22 of them = 19.65; losers (-1.0 - 0.155)^2 = 1.334 each, 18 of them = 24.01. Sum 43.66; divided by 39 = 1.1195; square root = 1.058R, the standard deviation of a single trade's outcome. Standard error = 1.058 / sqrt(40) = 1.058 / 6.325 = 0.167R.

Two standard errors = 0.335R. The measured +0.155R is 0.93 standard errors above zero. Conclusion: the setup has not yet shown a positive expectancy at the plan's standard; it has shown a number that a zero-expectancy setup produces about 18% of the time. To reach two standard errors at this mean and standard deviation needs n = (2 x 1.058 / 0.155)^2 = 186 trades. At the plan's pace of roughly one trade a day, that is nine months.

Dollars, for the account in lesson 7 with 1R = $320: +0.155R x 40 = +6.2R = +$1,984 over the 40 trades. Real money, and still not evidence. The journal's job is to hold both facts at once.

Now the split. Suppose the same 40 trades had included six deviations: four stops widened to 1.6R before being hit, two targets taken early at 0.5R. Rule-followed rows: 34 trades, 20 wins at 1.1R and 14 losses at 1.0R, expectancy (22.0 - 14.0) / 34 = +0.235R. Deviation rows: 6 trades, 2 wins at 0.5R and 4 losses at 1.6R, total 1.0 - 6.4 = -5.4R, expectancy -0.90R. Pooled: (8.0 - 5.4) / 40 = +0.065R. Without the adherence field the trader sees +0.065R and doubts the plan. With it, they see a +0.235R plan and a -0.90R doer, and the correction is obvious and cheap.

## Chart

![Expectancy in R per trade for seven win-rate and average-win pairs, with the average loss fixed at 1R: 30% at 3.0R and 40% at 2.0R both earn +0.20R, while 80% at 0.2R loses 0.04R. Computed from expectancy = p x W - (1 - p) x 1. Source: this lesson's formula.](figures/expectancy-by-win-rate-and-payoff.svg)

## The weekly review

The review is on a fixed day, from the journal, with the platform closed. It answers five questions in order, and it is over when they are answered.

How many trades this week, and were any outside the plan's hours or setups? Count them; they are deviations regardless of outcome.

Adherence rate: rule-followed rows divided by all rows. Below 90% means the plan is being traded by the doer, and no other statistic this week means anything. The fix is the devices in lesson 8, not the plan.

Running expectancy and standard error over the whole log, and over the rule-followed rows. Written down with n beside them, as "+0.155R (n = 40, SE 0.167)".

Average loss in R over the rule-followed rows. Above 1.05R means stops are slipping or being moved; either way it is the lesson 3 asymmetry starting.

Is any rule change permitted this month? Only if the plan's cadence allows it (one change, at 30 or more trades since the last), and only in the direction the numbers point. A change is a new plan version, dated, and the count restarts.

What the review does not do is react to the week's P&L. A week is five to ten trades; lesson 5 gave the standard error of that sample as 0.22 on the win rate. There is no weekly signal to react to, only a weekly opportunity to check that the process ran.

## The fifteen fields

| Field | Recorded or computed | Why it is there |
|---|---|---|
| Date and session time | Recorded | Time-of-day splits later; adherence to hours |
| Setup name and plan version | Recorded | Expectancy is per setup per plan version |
| Side, entry price and time | Recorded | Reconstructs the trade |
| Planned stop and target | Recorded | The R definition; compared with actual exits |
| Size, and the equity figure it was computed from | Recorded | Confirms the size rule ran |
| Exit price, time and exit type (stop, target, time, manual) | Recorded | Exit-type counts; manual is a deviation unless the plan allows it |
| Cost: spread, slippage, commissions, fees | Recorded per fill | Net, not gross |
| Maximum adverse and favourable excursion | Recorded | Stop and target diagnostics |
| Rule followed? If not, which and how | Recorded | Splits plan from doer |
| Gross and net dollars | Computed | |
| Result in R, net | Computed | The unit of everything else |
| Running win rate with n | Computed | Always shown with its sample size |
| Running expectancy, whole log and rule-followed | Computed | The score |
| Standard error of expectancy | Computed | Whether the score means anything yet |
| Running peak and current drawdown in R | Computed | Feeds the lesson 12 stop rule |

## Sources

- Brad M. Barber and Terrance Odean, "Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors", Journal of Finance 55(2), 2000: https://doi.org/10.1111/0022-1082.00226
- Amit Seru, Tyler Shumway and Noah Stoffman, "Learning by Trading", Review of Financial Studies 23(2), 2010: https://doi.org/10.1093/rfs/hhp060
- Brad M. Barber, Yi-Tsung Lee, Yu-Jane Liu and Terrance Odean, "Do Day Traders Rationally Learn About Their Ability?" (2014): https://faculty.haas.berkeley.edu/odean/papers/Day%20Traders/Day%20Trading%20and%20Learning%20110217.pdf

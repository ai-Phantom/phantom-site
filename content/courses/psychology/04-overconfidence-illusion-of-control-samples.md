---
{
  "title": "Overconfidence, the Illusion of Control, and How Sample Size Fools You",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A coin that lands heads 60% of the time is flipped 10 times. The probability it shows 4 or fewer heads is about:", "opts": ["1%", "5%", "17%", "40%"], "correct": 2, "explain": "Summing the binomial terms for 0 to 4 heads at p = 0.6 gives 0.166. One trader in six with a genuine 60% edge will look like a loser over 10 trades."},
    {"q": "A fair coin (50%) flipped 10 times shows 7 or more heads with probability:", "opts": ["17%", "5%", "1%", "30%"], "correct": 0, "explain": "P(7 or more) at p = 0.5 is 0.172. So a 70% win rate over 10 trades is about as likely from no edge at all as a 40% win rate is from a real 60% edge."},
    {"q": "To make a 60% win rate two standard errors away from 50%, you need roughly how many trades?", "opts": ["10", "30", "100", "1,000"], "correct": 2, "explain": "The standard error of a proportion is sqrt(p(1-p)/n). At n = 100 it is about 0.05, so a 10-point gap is two standard errors. At n = 10 the error is 0.16 and nothing can be concluded."},
    {"q": "Fenton-O'Creevy and colleagues (2003) measured the illusion of control in 107 professional traders and found that traders with higher illusion-of-control scores:", "opts": ["Earned more", "Had lower performance ratings from managers and lower total remuneration", "Traded less", "Showed no difference"], "correct": 1, "explain": "Believing you influence an outcome you cannot influence was associated with worse measured results, in professionals, not students."},
    {"q": "Barber and Odean's evidence that overconfidence drives trading is that:", "opts": ["Men traded 45% more than women and their extra trading reduced net returns by 2.65 points a year, against 1.72 for women", "Women traded more", "Trading frequency had no effect on returns", "Confident traders picked better stocks"], "correct": 0, "explain": "The group that psychological surveys rate as more overconfident in finance traded more and lost more from it, while gross stock selection was not better."}
  ],
  "task": "Write down the number of trades in your current record and the standard error of your win rate; if it is over 0.05, write 'not yet known' next to your win rate everywhere you have recorded it."
}
---

## Two errors that feel like knowledge

Overconfidence is the belief that your estimate is more precise than it is. The illusion of control is the belief that you influence an outcome you do not. Both are measured, both are found in professional traders, and both are amplified by a third thing that is not a bias at all but a piece of arithmetic: small samples produce results that look like information and are not. This lesson takes the two biases briefly, because the literature is clear, and then spends most of its time on the arithmetic, because the arithmetic is the part you can check.

## Overconfidence: Barber and Odean's test

Lesson 1 gave the "Boys Will Be Boys" result: in 35,000 households, men traded 45% more than women, and the extra trading cost men 2.65 percentage points a year in net return against 1.72 for women. The paper's contribution is not the gender finding but the logic. Psychological surveys had found men more overconfident than women specifically in domains like finance. Models of overconfident investors predict that they trade more, because each trade is a bet that their estimate is better than the market's, and that their extra trades lose after cost, because the estimate was not better. Both predictions came true in the data, and the gap was largest for single men, the group that surveys rate as most overconfident. Gross returns did not differ. The overconfidence did not make anyone a worse stock picker; it made them a more frequent one, and frequency cost.

The result generalises past gender. Any trader who trades because "this looks good" is expressing a confidence interval around their estimate, and the width of that interval is a fact about their record, not about their feeling.

## The illusion of control: Langer and the trading floor

Ellen Langer's 1975 experiments established the illusion of control: people behave as though skill matters in tasks that are pure chance, and the illusion grows when the task has skill-like features, such as choice, familiarity, competition and involvement. Subjects who chose their own lottery ticket demanded four times as much to sell it as subjects who were handed one. The tickets had identical odds.

Trading has every one of Langer's skill cues. You choose the instrument, the timing, the size; you are familiar with the chart; you compete; you are extremely involved. Mark Fenton-O'Creevy and colleagues tested the consequence in 2003 with 107 traders at four investment banks. They measured the illusion of control with a computer task in which subjects could press keys that had no effect on an index, and asked how much control they believed they had. Traders who scored higher on the illusion had lower performance ratings from their managers and lower total remuneration. These were professionals with years of experience and a firm's risk management behind them, and the effect was still there.

The trading implication is not that you have no control. You control your process entirely: the setups, the stop, the size, the routine. You control the outcome of any single trade not at all. Traders who confuse the two attribute wins to skill and losses to bad luck, which is the pattern that prevents a journal from teaching anything.

## The arithmetic of small samples

Here is why the two biases are so hard to correct from experience. Suppose you genuinely have a 60% win rate, which is a good edge, and you take 10 trades. The number of wins is a binomial random variable with n = 10 and p = 0.6. Its probabilities:

P(4 or fewer wins) = 0.166. P(exactly 5) = 0.201. P(6 or more) = 0.633.

So one time in six, a trader with a real 60% edge finishes 10 trades at 40% or worse and concludes the setup is broken. And one time in three, they finish at 50% and conclude they have no edge.

Now the reverse. A trader with no edge, p = 0.5, takes 10 trades:

P(7 or more wins) = 0.172. P(8 or more) = 0.055.

One in six no-edge traders will show 70% over 10 trades and conclude they are good at this. One in eighteen will show 80%. There are millions of retail accounts. The "gifted beginners" that every forum contains are, in expectation, the top 5% of a coin-flip distribution, and their next 10 trades will show it.

The general tool is the standard error of a proportion, sqrt(p(1 - p) / n). At p = 0.55: n = 10 gives 0.157; n = 30 gives 0.091; n = 100 gives 0.050; n = 400 gives 0.025. A win-rate estimate is worth about as much as two standard errors: over 10 trades, a measured 55% means "somewhere between 24% and 86%". Over 100, it means 45% to 65%. To distinguish 60% from 50% at two standard errors you need about 100 trades; to distinguish 55% from 50% you need about 400. Almost every retail trader's opinion of their own win rate is formed on fewer than 30 trades.

## Worked example

Take a $10,000 account, a trader who believes their win rate is 65% after 10 trades in which they won 7, and work out what can and cannot be concluded.

Step 1, the estimate. Measured win rate = 7 / 10 = 0.70. Standard error = sqrt(0.70 x 0.30 / 10) = sqrt(0.021) = 0.145. Two standard errors = 0.29. Interval: 0.41 to 0.99. The record is consistent with a 45% win rate and with a 95% one.

Step 2, the base rate. If the true win rate were 50%, P(7 or more of 10) = 0.172; if 45%, P(7 or more) = 0.102. So a losing setup produces this record about one time in ten. The record is weak evidence of an edge, not proof.

Step 3, what the trader did with it. Believing 65% and a 1:1 payoff, they computed expectancy 0.65 - 0.35 = +0.30R and raised size from 1% to 3% of the account, $300 risk per trade. If the true rate is 45%, expectancy is 0.45 - 0.55 = -0.10R = -$30 per trade at the new size. Over the next 50 trades: -$1,500, or 15% of the account, on a decision made from ten data points.

Step 4, what the rule would have done. A plan that fixes size at 1% until 100 logged trades show expectancy more than two standard errors above zero would have kept risk at $100 and the same 50 trades would have cost $500. The rule did not know the win rate either; it knew that nobody did, and priced that in.

Step 5, how long the evidence takes. At 10 trades a week, 100 trades is ten weeks. At the end, the standard error is 0.05 and a measured 60% is just about distinguishable from 50%. A measured 55% is not; that needs 400 trades, or 40 weeks. Any decision to scale up before then is a bet on the sample, not the setup.

## Table

Probability of a given number of wins in 10 trades, for three true win rates. Each column sums to 1.

| Wins in 10 | True rate 45% | True rate 50% | True rate 60% |
|---|---|---|---|
| 4 or fewer | 0.504 | 0.377 | 0.166 |
| exactly 5 | 0.234 | 0.246 | 0.201 |
| 6 or more | 0.262 | 0.377 | 0.633 |
| 7 or more | 0.102 | 0.172 | 0.382 |
| 8 or more | 0.027 | 0.055 | 0.167 |

Read across any row: a record of "6 or more of 10" is produced by a losing setup 26% of the time, by no edge 38% of the time, and by a real edge 63% of the time. The record barely separates them.

## What to do instead

The process answer has three parts. Fix the size by rule, so that overconfidence cannot express itself in the one variable that determines how much a bad estimate costs. Record every trade with its sample size beside the statistic, so the journal always says "55% (n = 23, SE 0.10)" and never "55%". And set the threshold for changing anything, up or down, in advance: lesson 9 uses two standard errors above zero on expectancy, which is a demanding standard that a 10-trade record can never meet. Langer's subjects could not be talked out of the illusion, and Barber and Odean's men did not become women. Your win rate is not a belief you hold; it is a number your journal will eventually know, and until it does, the plan's default is that you do not.

## Sources

- Brad M. Barber and Terrance Odean, "Boys Will Be Boys: Gender, Overconfidence, and Common Stock Investment", Quarterly Journal of Economics 116(1), 2001: https://doi.org/10.1162/003355301556400
- Ellen J. Langer, "The Illusion of Control", Journal of Personality and Social Psychology 32(2), 1975: https://doi.org/10.1037/0022-3514.32.2.311
- Mark Fenton-O'Creevy, Nigel Nicholson, Emma Soane and Paul Willman, "Trading on Illusions: Unrealistic Perceptions of Control and Trading Performance", Journal of Occupational and Organizational Psychology 76(1), 2003: https://doi.org/10.1348/096317903321208880

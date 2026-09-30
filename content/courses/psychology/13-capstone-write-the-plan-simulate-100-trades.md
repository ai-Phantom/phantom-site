---
{
  "title": "Capstone: Write a Complete Plan and Simulate 100 Trades",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The reference simulation (55% win rate, +1.2R wins, -1.0R losses, 100 trades) produced 53 wins and a final result of +16.6R. Its realised expectancy was:", "opts": ["+0.166R, below the stated +0.21R because 53 wins came up instead of the expected 55", "+0.21R, the stated value", "+0.53R", "-0.166R"], "correct": 0, "explain": "16.6 / 100 = 0.166R. The stated expectancy is what the process produces on average; any one 100-trade run lands somewhere around it. This one landed 0.4 standard errors below."},
    {"q": "The reference run's maximum drawdown was 8.8R, from a peak of +5.0R after trade 6 to -3.8R after trade 28. Against lesson 12's 12R rule, this run:", "opts": ["Would have stopped trading at trade 28", "Would not have triggered the rule; 8.8R is near the 75th percentile of healthy runs", "Would have triggered at trade 14", "Cannot be compared"], "correct": 1, "explain": "The 10,000-run simulation put the 75th percentile of maximum drawdown at 8.4R and the 95th at 12.8R. An 8.8R drawdown is ordinary for this system."},
    {"q": "The longest losing streak in the reference run was 5 (trades 94 to 98). Lesson 10's arithmetic says a streak of 5 or more in 100 trades at a 55% win rate has probability:", "opts": ["1.9%", "18%", "65%", "99%"], "correct": 2, "explain": "64.7%. A five-loss streak is more likely than not in any 100-trade record of this system. Its appearance at the end of the run is not evidence of anything."},
    {"q": "After the first 20 trades the reference run showed 9 wins (45%) and a cumulative -0.2R. A trader reading that as 'the setup does not work' would be:", "opts": ["Correct", "Following the drawdown rule", "Following the plan", "Making the lesson 4 error: at n = 20 the standard error of the win rate is 0.11, and 45% is under one standard error from 55%"], "correct": 3, "explain": "sqrt(0.55 x 0.45 / 20) = 0.111. The 20-trade start is uninformative; the same run finished at +16.6R without any rule changing."},
    {"q": "The rubric awards the most points to:", "opts": ["A profitable simulated result", "A complete, executable plan and correct, fully shown arithmetic, regardless of what the random draw produced", "The longest simulation", "The highest stated win rate"], "correct": 1, "explain": "The random draw is not under your control and carries no credit. The plan's completeness and the honesty of the statistics are."}
  ],
  "task": "Submit your written plan, your 100-trade simulation with the outcome sequence and the seed or method used, the four computed statistics with arithmetic shown, and a half-page on what your run does and does not show."
}
---

## The exercise

There are two parts. First, write a complete trading plan for one setup, in the nine-section form of lesson 7, precise enough that another person could place your orders. Second, simulate 100 trades of that plan from a stated win rate and payoff, and compute from the simulated sequence the four statistics the course has taught you to compute. Then write half a page on what the simulation shows and what it cannot.

Part one: the plan. Nine sections, each as if-then rules: markets and hours; the setup as at most three observable conditions; the entry order; the stop order, placed with the entry; the target and time stop; the size formula from prior-day equity; the daily limits (loss limit, trade cap, consecutive-loss pause); the review cadence and change rule; and the stop rule with its drawdown threshold, break length and return criteria. Include the streak table from lesson 10 for your stated win rate: the probability of at least one 5-, 7- and 10-loss streak per 100 trades.

Part two: the simulation. State a win rate p and an average win W in R, with the average loss fixed at 1R. Do not choose numbers you have not measured or cannot justify; if you have a journal, use its figures, and if not, use the reference values below and say so. Compute the stated expectancy, p x W - (1 - p) x 1. Then draw 100 outcomes: for each trade, draw a uniform random number and record +W if it is below p, otherwise -1. Any method is acceptable as long as it is reproducible: a spreadsheet's random function with the values pasted as fixed numbers, a programming language's generator with the seed stated, or a table of random digits with the page cited.

From the 100 outcomes compute, showing every step:

1. Realised expectancy: total R divided by 100, and also as win rate times average win minus loss rate times average loss, with the standard error (standard deviation of the outcomes divided by 10) and the number of standard errors between realised and stated expectancy.
2. The longest losing streak, with the trade numbers where it occurred, and the lesson 10 probability of a streak at least that long in 100 trades at your stated p.
3. The maximum drawdown in R, with the trade number of the peak and of the trough, and where it sits against your stop rule's threshold.
4. The equity curve: cumulative R after each trade, plotted or tabulated.

Then the half page: what the simulation demonstrates about variance, what it cannot demonstrate about your edge, and how your drawdown threshold and streak table were informed by it.

## Worked example

The reference answer: p = 0.55, W = 1.2R, average loss 1.0R.

Stated expectancy = 0.55 x 1.2 - 0.45 x 1.0 = 0.66 - 0.45 = +0.21R per trade.

The 100 outcomes were drawn in Python with random.seed(2026): for each trade, a uniform draw below 0.55 records +1.2, otherwise -1.0. The full sequence is in the course's figure script, figures/make_figures.py, and the first 20 outcomes are: +1.2, +1.2, +1.2, -1.0, +1.2, +1.2, -1.0, -1.0, -1.0, +1.2, -1.0, -1.0, -1.0, -1.0, +1.2, -1.0, +1.2, -1.0, +1.2, -1.0.

Result: 53 wins, 47 losses.

1. Realised expectancy. Total R = 53 x 1.2 - 47 x 1.0 = 63.6 - 47.0 = +16.6R. Divided by 100: +0.166R per trade. By the other route: win rate 0.53 x 1.2 - 0.47 x 1.0 = 0.636 - 0.470 = +0.166R. Agrees. Standard deviation of the 100 outcomes: 1.104R; standard error = 1.104 / sqrt(100) = 0.110R. The realised +0.166R is (0.166 - 0.21) / 0.110 = -0.40 standard errors from the stated value, and 0.166 / 0.110 = 1.5 standard errors above zero. Even with the true expectancy known to be +0.21R, this 100-trade run would not pass lesson 9's two-standard-error test. The win rate's own standard error is sqrt(0.53 x 0.47 / 100) = 0.050; 53% is 0.4 standard errors below the true 55%.

2. Longest losing streak: 5, at trades 94 to 98. There were also two four-loss streaks (trades 11 to 14 and 25 to 28) and three three-loss streaks. Lesson 10's recursion at q = 0.45, n = 100: P(at least one streak of 5 or more) = 64.7%. This run's worst streak is the median experience for the system.

3. Maximum drawdown: the curve peaked at +5.0R after trade 6 and troughed at -3.8R after trade 28, a drawdown of 5.0 - (-3.8) = 8.8R, spanning 22 trades. The account was below its trade-6 peak until trade 52 (+5.2R), 46 trades later. At 1% per R on a $25,000 account, 8.8R is $2,200 and the final +16.6R is $4,150. Against lesson 12's 12R rule the drawdown did not trigger; against the 10,000-run distribution (median 6.6R, 75th percentile 8.4R, 95th 12.8R), 8.8R sits just above the 75th percentile: an ordinary run.

4. The equity curve is the chart below. Note the first 20 trades: 9 wins, 45%, cumulative -0.2R. After 50 trades: 24 wins, 48%, cumulative +2.8R. A trader judging the setup at either point would have seen a below-stated win rate and a flat curve, and the standard error of the win rate at n = 20 is sqrt(0.55 x 0.45 / 20) = 0.111, at n = 50 it is 0.070. Neither observation was more than one standard error from the truth, and the plan, unchanged, finished at +16.6R.

What this run shows: the shape of variance for a system whose edge is known with certainty. A known +0.21R edge produced a 22-trade, 8.8R drawdown, a 46-trade stretch below the early peak, a five-loss streak at the end, and a first 50 trades at a 48% win rate. Every one of those would feel, in a live account, like evidence. None of them was.

What it cannot show: anything about whether a real setup has the stated edge. The simulation assumes p and W; the only instrument that estimates them is the journal, and lesson 9 gives the standard error that estimate carries. The drawdown threshold at 12R was informed by running this simulation 10,000 times, not once, and the once-run curve here is one draw from that distribution.

## Chart

![Cumulative R over the reference 100-trade simulation (55% wins, +1.2R / -1.0R, seed 2026): the peak at +5.0R after trade 6, the trough at -3.8R after trade 28 giving an 8.8R drawdown, the five-loss streak at trades 94 to 98, and the finish at +16.6R. Source: this lesson's worked example and figures/make_figures.py.](figures/capstone-equity-curve.svg)

## Rubric

Graded out of 100. The random draw carries no credit in either direction; a simulated loss with correct arithmetic and an executable plan scores higher than a simulated profit with either missing.

| Criterion | What earns full marks | Points |
|---|---|---|
| Plan completeness and executability | All nine sections present as if-then rules; another reader could place the orders; size formula from prior-day equity; stop and target as orders with the entry; daily loss limit, trade cap and pause stated in R and dollars; drawdown threshold, break and return criteria stated as numbers | 30 |
| Simulation reproducibility and correctness | p and W stated with justification; method and seed or fixed values given; 100 outcomes listed; win count matches the sequence; stated expectancy computed | 15 |
| Statistics with arithmetic shown | Realised expectancy by both routes with standard error and distance from stated; longest streak with trade numbers and the recursion probability; maximum drawdown with peak and trough trade numbers; equity curve tabulated or plotted | 25 |
| Interpretation | The half page states what the run shows about variance, what it cannot show about edge, and that no in-run observation (early win rate, streak, drawdown) justified a rule change; quotes the relevant standard errors | 20 |
| Threshold provenance | The drawdown threshold and streak table are derived from the stated p and W (by the recursion and by repeated simulation or the quoted percentiles), not chosen by feel, and the plan text says so | 10 |

## Sources

- Fernando Chague, Rodrigo De-Losso and Bruno Giovannetti, "Day Trading for a Living?" (2020), SSRN, for the base rate any plan is written against: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101
- Brad M. Barber and Terrance Odean, "Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors", Journal of Finance 55(2), 2000: https://doi.org/10.1111/0022-1082.00226
- Mark F. Schilling, "The Longest Run of Heads", College Mathematics Journal 21(3), 1990, for the run-length arithmetic behind the streak table: https://doi.org/10.2307/2686886

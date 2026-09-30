---
{
  "title": "When to Stop: The Drawdown Rule, the Break, and the Criteria to Return",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "An account that has drawn down 20% from its peak needs a gain of what percentage to recover?", "opts": ["25%", "20%", "40%", "50%"], "correct": 0, "explain": "Recovery = d / (1 - d) = 0.20 / 0.80 = 25%. At 30% the figure is 42.9%; at 50% it is 100%. The required gain grows faster than the loss."},
    {"q": "In 10,000 simulated 100-trade runs of a healthy system (55% wins, +1.2R / -1.0R), the share that reached a 12R drawdown was 6.6%. For the same system with the win rate broken to 45%, the share was:", "opts": ["6.6%", "12%", "About 51%", "100%"], "correct": 2, "explain": "A 12R rule fires on one healthy run in fifteen and on half the broken ones. That ratio is what makes it a usable stop rule: it is rarely wrong when it fires and it fires often when something is wrong."},
    {"q": "Chague, De-Losso and Giovannetti found that among Brazilian day traders, persistence:", "opts": ["Improved results", "Did not improve results; average losses grew with the number of days traded", "Had no measurable relationship to results", "Was rare"], "correct": 1, "explain": "The traders who kept going were not the ones who had learned; they were the ones who had not stopped. A stop rule is what the population lacked."},
    {"q": "Kandasamy and colleagues' finding that eight days of raised cortisol cut risk appetite by 44% is relevant to the break because:", "opts": ["It shows traders should take more risk after a drawdown", "It shows cortisol is harmless", "It shows drawdowns are caused by hormones", "It shows that the trader immediately after a drawdown has a measurably different risk preference from the one who wrote the plan, so decisions about the plan should wait until the break has ended"], "correct": 3, "explain": "Any judgement about whether the plan is broken, made during or just after the drawdown, is made by a physiologically different person. The break is there so the planner can return."},
    {"q": "The return criteria in this lesson require, before live trading resumes:", "opts": ["A feeling of readiness", "One winning paper trade", "Thirty paper trades of the same plan with 95% adherence and an expectancy not more than two standard errors below zero, then resumption at half size", "A new plan"], "correct": 2, "explain": "The criteria are written before the drawdown and are the same for every drawdown. They test the process, not the mood."}
  ],
  "task": "Write your drawdown rule as a number in R and a percentage of equity, your fixed break length in sessions, and your three return criteria, and add them as the final section of your plan."
}
---

## The rule that the losing population lacked

The Brazilian day traders in lesson 1 had one thing in common that the arithmetic of this course can name precisely: they had no stop rule. Each of the 1,551 who persisted past 300 days did so through a drawdown that, at some point, would have triggered any reasonable written threshold. None had written one. Seru, Shumway and Stoffman's Finnish investors did stop, eventually, but the stopping was done by the account balance, which is the most expensive stop rule there is.

The daily loss limit in lesson 6 caps a day. This lesson's drawdown rule caps a period: it is the point at which the plan itself, rather than the day, goes on trial. Three things have to be written in advance: the threshold, the break, and the criteria for coming back. Each is a rule for the same reason all the others are, and this lesson also gives the specific reason the decision cannot be left to the trader in the drawdown.

## Why the trader in the drawdown cannot decide

Kandasamy and colleagues (2014) raised cortisol in volunteers by 68% over eight days, the elevation seen in real traders across a volatile period, and risk appetite fell by 44%. The acute dose had no effect; the sustained one did. A trader two weeks into a drawdown is that subject. Whatever they conclude about their plan, "it is broken", "I need a new setup", "I should size down permanently", is a conclusion drawn by a person whose risk preference has moved by nearly half. When the cortisol comes down, the preference comes back, and the conclusion looks different. Decisions about the plan made in that window are made by the wrong party, exactly as lesson 7 said of rules written during the session.

The reverse failure is the one the Brazilian data show: the trader who does not stop because the drawdown does not feel like enough yet. Lesson 3's loss branch makes each additional loss feel smaller than the last; lesson 4's illusion of control attributes the run to bad luck; lesson 5's anchoring sets the goal at "back to the peak". Each of these votes to continue. The rule does not vote.

## The threshold

The drawdown rule is a peak-to-trough loss, in R, at which live trading stops. It is set from the plan's own variance, not from how much loss feels tolerable, and lesson 10's streak arithmetic is the input. The method is to simulate the plan as written, many times, and place the threshold where a healthy plan rarely goes and a broken one usually does.

For the capstone's system, 55% wins with +1.2R and -1.0R, expectancy +0.21R, 10,000 simulated runs of 100 trades give a median maximum drawdown of 6.6R, a 75th percentile of 8.4R, a 95th percentile of 12.8R and a 99th of 16.4R. Only 6.6% of healthy runs ever touch 12R. Now break the system: keep the payoffs and drop the win rate to 45%, expectancy 0.45 x 1.2 - 0.55 x 1.0 = -0.01R, a setup with no edge. Its median maximum drawdown over 100 trades is 12.0R, and 50.8% of runs reach 12R.

A 12R rule therefore fires on one healthy run in fifteen and on half of the broken ones over any 100-trade window. Those are the properties a stop rule needs: rarely wrong when it fires, and likely to fire when something is wrong. Set at 6R, it would stop the healthy plan more often than not; set at 20R, it would let a dead plan run for hundreds of trades. At 1% per R, 12R is a 12% drawdown, and the recovery arithmetic below is why it should not be larger.

## Worked example

Recovery arithmetic first, then the rule applied to an account.

A drawdown of d requires a gain of d / (1 - d) to return to the peak. At 5%: 0.05 / 0.95 = 5.3%. At 10%: 0.10 / 0.90 = 11.1%. At 20%: 0.20 / 0.80 = 25.0%. At 30%: 0.30 / 0.70 = 42.9%. At 40%: 0.40 / 0.60 = 66.7%. At 50%: 0.50 / 0.50 = 100%. The required gain is convex in the loss; every additional 10% of drawdown costs more to recover than the last.

Time to recover matters too. Lesson 9's plan earns +0.155R per trade at about one trade a day, and 1R is 1% of equity. From a 12% drawdown the required gain is 0.12 / 0.88 = 13.6%, or about 13.6R. At 0.155R per trade that is 88 trades, roughly four months, if the plan is healthy. From a 30% drawdown, 42.9R, or 277 trades, more than a year. A rule at 12R keeps the recovery inside a horizon over which the plan can also be re-verified; a rule at 30R does not.

Now the account. $32,000 at the peak, 1R = $320. Trades proceed; the running peak-to-trough drawdown is a journal field. It reaches 12R = $3,840, equity $28,160. The rule fires, that day, in the post-market block: no live orders from the next session. Size is not the issue, the plan is on trial.

The break: five sessions minimum with no live and no paper trades, screens off. Sleep and exercise logged. The plan is not edited during the break. This is the cortisol window; nothing decided in it counts.

The paper phase: 30 trades of the same plan, same rules, at the same size the plan would compute, executed and journalled exactly as live. Two numbers come out. Adherence: rule-followed rows over all rows. Expectancy with its standard error over the 30. Suppose the 30 paper trades show 16 wins at +1.1R and 14 losses at -1.0R: expectancy (17.6 - 14.0) / 30 = +0.12R; standard deviation about 1.06R; standard error 1.06 / sqrt(30) = 0.194R. Two standard errors below zero would be -0.39R; +0.12R is above that. Adherence 29 / 30 = 96.7%. Both criteria pass.

Return: live at half size, 0.5% per R = $141 on the $28,160 account, for 30 trades. If adherence stays at or above 95% and the whole-log expectancy has not fallen further, size returns to 1%. If the paper phase had failed on adherence, the fix is the lesson 8 devices, and another 30 paper trades. If it had failed on expectancy, with adherence high, the plan is the problem: one rule is changed, the plan version increments, and the count restarts from zero at paper. The drawdown rule and its 12R threshold do not change in any of these cases; they were set from the plan's variance and were right to fire.

Contrast with no rule. The trader continues from -12R. If the plan is healthy, the median outcome is recovery over about four months and the rule cost nothing but 35 sessions. If the plan is broken, -0.01R per trade with a 1R standard deviation, the account drifts with a widening spread: the 10,000 broken runs had a median further drawdown of 12R per 100 trades. Six months of that from $28,160 is roughly $22,000, a 31% total drawdown needing 45% to recover. The rule's cost is 35 sessions; its benefit, when it is right, is the account.

## Chart

![The stop rule as five steps: the written drawdown threshold is hit, live trading stops the same day, a fixed break with no screens, thirty paper trades of the unchanged plan, and return criteria on adherence and expectancy before resuming at half size. Source: this lesson's worked example.](figures/stop-rule.svg)

## The stop rule, written out

| Component | Written in the plan as | Set from |
|---|---|---|
| Drawdown threshold | "Live trading stops when peak-to-trough drawdown reaches 12R (12% of equity at 1% per R)" | The plan's simulated variance: 95th percentile of healthy 100-trade max drawdown is 12.8R; half of zero-edge runs reach 12R |
| Trigger mechanics | "Checked in the post-market block from the journal's drawdown field; fires the same day; no live orders from the next session" | Lesson 11's routine |
| Break | "Five sessions minimum, no live or paper trades, no charts; sleep and exercise logged; plan not edited" | Kandasamy's eight-day cortisol window; Lim and Dinges on attention |
| Paper phase | "Thirty trades of the unchanged plan, journalled as live, at the plan's computed size" | Lesson 4: 30 trades gives a standard error near 0.19R, enough to catch a badly broken plan, not a subtle one |
| Return criteria | "Adherence at least 95%; expectancy not more than two standard errors below zero; then 30 live trades at half size before full size" | Lesson 9's two statistics |
| If criteria fail | "Adherence failure: fix devices, repeat paper phase. Expectancy failure with high adherence: change one rule, increment plan version, restart paper phase" | Lesson 7's one-change cadence |

## Stopping is part of the plan

Every study in this course measured a population that did not stop, or stopped only when the account did it for them. The drawdown rule is the difference between a plan and a hope: a plan states the conditions under which it will be declared wrong, in advance, in numbers, and names the party who will decide. The party is the rule. The trader's job when it fires is to close the platform, take the break, and run the paper phase, which are all things the doer can do. Deciding whether the plan survives is the planner's job, and the planner is only available after the break.

## Sources

- Narayanan Kandasamy, Ben Hardy, Lionel Page, Markus Schaffner, Johann Graggaber, Andrew S. Powlson, Paul C. Fletcher, Mark Gurnell and John Coates, "Cortisol Shifts Financial Risk Preferences", Proceedings of the National Academy of Sciences 111(9), 2014: https://doi.org/10.1073/pnas.1317908111
- Fernando Chague, Rodrigo De-Losso and Bruno Giovannetti, "Day Trading for a Living?" (2020), SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101
- Amit Seru, Tyler Shumway and Noah Stoffman, "Learning by Trading", Review of Financial Studies 23(2), 2010: https://doi.org/10.1093/rfs/hhp060
- U.S. Securities and Exchange Commission, "Day Trading: Your Dollars at Risk": https://www.sec.gov/investor/pubs/daytips.htm

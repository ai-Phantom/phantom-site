---
{
  "title": "Recency, Anchoring and the Narrative Fallacy in a Live Tape",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In Tversky and Kahneman's 1974 anchoring experiment, subjects who saw a wheel stop at 10 estimated the share of African nations in the UN at a median of 25%; those who saw 65 estimated:", "opts": ["25%", "35%", "45%", "65%"], "correct": 2, "explain": "A number the subjects knew was random moved their estimates by 20 points. The entry price on your screen is a far more salient anchor than a wheel."},
    {"q": "The 'Linda' problem (1983) showed that about 85% of subjects rated 'bank teller and active feminist' as more probable than 'bank teller'. The error is called:", "opts": ["The conjunction fallacy: a more detailed story is judged more likely even though it must be less likely", "The gambler's fallacy", "Loss aversion", "Anchoring"], "correct": 0, "explain": "Adding detail to a story makes it feel more plausible while making it strictly less probable. A trade thesis with five supporting reasons is a conjunction."},
    {"q": "Chen, Moskowitz and Shue (2016) found that baseball umpires were about 1.5 percentage points less likely to call a strike immediately after calling one. This is evidence of:", "opts": ["The hot hand", "The gambler's fallacy in trained professionals making sequential decisions", "Fatigue", "Home-team bias"], "correct": 1, "explain": "The same pattern appeared in loan officers and asylum judges: after a run of one decision, professionals leaned the other way with no change in the underlying cases."},
    {"q": "The standard error of a win rate estimated from the last 5 trades at p = 0.55 is about:", "opts": ["0.05", "0.10", "0.45", "0.22"], "correct": 3, "explain": "sqrt(0.55 x 0.45 / 5) = 0.222. A recent five-trade streak tells you almost nothing about the rate, which is why the plan's statistics use the whole log."},
    {"q": "The process rule this lesson gives against anchoring on the entry price is:", "opts": ["Hide the P&L column", "Every exit decision is written in terms of the stop, the target and the time stop, none of which reference whether the position is currently up or down", "Only trade round numbers", "Average down to lower the anchor"], "correct": 1, "explain": "Hiding the P&L helps some people, but the reliable fix is that the rules never take the entry price as an input to any live decision."}
  ],
  "task": "Take your last losing trade and write the thesis you had at entry in one sentence; then count the separate claims in it and write the probability you would assign to each on its own."
}
---

## Three heuristics and where they enter

Tversky and Kahneman's 1974 paper in Science, "Judgment under Uncertainty: Heuristics and Biases", described three shortcuts that people use to estimate probabilities, and the errors each produces. Availability: things that come easily to mind seem more likely. Anchoring: an initial number pulls the estimate toward it. Representativeness: things that look like a category are judged to belong to it, regardless of base rates. Half a century of replication has not removed any of the three.

A live price feed is an unusually efficient machine for triggering all three. The last few bars are the most available thing in the world; your entry price is an anchor you cannot un-see; and every chart pattern is a representativeness judgement. This lesson goes through each with the original evidence, then a fourth failure, the narrative fallacy, that is what happens when the three combine into a story. The process answers are at the end, and they are the same shape as before: decisions that reference recent bars, the entry price or a story are moved out of the session and into rules written before it.

## Recency

Availability is the general bias; recency is its tape-specific form. What happened in the last five trades or the last five bars is vivid, and it drives estimates that should be made from the whole record.

The arithmetic from lesson 4 says how bad this is. The standard error of a win rate from n trades at p = 0.55 is sqrt(0.55 x 0.45 / n). For n = 5 it is 0.222; two standard errors is 0.44. A run of four wins in five, a measured 80%, is consistent with a true rate anywhere from 36% to 100%. A run of four losses in five is consistent with 0% to 64%. Neither run carries information about the rate, and both change behaviour: the first raises size and loosens entry criteria, the second lowers size and skips the next valid signal, which is the one trade that a 55% setup most needs you to take.

The mirror image is the gambler's fallacy, the sense that after a run one way the next outcome is "due" the other. The clearest evidence that professionals fall for this in sequential decisions is Chen, Moskowitz and Shue (2016). Baseball umpires were about 1.5 percentage points less likely to call a borderline pitch a strike if they had called the previous one a strike. Loan officers in a lending experiment were more likely to reject an application after approving the previous one. US asylum judges were less likely to grant a case after granting the previous one. In each setting the decisions should have been independent and the deciders were experienced. In a trade sequence, the fallacy shows up as "I've lost three, the next one has to work", which is lesson 6's opening move.

## Anchoring

The 1974 experiment is the one to remember because it is so stark. Subjects watched a wheel of fortune, rigged to stop at 10 or 65, and were then asked whether the percentage of African nations in the United Nations was higher or lower than that number, and then for their estimate. The median estimate was 25% for the group that saw 10 and 45% for the group that saw 65. The subjects knew the wheel was random. It moved their answer by 20 points anyway.

Your entry price is not random, and it is on the screen next to a red or green number every second. Lesson 2 showed what it does: the same stock at the same price is treated differently depending on a number the market does not know. The specific anchored decisions are: holding a loser "until it gets back to my price"; taking a winner because it has reached "a round number above where I got in"; and adding to a loser because the average entry price will be lower, which is anchoring squared, since it manipulates the anchor rather than the position.

The arithmetic of "getting back to my price" is worth one line. A stock bought at $100 and now at $92 must rise 100/92 - 1 = 8.7% for the anchor to be satisfied. Odean's held losers earned -1.06% excess over the following year. The anchor asks for 8.7%; the base rate offers -1.06%.

## Representativeness and the narrative fallacy

The representativeness heuristic judges probability by resemblance. Its most famous demonstration is the Linda problem from Tversky and Kahneman's 1983 paper. Subjects read a description of Linda, a 31-year-old philosophy graduate concerned with social justice, and ranked the probability of statements including "Linda is a bank teller" and "Linda is a bank teller and is active in the feminist movement". About 85% ranked the second as more probable than the first. It cannot be: every feminist bank teller is a bank teller, so the conjunction can never be more likely than either part. The detail made the story fit better and the probability worse.

A trade thesis is a conjunction. "Earnings beat, the sector is rotating in, the 50-day is turning up, volume confirmed, and the Fed is on hold" is five claims, and the trade needs all five to matter. If each is 80% likely to be true and to matter, the conjunction is 0.8^5 = 0.33. The thesis feels stronger with every clause added and is, arithmetically, weaker. This is the narrative fallacy in its tradeable form: a story that explains the chart is available, coherent and representative, and its coherence is not evidence.

The hot hand belongs here too. Gilovich, Vallone and Tversky (1985) showed that basketball fans and players believed strongly in streak shooting, and that shooting records showed no such dependence; a 2018 correction by Miller and Sanjurjo found a small real hot-hand effect once a subtle selection bias in the 1985 measurement was fixed. The lesson for a trader is the corrected one: streak perception is far stronger than streak reality, and the reality, if any, is small enough that no sizing rule should depend on it. Lesson 10 does the streak arithmetic.

## Worked example

A trader on a $30,000 account is long 200 shares of a stock bought at $50.00 with a planned stop at $48.50 and target at $53.00. Risk per share $1.50, total risk $300, which is 1%. The stock is at $48.80 after three red bars, and the last three trades in the journal were losers.

Recency. The journal has 64 trades at 56% wins before this run. Including the three losses: 36 / 67 = 0.537. Standard error = sqrt(0.537 x 0.463 / 67) = 0.061. The rate moved from 0.56 to 0.54, one third of a standard error. The three losses changed the estimate by an amount that is invisible at this sample size, and the plan's size rule, which references the whole-log expectancy, does not change.

Anchoring. The stock needs 50.00 / 48.80 - 1 = 2.46% to reach the entry. The plan does not contain the number 50.00 anywhere except as the price at which the 1R was defined; the exit rules are $48.50 and $53.00. "Back to even" is not an exit in the plan, so it is not an exit.

Narrative. The thesis at entry had four clauses. Assign each an honest 75%: 0.75^4 = 0.316. The stop was placed on the assumption that the setup wins about 55% of the time, which already includes the cases where the story was wrong. Nothing in the three red bars changes the story's probability more than the stop already assumes.

Decision. The stop at $48.50 stays. If it is hit, the loss is 200 x 1.50 = $300 = 1R, as planned. The alternatives the heuristics propose: widen the stop to $47.00 (risk becomes 200 x 3.00 = $600 = 2R, the lesson 3 asymmetry); add 200 shares at $48.80 to lower the average to $49.40 (risk becomes 400 x (49.40 - 48.50) = $360, plus the stop is now more likely to be hit on the larger size); or exit at $48.80 for -$240 because "three losers in a row means the market has changed" (a 0.8R loss taken on a five-trade sample). Each alternative references either the entry, the recent run or the story. The rule references none of them.

## Table

| Heuristic | Original evidence | Tape form | Rule that removes the input |
|---|---|---|---|
| Availability / recency | Tversky and Kahneman 1974; Chen, Moskowitz and Shue 2016 (umpires, 1.5 points) | Last 5 trades or last 5 bars drive size and entry | Size and setup criteria reference the whole-log expectancy, recomputed weekly, never intraday |
| Anchoring | Wheel at 10 vs 65 moved estimates 25% to 45% (1974) | "Back to my price"; averaging down; round-number targets | Exits are the stop, the target and the time stop, all set before entry; the entry price is not an input to any live decision |
| Representativeness / conjunction | Linda: 85% chose the conjunction (1983) | Multi-clause thesis feels stronger as it grows | The setup is defined by at most two or three observable conditions; extra reasons do not change size |
| Streak perception | Gilovich, Vallone and Tversky 1985; Miller and Sanjurjo 2018 | "I'm hot" or "I'm due" | Sequence has no place in the sizing rule; lesson 10's streak table is read before the session, not during it |

## The common shape

Every entry in the last column does the same thing: it takes a quantity that the heuristic acts on and removes it from the set of inputs to a live decision. The heuristics are not disputed and not fought; the studies say they cannot be. Recency is not an input to size because size is fixed from the whole log. The entry price is not an input to exits because exits were placed with the order. The story is not an input to anything because the setup is defined by observable conditions, and the story was never one of them. What is left for the live session is execution of rules whose inputs are all on the chart, none of them in your head.

## Sources

- Amos Tversky and Daniel Kahneman, "Judgment under Uncertainty: Heuristics and Biases", Science 185(4157), 1974: https://doi.org/10.1126/science.185.4157.1124
- Amos Tversky and Daniel Kahneman, "Extensional versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment", Psychological Review 90(4), 1983: https://doi.org/10.1037/0033-295X.90.4.293
- Daniel L. Chen, Tobias J. Moskowitz and Kelly Shue, "Decision Making Under the Gambler's Fallacy: Evidence from Asylum Judges, Loan Officers, and Baseball Umpires", Quarterly Journal of Economics 131(3), 2016: https://doi.org/10.1093/qje/qjw017
- Thomas Gilovich, Robert Vallone and Amos Tversky, "The Hot Hand in Basketball: On the Misperception of Random Sequences", Cognitive Psychology 17(3), 1985: https://doi.org/10.1016/0010-0285(85)90010-6

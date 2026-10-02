---
{
  "title": "Loss Aversion and Prospect Theory: The Arithmetic of Asymmetry",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In Tversky and Kahneman's 1992 estimate of the value function, the loss-aversion coefficient lambda was:", "opts": ["1.0", "1.5", "2.25", "4.0"], "correct": 2, "explain": "A loss of x is felt about 2.25 times as strongly as a gain of x. The curvature exponent for both gains and losses was 0.88."},
    {"q": "Using v(x) = x^0.88 for gains and -2.25(-x)^0.88 for losses, a $100 loss and a $100 gain are valued at about:", "opts": ["-100 and +100", "-129.5 and +57.5", "-57.5 and +129.5", "-225 and +100"], "correct": 1, "explain": "100^0.88 = 57.5; 2.25 x 57.5 = 129.5 with a minus sign. The loss is felt 2.25 times the gain."},
    {"q": "Prospect theory predicts that people are risk-seeking in the domain of losses. In trading, that shows up as:", "opts": ["Taking profits too early", "Widening a stop or adding to a losing position to avoid realising a sure loss", "Refusing to trade at all", "Buying only index funds"], "correct": 1, "explain": "The convex loss branch means a sure loss of 1R feels worse than a gamble between 0 and 2R with the same mean. The disposition effect and revenge trading both live on that branch."},
    {"q": "A trader wins 55% of the time but, by cutting winners at 1R and letting losers run to 2R, has an average loss twice the average win. Expectancy per trade is:", "opts": ["+0.10R", "0", "-0.35R", "-0.90R"], "correct": 2, "explain": "0.55 x 1R - 0.45 x 2R = 0.55 - 0.90 = -0.35R. The same 55% win rate with 1R losses would earn +0.10R."},
    {"q": "With average losses twice average wins, the win rate needed to break even is:", "opts": ["50%", "55%", "60%", "66.7%"], "correct": 3, "explain": "Break-even requires p x 1 = (1 - p) x 2, so p = 2/3. Few discretionary retail setups reach that; the asymmetry, not the win rate, is what wrecks the account."}
  ],
  "task": "Compute your own realised average win and average loss in R from your last 30 trades and state the ratio; if the ratio is below 1, write down which exit rule you broke most often."
}
---

## The measured shape of feeling

Daniel Kahneman and Amos Tversky published prospect theory in Econometrica in 1979, and it earned Kahneman the Nobel memorial prize in 2002. It is a description of how people actually value gambles, fitted to experimental choices, as opposed to the expected-utility model of how they should. Three features of it matter to a trader, and each has a number attached.

First, outcomes are valued relative to a reference point, not as total wealth. You do not feel your net worth; you feel the change from where you started, and "where you started" is usually the entry price. Second, the value function is concave for gains and convex for losses: the second $100 of gain feels smaller than the first, and the second $100 of loss also feels smaller than the first. Third, and most important, the loss branch is steeper than the gain branch. The 1992 follow-up, "Advances in Prospect Theory", fitted the function to a fresh set of choices and estimated the curvature at 0.88 for both branches and the loss-aversion coefficient, lambda, at 2.25.

Written out: v(x) = x^0.88 for a gain of x, and v(x) = -2.25 x (-x)^0.88 for a loss of x. Every behaviour in the first two lessons and most of the remaining ones can be read off that formula.

## What 2.25 does to a trader

Start with the disposition effect from lesson 2. A position showing a $500 loss is, in felt terms, at -2.25 x 500^0.88 = -2.25 x 237.1 = -533. Selling it converts a paper loss into a realised one, and prospect theory says the pain of that is already being carried; what the sale removes is the possibility of getting back to zero. On the convex loss branch, a gamble between a $1,000 loss and no loss at all is preferred to a sure $500 loss, even at equal expected value, because -2.25 x 1000^0.88 / 2 = -2.25 x 436.5 / 2 = -491, which is less bad than -533. So the trader holds, hoping. That is the whole mechanism of "riding losers", and it is not a character flaw; it is the shape of a curve that 1979 and 1992 experimental subjects, professional traders in later replications and almost every population tested since have shared.

Now the gain side. A position up $500 is valued at 500^0.88 = 237. A gamble between $1,000 and zero, equal odds, is valued at 1000^0.88 / 2 = 218. The sure gain wins. So the trader takes the $500 and the position goes on to $1,000 without them. That is "selling winners too early".

Put the two together and you have the trade shape Odean measured: small realised gains, large unrealised losses. Nothing in that description references the market. It is produced entirely by the reference point (the entry) and the curve.

## The arithmetic that wrecks expectancy

Here is the part that turns a psychology finding into an accounting one. Expectancy per trade is win rate times average win minus loss rate times average loss. Prospect theory does not change your win rate; the market decides that. What it changes, through the disposition effect, is the ratio of average win to average loss. It shrinks the wins and grows the losses.

Suppose a setup that, traded by rule with a 1R stop and a 1R target, wins 55% of the time. Expectancy = 0.55 x 1 - 0.45 x 1 = +0.10R per trade. Modest, positive, and enough to compound.

Now let the same setup be traded by someone acting out the curve: winners are taken at 1R as planned (concave gains make that easy), but losers are held to 2R before the pain of a bigger loss finally overcomes the hope of recovery. The win rate is unchanged at 55%. Expectancy = 0.55 x 1 - 0.45 x 2 = 0.55 - 0.90 = -0.35R per trade. A setup with a real edge is now losing a third of a risk unit every trade.

Break-even at a 2:1 loss-to-win ratio needs p x 1 = (1 - p) x 2, so p = 2/3, a 66.7% win rate. Very few discretionary retail setups have that; the day-trading and mean-reversion courses in this catalogue tested several and found win rates in the 50s. The asymmetry, on its own, is enough to turn every one of them negative.

## Worked example

Work through the value function and the expectancy consequences with full arithmetic.

Value of a $100 gain: 100^0.88. Take logs: 0.88 x ln(100) = 0.88 x 4.605 = 4.052; e^4.052 = 57.5. So v(+100) = +57.5.

Value of a $100 loss: -2.25 x 100^0.88 = -2.25 x 57.5 = -129.5. So v(-100) = -129.5.

The ratio |v(-100)| / v(+100) = 129.5 / 57.5 = 2.25, which is lambda, as it must be when the exponents match.

What gain offsets a $100 loss? Solve G^0.88 = 2.25 x 100^0.88, so G = 100 x 2.25^(1/0.88) = 100 x 2.25^1.136. ln(2.25) = 0.811; 0.811 x 1.136 = 0.921; e^0.921 = 2.51. G = $251. A 50/50 bet that loses $100 must pay about $251 before this trader is indifferent to it. That is a 2.5:1 payoff for a coin flip, and it explains why so many people refuse trades with a genuine 1.5:1 edge and take trades with none: the felt payoff and the actual payoff are different quantities.

Now the account. A $20,000 account risking 1% = $200 per trade, 55% win rate.

Traded by rule, 1R win and 1R loss: expectancy = 0.55 x 200 - 0.45 x 200 = 110 - 90 = +$20 per trade. Over 200 trades a year: +$4,000, or 20% of the account before costs.

Traded by the curve, 1R win and 2R loss: expectancy = 0.55 x 200 - 0.45 x 400 = 110 - 180 = -$70 per trade. Over 200 trades: -$14,000, or 70% of the account.

Same setup, same win rate, same trader. The $18,000 difference is one rule: the stop is entered with the order and is not moved. Compare that with the more common intermediate case, 1R win and 1.5R loss: expectancy = 0.55 x 200 - 0.45 x 300 = 110 - 135 = -$25 per trade, -$5,000 a year. Even a half-R of average slippage on the exit side turns the edge negative. Break-even for a 1:1.5 ratio is p = 1.5 / 2.5 = 60%.

## Chart

![The prospect-theory value function with Tversky and Kahneman's 1992 parameters (curvature 0.88, loss aversion 2.25): a $100 loss is felt as -129.5 and a $100 gain as +57.5, so the curve is steeper and convex on the loss side. Source: Tversky and Kahneman, Journal of Risk and Uncertainty 1992.](figures/prospect-theory-value-curve.svg)

## Reference points are chosen, so choose them

The entry price is the default reference point because it is the number you remember. But prospect theory says only that there is a reference point, not what it must be, and the choice is a process decision.

A trader who defines the trade at entry as "I have spent 1R to buy this outcome" has moved the reference point to entry minus the stop. From there, a stop-out is arriving at the reference point, not a loss below it, and the only outcomes above it are gains. The arithmetic of the account does not change; the felt value of the stop-out does, from -2.25 x 200^0.88 to roughly zero. This is not a trick. It is the same relabelling the tax code performed in December for Odean's investors, and it works for the same reason: it changes what the loss branch is measured from.

Two further consequences follow. Position size is a reference-point decision: at 1% risk, a stop-out is 1% of the account and the curve barely bends; at 10%, the felt loss is large enough that the convex branch dominates every decision, and moving the stop becomes almost irresistible. The risk-management course sets the size; this lesson gives the reason the size must be small enough that a full loss is dull. And the "get back to even" target is a reference-point error: the account does not know where even is, and a rule that references it (lesson 6 on revenge trading) is a rule written by the loss branch.

## What this does not say

Prospect theory does not say you can feel losses less by understanding the curve. Kahneman was explicit that knowing about a bias does little to remove it, and there is no study in which trained traders showed a lambda near 1. What it says is where the decision points are, and the lesson's answer is to move them: the stop and target are chosen when x = 0 and the curve is flat; the size is chosen so that the loss branch is never steep; and the reference point is written into the plan as "1R spent", not "price paid". The curve is left alone. The process routes around it.

## Sources

- Daniel Kahneman and Amos Tversky, "Prospect Theory: An Analysis of Decision under Risk", Econometrica 47(2), 1979: https://www.jstor.org/stable/1914185
- Amos Tversky and Daniel Kahneman, "Advances in Prospect Theory: Cumulative Representation of Uncertainty", Journal of Risk and Uncertainty 5, 1992: https://doi.org/10.1007/BF00122574
- Terrance Odean, "Are Investors Reluctant to Realize Their Losses?", Journal of Finance 53(5), 1998: https://doi.org/10.1111/0022-1082.00072

---
{
  "title": "Revenge Trading and Tilt: The Physiology and the Circuit Breaker",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Coates and Herbert (2008) sampled hormones from 17 London traders over eight business days and found that cortisol rose with:", "opts": ["The size of the day's loss", "The variance of the trader's P&L and with market volatility", "The time of day", "Testosterone"], "correct": 1, "explain": "Cortisol tracked uncertainty rather than loss: it rose when outcomes became more variable. A tilted session is a high-variance session, and the hormone response is to the variance."},
    {"q": "Kandasamy and colleagues (2014) raised subjects' cortisol by 68% over eight days, mimicking the rise seen in traders during volatility. Risk appetite:", "opts": ["Rose by 44%", "Was unchanged", "Fell by 44%", "Rose on day one, then fell"], "correct": 2, "explain": "Chronically elevated cortisol reduced willingness to take risk in a lottery task. A trader after a bad week is physiologically not the trader who wrote the plan."},
    {"q": "After 24 hours without sleep, Venkatraman and colleagues (2007) found that subjects making risky choices:", "opts": ["Became more cautious", "Showed elevated expectation of gains and a blunted response to losses", "Performed identically", "Refused to gamble"], "correct": 1, "explain": "Sleep loss shifted the brain's response toward gains and away from losses: the opposite of what a stop rule needs."},
    {"q": "A trader risks 1R, loses, doubles to 2R, loses, doubles to 4R and loses. At a 45% loss probability, the chance of that three-loss sequence and the day's result are:", "opts": ["9.1% and -7R", "20% and -3R", "45% and -4R", "2% and -12R"], "correct": 0, "explain": "0.45^3 = 0.091, and 1 + 2 + 4 = 7R lost. A 2R daily loss limit would have ended the day at -2R, with the same 9.1% chance of the sequence."},
    {"q": "The daily loss limit works as a circuit breaker because:", "opts": ["It improves your win rate", "It guarantees a profitable month", "It bounds the worst day to a written number and removes the decision to continue from a trader whose physiology has changed", "It is required by regulators"], "correct": 2, "explain": "Its value is not in the trades it prevents on average; it is in capping the tail day, which the sizing rule alone cannot do once size is being raised by feeling."}
  ],
  "task": "Write your daily loss limit as a number in R and in dollars, write what you will physically do when it is hit (close the platform, leave the desk), and tape it below your monitor."
}
---

## Tilt has a body

Poker players call it tilt; traders call it revenge trading. The pattern is the same: after a loss, or a run of losses, the person takes more risk, faster, with less regard for their rules, in order to recover. Every trader has done it and most describe it afterwards as if a different person had been at the keyboard. That description is closer to the truth than it sounds, because the physiology of the trader during a losing run is measurably different from the physiology of the trader who wrote the plan.

This lesson gives the evidence for that claim, then the arithmetic of what revenge trading costs, then the one process device that has any record of working: a daily loss limit, decided before the session, that ends the session without a vote.

## The hormone evidence

John Coates, a former derivatives trader, and Joe Herbert took saliva samples from 17 male traders on a London trading floor twice a day for eight business days and matched the hormone levels to each trader's P&L. Two findings. Testosterone was higher in the morning on days when the trader went on to make above-median profit, which is consistent with the hormone raising confidence and risk appetite. Cortisol, the stress hormone, did not track losses; it tracked the variance of the trader's P&L and the level of market volatility. Uncertainty raised cortisol, and it rose by a lot: in the most volatile stretch, some traders' cortisol rose several-fold over their own baseline.

Narayanan Kandasamy, Coates and colleagues then asked the causal question. They gave 36 volunteers hydrocortisone for eight days, raising cortisol by 68%, which was the average rise the trading-floor study had seen over a comparable volatile period. Risk appetite in a lottery task fell by 44%. A single acute dose did nothing; the chronic elevation did. The paper's own conclusion was that during a period of market stress traders become more risk averse, which can amplify a sell-off. For a retail trader the point is more local: after a stressful week, the person sitting down on Monday is not the one who wrote the plan, and the plan was written on the assumption that they were.

Lo and Repin (2002) measured the acute side. Ten professional foreign-exchange and derivatives traders wore sensors for skin conductance, heart rate, blood volume pulse and other autonomic measures during live trading. All ten showed significant physiological responses to market events such as volatility spikes and trend reversals. The less experienced traders showed larger responses. Whatever a trader believes about their own calm, their skin conductance is reporting otherwise, and the least experienced are reporting loudest.

## Sleep

Revenge trading is worse at the end of a bad day and much worse after a bad night. Vinod Venkatraman and colleagues (2007) had subjects make risky choices in a scanner after a normal night and after 24 hours of sleep deprivation. Sleep-deprived subjects showed elevated activation in reward regions when anticipating gains and reduced activation in the regions that respond to losses. Their choices shifted accordingly: more attention to what could be won, less to what could be lost. A stop rule requires the second thing to be working.

Lim and Dinges' 2010 meta-analysis of 70 studies found that short-term sleep deprivation degrades sustained attention most strongly, with reliable effects on working memory and processing speed. Sustained attention is what a session requires: watching for the setup and nothing else. The routine lesson (11) turns this into a rule about hours and screens; here it is one more reason the trader on tilt is not the plan's author.

## The arithmetic of getting it back

Revenge trading has a signature: size goes up after a loss. The mildest form is "I'm down 1R, I'll risk 2R on the next one so a win gets me to even". The full form is a martingale, doubling after each loss, and it is worth working through because the arithmetic is unambiguous.

Take a $25,000 account, 1R = 1% = $250, and a setup with a 55% win rate. The trader loses 1R, doubles to 2R, loses, doubles to 4R, loses. The probability of three consecutive losses is 0.45 x 0.45 x 0.45 = 0.091. The loss is 1 + 2 + 4 = 7R = $1,750, which is 7% of the account. If the fourth trade were also doubled to 8R and lost (probability 0.45^4 = 0.041), the day would be -15R, and a broker would probably decline the 16R attempt.

A trader who did not double but kept 1R and kept trading through the day would, after three losses, be at -3R with the same 9.1% probability. A trader with a 2R daily loss limit would be at -2R and finished, with the same probability. Over 250 trading days, three-loss openings happen about 23 times a year (250 x 0.091). At 7R each for the doubler, that is 160R a year lost on the bad openings alone, before any of the winning days count. At 2R each for the limit trader, it is 46R, and the remaining 227 days carry the +0.10R per trade edge.

## Worked example

Two traders with identical setups and accounts, one day, full arithmetic.

Account $25,000, 1R = $250, win rate 55%, 1:1 payoff, expectancy +0.10R = +$25 per trade by rule.

Trader A, no loss limit, doubles after losses. Trade 1: -1R (-$250). Trade 2 at 2R: -$500, running -$750. Trade 3 at 4R: -$1,000, running -$1,750. Trade 4 at 8R: wins, +$2,000, running +$250. Trader A ends the day up $250, having had $2,000 at risk on a single trade (8% of the account), and has learned that doubling works.

The expected value of that fourth trade was 0.55 x 2,000 - 0.45 x 2,000 = +$200, which is eight times the plan's +$25 because the size was eight times the plan's. The variance was 64 times the plan's. On the 45% of days the fourth trade loses, the day is -$3,750, 15% of the account, and a fifth trade at 16R ($4,000 at risk) is what the sequence demands.

Trader B, 2R daily loss limit. Trade 1: -$250. Trade 2 at 1R: -$250, running -$500 = -2R. Session ends. Platform closed by rule, not by decision.

Now the year. Assume each trader hits a two-loss opening on 0.45^2 = 20.25% of days, about 51 days a year, and a three-loss opening on 9.1%, about 23 days.

Trader B's worst day is -2R = -$500 every time, so the 51 two-loss days cost at most 102R, and on the other 199 days the plan's edge runs at about 4 trades a day: 199 x 4 x 0.10R = +80R. Net about -22R before the two-loss days' own partial recoveries, which is roughly break-even on this simplified accounting, and, more important, a maximum daily loss of 2% ever.

Trader A's 23 three-loss days, if each resolves like the example (a fourth trade at 8R that wins 55% of the time), contribute 23 x (0.55 x 250 - 0.45 x 3,750) = 23 x (137.5 - 1,687.5) = 23 x (-1,550) = -$35,650, which exceeds the account. The account does not survive the year, in expectation, regardless of the edge.

The difference between the two is not the setup, the win rate or the trader's understanding of statistics. It is that Trader B's session had an end condition written before it began.

## Table

| Device | What it fixes | Written as |
|---|---|---|
| Daily loss limit | Caps the tail day; removes the "continue?" decision from a trader whose cortisol and sleep state have changed | "Session ends at -2R realised or -2.5R including open positions, whichever first; platform closed; no re-entry until next session" |
| Maximum trades per day | Caps frequency, the Barber-Odean variable, when the loss limit is not hit but quality is falling | "Four trades maximum; the fourth is the last regardless of outcome" |
| Fixed size, no exceptions | Removes the only lever that revenge trading uses | "Risk per trade is 1% of prior-day closing equity, computed before the open, not adjustable intraday" |
| Consecutive-loss pause | Breaks the sequence before the limit | "After two consecutive losses, 20 minutes away from the screen before the next order" |
| Physical exit | Makes the limit real | "When the limit is hit, log the trades, close the platform, leave the desk. The rule is complete when the chair is empty" |

## Why a rule and not resolve

Every device in the table is dumb. None of them knows whether the next trade would have won, and on some days it would have. That is the point. The trader on tilt is, by the measurements above, higher-cortisol, more gain-focused, more autonomically aroused and less able to sustain attention than the trader who wrote the plan, and the plan's author is the only one of the two who should be making decisions. A rule written by the author and executed mechanically by the tilted trader is the mechanism by which the author stays in charge. Resolve is a resource of the tilted trader, and the studies say it is the resource most depleted.

Set the limit small enough that hitting it is boring: 2R is common, 3R is the upper end. A limit at 10R is not a circuit breaker; it is a description of a catastrophe. Lesson 12 extends the same idea from the day to the month.

## Sources

- John M. Coates and Joe Herbert, "Endogenous Steroids and Financial Risk Taking on a London Trading Floor", Proceedings of the National Academy of Sciences 105(16), 2008: https://doi.org/10.1073/pnas.0704025105
- Narayanan Kandasamy, Ben Hardy, Lionel Page, Markus Schaffner, Johann Graggaber, Andrew S. Powlson, Paul C. Fletcher, Mark Gurnell and John Coates, "Cortisol Shifts Financial Risk Preferences", Proceedings of the National Academy of Sciences 111(9), 2014: https://doi.org/10.1073/pnas.1317908111
- Andrew W. Lo and Dmitry V. Repin, "The Psychophysiology of Real-Time Financial Risk Processing", Journal of Cognitive Neuroscience 14(3), 2002: https://doi.org/10.1162/089892902317361877
- Vinod Venkatraman, Y. M. Lisa Chuah, Scott A. Huettel and Michael W. L. Chee, "Sleep Deprivation Elevates Expectation of Gains and Attenuates Response to Losses Following Risky Decisions", Sleep 30(5), 2007: https://doi.org/10.1093/sleep/30.5.603

---
{
  "title": "The Disposition Effect: Selling Winners, Holding Losers",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Odean (1998) measured the disposition effect by comparing:", "opts": ["The proportion of available gains that were realized (PGR) to the proportion of available losses that were realized (PLR)", "The number of winning trades to losing trades", "Average holding period of winners to losers", "Portfolio returns before and after a sale"], "correct": 0, "explain": "Counting sales alone would be biased by how many positions happened to be up. PGR and PLR divide realized gains and losses by the opportunities to realize them, day by day."},
    {"q": "Over the whole year in Odean's sample, PGR and PLR were:", "opts": ["0.098 and 0.148", "0.148 and 0.098", "0.50 and 0.50", "0.108 and 0.128"], "correct": 1, "explain": "13,883 / 93,541 = 0.148 for gains and 11,930 / 122,278 = 0.098 for losses: investors were about 1.5 times more likely to sell a winner than a loser."},
    {"q": "In December the pattern reversed (PGR 0.108, PLR 0.128). The best explanation is:", "opts": ["Investors learned in December", "Prices fell in December", "A data error", "Tax-loss selling gave investors an external rule that overrode the preference"], "correct": 3, "explain": "The reversal shows the behaviour is not fixed: when a rule (realise losses before year end for tax) exists, people follow it. The rest of the year, no rule exists, and the preference wins."},
    {"q": "Over the year following the sale, the winners Odean's investors sold outperformed the losers they kept by about:", "opts": ["0%", "3.4 percentage points (excess returns of +2.35% vs -1.06%)", "10 percentage points", "The losers recovered and did better"], "correct": 1, "explain": "The positions people were most eager to sell went on to do better than the ones they clung to. The preference was costly on top of being irrational."},
    {"q": "This lesson's answer to the disposition effect is:", "opts": ["Learn to tolerate losses emotionally", "Never sell a winner", "Place the stop and the target with the entry so that the exit is not a decision taken while the position is open", "Avoid looking at the P&L"], "correct": 2, "explain": "The behaviour appears when a live decision is made in the presence of an open gain or loss. Removing the decision removes the behaviour; willpower has no measured record of doing so."}
  ],
  "task": "For every open position you hold, write down the price at which you will exit if it goes against you and the price at which you will exit if it goes for you, and enter both as resting orders."
}
---

## The behaviour with the best evidence

Of every documented trading behaviour, the disposition effect has the longest and cleanest evidence trail, which is why it is the second lesson rather than the sixth. Hersh Shefrin and Meir Statman named it in 1985: the disposition to sell winners too early and ride losers too long. Terrance Odean measured it in 1998 in 10,000 discount-broker accounts. It has since been replicated in professional futures traders, in Finnish and Taiwanese and Chinese account data, in housing markets and in laboratory experiments.

It also has a clean fix, which is the point of this lesson. The behaviour happens when a person makes a live decision in the presence of an open gain or an open loss. If the exit is decided, and entered as an order, before the position exists, the live decision never happens. This is the first instance of the course's general claim: the answer to a bias is not to feel it less but to arrange the process so that the moment where it acts never arrives.

## How Odean measured it

The naive measurement, counting how many winners and losers people sold, does not work: in a rising market most positions are winners, so most sales will be winners whether or not anyone prefers them. Odean's method corrects for this. On every day an investor sold anything, he looked at every position in the account and classified each as a gain or a loss relative to its purchase price. A position sold at a gain is a realized gain; a gain-position not sold that day is a paper gain; the same for losses.

Over 1987 to 1993, across 10,000 accounts, the totals were 13,883 realized gains, 79,658 paper gains, 11,930 realized losses and 110,348 paper losses. From these come two ratios:

Proportion of gains realized, PGR = realized gains / (realized gains + paper gains).
Proportion of losses realized, PLR = realized losses / (realized losses + paper losses).

If investors were indifferent between selling winners and losers, the two ratios would be equal. They were not: PGR was 0.148 and PLR was 0.098. Given an opportunity to sell, investors took it 51% more often for a winner than for a loser.

Odean checked the obvious rational explanations. Rebalancing: if you sell winners to keep positions equal-weighted, you sell winners, but the effect survived excluding partial sales and sales followed by a repurchase. Transaction costs: losers trade at lower prices with wider proportional spreads, but the effect survived excluding low-priced stocks. Belief in mean reversion: perhaps the losers were expected to recover. That one is testable, and Odean tested it.

## The losers kept did worse

He followed the positions after the decision. Over the 252 trading days after a sale, the winners that investors sold earned an average excess return of +2.35%. Over the same horizon, the losers they held on to earned an average excess return of -1.06%. The difference is 3.41 percentage points a year, in favour of the positions people chose to get rid of. The preference for holding losers was not a bet on mean reversion that happened to be right; it was a bet that was systematically wrong.

The December result is the second thing to hold onto. In December alone, PGR fell to 0.108 and PLR rose to 0.128: investors were more likely to sell losers than winners. Nothing about their psychology changed in December. What changed was that an external rule, the tax code, gave them a reason to realise losses before year end, and they followed it. Rules beat preferences when rules exist. For eleven months of the year the investors had no rule, and the preference ran the account.

## Why it happens

Shefrin and Statman built the explanation from prospect theory, which is lesson 3, and from a mental-accounting idea: each position is a separate account opened at the purchase price. Closing an account at a loss forces the loss from "paper", where it can still be undone, into "realised", where it cannot. Closing at a gain locks in a success. Because losses are felt roughly twice as strongly as gains (lesson 3 gives the measured coefficient), the pain of closing the losing account is large enough that people pay a measured 3.4 points a year to postpone it.

Note what this account predicts. The behaviour is not about the stock. It is about the purchase price, a number the market does not know. A stock at $92 does not care whether you bought it at $100 or $80, yet Odean's investors treated the same stock at the same price completely differently depending on that irrelevant number. Lesson 5 returns to this as anchoring. For now, the trading implication is direct: any rule that references the entry price only through the pre-set stop and target, and never through "am I up or down", removes the variable that drives the effect.

## Worked example

Take the numbers from Odean's Table I and reproduce the headline ratios, then translate them into a per-year cost.

PGR = 13,883 / (13,883 + 79,658) = 13,883 / 93,541 = 0.1484.
PLR = 11,930 / (11,930 + 110,348) = 11,930 / 122,278 = 0.0976.
Ratio PGR / PLR = 0.1484 / 0.0976 = 1.52.

So on a day when the investor sold something, a winning position had a 14.8% chance of being the thing sold and a losing position a 9.8% chance.

Now the cost. Suppose a $50,000 account whose owner behaves like the sample, and that at any time half the account is in positions showing a loss that the owner is holding rather than selling. Odean's held losers earned -1.06% excess over the next year and the sold winners +2.35%. If the held-loser half had instead been rotated into the kind of position being sold, the swing is 3.41 points on $25,000 = $852 a year, before costs. It is not dramatic in any single year, which is exactly why it persists: nobody notices an $852 leak. Over ten years at that rate, the leak is $8,520 plus whatever it would have compounded to, on an account that started at $50,000.

Compare that with the cost of the fix. A resting stop order and a resting target order cost nothing to place at a US equity broker. The decision to place them takes about a minute at entry. The trade-off is $852 a year against one minute per trade.

Finally, the December check in the same units. In December PLR (0.128) exceeded PGR (0.108): ratio 0.84. The same people, when given a rule, realised losses 18% more readily than gains. The capacity to sell losers was there all year; only the rule was missing.

## Chart

![Odean (1998), Table I: over the whole year investors realized 14.8% of their available gains but only 9.8% of their available losses; in December, when tax-loss selling supplied a rule, the pattern reversed to 10.8% and 12.8%. Source: Odean, Journal of Finance 1998.](figures/disposition-effect-odean-1998.svg)

## The rule that removes the decision

The rule is short enough to write on the order ticket: no position is opened without a stop order and a target order, or a time exit, entered at the same moment as the entry, and none of the three is moved in the direction of more risk while the position is open.

Each clause targets a measured behaviour. "Entered at the same moment" means the exit is chosen when there is no open gain or loss to feel. "Stop order" rather than "mental stop" means the exit does not require a decision at the time the loss is showing; Odean's investors all had mental stops, presumably, and PLR was 0.098. "Not moved in the direction of more risk" closes the loophole by which a stop at $95 becomes a stop at $90 becomes a hold. Moving a stop closer, or a target closer, reduces risk and is permitted if your plan says so; moving either away is the disposition effect wearing a different coat.

Two objections come up. First, "stops get hunted." Whether that is true for your instrument is an empirical question for your journal (lesson 9), and if the answer is yes, the fix is a wider stop and a smaller size, not no stop. Second, "I want discretion to exit early." You can have it, if the plan writes the discretion as a rule: for example, exit if the position has not moved 0.5R in your favour within 20 bars. That is a time stop, it is set before entry, and it is not the disposition effect. What you cannot have is the option to decide, with a loss on the screen, whether this one is different. The data say you will decide that it is.

## Sources

- Terrance Odean, "Are Investors Reluctant to Realize Their Losses?", Journal of Finance 53(5), 1998: https://doi.org/10.1111/0022-1082.00072
- Hersh Shefrin and Meir Statman, "The Disposition to Sell Winners Too Early and Ride Losers Too Long: Theory and Evidence", Journal of Finance 40(3), 1985: https://doi.org/10.1111/j.1540-6261.1985.tb05002.x
- Martin Weber and Colin F. Camerer, "The Disposition Effect in Securities Trading: An Experimental Analysis", Journal of Economic Behavior and Organization 33(2), 1998: https://doi.org/10.1016/S0167-2681(97)00089-0

---
{
  "title": "Scalping Mechanics: Spreads, Ticks, Fill Quality, and Why Costs Decide Everything",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "With a 1:1 target and a round-trip cost equal to 10% of the risk per trade, the break-even win rate is:", "opts": ["50%", "52.5%", "55%", "60%"], "correct": 2, "explain": "p > (1 + c) / (T + 1) = (1 + 0.10) / 2 = 0.55."},
    {"q": "The median 5-minute bar range in the 60-session SPY sample was $0.50. What does that say about a $0.20 stop?", "opts": ["It is generous", "It is inside the noise of a single bar and will be hit by random movement", "It is only valid at the close", "Nothing; stops are independent of bar range"], "correct": 1, "explain": "No 5-minute bar in the sample had a range of $0.10 or less, and only 9.2% had a range of $0.25 or less."},
    {"q": "Raising the assumed round-trip cost on the reference opening-range rule from $0.02 to $0.10 per share changed its 60-session net from $15.00 to:", "opts": ["$14.80", "$10.20", "$5.00", "−$1.00"], "correct": 1, "explain": "Sixty trades at $0.10 is $6.00 of cost; 16.20 − 6.00 = 10.20. The rule survives because its average risk per trade is $2.18, so cost is a small share of R."},
    {"q": "Glosten and Milgrom explain the bid-ask spread as compensation for:", "opts": ["Exchange fees", "The market maker's risk of trading against better-informed counterparties", "Regulatory capital", "Clearing costs"], "correct": 1, "explain": "The spread exists because some counterparties know more; the market maker prices that adverse selection into the quote."},
    {"q": "Which of these is a cost the scalper pays even with zero commission?", "opts": ["The spread crossed on entry and exit plus any slippage", "Exchange data fees only", "Margin interest on overnight positions", "None; zero commission means zero cost"], "correct": 0, "explain": "Zero-commission brokers are paid through order routing; the spread and slippage are still paid by the trader on every round trip."}
  ],
  "task": "Look up your broker's per-share commission, exchange fees and any minimum ticket charge, and compute your true round-trip cost per share for a 100-share SPY trade."
}
---

## What a scalp is

A scalp is a trade that targets a few ticks or cents and holds for seconds to minutes. In SPY, the minimum price increment is one cent, the quoted spread is usually one cent during regular hours, and a scalper might target 10 to 30 cents with a stop of similar size. The appeal is obvious: the profit target is small, so it should be hit often. The problem is arithmetic, and it is the subject of this lesson.

Every round trip pays at least half the spread twice (once to buy at the offer, once to sell at the bid), plus any slippage on either side, plus commissions and fees if your broker charges them. On a trade risking $2, a 2-cent cost is 1%. On a trade risking $0.20, the same 2 cents is 10%. Same instrument, same cost, tenfold difference in what it does to your required win rate.

## Where the spread comes from

Glosten and Milgrom's 1985 model explains why the spread exists at all: a market maker who quotes a two-sided price will sometimes trade against a counterparty who knows something, and the spread is what compensates for that adverse selection. It follows that the spread is not a fixed toll; it widens exactly when information arrives, which is when scalpers most want to trade, and it is an underestimate of true cost because a marketable order can also walk through the displayed size.

Modern market making is automated. Menkveld's study of a high-frequency market maker found it participated in a large share of trades and earned its return from the spread while managing inventory tick by tick. That is your counterparty on most scalps. The relevant question is not whether you can out-read them but whether your expected move per trade exceeds what they collect from you on every crossing.

## The three components of cost

Spread: in SPY, typically $0.01 in regular hours. You pay half on entry and half on exit if you use market orders, so $0.01 round trip. If you post limit orders and get filled you may pay nothing, but you will be filled preferentially when price is moving against you (that is adverse selection again) and unfilled when it moves your way.

Slippage: the difference between the price you decided on and the price you got. For a 5-minute-bar strategy this is measurable: lesson 11 measures it at an average of $0.014 per share on the 60 opening-range entries when the decision is made at a bar close and the fill is the next bar's open. For a scalper reacting to the tape it is larger relative to the target and much harder to measure.

Commissions and fees: many US brokers charge no commission on equities; some charge $0.005 per share with a $1 minimum; exchange, SEC and FINRA fees add fractions of a cent on sales. The zero-commission brokers are paid by wholesalers through payment for order flow, which the SEC's order-handling disclosure rules require them to report. Zero commission does not mean zero cost; it moves the cost into the fill.

For the rest of the course the reference assumption is $0.02 per share round trip: a one-cent spread crossed once plus half a cent of slippage on each side. That is generous to a scalper and about right for a bar-based trader.

## Worked example

Cost as a share of risk decides the win rate you need. With target T (in units of R), risk 1R, and round-trip cost c (in units of R), a trade's expectancy is p × T − (1 − p) × 1 − c. Setting it to zero and solving:

p_breakeven = (1 + c) / (T + 1).

Scalp A: target $0.20, stop $0.20 (T = 1), cost $0.02 per share round trip. c = 0.02 / 0.20 = 0.10. p_breakeven = (1 + 0.10) / 2 = 0.55. You need to be right 55% of the time just to reach zero.

Scalp B: same trade at a broker charging $0.005 per share with a $1 minimum, so a 100-share order pays $1 each way, another $0.02 per share round trip. Total cost $0.04, c = 0.20, p_breakeven = 1.20 / 2 = 0.60.

Scalp C: target $0.10, stop $0.10, cost $0.02. c = 0.20, p_breakeven = 0.60. Now check the target against the data: the median 5-minute bar range in the 60-session SPY sample (2026-06-30 to 2026-09-23, Yahoo Finance) was $0.50, the 25th percentile was $0.35, and not one of the 4,680 bars had a range of $0.10 or less. A $0.10 stop is inside every single bar.

Reference opening-range rule (lesson 3): average risk per trade was $2.18 per share, so c = 0.02 / 2.18 = 0.0092. p_breakeven = 1.0092 / 2 = 0.505. Costs barely move the hurdle. The rule's measured win rate was 58.3%, comfortably above 50.5%; whether that is real is a separate question (lesson 1), but it is not a question about costs.

Now the empirical version. Re-running the reference rule over the same 60 sessions with different assumed costs:

- $0.00 per round trip: net +$16.20 per share
- $0.02: +$15.00
- $0.05: +$13.20
- $0.10: +$10.20

Each cent of cost per round trip costs exactly 60 cents over 60 trades. A rule with a $2 average R absorbs that. A rule with a $0.20 R would need to make ten times as many correct calls to pay the same toll.

## Chart

![Break-even win rate against round-trip cost expressed as a percentage of the risk per trade, for targets of 0.5R (a scalp with a wider stop than target), 1R and 2R. At 10% cost a 1R target needs 55%; a 0.5R target needs 73%. Computed from p = (1 + c) / (T + 1).](figures/cost-vs-win-rate.svg)

The three lines diverge as cost rises. The scalp line (0.5R target) starts at 67% with no cost at all and reaches 73% at 10% cost, which is why scalpers who target less than they risk need extraordinary hit rates. The 2R line starts at 33% and barely moves, which is why swing traders can be wrong most of the time and still be paid.

## Fill quality: the cost you cannot see on the statement

Your broker must give you best execution under FINRA Rule 5310 and report its order-handling practices under the SEC's disclosure rules, but "best" is measured against the national best bid and offer at the moment of routing, not against the price you saw on your screen a quarter-second earlier. Three things degrade fills for a scalper:

Queue position. A limit order joins the back of the queue at its price. At the open, lesson 2 measured roughly 7,300 shares per second trading in SPY; a few hundred shares ahead of you clear in a blink, but tens of thousands do not, and by the time you are at the front the price is often about to move away.

Adverse selection on limit fills. Your resting buy gets filled when someone is willing to sell down into it, which is disproportionately when price is about to fall further. Your fills are worse than a random sample of prices at that level.

Latency. Lesson 11 covers this. For now: if your quote is 500 milliseconds stale, every scalp decision is made on a market that no longer exists, and the counterparties who see the current market are the ones filling you.

## What this means for the course

Scalping SPY for dimes is, on the arithmetic above, a business with a 55% to 60% hurdle before a single edge is considered, using stops that sit inside the noise of one bar. That is why this course does not build a scalping playbook. It teaches the mechanics so that you can recognise when a setup's costs are a large fraction of its risk, and it directs the playbook and capstone toward the opening range, whose costs are under 1% of R on this data. If you want to scalp anyway, the test is the same as everywhere else in this course: 60 logged trades, expectancy after costs, and a confidence interval. Most scalpers never do that test because the answer is unpleasant.

## Table

Break-even win rate for common target-to-stop ratios and cost levels, from p = (1 + c) / (T + 1).

| Cost as % of R | Target 0.5R | Target 1R | Target 2R | Target 3R |
|---|---|---|---|---|
| 0% | 66.7% | 50.0% | 33.3% | 25.0% |
| 1% (reference OR rule) | 67.3% | 50.5% | 33.7% | 25.3% |
| 5% | 70.0% | 52.5% | 35.0% | 26.3% |
| 10% (20-cent scalp, 2-cent cost) | 73.3% | 55.0% | 36.7% | 27.5% |
| 20% (10-cent scalp, or 20-cent with commissions) | 80.0% | 60.0% | 40.0% | 30.0% |
| 50% | 100.0% | 75.0% | 50.0% | 37.5% |

## Sources

- Lawrence Glosten and Paul Milgrom, "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," Journal of Financial Economics 14(1), 1985: https://doi.org/10.1016/0304-405X(85)90044-3
- Albert Menkveld, "High Frequency Trading and the New Market Makers," Journal of Financial Markets 16(4), 2013: https://doi.org/10.1016/j.finmar.2013.06.006
- U.S. Securities and Exchange Commission, "Disclosure of Order Handling Information," Release No. 34-84528 (amendments to Rule 606), 2018: https://www.sec.gov/rules/final/2018/34-84528.pdf
- FINRA Rule 5310, Best Execution and Interpositioning: https://www.finra.org/rules-guidance/rulebooks/finra-rules/5310

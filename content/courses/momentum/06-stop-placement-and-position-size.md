---
{
  "title": "Stop Placement and What It Does to Size",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A 'technically valid' stop level is one that:", "opts": ["Is exactly 5% below the entry", "Sits below the price at which the setup is proven wrong, such as the breakout level or the consolidation low", "Is round-numbered so it is easy to remember", "Is as close as possible to the entry to minimise loss"], "correct": 1, "explain": "The stop marks the price at which the reason for the trade no longer exists. A fixed percentage ignores the chart; the tightest possible stop ignores normal noise."},
    {"q": "With a $50,000 account risking 1% per trade and the NVDA entry at 155.98, a stop at 147.94 gives a per-share risk of 8.04. How many shares?", "opts": ["500", "62", "27", "320"], "correct": 1, "explain": "$500 / 8.04 = 62.2, rounded down to 62 shares, a position of $9,671 or 19.3% of the account."},
    {"q": "Moving the stop from 147.94 to 137.50 on the same trade changes the position from 62 shares to 27. The trade later exits at 175.17. What happens to the dollar result?", "opts": ["It is unchanged because the exit is the same", "It falls from about $1,190 to about $518 because fewer shares were held", "It rises because the wider stop is safer", "It cannot be computed without knowing the commission"], "correct": 1, "explain": "Dollar profit is shares times the price gain: 62 × 19.19 = $1,189.78 versus 27 × 19.19 = $518.13. The wider stop did not change the outcome of this trade, only its size."},
    {"q": "Why does a stop order not guarantee the stop price?", "opts": ["Brokers ignore stops", "A stop becomes a market order once triggered, so on a gap it fills at the next available price, which can be far through the level", "Stops only work on options", "Stops expire at the close"], "correct": 1, "explain": "The SEC's description is explicit: a stop order becomes a market order when the stop price is reached, and the fill can differ substantially from the stop price in a fast or gapping market."},
    {"q": "In the LLY example, the breakout on 2026-01-07 was entered at 1113.69 with a stop at 1057.61. On which date did the stop get hit and what was the approximate loss on 8 shares?", "opts": ["2026-01-08, about $100", "2026-01-15, about $449", "2026-01-28, about $900", "It was never hit"], "correct": 1, "explain": "The stock traded to 1012.57 on 2026-01-15, through the 1057.61 stop. At the stop price the loss is 8 × 56.08 = $448.64, and the real fill would have been worse."}
  ],
  "task": "For the breakout you identified after lesson 5, write down three candidate stop levels (breakout level, breakout-bar low, consolidation low), the per-share risk of each, and the share count each implies at 1% of your account."
}
---

The stop is the only number in a trade that you control completely. You do not control where the stock goes, how fast, or whether it gaps. You do control the price at which you have agreed, in advance, that you were wrong. Everything else in position management flows from that price: the share count, the dollar exposure, the reward-to-risk ratio, and whether a normal pullback takes you out or not.

## What "technically valid" means

A technically valid stop sits just beyond the price at which the reason for the trade stops being true. For a breakout, the reason is that the stock has left its range. If it trades back into the range and keeps going, the breakout has failed, so the stop belongs below the breakout level. For a pullback to a rising average, the reason is that the average held, so the stop belongs below the pullback low. The chart tells you where the line is; you add a cushion for noise and put the order under it.

Three levels are usually available on a breakout, from tightest to widest:

- **Below the breakout bar's low.** The tightest choice. It assumes that a stock which has really broken out should not trade back through the day it did so.
- **Below the breakout level itself.** The level the stock cleared, which is the prior 20-day high. This is the most defensible line because it is the definition of the setup.
- **Below the consolidation low.** The widest choice. It says the trade is wrong only when the entire base is undercut.

An ATR-based distance (lesson 7) is not a fourth kind of level; it is a way to check that the level you chose is not inside the stock's normal daily noise. When the technical level and a 2-ATR distance agree, as they do in the example below, you have a stop you can defend twice over.

## From stop to size

The account risk per trade is a fixed fraction of equity. One percent is the standard in this course; a half percent is sensible while you are learning. Size follows from the stop, never the other way round:

risk per share = entry − stop
shares = (account × risk fraction) / risk per share
position value = shares × entry

A wide stop means fewer shares; a tight stop means more. This is why "I'll use a wide stop to be safe" is not safe in the way people mean. It reduces the chance of being stopped by noise and it reduces the payoff of every winner in the same proportion. The next section shows the trade-off in dollars on a real trade.

## Worked example

The trade is the NVDA breakout from lesson 5. Entry on 2025-06-26 at the open, **155.98**. The 14-day ATR on the breakout day was 4.02. The prior 20-day high was 147.96, the breakout bar's low was 149.26, and the consolidation low was 137.95 (2025-06-03). Data: Yahoo Finance daily bars, pulled 2026-09-24. The account is $50,000 and the risk per trade is 1%, so the dollar risk is $500.

Three stops, each a small cushion under its level:

**Stop A, 147.94.** Two ATRs under the entry: 155.98 − 2 × 4.02 = 147.94. This happens to sit two cents under the 147.96 breakout level, so it is both the ATR stop and the technical stop.
Risk per share = 155.98 − 147.94 = 8.04. Shares = 500 / 8.04 = 62.2, rounded down to **62**. Position = 62 × 155.98 = **$9,671**, or 19.3% of the account.

**Stop B, 148.90.** Under the breakout bar's low of 149.26.
Risk per share = 155.98 − 148.90 = 7.08. Shares = 500 / 7.08 = 70.6, so **70**. Position = 70 × 155.98 = **$10,919**, or 21.8%.

**Stop C, 137.50.** Under the consolidation low of 137.95.
Risk per share = 155.98 − 137.50 = 18.48. Shares = 500 / 18.48 = 27.06, so **27**. Position = 27 × 155.98 = **$4,211**, or 8.4%.

What happened: the lowest low between entry and the exit signal was 151.49 on 2025-07-01. None of the three stops was touched. The exit, by the trailing rule in lesson 8, came at the open of 2025-08-20 at **175.17**, a gain of 175.17 − 155.98 = 19.19 per share.

| Stop | Level | Risk/share | Shares | Position | P&L at 175.17 | R multiple |
|---|---|---|---|---|---|---|
| A: 2 × ATR (= breakout level) | 147.94 | 8.04 | 62 | $9,671 | $1,189.78 | 2.39 |
| B: breakout-bar low | 148.90 | 7.08 | 70 | $10,919 | $1,343.30 | 2.71 |
| C: consolidation low | 137.50 | 18.48 | 27 | $4,211 | $518.13 | 1.04 |

The R multiple is the gain divided by the risk per share: 19.19 / 8.04 = 2.39 for stop A. Same entry, same exit, same stock, and the choice of stop moved the result between $518 and $1,343. Stop C was never close to being hit, so on this trade its width bought nothing and cost $672 against stop A.

Now the other side. LLY closed above its 20-day high of 1088.48 on 2026-01-07 at 1108.09 with a rising 50-day average: a valid breakout by the lesson-5 rule. Entry at the next open, 2026-01-08, **1113.69**. ATR 28.04, so the 2-ATR stop is 1113.69 − 56.08 = **1057.61**. Shares = 500 / 56.08 = 8.9, so 8. The stock closed at 1085.19, 1063.56, 1081.00, 1077.19 and 1073.29 over the next five sessions, never touching the stop, and on 2026-01-15 it traded down to 1012.57, through it by 45 points. At the stop price the loss is 8 × 56.08 = **$448.64**; the real fill would have been lower still. Two weeks later LLY was at 1023.80. The tight stop C-style alternative, under the consolidation low, would have been hit too. Sometimes a breakout is simply wrong, and the stop's job is to make that cost one unit of risk rather than three.

## Gaps and what a stop order actually does

The SEC's investor education material describes a stop order plainly: once the stop price is reached, it becomes a market order and fills at the next available price. On a gap, that price can be far from the stop. The UNH gap of 2025-04-17, which opened 17.6% below the prior close, would have filled a stop placed 2 ATRs below entry at roughly 5.7 ATRs below it. Lesson 11 covers how to avoid holding through scheduled events; for unscheduled ones, the defence is the size rule. A 1% risk that becomes a 3% loss on a gap is unpleasant. A 5% risk that becomes 15% is how accounts end.

Stop-limit orders avoid the bad fill by not filling at all, which is worse for a swing trader holding a losing position. Use plain stops, keep them on the broker's server rather than in your head, and let the sizing rule absorb the gap risk.

## Where the stop goes after entry

At entry, the stop is technical. After entry, it can move only in the direction of the trade, and only for a reason defined in advance. The trailing rule in lesson 8 is one such reason. "It feels like it's turning" is not. A stop that moves toward the entry after a bad day is a decision to take a smaller loss than you agreed to, which sounds prudent and is actually a refusal to let the trade have the room you sized it for.

The single most common failure in swing trading is not a bad stop level. It is a good stop level that was cancelled.

## Sources

- U.S. Securities and Exchange Commission, Investor.gov glossary: Stop order. https://www.investor.gov/introduction-investing/investing-basics/glossary/stop-order
- U.S. Securities and Exchange Commission (2011). Trading Basics: Understanding the Different Ways to Buy and Sell Stock. https://www.sec.gov/investor/alerts/trading101basics.pdf
- Odean, T. (1998). Are investors reluctant to realize their losses? *Journal of Finance*, 53(5), 1775–1798. https://doi.org/10.1111/0022-1082.00072
- Yahoo Finance historical data, LLY: https://finance.yahoo.com/quote/LLY/history/

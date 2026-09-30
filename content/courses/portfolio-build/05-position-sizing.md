---
{
  "title": "Position Sizing",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Account $25,000, risk per position 1%, entry $50, stop $45. How many shares does the risk-per-trade formula give?", "opts": ["25", "50", "100", "500"], "correct": 1, "explain": "Dollar risk = 25,000 × 1% = $250. Risk per share = 50 − 45 = $5. Shares = 250 ÷ 5 = 50, a $2,500 position or 10% of the account."},
    {"q": "Same account and 1% risk, but the stop is at $47.50 (5% below entry). The formula gives 100 shares, a $5,000 position. Why should a maximum-weight cap still apply?", "opts": ["Because 100 shares is an odd number", "Because a tighter stop only limits the loss if the stop executes; a gap through the stop or a permanent-loss event exposes the full 20% weight", "Because the broker requires it", "Because the formula is wrong"], "correct": 1, "explain": "Risk-per-trade sizing assumes the exit happens at the stop. Overnight gaps, halts and fraud do not honour stops, so a separate cap on position weight is the second line of defence."},
    {"q": "After 10 consecutive losing positions, an account risking 1% per position retains about 90%. At 5% per position it retains about", "opts": ["50%", "60%", "75%", "95%"], "correct": 1, "explain": "0.95^10 = 0.599, so about 60% remains, and recovering needs a 67% gain. At 1% the recovery needed is only 11%. Small per-position risk keeps a losing streak survivable."},
    {"q": "With a 55% win rate and 1:1 payoff, the full Kelly fraction is 10%. Why do most practitioners size at a fraction of Kelly?", "opts": ["Kelly is illegal", "Because win rate and payoff are estimates; over-estimating them makes full Kelly ruinous, and half Kelly gives up little growth for far less variance", "Because Kelly only works for coin flips", "Because brokers cap position sizes at 5%"], "correct": 1, "explain": "Kelly maximises long-run growth only if the inputs are exactly right. Betting more than Kelly reduces growth and raises ruin risk sharply, so uncertainty about the inputs argues for staying well below it."},
    {"q": "Fixed-fractional sizing means", "opts": ["Buying a fixed number of shares each time", "Each position is a fixed percentage of current account value, so size scales down after losses and up after gains", "Never selling", "Sizing by the stock's price"], "correct": 1, "explain": "Sizing to a fixed fraction of current equity is self-correcting: it automatically reduces exposure in a drawdown and increases it as the account grows."}
  ],
  "task": "Compute the risk-per-trade size for one stock you are considering, using 1% of your account and a stop you would honour, and compare it to your maximum position weight."
}
---

## The question sizing answers

You have decided a holding belongs in the portfolio. The next question is how much, and it is the question beginners skip most often. They decide whether to buy, then buy an amount that feels right: $1,000 because it is round, or 100 shares because that is a lot, or "about the same as the others." None of those is a sizing rule, and the absence of a rule is how one position ends up at 35% of the account.

Sizing is the mechanism that connects the risk budget from lesson 1 to the individual positions. There are two families of rule. Both work. The mistake is to use neither.

## Fixed-fractional sizing

The simplest rule: each position is a fixed percentage of current account value. Ten positions at 10% each, or a core fund at 60% and eight satellites at 5% each. When you add money or the account grows, the percentages stay the same and the dollars scale.

Fixed-fractional sizing is self-correcting in a drawdown. If the account falls 20%, every new position is sized 20% smaller in dollars, which is what you want when things are going badly. It also has a built-in cap: no position can exceed its fraction at purchase, and rebalancing (lesson 8) pulls it back if it grows past.

What fixed-fractional does not do is adjust for how risky each holding is. A 10% position in a bond fund and a 10% position in a small biotech are the same dollars and very different risks. For the core of a portfolio, where the holdings are broad funds, this does not matter much. For individual stocks it does, which is what the second family handles.

## Risk-per-trade sizing

The risk-per-trade rule starts from the loss you will accept on this one position if it goes wrong, and works backwards to the number of shares.

Shares = (Account value × Risk per position) ÷ (Entry price − Stop price)

The "risk per position" is typically 1% to 2% of the account. The stop is the price at which you have decided, in advance, that the reason you bought no longer holds. The distance from entry to stop is your risk per share. Divide the dollar risk by the risk per share and you have the position size.

This is the "1% rule" or "2% rule." What it means is not "put 1% of the account in each stock." It means "size each position so that if it hits its stop, the account loses 1%." A wide stop produces a small position; a tight stop produces a large one.

## Worked example

Account: $25,000. Risk per position: 1%, so $250. You want to buy a stock at $50 with a stop at $45.

**Step 1: dollar risk.** 25,000 × 0.01 = $250.

**Step 2: risk per share.** 50 − 45 = $5.

**Step 3: shares.** 250 ÷ 5 = 50 shares.

**Step 4: position value.** 50 × $50 = $2,500, which is 10% of the account.

If the stop is hit you lose 50 × $5 = $250, exactly 1%. If the stock instead rises to $60, you gain $500, 2% of the account, for a 2:1 payoff on the risk taken.

**Now tighten the stop to $47.50.** Risk per share is $2.50. Shares = 250 ÷ 2.50 = 100. Position value = $5,000, 20% of the account.

The risk-per-trade formula is satisfied: a stop at $47.50 loses $250. But the position is now a fifth of the account, and the formula's assumption is that you will get out at $47.50. Stocks gap. A company that reports bad earnings after the close can open 25% lower, and your stop executes at $37.50, a loss of $1,250 or 5% of the account. A fraud, a delisting or a halted stock can take the whole position.

So the second rule applies alongside the first: **no position larger than a stated maximum weight**, typically 5% to 15% for individual stocks in a first portfolio. With a 15% cap, the maximum here is $3,750 or 75 shares, regardless of what the stop formula says. You take the smaller of the two numbers, always.

**What the two rules are protecting.** The risk-per-trade rule protects against the ordinary case: the thesis was wrong and the stop takes you out with a small, planned loss. The weight cap protects against the extraordinary case: the exit you planned does not happen. Bessembinder's finding from lesson 2, that most individual stocks lose to T-bills over their lives, is the reason both are needed.

## Why 1% to 2% and not more

The case for small per-position risk is a losing streak, and losing streaks are normal. A strategy with a 55% win rate will produce five consecutive losses about 1.8% of the time per sequence of five, which over a hundred positions means you should expect to see it. Ten in a row is rarer but not rare enough to ignore.

The table below shows what a run of ten losses does at different risk levels, and what gain is needed to get back to even afterwards.

## Table

| Risk per position | Equity after 10 straight losses | Gain needed to recover | Equity after 20 straight losses |
|---|---|---|---|
| 0.5% | 0.995^10 = 95.1% | 5.1% | 90.5% |
| 1% | 0.99^10 = 90.4% | 10.6% | 81.8% |
| 2% | 0.98^10 = 81.7% | 22.4% | 66.8% |
| 5% | 0.95^10 = 59.9% | 67.0% | 35.8% |
| 10% | 0.90^10 = 34.9% | 186.7% | 12.2% |

At 1%, ten losses in a row is a bad quarter you recover from. At 5% it is a catastrophe that requires a 67% gain just to get back to zero, and at 10% the account is functionally gone. The gap between 1% and 2% is real but survivable; the gap between 2% and 5% is the difference between a plan and a gamble.

## The Kelly criterion, briefly

There is a formula for the position size that maximises long-run growth, derived by John Kelly in 1956 and applied to markets by Edward Thorp. For a bet that wins with probability p and pays b dollars per dollar risked when it wins:

Kelly fraction = p − (1 − p) ÷ b

With p = 0.55 and b = 1 (you win as much as you lose), the fraction is 0.55 − 0.45 ÷ 1 = 0.10, so 10% of the account risked per position.

That is far more than 1%. Two reasons practitioners do not use it. First, the formula assumes you know p and b, and you do not; you have estimated them from a small sample, and if the true win rate is 50% rather than 55%, the Kelly fraction is zero and betting 10% is destroying capital at the fastest possible rate. Second, even at the correct fraction, full Kelly produces drawdowns most people cannot hold: a 50% drawdown has meaningful probability. Half Kelly gives up about a quarter of the growth rate for roughly half the variance, and quarter Kelly is closer to what most disciplined traders actually run. The 1% to 2% rule is, in effect, a fractional Kelly for someone honest about not knowing their edge.

## Putting the rules together

For the core: fixed-fractional. Decide the percentages, buy those percentages, rebalance back to them.

For each satellite position:

1. Write the stop, meaning the price at which the reason for owning it is invalid.
2. Compute shares from the 1% (or 2%) rule.
3. Compute the maximum shares from the weight cap.
4. Buy the smaller.
5. Record the entry, the stop, the share count and the dollar risk in one line.

Step 5 is not clerical. A position whose stop is not written down does not have a stop; it has a hope. Lesson 10 covers why the written version is the only one that survives contact with a red screen, and lesson 12 makes the rules part of your plan.

## Sources

- J. L. Kelly Jr., "A New Interpretation of Information Rate", Bell System Technical Journal 35(4), 1956: https://doi.org/10.1002/j.1538-7305.1956.tb03809.x
- Edward O. Thorp, "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market", in Handbook of Asset and Liability Management, 2006: https://www.eecs.harvard.edu/cs286r/courses/fall12/papers/Thorpe_KellyCriterion2007.pdf
- U.S. Securities and Exchange Commission, Investor.gov, "Stop-Loss Order": https://www.investor.gov/introduction-investing/investing-basics/glossary/stop-loss-order
- Hendrik Bessembinder, "Do Stocks Outperform Treasury Bills?", Journal of Financial Economics 129(3), 2018: https://doi.org/10.1016/j.jfineco.2018.06.004

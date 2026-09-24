---
{
  "title": "Market Makers: How They Quote, Inventory Risk, and Why Spreads Widen on News",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In the Glosten-Milgrom example with a 20% chance the next trader is informed and values of 186 or 188, the dealer's ask is:", "opts": ["187.00", "187.10", "187.20", "187.40"], "correct": 2, "explain": "P(high | buy) = 0.6, so ask = 0.6 × 188 + 0.4 × 186 = 187.20. The bid is symmetric at 186.80."},
    {"q": "Raising the informed share from 20% to 50% changes the spread from $0.40 to:", "opts": ["$0.50", "$0.80", "$1.00", "$2.00"], "correct": 2, "explain": "P(high | buy) becomes 0.75, ask = 187.50, bid = 186.50, spread $1.00, two and a half times wider with no change in the possible values."},
    {"q": "A market maker is long 40,000 shares more than it wants to be. According to inventory models, it will:", "opts": ["Raise both bid and ask", "Lower both bid and ask to attract buyers and discourage sellers", "Stop quoting", "Widen only the ask"], "correct": 1, "explain": "Ho and Stoll: the dealer shifts its quotes against its inventory so that the flow it attracts unwinds the position."},
    {"q": "Stoll's 1989 decomposition of the Nasdaq spread attributed roughly what share to adverse selection?", "opts": ["About 5%", "About 43%", "About 75%", "100%"], "correct": 1, "explain": "Stoll estimated adverse selection at about 43%, order processing about 47% and inventory about 10%."},
    {"q": "Why does a market maker widen its spread in the seconds before a scheduled economic release?", "opts": ["To earn more commission", "Because the probability that the next order is informed jumps, and the model spread rises with it", "Because exchanges require it", "Because volume falls"], "correct": 1, "explain": "The dealer cannot tell who knows what, so it prices the higher likelihood that the next trade is against it. Same values, wider spread."}
  ],
  "task": "At the next scheduled 08:30 Eastern data release, watch the pre-market quote on SPY from 08:29:30 to 08:30:30 and record the widest spread you see and how long it takes to return to normal."
}
---

## The dealer's problem

A market maker posts a bid and an ask at the same time and promises to trade at both. It earns the spread when a buyer and a seller arrive in sequence; it loses when the next trader knows something it does not, or when it accumulates a position it did not want. Everything about how spreads behave, including why they widen on news, why they are narrower in liquid names and why a wholesaler can quote tighter than an exchange, follows from two models that are old, short and worth understanding properly.

## Adverse selection: Glosten and Milgrom

Glosten and Milgrom (1985) considered a dealer facing a stream of traders, some of whom know the stock's true value and some of whom trade for reasons unrelated to it. The dealer cannot tell them apart. So the dealer sets the ask at the expected value of the stock conditional on the next order being a buy, and the bid at the expected value conditional on the next order being a sell. A buy is weak evidence the stock is worth more (an informed trader would only buy if it were), so the ask sits above the unconditional value; a sell is weak evidence it is worth less, so the bid sits below. The spread is the price of the dealer's ignorance, and it widens with the fraction of informed traders and with the size of what they might know.

That is the entire theory of why spreads widen on news, and it has nothing to do with volatility as such. In the seconds before an economic release the range of possible values widens and the probability that the next order is informed rises, so the model spread jumps. After the number is out and prices have adjusted, the informed share falls back and so does the spread. The worked example puts numbers on it.

## Inventory: Ho and Stoll

The second model is about position, not information. Ho and Stoll (1981) showed that a risk-averse dealer holding more stock than it wants will lower both its bid and its ask: the lower ask attracts buyers who take stock off its hands, and the lower bid discourages sellers from adding to the pile. A dealer that is short does the opposite. The midpoint of a dealer's quote therefore drifts with its inventory, and a large one-sided order flow moves prices not because anyone learned anything but because the dealers absorbing it are pricing their own risk. This is the mechanical link between order flow and price that the delta tools in lesson 7 try to exploit, and it is real: inventory effects are measurable in dealer data, though they decay within hours as inventories are worked off.

## What the components look like in data

Stoll (1989) decomposed the quoted spread on Nasdaq stocks into three parts using the way trade prices bounce between bid and ask. His estimates: adverse selection about 43%, order processing (the dealer's fixed costs and profit) about 47%, and inventory about 10%. The proportions vary by stock and by era, and the order-processing share has collapsed in penny-tick, electronic markets, which is part of why spreads on large caps fell from eighths of a dollar to a cent. But the structure holds: a spread is a fee for handling plus an insurance premium against informed traders plus a small charge for warehousing risk.

The SEC's Rule 605 reports, whose 2024 amendments (Release 34-99679) extended coverage to larger brokers and finer time buckets, measure effective spreads for every reporting market center by order size and type. The effective spread is twice the difference between your fill and the midpoint at the time of order receipt, exactly the figure computed for the 4,000-share order in lesson 1. Read a 605 report for your broker's main wholesaler and you will find effective spreads in large caps of a fraction of a cent, which is the empirical face of segmented, low-adverse-selection flow from lesson 4.

## Modern market making

Today's market makers are the same firms that appeared as wholesalers in lesson 4, plus exchange-focused proprietary firms. They quote on every exchange at once, hedge across correlated instruments (an SPY quote is hedged in ES futures within microseconds), and manage inventory across hundreds of names. Their quotes are small at the inside (recall the thin top of the book in lesson 1) because the first shares at a price bear the most adverse selection, and they cancel and replace quotes thousands of times a second as the hedging instruments move. When you see the best bid and offer flicker without any trade, you are watching this: dealers repricing to the futures.

They are also the reason spreads gap on real news. A dealer that cannot hedge because the futures are also moving, and cannot tell whether the next order is from someone who already read the headline, does the only sensible thing and widens. Retail market orders in the first seconds after a surprise fill into that widened quote, which is why lesson 12's rule set says not to send them.

## Worked example

Use Glosten-Milgrom with the smallest possible setup. A stock will be worth either V_H = 188 or V_L = 186 with equal probability, so its unconditional value is 187. A fraction π of arriving traders are informed and trade in the direction of the true value; the rest trade at random, buying or selling with equal probability.

Case 1: normal conditions, π = 0.20.

- Probability the next order is a buy if the true value is 188: informed always buy, uninformed buy half the time. P(buy | H) = 0.20 + 0.80 × 0.5 = 0.60.
- Probability of a buy if the true value is 186: P(buy | L) = 0 + 0.80 × 0.5 = 0.40.
- Posterior that the value is 188 given a buy, by Bayes with equal priors: P(H | buy) = 0.60 / (0.60 + 0.40) = 0.60.
- Ask = E[V | buy] = 0.60 × 188 + 0.40 × 186 = 112.8 + 74.4 = 187.20.
- By symmetry the bid = E[V | sell] = 0.40 × 188 + 0.60 × 186 = 75.2 + 111.6 = 186.80.
- Spread = 187.20 − 186.80 = $0.40, or 0.40 / 187 = 21 basis points.

Case 2: seconds before a scheduled release, π = 0.50.

- P(buy | H) = 0.50 + 0.50 × 0.5 = 0.75. P(buy | L) = 0.25.
- P(H | buy) = 0.75 / (0.75 + 0.25) = 0.75.
- Ask = 0.75 × 188 + 0.25 × 186 = 141 + 46.5 = 187.50. Bid = 0.25 × 188 + 0.75 × 186 = 47 + 139.5 = 186.50.
- Spread = $1.00, or 53 basis points. Ratio to case 1: 1.00 / 0.40 = 2.5×.

Case 3: same π = 0.20 but the possible values widen to 185 and 189 (a bigger number is expected).

- Ask = 0.60 × 189 + 0.40 × 185 = 113.4 + 74 = 187.40. Bid = 186.60. Spread = $0.80, twice case 1.

Now the inventory adjustment. Suppose the dealer in case 1 is long 40,000 shares it wants to shed, and its risk rule shifts its midpoint by $0.05 per 40,000 shares of unwanted inventory. Quotes become bid 186.75, ask 187.15: the spread is still $0.40, but both sides moved down five cents. A trader watching only the tape would see the price "fall" on no news; what actually happened is one dealer paying to get flat. Multiply by every dealer absorbing the same one-sided flow, and you have the mechanism by which imbalance moves price on a scale of minutes to hours.

## Table

| Spread component | What it pays for | Stoll (1989) share of Nasdaq spread | Behaviour on news |
|---|---|---|---|
| Adverse selection | Expected loss to traders who know the value | ~43% | Rises sharply as the informed share and value range grow |
| Order processing | Fixed costs, technology, dealer margin | ~47% | Roughly flat; has collapsed in penny-tick electronic markets |
| Inventory | Compensation for holding an unwanted position | ~10% | Rises when hedges (futures) are also moving; shifts the midpoint, not just the width |

The table is a map, not a measurement of any current stock; use a Rule 605 report for that.

## Sources

- Lawrence Glosten and Paul Milgrom, "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders", Journal of Financial Economics 14(1), 1985: https://doi.org/10.1016/0304-405X(85)90044-3
- Thomas Ho and Hans Stoll, "Optimal Dealer Pricing under Transactions and Return Uncertainty", Journal of Financial Economics 9(1), 1981: https://doi.org/10.1016/0304-405X(81)90020-9
- Hans Stoll, "Inferring the Components of the Bid-Ask Spread: Theory and Empirical Tests", Journal of Finance 44(1), 1989: https://doi.org/10.1111/j.1540-6261.1989.tb02407.x
- SEC, "Disclosure of Order Execution Information", final rule, Release No. 34-99679 (March 6, 2024): https://www.sec.gov/files/rules/final/2024/34-99679.pdf

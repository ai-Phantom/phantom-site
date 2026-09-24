---
{
  "title": "The Limit Order Book: Bids, Asks, Depth and Queue Priority",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "In the representative book, the best bid is 187.10 for 1,200 shares and the best ask is 187.12 for 900 shares. What is the quoted spread and the midpoint?", "opts": ["$0.01 and 187.11", "$0.02 and 187.11", "$0.02 and 187.12", "$0.01 and 187.10"], "correct": 1, "explain": "Spread = ask − bid = 187.12 − 187.10 = $0.02. Midpoint = (187.10 + 187.12) / 2 = 187.11."},
    {"q": "A 4,000-share market buy hits the representative book. Where does the last share fill?", "opts": ["187.12", "187.13", "187.14", "187.15"], "correct": 2, "explain": "900 fill at 187.12, 1,800 at 187.13 (2,700 so far), and the remaining 1,300 fill at 187.14, leaving 1,100 shares resting there."},
    {"q": "Under price-time priority, two limit buys at 187.10 rest in the book. Which fills first when a sell arrives?", "opts": ["The larger one", "The one from the exchange member with the most volume", "The one entered first", "They fill pro rata"], "correct": 2, "explain": "At the same price, the earlier order has time priority. Size and identity do not matter in a price-time book; pro rata is a different rule used on some futures contracts."},
    {"q": "After the 4,000-share market buy, what happens to the quoted spread?", "opts": ["It stays at $0.02", "It widens to $0.04 until someone posts a new ask", "It narrows to $0.01", "It becomes zero"], "correct": 1, "explain": "The 187.12 and 187.13 asks are gone. Best ask is now 187.14 against a 187.10 bid, a $0.04 spread, until a new order replenishes the inside."},
    {"q": "Why is displayed depth an unreliable guide to how much you can actually trade at a price?", "opts": ["Exchanges round sizes down", "Resting orders can be cancelled in microseconds, and hidden or reserve orders are not shown", "Depth is only published once per second", "Odd lots are illegal"], "correct": 1, "explain": "The book is a snapshot of intentions that can be withdrawn faster than you can act, and hidden, reserve and off-exchange interest never appears in it."}
  ],
  "task": "Open your broker's Level 2 window on a liquid stock for five minutes and write down how many times the best bid or ask size changed without a single trade printing."
}
---

## What the book is

Every price you see quoted for a stock is the top of a queue. Behind the best bid and the best ask sit thousands of resting limit orders at worse prices, and the whole structure, sorted by price and then by arrival time, is the limit order book. Modern US exchanges are almost all pure electronic books: no specialist decides who trades, a matching engine applies fixed rules, and the rules are public in each exchange's rulebook (Nasdaq Rule 4757 and NYSE Rule 7.36 are the two you will be quoted most often).

Two kinds of order live in this world. A limit order says "buy up to this price" or "sell at this price or better" and rests in the book if it cannot fill immediately. It provides liquidity: it is the thing other people trade against. A market order says "fill me now at whatever is available." It consumes liquidity, walking through resting orders from the best price outward until it is done. Everything else in this course, from the closing auction to spoofing cases to cumulative delta, is a story about who is providing, who is consuming, and what that does to price.

## Bids, asks, depth

The bid side lists prices buyers are willing to pay, highest first. The ask (or offer) side lists prices sellers will accept, lowest first. The best bid and best ask together are the inside market, and their difference is the quoted spread. Below is the representative book used throughout this lesson. It is not a real snapshot of any stock; it is built to be typical of a $187 large-cap around mid-morning, with a two-cent spread and depth that thickens away from the inside.

Bids: 187.10 × 1,200; 187.09 × 2,600; 187.08 × 3,100; 187.07 × 4,500; 187.06 × 6,000.
Asks: 187.12 × 900; 187.13 × 1,800; 187.14 × 2,400; 187.15 × 5,200; 187.16 × 7,000.

Total displayed bids over five levels: 17,400 shares. Total displayed asks: 17,300 shares. The book is roughly balanced in size, but notice the shape: the inside is thin (1,200 and 900) and the fourth and fifth levels are fat. That shape is common. Participants who post at the inside are exposed to being picked off when news arrives, so they post small; participants deeper in the book are less exposed and post larger, and many deeper orders are algorithmic "reserve" orders that show only a slice of their true size.

## Queue priority

When a marketable order arrives, the engine matches it against the best price first. Within a price level, the order that arrived first fills first. This is price-time priority, and it is the rule on every major US equity exchange. It has three practical consequences.

First, being early at a price matters as much as the price itself. If 20,000 shares are already bid at 187.10 and you join at the back, a 5,000-share sell order fills the first 5,000 in the queue and you get nothing. Your fill probability is a function of your position in the queue, not just your price.

Second, cancelling and re-entering sends you to the back. Traders who "refresh" an order to change its size lose their place; on Nasdaq a size increase is treated as a new order, while a size decrease keeps priority.

Third, exchanges with different rules exist. Some futures contracts use pro rata allocation, where a large order at the inside gets a proportional share of each incoming fill regardless of time. IEX and a few others add a speed bump. The default for US stocks, however, is price-time, and it rewards two things: a better price, or the same price earlier.

## What a market order does to the book

A market order is a demand for immediacy, and immediacy has a price beyond the spread. The worked example below walks a 4,000-share buy through the representative book. Read it slowly; this arithmetic is the foundation for the market-impact lesson later in the course.

Three things happen. The order fills at progressively worse prices, so the average fill is worse than the quoted ask. The inside of the book is consumed, so the spread widens until liquidity providers replace it. And the last fill sets a new "last price" that everyone else sees on the tape, which is how a single impatient order moves the printed price even though nobody's opinion of the stock changed.

Institutions know this, which is why the largest orders you will never see are sliced into hundreds of small pieces spread over hours (lesson 10). Retail traders often do not know it, which is why a market order for a few thousand shares in a thin name at 09:31 can cost more than the commission ever did.

## Worked example

A 4,000-share market buy arrives against the representative book. The engine fills from the best ask outward.

- Level 1: 900 shares at 187.12. Cost = 900 × 187.12 = $168,408.00. Remaining 3,100.
- Level 2: 1,800 shares at 187.13. Cost = 1,800 × 187.13 = $336,834.00. Remaining 1,300.
- Level 3: 1,300 of the 2,400 shares at 187.14. Cost = 1,300 × 187.14 = $243,282.00. Remaining 0.

Total cost = 168,408.00 + 336,834.00 + 243,282.00 = $748,524.00.

Average fill price = 748,524.00 / 4,000 = $187.131.

Compare that to the three reference prices a trader might have had in mind:

- Versus the quoted ask (187.12): 187.131 − 187.12 = $0.011 per share, or 4,000 × 0.011 = $44.00 of price impact beyond the spread.
- Versus the midpoint (187.11): 187.131 − 187.11 = $0.021 per share, or $84.00. This is the effective half-spread the SEC's Rule 605 reports measure.
- In basis points of the midpoint: 0.021 / 187.11 = 0.000112 = 1.12 basis points.

The book afterwards: bids unchanged; asks are now 187.14 × 1,100; 187.15 × 5,200; 187.16 × 7,000. The quoted spread has widened from 187.12 − 187.10 = $0.02 to 187.14 − 187.10 = $0.04, and the last print on the tape reads 187.14, two cents above the previous last. Nothing about the company changed. One order did that.

Now reverse it: a 4,000-share market sell. It takes 1,200 at 187.10, 2,600 at 187.09, and 200 at 187.08. Cost basis of the fills = 1,200 × 187.10 + 2,600 × 187.09 + 200 × 187.08 = 224,520 + 486,434 + 37,416 = $748,370. Average = 748,370 / 4,000 = $187.0925, or $0.0175 below the mid. The sell side of this book is slightly deeper at the inside, so the same size costs a little less. Depth is not symmetric, and neither is impact.

## Chart

![Representative order book: resting shares at each of five bid levels (green, 187.06 to 187.10) and five ask levels (red, 187.12 to 187.16). Inside sizes are 1,200 and 900; depth thickens outward to 6,000 and 7,000. Representative data built for this lesson, not a real snapshot.](figures/order-book-depth-ladder.svg)

The ladder is the shape to remember: thin inside, thick outside. A market order's cost is set by how quickly the ladder fills in behind the inside, not by the inside quote alone.

## What the book does not show

Displayed depth is a snapshot of intentions, and intentions can be withdrawn. A resting order can be cancelled in a few microseconds; on the Nasdaq TotalView-ITCH feed, order additions and deletions are the majority of all messages, and only a small fraction of messages are executions. So when you see 6,000 shares bid at 187.06, you are seeing what someone is willing to do right now, with no commitment to be there when your order arrives.

Three other things are invisible. Hidden and reserve orders rest on exchange books without being displayed, and midpoint-pegged orders exist only in the engine's memory. Off-exchange liquidity, including the wholesalers who fill most retail orders and the dark pools where institutions cross blocks, never touches the displayed book at all; in 2025 that was slightly more than half of all US share volume (lesson 4). And auction interest, the market-on-close orders queued for 16:00, sits in a separate book until the imbalance feeds begin publishing it (lesson 2).

The honest reading of a book is therefore conditional: "if nothing changes, a 4,000-share buy costs 1.12 basis points." Things change. Later lessons measure how much.

## Sources

- Nasdaq Stock Market Rulebook, Equity 4, Rule 4757 (Book Processing, price-time priority): https://listingcenter.nasdaq.com/rulebook/nasdaq/rules/nasdaq-equity-4
- NYSE Rules, Rule 7.36 (Order Ranking and Display): https://nyseguide.srorules.com/rules
- Nasdaq TotalView-ITCH 5.0 specification (message types for adds, cancels and executions): https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHspecification.pdf
- Lawrence Glosten, "Is the Electronic Open Limit Order Book Inevitable?", Journal of Finance 49(4), 1994: https://doi.org/10.1111/j.1540-6261.1994.tb02450.x

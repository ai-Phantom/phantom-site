---
{
  "title": "Order Types, Fills, Slippage and the Depth of Book in ES",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "ES is 7,772.25 bid / 7,772.50 offer. You send a market buy for one contract. Ignoring commission, what did crossing the spread cost relative to the mid?", "opts": ["$0", "$6.25", "$12.50", "$25.00"], "correct": 1, "explain": "You pay the offer, one tick ($12.50) above the bid and half a tick ($6.25) above the 7,772.375 mid. A round trip at market costs one full tick, $12.50, before commission."},
    {"q": "A sell stop at 6,560 is resting overnight. The next session opens at 6,510 after a gap. Where does the stop fill?", "opts": ["6,560, the stop price", "6,559.75, one tick below", "At or near 6,510, the first trade after the gap", "It is cancelled"], "correct": 2, "explain": "A stop becomes a market order when the stop price is touched or passed; the first trade after the gap is around 6,510, so the fill is about 50 points ($2,500) worse than the stop price."},
    {"q": "What is the main danger of a stop-limit order used as a protective stop?", "opts": ["It fills at a worse price than a stop-market", "It may not fill at all if price moves through the limit, leaving you in the position", "It is rejected by Globex", "It costs a higher commission"], "correct": 1, "explain": "A stop-limit converts to a limit order when triggered. If the market gaps past the limit price, the order rests unfilled and the position is unprotected."},
    {"q": "How does CME Globex prioritise resting limit orders at the same price in ES?", "opts": ["Largest order first", "Pro-rata by size", "First in, first out by time", "Randomly"], "correct": 2, "explain": "ES uses FIFO (price-time priority). The order that arrived first at a price fills first; joining a queue late means many contracts must trade before yours."},
    {"q": "Which order type lets you enter a bracket with a stop and a target where filling one cancels the other?", "opts": ["Fill-or-kill", "OCO (one-cancels-other)", "Market-on-close", "Good-till-date"], "correct": 1, "explain": "An OCO pair links a stop and a limit target so the survivor is cancelled when one fills. Most platforms build a bracket order from an entry plus an OCO exit pair."}
  ],
  "task": "Place one MES limit order two ticks below the market in your simulator, note how many contracts are ahead of you in the queue on the DOM, and watch what happens to that number over five minutes."
}
---

## The book you are trading into

CME Globex is a central limit order book. Every resting limit order sits at a price level, and the book shows, for each level, the total contracts bid or offered. Your platform's depth-of-market display (the DOM, or ladder) typically shows ten levels each side. During regular hours the ES book is thick: the top level often holds hundreds of contracts and the ten visible levels on each side thousands. Overnight the same display shows tens of contracts per level and gaps where no one is resting at all.

Matching in ES is **FIFO**, first in, first out: at a given price, the order that arrived first fills first. If 800 contracts are bid at 7,772.25 and you join the bid, 800 contracts must trade at that price before yours does. Joining a queue is free but slow; crossing the spread is fast but costs a tick. Every order type below is a choice about where you sit on that trade-off.

## The order types

**Market.** Buy at the best offer, sell at the best bid, right now. Guaranteed to fill; not guaranteed a price. In a thick book at 10:00 a.m. a one-lot fills at the touch. In a thin book at 2:00 a.m. a five-lot may walk through two or three levels.

**Limit.** Buy at your price or lower, sell at your price or higher. Guaranteed a price; not guaranteed to fill. A limit at the touch (buying at the bid) joins the queue; a limit through the touch (buying at the offer) behaves like a market order capped at that price, which is the safest way to take liquidity in a thin book.

**Stop (stop-market).** Dormant until the market trades at or through the stop price, then becomes a market order. This is the standard protective stop. Its weakness is the gap: when the trigger is passed by a jump rather than a tick, the fill is wherever the first trade after the jump is, and that can be far from the stop.

**Stop-limit.** Dormant until triggered, then becomes a limit order at the limit price. It protects you from a bad fill and does not protect you from a bad market: if price jumps through the limit the order rests unfilled and you are still in the position. Use it for entries, never as your only exit.

**MIT (market-if-touched).** The mirror of a stop: dormant until price touches it, then a market order, used for profit targets when you want certainty of exit over an exact price.

**OCO and bracket.** One-cancels-other links two exit orders, a stop and a limit target, so that when one fills the other is cancelled. A bracket order is an entry with an OCO pair attached, submitted together, so you are never in a position without a resting stop. Most retail platforms build this natively; on Globex the legs are ordinary orders that the platform or the broker's server manages.

**Time in force.** Day (cancelled at the session end, 5:00 p.m. ET for ES, which is not the cash close), GTC (good till cancelled; check whether your broker honours it across the roll), GTD (good till a date), IOC (fill what you can immediately, cancel the rest), FOK (fill all immediately or cancel). A Day stop placed at 3:00 p.m. that you think protects you overnight expires at 5:00 p.m.

## Slippage, measured

Slippage is the difference between the price you meant and the price you got. It has three sources. The **spread**: a market order pays half a tick against the mid on each side, one tick per round trip, $12.50 on ES. **Depth**: an order larger than the top level walks the book; five contracts against a two-contract offer take the next level too. **Gaps**: the market jumps over your price and there is nothing to fill against in between.

The first two are functions of the clock. From Lesson 7, the 10:00 a.m. ET hour carried 16.2% of monthly ES volume and the 2:00 a.m. hour 0.8%, a 20-to-1 ratio. Depth scales similarly. The cost of a market order at 2:00 a.m. is not "a bit more"; for anything larger than a one-lot it is a different order of magnitude.

## Worked example

Two real situations from the Yahoo Finance ES=F series.

**A gap through a stop.** On Friday 2026-03-20 the continuous series closed at 6,594.63 (an expiry-day vendor artefact; the nearest real print is 6,594.50). On Monday 2026-03-23 the session opened at 6,510.00, a gap of -84.63 points, -1.28%, the largest opening gap of the year. Suppose a trader was long one ES with a sell stop at 6,560.00, a 34.5-point stop, $1,725 of intended risk.

The stop was triggered by the opening print at 6,510.00, which was already 50.00 points through the stop price. The stop became a market order at that moment and filled near 6,510.00 (assume 6,509.75, one tick of spread). Realised loss: (6,594.50 - 6,509.75) x $50 = 84.75 x $50 = $4,237.50, against the $1,725 the stop was meant to cap. Slippage on the stop: 50.25 points, $2,512.50, 2.46 times the intended risk. Had the order been a stop-limit with a limit at 6,559.00, it would not have filled at all, and by 10:00 a.m. the market had traded as low as 6,483.50, another $1,312.50 lower.

**A market order at the open versus overnight.** On 2026-09-22 the 9:30 a.m. ET five-minute bar traded 31,930 contracts and the 4:30 p.m. bar traded 982. A market buy of five ES at 9:30, with a typical one-tick spread and several hundred contracts on the offer, costs about half a tick against mid per contract: 5 x $6.25 = $31.25. The same five-lot into a book showing, say, two contracts at the offer, three at the next level and none until two ticks further would fill 2 at the touch, 3 one tick higher, or worse, averaging a tick or more of extra cost: roughly 5 x $12.50 to 5 x $25.00 = $62.50 to $125.00 on top of the spread. Two to four times the daytime cost, for the same five contracts, in the same product.

Commission arithmetic to complete the picture. Assume $2.50 per side per contract (use your broker's figure). A one-ES round trip: $5.00 commission plus one tick of spread ($12.50) = $17.50 fixed cost, which is 1.4 ticks. A one-MES round trip: $5.00 plus one tick of $1.25 = $6.25, which is 5 ticks of MES. Per dollar of exposure the micro costs about three and a half times more to trade, which is the price of its granularity.

## Table

| Order type | Fill certainty | Price certainty | Typical use in ES | Failure mode |
|---|---|---|---|---|
| Market | Yes | No | Small lots during RTH | Walks the book overnight |
| Limit (at touch) | No | Yes | Patient entries, targets | Never fills; FIFO queue |
| Limit (through touch) | Usually | Capped | Taking liquidity in thin books | Partial fill if depth is short |
| Stop (market) | Yes, once triggered | No | Protective exit | Gap slippage (50 pts on 2026-03-23) |
| Stop-limit | No | Yes | Breakout entries | Unfilled through a gap; no protection |
| MIT | Yes, once touched | No | Profit target with certainty | Fills below target on a spike |
| OCO / bracket | Per leg | Per leg | Every entry, with stop attached | Platform-held legs die if the platform disconnects; check whether your broker holds them server-side |

Time-in-force reminder: a Day order in ES expires at 5:00 p.m. ET, not 4:00 p.m.

## Sources

- CME Group, E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- CME Group, CME Globex matching algorithms and order types (Client Systems Wiki) — https://www.cmegroup.com/confluence/display/EPICSANDBOX/Matching+Algorithms
- CFTC, "Basics of Futures Trading" — https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index.htm
